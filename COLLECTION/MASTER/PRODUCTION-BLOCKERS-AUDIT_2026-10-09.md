# Collection Production Blockers Audit — 2026-10-09

## Scope and standard

This audit separates observed failures from risks and from unverified claims. “0% known blockers / 100% production” is a target, not a guarantee: a system can only be called production-proven for the exact workload and environment covered by reproducible evidence.

## Confirmed blockers

### P0 — Generated state is empty on main
Observed on 2026-10-09: `READY.json`, `PROMOTION-QUEUE.json`, `READINESS-QUEUE.json`, and `RESTRICTED-QUEUE.json` are present as zero-byte blobs. This is an operational failure even though the extractor manifest contains 1,910 extracted sources and 1,948 enumerated repositories. The pipeline must regenerate these artifacts and persist them only after validation.

### P0 — Cross-workflow write race
The 2026-10-09 digest records Collection run 37827674519 passing extraction/processing/policy checks but failing at `git push` with non-fast-forward because another writer updated main. Separate writer workflows using different concurrency groups can still race. The installation writer was moved to the shared `collection-writer` group in commit `913ab024cd1929dd0885003d77979fe72d65405f`. All workflows that commit to this repository must use the same writer group or a single write coordinator.

### P0 — Stale extracted artifacts could be reprocessed
Before commit `008013f58f2c4788781818c7ecb106dfeefcbf1f`, `process_collection.py` scanned every JSON file in the extraction directory, even if the current manifest marked that source blocked or no longer indexed it. Old artifacts are retained intentionally, but should not silently re-enter current evidence. The processor now selects only manifest-declared extracted artifacts and validates path containment, non-empty JSON, source identity, and revision before processing. Runtime confirmation is still required.

### P1 — Installation verification dropped already-installed assets
Before commit `f30934bb92a2cb0310f54c5cba093297254d262a`, `verify_installed_assets.py` accepted only status `INSTALLED`, while the installer emits `ALREADY_INSTALLED` on a repeat run. This could make valid previously installed assets disappear from the verification queue. The verifier now accepts both statuses while still checking the install marker and pinned revision.

### P1 — Inventory/manifest mismatch
The committed digest reports 1,948 repositories in the current manifest but 2,943 extracted JSON artifacts scanned by the old processor. The manifest does not fully index retained on-disk artifacts. The new processor avoids treating unindexed files as current evidence; a separate reconciliation should inventory legacy artifacts into an explicit archive/manifest without silently promoting them.

### P1 — Incomplete account and gist coverage
The digest reports 8 owner-enumeration failures, 21 gist-enumeration failures, 38 source-level blocked records (67 blocked attempts overall), 3 truncated Git trees, and 18 sources with zero selected files. Therefore the sweep is not exhaustive. Preserve blocked items as retryable records, classify error types, retry transient failures with rate-limit-aware backoff, and make completeness metrics a visible gate.

### P1 — Large generated state file
The prior digest measured `COLLECTION/MASTER/READY.json` at 50.95 MB. That increases clone, diff, review, and commit cost. Keep a compact summary/index and shard detailed decisions by stable key; retain deterministic generation and validate shard counts/hashes before publishing.

### P1 — Extractor cache is not content-integrity proof
Incremental caching currently reuses an artifact when `pushed_at` and `state=extracted` match. It does not prove the file contents still match a stored artifact hash, nor that the manifest row matches the actual artifact beyond the checks added to the processor. Add artifact SHA-256/size fields to the manifest and validate them before downstream use.

### P1 — API and raw-fetch failure handling
The extractor records blocked calls but still permits a partially complete manifest. GitHub API rate limits, forbidden access, transient 5xx/timeouts, deleted repositories, and empty/unsupported repositories must be distinct outcomes. Do not report “complete sweep” when any frontier owner is blocked. Retry transient classes with reset-aware backoff; do not repeatedly retry permanent 401/403/404 errors.

### P1 — Installation is not the same as usable runtime
Installation verification checks directory/marker integrity, not that a candidate can build, start, serve a health check, or pass a capability-specific smoke. Keep candidates `READY_FOR_VERIFICATION` until the exact selected entrypoint runs successfully. Hyperswitch proof is limited to deterministic local tests; it does not prove live payment-network or production settlement behavior.

### P1 — Independent workflows can validate inconsistent snapshots
Canonical reconciliation, continuous extraction, installation, deep extraction, and smoke workflows can read different commits. Only workflows that write must share the writer serialization policy; read-only validators should validate a pinned commit or run inside the owning writer workflow. No validator should publish a status for a different source revision than the one it checked.

### P2 — Promotion queue is a review plan, not automatic integration
The prior digest has 22,920 capability groups and a 16,412-item promotion queue. Queueing and classification do not mean a Skill was deduplicated, adapted, installed, or proven callable. The operator must execute one bounded next action per item and record its output/evidence, or keep it explicitly on shelf.

## Changes applied in this audit window

- `008013f58f2c4788781818c7ecb106dfeefcbf1f`: current-manifest-only extraction processing; stale artifacts fail closed.
- `f30934bb92a2cb0310f54c5cba093297254d262a`: already-installed assets remain visible to verification.
- `913ab024cd1929dd0885003d77979fe72d65405f`: installation workflow shares the Collection writer concurrency group.
- `387becd7ba468a635c4ebfee91c22cef62137186`: restored account-frontier trigger without adding generated outputs to push paths.

## Required release gates

1. Re-run the continuous pipeline on main and require non-empty, valid generated queues.
2. Confirm the run's `git push` succeeds; no non-fast-forward rejection.
3. Require manifest-to-artifact identity, revision, and hash integrity.
4. Report frontier coverage as complete only when all target owner/gist enumerations have explicit terminal outcomes; blocked outcomes keep the sweep partial.
5. Keep generated state under a repository-friendly size using deterministic shards.
6. For each promoted capability, require exact revision + license + dependencies + activation recipe + smoke output + workflow run/attempt + artifact hash.
7. Distinguish `PROVEN_CALLABLE` for a bounded test from `PRODUCTION_PROVEN` for a real end-to-end production path.
8. Only claim production success after these gates pass in actual Actions logs. This audit itself is not runtime evidence.
