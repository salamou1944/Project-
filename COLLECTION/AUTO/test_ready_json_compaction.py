#!/usr/bin/env python3
"""Regression test: compact READY.json without changing its JSON data."""
import json
import tempfile
from pathlib import Path

from process_collection import atomic_json_write


def main() -> None:
    payload = {
        "generated_at": "2026-10-10T00:00:00+00:00",
        "decisions": [
            {"capability_key": "sample capability", "description": "preserve meaningful spaces", "evidence_count": 2}
        ],
    }
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        ready = root / "READY.json"
        regular = root / "REGULAR.json"
        atomic_json_write(ready, payload)
        atomic_json_write(regular, payload)

        compact_text = ready.read_text(encoding="utf-8")
        pretty_text = regular.read_text(encoding="utf-8")
        assert json.loads(compact_text) == payload
        assert json.loads(pretty_text) == payload
        assert ready.stat().st_size < regular.stat().st_size
        assert ": " not in compact_text and ", " not in compact_text
        assert ": " in pretty_text and ", " in pretty_text

    print("READY.json compact serialization: PASS (round-trip preserved; formatting whitespace removed)")


if __name__ == "__main__":
    main()
