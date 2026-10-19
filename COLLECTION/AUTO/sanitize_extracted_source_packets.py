#!/usr/bin/env python3
"""Sanitize secret-bearing content from derived Collection packets without deleting provenance."""
import datetime
import hashlib
import json
import os
from pathlib import Path

from source_content_safety import sanitize_document

ROOT = Path("COLLECTION")
REPORT = ROOT / "VERIFICATION" / "SOURCE_CONTENT_REDACTION_REPORT.json"
EXCLUDED_PARTS = {"INSTALLED"}
EXCLUDED_FILES = {REPORT.as_posix()}


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)


def main() -> int:
    scanned = 0
    changed = []
    redaction_count = 0
    failures = []

    for path in sorted(ROOT.rglob("*.json")):
        rel = path.as_posix()
        if rel in EXCLUDED_FILES:
            continue
        try:
            relative = path.relative_to(ROOT)
        except ValueError:
            continue
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        try:
            raw = path.read_bytes()
            document = json.loads(raw.decode("utf-8-sig"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            failures.append({"path": rel, "error": f"{type(exc).__name__}: {exc}"[:200]})
            continue

        scanned += 1
        original_hash = hashlib.sha256(raw).hexdigest()
        count = sanitize_document(document)
        if not count:
            continue

        serialized = json.dumps(document, ensure_ascii=False, indent=2) + "\n"
        encoded = serialized.encode("utf-8")
        atomic_write(path, serialized)
        redaction_count += count
        changed.append({
            "path": rel,
            "original_file_sha256": original_hash,
            "sanitized_file_sha256": hashlib.sha256(encoded).hexdigest(),
            "content_fields_redacted": count,
            "source_contents_removed": True,
        })

    report = {
        "schema_version": "collection-source-content-redaction/v1",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "policy": {
            "preserve_source_identity_and_hashes": True,
            "redact_sensitive_paths_and_high_confidence_secret_literals": True,
            "preserve_raw_installed_third_party_trees": True,
            "never_store_secret_values_in_report": True,
        },
        "json_files_scanned": scanned,
        "json_files_changed": len(changed),
        "content_fields_redacted": redaction_count,
        "parse_or_read_failures": failures,
        "changed_files": changed,
    }
    if changed or failures or not REPORT.exists():
        atomic_write(REPORT, json.dumps(report, ensure_ascii=False, indent=2) + "\n")

    print(json.dumps({
        "status": "PASS" if not failures else "WARN",
        "json_files_scanned": scanned,
        "json_files_changed": len(changed),
        "content_fields_redacted": redaction_count,
        "parse_or_read_failures": len(failures),
        "report": REPORT.as_posix(),
    }, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
