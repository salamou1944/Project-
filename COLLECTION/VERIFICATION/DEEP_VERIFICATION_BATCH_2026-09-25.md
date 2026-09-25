# Deep Verification Batch — 2026-09-25

Status: VERIFIED_EVIDENCE_CAPTURED (repository-level evidence; not production deployment validation)

## Preloop
- Upstream: https://github.com/Preloop/Preloop
- License: Apache-2.0 for the OSS repository.
- Self-hosting: Docker Compose and Helm are documented supported install surfaces; self-hosted data can remain on the operator's machine.
- Core capabilities evidenced in README: MCP firewall; OpenAI/Anthropic/Gemini-compatible model gateway; budgets; model allowlists; token accounting; policy-as-code with YAML+CEL; human approvals; runtime session observability; audited session search; event-driven flows.
- Security/evidence boundary: production self-host requires SECRET_KEY; telemetry is enabled by default but can be disabled with PRELOOP_DISABLE_TELEMETRY=true.
- Paid boundary: OSS is one operator/account. Multi-user RBAC, team/user budgets, multi-approver/quorum/escalations are Cloud/Enterprise.
- Project fit: very high for Elite/ARMY-14 evidence gates, agent control, approvals, audit and cost attribution.
- Verification limit: repository evidence confirms advertised architecture/licensing/install surfaces, not that every policy path has been independently attacked.

## Agent Reach
- Upstream: https://github.com/Panniantong/Agent-Reach
- Default agent-reach install --env=auto is read-only; system changes require --system after explicit approval.
- It acts as selector/installer/health checker/router around upstream tools.
- Documented upstream tools include OpenCLI, twitter-cli, bili-cli, rdt-cli, yt-dlp, mcporter and gh CLI.
- agent-reach doctor is the health evidence surface; watch supports scheduled health/update checks.
- Project fit: high for persistent research intake and web-research capability routing.
- Boundary: channel access can still require credentials, cookies, proxies or external services.

## Activepieces
- Upstream: https://github.com/activepieces/activepieces
- Community Edition: MIT; enterprise features are separately commercially licensed.
- README documents versioned flows, branching, retries, HTTP/code steps and 200+ integrations/pieces.
- Project fit: candidate for replacing hosted workflow automation.
- Verification limit: exact CE/enterprise boundary and runtime profile require deeper inspection.

## Windmill
- Upstream: https://github.com/windmill-labs/windmill
- Backend/frontend are AGPLv3 except enterprise snippets; clients/OpenAPI are Apache-2.0.
- Source-build without enterprise is described as AGPLv3.
- README documents scripts/flows, schedules, webhooks, HTTP routes, Kafka, WebSockets and email triggers, plus Docker Compose and Kubernetes.
- Project fit: strong durable workflow/job-execution candidate.
- Critical license boundary: Community Edition binaries/images include proprietary/non-public code; do not equate them with a pure open-source artifact.

## Hatchet
- Upstream: https://github.com/hatchet-dev/hatchet
- License: MIT.
- Candidate role: durable execution/workflow orchestration for long-running agent/research/deployment jobs.
- Verification limit: this batch captured license evidence only; persistence, retries, idempotency, queue behavior and recovery still require inspection.

## LiteLLM
- Upstream: https://github.com/BerriAI/litellm
- Content outside enterprise is MIT; enterprise has separate licensing.
- Candidate role: OpenAI-compatible gateway/provider normalization and routing.
- Boundary: a gateway does not eliminate paid model/provider costs; local runtimes can change that boundary.

## Restic
- Upstream: https://github.com/restic/restic
- Repository content is encrypted/authenticated; design documents AES-256-CTR and Poly1305-AES.
- Restic explicitly emphasizes verifiability and restore capability.
- Threat-model evidence states restic does not by itself prevent an attacker with storage access from deleting backups; stronger deletion resistance needs storage/append-only controls.
- Project fit: high for Project-/EASY/Elite evidence-store backup and disaster recovery.
- Operational rule: a backup job is not evidence of recoverability; schedule verification and restore tests.

