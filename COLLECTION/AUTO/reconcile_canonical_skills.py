#!/usr/bin/env python3
"""Reconcile Collection candidates against the canonical Agent Skills repository.

This is deliberately conservative: it never copies third-party code and never
auto-promotes ambiguous candidates. Explicit decisions recorded in
COLLECTION/MASTER/CANONICAL-DECISIONS.json are authoritative. Obvious
repository-specific test/docs material is classified as REFERENCE. Everything
else remains REVIEW until semantic dedupe + validation evidence exists.
"""
import json,re,urllib.request
from pathlib import Path

QUEUE=Path("COLLECTION/MASTER/PROMOTION-QUEUE.json")
DECISIONS=Path("COLLECTION/MASTER/CANONICAL-DECISIONS.json")
OUT=Path("COLLECTION/MASTER/CANONICAL-PROMOTION-PLAN.json")
SKILLS_URL="https://api.github.com/repos/salamou1944/agent-skills/contents/skills"

def norm(s): return set(re.findall(r"[a-z0-9]+",s.lower()))

def load_skills():
    req=urllib.request.Request(SKILLS_URL,headers={"Accept":"application/vnd.github+json","User-Agent":"collection-canonical-reconciler"})
    with urllib.request.urlopen(req,timeout=30) as r: data=json.load(r)
    return sorted(x["name"] for x in data if x.get("type")=="dir")

def main():
    queue=json.loads(QUEUE.read_text()) if QUEUE.exists() else {"items":[]}
    explicit=json.loads(DECISIONS.read_text()) if DECISIONS.exists() else {}
    skills=load_skills()
    skill_tokens={s:norm(s) for s in skills}
    plan=[]
    for item in queue.get("items",[]):
        key=item.get("capability_key","")
        if key in explicit:
            decision=explicit[key]
            plan.append({**item,"terminal_decision":decision["decision"],"canonical_skill":decision.get("canonical_skill"),"reason":decision["reason"],"decision_source":"explicit"})
            continue
        text=" ".join([key,item.get("next_gate","")," ".join(item.get("sources",[]))])
        tokens=norm(text)
        obvious=bool(re.search(r"(test|fixture|runbook|example|documentation|docs|readme)$",key))
        matches=sorted((len(tokens & st),name) for name,st in skill_tokens.items() if tokens & st)
        best=matches[-1] if matches else (0,None)
        if obvious:
            decision="REFERENCE"; reason="Repository-specific test/runbook/example material without a distinct reusable procedure."
        elif best[0]>=2:
            decision="UPGRADE"; reason=f"Conservative lexical collision with existing canonical Skill '{best[1]}'; requires validation before readiness."
        else:
            decision="REVIEW_NEW_OR_UPGRADE"; reason="No sufficiently strong canonical match; semantic review and validation required."
        plan.append({**item,"terminal_decision":decision,"canonical_skill":best[1],"reason":reason,"decision_source":"reconciler"})
    summary={}
    for p in plan: summary[p["terminal_decision"]]=summary.get(p["terminal_decision"],0)+1
    OUT.write_text(json.dumps({"schema_version":"canonical-promotion-plan/v1","canonical_repo":"salamou1944/agent-skills","source_queue_generated_at":queue.get("generated_at"),"skill_count":len(skills),"summary":summary,"items":plan},ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"skills":len(skills),"items":len(plan),"summary":summary},sort_keys=True))

if __name__=="__main__": main()
