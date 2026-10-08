#!/usr/bin/env python3
"""Validate Collection's callable registry fail-closed contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REG = ROOT / "COLLECTION" / "MASTER" / "CALLABLE-REGISTRY.json"
SCHEMA = ROOT / "COLLECTION" / "MASTER" / "CALLABLE-REGISTRY.schema.json"


def main() -> int:
    data = json.loads(REG.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    assert data.get("schema_version") == schema["properties"]["schema_version"]["const"]
    entries = data.get("entries", [])
    ids = set()
    for e in entries:
        required = ["capability_id","name","kind","source","our_location","entrypoint","invocation","dependencies","secret_refs","status","evidence"]
        missing = [k for k in required if k not in e]
        assert not missing, f"{e.get('capability_id')}: missing {missing}"
        cid = e["capability_id"]
        assert cid not in ids, f"duplicate capability_id: {cid}"
        ids.add(cid)
        assert e["status"] in {"REGISTERED","CALLABLE_ON_DEMAND","PROVEN_CALLABLE","BLOCKED"}
        inv = e["invocation"]
        assert isinstance(inv, dict) and isinstance(inv.get("argv"), list) and inv["argv"], f"{cid}: invalid invocation"
        assert all(isinstance(x, str) and x for x in inv["argv"]), f"{cid}: invalid argv"
        assert isinstance(e["secret_refs"], list)
        # Fail closed: callable states require concrete local implementation paths.
        if e["status"] in {"CALLABLE_ON_DEMAND","PROVEN_CALLABLE"}:
            assert e["our_location"]["repository"] == "salamou1944/Project-", f"{cid}: callable artifact must be in Project-"
            p = (ROOT / e["our_location"]["path"]).resolve()
            assert ROOT in p.parents or p == ROOT, f"{cid}: artifact escapes root"
            assert p.exists(), f"{cid}: artifact path missing: {e['our_location']['path']}"
            assert e["entrypoint"] in e["invocation"]["argv"] or e["entrypoint"].endswith(e["invocation"]["argv"][-1]), f"{cid}: entrypoint not bound to invocation"
        if e["status"] == "PROVEN_CALLABLE":
            assert e["evidence"], f"{cid}: PROVEN_CALLABLE requires execution evidence"
    print(f"CALLABLE_REGISTRY_VALID entries={len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
