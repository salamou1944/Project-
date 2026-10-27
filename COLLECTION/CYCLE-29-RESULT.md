# Collection cycle 29 — verified result

Date: 2026-10-27

## Execution evidence

- Full-cycle workflow: [Actions run 40436631814](https://github.com/salamou1944/Project-/actions/runs/40436631814) — success.
- Semantic regression audit after the generated-state commit: [Actions run 40438267766](https://github.com/salamou1944/Project-/actions/runs/40438267766) — success.
- Shard reader/writer, migration, and policy regression coverage merged in [PR #48](https://github.com/salamou1944/Project-/pull/48).
- Main-only writer guard and weekly schedule merged in [PR #50](https://github.com/salamou1944/Project-/pull/50).
- Historical semantic audit recovery merged in [PR #51](https://github.com/salamou1944/Project-/pull/51).

## Collection output

- 100 repositories selected for the bounded incremental pass.
- 76 refreshed; 24 blocked attempts preserved.
- 5,846 source rows; 5,822 extracted artifacts validated.
- Inventory: 31,513 repositories; 18,593 deferred; 1,735 prior sources preserved but not selected.
- License metadata is now carried from revision-validated extraction artifacts into cached and preserved manifest rows. Missing or mismatched artifacts remain blocked; no license is inferred from a repository name.

## State-file partitioning

| State file | Records/items | Shards | Total shard bytes | Largest physical shard |
|---|---:|---:|---:|---:|
| READY.json | 51,667 | 11 | 90,695,293 | 8,388,320 bytes |
| PROMOTION-QUEUE.json | 35,484 | 7 | 53,640,665 | 8,388,131 bytes |
| CANONICAL-PROMOTION-PLAN.json | 35,484 | 8 | 61,237,277 | 8,388,520 bytes |

Shard manifests, per-shard hashes, item counts, semantic round trips, and state guards passed. The largest physical file is now approximately 8.4 MB, below GitHub's 50 MB recommended file-size threshold.

## Semantic evidence preservation

- Current-main JSON audit: 13,846 JSON/JSONC files; 0 parse failures; 1,023,124,539 bytes.
- Latest semantic audit verified 243 prior evidence records against exact historical source packets; 0 prior evidence identities remain missing.
- Sixty-seven old BLOCKED_EXTERNAL_ACCESS rows had no revision SHA and no artifact path. They were metadata-only failed discovery attempts, not extracted evidence. The audit now classifies them separately rather than falsely treating them as lost source artifacts.
- The semantic audit still fails closed if an extracted source revision, prior evidence file, or content hash cannot be verified in current or immutable historical snapshots.

## Installation outcome

The installation step completed without error but returned NO_APPROVED_CANDIDATES:

- installed or already installed: 0
- ready for verification: 0
- blocked by size: 0

This is an intentional fail-closed result. Candidate-specific install approval and independent integration/security PASS evidence are still absent. The pipeline must not turn an unreviewed source into a usable asset by changing status labels. No new asset is claimed as installed or production-ready.

## Weekly operation

The deep-extraction refresh remains scheduled for Sundays at 03:20 UTC. The bounded full Collection cycle is scheduled for Sundays at 05:20 UTC on main. Marker-triggered runs and the writer job are restricted to main to prevent feature-branch pushes from starting a writer that updates main.
