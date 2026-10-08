#!/usr/bin/env python3
"""Account-wide, high-density extraction with rate-limit-aware public GitHub access.

Stops at dedupe/adaptation handoff. It never claims runtime readiness.
"""
import base64, datetime, hashlib, json, os, re, time, urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

TOKEN = os.environ.get("GH_TOKEN", "")
API = "https://api.github.com"
ACCOUNTS = Path("COLLECTION/ACCOUNTS")
OUT = Path("COLLECTION/AUTO/DEEP-EXTRACTED")
MAX_FILES = int(os.getenv("COLLECTION_DEEP_MAX_FILES", "48"))
MAX_FILE = int(os.getenv("COLLECTION_DEEP_MAX_FILE_BYTES", "100000"))
MAX_REPO = int(os.getenv("COLLECTION_DEEP_MAX_REPO_BYTES", "1500000"))
WORKERS = int(os.getenv("COLLECTION_DEEP_WORKERS", "8"))
API_WORKERS = int(os.getenv("COLLECTION_DEEP_API_WORKERS", "4"))
RETRIES = int(os.getenv("COLLECTION_DEEP_RETRIES", "5"))
CACHE = {}
RESERVED = {"features","topics","search","explore","marketplace","settings","login","signup","about","orgs","users"}
BUCKETS = {
    "readme": ("readme",), "contract": ("schema","openapi","asyncapi","api","sdk","client","adapter","gateway","provider"),
    "agent": ("agent","skill","mcp","tool","prompt","workflow","orchestration"),
    "runtime": ("runtime","server","service","worker","queue","scheduler","browser","computer","sandbox"),
    "security": ("auth","security","permission","policy","rbac","secret","credential","identity"),
    "data": ("dataset","fixture","migration","storage","database","vector","embedding","index"),
    "ops": ("deploy","docker","compose","kubernetes","helm","terraform","railway","vercel","ci","cd","monitor","observability"),
    "eval": ("test","spec","eval","benchmark","regression","quality","e2e"),
    "media": ("video","audio","image","media","caption","subtitle","creative"),
    "docs": ("docs/","documentation","guide","example","sample"),
}

def api(path):
    if path in CACHE:
        return CACHE[path]
    last = None
    for attempt in range(RETRIES):
        headers = {"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"collection-deep-extractor"}
        if TOKEN:
            headers["Authorization"] = f"Bearer {TOKEN}"
        try:
            req = urllib.request.Request(API + path, headers=headers)
            with urllib.request.urlopen(req, timeout=45) as r:
                data = json.load(r)
            CACHE[path] = data
            return data
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in {403, 429, 500, 502, 503, 504}:
                raise
            retry_after = exc.headers.get("Retry-After")
            reset = exc.headers.get("X-RateLimit-Reset")
            if retry_after:
                delay = min(60.0, float(retry_after))
            elif reset and str(reset).isdigit():
                delay = min(60.0, max(1.0, int(reset) - int(time.time()) + 1))
            else:
                delay = min(30.0, 1.5 ** attempt)
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            time.sleep(min(20.0, 1.5 ** attempt))
    raise last

def paged(path):
    page = 1
    while True:
        sep = "&" if "?" in path else "?"
        data = api(f"{path}{sep}per_page=100&page={page}")
        if not data:
            return
        yield from data
        if len(data) < 100:
            return
        page += 1

def redact(s):
    s = re.sub(r"""(?im)([A-Z0-9_]*(?:TOKEN|API[_-]?KEY|SECRET|PASSWORD|PASSWD)[A-Z0-9_]*\s*[:=]\s*["']?)([^\s"']+)""", r"\1<REDACTED>", s)
    return re.sub(r"(?i)(bearer\s+)[A-Za-z0-9._~+/=-]{16,}", r"\1<REDACTED>", s)

def owners():
    out = set()
    for p in ACCOUNTS.glob("*.md"):
        t = p.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"https?://github\.com/([A-Za-z0-9_.-]+)(?:[\s/]|$)", t):
            o = m.group(1)
            if o.lower() not in RESERVED and o.lower() != "salamou1944":
                out.add(o)
    return sorted(out, key=str.lower)

def repos(owner):
    paths = (
        f"/users/{urllib.parse.quote(owner, safe='')}/repos?type=all",
        f"/orgs/{urllib.parse.quote(owner, safe='')}/repos",
    )
    for ep in paths:
        try:
            r = list(paged(ep))
            if r:
                return r
        except Exception:
            continue
    return []

def score(path):
    p = path.lower()
    if any(x in p for x in ("node_modules/","vendor/","dist/","build/","coverage/","__pycache__/")):
        return -999
    if p.endswith((".png",".jpg",".jpeg",".gif",".webp",".mp4",".mov",".zip",".tar",".gz",".woff",".ttf",".lock")):
        return -999
    return sum(70 for terms in BUCKETS.values() if any(x in p for x in terms)) + (25 if p.endswith((".py",".ts",".tsx",".js",".jsx",".go",".rs",".java",".php",".rb",".sh",".sql",".yaml",".yml",".json",".toml",".md")) else 0) - p.count("/")

