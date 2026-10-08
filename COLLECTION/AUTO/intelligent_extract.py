#!/usr/bin/env python3
"""High-throughput, incremental Collection harvester.

Design goals:
- derive the account frontier from COLLECTION itself (no hard-coded 5-account ceiling)
- enumerate every public repo of every discovered owner/org
- use GitHub API only for metadata/tree; fetch selected public files from raw.githubusercontent.com
- skip unchanged repositories using pushed_at/revision state
- parallelize account, repo, and file work while keeping bounded worker pools
- preserve provenance; never claim readiness from collection alone
"""
import datetime, hashlib, json, os, re, time, urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

TOKEN = os.environ["GH_TOKEN"]
API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"
ROOT = Path("COLLECTION/AUTO/EXTRACTED")

MAX_FILES = int(os.getenv("COLLECTION_MAX_FILES", "24"))
MAX_BYTES_PER_FILE = int(os.getenv("COLLECTION_MAX_FILE_BYTES", "60000"))
MAX_BYTES_PER_SOURCE = int(os.getenv("COLLECTION_MAX_SOURCE_BYTES", "1000000"))
MAX_WORKERS = int(os.getenv("COLLECTION_WORKERS", "32"))
API_WORKERS = int(os.getenv("COLLECTION_API_WORKERS", "16"))
RAW_WORKERS = int(os.getenv("COLLECTION_RAW_WORKERS", "32"))
_cache = {}

def api(path):
    if path in _cache:
        return _cache[path]
    req = urllib.request.Request(API + path, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "collection-bot"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as ex:
        body = ex.read().decode("utf-8", "replace")
        if ex.code == 403 and "rate limit" in body.lower():
            reset = ex.headers.get("X-RateLimit-Reset")
            remaining = ex.headers.get("X-RateLimit-Remaining")
            for attempt in range(6):
                if remaining == "0" and reset:
                    delay = max(1, min(60, int(reset) - int(time.time()) + 1))
                else:
                    delay = min(30, 2 ** attempt)
                time.sleep(delay)
                try:
                    retry_req = urllib.request.Request(API + path, headers={
                        "Authorization": f"Bearer {TOKEN}",
                        "Accept": "application/vnd.github+json",
                        "X-GitHub-Api-Version": "2022-11-28",
                        "User-Agent": "collection-bot"})
                    with urllib.request.urlopen(retry_req, timeout=30) as resp:
                        data = json.load(resp)
                    _cache[path] = data
                    return data
                except urllib.error.HTTPError as retry_ex:
                    retry_body = retry_ex.read().decode("utf-8", "replace")
                    if retry_ex.code != 403 or "rate limit" not in retry_body.lower():
                        raise RuntimeError(f"github_api_http_{retry_ex.code}:{path}") from retry_ex
            raise RuntimeError(f"github_rate_limit_exhausted_after_backoff:{path}") from ex
        raise RuntimeError(f"github_api_http_{ex.code}:{path}") from ex
    _cache[path] = data
    return data

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

def safe_name(value):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value)

def owner_from_url(url):
    m = re.search(r"https?://github\.com/([^/]+)/?(?:#.*)?$", url.strip())
    return m.group(1) if m else None

def discover_accounts():
    """Build the frontier from Collection account records and INDEX references."""
    owners = set()
    accounts_dir = Path("COLLECTION/ACCOUNTS")
    if accounts_dir.exists():
        for path in accounts_dir.glob("*.md"):
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            # Prefer explicit Account/Source owner URLs, but accept any root GitHub owner URL.
            for line in text.splitlines()[:80]:
                if re.search(r"^\s*(?:Account|Source|Owner|Repository|Official repository):", line, re.I):
                    m = re.search(r"https?://github\.com/([^/\s)]+)", line)
                    if m:
                        owners.add(m.group(1))
    index = Path("COLLECTION/INDEX.md")
    if index.exists():
        text = index.read_text(encoding="utf-8", errors="ignore")
        # Only root account URLs, not repository URLs.
        for m in re.finditer(r"https?://github\.com/([^/\s)]+)(?=[\s)\n]|$)", text):
            owners.add(m.group(1))
    # Keep known operational owners even if their capture record is temporarily absent.
    owners.update({"salamou1944"})
    return sorted(x for x in owners if re.fullmatch(r"[A-Za-z0-9-]+", x))

