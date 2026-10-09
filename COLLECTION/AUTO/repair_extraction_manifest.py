#!/usr/bin/env python3
"""Reconcile manifest rows with preserved extraction artifacts before derived-state rebuild.

This is a recovery gate, not a second harvester: it never fetches sources or deletes
artifacts. Invalid rows are marked blocked and remain retryable by intelligent_extract.py.
"""
from __future__ import annotations
import datetime
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXTRACTED = ROOT / "COLLECTION/AUTO/EXTRACTED"
MANIFEST = EXTRACTED / "MANIFEST.json"


def load_json(path: Path):
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError("missing_or_empty_artifact")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    manifest = load_json(MANIFEST)
    sources = manifest.get("sources")
    if not isinstance(sources, list):
        raise SystemExit("manifest.sources must be a list")

    repaired = 0
    blocked = 0
    valid = 0
    for item in sources:
        if not isinstance(item, dict) or item.get("state") != "extracted":
            continue
        raw = item.get("path")
        reason = None
        artifact = None
        if not isinstance(raw, str) or not raw:
            reason = "missing_artifact_path"
        else:
            candidate = Path(raw)
            if not candidate.is_absolute():
                candidate = ROOT / candidate
            candidate = candidate.resolve()
            if EXTRACTED.resolve() not in candidate.parents or candidate.name == "MANIFEST.json" or candidate.suffix != ".json":
                reason = "artifact_path_outside_extracted_root"
            else:
                try:
                    artifact = load_json(candidate)
                except (OSError, ValueError, json.JSONDecodeError):
                    reason = "missing_empty_or_invalid_json_artifact"

        if reason is None and artifact is not None:
            if artifact.get("state") != "extracted":
                reason = "artifact_state_mismatch"
            elif artifact.get("canonical_source") != item.get("canonical_source"):
                reason = "artifact_source_identity_mismatch"
            elif item.get("revision_sha") and artifact.get("revision_sha") != item.get("revision_sha"):
                reason = "artifact_revision_mismatch"
            else:
                files = artifact.get("files")
                if not isinstance(files, list):
                    reason = "artifact_files_not_list"
                else:
                    usable = [
                        f for f in files
                        if isinstance(f, dict) and not f.get("error")
                        and isinstance(f.get("content"), str) and bool(f["content"])
                    ]
                    if not usable:
                        reason = "artifact_has_no_usable_files"
                    else:
                        actual = len(usable)
                        if int(item.get("files_extracted", 0) or 0) != actual:
                            item["files_extracted"] = actual
                            repaired += 1
                        item["artifact_bytes"] = candidate.stat().st_size
                        item["artifact_sha256"] = hashlib.sha256(candidate.read_bytes()).hexdigest()
                        valid += 1

        if reason:
            item["state"] = "BLOCKED_EXTERNAL_ACCESS"
            item["error"] = reason
            item["blocked_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            blocked += 1

    manifest["manifest_repair"] = {
        "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "valid_extracted_artifacts": valid,
        "blocked_invalid_artifacts": blocked,
        "corrected_file_counts": repaired,
        "policy": "preserve bytes; block invalid manifest rows; retry through normal harvester"
    }
    tmp = MANIFEST.with_name("MANIFEST.json.tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
    tmp.replace(MANIFEST)
    print(json.dumps(manifest["manifest_repair"], sort_keys=True))
    if valid == 0:
        raise SystemExit("no valid extracted artifacts remain after manifest reconciliation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
