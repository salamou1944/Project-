# COLLECTION recovery status — 2026-10-16

## Scope and safety

This note records repository evidence after PR #39 merged. It does not claim a successful end-to-end collection/install cycle. No generated queue, manifest, vendored source, or large binary was deleted or rewritten as part of this review.

## Manifest fix

- PR: https://github.com/salamou1944/Project-/pull/39
- Merge commit: `8b67d407c1e5c6c5cab85e32a41784ff91013011`
- The policy check now validates `repo_count + gist_count + preserved_sources_after_refresh_failure == len(sources)`.
- PR check: https://github.com/salamou1944/Project-/actions/runs/38813443990 — `collection-manifest-integrity-test` succeeded.
- The latest full `collection-continuous` run inspected was run 38798102097 on pre-merge commit `4cabc9c463041d945a8220bf8f46a664d93b8434`. It failed at the old assertion in `test_collection_policy.py`; the harvest and state-regression guard steps passed. This run predates the merge and is not evidence of the current main branch failing after PR #39.

## Current generated state and large-file risks

Repository tree inspection on main found these large tracked files:

| Path | Approx. size | Risk / next step |
| --- | ---: | --- |
| `COLLECTION/MASTER/READY.json` | 51.1 MiB | Keep canonical data intact; measure JSON parsing and regeneration cost, then evaluate a versioned compact/indexed representation with round-trip tests. |
| `COLLECTION/MASTER/PROMOTION-QUEUE.json` | 31.5 MiB | Same; inspect producer/consumer contracts before changing serialization. |
| `COLLECTION/MASTER/CANONICAL-PROMOTION-PLAN.json` | 35.4 MiB | Determine whether it is a derived duplicate or an independently consumed canonical artifact before proposing deduplication. |
| `COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json` | about 20 MiB in the prior inspection | Preserve quarantine evidence; optimize read/index paths rather than dropping records. |
| `COLLECTION/INSTALLED/juspay__hyperswitch/docs/gifs/quickstart.gif` | 94.4 MiB | Confirm upstream provenance and references; only consider Git LFS or exclusion from vendored snapshots after a reproducible source/restore plan. |

The GitHub contents API rejected `PROMOTION-QUEUE.json` because its decoded response exceeded the tool's 64 MiB response limit. That is a tooling/representation limitation, not proof that the JSON is corrupt.

## Installed asset verification

The current install marker pins `juspay/hyperswitch` to revision `1d71d94d2e2e1c72f3ede13abebc24132997685f`, license `Apache-2.0`, with `status: INSTALLED` and vendored-source mode. The installation report says `ALREADY_INSTALLED`. These prove source presence and revision pinning, not runtime callability.

The existing `collection-installation.yml` defines a deterministic router smoke test:
`cargo test -p router --lib test_profile_id_unavailable_initialization`
It only records `PROVEN_CALLABLE` evidence after that test succeeds. The smoke test has not been verified by the evidence reviewed in this recovery note, so no callable claim is made here.

## Controlled next steps

1. Run `collection-continuous` manually with `force_refresh=false` after PR #39, then inspect all steps and confirm the run used the merge commit or a descendant. Do not push `.github/COLLECTION_FORCE_REFRESH_ONCE`, because that path forces a full refresh.
2. If the full cycle passes, separately verify whether the installation and callable smoke steps ran; do not infer runtime success from a successful manifest test.
3. Run `collection-installation` only as a separately reviewed action if the full cycle does not already execute the existing deterministic smoke test.
4. Before any large-file refactor, create and verify an immutable backup or reproducible regeneration path; record hashes, producers, consumers, and round-trip tests. No large-file rewrite or deletion is authorized by this note.
5. Refresh `COLLECTION/INDEX.md` only after the post-merge full-cycle result is known, so its status/date reflects verified state rather than this review alone.

## Constraint

Codex balance is unavailable. This recovery used the connected GitHub repository interface and did not depend on Codex execution, paid model calls, or new API keys.
