#!/usr/bin/env python3
"""Fast evidence-first post-extraction pipeline.
Route: normalize -> classify -> dedupe -> promotion decision -> verification queue.
Third-party code is never copied into executable Skills automatically.
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
        if not families and not restricted: continue
        key=norm((families[0]["family"] if families else "restricted")+"-"+Path(title).stem)
        digest=hashlib.sha256((source+"|"+title+"|"+f.get("content_sha256","")).encode()).hexdigest()
        records.append({"capability_key":key,"evidence_id":digest[:16],"source":source,
        "source_revision":data.get("revision_sha"),"source_license":data.get("license"),
        "file":title,"families":families,"classification":"RESTRICTED" if restricted else "REVIEW",
        "restriction_signals":restricted,"content_sha256":f.get("content_sha256"),
        "evidence_excerpt":body[:500].replace("\n"," ")})
    return records

def main():
    MASTER.mkdir(parents=True,exist_ok=True); VERIFY.mkdir(parents=True,exist_ok=True)
    files=[p for p in EXTRACTED.glob("*.json") if p.name!="MANIFEST.json"]
    all_records=[]
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures=[ex.submit(inspect_file,p) for p in files]
        for fut in as_completed(futures): all_records.extend(fut.result())
    by_key={}
    for r in all_records: by_key.setdefault(r["capability_key"],[]).append(r)
    decisions=[]
    for key,group in sorted(by_key.items()):
        sources=sorted({x["source"] for x in group})
        restricted=any(x["classification"]=="RESTRICTED" for x in group)
        action="RESTRICTED" if restricted else ("MERGE_OR_UPGRADE_REVIEW" if len(sources)>1 else "NEW_OR_UPGRADE_REVIEW")
        decisions.append({"capability_key":key,"action":action,"evidence_count":len(group),
        "source_count":len(sources),"sources":sources[:20],"evidence":group[:20],
        "next_gate":"safety review + authorization gate" if restricted else "canonical Skill dedupe + validation"})
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    counts={"files_scanned":len(files),"evidence_records":len(all_records),"capability_groups":len(decisions),
    "restricted":sum(d["action"]=="RESTRICTED" for d in decisions),
    "merge_or_upgrade":sum(d["action"]=="MERGE_OR_UPGRADE_REVIEW" for d in decisions),
    "new_or_upgrade":sum(d["action"]=="NEW_OR_UPGRADE_REVIEW" for d in decisions)}
    ready={"generated_at":now,"pipeline":["extract","normalize","classify","dedupe","decide","verify"],"counts":counts,"decisions":decisions}
    (MASTER/"READY.json").write_text(json.dumps(ready,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    queue=[d for d in decisions if d["action"]!="RESTRICTED"]
    (MASTER/"PROMOTION-QUEUE.json").write_text(json.dumps({"generated_at":now,"items":queue},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    restricted_queue=[d for d in decisions if d["action"]=="RESTRICTED"]
    (VERIFY/"RESTRICTED-QUEUE.json").write_text(json.dumps({"generated_at":now,"items":restricted_queue},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(counts))

if __name__=="__main__": main()
