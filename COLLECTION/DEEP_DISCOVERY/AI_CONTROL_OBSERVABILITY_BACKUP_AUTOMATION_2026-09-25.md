# DEEP-DISCOVERY BATCH — AI CONTROL, OBSERVABILITY, BACKUP & AUTOMATION — 2026-09-25

## Newly surfaced high-value candidates

### AI governance / control
- https://github.com/Preloop/Preloop — self-hostable AI-agent control plane with MCP firewall, model gateway, budgets, approvals, policy and audit. Discovery source currently describes these capabilities; verify enforcement, license, deployment and persistence before reuse.
- https://github.com/relayroom/relayroom — self-hosted coordination/observability hub for coding agents; MCP messaging, Postgres-backed events, worktree coordination and wake-budget controls. Verify telemetry, permissions and license.
- https://github.com/superloglabs/superlog — Apache-2.0 community observability stack with OTLP, Postgres/ClickHouse and local agent runner. Verify open-source scope versus hosted/paid features and security model.
- OpenObserve — investigate as an object-storage-oriented observability candidate, especially where predictable storage costs matter; verify current OSS/enterprise boundaries before adoption.
- Coroot — investigate for self-hosted infrastructure observability and MCP/agentic capabilities; verify community versus enterprise boundaries.

### Workflow / scheduling
- Dagu — YAML workflow orchestration with a lightweight/no-database operating model; verify current repository/license and suitability for durable production workflows.
- Healthchecks — scheduled-job/cron failure alerting candidate; useful as a narrow reliability primitive rather than a full workflow engine.
- Dyrector — container deployment/control candidate; verify license and current scope.
- Bacalhau — compute-over-data candidate for distributed data processing; verify complexity and actual fit.
- 1Panel — server management panel candidate; verify security posture and licensing before exposing to the Internet.

### Backup / recovery
- Plakar — encrypted/queryable backup candidate; verify repository license, restore semantics and supported storage backends.
- Pluton — encrypted self-hosted backup candidate with many storage options; verify maturity, restore testing and licensing.
- Existing Restic/Kopia/Borg/Borgmatic/Syncthing/rclone remain the baseline comparison set.

### AI discovery / local stack
- AnythingLLM — self-hostable AI/RAG/agent platform.
- Khoj — self-hosted AI second-brain/research/automation candidate.
- Langflow — visual AI workflow/agent builder.
- Dify — self-hosted AI application platform.
- LibreChat — self-hosted multi-provider AI interface.
- Flowise — self-hosted visual LLM application builder.
- Langfuse — self-hosted LLM observability.
- Arize Phoenix — AI observability/evaluation candidate.
- Helicone — self-hosted LLM observability candidate.

## Verification priority
1. Preloop: check whether policy enforcement is real at the MCP/model boundary.
2. Superlog/OpenObserve/SigNoz: compare actual self-hosted features, licenses and storage costs.
3. Dagu/Healthchecks/Hatchet/Temporal: compare durable execution versus lightweight scheduled jobs.
4. Plakar/Pluton/Restic/Kopia/Borg: compare restore verification and object-storage support.
5. Khoj/AnythingLLM/Dify/Langflow/LibreChat: compare local-model support and external API dependence.

## Evidence boundary
Current web discovery confirms the existence and advertised scope of these projects, but repository-level production suitability has not been established merely from directory or README claims. Self-hosting can eliminate software subscriptions while leaving hosting, network, model, email, SMS and other external operating costs.
