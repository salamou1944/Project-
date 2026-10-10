#!/usr/bin/env python3
"""Read-only READY.json non-regression audit.

The compared revisions can contain legitimate new extraction results, so exact
whole-document equality is not a valid requirement. This audit instead verifies
that the regenerated state has not lost prior decision identities or decreased
any previously recorded count. Serialization correctness is tested separately
by test_ready_json_compaction.py.
"""
from __future__ import annotations
import json
import subprocess

PATH = "COLLECTION/MASTER/READY.json"
BEFORE = "0d824d436b4e2a3c01ef6115c266f32c8e48f836"
AFTER = "HEAD"


def load_revision(revision: str):
    proc = subprocess.run(
        ["git", "show", f"{revision}:{PATH}"],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return json.loads(proc.stdout)


def shape(value):
    if isinstance(value, dict):
        return {"type": "object", "keys": len(value), "keys_sample": sorted(value)[:30]}
    if isinstance(value, list):
        return {"type": "array", "items": len(value)}
    return {"type": type(value).__name__}


def main() -> int:
    print(f"Loading pre-recovery revision {BEFORE}...", flush=True)
    before = load_revision(BEFORE)
    print(f"Loading current revision {AFTER}...", flush=True)
    after = load_revision(AFTER)
    print("BEFORE_SHAPE=" + json.dumps(shape(before), sort_keys=True))
    print("AFTER_SHAPE=" + json.dumps(shape(after), sort_keys=True))

    before_counts = before.get("counts", {})
    after_counts = after.get("counts", {})
    regressions = {
        key: {"before": value, "after": after_counts.get(key)}
        for key, value in before_counts.items()
        if isinstance(value, (int, float))
        and (not isinstance(after_counts.get(key), (int, float)) or after_counts[key] < value)
    }
    print("COUNTS_BEFORE=" + json.dumps(before_counts, sort_keys=True))
    print("COUNTS_AFTER=" + json.dumps(after_counts, sort_keys=True))
    print("COUNT_REGRESSIONS=" + json.dumps(regressions, sort_keys=True))

    old_decisions = before.get("decisions", [])
    new_decisions = after.get("decisions", [])
    old_keys = {
        item.get("capability_key") for item in old_decisions
        if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
    }
    new_keys = {
        item.get("capability_key") for item in new_decisions
        if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
    }
    missing = sorted(old_keys - new_keys)
    print(f"DECISIONS_LENGTH_BEFORE={len(old_decisions)}")
    print(f"DECISIONS_LENGTH_AFTER={len(new_decisions)}")
    print(f"DECISION_IDENTITIES_BEFORE={len(old_keys)}")
    print(f"DECISION_IDENTITIES_AFTER={len(new_keys)}")
    print("MISSING_PRIOR_DECISION_IDENTITIES=" + json.dumps(missing[:100], ensure_ascii=False))
    if missing:
        prior_by_key = {
            item.get("capability_key"): item for item in old_decisions
            if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
        }
        print("MISSING_PRIOR_DECISION_RECORDS=" + json.dumps(
            [prior_by_key[key] for key in missing[:30]], sort_keys=True, ensure_ascii=False
        )[:12000])

    if regressions or missing or len(old_keys) != len(old_decisions) or len(new_keys) != len(new_decisions):
        print("NON_REGRESSION=FAIL")
        print("Conclusion: prior decision identities or count invariants require investigation.")
        return 2

    if before == after:
        print("NON_REGRESSION=PASS (exact semantic equality)")
    else:
        print("NON_REGRESSION=PASS (all prior decision identities and counts preserved; additions allowed)")
    print("Conclusion: no prior decision identity or recorded count was lost in regeneration.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"AUDIT_ERROR={type(exc).__name__}: {exc}")
        raise SystemExit(3)
