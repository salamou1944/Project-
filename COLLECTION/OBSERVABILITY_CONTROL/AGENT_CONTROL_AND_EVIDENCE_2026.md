# Agent Control / Evidence / Observability — 2026-09-25

Status: DISCOVERY_CAPTURED

## Preloop
- https://github.com/Preloop/Preloop
- MCP firewall, model gateway, budgets, approvals, policy-as-code, session timelines and audit.
- Strong conceptual overlap with evidence-gated autonomous execution.
- Must verify enforcement and isolation before reuse.

## Hecate
- https://github.com/hecatehq/hecate
- Operator UI/runtime for tasks, approvals, sandbox policy, artifacts, retries/resumes, external coding-agent supervision and evidence.
- Useful as a discovery source for control-plane UX and evidence collection patterns.
- Must inspect source before treating evidence claims as proven.

## DojoGenesis Agentic Gateway
- https://github.com/DojoGenesis/gateway
- Self-hosted Go agent runtime with multi-provider routing, DAG orchestration, WASM sandbox, actor supervision and SSE/OpenTelemetry observability.
- Repository documentation describes Docker deployment and non-root runtime.
- Potential value: reference for resilient agent execution and provider abstraction.
- Verification required: license, sandbox threat model, tests and current release.

## General evidence rule
An observability UI, trace, or log is not itself proof that a policy or state transition was enforced. For reuse, inspect the enforcement point, failure paths, persistence, tests and tamper resistance.
