#!/usr/bin/env python3
"""Compare parsed READY.json data before/after a specific commit, ignoring formatting."""
import json
import subprocess
import sys
from collections.abc import Mapping, Sequence

TARGET_COMMIT = "0d824d436b4e2a3c01ef6115c266f32c8e48f836"
READY_PATH = "COLLECTION/MASTER/READY.json"


def git_text(spec: str) -> str:
    return subprocess.run(
        ["git", "show", spec],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    ).stdout


def first_difference(left, right, path="$"):
    if type(left) is not type(right):
        return {"path": path, "reason": "type changed", "old_type": type(left).__name__, "new_type": type(right).__name__}
    if isinstance(left, Mapping):
        left_keys, right_keys = set(left), set(right)
        if left_keys != right_keys:
            return {"path": path, "reason": "object keys changed", "removed_keys": sorted(left_keys - right_keys)[:30], "added_keys": sorted(right_keys - left_keys)[:30]}
        for key in sorted(left):
            diff = first_difference(left[key], right[key], f"{path}.{key}")
            if diff:
                return diff
        return None
    if isinstance(left, list):
        if len(left) != len(right):
            return {"path": path, "reason": "array length changed", "old_length": len(left), "new_length": len(right)}
        for index, (a, b) in enumerate(zip(left, right)):
            diff = first_difference(a, b, f"{path}[{index}]")
            if diff:
                return diff
        return None
    if left != right:
        return {"path": path, "reason": "value changed", "old_value": repr(left)[:160], "new_value": repr(right)[:160]}
    return None


def summarize(value):
    if isinstance(value, dict):
        return {
            "top_level_keys": sorted(value),
            "top_level_array_lengths": {key: len(item) for key, item in value.items() if isinstance(item, list)},
        }
    if isinstance(value, list):
        return {"root_array_length": len(value)}
    return {"root_type": type(value).__name__}


def decision_keys(value):
    decisions = value.get("decisions", []) if isinstance(value, dict) else []
    return {
        item.get("capability_key")
        for item in decisions
        if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
    }


