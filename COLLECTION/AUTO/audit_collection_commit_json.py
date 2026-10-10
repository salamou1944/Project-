#!/usr/bin/env python3
"""Read-only semantic comparison of every JSON file changed by a target commit."""
import json
import subprocess
import sys
from collections.abc import Mapping

DEFAULT_COMMIT = "0d824d436b4e2a3c01ef6115c266f32c8e48f836"


def run_git(*args, check=True):
    return subprocess.run(
        ["git", *args], check=check, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=False,
    )


def first_difference(a, b, path="$"):
    if type(a) is not type(b):
        return {"path": path, "reason": "type changed",
                "old_type": type(a).__name__, "new_type": type(b).__name__}
    if isinstance(a, Mapping):
        ak, bk = set(a), set(b)
        if ak != bk:
            return {"path": path, "reason": "object keys changed",
                    "removed_keys": sorted(ak-bk)[:20],
                    "added_keys": sorted(bk-ak)[:20]}
        for key in sorted(a):
            diff = first_difference(a[key], b[key], f"{path}.{key}")
            if diff:
                return diff
        return None
    if isinstance(a, list):
        if len(a) != len(b):
            return {"path": path, "reason": "array length changed",
                    "old_length": len(a), "new_length": len(b)}
        for i, (x, y) in enumerate(zip(a, b)):
            diff = first_difference(x, y, f"{path}[{i}]")
            if diff:
                return diff
        return None
    if a != b:
        return {"path": path, "reason": "value changed",
                "old_value": repr(a)[:100], "new_value": repr(b)[:100]}
    return None


def summary(value):
    if isinstance(value, dict):
        return {
            "root_type": "object",
            "keys": sorted(value)[:30],
            "array_lengths": {k: len(v) for k, v in value.items() if isinstance(v, list)},
            "numeric_counts": {k: v for k, v in value.items()
                               if isinstance(v, (int, float)) and not isinstance(v, bool)},
        }
    if isinstance(value, list):
        return {"root_type": "array", "length": len(value)}
    return {"root_type": type(value).__name__}


def main():
    commit = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMIT
    try:
        run_git("cat-file", "-e", f"{commit}^{{commit}}")
        names = run_git("diff-tree", "--no-commit-id", "--name-status", "-r", commit).stdout.decode().splitlines()
        files = []
        for row in names:
            parts = row.split("\t")
            status, path = parts[0], parts[-1]
            if not path.lower().endswith(".json"):
                continue
            if status.startswith("R") or status.startswith("C"):
                path = parts[-1]
            old_raw = new_raw = None
            old_data = new_data = None
            if not status.startswith("A"):
                p = run_git("show", f"{commit}^:{path}", check=False)
                if p.returncode == 0:
                    old_raw = p.stdout
                    old_data = json.loads(old_raw)
            if not status.startswith("D"):
                p = run_git("show", f"{commit}:{path}", check=False)
                if p.returncode == 0:
                    new_raw = p.stdout
                    new_data = json.loads(new_raw)
            diff = None if old_data is None or new_data is None else first_difference(old_data, new_data)
            files.append({
                "path": path, "change_status": status,
                "old_bytes": len(old_raw) if old_raw is not None else None,
                "new_bytes": len(new_raw) if new_raw is not None else None,
                "semantic_equal": diff is None if old_data is not None and new_data is not None else False,
                "old_summary": summary(old_data) if old_data is not None else None,
                "new_summary": summary(new_data) if new_data is not None else None,
                "first_difference": diff,
            })
        result = {
            "status": "PASS" if all(x["semantic_equal"] for x in files) else "DIFFERENCES_REPORTED",
            "commit": commit,
            "json_files_checked": len(files),
            "semantic_equal_files": sum(x["semantic_equal"] for x in files),
            "files_with_semantic_changes_or_additions_deletions": sum(not x["semantic_equal"] for x in files),
            "files": files,
        }
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0
    except Exception as exc:
        print(json.dumps({"status": "ERROR", "commit": commit,
                          "error": f"{type(exc).__name__}: {exc}"}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
