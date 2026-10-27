#!/usr/bin/env python3
"""Read-only diagnosis of why the Collection installer selected zero candidates.

This never changes approvals or installs sources. It separates queue-level
authorization blockers from source-level eligibility and emits a small review
shortlist so an explicit, evidence-backed approval can be made deliberately.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from collection_json_io import load_collection_json
from install_assets import ALLOWED, is_quarantined_revision, load_quarantined_revisions

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "COLLECTION/AUTO/EXTRACTED/MANIFEST.json"
QUEUE = ROOT / "COLLECTION/MASTER/VALUE-OPERATOR-QUEUE.json"


def main() -> None:
    manifest = load_collection_json(MANIFEST)
    queue = load_collection_json(QUEUE)
    rows = manifest.get("sources", [])
    items = queue.get("items", [])
    if not isinstance(rows, list) or not isinstance(items, list):
        raise SystemExit("invalid manifest/value-queue shape; no diagnosis possible")
    quarantined = load_quarantined_revisions()
    license_counts = Counter(str(row.get("license") or "<missing>") for row in rows if isinstance(row, dict))
    global_eligible = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        source = row.get("canonical_source")
        revision = row.get("revision_sha")
        if (row.get("state") == "extracted" and row.get("license") in ALLOWED
                and row.get("mode") in {"cached", "refreshed"}
                and isinstance(source, str) and source.startswith("github:")
                and isinstance(revision, str) and len(revision) == 40
                and int(row.get("files_extracted", 0) or 0) > 0):
            repo = source.removeprefix("github:")
            if not is_quarantined_revision(repo, revision, quarantined):
                global_eligible.append({"repo": repo, "revision": revision, "license": row.get("license"), "mode": row.get("mode"), "files_extracted": row.get("files_extracted")})
    by_source = {
        row.get("canonical_source"): row
        for row in rows
        if isinstance(row, dict) and isinstance(row.get("canonical_source"), str)
    }
    queue_gates = Counter()
    source_gates = Counter()
    shortlist = []
    high_value_shortlist = []
    seen = set()

    for item in items:
        if not isinstance(item, dict):
            queue_gates["malformed_queue_item"] += 1
            continue
        promotion = item.get("promotion_action", item.get("action"))
        approval = item.get("install_approval", "NOT_APPROVED")
        integration = item.get("integration_gate", "UNVERIFIED")
        security = item.get("security_gate", "UNVERIFIED")
        queue_gates[f"promotion_action:{promotion}"] += 1
        queue_gates[f"install_approval:{approval}"] += 1
        queue_gates[f"integration_gate:{integration}"] += 1
        queue_gates[f"security_gate:{security}"] += 1

        sources = item.get("sources", [])
        capability = str(item.get("capability_key") or "").lower()
        noise_terms = ("test", "fixture", "mock", "benchmark", "readme", "docs", "runbook", "example", "sample", "demo")
        priority = item.get("priority", [0])
        if isinstance(priority, (list, tuple)):
            priority_score = int(priority[0]) if priority and str(priority[0]).lstrip("-").isdigit() else 0
        else:
            priority_score = int(priority) if str(priority).lstrip("-").isdigit() else 0
        if not isinstance(sources, list):
            source_gates["malformed_sources_list"] += 1
            continue
        for source in sources:
            row = by_source.get(source)
            if not isinstance(row, dict):
                source_gates["missing_manifest_source"] += 1
                continue
            repo = source.removeprefix("github:")
            revision = row.get("revision_sha")
            if row.get("state") != "extracted":
                source_gates["not_extracted"] += 1
                continue
            if row.get("license") not in ALLOWED:
                source_gates["license_not_allowed_or_unknown"] += 1
                continue
            if row.get("mode") not in {"cached", "refreshed"}:
                source_gates["stale_or_unknown_refresh_mode"] += 1
                continue
            if not isinstance(revision, str) or len(revision) != 40 or any(c not in "0123456789abcdefABCDEF" for c in revision):
                source_gates["revision_not_full_sha"] += 1
                continue
            try:
                if int(row.get("files_extracted", 0) or 0) <= 0:
                    source_gates["no_extracted_files"] += 1
                    continue
            except (TypeError, ValueError):
                source_gates["invalid_file_count"] += 1
                continue
            if is_quarantined_revision(repo, revision, quarantined):
                source_gates["quarantined_revision"] += 1
                continue
            source_gates["source_level_eligible_before_approval"] += 1
            identity = (repo, revision.lower())
            if not any(term in capability for term in noise_terms) and any(term in (capability + " " + repo.lower()) for term in ("api", "gateway", "provider", "mcp", "router", "agent", "quota", "validation", "model", "skill", "workflow", "runtime")):
                high_value_shortlist.append({
                    "priority_score": priority_score,
                    "operator_action": item.get("operator_action"),
                    "capability_key": item.get("capability_key"),
                    "repo": repo,
                    "revision": revision,
                    "license": row.get("license"),
                    "mode": row.get("mode"),
                    "files_extracted": row.get("files_extracted"),
                    "install_approval": approval,
                    "integration_gate": integration,
                    "security_gate": security,
                })
            if identity in seen:
                continue
            seen.add(identity)
            shortlist.append({
                "repo": repo,
                "revision": revision,
                "license": row.get("license"),
                "mode": row.get("mode"),
                "files_extracted": row.get("files_extracted"),
                "capability_key": item.get("capability_key"),
                "promotion_action": promotion,
                "install_approval": approval,
                "integration_gate": integration,
                "security_gate": security,
            })

    high_value_shortlist.sort(key=lambda row: (row["priority_score"], row["capability_key"], row["repo"]), reverse=True)
    report = {
        "status": "DIAGNOSIS_ONLY_NO_INSTALLS",
        "manifest_sources": len(rows),
        "manifest_license_counts": dict(license_counts.most_common()),
        "globally_eligible_sources_before_capability_and_approval": len(global_eligible),
        "global_eligible_source_sample": global_eligible[:20],
        "value_queue_items": len(items),
        "queue_gate_counts": dict(sorted(queue_gates.items())),
        "source_gate_counts": dict(sorted(source_gates.items())),
        "source_level_eligible_but_not_authorized_count": len(shortlist),
        "review_shortlist": shortlist[:12],
        "high_value_review_shortlist": high_value_shortlist[:30],
        "policy_note": "No approval is inferred. Each installation requires explicit approval and independently evidenced PASS integration/security gates.",
    }
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
