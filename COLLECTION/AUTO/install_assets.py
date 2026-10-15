#!/usr/bin/env python3
"""High-throughput, fail-closed installer for valuable OSS sources.

Policy:
- installs only explicitly eligible permissive/open-source sources;
- pins every install to an exact revision;
- never copies secrets;
- deduplicates by source+revision;
- installs in parallel;
- records success/failure without stopping the batch;
- never treats preservation as installation.
"""
from __future__ import annotations
import argparse, concurrent.futures, json, os, re, shutil, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT / "COLLECTION" / "SOURCES"
INSTALLED = ROOT / "COLLECTION" / "INSTALLED"
REPORT = ROOT / "COLLECTION" / "MASTER" / "INSTALLATION-REPORT.json"
ALLOWED = {"MIT","Apache-2.0","BSD-2-Clause","BSD-3-Clause","ISC","MPL-2.0","Unlicense","0BSD"}
DEFAULT_WORKERS = int(os.getenv("COLLECTION_INSTALL_WORKERS", "8"))
MAX_MB = int(os.getenv("COLLECTION_INSTALL_MAX_MB", "250"))

QUARANTINE = ROOT / "COLLECTION" / "SECURITY" / "SOURCE-QUARANTINE.json"


def load_quarantined_revisions():
    """Load exact compromised source revisions; missing/invalid policy blocks installation."""
    if not QUARANTINE.is_file():
        raise SystemExit(f"missing source quarantine registry; refusing installation: {QUARANTINE}")
    try:
        doc = json.loads(QUARANTINE.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SystemExit(f"invalid source quarantine registry; refusing installation: {exc}")
    entries = doc.get("entries") if isinstance(doc, dict) else None
    if not isinstance(doc, dict) or doc.get("schema_version") != "collection-source-quarantine/v1" or not isinstance(entries, list):
        raise SystemExit("source quarantine registry schema is invalid; refusing installation")
    blocked = set()
    for item in entries:
        if not isinstance(item, dict):
            raise SystemExit("source quarantine entry must be an object; refusing installation")
        repo = item.get("repo")
        revision = item.get("revision_sha")
        if (not isinstance(repo, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo)
                or not isinstance(revision, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", revision)
                or not item.get("reason")):
            raise SystemExit("source quarantine entry is incomplete or invalid; refusing installation")
        blocked.add((repo, revision.lower()))
    return blocked


def is_quarantined_revision(repo, revision, quarantined_revisions):
    """Match exact revisions and abbreviated Git SHAs without allowing prefix bypass."""
    if not isinstance(repo, str) or not isinstance(revision, str):
        return False
    candidate = revision.lower()
    return any(
        blocked_repo == repo
        and (blocked_revision.startswith(candidate) or candidate.startswith(blocked_revision))
        for blocked_repo, blocked_revision in quarantined_revisions
    )


def select_collected_candidates(manifest, value_queue, max_candidates=5, quarantined_revisions=None):
    """Select a small, evidence-prioritized set from the current Collection manifest.

    A source is eligible only when it is present in the non-quarantined value
    queue, has a usable extracted artifact, is pinned to a full commit SHA, and
    declares an explicitly allowed license. This is a bounded install shortlist,
    not a blanket install of every discovered repository.
    """
    if not isinstance(max_candidates, int) or isinstance(max_candidates, bool) or not 0 <= max_candidates <= 20:
        raise ValueError("max_candidates must be between 0 and 20")
    rows = manifest.get("sources") if isinstance(manifest, dict) else None
    items = value_queue.get("items") if isinstance(value_queue, dict) else None
    if not isinstance(rows, list) or not isinstance(items, list):
        raise ValueError("manifest.sources and value_queue.items must be lists")
    if max_candidates == 0:
        return []
    by_source = {
        row.get("canonical_source"): row
        for row in rows
        if isinstance(row, dict) and isinstance(row.get("canonical_source"), str)
    }
    blocked_revisions = {(repo, revision.lower()) for repo, revision in (quarantined_revisions or set())}
    selected, seen = [], set()
    for queued in items:
        if not isinstance(queued, dict) or queued.get("promotion_action") == "QUARANTINE":
            continue
        sources = queued.get("sources", [])
        if not isinstance(sources, list):
            continue
        for source in sources:
            row = by_source.get(source)
            if not isinstance(row, dict):
                continue
            repo = source.removeprefix("github:")
            if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
                continue
            revision = row.get("revision_sha")
            if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", revision):
                continue
            if row.get("state") != "extracted" or row.get("license") not in ALLOWED:
                continue
            # Old snapshots preserved after a failed refresh must never be installed.
            if row.get("mode") not in {"cached", "refreshed"}:
                continue
            if is_quarantined_revision(repo, revision, blocked_revisions):
                continue
            try:
                if int(row.get("files_extracted", 0) or 0) <= 0:
                    continue
            except (TypeError, ValueError):
                continue
            if repo in seen:
                continue
            selected.append({
                "source_record": "COLLECTION/MASTER/VALUE-OPERATOR-QUEUE.json",
                "repo": repo,
                "url": "https://github.com/" + repo,
                "revision": revision,
                "license": row["license"],
                "selected_capabilities": [queued.get("capability_key")] if queued.get("capability_key") else [],
            })
            seen.add(repo)
            if len(selected) >= max_candidates:
                return selected
    return selected


def source_records(max_auto_candidates=5):
    out = []
    quarantined_revisions = load_quarantined_revisions()
    manifest = ROOT / "COLLECTION" / "AUTO" / "DEEP-EXTRACTED" / "MANIFEST.json"
    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise SystemExit(f"invalid deep-extraction manifest; refusing partial install selection: {exc}")
        repos = data.get("repos", [])
        if not isinstance(repos, list):
            raise SystemExit("deep-extraction manifest repos must be a list")
        for x in repos:
            if not isinstance(x, dict):
                continue
            repo = x.get("repo")
            rev = x.get("revision_sha")
            lic = x.get("license")
            if repo and rev and lic in ALLOWED and not is_quarantined_revision(repo, str(rev), quarantined_revisions):
                out.append({
                    "source_record": "DEEP-EXTRACTED/MANIFEST.json",
                    "repo": repo,
                    "url": "https://github.com/" + repo,
                    "revision": rev,
                    "license": lic,
                })
    canonical_manifest = ROOT / "COLLECTION" / "AUTO" / "EXTRACTED" / "MANIFEST.json"
    value_queue_path = ROOT / "COLLECTION" / "MASTER" / "VALUE-OPERATOR-QUEUE.json"
    if canonical_manifest.exists() and value_queue_path.exists() and max_auto_candidates:
        try:
            canonical_data = json.loads(canonical_manifest.read_text(encoding="utf-8"))
            value_data = json.loads(value_queue_path.read_text(encoding="utf-8"))
            out.extend(select_collected_candidates(canonical_data, value_data, max_auto_candidates, quarantined_revisions))
        except (OSError, ValueError) as exc:
            raise SystemExit(f"invalid Collection shortlist input; refusing automatic install selection: {exc}")

    for p in sorted(SOURCES.glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"^- Source:\s*(https?://github\.com/[^\s]+)", text, re.M)
        r = re.search(r"^- Repository:\s*([^\s]+)", text, re.M)
        owner = re.search(r"^- Owner:\s*([^\s]+)", text, re.M)
        rev = re.search(r"^- Main revision inspected:\s*`?([0-9a-f]{7,40})`?", text, re.M)
        lic = re.search(r"^- License:\s*([^\n]+)", text, re.M)
        if not (m and rev and lic):
            continue
        url = m.group(1).rstrip("/")
        license_name = lic.group(1).strip()
        if license_name not in ALLOWED:
            continue
        repo_value = r.group(1).strip() if r else ""
        owner_value = owner.group(1).strip() if owner else ""
        if "/" in repo_value:
            owner_repo = repo_value
        elif owner_value and repo_value:
            owner_repo = owner_value.rstrip("/") + "/" + repo_value.lstrip("/")
        else:
            parts = url.split("github.com/", 1)[-1].strip("/").split("/")
            owner_repo = "/".join(parts[:2]) if len(parts) >= 2 else ""
        if not owner_repo or owner_repo.count("/") != 1:
            continue
        if is_quarantined_revision(owner_repo, rev.group(1), quarantined_revisions):
            continue
        out.append({
            "source_record": p.name,
            "repo": owner_repo,
            "url": url,
            "revision": rev.group(1),
            "license": license_name,
        })
    return out

def safe_name(repo):
    return re.sub(r"[^A-Za-z0-9_.-]+", "__", repo)

def install_one(item):
    target = INSTALLED / safe_name(item["repo"])
    marker = target / ".collection-install.json"
    if marker.exists():
        try:
            old = json.loads(marker.read_text())
            if old.get("repo") == item["repo"] and old.get("revision") == item["revision"]:
                return {**item, "status":"ALREADY_INSTALLED", "path":str(target)}
        except Exception:
            pass
    tmp = Path(tempfile.mkdtemp(prefix="collection-install-"))
    try:
        clone = tmp / "repo"
        subprocess.run(
            ["git","clone","--filter=blob:none","--no-checkout",item["url"],str(clone)],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=180
        )
        subprocess.run(["git","-C",str(clone),"fetch","--depth","1","origin",item["revision"]],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=180)
        subprocess.run(["git","-C",str(clone),"checkout","--detach",item["revision"]],
                       check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=120)
        size_mb = int(subprocess.check_output(
            ["du","-sm",str(clone)], text=True, timeout=30
        ).split()[0])
        if size_mb > MAX_MB:
            return {**item, "status":"BLOCKED_SIZE", "size_mb":size_mb, "limit_mb":MAX_MB}
        target.parent.mkdir(parents=True, exist_ok=True)
        # Prepare the complete replacement beside the target so rename stays
        # on the same filesystem. Never delete the last known-good install first.
        staged = Path(tempfile.mkdtemp(prefix=f".{target.name}.staged-", dir=target.parent))
        backup = target.with_name(f".{target.name}.backup-{os.getpid()}")
        try:
            shutil.rmtree(staged)
            shutil.copytree(clone, staged, ignore=shutil.ignore_patterns(".git"))
            staged_marker = staged / ".collection-install.json"
            staged_marker.write_text(json.dumps({
                **item, "status":"INSTALLED", "install_mode":"vendored_source",
                "revision_pinned":True, "size_mb":size_mb
            }, indent=2)+"\n", encoding="utf-8")
            # A stale backup is not silently deleted: fail closed to preserve recovery material.
            if backup.exists():
                raise RuntimeError(f"install_backup_already_exists:{backup}")
            moved_old = False
            if target.exists():
                target.rename(backup)
                moved_old = True
            try:
                staged.rename(target)
            except Exception:
                if moved_old and backup.exists() and not target.exists():
                    backup.rename(target)
                raise
            if moved_old:
                shutil.rmtree(backup)
        finally:
            if staged.exists():
                shutil.rmtree(staged, ignore_errors=True)
        return {**item, "status":"INSTALLED", "path":str(target), "size_mb":size_mb}
    except Exception as exc:
        return {**item, "status":"FAILED", "error":str(exc)[:1000]}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    ap.add_argument("--max-mb", type=int, default=MAX_MB)
    ap.add_argument("--max-auto-candidates", type=int, default=5,
                    help="maximum prioritized candidates selected from the current Collection value queue (0-20)")
    ns = ap.parse_args()
    if ns.workers < 1 or ns.max_mb < 1 or not 0 <= ns.max_auto_candidates <= 20:
        ap.error("workers and max-mb must be positive; max-auto-candidates must be between 0 and 20")
    globals()["MAX_MB"] = ns.max_mb
    items = source_records(ns.max_auto_candidates)
    # Source+revision is the installation identity; preserve distinct records but install once.
    unique = {}
    for x in items:
        unique[(x["repo"],x["revision"])] = x
    # The destination path is repo-scoped, not revision-scoped. Installing two
    # revisions of one repo concurrently would race and could mislabel the final tree.
    by_repo = {}
    for item in unique.values():
        by_repo.setdefault(item["repo"], []).append(item)
    installable = []
    results = []
    for repo, versions in sorted(by_repo.items()):
        revisions = sorted({x["revision"] for x in versions})
        if len(revisions) > 1:
            results.append({
                "repo": repo,
                "status": "BLOCKED_REVISION_CONFLICT",
                "revisions": revisions,
                "reason": "multiple pinned revisions target the same repository-scoped install path; choose one explicitly"
            })
        else:
            installable.append(versions[0])
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, ns.workers)) as ex:
        futures = [ex.submit(install_one,x) for x in installable]
        for f in concurrent.futures.as_completed(futures):
            results.append(f.result())
    results.sort(key=lambda x:(x["status"],x["repo"]))
    report = {
        "schema_version":"collection-installation/v1",
        "policy":"permissive OSS only; exact revision; deduplicated; fail-closed",
        "candidate_count":len(unique),
        "results":results,
        "counts":{}
    }
    for x in results:
        report["counts"][x["status"]] = report["counts"].get(x["status"],0)+1
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    tmp_report = REPORT.with_name(REPORT.name + ".tmp")
    with tmp_report.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(tmp_report, REPORT)
    print(json.dumps({"candidates":len(unique),"counts":report["counts"]},sort_keys=True))

if __name__=="__main__":
    main()
