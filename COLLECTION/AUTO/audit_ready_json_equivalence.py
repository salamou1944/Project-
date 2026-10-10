#!/usr/bin/env python3
"""Read-only READY.json non-regression audit.

The compared revisions can contain legitimate new extraction results, so exact
whole-document equality is not a valid requirement. This audit verifies that
recorded counts do not regress and that evidence behind any prior decision no
longer active is still available in the exact archived source revision. It does
not assert that every prior decision remains active. Serialization correctness
is tested separately by test_ready_json_compaction.py.
"""
from __future__ import annotations
import json
import subprocess

PATH = "COLLECTION/MASTER/READY.json"
MANIFEST_PATH = "COLLECTION/AUTO/EXTRACTED/MANIFEST.json"
BEFORE = "0d824d436b4e2a3c01ef6115c266f32c8e48f836"
MANIFEST_BEFORE = "49aac90e"
AFTER = "HEAD"


def load_revision(revision: str):
    proc = subprocess.run(
        ["git", "show", f"{revision}:{PATH}"],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return json.loads(proc.stdout)


def load_revision_path(revision: str, path: str):
    proc = subprocess.run(
        ["git", "show", f"{revision}:{path}"],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return json.loads(proc.stdout)


def audit_manifest_preservation() -> list[dict]:
    """Ensure harvested source identities/states survive and changed revisions are archived."""
    print(f"Loading pre-recovery manifest {MANIFEST_BEFORE}...", flush=True)
    before = load_revision_path(MANIFEST_BEFORE, MANIFEST_PATH)
    print(f"Loading current manifest {AFTER}...", flush=True)
    after = load_revision_path(AFTER, MANIFEST_PATH)
    old_sources = before.get("sources", [])
    new_sources = after.get("sources", [])
    old_by_source = {item.get("canonical_source"): item for item in old_sources
                     if isinstance(item, dict) and isinstance(item.get("canonical_source"), str)}
    new_by_source = {item.get("canonical_source"): item for item in new_sources
                     if isinstance(item, dict) and isinstance(item.get("canonical_source"), str)}
    missing_sources = sorted(set(old_by_source) - set(new_by_source))
    state_regressions = [
        {"source": source, "before": old_by_source[source].get("state"),
         "after": new_by_source[source].get("state")}
        for source in old_by_source.keys() & new_by_source.keys()
        if old_by_source[source].get("state") == "extracted"
        and new_by_source[source].get("state") != "extracted"
    ]
    missing_archives = []
    changed_revisions = 0
    for source, old in old_by_source.items():
        current = new_by_source.get(source)
        if current is None or old.get("state") != "extracted":
            continue
        old_revision = old.get("revision_sha")
        new_revision = current.get("revision_sha")
        if not isinstance(old_revision, str) or not old_revision or old_revision == new_revision:
            continue
        changed_revisions += 1
        slug = source.removeprefix("github:").replace("/", "_")
        archive = f"COLLECTION/AUTO/EXTRACTED/HISTORY/{slug}__{old_revision}.json"
        proc = subprocess.run(["git", "show", f"HEAD:{archive}"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode:
            missing_archives.append({"source": source, "revision": old_revision, "archive": archive})
            continue
        try:
            artifact = json.loads(proc.stdout)
        except Exception:
            missing_archives.append({"source": source, "revision": old_revision,
                                     "archive": archive, "reason": "invalid_json"})
            continue
        if artifact.get("canonical_source") != source or artifact.get("revision_sha") != old_revision:
            missing_archives.append({"source": source, "revision": old_revision,
                                     "archive": archive, "reason": "identity_mismatch"})
    print(f"MANIFEST_SOURCES_BEFORE={len(old_sources)}")
    print(f"MANIFEST_SOURCES_AFTER={len(new_sources)}")
    print(f"MANIFEST_PRIOR_SOURCES_MISSING={len(missing_sources)}")
    print("MANIFEST_PRIOR_SOURCES_MISSING_SAMPLE=" + json.dumps(missing_sources[:30], ensure_ascii=False))
    print(f"MANIFEST_EXTRACTED_STATE_REGRESSIONS={len(state_regressions)}")
    print("MANIFEST_STATE_REGRESSION_SAMPLE=" + json.dumps(state_regressions[:30], ensure_ascii=False))
    print(f"MANIFEST_CHANGED_REVISIONS={changed_revisions}")
    print(f"MANIFEST_PRIOR_REVISION_ARCHIVES_MISSING={len(missing_archives)}")
    print("MANIFEST_MISSING_ARCHIVE_SAMPLE=" + json.dumps(missing_archives[:30], ensure_ascii=False))
    return ([{"kind": "missing_source", "source": source} for source in missing_sources]
            + [{"kind": "state_regression", **item} for item in state_regressions]
            + [{"kind": "missing_archive", **item} for item in missing_archives])

def shape(value):
    if isinstance(value, dict):
        return {"type": "object", "keys": len(value), "keys_sample": sorted(value)[:30]}
    if isinstance(value, list):
        return {"type": "array", "items": len(value)}
    return {"type": type(value).__name__}


def main() -> int:
    manifest_errors = audit_manifest_preservation()
    print(f"Loading pre-recovery revision {BEFORE}...", flush=True)
    before = load_revision(BEFORE)
    print(f"Loading current revision {AFTER}...", flush=True)
    after = load_revision(AFTER)
    print("BEFORE_SHAPE=" + json.dumps(shape(before), sort_keys=True))
    print("AFTER_SHAPE=" + json.dumps(shape(after), sort_keys=True))

    before_counts = before.get("counts", {})
    after_counts = after.get("counts", {})
    regressions = {
        key: {"before": value, "after": after_counts.get(key)}
        for key, value in before_counts.items()
        if isinstance(value, (int, float))
        and (not isinstance(after_counts.get(key), (int, float)) or after_counts[key] < value)
    }
    print("COUNTS_BEFORE=" + json.dumps(before_counts, sort_keys=True))
    print("COUNTS_AFTER=" + json.dumps(after_counts, sort_keys=True))
    print("COUNT_REGRESSIONS=" + json.dumps(regressions, sort_keys=True))

    old_decisions = before.get("decisions", [])
    new_decisions = after.get("decisions", [])
    old_keys = {
        item.get("capability_key") for item in old_decisions
        if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
    }
    new_keys = {
        item.get("capability_key") for item in new_decisions
        if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
    }
    missing = sorted(old_keys - new_keys)
    print(f"DECISIONS_LENGTH_BEFORE={len(old_decisions)}")
    print(f"DECISIONS_LENGTH_AFTER={len(new_decisions)}")
    print(f"DECISION_IDENTITIES_BEFORE={len(old_keys)}")
    print(f"DECISION_IDENTITIES_AFTER={len(new_keys)}")
    print("MISSING_PRIOR_DECISION_IDENTITIES=" + json.dumps(missing[:100], ensure_ascii=False))

    # A missing current decision is acceptable only if its exact source revision
    # and evidence file remain archived in Git history.
    prior_by_key = {
        item.get("capability_key"): item for item in old_decisions
        if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
    }
    missing_evidence = []
    checked_archives = 0
    for key in missing:
        prior_evidence = prior_by_key[key].get("evidence", [])
        if not isinstance(prior_evidence, list) or not prior_evidence:
            missing_evidence.append({"key": key, "reason": "prior decision has no evidence records to verify"})
            continue
        verified_for_decision = 0
        for evidence in prior_evidence:
            if not isinstance(evidence, dict):
                missing_evidence.append({"key": key, "reason": "malformed prior evidence record"})
                continue
            source = evidence.get("source")
            revision = evidence.get("source_revision")
            file_path = evidence.get("file")
            expected_hash = evidence.get("content_sha256")
            if not all(isinstance(value, str) and value for value in (source, revision, file_path)):
                missing_evidence.append({"key": key, "reason": "incomplete evidence identity"})
                continue
            slug = source.removeprefix("github:").replace("/", "_")
            candidates = [
                f"COLLECTION/AUTO/EXTRACTED/HISTORY/{slug}__{revision}.json",
                f"COLLECTION/AUTO/EXTRACTED/{slug}.json",
            ]
            found = False
            for candidate in candidates:
                proc = subprocess.run(["git", "show", f"HEAD:{candidate}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if proc.returncode:
                    continue
                try:
                    artifact = json.loads(proc.stdout)
                except Exception:
                    continue
                if artifact.get("canonical_source") != source or artifact.get("revision_sha") != revision:
                    continue
                for item in artifact.get("files", []):
                    if not isinstance(item, dict) or item.get("path") != file_path:
                        continue
                    if expected_hash and item.get("content_sha256") != expected_hash:
                        continue
                    found = True
                    checked_archives += 1
                    verified_for_decision += 1
                    break
                if found:
                    break
            if not found:
                missing_evidence.append({"key": key, "source": source, "revision": revision, "file": file_path})
        if verified_for_decision == 0 and not any(
            item.get("key") == key for item in missing_evidence
        ):
            missing_evidence.append({"key": key, "reason": "no prior evidence record could be verified"})

    print(f"ARCHIVED_PRIOR_EVIDENCE_VERIFIED={checked_archives}")
    print(f"PRIOR_EVIDENCE_NOT_FOUND={len(missing_evidence)}")
    print("PRIOR_EVIDENCE_NOT_FOUND_SAMPLE=" + json.dumps(missing_evidence[:50], ensure_ascii=False))

    if manifest_errors or regressions or missing_evidence or len(old_keys) != len(old_decisions) or len(new_keys) != len(new_decisions):
        print("NON_REGRESSION=FAIL")
        print("Conclusion: prior evidence or count invariants require investigation.")
        return 2

    if before == after:
        print("NON_REGRESSION=PASS (exact semantic equality)")
    else:
        print("NON_REGRESSION=PASS (counts did not regress; removed active decisions are preserved by exact historical evidence)")
    print("Conclusion: no prior evidence or recorded count was lost; regenerated READY may reflect newer source revisions.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"AUDIT_ERROR={type(exc).__name__}: {exc}")
        raise SystemExit(3)
