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
MAX_FILES = int(os.getenv("COLLECTION_DEEP_MAX_FILES", "24"))
MAX_FILE = int(os.getenv("COLLECTION_DEEP_MAX_FILE_BYTES", "50000"))
MAX_REPO = int(os.getenv("COLLECTION_DEEP_MAX_REPO_BYTES", "300000"))
MAX_DEEP_REPOS = int(os.getenv("COLLECTION_DEEP_MAX_REPOS", "200"))
MAX_DEEP_REPOS_PER_OWNER = int(os.getenv("COLLECTION_DEEP_MAX_REPOS_PER_OWNER", "2"))
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

def _http_error_message(exc):
    """Read a GitHub error body once and return a short, non-secret diagnostic."""
    try:
        body = exc.read().decode("utf-8", "replace")
    except Exception:
        body = ""
    try:
        parsed = json.loads(body)
        message = parsed.get("message", body) if isinstance(parsed, dict) else body
    except (ValueError, TypeError):
        message = body
    message = re.sub(r"(?i)bearer\s+[A-Za-z0-9._~+/=-]{12,}", "Bearer <REDACTED>", str(message))
    return message.strip().replace("\n", " ")[:300]


def _retryable_http_error(exc, message):
    """Retry only transient server/rate-limit responses, not ordinary permission 403s."""
    if exc.code == 429 or exc.code in {500, 502, 503, 504}:
        return True
    if exc.code != 403:
        return False
    remaining = exc.headers.get("X-RateLimit-Remaining", "")
    text = message.lower()
    return remaining == "0" or any(
        marker in text for marker in ("rate limit", "secondary rate limit", "abuse detection")
    )


def _http_error_summary(exc, path, message):
    request_id = exc.headers.get("X-GitHub-Request-Id", "unknown")
    remaining = exc.headers.get("X-RateLimit-Remaining", "unknown")
    reset = exc.headers.get("X-RateLimit-Reset", "unknown")
    return (f"github_api_http_{exc.code}:{path}:message={message or 'no_message'}:"
            f"request_id={request_id}:rate_remaining={remaining}:rate_reset={reset}")


def api(path):
    if path in CACHE:
        return CACHE[path]
    last = None
    attempts = max(1, RETRIES)
    for attempt in range(attempts):
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
            message = _http_error_message(exc)
            summary = _http_error_summary(exc, path, message)
            if not _retryable_http_error(exc, message):
                raise RuntimeError(summary) from exc
            last = RuntimeError(summary)
            if attempt + 1 >= attempts:
                break
            retry_after = exc.headers.get("Retry-After")
            reset = exc.headers.get("X-RateLimit-Reset")
            remaining = exc.headers.get("X-RateLimit-Remaining")
            if retry_after:
                try:
                    delay = max(0.0, float(retry_after))
                except ValueError:
                    delay = min(30.0, 1.5 ** attempt)
            elif remaining == "0" and reset and str(reset).isdigit():
                delay = max(1.0, int(reset) - int(time.time()) + 1)
            else:
                delay = min(30.0, 1.5 ** attempt)
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            if attempt + 1 >= attempts:
                break
            time.sleep(min(20.0, 1.5 ** attempt))
    if isinstance(last, RuntimeError):
        raise RuntimeError(f"github_api_retry_exhausted:{path}:{last}") from last
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
    # GitHub logins are case-insensitive. Canonicalize keys so mixed-case links
    # across old account captures do not trigger duplicate owner-wide sweeps.
    out = {}
    for p in sorted(ACCOUNTS.glob("*.md")):
        t = p.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r"https?://github\.com/([A-Za-z0-9_.-]+)(?=[^A-Za-z0-9_.-]|$)", t):
            o = m.group(1).rstrip(".,;:!?)")
            key = o.lower()
            if key not in RESERVED and key != "salamou1944":
                out.setdefault(key, o)
    return sorted(out.values(), key=str.lower)
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

