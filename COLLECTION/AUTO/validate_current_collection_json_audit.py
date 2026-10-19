#!/usr/bin/env python3
"""Validate the persisted current-Collection JSON audit report after it is committed."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "COLLECTION" / "VERIFICATION" / "CURRENT_MAIN_JSON_AUDIT.json"

def main():
    if not REPORT.is_file():
        raise SystemExit("current JSON audit report is missing")
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    files = data.get("files")
    if data.get("schema_version") != "collection-current-json-audit/v1" or not isinstance(files, list):
        raise SystemExit("current JSON audit report schema is invalid")
    if data.get("json_file_count") != len(files):
        raise SystemExit("current JSON audit file count does not match the file rows")
    if data.get("total_bytes") != sum(row.get("bytes", 0) for row in files):
        raise SystemExit("current JSON audit byte total does not match the file rows")
    for row in files:
        if not isinstance(row.get("path"), str) or not isinstance(row.get("bytes"), int):
            raise SystemExit("current JSON audit row lacks path/byte metadata")
        if not re.fullmatch(r"[0-9a-f]{64}", str(row.get("sha256", ""))):
            raise SystemExit(f"invalid SHA-256 for {row.get('path')}")
        if row.get("json_parse") not in {"PASS", "FAIL"}:
            raise SystemExit(f"invalid JSON parse status for {row.get('path')}")
    failures = data.get("parse_failure_count")
    if failures != sum(row.get("json_parse") == "FAIL" for row in files):
        raise SystemExit("current JSON audit parse-failure count does not match rows")
    print(json.dumps({"status": "PASS" if failures == 0 else "FAIL",
                      "json_file_count": len(files),
                      "parse_failure_count": failures,
                      "total_bytes": data["total_bytes"],
                      "report": REPORT.relative_to(ROOT).as_posix()}, sort_keys=True))
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