def discover():
    repos, gists, blocked = {}, {}, []
    accounts = discover_accounts()

    def enumerate_owner(owner):
        encoded = urllib.parse.quote(owner, safe="")
        try:
            identity = api(f"/users/{encoded}")
            kind = "org" if identity.get("type") == "Organization" else "user"
            items = list(paged(
                f"/orgs/{encoded}/repos?type=all" if kind == "org"
                else f"/users/{encoded}/repos?type=all"
            ))
            return owner, items, kind, None
        except RuntimeError as error:
            return owner, [], "unknown", str(error)

    with ThreadPoolExecutor(max_workers=min(API_WORKERS, max(1, len(accounts)))) as ex:
        futures = [ex.submit(enumerate_owner, owner) for owner in accounts]
        for fut in as_completed(futures):
            owner, items, kind, error = fut.result()
            if error:
                blocked.append({"owner": owner, "kind": kind, "error": error})
                continue
            for item in items:
                repos[item["full_name"]] = {
                    "kind": "repo", "full_name": item["full_name"],
                    "owner": owner, "owner_kind": kind
                }
            if kind == "user":
                try:
                    for item in paged(f"/users/{urllib.parse.quote(owner, safe='')}/gists"):
                        gists[item["id"]] = {"kind": "gist", "id": item["id"], "owner": owner}
                except RuntimeError as ex2:
                    blocked.append({"owner": owner, "kind": "gists", "error": str(ex2)})
    return list(repos.values()), list(gists.values()), blocked, accounts

def score(path):
    p = path.lower()
    if any(x in p for x in (".png",".jpg",".jpeg",".gif",".webp",".ico",".mp4",".mov",".zip",".tar",".gz",".woff",".ttf",".lock")):
        return -100
    if any(x in p for x in ("node_modules/","vendor/","dist/","build/","coverage/","__pycache__/",".git/")):
        return -100
    weights = (
        (("readme",),100),(("/docs/","docs/"),70),((".github/workflows/",),95),
        (("dockerfile","compose","pyproject.toml","package.json","go.mod","cargo.toml","requirements.txt","makefile"),85),
        (("install","setup","bootstrap","action"),82),
        (("auth","security","secret","credential","permission","rbac"),80),
        (("api","sdk","mcp","agent","browser","crawl","search","llm","model"),75),
        (("deploy","railway","vercel","terraform","kubernetes","helm","ansible","ci","cd"),72),
        (("test","spec","fixture","mock"),60),
        (("payment","billing","commerce","email","crm","support"),60),
        (("storage","backup","database","postgres","redis","observability","monitor","prometheus","grafana"),60),
        (("retry","backoff","rate-limit","ratelimit","cache","idempot","validation"),58),
    )
    s = 0
    for keys, weight in weights:
        if any(x in p for x in keys):
            s += weight
    if p.endswith((".py",".ts",".tsx",".js",".jsx",".go",".rs",".java",".php",".rb",".sh",".sql",".yaml",".yml",".json",".toml")):
        s += 35
    return s - p.count("/") * 2

