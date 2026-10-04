# PLATFORM REUSE SWEEP — 2026-10-04

## Decision
Repository-first sweep completed against known full-platform candidates. The strongest reusable base found is **ttoss/soat** for an AI/API execution substrate; **thekaveh/atlas** is the strongest broad self-hosted infrastructure stack; **off-grid-ai/OGAC** is technically strong but its source-available license imposes a 25-user community limit and commercial restrictions, so it is not the default commercial base.

## Verified evidence

### ttoss/soat
- Repository: ttoss/soat
- Default branch: main
- README revision: db9f9a893144e958d778fdcab17be4c31f24ac84
- License: Apache 2.0
- Self-hostable Node.js server backed by PostgreSQL.
- Includes IAM, files/documents, vector search, memory, agents, DAG orchestrations, RAG, guardrails, human approvals, quotas/metering, versioned agents/canary rollout, evaluations, MCP/OAuth, REST, CLI, TypeScript SDK and web console.
- Docker Compose is the documented fastest path.
- Commercial reuse is license-compatible at the source level; third-party dependencies still require their own review.
- Classification: **REUSE CANDIDATE — highest priority**.

### thekaveh/atlas
- Repository: thekaveh/atlas
- Default branch: main
- License: Apache 2.0
- One Docker Compose stack integrating 30+ services.
- Includes Kong, Supabase, Redis, LiteLLM, local LLM engines, vector/graph stores, Crawl4AI, Docling, SearXNG, n8n, Airflow, OpenClaw, MCP servers, Open WebUI, research tooling, observability and backend API.
- Classification: **INFRASTRUCTURE REUSE CANDIDATE — strong for a broad local/self-hosted lab, heavier operational footprint**.

### off-grid-ai/OGAC
- Repository: off-grid-ai/OGAC
- Default branch: main
- Source-available, not ordinary permissive OSS.
- README documents a working Docker/Node 22 stack with gateway, pipelines, evals, guardrails, PII masking, audit, lineage, knowledge bases, governed apps/agents and human approvals.
- License verified from LICENSE: free community use only up to 25 users across a rolling 30-day period; without a separate commercial license, no charging for access, unrelated third-party hosting, proprietary embedding/redistribution, or white-labeling.
- Classification: **TECHNICAL REFERENCE / POSSIBLE INTERNAL USE ONLY unless commercial license is obtained**.

## Account expansion
The owner accounts were expanded rather than treating the discovered repository as an isolated source:
- ttoss: multiple public repositories inspected; soat is the relevant full platform.
- off-grid-ai: OGAM, OGAD, OGAC and other account repositories identified; OGAD is an on-device local AI runtime/studio and OGAM is mobile/on-device AI, while OGAC is the governed enterprise console.
- thekaveh: atlas is the relevant integrated platform.

## Next reuse path
1. Use SOAT as the first candidate substrate for the existing AI/API/Elite execution layer.
2. Use Atlas selectively for infrastructure components rather than adopting its entire 30+ service footprint by default.
3. Keep OGAC as a reference unless licensing is separately cleared.
4. Do not create a new AI-agent platform from scratch until SOAT is tested against the existing AI/API-HUB, MONY, EASY and Elite requirements.

## Evidence boundary
This is repository-level verification, not a claim that any candidate is already deployed or production-ready in our environment. Runtime installation/smoke testing is the next verification gate.
