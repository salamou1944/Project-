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
MAX_BYTES_PER_SOURCE = int(os.getenv("COLLECTION_MAX_SOURCE_BYTES", "300000"))
MAX_WORKERS = int(os.getenv("COLLECTION_WORKERS", "8"))
API_WORKERS = int(os.getenv("COLLECTION_API_WORKERS", "8"))
RAW_WORKERS = int(os.getenv("COLLECTION_RAW_WORKERS", "12"))
MAX_REPOS_PER_RUN = int(os.getenv("COLLECTION_MAX_REPOS_PER_RUN", "100"))
MAX_REPOS_PER_OWNER = int(os.getenv("COLLECTION_MAX_REPOS_PER_OWNER", "1"))
MAX_GISTS_PER_RUN = int(os.getenv("COLLECTION_MAX_GISTS_PER_RUN", "25"))
DEEP_ROOT = Path("COLLECTION/AUTO/DEEP-EXTRACTED")
FRONTIER_META = {}
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
        isinstance(f, dict)
        and not f.get("error")
        and isinstance(f.get("content"), str)
        and f["content"]
        for f in files
    )

def safe_name(value):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value)


def archive_prior_revision(out, cached, new_data, history_root=None):
    """Preserve a validated prior snapshot before replacing it with a newer revision."""
    if not isinstance(cached, dict) or cached.get("state") != "extracted" or not has_usable_files(cached):
        return None
    old_revision = cached.get("revision_sha")
    new_revision = new_data.get("revision_sha") if isinstance(new_data, dict) else None
    if not isinstance(old_revision, str) or not old_revision or old_revision == new_revision:
        return None
    history_root = Path(history_root) if history_root is not None else ROOT / "HISTORY"
    identity = safe_name(cached.get("repo") or Path(out).stem)
    archive_path = history_root / f"{identity}__{safe_name(old_revision)}.json"
    if not archive_path.exists():
        atomic_write_json(archive_path, cached)
    return str(archive_path)

def owner_from_url(url):
    m = re.search(r"https?://github\.com/([^/]+)/?(?:#.*)?$", url.strip())
    return m.group(1) if m else None

def discover_accounts(root=Path(".")):
    """Discover root owner URLs from all Markdown lines, deduplicated case-insensitively."""
    owner_keys = set()
    pattern = re.compile(r"https?://github\.com/([A-Za-z0-9-]+)(?=[\s)\],.;:\n]|$)", re.I)
    accounts_dir = Path(root) / "COLLECTION" / "ACCOUNTS"
    if accounts_dir.exists():
        for path in accounts_dir.glob("*.md"):
            try:
                content = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for match in pattern.finditer(content):
                owner_keys.add(match.group(1).lower())
    index = Path(root) / "COLLECTION" / "INDEX.md"
    if index.exists():
        try:
            content = index.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            content = ""
        for match in pattern.finditer(content):
            owner_keys.add(match.group(1).lower())
    owner_keys.add("salamou1944")
    return sorted(owner for owner in owner_keys if re.fullmatch(r"[a-z0-9-]+", owner))


