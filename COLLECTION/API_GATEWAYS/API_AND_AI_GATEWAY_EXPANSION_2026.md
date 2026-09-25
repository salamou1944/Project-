# API / AI Gateway Expansion — 2026-09-25

Status: DISCOVERY_CAPTURED

## Apache APISIX
- URL: https://github.com/apache/apisix
- Official site: https://apisix.apache.org/
- Capability: open-source API gateway plus AI gateway for API/microservice/LLM traffic.
- Observed: dynamic routing, load balancing, authentication, observability, 100+ plugins; Apache 2.0.
- AI gateway can proxy OpenAI-compatible and provider traffic including local Ollama.
- Verification required: current release, deployment topology, plugin security, AI-specific configuration and operational cost.

## Faucet
- URL: https://github.com/faucetdb/faucet
- Capability: single-binary SQL-to-REST API gateway with OpenAPI, RBAC and native MCP.
- Observed repository structure includes Docker, Go modules, tests/configuration artifacts.
- Important limitation: repository documentation says row-level security enforcement is planned rather than currently enforced.
- Potential value: rapid governed API/MCP surface for SQL-backed systems.
- Verification required: license, security model, database compatibility, current release and RLS behavior.

## STOA
- URL: https://github.com/stoa-platform/stoa
- Capability: self-hosted MCP/API gateway and control plane with OAuth/mTLS/RBAC/quotas/audit, developer portal and observability.
- Core platform: Apache 2.0 according to project documentation.
- Uses Keycloak, Prometheus/Grafana/Loki/OpenSearch and supports multiple upstream API gateways.
- Potential value: governed agent-to-API layer and API Factory infrastructure.
- Verification required: maturity, dependency burden, exact component licenses and production hardening.

## Ferro Labs AI Gateway
- URL: https://github.com/FerroLabs/ai-gateway
- Docs: https://docs.ferrolabs.ai/
- Capability observed: self-hosted Go AI gateway, OpenAI-compatible ingress, routing across many providers/models, safety/cost policies and observability.
- Current docs advertise v1.5.8 and 30 providers / 2,500+ models.
- Verification required: repository license, provider/model licensing, current source/release and feature boundaries.

## Eden
- URL: https://github.com/eden-dev-inc/eden
- Capability: open-source gateway/control-plane approach for data and AI workloads.
- Project announcement states Apache 2.0 open-sourcing in June 2026.
- Potential value: unified gateway between databases, model providers, agents, applications and infrastructure APIs.
- Verification required: repository state, deployment instructions, dependencies and current scope.

## Preloop
- URL: https://github.com/Preloop/Preloop
- Capability: self-hosted AI-agent control plane with MCP firewall, model gateway, budgets, human approvals, policy-as-code, observability and audit.
- Potential value: evidence/policy layer around autonomous agents.
- Verification required: license, sandbox/isolation, auth, policy enforcement and current source.

## Hecate
- URL: https://github.com/hecatehq/hecate
- Capability: local AI workspace/runtime with model gateway, agent tasks, approvals, sandbox policy, artifacts, retries/resumes, external coding-agent supervision and evidence trails.
- Potential value: operator-facing control/evidence patterns.
- Verification required: license, threat model, persistence and current maturity.

## Rule
Gateway discovery is not adoption. Record whether the core is actually open/self-hostable, whether provider calls remain metered, and whether security controls are enforced rather than merely exposed.
