#!/usr/bin/env python3
"""Validate explicit Collection readiness declarations.

Fail-closed: no declaration means no runtime readiness claim.
This validates the evidence contract; it does not execute activation commands.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QUEUE = ROOT / "COLLECTION/MASTER/READINESS-QUEUE.json"
DECL = ROOT / "COLLECTION/MASTER/READINESS-DECLARATIONS.json"

STATES = {
    "READY_ON_DEMAND","READY_TO_USE","INTEGRATED","TESTED","HUMAN_READY","PRODUCTION_PROVEN"
}
REQUIRED = {
    "capability_key","state","source_revisions","license_boundary",
    "dependencies","config_schema","activation_recipe","smoke_test","evidence_refs"
}

def main():
    queue = json.loads(QUEUE.read_text())
    declarations_doc = json.loads(DECL.read_text()) if DECL.exists() else {"items": {}}
    declarations = declarations_doc.get("items", {})

    if not isinstance(declarations, dict):
        raise SystemExit("readiness declarations must be an object keyed by capability_key")

    known = {item["capability_key"]: item for item in queue["items"]}

    for key, d in declarations.items():
        if key not in known:
            raise SystemExit(f"declaration references unknown capability_key: {key}")
        missing = sorted(REQUIRED - set(d))
        if missing:
            raise SystemExit(f"{key}: missing readiness fields: {missing}")
        if d["state"] not in STATES:
            raise SystemExit(f"{key}: invalid readiness state {d['state']}")
        if d["state"] == "READY_TO_USE" and "execution_evidence" not in d:
            raise SystemExit(f"{key}: READY_TO_USE requires execution_evidence")
        if d["state"] in {"INTEGRATED","TESTED","HUMAN_READY","PRODUCTION_PROVEN"} and "execution_evidence" not in d:
            raise SystemExit(f"{key}: {d['state']} requires execution_evidence")

    for key, item in known.items():
        if item["promotion_action"] == "QUARANTINE" and key in declarations:
            raise SystemExit(f"{key}: quarantined evidence cannot receive readiness declaration")

    print(json.dumps({
        "status":"PASS",
        "queue_items":len(known),
        "explicit_declarations":len(declarations),
        "runtime_readiness_claims":len(declarations)
    }, sort_keys=True))

if __name__ == "__main__":
    main()
