#!/usr/bin/env python3
import base64, datetime, hashlib, json, os, re, urllib.request, urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

TOKEN = os.environ["GH_TOKEN"]
API = "https://api.github.com"
ROOT = Path("COLLECTION/AUTO/EXTRACTED")
MAX_FILES = 8
MAX_BYTES_PER_FILE = 60000
MAX_BYTES_PER_SOURCE = 300000

def api(path):
    req = urllib.request.Request(API + path, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "collection-bot",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def paged(path):
    page = 1
    while True:
        sep = "&" if "?" in path else "?"
        data = api(f"{path}{sep}per_page=100&page={page}")
        if not data:
            return
        for x in data:
            yield x
        if len(data) < 100:
            return
        page += 1

def safe_name(s):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s)

def score(path):
    p = path.lower()
    if any(x in p for x in (".png",".jpg",".jpeg",".gif",".webp",".ico",".mp4",".mov",".zip",".tar",".gz",".woff",".ttf",".lock")):
        return -100
    if any(x in p for x in ("node_modules/","vendor/","dist/","build/","coverage/","__pycache__/",".git/")):
        return -100
    s = 0
    if p.startswith("readme"): s += 100
    if "/docs/" in p or p.startswith("docs/") or p.endswith(".md"): s += 70
    if ".github/workflows/" in p: s += 90
    if any(x in p for x in ("dockerfile","compose","pyproject.toml","package.json","go.mod","cargo.toml","requirements.txt","makefile")): s += 85
    if any(x in p for x in ("auth","security","secret","credential","permission","rbac")): s += 80
    if any(x in p for x in ("api","sdk","mcp","agent","browser","crawl","search","llm","model")): s += 75
    if any(x in p for x in ("deploy","railway","vercel","terraform","kubernetes","helm","ansible","ci","cd")): s += 72
    if any(x in p for x in ("test","spec")): s += 60
    if any(x in p for x in ("payment","billing","commerce","email","crm","support")): s += 60
    if any(x in p for x in ("storage","backup","database","postgres","redis","observability","monitor","prometheus","grafana")): s += 60
    if p.endswith((".py",".ts",".tsx",".js",".jsx",".go",".rs",".java",".php",".rb",".sh",".sql",".yaml",".yml",".json")): s += 35
    depth = p.count("/")
    return s - depth * 2

def discover():
    sources = {}
    for user in ("aw-junaid","mufeedvh","Panniantong","salamou1944"):
        for r in paged(f"/users/{user}/repos?type=all"):
            if not r.get("fork"):
                sources[r["full_name"]] = {"kind":"repo","full_name":r["full_name"]}
    for r in paged("/orgs/nmap/repos?type=all"):
        if not r.get("fork"):
            sources[r["full_name"]] = {"kind":"repo","full_name":r["full_name"]}
    gists = {}
    for user in ("aw-junaid","mufeedvh","Panniantong","salamou1944"):
        for g in paged(f"/users/{user}/gists"):
            gists[g["id"]] = {"kind":"gist","id":g["id"],"owner":user}
    return list(sources.values()), list(gists.values())

