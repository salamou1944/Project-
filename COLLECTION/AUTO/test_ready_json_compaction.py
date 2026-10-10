#!/usr/bin/env python3
"""Regression test: READY.json remains readable and round-trips without data loss."""
import json
import tempfile
from pathlib import Path

from process_collection import atomic_json_write


def main() -> None:
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
