# Hikhakk / Higgsfield — Reusable Reliability Skill Pack — 2026-10-06

Source: https://github.com/Hikhakk/higgsfield-mcp-unified
Canonical collection record: COLLECTION/ACCOUNTS/HIKHAKK_2026-10-06.md

## Purpose
Convert proven implementation patterns from the source repository into reusable skill specifications instead of storing the repository as passive knowledge.

## Skills

### 1. provider-preflight
Before an expensive provider action, verify credentials, configuration and reachability without consuming the paid operation.
Evidence: source exposes preflight_check for backend auth/config validation.

### 2. provider-error-taxonomy
Normalize provider failures into stable categories such as authentication, network, schema and HTTP/provider errors so callers can make deterministic decisions.
Evidence: source implements typed backend error classification.

### 3. retry-backoff-jitter
Retry transient provider/network failures with bounded backoff, jitter and Retry-After support.
Guardrail: never retry non-transient validation/auth failures blindly.

### 4. circuit-breaker
Stop repeatedly calling a failing provider after a failure threshold and allow controlled recovery probes.
Goal: prevent cascading failures and wasted calls/credits.

### 5. idempotent-execution
Attach a stable idempotency key to a logical operation and preserve it across retries.
Goal: avoid duplicate provider jobs/charges.

### 6. provider-model-registry
Maintain one registry of providers/models with capability metadata and verification confidence.
Goal: route only to known-valid combinations by default.

### 7. capability-model-selection
Select a model from intent + capability constraints without performing the expensive generation itself.
Goal: separate discovery/selection from execution.

### 8. structured-output-contract
Return typed/schema-bound tool results instead of opaque provider blobs.
Goal: make downstream orchestration deterministic and testable.

### 9. provider-adapter-boundary
Hide provider-specific transport/auth/request details behind a stable adapter interface.
Goal: allow provider replacement without rewriting business logic.

### 10. evidence-smoke-verification
Expose cheap checks for configuration, reachability and contract validity before declaring an execution path ready.
Goal: enforce the rule: no mock = no production claim.

## Dedupe / integration rule
These are extraction candidates, not ten new duplicate skills. First map each capability to existing skills in salamou1944/agent-skills and AI_operating_memory. If an equivalent skill exists, strengthen it with the missing evidence/pattern instead of creating another name.

## Priority integration targets
1. AI Operating
2. agent-skills / Elite / ARMY-14
3. Salamou-31 API Factory
4. EASY Creative Engine

## Safety / licensing boundary
MIT source. Reuse implementation patterns with attribution/provenance. Do not import the experimental private-web-backend automation as a default production dependency.
