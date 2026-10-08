#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
Q=ROOT/"COLLECTION/AUTO/DEEP-EXTRACTED/EXTRACTION-READY-QUEUE.json"
S=ROOT/"COLLECTION/MASTER/EXTRACTION-READY.schema.json"
def main():
    doc=json.loads(Q.read_text(encoding="utf-8")); assert doc["schema_version"]=="collection-extraction-ready/v1"
    items=doc.get("items",[]); ids=set()
    for x in items:
        for k in ("extraction_id","source","source_revision","file","asset_type","content_sha256"): assert x.get(k),k
        assert x["handoff_status"]=="READY_FOR_DEDUPE"; assert x["readiness_state"]=="ON_SHELF"
        assert x["extraction_id"] not in ids,"duplicate extraction_id"
        ids.add(x["extraction_id"])
    json.loads(S.read_text(encoding="utf-8"))
    print(json.dumps({"status":"PASS","items":len(items)}))
if __name__=="__main__": main()