def raw_file(repo, revision, path):
    """Fetch content pinned to the exact commit used to enumerate the tree."""
    url = f"https://raw.githubusercontent.com/{repo}/{urllib.parse.quote(revision, safe='')}/{urllib.parse.quote(path, safe='/')}"
    req = urllib.request.Request(url, headers={"User-Agent":"collection-deep-extractor"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read(MAX_FILE + 1)

def content_file(repo, revision, path):
    """Use the same immutable revision for raw and Contents API fallback reads."""
    try:
        return raw_file(repo, revision, path)
    except Exception:
        d = api(f"/repos/{repo}/contents/{urllib.parse.quote(path, safe='')}?ref={urllib.parse.quote(revision, safe='')}")
        return base64.b64decode(d.get("content", ""))

def extract(repo, meta=None):
    meta = meta or api(f"/repos/{repo}")
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
        raw = content_file(repo, rev, e["path"])
        raw = raw[:MAX_FILE]
        text = redact(raw.decode("utf-8", "replace"))
        return {"path":e["path"],"sha":e.get("sha"),"bucket":bucket(e["path"], text),
                "content_sha256":hashlib.sha256(text.encode()).hexdigest(),"content":text}

    # Fetch concurrently, then apply the byte budget in deterministic relevance order.
    fetched = {}
    with ThreadPoolExecutor(max_workers=min(API_WORKERS, max(1, len(selected)))) as ex:
        futures = {ex.submit(one, e): e["path"] for e in selected}
        for fut in as_completed(futures):
            fetched[futures[fut]] = fut.result()
    files, total = [], 0
    for e in selected:
        x = fetched.get(e["path"])
        if x is None:
            continue
        n = len(x["content"].encode())
        if total + n <= MAX_REPO:
            files.append(x); total += n
    return {
        "canonical_source": f"github:{repo}", "repo":repo, "revision_sha":rev,
        "default_branch":branch, "license":(meta.get("license") or {}).get("spdx_id"),
        "description":meta.get("description"), "topics":meta.get("topics",[]),
        "source_pushed_at":meta.get("pushed_at"), "source_updated_at":meta.get("updated_at"),
        "stargazers_count":meta.get("stargazers_count",0), "size_kb":meta.get("size",0),
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

def atomic_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp, path)

def repo_priority(meta, now=None):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    owner = (meta.get("owner") or {}).get("login", "")
    topics = meta.get("topics") or []
    text = " ".join([meta.get("full_name", ""), owner, meta.get("name", ""),
                     meta.get("description") or "", " ".join(topics),
                     meta.get("language") or ""]).lower()
    weights = {
        "agent": 6, "skill": 6, "mcp": 6, "api": 5, "provider": 5,
        "gateway": 5, "llm": 5, "model": 4, "inference": 5, "browser": 5,
        "sandbox": 5, "workflow": 4, "automation": 4, "openapi": 5,
        "sdk": 3, "security": 4, "auth": 3, "database": 4, "storage": 4,
        "vector": 3, "embedding": 3, "rag": 3, "prompt": 4, "ollama": 5,
        "gemini": 4, "free": 3, "eval": 3, "benchmark": 3, "image": 3,
        "video": 3, "audio": 3, "creative": 4, "deploy": 2, "server": 2,
        "runtime": 4, "cli": 3, "collection": 3, "orchestration": 4,
        "research": 2, "dataset": 2, "memory": 3, "computer-use": 4,
    }
    score_value = sum(weight for term, weight in weights.items() if term in text)
    stars = max(0, int(meta.get("stargazers_count") or 0))
    score_value += min(10, stars.bit_length())
    if (meta.get("license") or {}).get("spdx_id"):
        score_value += 2
    if not meta.get("fork"):
        score_value += 1
    updated = meta.get("pushed_at") or meta.get("updated_at")
    try:
        stamp = datetime.datetime.fromisoformat(updated.replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            stamp = stamp.replace(tzinfo=datetime.timezone.utc)
        age_days = max(0, (now - stamp).days)
        score_value += 10 if age_days <= 30 else 6 if age_days <= 180 else 3 if age_days <= 365 else 0
    except (AttributeError, TypeError, ValueError):
        pass
    return score_value


def select_deep_batch(repo_metadata, existing_rows, now=None):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    refresh_existing = os.getenv("COLLECTION_DEEP_REFRESH_EXISTING", "false").lower() in {"1", "true", "yes"}
    candidates_by_owner = {}
    scores = {}
    for repo, meta in repo_metadata.items():
        scores[repo] = repo_priority(meta, now)
        if meta.get("archived", False):
            continue
        prior = existing_rows.get(repo)
        pushed = meta.get("pushed_at") or meta.get("updated_at")
        is_new = prior is None or not prior.get("revision_sha")
        is_stale = bool(prior and prior.get("source_pushed_at") and pushed and prior.get("source_pushed_at") != pushed)
        if not (is_new or is_stale or refresh_existing):
            continue
        owner = (meta.get("owner") or {}).get("login") or repo.split("/", 1)[0]
        candidates_by_owner.setdefault(owner, []).append(repo)

    for owner, names in candidates_by_owner.items():
        names.sort(key=lambda repo: (
            scores[repo],
            int(repo_metadata[repo].get("stargazers_count") or 0),
            repo_metadata[repo].get("pushed_at") or repo_metadata[repo].get("updated_at") or "",
            repo.lower(),
        ), reverse=True)
    owner_order = sorted(
        candidates_by_owner,
        key=lambda owner: (max(scores[r] for r in candidates_by_owner[owner]), owner.lower()),
        reverse=True,
    )
    selected = []
    if MAX_DEEP_REPOS <= 0 or MAX_DEEP_REPOS_PER_OWNER <= 0:
        return selected, scores
    for rank in range(MAX_DEEP_REPOS_PER_OWNER):
        for owner in owner_order:
            names = candidates_by_owner[owner]
            if rank < len(names):
                selected.append(names[rank])
                if len(selected) >= MAX_DEEP_REPOS:
                    return selected, scores
    return selected, scores


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    previous = {}
    manifest_path = OUT / "MANIFEST.json"
    if manifest_path.exists():
        try:
            prior = json.loads(manifest_path.read_text(encoding="utf-8"))
            for row in prior.get("repos", []):
                if isinstance(row, dict) and row.get("repo"):
                    previous[row["repo"]] = row
        except (OSError, ValueError):
            raise SystemExit("existing deep-extraction manifest is invalid; refusing destructive refresh")

    owner_list = owners()
    repo_metadata = {}
    owner_errors = {}
    for owner in owner_list:
        discovered = False
        errors = []
        for endpoint in (f"/users/{urllib.parse.quote(owner, safe='')}/repos?type=all",
                         f"/orgs/{urllib.parse.quote(owner, safe='')}/repos"):
            try:
                found = list(paged(endpoint))
                if found:
                    discovered = True
                    for repo_meta in found:
                        if repo_meta.get("full_name"):
                            repo_metadata[repo_meta["full_name"]] = repo_meta
                    break
            except Exception as exc:
                errors.append(str(exc))
        if not discovered and errors:
            owner_errors[owner] = errors[-1]

    rows = {}
    # Preserve the latest successful packet when a source refresh is blocked or deferred.
    for repo, row in previous.items():
        packet_path = OUT / (repo.replace("/", "__") + ".json")
        if packet_path.is_file() and row.get("revision_sha"):
            try:
                packet_doc = json.loads(packet_path.read_text(encoding="utf-8"))
                if packet_doc.get("repo") == repo and packet_doc.get("revision_sha") == row.get("revision_sha"):
                    rows[repo] = row
            except (OSError, ValueError):
                pass

    now = datetime.datetime.now(datetime.timezone.utc)
    selected_names, priority_scores = select_deep_batch(repo_metadata, rows, now)
    selected_set = set(selected_names)
    failures = []
    blocked_repos = set()
    successful_this_run = set()
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        jobs = {ex.submit(extract, repo, repo_metadata[repo]): repo for repo in selected_names}
        for fut in as_completed(jobs):
            repo = jobs[fut]
            try:
                packet_doc = fut.result()
                out = OUT / (repo.replace("/", "__") + ".json")
                packet_doc["generated_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
                atomic_json(out, packet_doc)
                rows[repo] = {
                    "repo": repo, "revision_sha": packet_doc["revision_sha"],
                    "files": len(packet_doc["files"]), "path": str(out),
                    "source_pushed_at": packet_doc.get("source_pushed_at"),
                    "priority_score": priority_scores.get(repo, 0),
                }
                successful_this_run.add(repo)
            except Exception as exc:
                blocked_repos.add(repo)
                failures.append({"repo": repo, "state": "BLOCKED_EXTERNAL_ACCESS", "error": str(exc)})
                if repo not in rows:
                    rows[repo] = {"repo": repo, "state": "BLOCKED_EXTERNAL_ACCESS", "error": str(exc)}

    for owner, error in owner_errors.items():
        failures.append({"owner": owner, "state": "OWNER_DISCOVERY_BLOCKED", "error": error})

    inventory_rows = []
    for repo, meta in sorted(repo_metadata.items()):
        owner = (meta.get("owner") or {}).get("login") or repo.split("/", 1)[0]
        prior = rows.get(repo) or previous.get(repo) or {}
        pushed = meta.get("pushed_at") or meta.get("updated_at")
        stale_packet = bool(prior.get("source_pushed_at") and pushed and prior.get("source_pushed_at") != pushed)
        if repo in blocked_repos:
            state = "BLOCKED_EXTERNAL_ACCESS"
        elif meta.get("archived", False):
            state = "ARCHIVED_METADATA_ONLY"
        elif repo in selected_set:
            state = "SELECTED_FOR_DEEP_EXTRACTION"
        elif repo in rows and not stale_packet:
            state = "SOURCE_PACKET_PRESERVED"
        elif repo in rows and stale_packet:
            state = "DEFERRED_REFRESH"
        else:
            state = "DEFERRED_BY_BUDGET"
        inventory_rows.append({
            "repo": repo, "owner": owner, "name": meta.get("name"),
            "html_url": meta.get("html_url"), "description": meta.get("description"),
            "topics": meta.get("topics") or [], "language": meta.get("language"),
            "license_spdx_id": (meta.get("license") or {}).get("spdx_id"),
            "stargazers_count": meta.get("stargazers_count", 0),
            "forks_count": meta.get("forks_count", 0), "size_kb": meta.get("size", 0),
            "updated_at": meta.get("updated_at"), "pushed_at": meta.get("pushed_at"),
            "default_branch": meta.get("default_branch"), "archived": bool(meta.get("archived", False)),
            "fork": bool(meta.get("fork", False)), "priority_score": priority_scores.get(repo, 0),
            "deep_extraction_state": state,
        })

    inventory_path = OUT / "REPO-INVENTORY.json"
    inventory_payload = {
        "schema_version": "collection-repo-inventory/v1",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "owner_count": len(owner_list), "repo_count": len(inventory_rows),
        "deep_extraction_budget": {
            "max_repos_per_run": MAX_DEEP_REPOS, "max_repos_per_owner": MAX_DEEP_REPOS_PER_OWNER,
            "max_files_per_repo": MAX_FILES, "max_file_bytes": MAX_FILE, "max_source_bytes_per_repo": MAX_REPO,
        },
        "rows": inventory_rows,
    }
    atomic_json(inventory_path, inventory_payload)
    deferred_rows = [row for row in inventory_rows if row["deep_extraction_state"] in {
        "DEFERRED_BY_BUDGET", "DEFERRED_REFRESH", "BLOCKED_EXTERNAL_ACCESS"
    }]
    deferred_path = OUT / "DEFERRED-REPOSITORY-QUEUE.json"
    atomic_json(deferred_path, {
        "schema_version": "collection-deferred-repositories/v1",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "rule": "Metadata for every discovered repository is preserved; deep source packets are processed in bounded, prioritized batches.",
        "deferred_count": len(deferred_rows), "items": deferred_rows,
    })

    packets = []
    valid_packet_repos = set()
    for repo, row in sorted(rows.items()):
        packet_path = OUT / (repo.replace("/", "__") + ".json")
        if not packet_path.is_file():
            continue
        try:
            packet_doc = json.loads(packet_path.read_text(encoding="utf-8"))
            if packet_doc.get("repo") != repo or not packet_doc.get("revision_sha") or packet_doc.get("revision_sha") != row.get("revision_sha"):
                continue
            valid_packet_repos.add(repo)
            packets.extend(packet(packet_doc, file_row) for file_row in packet_doc.get("files", []))
        except (OSError, ValueError):
            continue

    manifest = {
        "schema_version": "collection-deep-extraction/v1",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "owners": owner_list, "repo_count": len(valid_packet_repos), "manifest_repo_row_count": len(rows),
        "inventory_repo_count": len(inventory_rows), "packet_repo_count": len(valid_packet_repos),
        "selected_for_deep_extraction": len(selected_names), "deep_extracted_this_run": len(successful_this_run),
        "blocked_selected_count": len(blocked_repos), "deferred_repo_count": len(deferred_rows),
        "archived_repo_count": sum(1 for row in inventory_rows if row["deep_extraction_state"] == "ARCHIVED_METADATA_ONLY"),
        "deep_extraction_budget": {
            "max_repos_per_run": MAX_DEEP_REPOS, "max_repos_per_owner": MAX_DEEP_REPOS_PER_OWNER,
            "max_files_per_repo": MAX_FILES, "max_file_bytes": MAX_FILE, "max_source_bytes_per_repo": MAX_REPO,
        },
        "repo_inventory_path": str(inventory_path), "deferred_queue_path": str(deferred_path),
        "owner_discovery_errors": owner_errors, "refresh_failures": failures,
        "packet_count": len(packets), "asset_type_counts": {},
    }
    manifest["repo_inventory_sha256"] = hashlib.sha256(inventory_path.read_bytes()).hexdigest()
    manifest["deferred_queue_sha256"] = hashlib.sha256(deferred_path.read_bytes()).hexdigest()
    for item in packets:
        manifest["asset_type_counts"][item["asset_type"]] = manifest["asset_type_counts"].get(item["asset_type"], 0) + 1
    atomic_json(manifest_path, manifest)
    atomic_json(OUT / "EXTRACTION-READY-QUEUE.json", {
        "schema_version": "collection-extraction-ready/v1",
        "rule": "ready for canonical dedupe/adaptation, never runtime readiness",
        "items": packets,
    })
    print(json.dumps({
        "owners": len(owner_list), "discovered_repos": len(inventory_rows),
        "selected_for_deep_extraction": len(selected_names),
        "deferred_repos": len(deferred_rows),
        "archived_repos": manifest["archived_repo_count"],
        "retained_packet_repos": len(valid_packet_repos), "manifest_repo_rows": len(rows),
        "successful_extractions_this_run": len(successful_this_run), "blocked_selected_repos": len(blocked_repos),
        "refresh_failures": len(failures),
        "packets": len(packets), "asset_types": manifest["asset_type_counts"],
    }, sort_keys=True))

if __name__ == "__main__":
    main()
