#!/usr/bin/env python3
"""Regression tests for strict JSON and known JSONC configuration files."""
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

from audit_current_collection_json import parse_json_document, strip_jsonc


class JsonAuditParsingTests(unittest.TestCase):
    def test_strict_json_keeps_strict_mode(self):
        value, mode = parse_json_document("ordinary.json", b'{"a": 1, "url": "https://example.com/a//b"}')
        self.assertEqual(mode, "JSON")
        self.assertEqual(value["url"], "https://example.com/a//b")

    def test_devcontainer_jsonc_comments_and_trailing_commas(self):
        raw = b'''// leading comment
{
  "url": "https://example.com/a//b",
  "features": {"sample": {},},
  "forwardPorts": [8080,], // trailing comment
}
'''
        value, mode = parse_json_document(".devcontainer/devcontainer.json", raw)
        self.assertEqual(mode, "JSONC")
        self.assertEqual(value["url"], "https://example.com/a//b")
        self.assertEqual(value["forwardPorts"], [8080])

    def test_comment_markers_inside_strings_are_preserved(self):
        text = '{"a":"// not a comment", "b":"/* not a comment */"}'
        self.assertEqual(json.loads(strip_jsonc(text)), {"a": "// not a comment", "b": "/* not a comment */"})

    def test_jsonc_fallback_is_limited_to_devcontainer_filename(self):
        with self.assertRaises(json.JSONDecodeError):
            parse_json_document("ordinary.json", b'{"a": 1,}')

    def test_malformed_devcontainer_jsonc_still_fails(self):
        with self.assertRaises(json.JSONDecodeError):
            parse_json_document(".devcontainer/devcontainer.json", b'{"a": }')

    def test_preserved_hyperswitch_devcontainer_source_parses_as_jsonc(self):
        path = ROOT / "COLLECTION" / "INSTALLED" / "juspay__hyperswitch" / ".devcontainer" / "devcontainer.json"
        value, mode = parse_json_document(path, path.read_bytes())
        self.assertIn(mode, {"JSON", "JSONC"})
        self.assertEqual(value["forwardPorts"], [8080])


if __name__ == "__main__":
    unittest.main()
