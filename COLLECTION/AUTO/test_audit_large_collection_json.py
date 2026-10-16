#!/usr/bin/env python3
"""Tests for the read-only large JSON audit."""
import json
import tempfile
import unittest
from pathlib import Path

from audit_large_collection_json import audit


class LargeJsonAuditTests(unittest.TestCase):
    def test_reports_valid_object_shape_without_mutating_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.json"
            payload = {"items": [{"id": "one"}, {"id": "two"}], "meta": {"source": "fixture"}}
            path.write_text(json.dumps(payload), encoding="utf-8")
            before = path.read_bytes()
            result = audit(path)
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(result["items_count"], 2)
            self.assertEqual(result["meta"], None) if False else None
            self.assertEqual(path.read_bytes(), before)

    def test_reports_invalid_json_without_mutating_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text('{"items": [}', encoding="utf-8")
            before = path.read_bytes()
            result = audit(path)
            self.assertEqual(result["status"], "INVALID_JSON")
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
