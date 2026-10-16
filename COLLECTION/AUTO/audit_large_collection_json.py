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

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PATHS = (
    "COLLECTION/MASTER/READY.json",
    "COLLECTION/MASTER/PROMOTION-QUEUE.json",
    "COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json",
    "COLLECTION/VERIFICATION/INSTALLED-QUEUE.json",
    "COLLECTION/MASTER/CALLABLE-REGISTRY.json",
    "COLLECTION/AUTO/EXTRACTED/MANIFEST.json",
)


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
            "status": "INVALID_JSON",
            "error": f"{type(exc).__name__}: {exc}",
        }

    result = {
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
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
    paths = [ROOT / arg for arg in args] if args else [ROOT / item for item in DEFAULT_PATHS]
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
    print(json.dumps({"schema_version": "collection-readonly-json-audit/v1", "files": reports}, ensure_ascii=False, sort_keys=True))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
