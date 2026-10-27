#!/usr/bin/env python3
"""Non-destructive migration test against the repository's real large state files.

The test copies each logical document into a temporary directory, writes it using
the shard writer, reloads it through the production reader, and verifies semantic
equality, manifest counts, hashes, and the physical shard-size ceiling.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from collection_json_io import DEFAULT_MAX_SHARD_BYTES, load_collection_json, write_collection_json

ROOT = Path(__file__).resolve().parents[2]
TARGETS = (
    ("COLLECTION/MASTER/READY.json", "decisions"),
    ("COLLECTION/MASTER/PROMOTION-QUEUE.json", "items"),
    ("COLLECTION/MASTER/CANONICAL-PROMOTION-PLAN.json", "items"),
)


def atomic_writer(path: Path, payload: dict, compact_array_keys=None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def main() -> None:
    reports = []
    for relative, array_key in TARGETS:
        source = ROOT / relative
        if not source.is_file() or source.stat().st_size == 0:
            raise SystemExit(f"required generated state missing or empty: {relative}")
        original = load_collection_json(source)
        if not isinstance(original, dict) or not isinstance(original.get(array_key), list):
            raise SystemExit(f"{relative} does not contain a list at {array_key!r}")
        with tempfile.TemporaryDirectory(prefix="collection-shard-migration-") as directory:
            target = Path(directory) / source.name
            result = write_collection_json(
                target,
                original,
                array_key=array_key,
                monolithic_writer=atomic_writer,
                threshold_bytes=40_000_000,
                max_shard_bytes=DEFAULT_MAX_SHARD_BYTES,
            )
            reconstructed = load_collection_json(target)
            if reconstructed != original:
                raise SystemExit(f"semantic round-trip mismatch: {relative}")
            if result.get("format") != "sharded":
                raise SystemExit(f"large state did not shard as expected: {relative}: {result}")
            manifest = json.loads(target.read_text(encoding="utf-8"))
            shards = manifest.get("shards", [])
            if manifest.get("item_count") != len(original[array_key]):
                raise SystemExit(f"manifest item count mismatch: {relative}")
            if not shards or manifest.get("shard_count") != len(shards):
                raise SystemExit(f"manifest shard count mismatch: {relative}")
            physical_sizes = [target.stat().st_size]
            for entry in shards:
                shard = target.parent / entry["path"]
                physical_sizes.append(shard.stat().st_size)
                if shard.stat().st_size > DEFAULT_MAX_SHARD_BYTES:
                    raise SystemExit(f"physical shard exceeds size ceiling: {relative}/{entry['path']}")
            reports.append({
                "path": relative,
                "logical_items": len(original[array_key]),
                "format": result["format"],
                "shards": len(shards),
                "largest_physical_file_bytes": max(physical_sizes),
                "semantic_round_trip": "PASS",
                "hash_and_count_verification": "PASS",
            })
    print(json.dumps({"status": "PASS", "files": reports}, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
