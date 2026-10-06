# Collection Promotion Gate

This gate is the boundary between harvested evidence and canonical Skills.

## Allowed terminal promotion classes

These are terminal states only:

- NEW: a reusable Skill does not exist yet.
- UPGRADE: an existing Skill is strengthened by verified evidence.
- MERGE: multiple findings are consolidated into one canonical Skill.
- REFERENCE: retained as knowledge; no Skill is created.
- QUARANTINE: retained for controlled review; never promoted automatically.

### Transitional review states

`REVIEW_*` queue actions are non-terminal and must not be presented as completed promotion decisions. They mean the evidence is retained for the canonical dedupe/validation gate. The processor may emit `REVIEW_NEW_OR_UPGRADE` for a single-source candidate or `REVIEW_MERGE_OR_UPGRADE` for multi-source evidence. Only after canonical Skill comparison and validation may the item receive one of the five terminal states above.

`RESTRICTED` is not a terminal promotion class. Restricted evidence enters `QUARANTINE` and the safety/authorization gate.

## Required evidence

A promotion candidate must have:
1. source and immutable revision;
2. license information;
3. evidence identifier and content hash;
4. capability family;
5. dedupe decision against the canonical Skills repository;
6. validation evidence before the Skill is considered ready.

## Separation and provenance rule

Collection evidence is provenance, not execution proof. Source application code is not copied wholesale into Skills. Distinct source captures remain preserved as provenance even when their capabilities are semantically equivalent; deduplication applies to the canonical Skill layer, not to historical source evidence.

## Completion rule

Every retained candidate ends in one explicit state: NEW, UPGRADE, MERGE, REFERENCE, or QUARANTINE, with a recorded reason.
