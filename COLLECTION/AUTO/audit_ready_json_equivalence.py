#!/usr/bin/env python3
"""Read-only semantic audit of READY.json against the last known-good revision.

Loads the preserved baseline and current checkout from Git history and compares
parsed values. It does not write to the repository or alter either revision.
"""
from __future__ import annotations
import json
import subprocess
import sys

PATH = "COLLECTION/MASTER/READY.json"
BEFORE = "147872fbdb542b0f9b3d403695742ca941018449"
AFTER = "HEAD"


def load_revision(revision: str):
    proc = subprocess.Popen(
        ["git", "show", f"{revision}:{PATH}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert proc.stdout is not None
    try:
        value = json.load(proc.stdout)
    except Exception:
        proc.kill()
        raise
    stderr = proc.stderr.read() if proc.stderr else b""
    code = proc.wait()
    if code:
        raise RuntimeError(f"git show failed for {revision}: {stderr.decode(errors='replace')}")
    return value


def shape(value):
    if isinstance(value, dict):
        return {"type": "object", "keys": len(value), "keys_sample": sorted(value)[:30]}
    if isinstance(value, list):
        return {"type": "array", "items": len(value)}
    return {"type": type(value).__name__}


def main() -> int:
    print(f"Loading before revision {BEFORE}...", flush=True)
    before = load_revision(BEFORE)
    print(f"Loading current revision {AFTER}...", flush=True)
    after = load_revision(AFTER)
    print("BEFORE_SHAPE=" + json.dumps(shape(before), sort_keys=True))
    print("AFTER_SHAPE=" + json.dumps(shape(after), sort_keys=True))
    for field in ("counts", "pipeline"):
        if isinstance(before, dict) and isinstance(after, dict) and field in before and field in after and before[field] != after[field]:
            print(f"{field.upper()}_BEFORE=" + json.dumps(before[field], sort_keys=True, ensure_ascii=False))
            print(f"{field.upper()}_AFTER=" + json.dumps(after[field], sort_keys=True, ensure_ascii=False))
    if isinstance(before, dict) and isinstance(after, dict):
        for field in ("decisions",):
            if isinstance(before.get(field), list) and isinstance(after.get(field), list):
                print(f"{field.upper()}_LENGTH_BEFORE={len(before[field])}")
                print(f"{field.upper()}_LENGTH_AFTER={len(after[field])}")
    if before == after:
        print("SEMANTIC_EQUALITY=PASS")
        print("Conclusion: parsed JSON values match the preserved baseline.")
        return 0
    print("SEMANTIC_EQUALITY=FAIL")
    if isinstance(before, dict) and isinstance(after, dict):
        bkeys, akeys = set(before), set(after)
        print("TOP_LEVEL_KEYS_ONLY_BEFORE=" + json.dumps(sorted(bkeys - akeys)[:100]))
        print("TOP_LEVEL_KEYS_ONLY_AFTER=" + json.dumps(sorted(akeys - bkeys)[:100]))
        for key in sorted(bkeys & akeys):
            if before[key] != after[key]:
                print("FIRST_DIFFERING_TOP_LEVEL_KEY=" + json.dumps(key))
                print("BEFORE_VALUE_SHAPE=" + json.dumps(shape(before[key]), sort_keys=True))
                print("AFTER_VALUE_SHAPE=" + json.dumps(shape(after[key]), sort_keys=True))
                break
    print("Conclusion: current READY.json differs semantically from the preserved baseline; investigate before declaring recovery complete.")
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"AUDIT_ERROR={type(exc).__name__}: {exc}", file=sys.stderr)
        raise SystemExit(3)
