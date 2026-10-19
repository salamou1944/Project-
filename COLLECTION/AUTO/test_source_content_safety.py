#!/usr/bin/env python3
import hashlib
import unittest

from source_content_safety import (
    is_sensitive_path,
    redact_sensitive_content,
    sanitize_document,
    sanitize_source_content,
)


class SourceContentSafetyTests(unittest.TestCase):
    def test_sensitive_credential_paths_are_redacted(self):
        for path in (
            "n8n/demo-data/credentials/sample.json",
            ".env",
            "service-account.json",
            ".aws/credentials",
            "keys/server.pem",
            "terraform.tfstate",
        ):
            with self.subTest(path=path):
                self.assertTrue(is_sensitive_path(path))
                redacted, reasons = sanitize_source_content(path, "demo-secret-material-123456")
                self.assertIn("REDACTED", redacted)
                self.assertIn("sensitive_path", reasons)

    def test_safe_examples_are_not_blocked_by_path_alone(self):
        self.assertFalse(is_sensitive_path(".env.example"))
        self.assertFalse(is_sensitive_path("docs/secrets.md"))
        self.assertFalse(is_sensitive_path("tests/test_secret_redaction.py"))

    def test_known_token_patterns_are_redacted_without_echoing_values(self):
        source = "OPENAI_API_KEY=sk-proj-" + "A" * 28 + "\nAuthorization: Bearer " + "b" * 32
        redacted, reasons = redact_sensitive_content(source)
        self.assertNotIn("sk-proj-", redacted)
        self.assertNotIn("b" * 24, redacted)
        self.assertIn("openai_key", reasons)
        self.assertIn("bearer_token", reasons)

    def test_secret_assignment_values_are_redacted(self):
        redacted, reasons = redact_sensitive_content('{"client_secret":"abcdef1234567890"}')
        self.assertNotIn("abcdef1234567890", redacted)
        self.assertIn("secret_assignment", reasons)

    def test_recursive_packet_sanitizer_preserves_raw_hash_and_path(self):
        raw = "AQICAHh0aGlzLWlzLWRlbW8tY3lwaGVydGV4dA=="
        document = {
            "repo": "example/project",
            "files": [{
                "path": "demo/credentials/account.json",
                "content_sha256": hashlib.sha256(raw.encode()).hexdigest(),
                "content": raw,
            }],
        }
        count = sanitize_document(document)
        file_record = document["files"][0]
        self.assertEqual(count, 1)
        self.assertEqual(file_record["content_sha256"], hashlib.sha256(raw.encode()).hexdigest())
        self.assertEqual(file_record["path"], "demo/credentials/account.json")
        self.assertNotIn(raw, file_record["content"])
        self.assertTrue(file_record["redaction_applied"])
        self.assertIn("sensitive_path", file_record["redaction_reasons"])


if __name__ == "__main__":
    unittest.main()
