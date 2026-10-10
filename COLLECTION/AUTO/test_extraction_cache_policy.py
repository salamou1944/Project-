#!/usr/bin/env python3
"""Regression tests for stale/empty extraction cache handling."""
import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "COLLECTION/AUTO"))
from intelligent_extract import archive_prior_revision, has_usable_files


def test_preserved_record_source_is_bound_to_artifact_data():
    source = (ROOT / "COLLECTION/AUTO/intelligent_extract.py").read_text(encoding="utf-8")
    start = source.index("def preserved_record(")
    end = source.index("\ndef main()", start)
    body = source[start:end]
    assert 'for f in data.get("files", [])' in body
    assert "for f in files" not in body


def test_prior_revision_is_archived_before_replacement():
    old = {
        "repo": "owner/repo",
        "revision_sha": "old123",
        "state": "extracted",
        "files": [{"path": "src/valuable.py", "content": "preserve-me"}],
    }
    new = {"revision_sha": "new456"}
    with TemporaryDirectory() as temp:
        history = Path(temp) / "HISTORY"
        archived = archive_prior_revision(Path(temp) / "owner_repo.json", old, new, history)
        assert archived is not None
        snapshot = json.loads(Path(archived).read_text(encoding="utf-8"))
        assert snapshot["revision_sha"] == "old123"
        assert snapshot["files"][0]["content"] == "preserve-me"
        # Existing historical snapshots are immutable; never overwrite them.
        Path(archived).write_text('{"sentinel": true}', encoding="utf-8")
        archive_prior_revision(Path(temp) / "owner_repo.json", old, new, history)
        assert json.loads(Path(archived).read_text(encoding="utf-8")) == {"sentinel": True}
    assert archive_prior_revision(Path("owner_repo.json"), old, old) is None
    assert archive_prior_revision(Path("owner_repo.json"), {"state": "blocked"}, new) is None

def main():
    assert has_usable_files({"files": [{"path": "README.md", "content": "# valid"}]})
    assert not has_usable_files({"files": []})
    assert not has_usable_files({"files": [{"path": "README.md", "error": "403"}]})
    assert not has_usable_files({"files": [{"path": "README.md", "error": "403", "content": "error page"}]})
    assert not has_usable_files({"files": [{"path": "README.md", "content": ""}]})
    assert not has_usable_files(None)
    test_preserved_record_source_is_bound_to_artifact_data()
    test_prior_revision_is_archived_before_replacement()
    print("extraction cache policy: PASS (usable cache + preservation fallback regression)")


if __name__ == "__main__":
    main()


