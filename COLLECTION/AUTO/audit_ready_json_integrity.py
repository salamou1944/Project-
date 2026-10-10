#!/usr/bin/env python3
"""Read-only semantic audit of READY.json around a target commit."""
import json
import subprocess
import sys
from collections import Counter
from collections.abc import Mapping

TARGET_COMMIT = "0d824d436b4e2a3c01ef6115c266f32c8e48f836"
READY_PATH = "COLLECTION/MASTER/READY.json"


def git_bytes(spec):
    return subprocess.run(
        ["git", "show", spec], check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout


def first_difference(left, right, path="$"):
    if type(left) is not type(right):
        return {"path": path, "reason": "type changed",
                "old_type": type(left).__name__, "new_type": type(right).__name__}
    if isinstance(left, Mapping):
        lk, rk = set(left), set(right)
        if lk != rk:
            return {"path": path, "reason": "object keys changed",
                    "removed_keys": sorted(lk-rk)[:30], "added_keys": sorted(rk-lk)[:30]}
        for key in sorted(left):
            diff = first_difference(left[key], right[key], f"{path}.{key}")
            if diff:
                return diff
        return None
    if isinstance(left, list):
        if len(left) != len(right):
            return {"path": path, "reason": "array length changed",
                    "old_length": len(left), "new_length": len(right)}
        for i, (a, b) in enumerate(zip(left, right)):
            diff = first_difference(a, b, f"{path}[{i}]")
            if diff:
                return diff
        return None
    if left != right:
        return {"path": path, "reason": "value changed",
                "old_value": repr(left)[:120], "new_value": repr(right)[:120]}
    return None


def decision_map(data):
    return {
        item["capability_key"]: item
        for item in data.get("decisions", [])
        if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
    }


def evidence_map(data):
    result = {}
    for key, decision in decision_map(data).items():
        for item in decision.get("evidence", []):
            if not isinstance(item, dict):
                continue
            identity = (
                key, item.get("source"), item.get("source_revision"),
                item.get("file"), item.get("content_sha256"),
            )
            result[identity] = item
    return result


def main():
    commit = sys.argv[1] if len(sys.argv) > 1 else TARGET_COMMIT
    try:
        old_raw = git_bytes(f"{commit}^:{READY_PATH}")
        new_raw = git_bytes(f"{commit}:{READY_PATH}")
        old, new = json.loads(old_raw), json.loads(new_raw)
    except Exception as exc:
        print(json.dumps({"status": "ERROR", "commit": commit, "error": str(exc)}))
        return 2

    old_decisions, new_decisions = decision_map(old), decision_map(new)
    old_keys, new_keys = set(old_decisions), set(new_decisions)
    common = old_keys & new_keys
    changed_fields = Counter()
    changed_samples = []
    evidence_count_changes = []
    for key in sorted(common):
        a, b = old_decisions[key], new_decisions[key]
        fields = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))
        if fields:
            changed_fields.update(fields)
            if len(changed_samples) < 40:
                changed_samples.append({
                    "capability_key": key,
                    "changed_fields": fields,
                    "old_evidence_count": len(a.get("evidence", [])) if isinstance(a.get("evidence"), list) else None,
                    "new_evidence_count": len(b.get("evidence", [])) if isinstance(b.get("evidence"), list) else None,
                })
            old_ev = a.get("evidence", [])
            new_ev = b.get("evidence", [])
            if isinstance(old_ev, list) and isinstance(new_ev, list) and len(old_ev) != len(new_ev):
                def ev_id(item):
                    if not isinstance(item, dict):
                        return {"malformed": repr(item)[:100]}
                    return {
                        "source": item.get("source"),
                        "source_revision": item.get("source_revision"),
                        "file": item.get("file"),
                        "content_sha256": item.get("content_sha256"),
                    }
                old_ids = {json.dumps(ev_id(item), sort_keys=True) for item in old_ev}
                new_ids = {json.dumps(ev_id(item), sort_keys=True) for item in new_ev}
                evidence_count_changes.append({
                    "capability_key": key,
                    "old": len(old_ev),
                    "new": len(new_ev),
                    "removed_evidence": [json.loads(item) for item in sorted(old_ids - new_ids)],
                    "added_evidence": [json.loads(item) for item in sorted(new_ids - old_ids)],
                })

    old_evidence, new_evidence = evidence_map(old), evidence_map(new)
    missing_evidence = old_evidence.keys() - new_evidence.keys()
    added_evidence = new_evidence.keys() - old_evidence.keys()

    def evidence_identity_sets(data):
        full, without_revision, content = set(), set(), set()
        for key, decision in decision_map(data).items():
            for item in decision.get("evidence", []):
                if not isinstance(item, dict):
                    continue
                source, revision, file_path, digest = (
                    item.get("source"), item.get("source_revision"),
                    item.get("file"), item.get("content_sha256")
                )
                full.add((key, source, revision, file_path, digest))
                without_revision.add((key, source, file_path, digest))
                content.add((source, file_path, digest))
        return full, without_revision, content

    old_full, old_without_revision, old_content = evidence_identity_sets(old)
    new_full, new_without_revision, new_content = evidence_identity_sets(new)

    # Verify old source-file hashes no longer represented in READY remain recoverable.
    old_changed_records = {}
    for key, decision in decision_map(old).items():
        for item in decision.get("evidence", []):
            if not isinstance(item, dict):
                continue
            source, revision, file_path, digest = (
                item.get("source"), item.get("source_revision"),
                item.get("file"), item.get("content_sha256")
            )
            if not all(isinstance(v, str) and v for v in (source, revision, file_path, digest)):
                continue
            if (source, file_path, digest) in new_content:
                continue
            old_changed_records[(source, revision, file_path, digest)] = item

    archived_old_hashes_verified = []
    archived_old_hashes_missing = []
    for source, revision, file_path, digest in sorted(old_changed_records, key=lambda x: tuple(str(v) for v in x)):
        slug = source.removeprefix("github:").replace("/", "_")
        candidates = [
            f"COLLECTION/AUTO/EXTRACTED/HISTORY/{slug}__{revision}.json",
            f"COLLECTION/AUTO/EXTRACTED/{slug}.json",
        ]
        found = False
        # Check both the post-refresh tree and the pre-refresh parent tree.
        for tree_ref in (commit, f"{commit}^"):
            for candidate in candidates:
                proc = subprocess.run(
                    ["git", "show", f"{tree_ref}:{candidate}"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                )
                if proc.returncode:
                    continue
                try:
                    artifact = json.loads(proc.stdout)
                except Exception:
                    continue
                if artifact.get("canonical_source") != source or artifact.get("revision_sha") != revision:
                    continue
                for file_item in artifact.get("files", []):
                    if isinstance(file_item, dict) and file_item.get("path") == file_path and file_item.get("content_sha256") == digest:
                        archived_old_hashes_verified.append((source, revision, file_path, digest))
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if not found:
            archived_old_hashes_missing.append((source, revision, file_path, digest))
    old_counts = old.get("counts", {}) if isinstance(old, dict) else {}
    new_counts = new.get("counts", {}) if isinstance(new, dict) else {}
    count_changes = {
        key: {"old": old_counts.get(key), "new": new_counts.get(key)}
        for key in sorted(set(old_counts) | set(new_counts))
        if old_counts.get(key) != new_counts.get(key)
    }
    count_regressions = {
        key: {"old": old_counts.get(key), "new": new_counts.get(key)}
        for key, value in old_counts.items()
        if isinstance(value, (int, float))
        and (not isinstance(new_counts.get(key), (int, float)) or new_counts[key] < value)
    }
    exact_diff = first_difference(old, new)
    result = {
        "status": "EXACT_DATA_EQUAL" if exact_diff is None else "DATA_DIFFERENCE_REPORTED",
        "commit": commit,
        "path": READY_PATH,
        "old_bytes": len(old_raw),
        "new_bytes": len(new_raw),
        "old_decision_count": len(old.get("decisions", [])),
        "new_decision_count": len(new.get("decisions", [])),
        "old_unique_decision_keys": len(old_keys),
        "new_unique_decision_keys": len(new_keys),
        "prior_decision_keys_missing_count": len(old_keys - new_keys),
        "prior_decision_keys_missing_sample": sorted(old_keys - new_keys)[:50],
        "new_decision_keys_count": len(new_keys - old_keys),
        "new_decision_keys_sample": sorted(new_keys - old_keys)[:50],
        "count_changes": count_changes,
        "count_regressions": count_regressions,
        "common_decisions_with_changed_fields_count": sum(bool(old_decisions[k] != new_decisions[k]) for k in common),
        "changed_decision_field_frequency": dict(changed_fields.most_common()),
        "changed_decision_samples": changed_samples,
        "evidence_identity_counts": {"old": len(old_evidence), "new": len(new_evidence)},
        "prior_evidence_identities_missing_count": len(missing_evidence),
        "prior_evidence_identities_missing_sample": [
            {"capability_key": k, "source": s, "revision": rev, "file": path, "content_sha256": digest}
            for k, s, rev, path, digest in sorted(missing_evidence, key=lambda x: tuple(str(v) for v in x))[:50]
        ],
        "new_evidence_identities_count": len(added_evidence),
        "evidence_missing_after_ignoring_revision_count": len(old_without_revision - new_without_revision),
        "evidence_added_after_ignoring_revision_count": len(new_without_revision - old_without_revision),
        "source_file_content_hashes_missing_count": len(old_content - new_content),
        "source_file_content_hashes_added_count": len(new_content - old_content),
        "changed_old_content_records_checked_in_history": len(old_changed_records),
        "changed_old_content_records_archived_verified": len(archived_old_hashes_verified),
        "changed_old_content_records_archive_missing_count": len(archived_old_hashes_missing),
        "changed_old_content_records_archive_missing_sample": [
            {"source": source, "revision": revision, "file": file_path, "content_sha256": digest}
            for source, revision, file_path, digest in archived_old_hashes_missing[:30]
        ],
        "source_file_content_hashes_missing_sample": [
            {"source": source, "file": file_path, "content_sha256": digest}
            for source, file_path, digest in sorted(old_content - new_content, key=lambda x: tuple(str(v) for v in x))[:25]
        ],
        "new_evidence_identities_sample": [
            {"capability_key": k, "source": s, "revision": rev, "file": path, "content_sha256": digest}
            for k, s, rev, path, digest in sorted(added_evidence, key=lambda x: tuple(str(v) for v in x))[:50]
        ],
        "evidence_count_changes_sample": evidence_count_changes[:40],
        "first_structural_difference": exact_diff,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    # Diagnostic audit: return failure only if the report itself could not be made.
    # A real data difference is intentionally reported in the JSON above.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
