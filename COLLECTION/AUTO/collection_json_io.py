"""Read/write large collection JSON objects with backward-compatible shards.

The canonical path remains a valid JSON document. Small documents stay monolithic;
large documents become a manifest whose shards are verified before reconstruction.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any, Callable

SHARD_SCHEMA = "collection-json-shards/v1"
DEFAULT_THRESHOLD_BYTES = 40_000_000
DEFAULT_MAX_SHARD_BYTES = 8 * 1024 * 1024
DEFAULT_BUCKETS = 32


def _compact(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _stable_key(item: Any) -> str:
    if isinstance(item, dict):
        for field in ("capability_key", "id", "key", "canonical_source", "source", "name"):
            value = item.get(field)
            if isinstance(value, str) and value:
                return field + ":" + value
    return "sha256:" + hashlib.sha256(_compact(item)).hexdigest()


def _estimate_bytes(payload: dict, array_key: str) -> int:
    items = payload.get(array_key)
    if not isinstance(items, list):
        raise ValueError(f"payload[{array_key!r}] must be a list")
    root = {key: value for key, value in payload.items() if key != array_key}
    return len(json.dumps(root, ensure_ascii=False, indent=2).encode("utf-8")) + 4 + sum(len(_compact(item)) + 2 for item in items)


def _atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def _read_git_file(repo_root: Path, relative_path: str, git_ref: str) -> bytes:
    proc = subprocess.run(
        ["git", "show", f"{git_ref}:{relative_path}"],
        cwd=str(repo_root),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise FileNotFoundError(f"cannot read {git_ref}:{relative_path} from git history")
    return proc.stdout


def load_collection_json(
    path: str | Path,
    *,
    git_ref: str | None = None,
    repo_root: str | Path | None = None,
    verify_hashes: bool = True,
) -> Any:
    """Load a monolithic collection JSON file or reconstruct its shard manifest.

    When git_ref is supplied, both the manifest and its shards are read from that
    exact git tree. This is required for baseline-vs-current regression checks.
    """
    source = Path(path)
    if git_ref:
        root = Path(repo_root or Path.cwd()).resolve()
        manifest_path = source if source.is_absolute() else (root / source)
        manifest_path = manifest_path.resolve()
        raw = _read_git_file(root, manifest_path.relative_to(root).as_posix(), git_ref)
    else:
        manifest_path = source
        raw = manifest_path.read_bytes()

    document = json.loads(raw)
    if not isinstance(document, dict) or document.get("schema_version") != SHARD_SCHEMA:
        return document

    array_key = document.get("array_key")
    root_fields = document.get("root_fields")
    shard_entries = document.get("shards")
    if not isinstance(array_key, str) or not array_key:
        raise ValueError(f"{manifest_path}: shard manifest has no array_key")
    if not isinstance(root_fields, dict) or array_key in root_fields:
        raise ValueError(f"{manifest_path}: malformed root_fields")
    if not isinstance(shard_entries, list):
        raise ValueError(f"{manifest_path}: malformed shards list")

    items = []
    total_bytes = 0
    for entry in shard_entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            raise ValueError(f"{manifest_path}: malformed shard entry")
        relative_shard = entry["path"]
        if git_ref:
            root = Path(repo_root or Path.cwd()).resolve()
            shard_path = (manifest_path.parent / relative_shard).resolve()
            shard_raw = _read_git_file(root, shard_path.relative_to(root).as_posix(), git_ref)
        else:
            shard_path = manifest_path.parent / relative_shard
            shard_raw = shard_path.read_bytes()
        if verify_hashes:
            actual_hash = hashlib.sha256(shard_raw).hexdigest()
            if actual_hash != entry.get("sha256"):
                raise ValueError(f"{manifest_path}: SHA-256 mismatch for {relative_shard}")
            if len(shard_raw) != entry.get("bytes"):
                raise ValueError(f"{manifest_path}: byte count mismatch for {relative_shard}")
        shard_items = json.loads(shard_raw)
        if not isinstance(shard_items, list):
            raise ValueError(f"{manifest_path}: shard {relative_shard} is not an array")
        if len(shard_items) != entry.get("item_count"):
            raise ValueError(f"{manifest_path}: item count mismatch for {relative_shard}")
        items.extend(shard_items)
        total_bytes += len(shard_raw)

    if len(items) != document.get("item_count"):
        raise ValueError(f"{manifest_path}: reconstructed item count mismatch")
    if document.get("shard_count") != len(shard_entries):
        raise ValueError(f"{manifest_path}: shard count mismatch")
    if document.get("total_shard_bytes") != total_bytes:
        raise ValueError(f"{manifest_path}: total shard byte count mismatch")

    result = dict(root_fields)
    result[array_key] = items
    return result


def write_collection_json(
    path: str | Path,
    payload: dict,
    *,
    array_key: str,
    monolithic_writer: Callable[..., None],
    threshold_bytes: int = DEFAULT_THRESHOLD_BYTES,
    max_shard_bytes: int = DEFAULT_MAX_SHARD_BYTES,
    initial_buckets: int = DEFAULT_BUCKETS,
) -> dict:
    """Write monolithic JSON below threshold, otherwise write a verified shard manifest."""
    target = Path(path)
    if not isinstance(payload, dict) or not isinstance(payload.get(array_key), list):
        raise ValueError(f"payload must contain list field {array_key!r}")
    items = payload[array_key]
    estimated = _estimate_bytes(payload, array_key)

    if estimated <= threshold_bytes:
        monolithic_writer(target, payload, compact_array_keys={array_key})
        _remove_stale_shard_dirs(target, keep=None)
        return {"format": "monolithic", "items": len(items), "estimated_bytes": estimated}

    bucket_count = max(1, initial_buckets)
    while True:
        buckets = [[] for _ in range(bucket_count)]
        for item in items:
            identity = _stable_key(item)
            slot = int(hashlib.sha256(identity.encode("utf-8")).hexdigest()[:8], 16) % bucket_count
            buckets[slot].append(item)
        for bucket in buckets:
            bucket.sort(key=lambda item: (_stable_key(item), _compact(item)))
        serialized = [
            b"[\n" + b",\n".join(_compact(item) for item in bucket) + b"\n]\n"
            for bucket in buckets if bucket
        ]
        if all(len(raw) <= max_shard_bytes for raw in serialized):
            break
        bucket_count *= 2
        if bucket_count > 2048:
            raise ValueError("cannot partition collection JSON below max_shard_bytes")

    shard_digest = hashlib.sha256()
    for raw in serialized:
        shard_digest.update(hashlib.sha256(raw).digest())
    shard_digest.update(_compact({key: value for key, value in payload.items() if key != array_key}))
    shard_digest.update(array_key.encode("utf-8"))
    shard_dir_name = f"{target.name}.parts-{shard_digest.hexdigest()[:12]}"
    final_dir = target.parent / shard_dir_name
    temporary_dir = target.parent / (shard_dir_name + ".tmp")
    if temporary_dir.exists():
        shutil.rmtree(temporary_dir)
    temporary_dir.mkdir(parents=True, exist_ok=True)

    shard_entries = []
    raw_index = 0
    for bucket_index, bucket in enumerate(buckets):
        if not bucket:
            continue
        raw = b"[\n" + b",\n".join(_compact(item) for item in bucket) + b"\n]\n"
        filename = f"part-{bucket_index:04d}.json"
        (temporary_dir / filename).write_bytes(raw)
        shard_entries.append({
            "path": f"{shard_dir_name}/{filename}",
            "item_count": len(bucket),
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
        })
        raw_index += 1

    if final_dir.exists():
        shutil.rmtree(temporary_dir)
    else:
        os.replace(temporary_dir, final_dir)

    root_fields = {key: value for key, value in payload.items() if key != array_key}
    total_shard_bytes = sum(entry["bytes"] for entry in shard_entries)
    manifest = {
        "schema_version": SHARD_SCHEMA,
        "source_schema_version": root_fields.get("schema_version"),
        "array_key": array_key,
        "root_fields": root_fields,
        "item_count": len(items),
        "shard_count": len(shard_entries),
        "total_shard_bytes": total_shard_bytes,
        "estimated_monolithic_bytes": estimated,
        "shards": shard_entries,
    }
    _atomic_json(target, manifest)
    _remove_stale_shard_dirs(target, keep=shard_dir_name)
    return {
        "format": "sharded",
        "items": len(items),
        "shards": len(shard_entries),
        "estimated_bytes": estimated,
        "shard_bytes": total_shard_bytes,
        "manifest": str(target),
    }


def _remove_stale_shard_dirs(path: Path, keep: str | None) -> None:
    prefix = path.name + ".parts-"
    for candidate in path.parent.glob(prefix + "*"):
        if candidate.is_dir() and candidate.name != keep and not candidate.name.endswith(".tmp"):
            shutil.rmtree(candidate)
