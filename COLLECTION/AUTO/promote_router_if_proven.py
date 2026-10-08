#!/usr/bin/env python3
import json
from pathlib import Path

REGISTRY = Path("COLLECTION/MASTER/CALLABLE-REGISTRY.json")
EVIDENCE = Path("COLLECTION/VERIFICATION/HYPERSWITCH-ROUTER-SMOKE-EVIDENCE.json")
CAPABILITY = "hyperswitch.router_deterministic_unit_execution"

def main():
    if not EVIDENCE.exists():
        print("router promotion: no evidence; fail-closed")
        return 0

    evidence = json.loads(EVIDENCE.read_text())
    if evidence.get("execution_status") != "PROVEN_CALLABLE":
        print("router promotion: evidence is not PROVEN_CALLABLE; fail-closed")
        return 0
    if not evidence.get("workflow_run") or not evidence.get("workflow_attempt"):
        print("router promotion: missing workflow identity; fail-closed")
        return 0

    registry = json.loads(REGISTRY.read_text())
    for entry in registry.get("entries", []):
        if entry.get("capability_id") != CAPABILITY:
            continue
        entry["status"] = "PROVEN_CALLABLE"
        entry["evidence"] = [
            f"GitHub Actions run {evidence['workflow_run']}, attempt {evidence['workflow_attempt']} produced successful deterministic Router smoke evidence.",
            "COLLECTION/VERIFICATION/HYPERSWITCH-ROUTER-SMOKE-EVIDENCE.json records the execution.",
            "Promotion is fail-closed and occurs only when execution_status is PROVEN_CALLABLE and workflow identity is present."
        ]
        break
    else:
        raise SystemExit(f"capability not found: {CAPABILITY}")

    REGISTRY.write_text(json.dumps(registry, indent=2) + "\n")
    print("router promotion: PROVEN_CALLABLE")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
