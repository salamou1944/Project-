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

## Verification state
- VERIFIED_EVIDENCE_CAPTURED: Preloop, Agent Reach, Activepieces, Windmill, Hatchet (license), LiteLLM (license), Restic (security/design), Ollama (API).
- PARTIAL: Plakar.
- NOT_YET_VERIFIED: production security, dependency graphs, runtime benchmarks, failure-injection, restore drills, and exact enterprise/cloud feature parity.
