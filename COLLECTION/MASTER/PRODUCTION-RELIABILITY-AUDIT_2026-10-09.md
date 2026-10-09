# Collection Production-Reliability Audit — 2026-10-09

## Scope and standard

This audit covers the repository-visible Collection pipeline and its GitHub Actions orchestration. “100% production” is not a technically honest guarantee: external APIs, rate limits, upstream changes, CI availability, and runtime dependencies can fail. The actionable target is **fail-closed behavior, zero silent corruption, bounded retries, observable failures, and evidence-backed readiness**.

## Confirmed defects and corrective actions

### 1. Raw extraction errors were represented as file records
**Evidence:** `COLLECTION/AUTO/intelligent_extract.py` appended every `raw_fetch` result to `files`, including entries carrying an `error` and no content. The manifest then counted `len(data["files"])` as extracted files. This could make a repository look extracted when every raw fetch failed.

**Correction committed:** `b7d58d461ee7bf5f1bbb119375c911f894c9412e`
- Failed/empty fetches are now separated into `fetch_errors`.
- Only non-empty successful fetches are retained as extracted files.
- A repository with zero usable files raises an explicit extraction error and becomes blocked in the manifest rather than falsely extracted.

**Still required:** run the real workflow and verify its manifest reports successful files and blocked sources truthfully.

### 2. Installer silently ignored a malformed deep-extraction manifest
**Evidence:** `COLLECTION/AUTO/install_assets.py` caught all exceptions parsing `COLLECTION/AUTO/DEEP-EXTRACTED/MANIFEST.json` and continued using other records. That made an incomplete install selection possible without surfacing the corrupted manifest.

**Correction committed:** `a57015cfab198fa8856bc0052eb0bd2b41535a14`
- Invalid/unreadable manifest now fails closed.
- The `repos` field must be a list.

### 3. Parallel installer jobs could target the same directory for different revisions
**Evidence:** install identity was deduplicated by `(repo, revision)`, while the destination directory was keyed only by repository. Two revisions of one repository could therefore race while replacing the same destination.

**Correction committed:** `a57015cfab198fa8856bc0052eb0bd2b41535a14`
- Multiple pinned revisions for the same repository are now blocked as `BLOCKED_REVISION_CONFLICT`.
- A human/explicit policy choice is required before selecting one revision.

### 4. Value-operator output was not atomically published
**Evidence:** `COLLECTION/AUTO/collection_value_operator.py` wrote its generated JSON directly to the final path, so interruption could leave a truncated file.

**Correction committed:** `00641a21ea3bee928426912590ae20a150e503eb`
- It now writes and flushes a temporary file, then replaces the final output atomically.

### 5. Recovery trigger had been removed from the continuous workflow
**Evidence:** the recovery marker was in `COLLECTION/ACCOUNTS/`, but the push-path filter omitted that directory.

**Correction committed:** `387becd7ba468a635c4ebfee91c22cef62137186`
- Restored `COLLECTION/ACCOUNTS/**` to the trigger list.
- Generated outputs remain excluded from push triggers to avoid output-recursion loops.

## Known structural risks that remain open

1. **No verified end-to-end run after these changes yet.** Code changes are not proof of execution. Require a real Actions run and inspect job logs/artifacts plus resulting committed manifest/queues.
2. **Extraction coverage is bounded by policy** (`COLLECTION_MAX_FILES`, per-file and per-source byte limits). This is a prioritized sample, not a complete mirror of every repository.
3. **GitHub API throttling/access failures remain external dependencies.** The pipeline must retain explicit blocked-source diagnostics; a successful overall job must not be interpreted as every account/repository being extracted.
4. **The classifier is keyword-based.** It can misclassify benign documentation containing words such as “secret”, “token”, “exploit”, or “bypass”. Quarantine is conservative, but false positives need review and a test corpus.
5. **Readiness declarations validate evidence shape, not runtime behavior.** `validate_readiness.py` explicitly does not execute activation commands. Runtime states must remain gated by actual environment-specific smoke evidence.
6. **Installation is not runtime integration.** A vendored source directory and marker do not establish buildability, callable entrypoints, security suitability, or production behavior.
7. **Installer replacement safety — corrective change committed, runtime proof pending.** Commit `1914fee4ce5ed8d55cc8dc0d9d00001b9a16d79c` prepares a staged tree beside the destination, preserves the previous tree as a backup during the two-step rename, restores it if activation fails, refuses to overwrite a stale backup, and publishes the installation report atomically. Directory replacement is rollback-protected but is not a single atomic directory operation. The continuous workflow now includes `install_assets.py` in its Python compile gate. This reduces interruption risk but still needs a real CI run and fault-injection tests before calling the installer production-proven.
8. **Workflow concurrency protects the configured writer group only.** All workflows that write the same generated files must continue to share a compatible concurrency policy; direct manual edits to generated files during runs can still conflict.
9. **The value operator produces a review plan, not autonomous verified integration.** Its `execution_state` remains `NOT_EXECUTED`; a separate evidence-backed adapter/test gate is required before promoting a candidate.
10. **No zero-failure guarantee is possible for production systems.** The realistic goal is no silent failure, deterministic rollback/recovery, measured service-level objectives, and explicit evidence for each promoted capability.

## Acceptance gates before declaring Collection recovered

- [ ] A real `collection-continuous` run completes on current `main` after the installer-swap fix and compile-gate update.
- [ ] `MANIFEST.json` has non-empty sources and distinguishes extracted, cached, refreshed, and blocked outcomes accurately.
- [ ] Each source declared extracted has a non-empty artifact, matching canonical source and exact revision.
- [ ] `READY.json`, `PROMOTION-QUEUE.json`, `READINESS-QUEUE.json`, `RESTRICTED-QUEUE.json`, and `VALUE-OPERATOR-QUEUE.json` parse as JSON and agree on counts.
- [ ] Policy, readiness, callable-registry, and installation-integrity validators pass.
- [ ] Every `PROVEN_CALLABLE` entry has a concrete invocation and traceable successful execution evidence.
- [ ] A failed/blocked source remains visible in diagnostics and cannot silently become usable.
- [ ] A real install candidate is built/tested in an isolated job before any runtime readiness claim.
- [ ] A subsequent scheduled cycle runs without generated-output recursion or concurrent-writer conflicts.

## Evidence discipline

The commits above prove that code was changed, not that the GitHub Actions pipeline has passed after those changes. Until the acceptance gates are satisfied, the honest status is **corrective changes committed; end-to-end recovery pending runtime evidence**.
