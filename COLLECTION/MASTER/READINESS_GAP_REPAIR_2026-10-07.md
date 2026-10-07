# Collection Readiness Gap Repair — 2026-10-07

## Audit conclusion

The apparent gap was **not** a missing Collection architecture.

Existing Collection design already intentionally separated:
- source discovery/preservation;
- canonical Skill promotion;
- external verification/adaptation;
- integration/testing/human readiness.

The reason for that separation is correct: source evidence and promotion decisions must never be mistaken for runtime proof.

The actual gap was narrower:

> every retained asset did not have an explicit, machine-checkable state describing whether it was merely on the shelf, ready to activate on demand, actually usable, integrated, tested, human-ready, or production-proven.

## Repair applied

1. Added `COLLECTION/MASTER/READINESS-GATE.md`.
2. Added `COLLECTION/MASTER/READINESS-DECLARATION.schema.json`.
3. Added fail-closed `COLLECTION/AUTO/validate_readiness.py`.
4. Extended `COLLECTION/AUTO/process_collection.py` to emit `COLLECTION/MASTER/READINESS-QUEUE.json`.
5. Materialized the current readiness queue from the existing Collection evidence.
6. Extended Collection policy tests and both Collection workflows so readiness integrity is enforced automatically.
7. Added workflow concurrency serialization after observing real concurrent-write failures during verification.

## Current state after repair

Current Collection evidence produced:
- 755 capability groups;
- 509 non-quarantined items explicitly classified `ON_SHELF`;
- 246 restricted items explicitly classified `QUARANTINED`;
- 0 assets were falsely promoted to `READY_ON_DEMAND` or `READY_TO_USE`.

This is intentional.

A future asset can move to `READY_ON_DEMAND` only when its activation recipe, dependencies, configuration schema, smoke test, limitations and evidence are explicitly recorded.

It can move to `READY_TO_USE` only after successful target-environment execution evidence exists.

## Non-regression

This repair does not:
- replace the existing promotion gate;
- deduplicate or delete historical provenance;
- copy third-party projects wholesale;
- turn `VERIFIED_EXTERNAL_READY` into production readiness;
- treat paid/external blockers as success;
- weaken the quarantine boundary.

The resulting operating path is:

**COLLECT → PRESERVE → PROMOTE/REFERENCE/QUARANTINE → ON_SHELF → READY_FOR_ADAPTATION → READY_ON_DEMAND → READY_TO_USE → INTEGRATED → TESTED → HUMAN_READY → PRODUCTION_PROVEN**

The states are evidence-gated and independent; no later state is inferred from an earlier one.

## Verification note
The Collection workflows now share a repository-level concurrency group so the promotion/readiness gates do not race each other on writes.