def load_deep_inventory(inventory_path=None, manifest_path=None):
    """Reuse the completed deep-extraction inventory instead of re-enumerating every owner."""
    inventory_path = Path(inventory_path or (DEEP_ROOT / "REPO-INVENTORY.json"))
    manifest_path = Path(manifest_path or (DEEP_ROOT / "MANIFEST.json"))
    if not inventory_path.is_file() or not manifest_path.is_file():
        return None
    try:
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        deep_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise RuntimeError(f"deep_inventory_invalid:{exc}") from exc
    if inventory.get("schema_version") != "collection-repo-inventory/v1":
        raise RuntimeError("deep_inventory_schema_mismatch")
    rows = inventory.get("rows")
    if not isinstance(rows, list):
        raise RuntimeError("deep_inventory_rows_missing")
    accounts = deep_manifest.get("owners", [])
    if not rows and accounts:
        raise RuntimeError("deep_inventory_contains_no_repositories")
    if not isinstance(accounts, list):
        raise RuntimeError("deep_manifest_owners_invalid")
    repos = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        full_name = row.get("repo")
        if not isinstance(full_name, str) or full_name.count("/") != 1:
            continue
        owner = (row.get("owner") or full_name.split("/", 1)[0]).lower()
        license_spdx = row.get("license_spdx_id")
        meta = {
            "full_name": full_name, "name": row.get("name") or full_name.split("/", 1)[1],
            "owner": {"login": owner}, "html_url": row.get("html_url") or f"https://github.com/{full_name}",
            "description": row.get("description"), "topics": row.get("topics") or [],
            "language": row.get("language"), "license": {"spdx_id": license_spdx} if license_spdx else None,
            "stargazers_count": row.get("stargazers_count", 0), "forks_count": row.get("forks_count", 0),
            "size": row.get("size_kb", 0), "updated_at": row.get("updated_at"),
            "pushed_at": row.get("pushed_at"), "default_branch": row.get("default_branch"),
            "archived": bool(row.get("archived", False)), "fork": bool(row.get("fork", False)),
            "priority_score": row.get("priority_score", 0),
        }
        repos.append({"kind": "repo", "full_name": full_name, "owner": owner, "owner_kind": "unknown", "repo_meta": meta})
    if not accounts:
        accounts = sorted({item["owner"] for item in repos} | {"salamou1944"})
    blocked = [
        {"owner": owner, "kind": "owner_inventory", "error": error}
        for owner, error in (deep_manifest.get("owner_discovery_errors") or {}).items()
    ]
    global FRONTIER_META
    FRONTIER_META = {
        "path": str(inventory_path), "sha256": hashlib.sha256(inventory_path.read_bytes()).hexdigest(),
        "inventory_repo_count": len(repos),
        "deep_manifest_path": str(manifest_path),
        "deep_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "upstream_refresh_failures": deep_manifest.get("refresh_failures", []),
    }
    return repos, [], blocked, sorted({str(owner).lower() for owner in accounts})


def discover():
    """Prefer the completed deep inventory; only use live enumeration for standalone runs."""
    global FRONTIER_META
    FRONTIER_META = {}
    try:
        inventory_result = load_deep_inventory()
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc
    if inventory_result is not None:
        return inventory_result
    require_inventory = os.getenv("COLLECTION_REQUIRE_DEEP_INVENTORY", "false").strip().lower() in {"1", "true", "yes"}
    if require_inventory:
        raise SystemExit("deep repository inventory is missing; run the bounded deep-extraction workflow first")

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
                    "owner": owner.lower(), "owner_kind": kind,
                    "repo_meta": {
                        "full_name": item.get("full_name"), "name": item.get("name"),
                        "owner": item.get("owner"), "html_url": item.get("html_url"),
                        "description": item.get("description"), "language": item.get("language"),
                        "stargazers_count": item.get("stargazers_count", 0), "forks_count": item.get("forks_count", 0),
                        "size": item.get("size", 0), "archived": item.get("archived", False),
                        "fork": item.get("fork", False), "pushed_at": item.get("pushed_at"),
                        "default_branch": item.get("default_branch"), "updated_at": item.get("updated_at"),
                        "license": item.get("license"), "topics": item.get("topics", []),
                    },
                }
            if kind == "user" and os.getenv("COLLECTION_INCLUDE_GISTS", "0").strip().lower() in {"1", "true", "yes"}:
                try:
                    for item in paged(f"/users/{urllib.parse.quote(owner, safe='')}/gists"):
                        gists[item["id"]] = {"kind": "gist", "id": item["id"], "owner": owner}
                except RuntimeError as ex2:
                    blocked.append({"owner": owner, "kind": "gists", "error": str(ex2)})
    FRONTIER_META = {"path": None, "sha256": None, "inventory_repo_count": len(repos), "upstream_refresh_failures": []}
    return list(repos.values()), list(gists.values()), blocked, accounts


