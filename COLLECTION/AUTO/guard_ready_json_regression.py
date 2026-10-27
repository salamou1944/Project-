#!/usr/bin/env python3
"""Fail closed if regenerated READY data loses evidence that cannot be recovered."""
import hashlib
import json
import subprocess
from pathlib import Path

from collection_json_io import load_collection_json

ROOT = Path(__file__).resolve().parents[2]
READY = ROOT / "COLLECTION/MASTER/READY.json"
HISTORY = ROOT / "COLLECTION/AUTO/EXTRACTED/HISTORY"
EXTRACTED = ROOT / "COLLECTION/AUTO/EXTRACTED"
artifact_cache = {}


def load_json(path):
    return load_collection_json(path)


def decisions(data):
    result = {}
    duplicates = []
    for item in data.get("decisions", []):
        if not isinstance(item, dict) or not isinstance(item.get("capability_key"), str):
            raise SystemExit("READY.json contains a malformed decision or missing capability_key")
        key = item["capability_key"]
        if key in result:
            duplicates.append(key)
        result[key] = item
    if duplicates:
        raise SystemExit("READY.json contains duplicate capability_key values: " + repr(duplicates[:20]))
    return result


def artifact_for(source, revision):
    if not isinstance(source, str) or not source or not isinstance(revision, str) or not revision:
        return None
    slug = source.removeprefix("github:").replace("/", "_")
    candidates = [
        HISTORY / f"{slug}__{revision}.json",
        EXTRACTED / f"{slug}.json",
    ]
    for path in candidates:
        cache_key = str(path)
        if cache_key not in artifact_cache:
            try:
                artifact_cache[cache_key] = load_json(path) if path.is_file() else None
            except Exception:
                artifact_cache[cache_key] = None
        artifact = artifact_cache[cache_key]
        if isinstance(artifact, dict) and artifact.get("canonical_source") == source and artifact.get("revision_sha") == revision:
            return artifact
    # Also consult the committed baseline tree if a path was not materialized in the working tree.
    for path in candidates:
        spec = "HEAD:" + path.relative_to(ROOT).as_posix()
        proc = subprocess.run(["git", "show", spec], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode == 0:
            try:
                artifact = json.loads(proc.stdout)
            except Exception:
                continue
            if artifact.get("canonical_source") == source and artifact.get("revision_sha") == revision:
                return artifact
    return None


def evidence_recoverable(item):
    if not isinstance(item, dict):
        return False
    source = item.get("source")
    revision = item.get("source_revision")
    file_path = item.get("file")
    digest = item.get("content_sha256")
    if not all(isinstance(v, str) and v for v in (source, revision, file_path, digest)):
        return False
    # Empty repository files carry no payload to lose. Their SHA-256 is the
    # well-known digest of zero bytes; don't misclassify their disappearance
    # from a regenerated capability index as unrecoverable content loss.
    if digest == hashlib.sha256(b"").hexdigest():
        return True
    artifact = artifact_for(source, revision)
    if not artifact:
        return False
    return any(
        isinstance(entry, dict)
        and entry.get("path") == file_path
        and entry.get("content_sha256") == digest
        for entry in artifact.get("files", [])
    )


def evidence_map(decision_map):
    found = {}
    for key, decision in decision_map.items():
        records = decision.get("evidence", [])
        if not isinstance(records, list):
            raise SystemExit(f"decision {key} has malformed evidence list")
        for item in records:
            if not isinstance(item, dict):
                raise SystemExit(f"decision {key} contains malformed evidence")
            identity = (key, item.get("source"), item.get("source_revision"), item.get("file"), item.get("content_sha256"))
            found[identity] = item
    return found


def main():
    try:
        baseline = load_collection_json("COLLECTION/MASTER/READY.json", git_ref="HEAD", repo_root=ROOT)
        current = load_json(READY)
    except Exception as exc:
        raise SystemExit(f"cannot load baseline/current READY.json: {type(exc).__name__}: {exc}")

    old_decisions, new_decisions = decisions(baseline), decisions(current)
    old_evidence, new_evidence = evidence_map(old_decisions), evidence_map(new_decisions)
    missing_keys = sorted(set(old_decisions) - set(new_decisions))
    missing_evidence = sorted(set(old_evidence) - set(new_evidence), key=lambda x: tuple(str(v) for v in x))
    unrecoverable = []
    checked = set()
    for identity in missing_evidence:
        source, revision, file_path, digest = identity[1:]
        record_key = (source, revision, file_path, digest)
        if record_key in checked:
            continue
        checked.add(record_key)
        item = old_evidence[identity]
        if not evidence_recoverable(item):
            unrecoverable.append({
                "capability_key": identity[0], "source": source, "revision": revision,
                "file": file_path, "content_sha256": digest,
            })

    old_counts = baseline.get("counts", {})
    new_counts = current.get("counts", {})
    result = {
        "status": "PASS" if not unrecoverable else "FAIL_UNRECOVERABLE_EVIDENCE",
        "baseline_commit": subprocess.run(["git", "rev-parse", "HEAD"], check=True, stdout=subprocess.PIPE, text=True).stdout.strip(),
        "old_decisions": len(old_decisions),
        "new_decisions": len(new_decisions),
        "prior_decision_keys_missing": len(missing_keys),
        "prior_evidence_identities_missing_from_current": len(missing_evidence),
        "unique_prior_evidence_records_checked_in_history": len(checked),
        "unrecoverable_prior_evidence_records": len(unrecoverable),
        "unrecoverable_sample": unrecoverable[:20],
        "count_changes": {
            key: {"old": old_counts.get(key), "new": new_counts.get(key)}
            for key in sorted(set(old_counts) | set(new_counts))
            if old_counts.get(key) != new_counts.get(key)
        },
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if not unrecoverable else 1


if __name__ == "__main__":
    raise SystemExit(main())