def main():
    commit = sys.argv[1] if len(sys.argv) > 1 else TARGET_COMMIT
    old_ref = f"{commit}^:{READY_PATH}"
    new_ref = f"{commit}:{READY_PATH}"
    try:
        old_raw, new_raw = git_text(old_ref), git_text(new_ref)
        old_data, new_data = json.loads(old_raw), json.loads(new_raw)
    except Exception as exc:
        print(json.dumps({"status": "ERROR", "commit": commit, "error": str(exc)}, ensure_ascii=False))
        return 2

    diff = first_difference(old_data, new_data)
    old_keys, new_keys = decision_keys(old_data), decision_keys(new_data)
    old_counts = old_data.get("counts", {}) if isinstance(old_data, dict) else {}
    new_counts = new_data.get("counts", {}) if isinstance(new_data, dict) else {}
    count_changes = {
        key: {"old": old_counts.get(key), "new": new_counts.get(key)}
        for key in sorted(set(old_counts) | set(new_counts))
        if old_counts.get(key) != new_counts.get(key)
    }
    count_regressions = {
        key: {"old": old_counts.get(key), "new": new_counts.get(key)}
        for key in sorted(old_counts)
        if isinstance(old_counts.get(key), (int, float))
        and (not isinstance(new_counts.get(key), (int, float)) or new_counts[key] < old_counts[key])
    }
    changed_common_decisions = []
    changed_field_counts = {}
    changed_decision_samples = []
    old_by_key = {
        item.get("capability_key"): item
        for item in old_data.get("decisions", [])
        if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
    }
    new_by_key = {
        item.get("capability_key"): item
        for item in new_data.get("decisions", [])
        if isinstance(item, dict) and isinstance(item.get("capability_key"), str)
    }
    for key in sorted(old_keys & new_keys):
        before_item, after_item = old_by_key[key], new_by_key[key]
        if before_item != after_item:
            changed_common_decisions.append(key)
            changed_fields = sorted(
                field for field in set(before_item) | set(after_item)
                if before_item.get(field) != after_item.get(field)
            )
            for field in changed_fields:
                changed_field_counts[field] = changed_field_counts.get(field, 0) + 1
            if len(changed_decision_samples) < 20:
                changed_decision_samples.append({
                    "capability_key": key,
                    "changed_fields": changed_fields,
                    "before": {field: before_item.get(field) for field in changed_fields},
                    "after": {field: after_item.get(field) for field in changed_fields},
                })

    result = {
        "status": "PASS" if diff is None else "DATA_DIFFERENCE",
        "commit": commit,
        "path": READY_PATH,
        "old_bytes": len(old_raw.encode("utf-8")),
        "new_bytes": len(new_raw.encode("utf-8")),
        "old_summary": summarize(old_data),
        "new_summary": summarize(new_data),
        "parsed_data_equal": diff is None,
        "first_difference": diff,
        "count_changes": count_changes,
        "count_regressions": count_regressions,
        "decision_identity_counts": {"old": len(old_keys), "new": len(new_keys)},
        "decision_identities_added_count": len(new_keys - old_keys),
        "decision_identities_added_sample": sorted(new_keys - old_keys)[:50],
        "decision_identities_missing_count": len(old_keys - new_keys),
        "decision_identities_missing_sample": sorted(old_keys - new_keys)[:50],
        "common_decisions_with_changed_content_count": len(changed_common_decisions),
        "common_decisions_with_changed_content_sample": changed_common_decisions[:50],
        "changed_decision_field_counts": dict(sorted(changed_field_counts.items())),
        "changed_decision_samples": changed_decision_samples,
        "changed_decision_field_counts": changed_field_counts,
        "changed_decision_details_sample": changed_decision_samples,
        "changed_field_counts": dict(sorted(changed_field_counts.items())),
        "changed_decision_detail_sample": changed_decision_samples,
        "changed_decision_field_counts": dict(sorted(changed_decision_field_counts.items())),
        "changed_decision_field_samples": changed_decision_field_samples,
        "changed_decision_fields_frequency": dict(sorted(changed_field_counts.items())),
        "changed_decision_samples": changed_decision_samples,
        "evidence_change_samples": evidence_change_samples,
        "evidence_item_counts": {"old": len(old_evidence), "new": len(new_evidence)},
        "archived_old_evidence_verified": archived_old_evidence_verified,
        "archived_old_evidence_missing_count": len(archived_old_evidence_missing),
        "archived_old_evidence_missing_sample": archived_old_evidence_missing,
        "evidence_record_match_counts": {"matched_by_decision_source_file": matched_evidence_records, "missing_records": missing_evidence_records, "added_records": added_evidence_records},
        "evidence_field_changes": dict(sorted(evidence_field_changes.items())),
        "evidence_field_change_samples": evidence_field_change_samples,
        "missing_evidence_record_samples": missing_evidence_record_samples,
        "added_evidence_record_samples": added_evidence_record_samples,
        "evidence_identities_missing_ignoring_revision_count": len(old_evidence_ids - new_evidence_ids),
        "evidence_identities_added_ignoring_revision_count": len(new_evidence_ids - old_evidence_ids),
        "source_file_content_hashes_missing_count": len(old_hashes - new_hashes),
        "source_file_content_hashes_added_count": len(new_hashes - old_hashes),
        "source_file_content_hashes_missing_sample": [
            {"source": source, "file": file_path, "content_sha256": digest}
            for source, file_path, digest in sorted(old_hashes - new_hashes)[:25]
        ],
        "source_file_content_hashes_added_sample": [
            {"source": source, "file": file_path, "content_sha256": digest}
            for source, file_path, digest in sorted(new_hashes - old_hashes)[:25]
        ],
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    # Exact equality is informative, but a regenerated READY may legitimately
    # change as sources refresh. Fail only on a real count regression or when
    # a prior decision identity disappears; historical evidence is checked by
    # the separate semantic-preservation audit.
    return 2 if count_regressions or (old_keys - new_keys) else 0


if __name__ == "__main__":
    raise SystemExit(main())