def extract_repo(repo):
    meta = api(f"/repos/{repo}")
    branch = meta["default_branch"]
    branch_data = api(f"/repos/{repo}/branches/{urllib.parse.quote(branch, safe='')}")
    revision_sha = branch_data.get("commit",{}).get("sha")
    tree = api(f"/repos/{repo}/git/trees/{revision_sha}?recursive=1")
    entries = tree.get("tree", [])
    candidates = [e for e in entries if e.get("type") == "blob" and e.get("size",0) <= MAX_BYTES_PER_FILE and score(e.get("path","")) > 0]
    candidates.sort(key=lambda e:(score(e["path"]), -e.get("size",0)), reverse=True)
    selected = candidates[:MAX_FILES]
    files=[]; total=0
    for e in selected:
        try:
            d=api(f"/repos/{repo}/contents/{urllib.parse.quote(e['path'], safe='') }?ref={branch}")
            raw=base64.b64decode(d.get("content","")).decode("utf-8","replace")
            raw=raw[:MAX_BYTES_PER_FILE]
            if total+len(raw.encode()) > MAX_BYTES_PER_SOURCE: break
            files.append({
                "path":e["path"], "sha":e.get("sha"), "content_sha256":hashlib.sha256(raw.encode()).hexdigest(),
                "score":score(e["path"]), "content":raw
            })
            total += len(raw.encode())
        except Exception as ex:
            files.append({"path":e["path"],"sha":e.get("sha"),"score":score(e["path"]),"error":str(ex)})
    return {
        "canonical_source": f"github:{repo}",
        "repo": repo,
        "revision_sha": revision_sha,
        "default_branch": branch,
        "repo_updated_at": meta.get("updated_at"),
        "license": (meta.get("license") or {}).get("spdx_id"),
        "topics": meta.get("topics",[]),
        "tree_truncated": tree.get("truncated",False),
        "state": "extracted",
        "extraction_policy": {"max_files":MAX_FILES,"max_file_bytes":MAX_BYTES_PER_FILE,"max_source_bytes":MAX_BYTES_PER_SOURCE},
        "files":files,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }

def extract_gist(gid, owner):
    g=api(f"/gists/{gid}")
    files=[]
    total=0
    for name,f in sorted(g.get("files",{}).items(), key=lambda kv: score(kv[0]), reverse=True):
        if len(files)>=MAX_FILES: break
        raw=f.get("content","")
        raw=raw[:MAX_BYTES_PER_FILE]
        if total+len(raw.encode()) > MAX_BYTES_PER_SOURCE: break
        files.append({
            "path":name, "sha":f.get("raw_url",""), "content_sha256":hashlib.sha256(raw.encode()).hexdigest(),
            "score":score(name), "content":raw
        })
        total += len(raw.encode())
    return {
        "canonical_source":f"github-gist:{gid}",
        "gist_id":gid, "owner":owner, "description":g.get("description"),
        "state":"extracted", "files":files,
        "generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat()
    }

def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    repos,gists=discover()
    manifest={"generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "repo_count":len(repos),"gist_count":len(gists),
              "policy":{"max_files_per_source":MAX_FILES,"max_file_bytes":MAX_BYTES_PER_FILE,"max_source_bytes":MAX_BYTES_PER_SOURCE},
              "sources":[]}
    jobs=[]
    with ThreadPoolExecutor(max_workers=8) as ex:
        for item in repos:
            jobs.append(("repo",item,ex.submit(extract_repo,item["full_name"])))
        for item in gists:
            jobs.append(("gist",item,ex.submit(extract_gist,item["id"],item["owner"])))
        for kind,item,fut in jobs:
            try:
                data=fut.result()
                if kind=="repo":
                    out=ROOT/f"{safe_name(item['full_name'])}.json"
                    record={"canonical_source":data["canonical_source"],"state":data["state"],"path":str(out),
                            "files_extracted":len(data["files"]),"tree_truncated":data["tree_truncated"]}
                else:
                    out=ROOT/f"gist_{safe_name(item['owner'])}_{item['id']}.json"
                    record={"canonical_source":data["canonical_source"],"state":data["state"],"path":str(out),
                            "files_extracted":len(data["files"])}
                out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
                manifest["sources"].append(record)
            except Exception as e:
                canonical=f"github:{item['full_name']}" if kind=="repo" else f"github-gist:{item['id']}"
                manifest["sources"].append({"canonical_source":canonical,"state":"BLOCKED_EXTERNAL_ACCESS","error":str(e)})
    manifest["extracted_sources"]=sum(1 for x in manifest["sources"] if x["state"]=="extracted")
    manifest["blocked_sources"]=sum(1 for x in manifest["sources"] if x["state"]=="BLOCKED_EXTERNAL_ACCESS")
    (ROOT/"MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"repo_count":len(repos),"gist_count":len(gists),
                      "extracted_sources":manifest["extracted_sources"],
                      "blocked_sources":manifest["blocked_sources"]}))

if __name__=="__main__":
    main()
