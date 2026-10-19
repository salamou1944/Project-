#!/usr/bin/env python3
"""Read-only inventory of current Collection JSON files: bytes, SHA-256, root shape, and record counts."""
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COLLECTION = ROOT / "COLLECTION"
OUTPUT = COLLECTION / "VERIFICATION" / "CURRENT_MAIN_JSON_AUDIT.json"
COUNT_KEYS = ("repos", "items", "files", "records", "entries", "results", "owners", "accounts", "sources", "skills")

def root_shape(value):
    if isinstance(value, dict):
        counts = {k: len(v) for k, v in value.items() if isinstance(v, list)}
        record_counts = {k: len(value[k]) for k in COUNT_KEYS if isinstance(value.get(k), list)}
        return {"root_type": "object", "top_level_key_count": len(value),
                "top_level_keys": sorted(value.keys())[:100],
                "top_level_array_lengths": counts, "record_counts": record_counts}
    if isinstance(value, list):
        return {"root_type": "array", "record_count": len(value)}
    return {"root_type": type(value).__name__}

def main():
    rows = []
    errors = []
    for path in sorted(COLLECTION.rglob("*.json")):
        if path == OUTPUT or ".git" in path.parts:
            continue
        raw = path.read_bytes()
        row = {"path": path.relative_to(ROOT).as_posix(), "bytes": len(raw),
               "sha256": hashlib.sha256(raw).hexdigest()}
        try:
            value = json.loads(raw)
            row.update(root_shape(value))
            row["json_parse"] = "PASS"
        except Exception as exc:
            row.update({"json_parse": "FAIL", "parse_error": f"{type(exc).__name__}: {exc}"[:300]})
            errors.append(row["path"])
        rows.append(row)
    report = {
        "schema_version": "collection-current-json-audit/v1",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "all COLLECTION/**/*.json files in the workflow checkout plus newly generated extraction files; excludes this report to avoid self-reference",
        "json_file_count": len(rows),
        "parse_failure_count": len(errors),
        "parse_failure_paths": errors,
        "total_bytes": sum(x["bytes"] for x in rows),
        "files": rows,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS" if not errors else "FAIL", "json_file_count": len(rows),
                      "parse_failure_count": len(errors), "total_bytes": report["total_bytes"],
                      "report": OUTPUT.relative_to(ROOT).as_posix()}, sort_keys=True))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
