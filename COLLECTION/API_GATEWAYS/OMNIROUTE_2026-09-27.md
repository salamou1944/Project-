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


## Source recheck — 2026-10-19

- Canonical source: [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute), MIT license, active release branch `release/v3.8.52`, last pushed `2026-10-19T01:33:39Z`. Do not substitute a fork/clone for the canonical source.
- Current README advertises 375 providers, 1,400+ models and 468 free-tier entries across 34 recurring pools; the aggregate estimate is ~1.62B recurring tokens/month. These are project-published catalog estimates across independent third-party accounts, **not** a token grant or guaranteed free capacity from OmniRoute.
- The upstream `docs/reference/FREE_TIERS.md` still declares version 3.8.50 / last updated 2026-10-18, but its research note says 2026-06-17 with a partial re-audit 2026-09-02 and selected checks 2026-10-08. Treat counts as discovery evidence and revalidate each provider's official pricing, terms, region, eligibility, hard-stop billing behavior and quota before routing.
- Existing source-level integration in Salamou-31 adopts OmniRoute's **schema/decision rules only**, not its runtime. Keep that boundary; do not create another gateway or copy the project wholesale.
- Local Ollama compose is relevant to the already-proven CI test path. For self-hosting, prefer the loopback-bound compose defaults; the separate local-Ollama compose publishes port 20128 on `0.0.0.0` by default and must not be exposed on an untrusted network without explicit authentication/reverse-proxy protection.
- The canonical repo has a substantial dependency/build surface (Node >=22.22.2, workspaces, native/optional build steps, large generated docs/catalogs). Preserve as a reference asset; **do not install or deploy it in this pass**. First compare specific routing/quotas features against the existing API Factory and test only isolated, reviewed components.
- The separate `mnfst/awesome-free-llm-apis` catalog's malicious `security-audit.yml` was removed at commit `cf97c32fec1b2e96e9936746e2731a81bd5ea33f`; the latest visible workflow run remains from 2026-10-05 and no later run proves the repository is currently safe. Continue treating it as untrusted discovery data; never execute its workflows or scripts or pass it credentials.
