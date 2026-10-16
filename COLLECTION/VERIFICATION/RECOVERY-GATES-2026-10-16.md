# COLLECTION recovery gates — 2026-10-16

## Verified state

- PR #39 is merged into `main` (merge commit `8b67d407c1e5c6c5cab85e32a41784ff91013011`). Its `collection-manifest-integrity-test` run #15 passed on the PR head.
- This verifies the manifest-count regression test only. It is **not** evidence that a full harvest/install cycle passed after merge.
- `.github/workflows/collection-continuous.yml` currently exposes manual `workflow_dispatch` and a force-refresh marker push. Its workflow comment says automatic harvest triggers are disabled pending verified recovery.
- `COLLECTION/INDEX.md` still says it was updated on 2026-10-07. Do not change that date until the current index is reconciled against the latest successful collection run.
- `COLLECTION/MASTER/READY.json` and `PROMOTION-QUEUE.json` exceed the GitHub connector's 64 MiB response ceiling in decoded form. This is a retrieval limitation, not proof that the JSON is corrupt.
- The installed Hyperswitch checkout is pinned to revision `1d71d94d2e2e1c72f3ede13abebc24132997685f`, Apache-2.0, with install marker status `INSTALLED`. The marker alone is not runtime proof. However, the callable registry and `COLLECTION/VERIFICATION/HYPERSWITCH-CALLABLE-EVIDENCE.json` record successful deterministic smoke evidence for `cargo test -p euclid --lib` (run [37737832199](https://github.com/salamou1944/Project-/actions/runs/37737832199)), Euclid routing benchmark (run [37752754856](https://github.com/salamou1944/Project-/actions/runs/37752754856)), and a Router unit smoke (run [38016666373](https://github.com/salamou1944/Project-/actions/runs/38016666373)). These prove only the specified local library/unit paths, not the whole payment service, live payment-network execution, or production payment processing. The aggregate `INSTALLED-QUEUE.json` still labels the repository `READY_FOR_VERIFICATION`; retain that conservative whole-repository state until the queue semantics explicitly distinguish verified sub-capabilities from full-application readiness.
- `RESTRICTED-QUEUE.json` contains quarantined items with restriction signals (for example, a filename containing `secret`). Do not promote these without their documented safety/authorization gate.

## Safe next execution sequence

1. Keep the large generated manifests untouched; do not delete, compact, or regenerate them as a diagnostic.
2. Run the existing unit/regression gates first on the merged `main`: `test_install_assets_selection.py`, `test_installation_outcome.py`, `test_extraction_cache_policy.py`, `test_ready_json_compaction.py`, and `test_collection_policy.py`.
3. Run the normal `collection-continuous` workflow only as a normal incremental/manual run with `force_refresh=false`. Do not use the marker file or set `force_refresh=true` for this recovery attempt.
4. Confirm the run's final conclusion and inspect every failed step. Then verify that the generated state guard, readiness validator, callable registry validator, installation report, and installed verification queue all completed. A successful workflow is still not proof an installed third-party app is callable.
5. Only after a successful full run, reconcile `COLLECTION/INDEX.md` with the run timestamp and actual output counts.
6. For Hyperswitch, first inspect its manifest, Cargo workspace/package entry points and required services. Choose one narrow, local, non-production test that can run without credentials or paid APIs. Record exact command, exit code and output before changing any callable status.
7. Evaluate large-file redesign separately: record exact byte sizes, JSON schema/consumer inventory, current Git blob IDs and recovery path first. Prefer a versioned compact/indexed representation with compatibility readers and round-trip tests; do not overwrite canonical data in the same change that introduces the new format.

## Constraints

- No Codex credit is assumed available. Prefer GitHub-hosted CI and direct repository operations that do not require a Codex session or paid model calls.
- Never describe an asset as usable based only on its presence in `INSTALLED`; require a real runtime invocation.
- Never claim the full collection cycle passed based only on PR #39's focused CI test.
