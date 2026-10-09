#!/usr/bin/env python3
"""Regression tests for stale/empty extraction cache handling."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "COLLECTION/AUTO"))
from intelligent_extract import has_usable_files


def main():
    assert has_usable_files({"files": [{"path": "README.md", "content": "# valid"}]})
    assert not has_usable_files({"files": []})
    assert not has_usable_files({"files": [{"path": "README.md", "error": "403"}]})
    assert not has_usable_files({"files": [{"path": "README.md", "error": "403", "content": "error page"}]})
    assert not has_usable_files({"files": [{"path": "README.md", "content": ""}]})
    assert not has_usable_files(None)
    print("extraction cache policy: PASS (usable artifacts only)")


if __name__ == "__main__":
    main()

# Regression: preserved_record must count files from the validated artifact data, not an undefined variable.
