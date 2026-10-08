#!/usr/bin/env python3
"""Turn Collection's existing promotion queue into a conservative next-action plan.

This is an orchestration layer, not a second extractor or readiness engine.
It consumes process_collection output and records the next reusable-value gate.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QUEUE = ROOT / "COLLECTION/MASTER/PROMOTION-QUEUE.json"
OUT = ROOT / "COLLECTION/MASTER/VALUE-OPERATOR-QUEUE.json"

FAMILY_ACTIONS = {
    "commerce_revenue": "REVENUE_INFRASTRUCTURE_REVIEW",
    "api_engineering": "API_FACTORY_REVIEW",
    "ai_model_routing": "MODEL_ROUTING_REVIEW",
    "agent_orchestration": "AGENT_RUNTIME_REVIEW",
    "deployment_operations": "OPS_AUTOMATION_REVIEW",
    "security_defense": "SECURITY_HARDENING_REVIEW",
    "data_storage": "DATA_RUNTIME_REVIEW",
    "evaluation_reliability": "EVALUATION_REVIEW",
    "media_content": "MEDIA_PIPELINE_REVIEW",
    "research_osint": "RESEARCH_REVIEW",
}

def score(item: dict) -> tuple[int, int, int]:
    families = item.get("evidence", [{}])[0].get("families", [])
    top = families[0] if families else {}
    return (int(top.get("score", 0)), int(item.get("evidence_count", 0)), int(item.get("source_count", 0)))

def main() -> None:
    if not QUEUE.exists() or QUEUE.stat().st_size == 0:
        raise SystemExit("promotion queue is missing or empty; Collection must finish process_collection first")
    doc = json.loads(QUEUE.read_text(encoding="utf-8"))
    plan = []
    for item in doc.get("items", []):
        families = item.get("evidence", [{}])[0].get("families", [])
        family = families[0].get("family") if families else None
        plan.append({
            "capability_key": item.get("capability_key"),
            "operator_action": FAMILY_ACTIONS.get(family, "GENERAL_REUSE_REVIEW"),
            "priority": score(item),
            "evidence_count": item.get("evidence_count", 0),
            "source_count": item.get("source_count", 0),
            "sources": item.get("sources", []),
            "promotion_action": item.get("action"),
            "execution_state": "NOT_EXECUTED",
            "next_gate": item.get("next_gate"),
        })
    plan.sort(key=lambda x: x["priority"], reverse=True)
    summary = {}
    for item in plan:
        summary[item["operator_action"]] = summary.get(item["operator_action"], 0) + 1
    OUT.write_text(json.dumps({
        "schema_version": "collection-value-operator/v1",
        "source": "COLLECTION/MASTER/PROMOTION-QUEUE.json",
        "rule": "plan next action from existing evidence; never infer readiness or execution",
        "generated_at": doc.get("generated_at"),
        "summary": summary,
        "items": plan,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "items": len(plan), "summary": summary}, sort_keys=True))

if __name__ == "__main__":
    main()
