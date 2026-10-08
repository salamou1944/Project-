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

def source_records():
    out = []
    manifest = ROOT / "COLLECTION" / "AUTO" / "DEEP-EXTRACTED" / "MANIFEST.json"
    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            for x in data.get("repos", []):
                repo = x.get("repo")
                rev = x.get("revision_sha")
                lic = x.get("license")
                if repo and rev and lic in ALLOWED:
                    out.append({
                        "source_record": "DEEP-EXTRACTED/MANIFEST.json",
                        "repo": repo,
                        "url": "https://github.com/" + repo,
                        "revision": rev,
                        "license": lic,
                    })
        except Exception:
            pass
    for p in sorted(SOURCES.glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"^- Source:\s*(https?://github\.com/[^\s]+)", text, re.M)
        r = re.search(r"^- Repository:\s*([^\s]+)", text, re.M)
        rev = re.search(r"^- Main revision inspected:\s*([0-9a-f]{7,40})", text, re.M)
        lic = re.search(r"^- License:\s*([^\n]+)", text, re.M)
        if not (m and r and rev and lic):
            continue
        url = m.group(1).rstrip("/")
        license_name = lic.group(1).strip()
        if license_name not in ALLOWED:
            continue
        owner_repo = r.group(1).strip()
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
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(clone, target, ignore=shutil.ignore_patterns(".git"))
        marker.write_text(json.dumps({
            **item, "status":"INSTALLED", "install_mode":"vendored_source",
            "revision_pinned":True, "size_mb":size_mb
        }, indent=2)+"\n", encoding="utf-8")
        return {**item, "status":"INSTALLED", "path":str(target), "size_mb":size_mb}
    except Exception as exc:
        return {**item, "status":"FAILED", "error":str(exc)[:1000]}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    ap.add_argument("--max-mb", type=int, default=MAX_MB)
    ns = ap.parse_args()
    globals()["MAX_MB"] = ns.max_mb
    items = source_records()
    # Source+revision is the installation identity; preserve distinct records but install once.
    unique = {}
    for x in items:
        unique[(x["repo"],x["revision"])] = x
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, ns.workers)) as ex:
        futures = [ex.submit(install_one,x) for x in unique.values()]
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
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"candidates":len(unique),"counts":report["counts"]},sort_keys=True))

if __name__=="__main__":
    main()
