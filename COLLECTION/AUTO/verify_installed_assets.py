#!/usr/bin/env python3
"""Fail-closed post-install verification bridge.

Turns successful installations into explicit verification candidates.
It never promotes arbitrary third-party source to runtime-callable status.
Callable promotion still requires a real local entrypoint and execution evidence.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "COLLECTION/MASTER/INSTALLATION-REPORT.json"
INSTALLED = ROOT / "COLLECTION/INSTALLED"
OUT = ROOT / "COLLECTION/VERIFICATION/INSTALLED-QUEUE.json"


def main() -> int:
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    items = []
    counts = {}

    for item in report.get("results", []):
        if item.get("status") not in {"INSTALLED", "ALREADY_INSTALLED"}:
            continue

        repo = item.get("repo", "")
        target = Path(item.get("path", ""))
        if not target.is_absolute():
            target = ROOT / target

        marker = target / ".collection-install.json"
        checks = {
            "path_exists": target.is_dir(),
            "marker_exists": marker.is_file(),
            "git_dir_absent": not (target / ".git").exists(),
            "non_empty": target.is_dir() and any(target.iterdir()),
        }

        marker_data = {}
        if checks["marker_exists"]:
            try:
                marker_data = json.loads(marker.read_text(encoding="utf-8"))
            except Exception:
                checks["marker_valid"] = False
            else:
                checks["marker_valid"] = (
                    marker_data.get("repo") == repo
                    and marker_data.get("revision") == item.get("revision")
                    and marker_data.get("status") == "INSTALLED"
                )
        else:
            checks["marker_valid"] = False

        verified = all(checks.values())
        state = "READY_FOR_VERIFICATION" if verified else "INSTALLATION_INTEGRITY_FAILED"
        callable_state = "NOT_CALLABLE_UNTIL_RUNTIME_ENTRYPOINT_AND_EXECUTION_EVIDENCE"

        row = {
            "repo": repo,
            "revision": item.get("revision"),
            "license": item.get("license"),
            "installed_path": str(target.relative_to(ROOT)) if target.is_relative_to(ROOT) else str(target),
            "verification_state": state,
            "callable_state": callable_state,
            "checks": checks,
            "next_gate": (
                "identify narrow entrypoint/adapter, register only after smoke execution evidence"
                if verified else "repair installation integrity before any promotion"
            ),
        }
        items.append(row)
        counts[state] = counts.get(state, 0) + 1

    payload = {
        "schema_version": "collection-installed-verification/v1",
        "rule": "installed is not callable; callable requires explicit entrypoint and execution evidence",
        "candidate_count": len(items),
        "counts": counts,
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    # Publish a complete report or keep the previous valid report on interruption.
    tmp = OUT.with_name(OUT.name + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        handle.flush()
        import os
        os.fsync(handle.fileno())
    tmp.replace(OUT)

    print(json.dumps({"candidate_count": len(items), "counts": counts}, sort_keys=True))
    return 0 if not counts.get("INSTALLATION_INTEGRITY_FAILED") else 1


if __name__ == "__main__":
    raise SystemExit(main())
