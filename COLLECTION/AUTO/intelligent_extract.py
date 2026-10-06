#!/usr/bin/env python3
import base64, datetime, hashlib, json, os, re, urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

TOKEN=os.environ["GH_TOKEN"]
API="https://api.github.com"
ROOT=Path("COLLECTION/AUTO/EXTRACTED")
MAX_FILES=16
MAX_BYTES_PER_FILE=60000
MAX_BYTES_PER_SOURCE=500000
MAX_WORKERS=int(os.getenv("COLLECTION_WORKERS","32"))
API_WORKERS=int(os.getenv("COLLECTION_API_WORKERS","16"))
_cache={}

def api(path):
    if path in _cache:
        return _cache[path]
    req=urllib.request.Request(API+path,headers={
        "Authorization":f"Bearer {TOKEN}",
        "Accept":"application/vnd.github+json",
        "X-GitHub-Api-Version":"2022-11-28",
        "User-Agent":"collection-bot"})
    try:
        with urllib.request.urlopen(req,timeout=30) as resp:
            data=json.load(resp)
    except urllib.error.HTTPError as ex:
        body=ex.read().decode("utf-8","replace")
        if ex.code==403 and "rate limit" in body.lower():
            raise RuntimeError(f"github_rate_limit_exhausted:{path}") from ex
        raise RuntimeError(f"github_api_http_{ex.code}:{path}") from ex
    _cache[path]=data
    return data

def paged(path):
    page=1
    while True:
        sep="&" if "?" in path else "?"
        data=api(f"{path}{sep}per_page=100&page={page}")
        if not data:
            return
        yield from data
        if len(data)<100:
            return
        page+=1

def safe_name(value):
    return re.sub(r"[^A-Za-z0-9_.-]+","_",value)

def score(path):
    p=path.lower()
    if any(x in p for x in (".png",".jpg",".jpeg",".gif",".webp",".ico",".mp4",".mov",".zip",".tar",".gz",".woff",".ttf",".lock")):
        return -100
    if any(x in p for x in ("node_modules/","vendor/","dist/","build/","coverage/","__pycache__/",".git/")):
        return -100
    weights=(
        (("readme",),100),(("/docs/","docs/"),70),((".github/workflows/",),90),
        (("dockerfile","compose","pyproject.toml","package.json","go.mod","cargo.toml","requirements.txt","makefile"),85),
        (("auth","security","secret","credential","permission","rbac"),80),
        (("api","sdk","mcp","agent","browser","crawl","search","llm","model"),75),
        (("deploy","railway","vercel","terraform","kubernetes","helm","ansible","ci","cd"),72),
        (("test","spec"),60),(("payment","billing","commerce","email","crm","support"),60),
        (("storage","backup","database","postgres","redis","observability","monitor","prometheus","grafana"),60))
    s=0
    for keys,weight in weights:
        if any(x in p for x in keys):
            s+=weight
    if p.endswith((".py",".ts",".tsx",".js",".jsx",".go",".rs",".java",".php",".rb",".sh",".sql",".yaml",".yml",".json")):
        s+=35
    return s-p.count("/")*2

def discover():
    repos={}
    gists={}
    for user in ("aw-junaid","mufeedvh","Panniantong","salamou1944"):
        try:
            for item in paged(f"/users/{user}/repos?type=all"):
                repos[item["full_name"]]={"kind":"repo","full_name":item["full_name"]}
        except RuntimeError as ex:
            repos[f"BLOCKED:{user}"]={"kind":"repo","owner":user,"blocked":str(ex)}
    try:
        for item in paged("/orgs/nmap/repos?type=all"):
            repos[item["full_name"]]={"kind":"repo","full_name":item["full_name"]}
    except RuntimeError as ex:
        repos["BLOCKED:nmap"]={"kind":"repo","owner":"nmap","blocked":str(ex)}
    for user in ("aw-junaid","mufeedvh","Panniantong","salamou1944"):
        try:
            for item in paged(f"/users/{user}/gists"):
                gists[item["id"]]={"kind":"gist","id":item["id"],"owner":user}
        except RuntimeError as ex:
            gists[f"BLOCKED:{user}"]={"kind":"gist","owner":user,"blocked":str(ex)}
    return list(repos.values()),list(gists.values())

def fetch_file(args):
    repo,path,branch,entry=args
    try:
        data=api(f"/repos/{repo}/contents/{urllib.parse.quote(path,safe='')}?ref={urllib.parse.quote(branch,safe='')}")
        raw=base64.b64decode(data.get("content","")).decode("utf-8","replace")[:MAX_BYTES_PER_FILE]
        return {"path":path,"sha":entry.get("sha"),"content_sha256":hashlib.sha256(raw.encode()).hexdigest(),"score":score(path),"content":raw}
    except Exception as ex:
        return {"path":path,"sha":entry.get("sha"),"score":score(path),"error":str(ex)}

