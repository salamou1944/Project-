#!/usr/bin/env python3
"""Fail-closed guard for Collection generated state."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = [
    ROOT / "COLLECTION/MASTER/READY.json",
    ROOT / "COLLECTION/MASTER/PROMOTION-QUEUE.json",
    ROOT / "COLLECTION/MASTER/READINESS-QUEUE.json",
    ROOT / "COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json",
]
MANIFEST = ROOT / "COLLECTION/AUTO/EXTRACTED/MANIFEST.json"

def load_nonempty(path):
    if not path.exists():
        raise SystemExit(f"missing generated state: {path}")
    if path.stat().st_size == 0:
        raise SystemExit(f"empty generated state: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"invalid JSON state {path}: {exc}")

def main():
    manifest = load_nonempty(MANIFEST)
    sources = manifest.get("sources", [])
    if not isinstance(sources, list):
        raise SystemExit("manifest sources must be a list")
    extracted_records = [
        item for item in sources
        if isinstance(item, dict) and item.get("state") == "extracted"
    ]
    extracted = len(extracted_records)
    extracted_with_files = sum(
        1 for item in extracted_records
        if int(item.get("files_extracted", 0) or 0) > 0
    )
    if extracted <= 0 or extracted_with_files <= 0:
        raise SystemExit(
            f"Collection manifest has no usable extracted sources: "
            f"extracted={extracted}, extracted_with_files={extracted_with_files}"
        )

    loaded = {str(p): load_nonempty(p) for p in REQUIRED}
    ready = loaded[str(REQUIRED[0])]
    promotion = loaded[str(REQUIRED[1])]
    readiness = loaded[str(REQUIRED[2])]
    restricted = loaded[str(REQUIRED[3])]

    counts = ready.get("counts", {})
    if int(counts.get("files_scanned", 0)) <= 0:
        raise SystemExit("READY.json reports zero scanned extracted files")
    if not isinstance(ready.get("decisions"), list):
        raise SystemExit("READY.json decisions must be a list")
    if not isinstance(promotion.get("items"), list):
        raise SystemExit("PROMOTION-QUEUE.json items must be a list")
    if not isinstance(readiness.get("items"), list):
        raise SystemExit("READINESS-QUEUE.json items must be a list")
    if not isinstance(restricted.get("items"), list):
        raise SystemExit("RESTRICTED-QUEUE.json items must be a list")

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
