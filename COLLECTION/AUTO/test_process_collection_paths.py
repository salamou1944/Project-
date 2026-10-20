#!/usr/bin/env python3
"""Regression tests for repository-root path resolution and sticky quarantine.
The focused workflow also reruns the previously failing full policy gate.
"""
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SOURCE = Path(__file__).resolve().with_name("process_collection.py")
SPEC = importlib.util.spec_from_file_location("process_collection_under_test", SOURCE)
PIPELINE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PIPELINE)


class CollectionPathTests(unittest.TestCase):
    def test_paths_are_anchored_to_repository_not_cwd(self):
        expected_root = Path(__file__).resolve().parents[2]
        self.assertEqual(PIPELINE.REPO_ROOT, expected_root)
        self.assertEqual(PIPELINE.EXTRACTED, expected_root / "COLLECTION/AUTO/EXTRACTED")
        self.assertEqual(PIPELINE.MASTER, expected_root / "COLLECTION/MASTER")
        self.assertEqual(PIPELINE.VERIFY, expected_root / "COLLECTION/VERIFICATION")
        with tempfile.TemporaryDirectory() as unrelated_cwd:
            previous = Path.cwd()
            try:
                os.chdir(unrelated_cwd)
                self.assertTrue(PIPELINE.MASTER.is_absolute())
                self.assertEqual(PIPELINE.QUARANTINE_LOCKS, expected_root / "COLLECTION/MASTER/QUARANTINE-LOCKS.json")
            finally:
                os.chdir(previous)

    def test_relative_manifest_artifact_paths_resolve_from_repo_root(self):
        with tempfile.TemporaryDirectory() as temporary_root, tempfile.TemporaryDirectory() as unrelated_cwd:
            root = Path(temporary_root)
            extracted = root / "COLLECTION/AUTO/EXTRACTED"
            extracted.mkdir(parents=True)
            artifact = extracted / "source.json"
            artifact.write_text(json.dumps({
                "state": "extracted",
                "canonical_source": "github:owner/repo",
                "revision_sha": "a" * 40,
                "files": []
            }), encoding="utf-8")
            manifest = {
                "sources": [{
                    "state": "extracted",
                    "path": "COLLECTION/AUTO/EXTRACTED/source.json",
                    "canonical_source": "github:owner/repo",
                    "revision_sha": "a" * 40
                }]
            }
            (extracted / "MANIFEST.json").write_text(json.dumps(manifest), encoding="utf-8")
            previous_root, previous_extracted = PIPELINE.REPO_ROOT, PIPELINE.EXTRACTED
            previous_cwd = Path.cwd()
            try:
                PIPELINE.REPO_ROOT = root
                PIPELINE.EXTRACTED = extracted
                os.chdir(unrelated_cwd)
                self.assertEqual(PIPELINE.source_files_from_manifest(), [artifact.resolve()])
            finally:
                os.chdir(previous_cwd)
                PIPELINE.REPO_ROOT, PIPELINE.EXTRACTED = previous_root, previous_extracted

    def test_existing_quarantine_lock_remains_locked(self):
        locks = PIPELINE.load_quarantine_locks()
        self.assertEqual(locks["evaluation-reliability-test-runtime"]["status"], "QUARANTINED")
        self.assertTrue(PIPELINE.is_quarantined(
            "evaluation-reliability-test-runtime",
            [],
            previous_quarantine_keys=set(),
            quarantine_locks=locks
        ))


if __name__ == "__main__":
    unittest.main()
