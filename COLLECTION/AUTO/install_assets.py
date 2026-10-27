#!/usr/bin/env python3
"""High-throughput, fail-closed installer for valuable OSS sources.

Policy:
- installs only explicitly approved permissive/open-source sources;
- requires promotion_action=INSTALL_APPROVED plus PASS integration/security gates;
- never auto-installs directly from the deep-extraction manifest or legacy source notes;
- pins every install to an exact revision;
- never copies secrets;
- deduplicates by source+revision;
- records success/failure without stopping the batch;
- never treats preservation as installation.
"""
from __future__ import annotations
import argparse, concurrent.futures, json, os, re, shutil, subprocess, tempfile
from urllib.parse import urlparse
from pathlib import Path

from collection_json_io import load_collection_json

ROOT = Path(__file__).resolve().parents[2]
INSTALLED = ROOT / "COLLECTION" / "INSTALLED"
REPORT = ROOT / "COLLECTION" / "MASTER" / "INSTALLATION-REPORT.json"
ALLOWED = {"MIT","Apache-2.0","BSD-2-Clause","BSD-3-Clause","ISC","MPL-2.0","Unlicense","0BSD"}
DEFAULT_WORKERS = int(os.getenv("COLLECTION_INSTALL_WORKERS", "8"))
MAX_MB = int(os.getenv("COLLECTION_INSTALL_MAX_MB", "250"))

QUARANTINE = ROOT / "COLLECTION" / "SECURITY" / "SOURCE-QUARANTINE.json"
INSTALL_APPROVALS = ROOT / "COLLECTION" / "MASTER" / "INSTALL-APPROVALS.json"


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

    A source is eligible only when the value queue explicitly marks INSTALL_APPROVED,
    install_approval=APPROVED, both integration/security gates PASS, the artifact is
    usable, the revision is pinned to a full commit SHA, and the license is allowed. This is a bounded install shortlist,
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
        if not isinstance(queued, dict):
            continue
        # Discovery/review/shelf/quarantine actions are not install authorization.
        # Require explicit approval and both integration/security gates.
        if queued.get("promotion_action") != "INSTALL_APPROVED":
            continue
        if queued.get("install_approval") != "APPROVED":
            continue
        if queued.get("integration_gate") != "PASS" or queued.get("security_gate") != "PASS":
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


