#!/usr/bin/env python3
"""Regression tests for evidence-prioritized, license-gated Collection installs."""
import unittest

from install_assets import ALLOWED, select_collected_candidates


def source(repo, *, state="extracted", license_name="MIT", files=1, revision=None):
    return {
        "canonical_source": f"github:{repo}",
        "state": state,
        "license": license_name,
        "files_extracted": files,
        "revision_sha": revision or ("a" * 40),
    }


def queue_item(key, sources, action="API_FACTORY_REVIEW"):
    return {
        "capability_key": key,
        "operator_action": action,
        "promotion_action": "REVIEW_NEW_OR_UPGRADE",
        "sources": sources,
        "priority": [100, 10, len(sources)],
    }


class InstallSelectionTests(unittest.TestCase):
    def test_selects_only_licensed_extracted_sources_in_priority_order(self):
        manifest = {"sources": [
            source("owner/first", license_name="MIT"),
            source("owner/second", license_name="Apache-2.0"),
            source("owner/no-license", license_name="NOASSERTION"),
            source("owner/blocked", state="BLOCKED_EXTERNAL_ACCESS"),
            source("owner/empty", files=0),
            source("owner/short-sha", revision="abc1234"),
        ]}
        queue = {"items": [
            queue_item("capability-high", [
                "github:owner/first", "github:owner/no-license",
                "github:owner/blocked", "github:owner/empty",
                "github:owner/short-sha",
            ]),
            queue_item("capability-next", ["github:owner/second"]),
        ]}

        selected = select_collected_candidates(manifest, queue, max_candidates=5)

        self.assertEqual([item["repo"] for item in selected], ["owner/first", "owner/second"])
        self.assertTrue(all(item["license"] in ALLOWED for item in selected))
        self.assertTrue(all(len(item["revision"]) == 40 for item in selected))
        self.assertEqual(selected[0]["selected_capabilities"], ["capability-high"])

    def test_quarantined_capabilities_are_never_installed(self):
        manifest = {"sources": [source("owner/restricted")]}
        queue = {"items": [
            queue_item("restricted", ["github:owner/restricted"], action="SECURITY_REVIEW")
            | {"promotion_action": "QUARANTINE"}
        ]}
        self.assertEqual(select_collected_candidates(manifest, queue), [])

    def test_candidate_limit_and_deduplication(self):
        manifest = {"sources": [
            source("owner/one"),
            source("owner/two", license_name="ISC"),
            source("owner/three", license_name="BSD-3-Clause"),
        ]}
        queue = {"items": [
            queue_item("capability-a", ["github:owner/one", "github:owner/two"]),
            queue_item("capability-b", ["github:owner/one", "github:owner/three"]),
        ]}
        selected = select_collected_candidates(manifest, queue, max_candidates=2)
        self.assertEqual([item["repo"] for item in selected], ["owner/one", "owner/two"])
        self.assertEqual(select_collected_candidates(manifest, queue, max_candidates=0), [])

    def test_invalid_candidate_limit_and_schema_fail_closed(self):
        with self.assertRaises(ValueError):
            select_collected_candidates({"sources": []}, {"items": []}, max_candidates=21)
        with self.assertRaises(ValueError):
            select_collected_candidates({"sources": {}}, {"items": []})
        with self.assertRaises(ValueError):
            select_collected_candidates({"sources": []}, {"items": {}})


if __name__ == "__main__":
    unittest.main()