def bucket(path, body=""):
    x = (path + " " + body[:4000]).lower()
    vals = {k: sum(x.count(t) for t in terms) for k, terms in BUCKETS.items()}
    k = max(vals, key=vals.get)
    return k if vals[k] else "other"

def raw_file(repo, branch, path):
    url = f"https://raw.githubusercontent.com/{repo}/{urllib.parse.quote(branch, safe='')}/{urllib.parse.quote(path, safe='/')}"
    req = urllib.request.Request(url, headers={"User-Agent":"collection-deep-extractor"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read(MAX_FILE + 1)

def content_file(repo, branch, path):
    try:
        return raw_file(repo, branch, path)
    except Exception:
        d = api(f"/repos/{repo}/contents/{urllib.parse.quote(path, safe='')}?ref={urllib.parse.quote(branch, safe='')}")
        return base64.b64decode(d.get("content", ""))

def extract(repo):
    meta = api(f"/repos/{repo}")
    branch = meta["default_branch"]
    rev = api(f"/repos/{repo}/branches/{urllib.parse.quote(branch, safe='')}")["commit"]["sha"]
    tree = api(f"/repos/{repo}/git/trees/{rev}?recursive=1")
    blobs = [e for e in tree.get("tree", []) if e.get("type") == "blob" and e.get("size", 0) <= MAX_FILE and score(e.get("path","")) >= 0]
    blobs.sort(key=lambda e: score(e["path"]), reverse=True)
    selected, seen = [], set()
    quota = {k: 6 for k in BUCKETS}
    for e in blobs:
        b = bucket(e["path"])
        if b in quota and quota[b] and e["path"] not in seen:
            selected.append(e); seen.add(e["path"]); quota[b] -= 1
    for e in blobs:
        if len(selected) >= MAX_FILES:
            break
        if e["path"] not in seen:
            selected.append(e); seen.add(e["path"])

    def one(e):
        raw = content_file(repo, branch, e["path"])
        raw = raw[:MAX_FILE]
        text = redact(raw.decode("utf-8", "replace"))
        return {"path":e["path"],"sha":e.get("sha"),"bucket":bucket(e["path"], text),
                "content_sha256":hashlib.sha256(text.encode()).hexdigest(),"content":text}

    files, total = [], 0
    with ThreadPoolExecutor(max_workers=min(API_WORKERS, max(1, len(selected)))) as ex:
        for fut in as_completed([ex.submit(one, e) for e in selected]):
            x = fut.result()
            n = len(x["content"].encode())
            if total + n <= MAX_REPO:
                files.append(x); total += n
    return {
        "canonical_source": f"github:{repo}", "repo":repo, "revision_sha":rev,
        "default_branch":branch, "license":(meta.get("license") or {}).get("spdx_id"),
        "description":meta.get("description"), "topics":meta.get("topics",[]),
        "tree_truncated":tree.get("truncated",False), "files":files,
        "policy":{"max_files":MAX_FILES,"max_file_bytes":MAX_FILE,"max_repo_bytes":MAX_REPO}
    }

def packet(d, f):
    eid = hashlib.sha256(f"{d['canonical_source']}|{d['revision_sha']}|{f['path']}|{f.get('sha','')}".encode()).hexdigest()[:20]
    return {"extraction_id":eid,"source":d["canonical_source"],"source_revision":d["revision_sha"],
            "source_license":d.get("license"),"file":f["path"],"asset_type":f["bucket"],
            "content_sha256":f["content_sha256"],"handoff_status":"READY_FOR_DEDUPE",
            "readiness_state":"ON_SHELF",
            "reuse_boundary":"extract narrow implementation pattern/contract; do not wholesale-copy source",
            "evidence_excerpt":f["content"][:700].replace("\n"," ")}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    os_ = owners()
    rs = {}
    for o in os_:
        for r in repos(o):
            if not r.get("archived", False):
                rs[r["full_name"]] = r
    manifest = {"schema_version":"collection-deep-extraction/v1",
                "generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "owners":os_, "repo_count":len(rs), "repos":[]}
    packets = []
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        jobs = {ex.submit(extract, repo):repo for repo in rs}
        for fut in as_completed(jobs):
            repo = jobs[fut]
            try:
                d = fut.result()
                out = OUT / (repo.replace("/","__") + ".json")
                d["generated_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
                out.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                manifest["repos"].append({"repo":repo,"revision_sha":d["revision_sha"],"files":len(d["files"]),"path":str(out)})
                packets.extend(packet(d, f) for f in d["files"])
            except Exception as e:
                manifest["repos"].append({"repo":repo,"state":"BLOCKED_EXTERNAL_ACCESS","error":str(e)})
    manifest["packet_count"] = len(packets)
    manifest["asset_type_counts"] = {}
    for p in packets:
        manifest["asset_type_counts"][p["asset_type"]] = manifest["asset_type_counts"].get(p["asset_type"], 0) + 1
    (OUT/"MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT/"EXTRACTION-READY-QUEUE.json").write_text(json.dumps(
        {"schema_version":"collection-extraction-ready/v1",
         "rule":"ready for canonical dedupe/adaptation, never runtime readiness",
         "items":packets}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"owners":len(os_), "repos":len(rs), "packets":len(packets),
                      "asset_types":manifest["asset_type_counts"]}, sort_keys=True))

if __name__ == "__main__":
    main()
