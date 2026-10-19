#!/usr/bin/env python3
"""Regression tests for evidence-prioritized, license-gated Collection installs."""
import unittest

from install_assets import ALLOWED, load_quarantined_revisions, select_collected_candidates


def source(repo, *, state="extracted", license_name="MIT", files=1, revision=None, mode="refreshed"):
    record = {
        "canonical_source": f"github:{repo}",
        "state": state,
        "license": license_name,
        "files_extracted": files,
        "revision_sha": revision or ("a" * 40),
    }
    if mode is not None:
        record["mode"] = mode
    return record


def queue_item(key, sources, action="API_FACTORY_REVIEW", promotion_action="INSTALL_APPROVED",
               install_approval="APPROVED", integration_gate="PASS", security_gate="PASS"):
    return {
        "capability_key": key,
        "operator_action": action,
        "promotion_action": promotion_action,
        "install_approval": install_approval,
        "integration_gate": integration_gate,
        "security_gate": security_gate,
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

    def test_review_only_or_shelf_items_are_never_installed(self):
        manifest = {"sources": [source("owner/shelf-browser")]}
        queue = {"items": [
            queue_item("shelf", ["github:owner/shelf-browser"], promotion_action="REVIEW_NEW_OR_UPGRADE"),
        ]}
        self.assertEqual(select_collected_candidates(manifest, queue), [])

    def test_promotion_action_alone_does_not_authorize_install(self):
        manifest = {"sources": [source("owner/unapproved")]}
        queue = {"items": [
            queue_item("unapproved", ["github:owner/unapproved"],
                       promotion_action="INSTALL_APPROVED", install_approval="NOT_APPROVED"),
        ]}
        self.assertEqual(select_collected_candidates(manifest, queue), [])

    def test_install_approval_requires_both_integration_and_security_gates(self):
        manifest = {"sources": [
            source("owner/no-integration-gate"),
            source("owner/no-security-gate"),
        ]}
        queue = {"items": [
            queue_item("no-integration", ["github:owner/no-integration-gate"],
                       integration_gate="UNVERIFIED", security_gate="PASS"),
            queue_item("no-security", ["github:owner/no-security-gate"],
                       integration_gate="PASS", security_gate="UNVERIFIED"),
        ]}
        self.assertEqual(select_collected_candidates(manifest, queue), [])

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

    def test_preserved_after_refresh_failure_is_never_installed(self):
        manifest = {"sources": [
            source("owner/stale", mode="preserved_after_refresh_failure"),
            source("owner/fresh", mode="refreshed"),
        ]}
        queue = {"items": [
            queue_item("capability", ["github:owner/stale", "github:owner/fresh"]),
        ]}
        selected = select_collected_candidates(manifest, queue)
        self.assertEqual([item["repo"] for item in selected], ["owner/fresh"])

    def test_known_compromised_revision_is_quarantined(self):
        quarantine = load_quarantined_revisions()
        bad_revision = "62705cdb645d36b5050d0f28b9b5b0ca175bc80f"
        manifest = {"sources": [
            source("mnfst/docs", license_name="MIT", revision=bad_revision, mode="cached"),
            source("owner/fresh", license_name="MIT", mode="refreshed"),
        ]}
        queue = {"items": [
            queue_item("security-sensitive", ["github:mnfst/docs", "github:owner/fresh"]),
        ]}
        selected = select_collected_candidates(manifest, queue, quarantined_revisions=quarantine)
        self.assertEqual([item["repo"] for item in selected], ["owner/fresh"])
        self.assertEqual(len(quarantine), 5)

    def test_missing_refresh_mode_fails_closed(self):
        manifest = {"sources": [source("owner/unknown-mode", mode=None)]}
        queue = {"items": [queue_item("capability", ["github:owner/unknown-mode"])]}
        self.assertEqual(select_collected_candidates(manifest, queue), [])

    def test_invalid_candidate_limit_and_schema_fail_closed(self):
        with self.assertRaises(ValueError):
            select_collected_candidates({"sources": []}, {"items": []}, max_candidates=21)
        with self.assertRaises(ValueError):
            select_collected_candidates({"sources": {}}, {"items": []})
        with self.assertRaises(ValueError):
            select_collected_candidates({"sources": []}, {"items": {}})


if __name__ == "__main__":
    unittest.main()
