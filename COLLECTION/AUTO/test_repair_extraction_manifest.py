#!/usr/bin/env python3
"""Regression tests for manifest license backfill from revision-validated artifacts."""
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "COLLECTION/AUTO"))
from repair_extraction_manifest import repair_manifest


def test_backfills_license_only_after_artifact_identity_and_revision_validate():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        extracted = root / "COLLECTION/AUTO/EXTRACTED"
        extracted.mkdir(parents=True)
        artifact = extracted / "owner_project.json"
        artifact.write_text(json.dumps({
            "canonical_source": "github:owner/project",
            "revision_sha": "a" * 40,
            "state": "extracted",
            "license": "MIT",
            "files": [{"path": "README.md", "content": "# project"}],
        }), encoding="utf-8")
        manifest = extracted / "MANIFEST.json"
        manifest.write_text(json.dumps({
            "sources": [{
                "canonical_source": "github:owner/project",
                "revision_sha": "a" * 40,
                "state": "extracted",
                "path": str(artifact),
                "files_extracted": 1,
            }],
        }), encoding="utf-8")

        report = repair_manifest(manifest_path=manifest, root=root, extracted_root=extracted)
        updated = json.loads(manifest.read_text(encoding="utf-8"))
        row = updated["sources"][0]

        assert report["valid_extracted_artifacts"] == 1
        assert report["backfilled_license_ids"] == 1
        assert row["license"] == "MIT"
        assert row["license_source"] == "github_repository_metadata_at_extraction"


def test_does_not_backfill_license_from_wrong_revision():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        extracted = root / "COLLECTION/AUTO/EXTRACTED"
        extracted.mkdir(parents=True)
        artifact = extracted / "owner_project.json"
        artifact.write_text(json.dumps({
            "canonical_source": "github:owner/project",
            "revision_sha": "b" * 40,
            "state": "extracted",
            "license": "MIT",
            "files": [{"path": "README.md", "content": "# project"}],
        }), encoding="utf-8")
        manifest = extracted / "MANIFEST.json"
        manifest.write_text(json.dumps({
            "sources": [{
                "canonical_source": "github:owner/project",
                "revision_sha": "a" * 40,
                "state": "extracted",
                "path": str(artifact),
                "files_extracted": 1,
            }],
        }), encoding="utf-8")

        report = repair_manifest(manifest_path=manifest, root=root, extracted_root=extracted)
        updated = json.loads(manifest.read_text(encoding="utf-8"))
        row = updated["sources"][0]

        assert report["backfilled_license_ids"] == 0
        assert row["state"] == "BLOCKED_EXTERNAL_ACCESS"
        assert "license" not in row


if __name__ == "__main__":
    test_backfills_license_only_after_artifact_identity_and_revision_validate()
    test_does_not_backfill_license_from_wrong_revision()
    print("manifest license backfill: PASS")
