#!/usr/bin/env python3
"""Read-only structural audit for Collection's large generated JSON files.

This utility never writes, compacts, repairs, or replaces Collection data. It
reports file size/hash, JSON root shape, top-level keys, and list/object counts
so large queues can be inspected without fetching their contents through APIs.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

from collection_json_io import SHARD_SCHEMA, load_collection_json

ROOT = Path(__file__).resolve().parents[2]
RECOMMENDED_BYTES = 50_000_000
BLOCK_COMMIT_BYTES = 95_000_000
DEFAULT_PATHS = (
    "COLLECTION/MASTER/READY.json",
    "COLLECTION/MASTER/PROMOTION-QUEUE.json",
    "COLLECTION/MASTER/READINESS-QUEUE.json",
    "COLLECTION/MASTER/CANONICAL-PROMOTION-PLAN.json",
    "COLLECTION/MASTER/VALUE-OPERATOR-QUEUE.json",
    "COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json",
    "COLLECTION/VERIFICATION/INSTALLED-QUEUE.json",
    "COLLECTION/MASTER/CALLABLE-REGISTRY.json",
    "COLLECTION/AUTO/EXTRACTED/MANIFEST.json",
)


def size_status(byte_count: int) -> str:
    if byte_count >= BLOCK_COMMIT_BYTES:
        return "BLOCK_HARD_LIMIT_RISK"
    if byte_count > RECOMMENDED_BYTES:
        return "OVER_RECOMMENDED_LIMIT"
    return "OK"


def audit(path: Path) -> dict:
    try:
        display_path = path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        display_path = path.name
    raw = path.read_bytes()
    try:
        payload = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        return {
            "path": display_path,
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "size_status": size_status(len(raw)),
            "status": "INVALID_JSON",
            "error": f"{type(exc).__name__}: {exc}",
        }

    if isinstance(payload, dict) and payload.get("schema_version") == SHARD_SCHEMA:
        try:
            reconstructed = load_collection_json(path)
            shards = payload.get("shards", [])
            shard_sizes = [entry.get("bytes", 0) for entry in shards if isinstance(entry, dict)]
            max_file_bytes = max([len(raw), *shard_sizes])
            result = {
                "path": display_path,
                "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "size_status": size_status(max_file_bytes),
                "status": "PASS",
                "root_type": type(reconstructed).__name__,
                "storage_format": "sharded",
                "item_count": payload.get("item_count"),
                "shard_count": len(shards),
                "total_shard_bytes": payload.get("total_shard_bytes"),
                "max_shard_bytes": max(shard_sizes, default=0),
                "max_file_bytes": max_file_bytes,
                "integrity_verified": True,
            }
            if isinstance(reconstructed, dict):
                result["top_level_keys"] = sorted(reconstructed.keys())
                for key in ("items", "decisions", "sources", "entries", "results"):
                    value = reconstructed.get(key)
                    if isinstance(value, (list, dict)):
                        result[f"{key}_count"] = len(value)
            return result
        except Exception as exc:
            return {
                "path": display_path,
                "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "size_status": size_status(len(raw)),
                "status": "INVALID_SHARDS",
                "error": f"{type(exc).__name__}: {exc}",
            }

    result = {
        "path": display_path,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_status": size_status(len(raw)),
        "status": "PASS",
        "root_type": type(payload).__name__,
    }
    if isinstance(payload, dict):
        result["top_level_keys"] = sorted(payload.keys())
        result["collections"] = {
            key: len(value)
            for key, value in payload.items()
            if isinstance(value, (list, dict))
        }
        for key in ("items", "decisions", "sources", "entries", "results"):
            if key in payload:
                value = payload[key]
                result[f"{key}_count"] = len(value) if isinstance(value, (list, dict)) else None
    elif isinstance(payload, list):
        result["record_count"] = len(payload)
    return result


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    enforce_size = "--enforce-size" in args
    path_args = [arg for arg in args if arg != "--enforce-size"]
    paths = [ROOT / arg for arg in path_args] if path_args else [ROOT / item for item in DEFAULT_PATHS]
    reports = []
    failed = False
    for path in paths:
        if not path.is_file():
            reports.append({"path": str(path), "status": "MISSING"})
            failed = True
            continue
        report = audit(path)
        reports.append(report)
        failed = failed or report["status"] != "PASS"
        if enforce_size and report.get("max_file_bytes", report.get("bytes", 0)) >= BLOCK_COMMIT_BYTES:
            failed = True
    print(json.dumps({"schema_version": "collection-readonly-json-audit/v1", "files": reports}, ensure_ascii=False, sort_keys=True))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
