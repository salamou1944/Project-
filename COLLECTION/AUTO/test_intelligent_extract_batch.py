import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import intelligent_extract as extractor


class IntelligentExtractBatchTests(unittest.TestCase):
    def test_discover_accounts_scans_full_markdown_and_deduplicates_case_insensitively(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            accounts = root / "COLLECTION" / "ACCOUNTS"
            accounts.mkdir(parents=True)
            body = ["# Frontier"] + ["metadata-only line"] * 100 + [
                "- https://github.com/LateOwner",
                "- [Owner](https://github.com/Owner)",
                "- https://github.com/owner.",
                "- https://github.com/org/repository",
            ]
            (accounts / "frontier.md").write_text("\n".join(body), encoding="utf-8")
            (root / "COLLECTION" / "INDEX.md").write_text(
                "[IndexOwner](https://github.com/IndexOwner)\n"
                "[repository link](https://github.com/IndexOwner/repository)\n",
                encoding="utf-8",
            )

            owners = extractor.discover_accounts(root)

        self.assertIn("lateowner", owners)
        self.assertIn("owner", owners)
        self.assertIn("indexowner", owners)
        self.assertIn("salamou1944", owners)
        self.assertNotIn("org", owners)
        self.assertEqual(len(owners), len(set(owners)))

    def test_load_deep_inventory_reuses_shared_frontier_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inventory_path = root / "REPO-INVENTORY.json"
            manifest_path = root / "MANIFEST.json"
            inventory_path.write_text(json.dumps({
                "schema_version": "collection-repo-inventory/v1",
                "rows": [{
                    "repo": "owner/project", "owner": "owner", "name": "project",
                    "html_url": "https://github.com/owner/project", "description": "API agent",
                    "topics": ["api", "agent"], "language": "Python", "license_spdx_id": "MIT",
                    "stargazers_count": 10, "forks_count": 2, "size_kb": 50,
                    "updated_at": "2026-10-18T00:00:00Z", "pushed_at": "2026-10-18T00:00:00Z",
                    "default_branch": "main", "archived": False, "fork": False, "priority_score": 20,
                }],
            }), encoding="utf-8")
            manifest_path.write_text(json.dumps({
                "schema_version": "collection-deep-extraction/v1",
                "owners": ["owner"], "owner_discovery_errors": {}, "refresh_failures": [],
            }), encoding="utf-8")

            repos, gists, blocked, owners = extractor.load_deep_inventory(inventory_path, manifest_path)

        self.assertEqual(len(repos), 1)
        self.assertEqual(repos[0]["full_name"], "owner/project")
        self.assertEqual(repos[0]["repo_meta"]["license"]["spdx_id"], "MIT")
        self.assertEqual(gists, [])
        self.assertEqual(blocked, [])
        self.assertEqual(owners, ["owner"])
        self.assertEqual(extractor.FRONTIER_META["inventory_repo_count"], 1)
        self.assertTrue(extractor.FRONTIER_META["sha256"])

    def test_force_refresh_rotates_from_oldest_cached_packet(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "COLLECTION" / "AUTO" / "EXTRACTED"
            root.mkdir(parents=True)
            pushed = "2026-10-18T00:00:00Z"

            def item(repo, owner, priority):
                return {
                    "kind": "repo", "full_name": repo, "owner": owner,
                    "repo_meta": {
                        "full_name": repo, "owner": {"login": owner},
                        "pushed_at": pushed, "updated_at": pushed, "default_branch": "main",
                        "archived": False, "fork": False, "stargazers_count": priority,
                        "priority_score": priority, "license": {"spdx_id": "MIT"},
                    },
                }

            repos = [item("ownerA/one", "ownerA", 100), item("ownerB/two", "ownerB", 90)]
            old_path = root / f"{extractor.safe_name('ownerA/one')}.json"
            new_path = root / f"{extractor.safe_name('ownerB/two')}.json"
            def packet(repo, generated_at):
                return {
                    "canonical_source": f"github:{repo}", "state": "extracted",
                    "pushed_at": pushed, "generated_at": generated_at,
                    "revision_sha": "a" * 40, "files": [{"content": "cached source"}],
                }
            old_path.write_text(json.dumps(packet("ownerA/one", "2026-01-01T00:00:00Z")), encoding="utf-8")
            new_path.write_text(json.dumps(packet("ownerB/two", "2026-10-01T00:00:00Z")), encoding="utf-8")

            with mock.patch.object(extractor, "ROOT", root), \
                 mock.patch.object(extractor, "MAX_REPOS_PER_RUN", 1), \
                 mock.patch.object(extractor, "MAX_REPOS_PER_OWNER", 1), \
                 mock.patch.dict("os.environ", {"COLLECTION_FORCE_REFRESH": "1"}):
                selected_first, _, _ = extractor.select_repo_batch(repos, set())
                self.assertEqual(selected_first[0]["full_name"], "ownerA/one")
                old_doc = json.loads(old_path.read_text(encoding="utf-8"))
                old_doc["generated_at"] = "2026-10-19T01:00:00Z"
                old_path.write_text(json.dumps(old_doc), encoding="utf-8")
                selected_second, _, _ = extractor.select_repo_batch(repos, set())

        self.assertEqual(selected_second[0]["full_name"], "ownerB/two")

    def test_batch_is_bounded_owner_diverse_and_skips_cached_deep_and_archived_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "COLLECTION" / "AUTO" / "EXTRACTED"
            root.mkdir(parents=True)
            pushed = "2026-10-18T00:00:00Z"

            def item(repo, owner, priority, archived=False, pushed_at=pushed):
                return {
                    "kind": "repo", "full_name": repo, "owner": owner,
                    "repo_meta": {
                        "full_name": repo, "owner": {"login": owner}, "html_url": f"https://github.com/{repo}",
                        "pushed_at": pushed_at, "updated_at": pushed_at, "default_branch": "main",
                        "archived": archived, "fork": False, "stargazers_count": priority,
                        "priority_score": priority, "license": {"spdx_id": "MIT"},
                    },
                }

            cached_repo = "ownerE/cached"
            cached_path = root / f"{extractor.safe_name(cached_repo)}.json"
            cached_path.write_text(json.dumps({
                "canonical_source": f"github:{cached_repo}", "state": "extracted",
                "pushed_at": pushed, "revision_sha": "a" * 40, "files": [{"content": "cached source"}],
            }), encoding="utf-8")

            stale_repo = "ownerB/stale"
            stale_path = root / f"{extractor.safe_name(stale_repo)}.json"
            stale_path.write_text(json.dumps({
                "canonical_source": f"github:{stale_repo}", "state": "extracted",
                "pushed_at": "2026-09-01T00:00:00Z", "revision_sha": "b" * 40,
                "files": [{"content": "old source"}],
            }), encoding="utf-8")

            repos = [
                item("ownerA/new-best", "ownerA", 100),
                item("ownerA/new-second", "ownerA", 90),
                item(stale_repo, "ownerB", 80),
                item("ownerC/deep-only", "ownerC", 70),
                item("ownerD/archived", "ownerD", 120, archived=True),
                item(cached_repo, "ownerE", 110),
                item("ownerF/new", "ownerF", 60),
                item("ownerG/new-low-priority", "ownerG", 10),
            ]
            with mock.patch.object(extractor, "ROOT", root), \
                 mock.patch.object(extractor, "MAX_REPOS_PER_RUN", 3), \
                 mock.patch.object(extractor, "MAX_REPOS_PER_OWNER", 1), \
                 mock.patch.dict("os.environ", {"COLLECTION_FORCE_REFRESH": "0"}):
                selected, states, _ = extractor.select_repo_batch(repos, {"ownerC/deep-only"})

        selected_names = [row["full_name"] for row in selected]
        self.assertEqual(set(selected_names), {"ownerA/new-best", "ownerF/new", "ownerG/new-low-priority"})
        self.assertNotIn(stale_repo, selected_names)
        self.assertEqual(states[stale_repo], "NEEDS_REFRESH")
        self.assertEqual(len(selected_names), 3)
        self.assertEqual(len({row["owner"].lower() for row in selected}), 3)
        self.assertEqual(states["ownerC/deep-only"], "DEEP_PACKET_ONLY")
        self.assertEqual(states["ownerD/archived"], "ARCHIVED_METADATA_ONLY")
        self.assertEqual(states[cached_repo], "CACHED_CURRENT")
        self.assertEqual(states[stale_repo], "NEEDS_REFRESH")


if __name__ == "__main__":
    unittest.main()
