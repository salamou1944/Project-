#!/usr/bin/env python3
"""Regression test: READY.json remains readable and round-trips without data loss."""
import json
import tempfile
from pathlib import Path

from process_collection import atomic_json_write

# Manifest inventory regression: retained prior sources are additional to the
# currently discovered repository/gist counts and must not be mistaken for drift.
from collection_state_guard import validate_manifest_source_count


def test_manifest_inventory_counts():
    valid = {
        "repo_count": 2981,
        "gist_count": 0,
        "preserved_sources_after_refresh_failure": 2,
        "sources": [{}] * 2983,
    }
    assert validate_manifest_source_count(valid) == 2983

    with_gists = {
        "repo_count": 10,
        "gist_count": 3,
        "preserved_sources_after_refresh_failure": 2,
        "sources": [{}] * 15,
    }
    assert validate_manifest_source_count(with_gists) == 15

    inconsistent = {
        "repo_count": 10,
        "gist_count": 0,
        "preserved_sources_after_refresh_failure": 2,
        "sources": [{}] * 11,
    }
    try:
        validate_manifest_source_count(inconsistent)
    except SystemExit as exc:
        assert "disagree with discovered inventory" in str(exc)
    else:
        raise AssertionError("inconsistent manifest must fail closed")




def main() -> None:
    test_manifest_inventory_counts()
    payload = {
        "generated_at": "2026-10-10T00:00:00+00:00",
        "decisions": [
            {"capability_key": "sample capability", "description": "preserve meaningful spaces", "evidence_count": 2},
            {"capability_key": "second sample", "description": "keep commas in arrays", "evidence_count": 1},
        ],
    }
    with tempfile.TemporaryDirectory() as directory:
        ready = Path(directory) / "READY.json"
        atomic_json_write(ready, payload)
        rendered = ready.read_text(encoding="utf-8")
        assert json.loads(rendered) == payload
        assert ": " in rendered and "\n  " in rendered
        assert rendered.endswith("\n")

    print("READY.json readable JSON round-trip: PASS")


if __name__ == "__main__":
    main()
