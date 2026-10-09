#!/usr/bin/env python3
"""Fast evidence-first post-extraction pipeline.

Route:
normalize -> classify -> dedupe -> promotion decision -> verification queue
-> explicit readiness state.

Readiness is deliberately NOT inferred from collection evidence. Collection
evidence can place an item ON_SHELF or QUARANTINED; READY_ON_DEMAND and
READY_TO_USE require a separate readiness declaration with activation and
runtime evidence.
"""
import datetime, hashlib, json, re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

EXTRACTED=Path("COLLECTION/AUTO/EXTRACTED")
MASTER=Path("COLLECTION/MASTER")
VERIFY=Path("COLLECTION/VERIFICATION")
MAX_WORKERS=16

SIGNALS={
"agent_orchestration":("agent","orchestration","workflow","tool calling","multi-agent"),
"api_engineering":("api","sdk","rest","graphql","webhook"),
"ai_model_routing":("llm","model","provider","inference","routing","gateway"),
"evaluation_reliability":("eval","evaluation","benchmark","test","regression","quality"),
"security_defense":("security","auth","rbac","permission","vulnerability","hardening"),
"deployment_operations":("deploy","railway","vercel","docker","kubernetes","ci","cd","observability"),
"data_storage":("database","postgres","redis","storage","backup","vector","embedding"),
"media_content":("video","audio","image","voice","caption","creative"),
"commerce_revenue":("payment","billing","commerce","affiliate","revenue","subscription"),
"research_osint":("osint","recon","rdap","dns","search","research"),
}
RESTRICTED=("credential","secret","token","malware","persistence","evasion","exfiltration","privilege","exploit","bypass","destructive")

def norm(s):
    return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")

def classify(text):
    low=text.lower()
    scores={k:sum(low.count(x) for x in xs) for k,xs in SIGNALS.items()}
    return [{"family":k,"score":v} for k,v in sorted(scores.items(),key=lambda x:x[1],reverse=True) if v][:5]

def inspect_file(path):
    data=json.loads(path.read_text(encoding="utf-8"))
    source=data.get("canonical_source",path.stem)
    records=[]
    for f in data.get("files",[]):
        body=f.get("content","")
        title=f.get("path","")
        sample=f"{title}\n{body[:12000]}"
        restricted=[x for x in RESTRICTED if x in sample.lower()]
        families=classify(sample)
        if not families and not restricted:
            continue
        key=norm((families[0]["family"] if families else "restricted")+"-"+Path(title).stem)
        digest=hashlib.sha256((source+"|"+title+"|"+f.get("content_sha256","")).encode()).hexdigest()
        records.append({
            "capability_key":key,
            "evidence_id":digest[:16],
            "source":source,
            "source_revision":data.get("revision_sha"),
            "source_license":data.get("license"),
            "file":title,
            "families":families,
            "classification":"RESTRICTED" if restricted else "REVIEW",
            "restriction_signals":restricted,
            "content_sha256":f.get("content_sha256"),
            "evidence_excerpt":body[:500].replace("\n"," ")
        })
    return records

def source_files_from_manifest():
    """Process only artifacts declared extracted in the current manifest.

    Stale JSON files left behind after a blocked refresh must never silently
    re-enter the active evidence pipeline.
    """
    manifest_path = EXTRACTED / "MANIFEST.json"
    if not manifest_path.is_file() or manifest_path.stat().st_size == 0:
        raise SystemExit("missing or empty extraction manifest; refusing stale-source processing")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit(f"invalid extraction manifest; refusing stale-source processing: {exc}")
    sources = manifest.get("sources")
    if not isinstance(sources, list):
        raise SystemExit("extraction manifest sources must be a list")
    paths = []
    seen = set()
    for item in sources:
        if not isinstance(item, dict) or item.get("state") != "extracted":
            continue
        raw_path = item.get("path")
        if not raw_path:
            raise SystemExit(f"extracted source has no artifact path: {item.get('canonical_source')}")
        path = Path(raw_path)
        if not path.is_absolute():
            path = Path.cwd() / path
        path = path.resolve()
        root = EXTRACTED.resolve()
        if root not in path.parents or path.name == "MANIFEST.json" or path.suffix != ".json":
            raise SystemExit(f"manifest source path escapes extracted root: {raw_path}")
        if path in seen:
            continue
        seen.add(path)
        if not path.is_file() or path.stat().st_size == 0:
            raise SystemExit(f"manifest declares missing/empty extracted artifact: {path}")
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise SystemExit(f"invalid extracted artifact {path}: {exc}")
        if data.get("state") != "extracted":
            raise SystemExit(f"artifact state disagrees with manifest: {path}")
        if data.get("canonical_source") != item.get("canonical_source"):
            raise SystemExit(f"artifact source identity disagrees with manifest: {path}")
        if item.get("revision_sha") and data.get("revision_sha") != item.get("revision_sha"):
            raise SystemExit(f"artifact revision disagrees with manifest: {path}")
        paths.append(path)
    if not paths:
        raise SystemExit("manifest contains no valid extracted source artifacts; refusing empty state regeneration")
    return sorted(paths)