def extract_repo(repo):
    meta=api(f"/repos/{repo}")
    branch=meta["default_branch"]
    branch_data=api(f"/repos/{repo}/branches/{urllib.parse.quote(branch,safe='')}")
    revision=branch_data.get("commit",{}).get("sha")
    tree=api(f"/repos/{repo}/git/trees/{revision}?recursive=1")
    candidates=[e for e in tree.get("tree",[]) if e.get("type")=="blob" and e.get("size",0)<=MAX_BYTES_PER_FILE and score(e.get("path",""))>0]
    candidates.sort(key=lambda e:(score(e["path"]),-e.get("size",0)),reverse=True)
    selected=candidates[:MAX_FILES]
    files=[]
    with ThreadPoolExecutor(max_workers=min(API_WORKERS,max(1,len(selected)))) as ex:
        futures=[ex.submit(fetch_file,(repo,e["path"],branch,e)) for e in selected]
        for fut in as_completed(futures):
            files.append(fut.result())
    files.sort(key=lambda x:x["score"],reverse=True)
    total=0
    bounded=[]
    for item in files:
        size=len(item.get("content","").encode())
        if size and total+size>MAX_BYTES_PER_SOURCE:
            continue
        bounded.append(item)
        total+=size
    return {"canonical_source":f"github:{repo}","repo":repo,"revision_sha":revision,
            "default_branch":branch,"repo_updated_at":meta.get("updated_at"),
            "license":(meta.get("license") or {}).get("spdx_id"),"topics":meta.get("topics",[]),
            "tree_truncated":tree.get("truncated",False),"state":"extracted",
            "extraction_policy":{"max_files":MAX_FILES,"max_file_bytes":MAX_BYTES_PER_FILE,"max_source_bytes":MAX_BYTES_PER_SOURCE},
            "files":bounded,"generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat()}

def extract_gist(gid,owner):
    gist=api(f"/gists/{gid}")
    files=[]; total=0
    for name,item in sorted(gist.get("files",{}).items(),key=lambda kv:score(kv[0]),reverse=True):
        if len(files)>=MAX_FILES:
            break
        raw=item.get("content","")[:MAX_BYTES_PER_FILE]
        size=len(raw.encode())
        if total+size>MAX_BYTES_PER_SOURCE:
            continue
        files.append({"path":name,"sha":item.get("raw_url",""),"content_sha256":hashlib.sha256(raw.encode()).hexdigest(),"score":score(name),"content":raw})
        total+=size
    return {"canonical_source":f"github-gist:{gid}","gist_id":gid,"owner":owner,"description":gist.get("description"),
            "state":"extracted","files":files,"generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat()}

def main():
    ROOT.mkdir(parents=True,exist_ok=True)
    repos,gists=discover()
    manifest={"generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"repo_count":len(repos),"gist_count":len(gists),
              "policy":{"max_files_per_source":MAX_FILES,"max_file_bytes":MAX_BYTES_PER_FILE,"max_source_bytes":MAX_BYTES_PER_SOURCE},"sources":[]}
    jobs=[]
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        for item in repos:
            if not item.get("blocked"):
                jobs.append(("repo",item,ex.submit(extract_repo,item["full_name"])))
        for item in gists:
            if not item.get("blocked"):
                jobs.append(("gist",item,ex.submit(extract_gist,item["id"],item["owner"])))
        future_map={future:(kind,item) for kind,item,future in jobs}
        for future in as_completed(future_map):
            kind,item=future_map[future]
            try:
                data=future.result()
                if kind=="repo":
                    out=ROOT/f"{safe_name(item['full_name'])}.json"
                    record={"canonical_source":data["canonical_source"],"state":data["state"],"path":str(out),"files_extracted":len(data["files"]),"tree_truncated":data["tree_truncated"]}
                else:
                    out=ROOT/f"gist_{safe_name(item['owner'])}_{item['id']}.json"
                    record={"canonical_source":data["canonical_source"],"state":data["state"],"path":str(out),"files_extracted":len(data["files"])}
                out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
                manifest["sources"].append(record)
            except Exception as ex:
                canonical=f"github:{item['full_name']}" if kind=="repo" else f"github-gist:{item['id']}"
                manifest["sources"].append({"canonical_source":canonical,"state":"BLOCKED_EXTERNAL_ACCESS","error":str(ex)})
    for item in repos:
        if item.get("blocked"):
            manifest["sources"].append({"canonical_source":f"github-repos:{item['owner']}","state":"BLOCKED_EXTERNAL_ACCESS","reason":item["blocked"]})
    for item in gists:
        if item.get("blocked"):
            manifest["sources"].append({"canonical_source":f"github-gists:{item['owner']}","state":"BLOCKED_EXTERNAL_ACCESS","reason":item["blocked"]})
    manifest["extracted_sources"]=sum(x["state"]=="extracted" for x in manifest["sources"])
    manifest["blocked_sources"]=sum(x["state"]=="BLOCKED_EXTERNAL_ACCESS" for x in manifest["sources"])
    (ROOT/"MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:manifest[k] for k in ("repo_count","gist_count","extracted_sources","blocked_sources")}))

if __name__=="__main__":
    main()