def raw_fetch(repo, path, revision):
    url = f"{RAW}/{repo}/{urllib.parse.quote(revision, safe='')}/{urllib.parse.quote(path, safe='/')}"
    req = urllib.request.Request(url, headers={"User-Agent": "collection-bot"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read(MAX_BYTES_PER_FILE + 1)
        if len(raw) > MAX_BYTES_PER_FILE:
            raw = raw[:MAX_BYTES_PER_FILE]
        text = raw.decode("utf-8", "replace")
        return {
            "path": path, "sha": None,
            "content_sha256": hashlib.sha256(raw).hexdigest(),
            "score": score(path), "content": text
        }
    except Exception as ex:
        return {"path": path, "sha": None, "score": score(path), "error": str(ex)}

def extract_repo(item):
    repo = item["full_name"]
    meta = api(f"/repos/{repo}")
    pushed_at = meta.get("pushed_at")
    out = ROOT / f"{safe_name(repo)}.json"
    cached = None
    if out.exists():
        try:
            cached = json.loads(out.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            cached = None
    if cached and cached.get("pushed_at") == pushed_at and cached.get("state") == "extracted":
        return cached, "cached"

    branch = meta["default_branch"]
    branch_data = api(f"/repos/{repo}/branches/{urllib.parse.quote(branch, safe='')}")
    revision = branch_data.get("commit", {}).get("sha")
    tree = api(f"/repos/{repo}/git/trees/{revision}?recursive=1")
    candidates = [
        e for e in tree.get("tree", [])
        if e.get("type") == "blob"
        and e.get("size", 0) <= MAX_BYTES_PER_FILE
        and score(e.get("path", "")) > 0
    ]
    candidates.sort(key=lambda e: (score(e["path"]), -e.get("size", 0)), reverse=True)
    selected = candidates[:MAX_FILES]
    files = []
    with ThreadPoolExecutor(max_workers=min(RAW_WORKERS, max(1, len(selected)))) as ex:
        futures = [ex.submit(raw_fetch, repo, e["path"], revision) for e in selected]
        for fut in as_completed(futures):
            files.append(fut.result())
    files.sort(key=lambda x: x["score"], reverse=True)
    total, bounded = 0, []
    for f in files:
        size = len(f.get("content", "").encode())
        if size and total + size > MAX_BYTES_PER_SOURCE:
            continue
        bounded.append(f)
        total += size
    data = {
        "canonical_source": f"github:{repo}", "repo": repo,
        "revision_sha": revision, "default_branch": branch,
        "pushed_at": pushed_at, "repo_updated_at": meta.get("updated_at"),
        "license": (meta.get("license") or {}).get("spdx_id"),
        "topics": meta.get("topics", []), "tree_truncated": tree.get("truncated", False),
        "state": "extracted",
        "extraction_policy": {
            "max_files": MAX_FILES, "max_file_bytes": MAX_BYTES_PER_FILE,
            "max_source_bytes": MAX_BYTES_PER_SOURCE,
            "raw_fetch": True, "incremental": True
        },
        "files": bounded,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
    return data, "refreshed"

def extract_gist(gid, owner):
    gist = api(f"/gists/{gid}")
    files, total = [], 0
    for name, item in sorted(gist.get("files", {}).items(), key=lambda kv: score(kv[0]), reverse=True):
        if len(files) >= MAX_FILES:
            break
        raw = item.get("content", "")[:MAX_BYTES_PER_FILE]
        size = len(raw.encode())
        if total + size > MAX_BYTES_PER_SOURCE:
            continue
        files.append({
            "path": name, "sha": item.get("raw_url", ""),
            "content_sha256": hashlib.sha256(raw.encode()).hexdigest(),
            "score": score(name), "content": raw
        })
        total += size
    return {
        "canonical_source": f"github-gist:{gid}", "gist_id": gid, "owner": owner,
        "description": gist.get("description"), "state": "extracted",
        "files": files, "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }

def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    repos, gists, blocked, accounts = discover()
    manifest = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "account_count": len(accounts), "accounts": accounts,
        "repo_count": len(repos), "gist_count": len(gists),
        "policy": {
            "max_files_per_source": MAX_FILES, "max_file_bytes": MAX_BYTES_PER_FILE,
            "max_source_bytes": MAX_BYTES_PER_SOURCE,
            "account_frontier": "COLLECTION/ACCOUNTS + COLLECTION/INDEX.md",
            "incremental": True, "raw_public_file_fetch": True
        },
        "sources": [], "blocked": blocked
    }

    jobs = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        for item in repos:
            jobs.append(("repo", item, ex.submit(extract_repo, item)))
        for item in gists:
            jobs.append(("gist", item, ex.submit(extract_gist, item["id"], item["owner"])))
        future_map = {future: (kind, item) for kind, item, future in jobs}
        for future in as_completed(future_map):
            kind, item = future_map[future]
            try:
                data, mode = future.result()
                if kind == "repo":
                    out = ROOT / f"{safe_name(item['full_name'])}.json"
                    record = {
                        "canonical_source": data["canonical_source"], "state": data["state"],
                        "path": str(out), "files_extracted": len(data["files"]),
                        "tree_truncated": data["tree_truncated"], "mode": mode,
                        "revision_sha": data.get("revision_sha")
                    }
                else:
                    out = ROOT / f"gist_{safe_name(item['owner'])}_{item['id']}.json"
                    record = {
                        "canonical_source": data["canonical_source"], "state": data["state"],
                        "path": str(out), "files_extracted": len(data["files"]), "mode": "refreshed"
                    }
                if mode != "cached":
                    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                manifest["sources"].append(record)
            except Exception as ex:
                canonical = f"github:{item['full_name']}" if kind == "repo" else f"github-gist:{item['id']}"
                manifest["sources"].append({
                    "canonical_source": canonical, "state": "BLOCKED_EXTERNAL_ACCESS",
                    "error": str(ex)
                })

    manifest["extracted_sources"] = sum(x["state"] == "extracted" for x in manifest["sources"])
    manifest["cached_sources"] = sum(x.get("mode") == "cached" for x in manifest["sources"])
    manifest["refreshed_sources"] = sum(x.get("mode") == "refreshed" for x in manifest["sources"])
    manifest["blocked_sources"] = sum(x["state"] == "BLOCKED_EXTERNAL_ACCESS" for x in manifest["sources"]) + len(blocked)
    (ROOT / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        k: manifest[k] for k in (
            "account_count","repo_count","gist_count","extracted_sources",
            "cached_sources","refreshed_sources","blocked_sources"
        )
    }, sort_keys=True))

if __name__ == "__main__":
    main()
