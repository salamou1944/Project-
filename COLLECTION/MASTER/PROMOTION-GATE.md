# Collection Promotion Gate

This gate is the boundary between harvested evidence and canonical Skills.

## Allowed promotion classes

- NEW: a reusable Skill does not exist yet.
- UPGRADE: an existing Skill is strengthened by verified evidence.
- MERGE: multiple findings are consolidated into one canonical Skill.
- REFERENCE: retained as knowledge; no Skill is created.
- QUARANTINE: retained for controlled review; never promoted automatically.

## Required evidence

A promotion candidate must have:
1. source and immutable revision;
2. license information;
3. evidence identifier and content hash;
4. capability family;
5. dedupe decision against the canonical Skills repository;
6. validation evidence before the Skill is considered ready.

## Separation rule

Collection evidence is provenance, not execution proof. Source application code is not copied wholesale into Skills.

## Completion rule

Every retained candidate ends in one explicit state: NEW, UPGRADE, MERGE, REFERENCE, or QUARANTINE, with a recorded reason.
