# reticlehq/reticle — COLLECTION capture

- Source: https://github.com/reticlehq/reticle
- Captured: 2026-10-07
- Category: AI agent verification / runtime proof
- Status: EXTRACTED_PENDING_INTEGRATION
- Reuse decision: HIGH-VALUE MERGE/UPGRADE candidate; do not import wholesale.

## Verified source capabilities

Reticle is a proof/verification layer for AI coding agents. It drives a real running application, observes runtime evidence, and produces pass/fail/unknown verdicts with diagnostic source location where available.

Core loop:
- LOOK
- ACT
- OBSERVE
- ASSERT

Important implementation boundary:
- `@reticlehq/engine` is intentionally isolated from browser, server, CLI and storage.
- The engine consumes runtime events and assertions and decides whether the expected condition held.
- Reticle explicitly treats `unknown` as not-pass when evidence is insufficient.
- Only verification operations that produce a verdict count as proof; observation/action alone does not.

Runtime evidence surfaces include:
- DOM/application state
- network requests and status
- console errors
- routing
- framework/store state
- event cardinality and contradictions

High-value diagnostic patterns:
- first divergence
- evidence-backed verdicts
- source file/line diagnosis
- recorded flows that can be replayed as regression guards
- batch verification of flows
- local/localhost execution
- MCP exposure to coding agents

Safety/resource patterns:
- dev-only SDK
- localhost-only bridge
- fixed command/tool surface rather than arbitrary JavaScript execution
- credential redaction before agent exposure
- local verdict generation
- explicit telemetry controls

## Collection leverage

1. Upgrade the existing evidence-bound completion rule: discovery != execution != verification.
2. Extract a reusable runtime-verification contract for SOAT / Elite / ARMY-14.
3. Extract a verdict contract with PASS / FAIL / UNKNOWN and evidence requirements.
4. Extract first-divergence + file:line diagnosis as a reusable repair signal.
5. Extract replayable-flow/regression-guard pattern.
6. Evaluate the standalone engine rules for reuse without importing the full Reticle runtime.
7. Evaluate MCP verification-tool contracts for AI Operating / agent-skills.

## Dedupe boundary

Do not duplicate existing SOAT, evidence, observability, or agent-skills infrastructure. Reticle is retained as a source and reference for the specific missing/stronger primitives above.

## License boundary

The repository states that SDK/adapters/core/engine are Apache-2.0. The server/CLI/init components use FSL-1.1 with ALv2 conversion terms. Any code reuse must be checked at path/package level before implementation.

## Verification boundary

Repository inspection is not runtime proof. Before promoting implementation into production, require source revision, license/dependency inspection, implementation inspection, adapter contract, tests, health/reachability evidence, and independent verification.
