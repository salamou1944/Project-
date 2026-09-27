# RuFlo capture — 2026-09-27

Source: https://github.com/ruvnet/ruflo
Revision inspected: main at README SHA e5233c9aa886d2aa9f47ce6c0c74df355913c26f; witness spec SHA 8a8007f72fc82cec8ec98f6f6523c26c170b2a89.
License: MIT verified from repository LICENSE.
Status: VERIFIED_SOURCE_CAPTURED; selected patterns are not automatically production capabilities.

## High-value patterns for AI Operating Operator

1. Witness/receipt verification
- Canonical JSON (RFC 8785 JCS), SHA-256 content IDs, Ed25519 domain-separated signatures.
- Explicit evidence grades: recomputed, signature-verified, trusted-assertion.
- Independent verifier must reject "independently verified" when an authorizing term is only an unapproved assertion.
- Evidence references carry provenance/authority scope; verification resolves them before promotion.
- Gate/schema versions are exact and non-retroactive.
- Cross-repo boundaries must preserve separation of proposer and promotion authority.

Operator leverage: strengthen Evidence Ledger + Independent Verifier with typed evidence grades, provenance scope, exact gate/schema versioning, and explicit cross-repo identity separation. Do not copy Ruflo's statistical flywheel gate into ordinary task completion.

2. Optional augmentation / fail-closed dependency pattern
- ruflo-metaharness is deliberately removable.
- MetaHarness is optionalDependencies, not a required boot dependency.
- Missing dependency/network failure emits degraded state rather than pretending capability exists.
- CI proves the system still operates with optional package removed.
Operator leverage: apply the same removable-augmentation rule to external research/browser/Cua/local-LLM components.

3. Harness security/readiness audit
- Pure-read MCP scan; severity-ranked findings; configurable fail threshold.
- Threat-model and drift-from-history concepts.
Operator leverage: add a read-only operator capability audit stage before promotion/deployment; findings must remain evidence, not authorization.

4. Goal planning and adaptive replanning
- Goal-oriented decomposition into preconditions/actions/effects.
- Replan from current state after failure rather than restarting blindly.
Operator leverage: improve task planner/router with explicit state transitions and bounded replanning, while keeping executor permissions independent.

5. Memory provenance and namespace isolation
- Memory records include provenance, tenant, namespace, source digest, observation/creation time, expiry, confidence and revocation in newer Ruflo architecture.
Operator leverage: keep collection/project memories separated; retrieval must carry source/provenance and must never become execution authority by itself.

6. Model/provider routing
- Ruflo documents hybrid routing and feedback-driven model selection.
Operator leverage: feed provider health/cost/quality evidence into routing, but keep external dependency failures fail-closed.

## Explicit limitations / non-copy rules
- Do not treat README feature counts as operational proof.
- Do not import unrestricted swarm/federation authority.
- Do not make MetaHarness a hard dependency.
- Do not promote memory/retrieval results into permissions.
- Ruflo itself documents implementation gaps in parts of its intelligence stack; selected patterns require independent tests.
- Do not use flywheel promotion statistics as a generic "task succeeded" gate; that protocol targets policy/evolution promotion.

## Promotion targets
DISCOVERY -> VERIFIED -> ADAPTER_READY -> INTEGRATED -> TESTED -> HUMAN_READY.
This capture is VERIFIED as a source/pattern record only. Runtime integration remains separately tested.
