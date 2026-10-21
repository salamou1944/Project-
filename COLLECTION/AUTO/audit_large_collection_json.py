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
        document = json.loads(raw)
        is_sharded = isinstance(document, dict) and document.get("schema_version") == SHARD_SCHEMA
        payload = load_collection_json(path) if is_sharded else document
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError, OSError) as exc:
        return {
            "path": display_path,
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "size_status": size_status(len(raw)),
            "status": "INVALID_JSON_OR_SHARD",
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
    if is_sharded:
        logical_bytes = int(document.get("estimated_monolithic_bytes", document.get("total_shard_bytes", 0)))
        result.update({
            "format": "sharded",
            "shard_count": document.get("shard_count"),
            "shard_bytes": document.get("total_shard_bytes"),
            "largest_shard_bytes": max((entry.get("bytes", 0) for entry in document.get("shards", [])), default=0),
            "logical_bytes_estimate": logical_bytes,
            "logical_size_status": size_status(logical_bytes),
            "shard_integrity": "PASS",
        })
    else:
        result["format"] = "monolithic"
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
        if enforce_size and report.get("bytes", 0) >= BLOCK_COMMIT_BYTES:
            failed = True
    print(json.dumps({"schema_version": "collection-readonly-json-audit/v1", "files": reports}, ensure_ascii=False, sort_keys=True))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
