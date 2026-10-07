"""Deterministic Collection promotion/readiness-policy consistency checks."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
PROMOTION = ROOT / "COLLECTION/MASTER/PROMOTION-QUEUE.json"
RESTRICTED = ROOT / "COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json"
READINESS = ROOT / "COLLECTION/MASTER/READINESS-QUEUE.json"
DECLARATIONS = ROOT / "COLLECTION/MASTER/READINESS-DECLARATIONS.json"
GATE = ROOT / "COLLECTION/MASTER/PROMOTION-GATE.md"
READINESS_GATE = ROOT / "COLLECTION/MASTER/READINESS-GATE.md"
REVIEW = {"REVIEW_NEW_OR_UPGRADE", "REVIEW_MERGE_OR_UPGRADE"}
LEGACY = {"RESTRICTED", "NEW_OR_UPGRADE_REVIEW", "MERGE_OR_UPGRADE_REVIEW"}
READINESS_STATES = {
    "ON_SHELF","READY_FOR_ADAPTATION","READY_ON_DEMAND","READY_TO_USE",
    "INTEGRATED","TESTED","HUMAN_READY","PRODUCTION_PROVEN","QUARANTINED"
}

def actions(doc):
    return {item.get("action") for item in doc.get("items", []) if item.get("action")}

def main():
    promotion = json.loads(PROMOTION.read_text())
    restricted = json.loads(RESTRICTED.read_text())
    readiness = json.loads(READINESS.read_text())
    declarations = json.loads(DECLARATIONS.read_text())

    pa, qa = actions(promotion), actions(restricted)
    assert pa <= REVIEW, f"unexpected promotion actions: {sorted(pa - REVIEW)}"
    assert qa <= {"QUARANTINE"}, f"unexpected restricted actions: {sorted(qa - {'QUARANTINE'})}"
    assert not (pa | qa) & LEGACY, "legacy policy state detected"

    items = readiness.get("items", [])
    assert items, "readiness queue is empty"
    assert all(item.get("readiness_state") in READINESS_STATES for item in items), "unknown readiness state"
    assert all(
        item.get("readiness_state") == ("QUARANTINED" if item.get("promotion_action") == "QUARANTINE" else "ON_SHELF")
        for item in items
    ), "collection processor must not infer runtime readiness"

    assert isinstance(declarations.get("items"), dict)
    for key, item in declarations["items"].items():
        assert key in {x["capability_key"] for x in items}
        assert item["state"] in READINESS_STATES - {"ON_SHELF","QUARANTINED"}

    gate = GATE.read_text()
    readiness_gate = READINESS_GATE.read_text()
    assert "REVIEW_NEW_OR_UPGRADE" in gate
    assert "REVIEW_MERGE_OR_UPGRADE" in gate
    assert "READY_ON_DEMAND" in readiness_gate
    assert "READY_TO_USE" in readiness_gate
    assert "must never infer" in readiness_gate

    print("collection promotion/readiness-policy consistency: PASS")

if __name__ == "__main__":
    main()
