# Collection Deep Extraction Gate

Status: ACTIVE

This gate adds a capability that did not previously exist: **account-wide, high-density extraction packets prepared for canonical dedupe/adaptation**.

It does not replace the existing promotion or runtime-readiness gates.

## Red-line non-duplication rule

Before adding or changing an extraction contract:
1. inspect the existing Collection automation and canonical Skill layer;
2. prove the behavior is absent or materially insufficient;
3. add only the missing behavior;
4. do not create a second implementation of an existing contract.

## What this layer adds

- derives owners from the existing `COLLECTION/ACCOUNTS/*.md` source graph;
- enumerates all public repositories for those owners;
- performs multi-pass extraction across distinct asset buckets instead of a single top-N file slice;
- binds every extracted packet to an exact source revision and file hash;
- redacts obvious credential values before preservation;
- produces `EXTRACTION-READY-QUEUE.json` for downstream dedupe/adaptation;
- keeps `readiness_state=ON_SHELF`; extraction readiness is never runtime readiness.

## Density policy

Default per repository:
- up to 48 high-value files;
- up to 100 KB per file;
- up to 1.5 MB total;
- bucket quotas preserve breadth across contracts, agents, runtime, security, data, ops, evaluation, media and docs.

These are bounded extraction limits, not claims of exhaustive source inspection. A truncated tree or blocked repository remains explicitly recorded.

## Handoff

`READY_FOR_DEDUPE` means the extracted packet is ready to enter canonical comparison/adaptation.

It does **not** mean:
- READY_ON_DEMAND;
- READY_TO_USE;
- INTEGRATED;
- TESTED;
- HUMAN_READY;
- PRODUCTION_PROVEN.

Those remain governed exclusively by `READINESS-GATE.md`.