def select_explicit_approval_candidates(manifest, approvals, max_candidates=5, quarantined_revisions=None, diagnostics=None):
    """Select exact-revision approvals only when both evidence-backed gates are PASS."""
    if not isinstance(max_candidates, int) or isinstance(max_candidates, bool) or not 0 <= max_candidates <= 20:
        raise ValueError("max_candidates must be between 0 and 20")
    rows = manifest.get("sources") if isinstance(manifest, dict) else None
    items = approvals.get("items") if isinstance(approvals, dict) else None
    if not isinstance(rows, list):
        raise ValueError("manifest.sources must be a list")
    if not isinstance(approvals, dict) or approvals.get("schema_version") != "collection-install-approvals/v1" or not isinstance(items, list):
        raise ValueError("install approvals schema is invalid")
    if max_candidates == 0:
        return []
    by_source = {
        row.get("canonical_source"): row
        for row in rows
        if isinstance(row, dict) and isinstance(row.get("canonical_source"), str)
    }
    blocked = {(repo, revision.lower()) for repo, revision in (quarantined_revisions or set())}
    selected, seen = [], set()
    diagnostics = diagnostics if diagnostics is not None else []
    def skip(approval, reason):
        diagnostics.append({"repo": approval.get("repo"), "revision_sha": approval.get("revision_sha"), "reason": reason})
    for approval in items:
        if not isinstance(approval, dict):
            raise ValueError("install approval entries must be objects")
        if approval.get("decision") != "INSTALL_APPROVED":
            skip(approval, "decision_not_install_approved")
            continue
        required = (
            "repo", "revision_sha", "license", "install_approval", "integration_gate",
            "security_gate", "integration_evidence", "security_evidence", "capability_key",
            "reviewed_at", "review_notes",
        )
        if any(not isinstance(approval.get(key), str) or not approval.get(key).strip() for key in required):
            raise ValueError("approved install record is incomplete")
        repo = approval["repo"]
        revision = approval["revision_sha"].lower()
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            raise ValueError("approved install repo is invalid")
        if not re.fullmatch(r"[0-9a-f]{40}", revision):
            raise ValueError("approved install revision must be a full commit SHA")
        if approval["install_approval"] != "APPROVED":
            skip(approval, "install_approval_not_approved")
            continue
        if approval["integration_gate"] != "PASS" or approval["security_gate"] != "PASS":
            skip(approval, "integration_or_security_gate_not_pass")
            continue
        for evidence_key in ("integration_evidence", "security_evidence"):
            parsed = urlparse(approval[evidence_key])
            if parsed.scheme != "https" or parsed.netloc != "github.com" or "/actions/runs/" not in parsed.path:
                raise ValueError(f"{evidence_key} must link to a GitHub Actions run")
        if approval["license"] not in ALLOWED:
            skip(approval, "approval_license_not_allowed")
            continue
        if (repo, revision) in blocked:
            skip(approval, "revision_quarantined")
            continue
        row = by_source.get("github:" + repo)
        if not isinstance(row, dict):
            skip(approval, "source_missing_from_current_manifest")
            continue
        row_revision = row.get("revision_sha")
        if not isinstance(row_revision, str) or row_revision.lower() != revision:
            skip(approval, "revision_does_not_match_current_manifest")
            continue
        if row.get("state") != "extracted" or row.get("license") != approval["license"]:
            skip(approval, "current_source_state_or_license_mismatch")
            continue
        # `preserved_not_selected` is still an exact extracted manifest row; it simply was not in this run's bounded refresh batch. Explicit revision-pinned approvals may use it. A failed refresh remains blocked.
        if row.get("mode") not in {"cached", "refreshed", "preserved_not_selected"}:
            skip(approval, "current_source_mode_not_installable:" + str(row.get("mode")))
            continue
        try:
            if int(row.get("files_extracted", 0) or 0) <= 0:
                skip(approval, "current_source_has_no_extracted_files")
                continue
        except (TypeError, ValueError):
            continue
        if repo in seen:
            skip(approval, "duplicate_approved_repo")
            continue
        selected.append({
            "source_record": "COLLECTION/MASTER/INSTALL-APPROVALS.json",
            "repo": repo,
            "url": "https://github.com/" + repo,
            "revision": revision,
            "license": approval["license"],
            "selected_capabilities": [approval["capability_key"]],
            "approval_evidence": {
                "integration": approval["integration_evidence"],
                "security": approval["security_evidence"],
                "reviewed_at": approval["reviewed_at"],
            },
        })
        seen.add(repo)
        if len(selected) >= max_candidates:
            break
    return selected


def source_records(max_auto_candidates=5):
    """Select only explicitly approved candidates from the canonical value queue."""
    out = []
    quarantined_revisions = load_quarantined_revisions()
    canonical_manifest = ROOT / "COLLECTION" / "AUTO" / "EXTRACTED" / "MANIFEST.json"
    value_queue_path = ROOT / "COLLECTION" / "MASTER" / "VALUE-OPERATOR-QUEUE.json"
    if not canonical_manifest.is_file():
        raise SystemExit(f"canonical Collection manifest is missing; refusing automatic install selection: {canonical_manifest}")
    if not value_queue_path.is_file():
        raise SystemExit(f"Collection value queue is missing; refusing automatic install selection: {value_queue_path}")
    if max_auto_candidates:
        try:
            canonical_data = json.loads(canonical_manifest.read_text(encoding="utf-8"))
            approval_data = json.loads(INSTALL_APPROVALS.read_text(encoding="utf-8"))
            approval_diagnostics = []
            explicit = select_explicit_approval_candidates(
                canonical_data, approval_data, max_auto_candidates, quarantined_revisions,
                diagnostics=approval_diagnostics,
            )
            print("EXPLICIT_INSTALL_APPROVAL_DIAGNOSTICS=" + json.dumps({
                "approval_records": len(approval_data.get("items", [])),
                "selected_repos": [item["repo"] for item in explicit],
                "skipped": approval_diagnostics,
            }, sort_keys=True))
            out.extend(explicit)
            seen = {item["repo"] for item in out}
            remaining = max_auto_candidates - len(out)
            if remaining > 0:
                value_data = load_collection_json(value_queue_path)
                queued = select_collected_candidates(canonical_data, value_data, remaining, quarantined_revisions)
                out.extend(item for item in queued if item["repo"] not in seen)
        except (OSError, ValueError) as exc:
            raise SystemExit(f"invalid Collection shortlist or approval input; refusing automatic install selection: {exc}")

    # Legacy source notes are preservation/research records only; they never feed auto-install.
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
