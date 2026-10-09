#!/usr/bin/env python3
"""Regression tests for stale/empty extraction cache handling."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "COLLECTION/AUTO"))
from intelligent_extract import has_usable_files


def test_preserved_record_source_is_bound_to_artifact_data():
    source = (ROOT / "COLLECTION/AUTO/intelligent_extract.py").read_text(encoding="utf-8")
    start = source.index("def preserved_record(")
    end = source.index("\ndef main()", start)
    body = source[start:end]
    assert 'for f in data.get("files", [])' in body
    assert "for f in files" not in body

def main():
    assert has_usable_files({"files": [{"path": "README.md", "content": "# valid"}]})
    assert not has_usable_files({"files": []})
    assert not has_usable_files({"files": [{"path": "README.md", "error": "403"}]})
    assert not has_usable_files({"files": [{"path": "README.md", "error": "403", "content": "error page"}]})
    assert not has_usable_files({"files": [{"path": "README.md", "content": ""}]})
    assert not has_usable_files(None)
    test_preserved_record_source_is_bound_to_artifact_data()
    print("extraction cache policy: PASS (usable cache + preservation fallback regression)")


if __name__ == "__main__":
    main()


