#!/usr/bin/env python3
"""Fail the Collection cycle after persisting install evidence if no install was verified."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "COLLECTION/MASTER/INSTALLATION-REPORT.json"
QUEUE = ROOT / "COLLECTION/VERIFICATION/INSTALLED-QUEUE.json"
FAILED_STATUSES = {"FAILED", "BLOCKED_REVISION_CONFLICT"}


def validate_outcome(report: dict, queue: dict) -> dict:
    results = report.get("results") if isinstance(report, dict) else None
    items = queue.get("items") if isinstance(queue, dict) else None
    if not isinstance(results, list) or not isinstance(items, list):
        raise ValueError("installation report results and verification queue items must be lists")

    successful = [
        item for item in results
        if isinstance(item, dict) and item.get("status") in {"INSTALLED", "ALREADY_INSTALLED"}
    ]
    failures = [
        item for item in results
        if isinstance(item, dict) and item.get("status") in FAILED_STATUSES
    ]
    if not successful:
        raise ValueError("no asset was installed or verified as already installed")
    if failures:
        detail = ", ".join(f"{item.get('repo', 'unknown')}:{item.get('status')}" for item in failures[:10])
        raise ValueError(f"installation failures remain in persisted report: {detail}")

    expected = {(item.get("repo"), item.get("revision")) for item in successful}
    actual = {
        (item.get("repo"), item.get("revision"))
        for item in items
        if isinstance(item, dict) and item.get("verification_state") == "READY_FOR_VERIFICATION"
    }
    # Report an explicit integrity failure before comparing the queue's size.
    # Otherwise an INSTALLATION_INTEGRITY_FAILED row is obscured as a generic count mismatch.
    if any(
        not isinstance(item, dict) or item.get("verification_state") != "READY_FOR_VERIFICATION"
        for item in items
    ):
        raise ValueError("installation integrity failures remain in the verification queue")
    if expected != actual:
        raise ValueError(
            f"verification queue mismatch: successful={len(expected)}, ready_for_verification={len(actual)}"
        )

    return {
        "status": "PASS",
        "installed_or_already_installed": len(successful),
        "ready_for_verification": len(actual),
        "blocked_by_size": sum(
            1 for item in results
            if isinstance(item, dict) and item.get("status") == "BLOCKED_SIZE"
        ),
    }


def main() -> int:
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    queue = json.loads(QUEUE.read_text(encoding="utf-8"))
    result = validate_outcome(report, queue)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