def main():
    MASTER.mkdir(parents=True,exist_ok=True)
    VERIFY.mkdir(parents=True,exist_ok=True)
    files=source_files_from_manifest()
    all_records=[]
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures=[ex.submit(inspect_file,p) for p in files]
        for fut in as_completed(futures):
            all_records.extend(fut.result())

    by_key={}
    for r in all_records:
        by_key.setdefault(r["capability_key"],[]).append(r)

    decisions=[]
    for key,group in sorted(by_key.items()):
        sources=sorted({x["source"] for x in group})
        restricted=any(x["classification"]=="RESTRICTED" for x in group)
        action="QUARANTINE" if restricted else ("REVIEW_MERGE_OR_UPGRADE" if len(sources)>1 else "REVIEW_NEW_OR_UPGRADE")
        decisions.append({
            "capability_key":key,
            "action":action,
            "evidence_count":len(group),
            "source_count":len(sources),
            "sources":sources[:20],
            "evidence":group[:20],
            "next_gate":"safety review + authorization gate" if restricted else "canonical Skill dedupe + validation"
        })

    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    counts={
        "files_scanned":len(files),
        "evidence_records":len(all_records),
        "capability_groups":len(decisions),
        "quarantine":sum(d["action"]=="QUARANTINE" for d in decisions),
        "review_merge_or_upgrade":sum(d["action"]=="REVIEW_MERGE_OR_UPGRADE" for d in decisions),
        "review_new_or_upgrade":sum(d["action"]=="REVIEW_NEW_OR_UPGRADE" for d in decisions)
    }

    ready={"generated_at":now,"pipeline":["extract","normalize","classify","dedupe","decide","verify"],"counts":counts,"decisions":decisions}
    (MASTER/"READY.json").write_text(json.dumps(ready,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    queue=[d for d in decisions if d["action"]!="QUARANTINE"]
    (MASTER/"PROMOTION-QUEUE.json").write_text(json.dumps({"generated_at":now,"items":queue},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    restricted_queue=[d for d in decisions if d["action"]=="QUARANTINE"]
    (VERIFY/"RESTRICTED-QUEUE.json").write_text(json.dumps({"generated_at":now,"items":restricted_queue},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    readiness_items=[]
    for d in decisions:
        readiness_items.append({
            "capability_key":d["capability_key"],
            "source_count":d["source_count"],
            "sources":d["sources"],
            "evidence_count":d["evidence_count"],
            "evidence_ids":[e["evidence_id"] for e in d["evidence"]],
            "source_revisions":sorted({e.get("source_revision") for e in d["evidence"] if e.get("source_revision")}),
            "licenses":sorted({e.get("source_license") for e in d["evidence"] if e.get("source_license")}),
            "promotion_action":d["action"],
            "readiness_state":"QUARANTINED" if d["action"]=="QUARANTINE" else "ON_SHELF",
            "next_readiness_gate":"safety/authorization" if d["action"]=="QUARANTINE" else "explicit readiness declaration + activation/smoke evidence"
        })
    (MASTER/"READINESS-QUEUE.json").write_text(
        json.dumps({
            "schema_version":"collection-readiness-queue/v1",
            "generated_at":now,
            "rule":"collection evidence is provenance; readiness is never inferred",
            "states":["ON_SHELF","READY_FOR_ADAPTATION","READY_ON_DEMAND","READY_TO_USE","INTEGRATED","TESTED","HUMAN_READY","PRODUCTION_PROVEN","QUARANTINED"],
            "items":readiness_items
        },ensure_ascii=False,indent=2)+"\n",encoding="utf-8"
    )
    print(json.dumps(counts))

if __name__=="__main__":
    main()
