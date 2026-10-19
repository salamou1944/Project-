import unittest

from collection_state_guard import validate_manifest_source_count


class CollectionStateGuardTests(unittest.TestCase):
    def test_legacy_manifest_accounting_remains_supported(self):
        manifest = {
            "repo_count": 2, "gist_count": 1,
            "preserved_sources_after_refresh_failure": 1,
            "sources": [{}, {}, {}, {}],
        }
        self.assertEqual(validate_manifest_source_count(manifest), 4)

    def test_bounded_manifest_accounts_for_processed_and_preserved_rows(self):
        manifest = {
            "repo_count": 10000, "gist_count": 0,
            "processed_repo_count": 2, "processed_gist_count": 0,
            "preserved_sources_after_refresh_failure": 1,
            "preserved_prior_sources_not_selected": 3,
            "sources": [{}, {}, {}, {}, {}, {}],
        }
        self.assertEqual(validate_manifest_source_count(manifest), 6)

    def test_bounded_manifest_mismatch_fails_closed(self):
        manifest = {
            "repo_count": 10000, "gist_count": 0,
            "processed_repo_count": 2, "processed_gist_count": 0,
            "preserved_sources_after_refresh_failure": 1,
            "preserved_prior_sources_not_selected": 3,
            "sources": [{}, {}, {}],
        }
        with self.assertRaises(SystemExit):
            validate_manifest_source_count(manifest)


if __name__ == "__main__":
    unittest.main()
