# AI Platform Stack Expansion — 2026-09-25

Status: DISCOVERY_CAPTURED

## Atlas
- URL: https://github.com/thekaveh/atlas
- Capability: self-hosted integrated GenAI/ML/data Docker Compose platform.
- Observed stack includes Ollama, LiteLLM, Supabase, n8n, Airflow, Spark, Weaviate, Neo4j, JupyterHub, Ray and ComfyUI behind Kong.
- Potential value: reference architecture for assembling local AI/data infrastructure from OSS components.
- Limitation: bundled stacks can have substantial resource and operational requirements.
- Verification required: source/release, licenses of every component, compose health, GPU requirements and security defaults.

## Off Grid AI / OGAC
- URL: https://github.com/off-grid-ai/OGAC
- Capability: self-hosted governed AI control plane with gateway, evals, guardrails, PII masking, data pipelines, audit, lineage and knowledge bases.
- Observed default stack includes Postgres, LanceDB, Auth.js and optional Keycloak/Qdrant/pgvector/OPA/LLM Guard integrations.
- Important distinction: source-available/open-source status and each dependency's license must be checked independently.
- Potential value: architecture reference for governed AI execution and evidence.

## SOAT
- URL: https://github.com/ttoss/soat
- Capability: self-hostable AI application infrastructure with IAM, file/document storage, vector search, memory, agent orchestration, DAG workflows, guardrails, human approvals, metering, versioned agents and MCP.
- Potential value: reusable platform substrate for AI/API products.
- Verification required: repository/license, database requirements, auth/security, deployment and current feature completeness.