## Plakar
- Upstream: https://github.com/PlakarKorp/plakar
- README describes an open-source backup engine with encrypted, deduplicated, verifiable snapshots and restore; integrations include databases, Kubernetes workloads and object stores.
- Project fit: promising alternative/complement to restic.
- Verification limit: license was not independently captured in this batch.

## Ollama
- Upstream: https://github.com/ollama/ollama
- Local API defaults to http://localhost:11434/api.
- API includes generation/chat, model management, embeddings, running-models and version endpoints.
- Project fit: direct local-model runtime for subscription-reduction paths.
- Boundary: local runtime removes provider API dependency only when a suitable local model/hardware path exists; model licensing and compute costs remain separate.

## Hatchet — deeper repository verification
- Upstream: https://github.com/hatchet-dev/hatchet
- Repository evidence confirms durable task/queue primitives in the codebase, including durable queues/listeners and durable task factories.
- Repository evidence contains an explicit idempotency repository and idempotency-key implementation; documentation describes using idempotency to prevent duplicate task runs from duplicate webhook/event sends.
- Project fit: strong candidate for long-running Elite/ARMY-14/research/deployment execution where retries, duplicate-event protection and durable state matter.
- Verification limit: this remains repository-level evidence; no production failure-injection or recovery drill has been executed against our systems.

## Coolify — self-hosted deployment boundary
- Upstream: https://github.com/coollabsio/coolify
- Repository evidence exposes a self-hosted operating path and Docker-based self-hosted upgrade checks.
- Project fit: infrastructure-cost-reduction candidate for workloads that can move from hosted deployment to operator-controlled infrastructure.
- Boundary: using Coolify would not remove the underlying VPS/server/network/storage cost and is not a drop-in replacement for Railway-specific managed infrastructure.
- Verification limit: no migration or production deployment has been performed; no claim of Railway feature parity.

## LiteLLM — deeper gateway evidence
- Upstream: https://github.com/BerriAI/litellm
- Repository evidence confirms MIT licensing for the OSS project components and a proxy/gateway architecture.
- README evidence confirms a unified OpenAI-format interface across many model providers and self-hosted proxy deployment.
- Project fit: strong candidate for Salamou-31 provider normalization and controlled routing, especially where the application already uses OpenAI-compatible interfaces.
- Boundary: LiteLLM normalizes/routs providers; it does not make paid model inference free. Local runtimes such as Ollama are a separate cost-reduction layer.
- Verification limit: no production gateway migration or load test has been executed in our projects.

## Agent Reach — current source evidence refresh
- Upstream: https://github.com/Panniantong/Agent-Reach
- Current README evidence states local cookies are retained locally and the project provides a health/diagnostic path plus primary/fallback routing for supported channels.
- Project fit: useful for research intake and source-routing, but each channel remains subject to its own authentication, anti-bot and external-service boundary.

## Ollama — current source evidence refresh
- Upstream: https://github.com/ollama/ollama
- Current repository API specification identifies MIT licensing for the HTTP API specification and the repository documents a local REST endpoint at localhost:11434.
- Repository README documents integration paths for Codex and other coding agents plus local model execution.
- Project fit: direct local inference option for development/research and for reducing dependence on paid API inference when hardware/model quality is sufficient.
- Boundary: local inference has compute, hardware and model-license constraints and is not a universal replacement for hosted frontier models.

## Verification state update
- VERIFIED_EVIDENCE_CAPTURED now includes deeper repository evidence for Hatchet durability/idempotency, Coolify self-hosting, LiteLLM gateway/OSS boundary, Agent Reach local/health-routing behavior, and Ollama local API/Codex integration.
- Still NOT production-verified: migration safety, runtime benchmarks, failure injection, recovery drills, and end-to-end integration inside our projects.

## Verification state
- VERIFIED_EVIDENCE_CAPTURED: Preloop, Agent Reach, Activepieces, Windmill, Hatchet (license), LiteLLM (license), Restic (security/design), Ollama (API).
- PARTIAL: Plakar.
- NOT_YET_VERIFIED: production security, dependency graphs, runtime benchmarks, failure-injection, restore drills, and exact enterprise/cloud feature parity.
