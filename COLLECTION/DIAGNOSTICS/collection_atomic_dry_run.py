#!/usr/bin/env python3
"""Read-only atomic dry-run of Collection's end-to-end path.

Does not invoke the harvester, write generated state, install assets, or call external APIs.
Stops at the first blocked stage and reports the exact gate.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGES = []

def gate(name, check):
    try:
        detail = check()
        STAGES.append({"stage": name, "status": "PASS", "detail": detail})
        print(f"PASS | {name} | {detail}")
        return True
    except Exception as exc:
        STAGES.append({"stage": name, "status": "BLOCKED", "detail": str(exc)})
        print(f"BLOCKED | {name} | {exc}")
        print(json.dumps({"status":"BLOCKED","first_blocker":name,"stages":STAGES}, ensure_ascii=False, indent=2))
        raise SystemExit(2)

def load_json(path):
    if not path.is_file():
        raise RuntimeError(f"missing file: {path.relative_to(ROOT)}")
    if path.stat().st_size == 0:
        raise RuntimeError(f"empty file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeError(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

def main():
    auto = ROOT / "COLLECTION/AUTO"
    manifest_path = auto / "EXTRACTED/MANIFEST.json"
    manifest = None
    def manifest_gate():
        nonlocal manifest
        manifest = load_json(manifest_path)
        if not isinstance(manifest.get("sources"), list):
            raise RuntimeError("manifest.sources is not a list")
        return f"accounts={manifest.get('account_count',0)} repos={manifest.get('repo_count',0)} sources={len(manifest['sources'])}"
    gate("1_manifest", manifest_gate)

    def artifact_gate():
        extracted = [s for s in manifest["sources"] if isinstance(s,dict) and s.get("state")=="extracted"]
        if not extracted:
            raise RuntimeError("manifest has no extracted sources")
        missing=[]; zero_files=[]; checked=0
        for item in extracted:
            raw=item.get("path")
            if not raw: missing.append("<missing path>"); continue
            p=Path(raw)
            if not p.is_absolute(): p=ROOT/p
            p=p.resolve()
            if ROOT.resolve() not in p.parents or p.name=="MANIFEST.json":
                missing.append(f"unsafe path: {raw}"); continue
            if not p.is_file() or p.stat().st_size==0:
                missing.append(raw); continue
            data=load_json(p)
            if data.get("state")!="extracted" or data.get("canonical_source")!=item.get("canonical_source"):
                missing.append(f"identity mismatch: {raw}"); continue
            checked+=1
            if int(item.get("files_extracted",0) or 0)==0: zero_files.append(raw)
        if missing: raise RuntimeError(f"{len(missing)} extracted artifacts missing/invalid; first={missing[0]}")
        if checked==0: raise RuntimeError("no valid extracted artifacts")
        return f"valid_artifacts={checked} zero_file_sources={len(zero_files)}"
    gate("2_preserved_artifacts", artifact_gate)

    def static_gate():
        required={
          "extractor":auto/"intelligent_extract.py",
          "processor":auto/"process_collection.py",
          "dispatcher":auto/"invoke_capability.py",
          "canonical_reconcile":auto/"reconcile_canonical_skills.py",
          "readiness_validator":auto/"validate_readiness.py",
          "registry_validator":auto/"validate_callable_registry.py",
          "state_guard":auto/"collection_state_guard.py",
          "value_operator":auto/"collection_value_operator.py",
          "installer":auto/"install_assets.py",
        }
        missing=[name for name,p in required.items() if not p.is_file() or p.stat().st_size==0]
        if missing: raise RuntimeError("pipeline components missing/empty: "+", ".join(missing))
        workflow=load_yaml_text(ROOT/".github/workflows/collection-continuous.yml")
        for needle in ("intelligent_extract.py","invoke_capability.py collection.process_collection","reconcile_canonical_skills.py","collection_state_guard.py","collection_value_operator.py","validate_readiness.py","validate_callable_registry.py","install_assets.py"):
            if needle not in workflow: raise RuntimeError(f"workflow missing stage reference: {needle}")
        return f"pipeline_components={len(required)} workflow_stages=8"
    gate("3_pipeline_wiring", static_gate)

    def generated_state_gate():
        paths=[
          ROOT/"COLLECTION/MASTER/READY.json",
          ROOT/"COLLECTION/MASTER/PROMOTION-QUEUE.json",
          ROOT/"COLLECTION/MASTER/READINESS-QUEUE.json",
          ROOT/"COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json",
        ]
        docs=[load_json(p) for p in paths]
        ready,promotion,readiness,restricted=docs
        if int(ready.get("counts",{}).get("files_scanned",0))<=0:
            raise RuntimeError("READY.json files_scanned is zero")
        for name,doc in (("READY",ready),("PROMOTION",promotion),("READINESS",readiness),("RESTRICTED",restricted)):
            key="decisions" if name=="READY" else "items"
            if not isinstance(doc.get(key),list): raise RuntimeError(f"{name}.{key} is not a list")
        return f"files_scanned={ready['counts']['files_scanned']} groups={ready['counts'].get('capability_groups',0)} promotion={len(promotion['items'])} readiness={len(readiness['items'])} restricted={len(restricted['items'])}"
    gate("4_generated_state", generated_state_gate)

    def registry_gate():
        reg=load_json(ROOT/"COLLECTION/MASTER/CALLABLE-REGISTRY.json")
        schema=load_json(ROOT/"COLLECTION/MASTER/CALLABLE-REGISTRY.schema.json")
        if reg.get("schema_version")!=schema.get("properties",{}).get("schema_version",{}).get("const"):
            raise RuntimeError("callable registry schema version mismatch")
        entries=reg.get("entries")
        if not isinstance(entries,list): raise RuntimeError("registry.entries is not a list")
        seen=set()
        for e in entries:
            cid=e.get("capability_id")
            if not cid or cid in seen: raise RuntimeError(f"missing/duplicate capability_id: {cid}")
            seen.add(cid)
            if e.get("status")=="PROVEN_CALLABLE" and not e.get("evidence"):
                raise RuntimeError(f"{cid}: PROVEN_CALLABLE without evidence")
            if e.get("status") in {"CALLABLE_ON_DEMAND","PROVEN_CALLABLE"}:
                p=(ROOT/e.get("our_location",{}).get("path","")).resolve()
                if ROOT.resolve() not in p.parents and p!=ROOT.resolve():
                    raise RuntimeError(f"{cid}: callable path escapes repository")
                if not p.exists(): raise RuntimeError(f"{cid}: callable path missing")
        return f"registry_entries={len(entries)}"
    gate("5_callable_registry", registry_gate)

    def readiness_gate():
        q=load_json(ROOT/"COLLECTION/MASTER/READINESS-QUEUE.json")
        d=load_json(ROOT/"COLLECTION/MASTER/READINESS-DECLARATIONS.json")
        items=q.get("items",[])
        declarations=d.get("items",{})
        if not isinstance(items,list) or not isinstance(declarations,dict):
            raise RuntimeError("readiness queue/declarations have invalid shapes")
        known={x.get("capability_key") for x in items}
        for key,value in declarations.items():
            if key not in known: raise RuntimeError(f"declaration for unknown capability: {key}")
            if value.get("state") in {"READY_TO_USE","INTEGRATED","TESTED","HUMAN_READY","PRODUCTION_PROVEN"} and not value.get("execution_evidence"):
                raise RuntimeError(f"{key}: execution evidence missing for {value.get('state')}")
        return f"readiness_items={len(items)} declarations={len(declarations)}"
    gate("6_readiness_contract", readiness_gate)

    print(json.dumps({"status":"PASS_DRY_RUN_ONLY","stages":STAGES,"mutations":0,"external_api_calls":0,"installation_executed":False,"note":"This validates the current repository state and wiring only; it does not claim a real harvest/install execution."},ensure_ascii=False,indent=2))

def load_yaml_text(path):
    if not path.is_file() or path.stat().st_size==0:
        raise RuntimeError(f"missing/empty workflow: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")

if __name__=="__main__":
    main()
