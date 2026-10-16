# COLLECTION Recovery Status — 2026-10-16

This note records verified repository evidence after the manifest source-count correction. It supplements, and does not replace, the historical COLLECTION index.

## Verified CI and collection state

- PR #39, `fix(collection): account for preserved manifest source rows`, was merged at merge commit `8b67d407c1e5c6c5cab85e32a41784ff91013011`.
- The PR's `collection-manifest-integrity-test` run #15 completed successfully (run ID `38813443990`).
- A controlled incremental collection run completed successfully: `collection-continuous` run #489, ID `38841155076`, commit `f5c7173ad754e7f2587892019e8620ee50aa2dce`.
- The incremental run explicitly disabled force refresh. Its job completed all listed steps successfully, including extraction/processing, policy and readiness validation, bounded installation, post-install verification queue recording, state revalidation, and persisted install-evidence checks.
- The workflow's concurrency group is `collection-writer`; keep collection writers serialized. Do not run a force refresh merely to repeat a successful incremental run.

## Callable proof already present

The repository contains execution evidence for the installed `juspay/hyperswitch` revision `1d71d94d2e2e1c72f3ede13abebc24132997685f`:

- `COLLECTION/VERIFICATION/HYPERSWITCH-CALLABLE-EVIDENCE.json`: Euclid library tests and deterministic routing smoke are marked `PROVEN_CALLABLE`.
- `COLLECTION/VERIFICATION/HYPERSWITCH-ROUTER-SMOKE-EVIDENCE.json`: one deterministic router unit test is recorded as successful.
- `COLLECTION/MASTER/CALLABLE-REGISTRY.json`: registers deterministic local execution capability.

Scope limitation: these tests do not prove live payment-network connectivity, production payment processing, or production readiness. No secrets or external payment network are required for the cited deterministic tests.

## Installation queue

The latest committed `COLLECTION/VERIFICATION/INSTALLED-QUEUE.json` still records one candidate, `juspay/hyperswitch`, as `READY_FOR_VERIFICATION` / `NOT_CALLABLE_UNTIL_RUNTIME_ENTRYPOINT_AND_EXECUTION_EVIDENCE`. This queue appears older than the separate callable evidence and should be reconciled by the next controlled collection/installation workflow; do not manually promote it without checking the workflow's state guard and generated-state ownership.

## Large-file follow-up — inspect before changing

Previously observed large paths requiring measured analysis:

- `COLLECTION/MASTER/READY.json` (~53.6 MB)
- `COLLECTION/MASTER/PROMOTION-QUEUE.json` (~33.1 MB)
- `COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json` (~20.5 MB)
- GIF under `COLLECTION/INSTALLED/juspay__hyperswitch` (~99 MB)

No deletion, compaction, or asset rewrite is authorized by this note. Next safe actions are to measure file sizes and JSON record counts in a read-only job, inspect consumers/tests for each schema, produce a before/after digest if any transformation is proposed, and verify a restorable Git revision before changing generated data.

## Free execution strategy

Prefer the existing GitHub Actions pipeline for repository-backed work while the Codex balance is unavailable. Avoid adding paid model/API calls. A local or self-hosted runner is only a later option if a reachable machine is available and safe to register; it is not assumed to exist. Any new coding-agent CLI still needs either an available model entitlement or local inference, so installing a CLI alone does not create free model capacity.
