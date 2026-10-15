#!/usr/bin/env python3
"""Regression tests for GitHub HTTP classification and retry behavior."""
import importlib.util
import io
import json
import pathlib
import urllib.error
import urllib.request
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("deep_extract_under_test", ROOT / "COLLECTION/AUTO/deep_extract.py")
deep = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(deep)


def http_error(code, message, headers=None):
    payload = json.dumps({"message": message}).encode()
    return urllib.error.HTTPError(
        "https://api.github.com/test", code, "error", headers or {}, io.BytesIO(payload)
    )


def response(payload):
    return io.BytesIO(json.dumps(payload).encode())


def run():
    deep.CACHE.clear()
    permission = http_error(403, "Resource not accessible by integration", {"X-GitHub-Request-Id": "req-permission"})
    with mock.patch.object(urllib.request, "urlopen", side_effect=permission) as open_mock, \
         mock.patch.object(deep.time, "sleep") as sleep_mock:
        try:
            deep.api("/permission-test")
            raise AssertionError("permission 403 should fail")
        except RuntimeError as exc:
            assert "github_api_http_403" in str(exc), str(exc)
            assert "Resource not accessible" in str(exc), str(exc)
            assert "req-permission" in str(exc), str(exc)
        assert open_mock.call_count == 1, open_mock.call_count
        sleep_mock.assert_not_called()

    deep.CACHE.clear()
    rate_limit = http_error(403, "API rate limit exceeded", {
        "X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "0"
    })
    with mock.patch.object(urllib.request, "urlopen", side_effect=[rate_limit, response({"ok": True})]) as open_mock, \
         mock.patch.object(deep.time, "sleep") as sleep_mock:
        assert deep.api("/rate-limit-test") == {"ok": True}
        assert open_mock.call_count == 2, open_mock.call_count
        sleep_mock.assert_called_once()

    deep.CACHE.clear()
    rate_429 = http_error(429, "Too Many Requests", {"Retry-After": "120"})
    with mock.patch.object(urllib.request, "urlopen", side_effect=[rate_429, response({"ok": "retry"})]) as open_mock, \
         mock.patch.object(deep.time, "sleep") as sleep_mock:
        assert deep.api("/429-test") == {"ok": "retry"}
        assert open_mock.call_count == 2, open_mock.call_count
        sleep_mock.assert_called_once_with(120.0)

    deep.CACHE.clear()
    missing = http_error(404, "Not Found")
    with mock.patch.object(urllib.request, "urlopen", side_effect=missing) as open_mock, \
         mock.patch.object(deep.time, "sleep") as sleep_mock:
        try:
            deep.api("/not-found-test")
            raise AssertionError("404 should fail")
        except RuntimeError as exc:
            assert "github_api_http_404" in str(exc), str(exc)
        assert open_mock.call_count == 1, open_mock.call_count
        sleep_mock.assert_not_called()

    deep.CACHE.clear()
    network_error = urllib.error.URLError("temporary network interruption")
    with mock.patch.object(urllib.request, "urlopen", side_effect=[network_error, response({"ok": "network-recovered"})]) as open_mock, \
         mock.patch.object(deep.time, "sleep") as sleep_mock:
        assert deep.api("/network-test") == {"ok": "network-recovered"}
        assert open_mock.call_count == 2, open_mock.call_count
        sleep_mock.assert_called_once()

    print(json.dumps({"status": "PASS", "cases": [
        "403 permission no retry", "403 rate limit retries", "429 retries",
        "404 no retry", "transient network retry"
    ]}))


if __name__ == "__main__":
    run()
