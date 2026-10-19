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


    def test_deep_batch_is_bounded_diverse_and_skips_archived(self):
        import datetime
        original_total = extractor.MAX_DEEP_REPOS
        original_per_owner = extractor.MAX_DEEP_REPOS_PER_OWNER
        try:
            extractor.MAX_DEEP_REPOS = 3
            extractor.MAX_DEEP_REPOS_PER_OWNER = 1
            now = datetime.datetime(2026, 10, 19, tzinfo=datetime.timezone.utc)
            base = {
                "description": "MCP agent provider API",
                "topics": ["agent", "api"],
                "language": "Python",
                "license": {"spdx_id": "MIT"},
                "stargazers_count": 100,
                "fork": False,
                "pushed_at": "2026-10-18T00:00:00Z",
                "updated_at": "2026-10-18T00:00:00Z",
            }
            repos = {
                "alpha/agent-router": {**base, "full_name": "alpha/agent-router", "name": "agent-router", "owner": {"login": "alpha"}},
                "alpha/old-docs": {**base, "full_name": "alpha/old-docs", "name": "old-docs", "owner": {"login": "alpha"}, "description": "old docs"},
                "beta/provider-api": {**base, "full_name": "beta/provider-api", "name": "provider-api", "owner": {"login": "beta"}},
                "gamma/llm-gateway": {**base, "full_name": "gamma/llm-gateway", "name": "llm-gateway", "owner": {"login": "gamma"}},
                "delta/archived-agent": {**base, "full_name": "delta/archived-agent", "name": "archived-agent", "owner": {"login": "delta"}, "archived": True},
            }
            selected, _ = extractor.select_deep_batch(repos, {}, now)
            self.assertEqual(len(selected), 3)
            self.assertEqual(len({repo.split("/", 1)[0] for repo in selected}), 3)
            self.assertNotIn("delta/archived-agent", selected)
            existing = {"alpha/agent-router": {"revision_sha": "abc", "source_pushed_at": "2026-10-18T00:00:00Z"}}
            selected_after_packet, _ = extractor.select_deep_batch(repos, existing, now)
            self.assertNotIn("alpha/agent-router", selected_after_packet)
        finally:
            extractor.MAX_DEEP_REPOS = original_total
            extractor.MAX_DEEP_REPOS_PER_OWNER = original_per_owner


if __name__ == "__main__":
    unittest.main()
