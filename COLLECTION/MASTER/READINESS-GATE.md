# Collection Readiness Gate

Status: ACTIVE / PERMANENT COLLECTION RULE  
Purpose: close the boundary between **preserved evidence** and an asset that can actually be activated or used, without weakening the existing promotion/security gates.

## Why this gate exists

The Collection already has two intentional protections:

1. **Promotion is not readiness.** \`PROMOTION-GATE.md\` controls whether evidence becomes a canonical Skill decision (NEW / UPGRADE / MERGE / REFERENCE / QUARANTINE).
2. **Verification is not production proof.** The Collection closure rules separate discovered, inspected, extracted, verified and reusable states, and the leverage matrix already requires \`DISCOVERY -> VERIFIED -> INTEGRATED -> TESTED -> HUMAN_READY\`.

The missing piece was not another discovery or Skill system. The missing piece was an explicit, machine-checkable bridge for **every retained asset** between ON-SHELF and actual activation/use.

This gate therefore sits **after preservation/promotion**, not inside the promotion decision.

## Readiness states

- \`ON_SHELF\` — preserved, searchable, provenance retained; not claimed usable.
- \`READY_FOR_ADAPTATION\` — source revision, license, dependencies, limits and reusable boundary are understood well enough to begin bounded adaptation.
- \`READY_ON_DEMAND\` — a reproducible activation recipe exists: dependencies, configuration schema, activation command/path, smoke test, expected result, known limits, and evidence references are recorded. It may still depend on an external credential, credit, service, GPU, or other explicitly recorded prerequisite. This means **ready to activate when the prerequisite exists**, not currently running.
- \`READY_TO_USE\` — the activation/use path has actually succeeded in the target environment and produced the expected artifact/result, with current evidence.
- \`INTEGRATED\` — the capability is wired into one of our canonical projects/systems.
- \`TESTED\` — the integrated path has passed the applicable automated/integration acceptance tests.
- \`HUMAN_READY\` — the path has passed the human-usable acceptance required by the consuming project.
- \`PRODUCTION_PROVEN\` — real production/runtime evidence exists for the exact revision and environment.
- \`QUARANTINED\` — blocked by the existing safety/authorization boundary; no readiness promotion is permitted.

No state implies another state automatically.

## Required evidence for activation readiness

A \`READY_ON_DEMAND\` declaration must identify:

- asset/capability key;
- exact source revision;
- license/boundary;
- dependencies and runtime prerequisites;
- configuration schema (never secrets);
- reproducible activation recipe;
- smoke/contract test and expected result;
- known limitations and external blockers;
- evidence references.

\`READY_TO_USE\` additionally requires:

- successful execution evidence in the target environment;
- produced artifact/result reference;
- timestamp/freshness;
- environment/runtime identity;
- exact revision binding.

\`INTEGRATED\`, \`TESTED\`, \`HUMAN_READY\`, and \`PRODUCTION_PROVEN\` require their respective direct evidence. Documentation, README claims, source presence, or a Collection listing alone can never satisfy these states.

## State transitions

\`\`\`
DISCOVERED
  -> PRESERVED / ON_SHELF
  -> VERIFIED
  -> READY_FOR_ADAPTATION
  -> READY_ON_DEMAND
  -> READY_TO_USE
  -> INTEGRATED
  -> TESTED
  -> HUMAN_READY
  -> PRODUCTION_PROVEN
\`\`\`

A state may remain ON-SHELF indefinitely. A blocked external dependency does not become a false success; it remains explicitly blocked while its activation recipe can still be READY_ON_DEMAND.

\`QUARANTINED\` is a side branch from any unsafe/restricted evidence and cannot advance until the existing safety/authorization gate clears it.

## Collection processor rule

\`COLLECTION/AUTO/process_collection.py\` now emits \`COLLECTION/MASTER/READINESS-QUEUE.json\`.

The processor may assign only:

- \`ON_SHELF\` for non-quarantined collected evidence;
- \`QUARANTINED\` for restricted evidence.

It must **never infer** \`READY_ON_DEMAND\`, \`READY_TO_USE\`, \`INTEGRATED\`, \`TESTED\`, \`HUMAN_READY\`, or \`PRODUCTION_PROVEN\` from source inspection alone.

Those states require an explicit readiness declaration and evidence.

## Operational rule

Before using an asset, search the readiness queue first:

1. \`READY_TO_USE\` / \`PRODUCTION_PROVEN\` — use only if the current revision and environment still match.
2. \`READY_ON_DEMAND\` — activate using the recorded recipe and run the smoke test.
3. \`READY_FOR_ADAPTATION\` — adapt only through a bounded, evidence-producing change.
4. \`ON_SHELF\` — inspect/verify/adapt before use.
5. \`QUARANTINED\` — do not activate.

This makes ON-SHELF a real inventory state rather than an ambiguous “maybe ready” bucket.

## Non-regression rules

- Preserve all source provenance even after adaptation/integration.
- Never copy third-party code wholesale merely to reach a readiness state.
- Never convert \`VERIFIED_EXTERNAL_READY\` into \`READY_TO_USE\` without target-environment execution evidence.
- Keep paid/cloud/external prerequisites explicit.
- Never let a missing prerequisite become a fake pass.
- Readiness does not replace canonical Skill dedupe/promotion; the two gates remain separate.
