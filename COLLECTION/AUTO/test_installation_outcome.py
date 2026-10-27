#!/usr/bin/env python3
"""Regression tests for the final install-cycle evidence gate."""
import unittest

from validate_installation_outcome import validate_outcome
from verify_installed_assets import load_callable_evidence


def result(repo, revision, status):
    return {"repo": repo, "revision": revision, "status": status}


def ready(repo, revision):
    return {"repo": repo, "revision": revision, "verification_state": "READY_FOR_VERIFICATION"}


class InstallationOutcomeTests(unittest.TestCase):
    def test_passes_only_when_successes_match_verified_queue(self):
        report = {"results": [
            result("owner/one", "a" * 40, "INSTALLED"),
            result("owner/two", "b" * 40, "ALREADY_INSTALLED"),
            result("owner/large", "c" * 40, "BLOCKED_SIZE"),
        ]}
        queue = {"items": [ready("owner/one", "a" * 40), ready("owner/two", "b" * 40)]}
        outcome = validate_outcome(report, queue)
        self.assertEqual(outcome["status"], "PASS")
        self.assertEqual(outcome["installed_or_already_installed"], 2)
        self.assertEqual(outcome["blocked_by_size"], 1)

    def test_modelparams_callable_evidence_is_exact_revision_and_has_successful_runs(self):
        evidence = load_callable_evidence()
        self.assertEqual(evidence["repo"], "mnfst/modelparams.dev")
        self.assertEqual(evidence["revision"], "0d09d9a3fb642770430fb357e3c72f8e7d9f1f67")
        self.assertEqual(evidence["execution_status"], "PROVEN_CALLABLE")
        self.assertEqual(evidence["installed_package_smoke"]["status"], "success")
        self.assertEqual(evidence["api_factory_integration"]["status"], "success")

    def test_safe_noop_when_no_candidate_has_explicit_approval(self):
        outcome = validate_outcome({"candidate_count": 0, "results": []}, {"items": []})
        self.assertEqual(outcome["status"], "NO_APPROVED_CANDIDATES")
        self.assertEqual(outcome["installed_or_already_installed"], 0)

    def test_fails_if_nothing_was_installed(self):
        with self.assertRaisesRegex(ValueError, "no asset was installed"):
            validate_outcome({"results": [result("owner/large", "a" * 40, "BLOCKED_SIZE")]}, {"items": []})

    def test_fails_if_installation_failed_even_when_another_item_succeeded(self):
        report = {"results": [
            result("owner/one", "a" * 40, "ALREADY_INSTALLED"),
            result("owner/broken", "b" * 40, "FAILED"),
        ]}
        queue = {"items": [ready("owner/one", "a" * 40)]}
        with self.assertRaisesRegex(ValueError, "installation failures remain"):
            validate_outcome(report, queue)

    def test_fails_if_verification_queue_is_missing_or_incomplete(self):
        report = {"results": [result("owner/one", "a" * 40, "INSTALLED")]}
        with self.assertRaisesRegex(ValueError, "verification queue mismatch"):
            validate_outcome(report, {"items": []})
        with self.assertRaisesRegex(ValueError, "integrity failures"):
            validate_outcome(report, {"items": [
                {"repo": "owner/one", "revision": "a" * 40, "verification_state": "INSTALLATION_INTEGRITY_FAILED"}
            ]})


if __name__ == "__main__":
    unittest.main()
