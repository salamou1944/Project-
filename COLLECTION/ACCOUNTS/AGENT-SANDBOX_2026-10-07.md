# Agent-Sandbox — Account Capture — 2026-10-07

Status: ACCOUNT_CAPTURED / HIGH-LEVERAGE CANDIDATE

## Owner
- https://github.com/agent-sandbox
- Public repositories enumerated: 2

## Repositories
1. agent-sandbox — active, Apache-2.0
2. agent-sandbox.github.io — active documentation site

## Primary source
https://github.com/agent-sandbox/agent-sandbox
Revision inspected: 6f7b273ea80732b063d1d1a914b7138780fa83a0 (README/docs search evidence)

## High-value reusable material
- Self-hosted Kubernetes-native sandbox runtime for AI agents.
- REST API + MCP server; agents can create/use/delete sandboxes without kubectl.
- Full E2B protocol/SDK compatibility.
- Isolated code execution, browser use, computer/desktop use and shell workflows.
- Per-agent/per-user multi-tenant isolation.
- Sandbox Pool for pre-warmed low-latency allocation.
- Pause/resume, snapshots and scale-to-zero lifecycle.
- Leader election, events, metrics and logs.
- Blueprint/Template separation with live-editable deployment/type layers.
- Dynamic regex-matched templates and per-template resource/warmup/pool controls.
- Built-in UI and single-component deployment.

## Evidence
- README and web/docs/overview.md explicitly describe the above capabilities.
- Discovery evidence is not runtime proof in this collection record.
- Deployment requires Kubernetes >=1.28; therefore this is not a zero-infra replacement for local lightweight execution.
- License: Apache-2.0.

## Semantic comparison
- Strong overlap with existing COLLECTION sandbox/isolation, CUA, OpenShell and evidence-gated execution material.
- Distinct leverage: E2B-compatible lifecycle + pre-warmed pool + snapshot/pause/resume + browser/computer/shell in one self-hosted runtime.
- Decision: preserve as source evidence and upgrade existing sandbox/agent-execution canonical Skill rather than create a duplicate capability family.

## Downstream candidates
- Existing Elite / agent-skills execution isolation.
- AI Operating runtime execution boundary.
- CUA/browser workflows.
- SOAT evidence and cleanup lifecycle.

## Boundary
Do not wholesale import. Extract lifecycle contracts, isolation controls, pool/snapshot semantics, and E2B compatibility patterns only after source-level verification.
