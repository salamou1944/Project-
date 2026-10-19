#!/usr/bin/env python3
"""Regression tests for owner extraction from raw and Markdown GitHub URLs."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import deep_extract as extractor


class OwnerParserTests(unittest.TestCase):
    def test_markdown_closers_punctuation_repo_paths_and_case_dedup(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a.md").write_text(
                "https://github.com/Panniantong\n"
                "[Panniantong](https://github.com/panniantong).\n"
                "https://github.com/diegosouzapw/OmniRoute\n"
                "https://github.com/zulip.\n",
                encoding="utf-8",
            )
            (root / "b.md").write_text(
                "[Microsoft](https://github.com/microsoft),\n"
                "https://github.com/salamou1944/private-repo\n"
                "https://github.com/settings/profile\n",
                encoding="utf-8",
            )
            original = extractor.ACCOUNTS
            try:
                extractor.ACCOUNTS = root
                found = extractor.owners()
            finally:
                extractor.ACCOUNTS = original
            self.assertEqual({name.lower() for name in found},
                             {"panniantong", "diegosouzapw", "zulip", "microsoft"})
            self.assertEqual(len(found), 4)


if __name__ == "__main__":
    unittest.main()
