# EXTERNAL READY CAPABILITY MATRIX — 2026-10-05

This is the next execution layer after READY_EXTERNAL_PROJECTS.
No project is copied or integrated by this file.

## P0 — OpenHands
**Best immediate leverage:** engineering automation/control plane.
- Self-hosted Agent Canvas.
- Supports OpenHands and ACP-compatible agents, including Codex/Claude Code/Gemini.
- Supports local/Docker/VM/cloud backends and webhook/scheduled automations.
- Important security boundary: its README warns that no-sandbox mode gives the agent filesystem access; sandbox/self-hosting hardening is mandatory before exposing it to production.
**Decision:** evaluate first for the engineering/Elite/agent-skills operating loop, not as a replacement for those systems.

## P0 — LiteLLM
**Best immediate leverage:** provider abstraction and routing.
- Unified OpenAI-compatible interface for 100+ LLM providers.
- Python SDK + proxy/gateway.
- Proxy includes virtual keys, spend tracking, guardrails and load balancing.
- Package metadata currently declares Python >=3.10,<3.15 and MIT for the core package.
**Decision:** strongest candidate for API Factory/provider-routing capability, but compare against existing Salamou-31 gateway code before integrating to avoid duplication.

## P0 — Ollama
**Best immediate leverage:** local inference fallback.
- MIT licensed.
- Local model runtime.
**Decision:** use as a $0/local path for development and provider-independent tests where model quality is sufficient. It does not replace cloud providers for workloads that need them.

## P1 — OmniRoute
**Best immediate leverage:** broad provider/fallback layer and free-tier discovery.
- Canonical repo: diegosouzapw/OmniRoute.
- Current package version verified: 3.8.52.
- Current default branch verified: release/v3.8.52.
- Package declares MIT.
- Package exposes OpenAI-oriented routing plus auto-fallback; repository also contains Docker Compose profiles, MCP/A2A and Codex app-server integration paths.
**Decision:** do NOT integrate wholesale. Extract only capabilities that beat the existing Salamou-31/API Factory implementation, especially provider catalog/free-tier intelligence and fallback/routing.

## Integration order

1. OpenHands → engineering automation evaluation.
2. LiteLLM → API Factory capability comparison.
3. Ollama → local fallback/test lane.
4. OmniRoute → routing/free-tier capability extraction only.

## Hard rule

No “ready” asset becomes part of a production project until:
- exact revision is pinned;
- dependencies and license boundary are recorded;
- smallest reusable capability is identified;
- isolated test passes;
- integration has production evidence.

Status: CAPABILITY_MAPPED
