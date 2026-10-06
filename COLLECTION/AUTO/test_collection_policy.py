"""Deterministic Collection promotion-policy consistency checks."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
PROMOTION = ROOT / "COLLECTION/MASTER/PROMOTION-QUEUE.json"
RESTRICTED = ROOT / "COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json"
GATE = ROOT / "COLLECTION/MASTER/PROMOTION-GATE.md"
REVIEW = {"REVIEW_NEW_OR_UPGRADE", "REVIEW_MERGE_OR_UPGRADE"}
LEGACY = {"RESTRICTED", "NEW_OR_UPGRADE_REVIEW", "MERGE_OR_UPGRADE_REVIEW"}

def actions(doc):
    return {item.get("action") for item in doc.get("items", []) if item.get("action")}

def main():
    promotion = json.loads(PROMOTION.read_text())
    restricted = json.loads(RESTRICTED.read_text())
    pa, qa = actions(promotion), actions(restricted)
    assert pa <= REVIEW, f"unexpected promotion actions: {sorted(pa - REVIEW)}"
    assert qa <= {"QUARANTINE"}, f"unexpected restricted actions: {sorted(qa - {'QUARANTINE'})}"
    assert not (pa | qa) & LEGACY, "legacy policy state detected"
    gate = GATE.read_text()
    assert "REVIEW_NEW_OR_UPGRADE" in gate
    assert "REVIEW_MERGE_OR_UPGRADE" in gate
    print("collection promotion-policy consistency: PASS")

if __name__ == "__main__":
    main()
