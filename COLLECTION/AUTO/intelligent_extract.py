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

TOKEN = os.getenv("GH_TOKEN", "")
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

def atomic_write_json(path, payload):
    """Write each artifact via same-directory replace to avoid truncated cache files."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)


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

def has_usable_files(data):
    """True only when an extracted artifact contains at least one non-empty file."""
    files = data.get("files") if isinstance(data, dict) else None
    return isinstance(files, list) and any(
        isinstance(f, dict) and isinstance(f.get("content"), str) and f["content"]
        for f in files
    )

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
            # Gists are optional enrichment, not a prerequisite for repo collection.
            # They consume the same GitHub API quota and frequently return 403 for
            # fine-grained tokens even when public repositories are readable. Keep the
            # default cycle fast and useful; enable them explicitly when quota permits.
            if kind == "user" and os.getenv("COLLECTION_INCLUDE_GISTS", "0").strip().lower() in {"1", "true", "yes"}:
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
    # A stale artifact marked extracted but containing no usable files must be
    # refreshed even when upstream pushed_at is unchanged.
    if (
        isinstance(cached, dict)
        and cached.get("pushed_at") == pushed_at
        and cached.get("state") == "extracted"
        and has_usable_files(cached)
    ):
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
    fetch_results = []
    with ThreadPoolExecutor(max_workers=min(RAW_WORKERS, max(1, len(selected)))) as ex:
        futures = [ex.submit(raw_fetch, repo, e["path"], revision) for e in selected]
        for fut in as_completed(futures):
            fetch_results.append(fut.result())
    # Failed/empty raw fetches are diagnostics, never extracted evidence.
    fetch_errors = [
        {"path": f.get("path"), "error": f.get("error", "empty content")}
        for f in fetch_results
        if f.get("error") or not f.get("content")
    ]
    files = [f for f in fetch_results if not f.get("error") and f.get("content")]
    files.sort(key=lambda x: x["score"], reverse=True)
    total, bounded = 0, []
    for f in files:
        size = len(f.get("content", "").encode())
        if total + size > MAX_BYTES_PER_SOURCE:
            continue
        bounded.append(f)
        total += size
    if not bounded:
        raise RuntimeError(
            f"raw_file_extraction_empty:{repo}:selected={len(selected)}:errors={len(fetch_errors)}"
        )
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
        "fetch_errors": fetch_errors,
        "fetch_error_count": len(fetch_errors),
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

def load_previous_manifest():
    """Read last source inventory without trusting missing/corrupt artifacts."""
    path = ROOT / "MANIFEST.json"
    if not path.is_file() or path.stat().st_size == 0:
        return []
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    return [item for item in doc.get("sources", []) if isinstance(item, dict)]


def preserved_record(item):
    """Preserve a prior extraction only when its artifact still validates."""
    if item.get("state") != "extracted" or not item.get("path"):
        return None
    path = Path(item["path"])
    if not path.is_absolute():
        path = Path.cwd() / path
    root = ROOT.resolve()
    try:
        resolved = path.resolve()
        if root not in resolved.parents or resolved.name == "MANIFEST.json":
            return None
        data = json.loads(resolved.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict) or data.get("state") != "extracted":
        return None
    if not has_usable_files(data):
        # Do not preserve an empty/stale artifact as extracted. Its bytes stay
        # in the repository for forensics, but it must be retried or marked blocked.
        return None
    if data.get("canonical_source") != item.get("canonical_source"):
        return None
    if item.get("revision_sha") and data.get("revision_sha") != item.get("revision_sha"):
        return None
    kept = dict(item)
    kept["files_extracted"] = sum(
        1 for f in files
        if isinstance(f, dict) and isinstance(f.get("content"), str) and f["content"]
    )
    kept["mode"] = "preserved_after_refresh_failure"
    return kept


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    previous_sources = load_previous_manifest()
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
                    atomic_write_json(out, data)
                manifest["sources"].append(record)
            except Exception as ex:
                canonical = f"github:{item['full_name']}" if kind == "repo" else f"github-gist:{item['id']}"
                previous = next(
                    (record for record in previous_sources if record.get("canonical_source") == canonical),
                    None,
                )
                preserved = preserved_record(previous) if previous else None
                if preserved:
                    # Keep the last validated artifact active while surfacing the
                    # failed refresh separately. A transient API/raw-fetch failure
                    # must not demote usable inventory or erase its provenance.
                    manifest["sources"].append(preserved)
                    manifest["blocked"].append({
                        "canonical_source": canonical,
                        "state": "REFRESH_BLOCKED_PRESERVED_PRIOR",
                        "error": str(ex),
                    })
                else:
                    manifest["sources"].append({
                        "canonical_source": canonical, "state": "BLOCKED_EXTERNAL_ACCESS",
                        "error": str(ex)
                    })

    # Preserve validated prior artifacts missing from this refresh. Temporary
    # API/rate-limit/permission failures must not erase usable Collection inventory.
    current_sources = {x.get("canonical_source"): x for x in manifest["sources"] if x.get("canonical_source")}
    preserved_count = 0
    for previous in previous_sources:
        canonical = previous.get("canonical_source")
        if not canonical or canonical in current_sources:
            continue
        kept = preserved_record(previous)
        if kept:
            manifest["sources"].append(kept)
            current_sources[canonical] = kept
            preserved_count += 1

    manifest["preserved_sources_after_refresh_failure"] = preserved_count
    manifest["extracted_sources"] = sum(x["state"] == "extracted" for x in manifest["sources"])
    manifest["cached_sources"] = sum(x.get("mode") == "cached" for x in manifest["sources"])
    manifest["refreshed_sources"] = sum(x.get("mode") == "refreshed" for x in manifest["sources"])
    manifest["blocked_sources"] = sum(x["state"] == "BLOCKED_EXTERNAL_ACCESS" for x in manifest["sources"]) + len(blocked)
    atomic_write_json(ROOT / "MANIFEST.json", manifest)
    print(json.dumps({
        k: manifest[k] for k in (
            "account_count","repo_count","gist_count","extracted_sources",
            "cached_sources","refreshed_sources","blocked_sources","preserved_sources_after_refresh_failure"
        )
    }, sort_keys=True))

if __name__ == "__main__":
    main()
