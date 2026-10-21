#!/usr/bin/env python3
"""Fail-closed guard for Collection generated state."""
import json
from pathlib import Path

from collection_json_io import load_collection_json

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    ROOT / "COLLECTION/MASTER/READY.json",
    ROOT / "COLLECTION/MASTER/PROMOTION-QUEUE.json",
    ROOT / "COLLECTION/MASTER/READINESS-QUEUE.json",
    ROOT / "COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json",
]
MANIFEST = ROOT / "COLLECTION/AUTO/EXTRACTED/MANIFEST.json"

# Safety floor from the verified 2026-10-15 canonical manifest (2,919 source rows).
# Lowering this requires a reviewed archival/migration plan and a preserved baseline.
MIN_EXPECTED_SOURCE_ROWS = 2500

def load_nonempty(path):
    if not path.exists():
        raise SystemExit(f"missing generated state: {path}")
    if path.stat().st_size == 0:
        raise SystemExit(f"empty generated state: {path}")
    try:
        return load_collection_json(path)
    except Exception as exc:
        raise SystemExit(f"invalid JSON state {path}: {exc}")

def validate_manifest_source_count(manifest):
    """Validate source rows against the bounded batch plus preserved prior rows."""
    sources = manifest.get("sources", [])
    if not isinstance(sources, list):
        raise SystemExit("manifest sources must be a list")
    counts = {}
    for key in ("repo_count", "gist_count", "preserved_sources_after_refresh_failure"):
        value = manifest.get(key, 0) if key != "repo_count" else manifest.get(key)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise SystemExit(f"manifest {key} must be a non-negative integer")
        counts[key] = value

    # New bounded manifests separate the full metadata inventory from source rows
    # processed in this run. Preserve compatibility with the historical full-sweep schema.
    if "processed_repo_count" in manifest:
        for key in ("processed_repo_count", "processed_gist_count", "preserved_prior_sources_not_selected"):
            value = manifest.get(key)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise SystemExit(f"manifest {key} must be a non-negative integer")
            counts[key] = value
        expected = (
            counts["processed_repo_count"] + counts["processed_gist_count"]
            + counts["preserved_sources_after_refresh_failure"]
            + counts["preserved_prior_sources_not_selected"]
        )
    else:
        expected = counts["repo_count"] + counts["gist_count"] + counts["preserved_sources_after_refresh_failure"]

    if expected != len(sources):
        raise SystemExit(
            f"manifest source rows ({len(sources)}) disagree with inventory/batch accounting "
            f"(repo_count={counts['repo_count']}, gist_count={counts['gist_count']}, "
            f"processed_repo_count={counts.get('processed_repo_count', 'legacy')}, "
            f"processed_gist_count={counts.get('processed_gist_count', 'legacy')}, "
            f"preserved_after_refresh_failure={counts['preserved_sources_after_refresh_failure']}, "
            f"preserved_not_selected={counts.get('preserved_prior_sources_not_selected', 0)}, expected={expected}); "
            "refusing to publish derived state"
        )
    return expected


def main():
    manifest = load_nonempty(MANIFEST)
    sources = manifest.get("sources", [])
    if not isinstance(sources, list):
        raise SystemExit("manifest sources must be a list")
    validate_manifest_source_count(manifest)
    if len(sources) < MIN_EXPECTED_SOURCE_ROWS:
        raise SystemExit(
            f"manifest source rows unexpectedly shrank to {len(sources)} "
            f"(safety floor: {MIN_EXPECTED_SOURCE_ROWS}); require reviewed recovery/migration"
        )
    extracted_records = [
        item for item in sources
        if isinstance(item, dict) and item.get("state") == "extracted"
    ]
    extracted = len(extracted_records)
    extracted_with_files = sum(
        1 for item in extracted_records
        if int(item.get("files_extracted", 0) or 0) > 0
    )
    loaded = {str(p): load_nonempty(p) for p in REQUIRED}
    ready = loaded[str(REQUIRED[0])]
    promotion = loaded[str(REQUIRED[1])]
    readiness = loaded[str(REQUIRED[2])]
    restricted = loaded[str(REQUIRED[3])]

    counts = ready.get("counts", {})
    decisions = ready.get("decisions")
    promotion_items = promotion.get("items")
    readiness_items = readiness.get("items")
    restricted_items = restricted.get("items")
    if extracted != extracted_with_files:
        raise SystemExit(
            f"manifest marks {extracted - extracted_with_files} source(s) extracted with zero usable files; "
            "harvester must refresh them or mark them blocked before publishing state"
        )
    if int(counts.get("files_scanned", 0)) <= 0:
        raise SystemExit("READY.json reports zero scanned extracted files")
    if int(counts.get("evidence_records", 0)) <= 0:
        raise SystemExit("READY.json reports zero evidence records")
    if int(counts.get("capability_groups", 0)) <= 0:
        raise SystemExit("READY.json reports zero capability groups")
    if not isinstance(decisions, list) or not decisions:
        raise SystemExit("READY.json decisions must be a non-empty list")
    if not isinstance(promotion_items, list):
        raise SystemExit("PROMOTION-QUEUE.json items must be a list")
    if not isinstance(readiness_items, list):
        raise SystemExit("READINESS-QUEUE.json items must be a list")
    if not isinstance(restricted_items, list):
        raise SystemExit("RESTRICTED-QUEUE.json items must be a list")
    expected_keys = {item.get("capability_key") for item in decisions}
    readiness_keys = {item.get("capability_key") for item in readiness_items}
    if expected_keys != readiness_keys:
        raise SystemExit("readiness queue does not cover exactly the generated capability decisions")
    expected_promotion = {item.get("capability_key") for item in decisions if item.get("action") != "QUARANTINE"}
    expected_restricted = {item.get("capability_key") for item in decisions if item.get("action") == "QUARANTINE"}
    actual_promotion = {item.get("capability_key") for item in promotion_items}
    actual_restricted = {item.get("capability_key") for item in restricted_items}
    if expected_promotion != actual_promotion:
        raise SystemExit("promotion queue differs from generated non-quarantined decisions")
    if expected_restricted != actual_restricted:
        raise SystemExit("restricted queue differs from generated quarantined decisions")
    if int(counts.get("capability_groups", 0)) != len(decisions):
        raise SystemExit("READY.json capability_groups count disagrees with decisions")
    if int(counts.get("review_merge_or_upgrade", 0)) + int(counts.get("review_new_or_upgrade", 0)) + int(counts.get("quarantine", 0)) != len(decisions):
        raise SystemExit("READY.json action counts disagree with decisions")

    print({
        "status": "PASS",
        "extracted_sources": extracted,
        "extracted_sources_with_files": extracted_with_files,
        "files_scanned": counts.get("files_scanned", 0),
        "capability_groups": counts.get("capability_groups", 0),
        "promotion_items": len(promotion["items"]),
        "readiness_items": len(readiness["items"]),
        "restricted_items": len(restricted["items"]),
    })

if __name__ == "__main__":
    main()
