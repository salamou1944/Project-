# OmniRoute — Collection Record

Status: DISCOVERY_CAPTURED

Source:
- Repository: https://github.com/diegosouzapw/OmniRoute
- License: MIT (per repository README)
- Revision observed: release/v3.8.51
- Captured: 2026-09-27

Observed capabilities:
- Unified AI gateway with one OpenAI-compatible endpoint.
- README currently advertises 359 providers, 150+ free providers, and 1200+ models.
- Quota-aware automatic fallback/routing.
- RTK+Caveman context/token compression.
- MCP and A2A support.
- Desktop/PWA and self-hosting paths.
- Free-provider onboarding documented in the repository.
- Local API/dashboard default shown as localhost:20128 and /v1.

Potential reuse targets:
- EASY: provider abstraction, fallback, quota-aware routing, and reduced single-provider dependency.
- Salamou-31 / API Factory: OpenAI-compatible gateway, multi-provider routing, MCP/A2A integration patterns.
- Elite / ARMY-14: resilience/routing and agent-to-agent integration patterns where independently verified.
- Cost reduction: free/self-hosted provider paths and token compression, subject to provider terms and actual quotas.

Important verification boundary:
- Discovery capture is not adoption.
- Provider availability, free quotas, authentication requirements, model quality, security controls, and operational behavior must be verified from source code/docs before integration.
- Do not treat a provider being listed as proof that it is permanently free or production-safe.
- Do not copy the whole project into a product repository; reuse only verified capabilities with explicit provenance.

Evidence:
- README: https://github.com/diegosouzapw/OmniRoute
- Wiki: https://github.com/diegosouzapw/OmniRoute/wiki