def repo_priority(item, now=None):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    meta = item.get("repo_meta") or {}
    supplied = meta.get("priority_score")
    if isinstance(supplied, int) and supplied > 0:
        return supplied
    topics = meta.get("topics") or []
    text = " ".join([item.get("full_name", ""), meta.get("description") or "",
                     " ".join(topics), meta.get("language") or ""]).lower()
    weights = {
        "agent": 6, "skill": 6, "mcp": 6, "api": 5, "provider": 5, "gateway": 5,
        "llm": 5, "model": 4, "inference": 5, "browser": 5, "sandbox": 5,
        "workflow": 4, "automation": 4, "openapi": 5, "sdk": 3, "security": 4,
        "auth": 3, "database": 4, "storage": 4, "vector": 3, "embedding": 3,
        "rag": 3, "prompt": 4, "ollama": 5, "gemini": 4, "free": 3,
        "eval": 3, "benchmark": 3, "image": 3, "video": 3, "audio": 3,
        "creative": 4, "deploy": 2, "server": 2, "runtime": 4, "cli": 3,
        "collection": 3, "orchestration": 4, "research": 2, "dataset": 2,
        "memory": 3, "computer-use": 4,
    }
    result = sum(weight for term, weight in weights.items() if term in text)
    stars = max(0, int(meta.get("stargazers_count") or 0))
    result += min(10, stars.bit_length())
    if (meta.get("license") or {}).get("spdx_id"):
        result += 2
    if not meta.get("fork"):
        result += 1
    updated = meta.get("pushed_at") or meta.get("updated_at")
    try:
        stamp = datetime.datetime.fromisoformat(updated.replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            stamp = stamp.replace(tzinfo=datetime.timezone.utc)
        age_days = max(0, (now - stamp).days)
        result += 10 if age_days <= 30 else 6 if age_days <= 180 else 3 if age_days <= 365 else 0
    except (AttributeError, TypeError, ValueError):
        pass
    return result


def load_deep_extracted_names(deep_root=None):
    deep_root = Path(deep_root or DEEP_ROOT)
    manifest_path = deep_root / "MANIFEST.json"
    if not manifest_path.is_file():
        return set()
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        raise RuntimeError("deep extraction manifest is invalid")
    names = set()
    for row in manifest.get("repos", []):
        if not isinstance(row, dict) or not row.get("repo") or not row.get("revision_sha"):
            continue
        packet_path = Path(row.get("path") or (deep_root / f"{safe_name(row['repo'])}.json"))
        if not packet_path.is_absolute():
            packet_path = Path.cwd() / packet_path
        try:
            resolved = packet_path.resolve()
            if deep_root.resolve() not in resolved.parents:
                continue
            packet_doc = json.loads(resolved.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        files = packet_doc.get("files") if isinstance(packet_doc, dict) else None
        if packet_doc.get("repo") == row["repo"] and packet_doc.get("revision_sha") == row["revision_sha"] and isinstance(files, list) and any(isinstance(f, dict) and isinstance(f.get("content"), str) and f.get("content") for f in files):
            names.add(row["repo"])
    return names


def select_repo_batch(repos, deep_extracted_names=None, now=None):
    """Choose a bounded, owner-diverse batch; preserve every other source on the shelf."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    deep_extracted_names = set(deep_extracted_names or ())
    force_refresh = os.getenv("COLLECTION_FORCE_REFRESH", "0").strip().lower() in {"1", "true", "yes"}
    by_owner, states, priorities = {}, {}, {}
    for item in repos:
        repo = item.get("full_name")
        if not repo:
            continue
        meta = item.get("repo_meta") or {}
        priorities[repo] = repo_priority(item, now)
        if meta.get("archived"):
            states[repo] = "ARCHIVED_METADATA_ONLY"
            continue
        packet_path = ROOT / f"{safe_name(repo)}.json"
        cached = None
        if packet_path.is_file():
            try:
                cached = json.loads(packet_path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                cached = None
        if isinstance(cached, dict) and cached.get("state") == "extracted" and has_usable_files(cached):
            if cached.get("pushed_at") == meta.get("pushed_at") and not force_refresh:
                states[repo] = "CACHED_CURRENT"
                continue
            states[repo] = "NEEDS_REFRESH"
        else:
            states[repo] = "NEEDS_REFRESH" if packet_path.exists() else "NEW"
        if repo in deep_extracted_names and not packet_path.exists():
            states[repo] = "DEEP_PACKET_ONLY"
            continue
        owner = (item.get("owner") or (meta.get("owner") or {}).get("login") or repo.split("/", 1)[0]).lower()
        by_owner.setdefault(owner, []).append(item)
    for owner, items in by_owner.items():
        items.sort(key=lambda item: (
            priorities[item["full_name"]],
            int((item.get("repo_meta") or {}).get("stargazers_count") or 0),
            (item.get("repo_meta") or {}).get("pushed_at") or (item.get("repo_meta") or {}).get("updated_at") or "",
            item["full_name"].lower(),
        ), reverse=True)
    owner_order = sorted(by_owner, key=lambda owner: (max(priorities[item["full_name"]] for item in by_owner[owner]), owner), reverse=True)
    selected = []
    if MAX_REPOS_PER_RUN <= 0 or MAX_REPOS_PER_OWNER <= 0:
        return selected, states, priorities
    for rank in range(MAX_REPOS_PER_OWNER):
        for owner in owner_order:
            if rank < len(by_owner[owner]):
                selected.append(by_owner[owner][rank])
                states[selected[-1]["full_name"]] = "SELECTED_FOR_EXTRACTION"
                if len(selected) >= MAX_REPOS_PER_RUN:
                    return selected, states, priorities
    return selected, states, priorities


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
    meta = item.get("repo_meta") or api(f"/repos/{repo}")
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
        and os.getenv("COLLECTION_FORCE_REFRESH", "0").strip().lower() not in {"1", "true", "yes"}
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
    archived_revision = archive_prior_revision(out, cached, data)
    if archived_revision:
        data["previous_revision_archive"] = archived_revision
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


def preserved_record(item, mode="preserved_after_refresh_failure"):
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
        1 for f in data.get("files", [])
        if isinstance(f, dict) and not f.get("error")
        and isinstance(f.get("content"), str) and f["content"]
    )
    kept["mode"] = mode
    return kept


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    previous_sources = load_previous_manifest()
    repos, gists, blocked, accounts = discover()
    deep_extracted_names = load_deep_extracted_names()
    selected_repos, cache_states, priorities = select_repo_batch(repos, deep_extracted_names)
    selected_names = {item["full_name"] for item in selected_repos}
    selected_gists = gists[:MAX_GISTS_PER_RUN]

    manifest = {
        "schema_version": "collection-intelligent-extraction/v2",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "account_count": len(accounts), "accounts": accounts,
        "repo_count": len(repos), "gist_count": len(gists),
        "inventory_repo_count": FRONTIER_META.get("inventory_repo_count", len(repos)),
        "selected_for_extraction_this_run": len(selected_repos),
        "selected_gists_this_run": len(selected_gists),
        "deep_extracted_repo_count": len(deep_extracted_names),
        "repo_inventory_path": FRONTIER_META.get("path"),
        "repo_inventory_sha256": FRONTIER_META.get("sha256"),
        "deep_manifest_path": FRONTIER_META.get("deep_manifest_path"),
        "deep_manifest_sha256": FRONTIER_META.get("deep_manifest_sha256"),
        "upstream_deep_extraction_failures": FRONTIER_META.get("upstream_refresh_failures", []),
        "batch_policy": {
            "max_repos_per_run": MAX_REPOS_PER_RUN, "max_repos_per_owner": MAX_REPOS_PER_OWNER,
            "max_files_per_source": MAX_FILES, "max_file_bytes": MAX_BYTES_PER_FILE,
            "max_source_bytes": MAX_BYTES_PER_SOURCE, "max_workers": MAX_WORKERS,
            "api_workers": API_WORKERS, "raw_workers": RAW_WORKERS,
        },
        "policy": {
            "max_files_per_source": MAX_FILES, "max_file_bytes": MAX_BYTES_PER_FILE,
            "max_source_bytes": MAX_BYTES_PER_SOURCE,
            "account_frontier": "COLLECTION/ACCOUNTS + COLLECTION/INDEX.md",
            "inventory_source": FRONTIER_META.get("path") or "live owner enumeration",
            "incremental": True, "raw_public_file_fetch": True,
            "bounded_source_batch": True,
        },
        "sources": [], "blocked": blocked,
    }

    # Reuse current canonical packets without refetching. Prior packets not selected
    # this cycle are preserved below; no existing source file is deleted.
    for item in repos:
        repo = item["full_name"]
        if cache_states.get(repo) != "CACHED_CURRENT":
            continue
        out = ROOT / f"{safe_name(repo)}.json"
        try:
            data = json.loads(out.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if data.get("state") != "extracted" or not has_usable_files(data):
            continue
        manifest["sources"].append({
            "canonical_source": data["canonical_source"], "state": data["state"],
            "path": str(out), "files_extracted": len(data["files"]),
            "tree_truncated": data.get("tree_truncated", False), "mode": "cached",
            "revision_sha": data.get("revision_sha"),
        })

    preserved_after_refresh_failure_count = 0
    with ThreadPoolExecutor(max_workers=min(MAX_WORKERS, max(1, len(selected_repos) + len(selected_gists)))) as ex:
        jobs = []
        for item in selected_repos:
            jobs.append(("repo", item, ex.submit(extract_repo, item)))
        for item in selected_gists:
            jobs.append(("gist", item, ex.submit(extract_gist, item["id"], item["owner"])))
        future_map = {future: (kind, item) for kind, item, future in jobs}
        for future in as_completed(future_map):
            kind, item = future_map[future]
            try:
                data, mode = future.result()
                if kind == "repo":
                    out = ROOT / f"{safe_name(item['full_name'])}.json"
                    if mode != "cached":
                        atomic_write_json(out, data)
                    record = {
                        "canonical_source": data["canonical_source"], "state": data["state"],
                        "path": str(out), "files_extracted": len(data["files"]),
                        "tree_truncated": data["tree_truncated"], "mode": mode,
                        "revision_sha": data.get("revision_sha"),
                    }
                    cache_states[item["full_name"]] = "EXTRACTED_THIS_RUN"
                else:
                    out = ROOT / f"gist_{safe_name(item['owner'])}_{item['id']}.json"
                    if mode != "cached":
                        atomic_write_json(out, data)
                    record = {
                        "canonical_source": data["canonical_source"], "state": data["state"],
                        "path": str(out), "files_extracted": len(data["files"]), "mode": "refreshed",
                    }
                manifest["sources"].append(record)
            except Exception as exc:
                canonical = f"github:{item['full_name']}" if kind == "repo" else f"github-gist:{item['id']}"
                previous = next(
                    (record for record in previous_sources if record.get("canonical_source") == canonical),
                    None,
                )
                preserved = preserved_record(previous) if previous else None
                if preserved:
                    manifest["sources"].append(preserved)
                    manifest["blocked"].append({
                        "canonical_source": canonical,
                        "state": "REFRESH_BLOCKED_PRESERVED",
                        "error": str(exc),
                    })
                    preserved_after_refresh_failure_count += 1
                    if kind == "repo":
                        cache_states[item["full_name"]] = "BLOCKED_REFRESH_PRESERVED"
                else:
                    manifest["sources"].append({
                        "canonical_source": canonical, "state": "BLOCKED_EXTERNAL_ACCESS",
                        "error": str(exc),
                    })
                    if kind == "repo":
                        cache_states[item["full_name"]] = "BLOCKED_EXTERNAL_ACCESS"

    # Count current-cycle rows before preserving the rest of the prior manifest.
    current_cycle_sources = list(manifest["sources"])
    processed_repo_count = sum(
        1 for row in current_cycle_sources
        if str(row.get("canonical_source", "")).startswith("github:")
        and row.get("mode") != "preserved_after_refresh_failure"
    )
    processed_gist_count = sum(
        1 for row in current_cycle_sources
        if str(row.get("canonical_source", "")).startswith("github-gist:")
        and row.get("mode") != "preserved_after_refresh_failure"
    )

    current_sources = {
        row.get("canonical_source"): row
        for row in manifest["sources"] if row.get("canonical_source")
    }
    preserved_not_selected_count = 0
    for previous in previous_sources:
        canonical = previous.get("canonical_source")
        if not canonical or canonical in current_sources:
            continue
        kept = preserved_record(previous, mode="preserved_not_selected")
        if kept:
            manifest["sources"].append(kept)
            current_sources[canonical] = kept
            preserved_not_selected_count += 1

    deferred_items = []
    for item in repos:
        repo = item["full_name"]
        state = cache_states.get(repo, "NEW")
        if state in {"NEW", "NEEDS_REFRESH", "SELECTED_FOR_EXTRACTION"}:
            if repo not in selected_names:
                state = "DEFERRED_BY_BUDGET"
            else:
                state = "BLOCKED_EXTERNAL_ACCESS"
        if state not in {"DEFERRED_BY_BUDGET", "BLOCKED_EXTERNAL_ACCESS", "BLOCKED_REFRESH_PRESERVED"}:
            continue
        meta = item.get("repo_meta") or {}
        deferred_items.append({
            "repo": repo, "owner": item.get("owner"),
            "html_url": meta.get("html_url"), "priority_score": priorities.get(repo, 0),
            "pushed_at": meta.get("pushed_at"), "state": state,
            "reason": "bounded batch budget" if state == "DEFERRED_BY_BUDGET" else "source extraction blocked or refresh failed",
        })
    deferred_path = ROOT / "DEFERRED-REPOSITORY-QUEUE.json"
    atomic_write_json(deferred_path, {
        "schema_version": "collection-canonical-deferred/v1",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "inventory_source": FRONTIER_META.get("path"),
        "deferred_count": len(deferred_items),
        "items": sorted(deferred_items, key=lambda row: (-int(row.get("priority_score") or 0), row["repo"].lower())),
    })

    manifest["processed_repo_count"] = processed_repo_count
    manifest["processed_gist_count"] = processed_gist_count
    manifest["preserved_sources_after_refresh_failure"] = preserved_after_refresh_failure_count
    manifest["preserved_prior_sources_not_selected"] = preserved_not_selected_count
    manifest["deferred_repo_count"] = len(deferred_items)
    manifest["deferred_queue_path"] = str(deferred_path)
    manifest["deferred_queue_sha256"] = hashlib.sha256(deferred_path.read_bytes()).hexdigest()
    manifest["extracted_sources"] = sum(x.get("state") == "extracted" for x in manifest["sources"])
    manifest["cached_sources"] = sum(x.get("mode") == "cached" for x in manifest["sources"])
    manifest["refreshed_sources"] = sum(x.get("mode") == "refreshed" for x in manifest["sources"])
    manifest["blocked_sources"] = (
        sum(x.get("state") == "BLOCKED_EXTERNAL_ACCESS" for x in manifest["sources"])
        + len(blocked) + preserved_after_refresh_failure_count
    )
    atomic_write_json(ROOT / "MANIFEST.json", manifest)
    print(json.dumps({
        "accounts": len(accounts), "inventory_repos": len(repos),
        "selected_repos_this_run": len(selected_repos),
        "deep_extracted_repos": len(deep_extracted_names),
        "deferred_repos": len(deferred_items),
        "source_rows": len(manifest["sources"]),
        "extracted_sources": manifest["extracted_sources"],
        "cached_sources": manifest["cached_sources"],
        "refreshed_sources": manifest["refreshed_sources"],
        "blocked_sources": manifest["blocked_sources"],
        "preserved_after_refresh_failure": preserved_after_refresh_failure_count,
        "preserved_not_selected": preserved_not_selected_count,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
