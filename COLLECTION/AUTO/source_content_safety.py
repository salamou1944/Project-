#!/usr/bin/env python3
"""Shared source-content safety helpers for Collection packet ingestion."""
from __future__ import annotations

import hashlib
import re
from pathlib import PurePosixPath

SENSITIVE_DIRS = {
    ".aws", ".ssh", ".azure", ".gcloud", "credentials", "secrets",
    "private_keys", "private-keys", "certificates", "certs",
}
SENSITIVE_EXTENSIONS = {
    ".pem", ".key", ".p12", ".pfx", ".jks", ".keystore", ".ppk",
    ".der", ".tfstate", ".kubeconfig",
}
DATA_EXTENSIONS = {".json", ".json5", ".jsonc", ".yaml", ".yml", ".toml", ".env", ".txt", ".bin", ".enc", ".db", ".sqlite"}
SAFE_ENV_SUFFIXES = (".example", ".sample", ".template", ".dist", ".test", ".testing")

CONTENT_FIELDS = {
    "content", "text", "excerpt", "source_excerpt", "snippet", "code",
    "body", "raw_content", "sample", "description", "summary", "notes",
}

TOKEN_PATTERNS = [
    ("openai_key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b")),
    ("github_token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("slack_token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("google_api_key", re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("stripe_or_webhook_secret", re.compile(r"\b(?:sk_live_|rk_live_|whsec_)[A-Za-z0-9]{16,}\b")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    ("bearer_token", re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/-]{20,}={0,2}")),
    ("private_key_block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
]
SECRET_ASSIGNMENT = re.compile(
    r'''(?i)(["']?(?:api[_-]?key|access[_-]?token|refresh[_-]?token|client[_-]?secret|clientsecret|password|passwd|secret|token|private[_-]?key|authorization)["']?\s*[:=]\s*["']?)([^"'\s,;}}\]]{12,})(["']?)'''
)


def is_sensitive_path(path: str) -> bool:
    """Return True for paths likely to contain raw credentials or private key material."""
    p = str(path or "").replace("\\", "/").strip("/")
    if not p:
        return False
    parts = [part.lower() for part in PurePosixPath(p).parts]
    base = parts[-1] if parts else ""
    suffix = PurePosixPath(base).suffix.lower()

    if base.startswith(".env") and not any(base.endswith(s) for s in SAFE_ENV_SUFFIXES):
        return True
    if base in {
        ".npmrc", ".pypirc", ".netrc", "credentials", "secrets",
        "id_rsa", "id_ed25519", "id_ecdsa", "id_dsa",
        "authorized_keys", "kubeconfig", "terraform.tfstate",
        "terraform.tfstate.backup", "service-account.json",
        "google-application-credentials.json", "application_default_credentials.json",
    }:
        return True
    if suffix in SENSITIVE_EXTENSIONS:
        return True
    if any(part in SENSITIVE_DIRS for part in parts[:-1]):
        return True
    if ".docker" in parts[:-1] and base in {"config.json", "config"}:
        return True
    if any(part in {"terraform.tfstate.d", "private", "private_key"} for part in parts[:-1]) and suffix in DATA_EXTENSIONS:
        return True
    if any(term in base for term in ("credential", "secret", "private-key", "private_key")) and suffix in DATA_EXTENSIONS:
        return True
    if "service-account" in base and suffix in {".json", ".yaml", ".yml"}:
        return True
    return False


def redact_sensitive_content(text: str) -> tuple[str, list[str]]:
    """Redact high-confidence token literals and secret assignments without returning values."""
    if not isinstance(text, str) or not text:
        return text, []
    out = text
    reasons = []
    for reason, pattern in TOKEN_PATTERNS:
        new = pattern.sub("[REDACTED]", out)
        if new != out:
            reasons.append(reason)
            out = new
    new = SECRET_ASSIGNMENT.sub(lambda m: m.group(1) + "[REDACTED]" + m.group(3), out)
    if new != out:
        reasons.append("secret_assignment")
        out = new
    return out, sorted(set(reasons))


def sanitize_source_content(path: str, text: str) -> tuple[str, list[str]]:
    """Redact entire sensitive files or high-confidence secrets embedded in other source files."""
    if is_sensitive_path(path):
        return "[REDACTED: sensitive source path; original source hash/path/revision retained]", ["sensitive_path"]
    return redact_sensitive_content(text)


def sanitize_document(document, inherited_path: str = ""):
    """Recursively sanitize content-bearing fields in a JSON packet; return the number of redactions."""
    count = 0
    if isinstance(document, list):
        for item in document:
            count += sanitize_document(item, inherited_path)
        return count
    if not isinstance(document, dict):
        return count

    current_path = inherited_path
    for key in ("path", "source_path", "file_path", "filename", "source_filename"):
        value = document.get(key)
        if isinstance(value, str) and value:
            current_path = value
            break

    path_sensitive = is_sensitive_path(current_path)
    for key, value in list(document.items()):
        if key in CONTENT_FIELDS and isinstance(value, str) and value:
            if path_sensitive:
                redacted = "[REDACTED: sensitive source path; original source hash/path/revision retained]"
                reasons = ["sensitive_path"]
            else:
                redacted, reasons = redact_sensitive_content(value)
            if reasons and redacted != value:
                if "content_sha256" not in document and "source_content_sha256" not in document:
                    document["source_content_sha256"] = hashlib.sha256(value.encode("utf-8", "replace")).hexdigest()
                document[key] = redacted
                document["redaction_applied"] = True
                previous = document.get("redaction_reasons", [])
                if not isinstance(previous, list):
                    previous = [str(previous)]
                document["redaction_reasons"] = sorted(set(previous + reasons))
                count += 1
        elif isinstance(value, (dict, list)):
            count += sanitize_document(value, current_path)
    return count
