# US GITHUB TECHNICAL FRONTIER — ACCOUNT CAPTURE
Date: 2026-10-08
Scope: United States GitHub account/organization frontier — all technical domains, account-wide.

## Operating rule
ACCOUNT TARGET → ALL PUBLIC REPOSITORIES → ALL RELEVANT CONTENT/SOURCES → NEW ACCOUNTS → REPEAT.

This is preservation/triage, not installation or runtime proof. Discovery ≠ extraction ≠ integration ≠ production readiness.

## Initial high-value account set

| Account | GitHub owner | Status in Collection | Primary frontier |
|---|---|---|---|
| Microsoft | microsoft | NEW | developer tools, runtimes, AI, security, cloud |
| Google | google | NEW | ML, infra, languages, data, security, developer tooling |
| Meta | facebook | NEW | AI/ML, mobile, web, infra, databases |
| OpenAI | openai | NEW | agents, coding agents, SDKs, MCP, security, APIs |
| Cloudflare | cloudflare | NEW | edge, serverless, networking, security, browser/runtime |
| Vercel | vercel | NEW | web, AI SDK, agents, workflows, deployment |
| NVIDIA | nvidia | EXISTING ACCOUNT EVIDENCE | GPU/AI infra, inference, CUDA ecosystem |
| AWS | aws | NEW | cloud primitives, SDKs, infra, containers, data |
| Uber | uber | EXISTING ACCOUNT EVIDENCE | geospatial, infra, registries, mobile, AI/security |
| Stripe | stripe | NEW | payments, billing, SDKs, financial infrastructure |
| Databricks | databricks | NEW | data engineering, ML, lakehouse, AI |
| PyTorch | pytorch | NEW | ML framework, training/inference, distributed AI |
| Hugging Face | huggingface | NEW | models, transformers, datasets, inference, robotics |
| HashiCorp | hashicorp | NEW | IaC, secrets, service networking, cloud automation |
| Elastic | elastic | NEW | search, observability, security, data |
| Docker | docker | NEW | containers, images, build/runtime tooling |
| Palantir | palantir | NEW | data/integration/agentic enterprise tooling |
| Coinbase | coinbase | NEW | fintech, crypto infrastructure, APIs |
| Supabase | supabase | NEW | Postgres, auth, storage, realtime, developer platform |
| GitHub | github | NEW | developer platform, Actions, security, Copilot/agent infrastructure |

## P0 repository triage targets

### Microsoft
- vscode
- TypeScript
- PowerToys
- terminal
- semantic-kernel
- AutoGen
- markitdown
- Playwright
- ONNX Runtime
- Dapr

### Google
- tensorflow
- jax
- googletest
- zx
- guava
- grpc
- gemma.cpp
- mediapipe
- diffusers-related Google projects
- cloud developer tooling

### Meta
- react
- react-native
- pytorch ecosystem contributions
- llama / Llama tooling
- docusaurus
- folly
- velox
- faiss
- avocado / infra projects where maintained

### OpenAI
- codex
- openai-agents-python
- openai-agents-js
- codex-security
- mcp-extensions
- openai-python
- openai-node
- openai-openapi
- cookbook

### Cloudflare
- workers-sdk
- workerd
- pingora
- cloudflared
- vinext
- durable-objects / edge-runtime projects
- security/agent skills and related tooling

### Vercel
- ai
- eve
- workflow
- next.js
- turborepo
- storage
- related AI SDK/provider packages

### NVIDIA
- TensorRT
- CUDA-related open components
- Triton
- NeMo
- TensorRT-LLM
- NIM/open inference tooling where public
- GPU benchmarking/agent skills

### AWS
- aws-sdk-* families
- aws-cdk
- boto3
- aws-lambda runtimes/tools
- sagemaker tooling
- container/serverless tooling
- Bedrock-related open-source integrations

### Uber
- h3 / h3-go
- RIBs
- kraken
- ADR
- NullAway
- submitqueue
- baseweb
- Michelangelo/ML infrastructure where public

### Stripe
- stripe-node
- stripe-python
- stripe-go
- stripe-java
- stripe-php
- stripe-ruby
- stripe-ios
- stripe-android
- stripe-mock
- payment/testing/integration tooling

### Databricks
- databricks-labs
- koalas
- delta / Delta Lake ecosystem
- ML/data engineering tooling
- Spark integrations and utilities

### PyTorch
- pytorch
- torchtitan
- torchao
- torchrec
- torcharrow
- distributed/training/inference tooling
- current non-archived projects only

### Hugging Face
- transformers
- diffusers
- datasets
- accelerate
- evaluate
- tokenizers
- safetensors
- lerobot
- inference/tooling ecosystem

### HashiCorp
- terraform
- vault
- consul
- nomad
- boundary
- waypoint
- packer
- go-plugin

### Elastic
- elasticsearch
- kibana
- beats
- logstash
- apm-server
- elastic-agent
- security/observability tooling

### Docker
- moby
- compose
- buildx
- buildkit
- cli
- containerd-related public work
- scout/desktop ecosystem where public

### Palantir
- public developer/data/agent projects only
- strict license and provenance review before any extraction

### Coinbase
- cloud APIs/SDKs
- commerce/payment tooling
- developer infrastructure
- blockchain/data tooling
- security tooling

### Supabase
- supabase
- postgres-related extensions
- auth
- storage
- realtime
- edge-runtime
- CLI and local development tooling

### GitHub
- actions/runner
- cli
- codeql
- semantic
- github-ospo
- agent/copilot-adjacent public tooling
- developer/security automation

## Red-line dedupe
Before extraction, compare every candidate against:
- COLLECTION existing sources/capability groups
- agent-skills canonical Skills
- Salamou-31 / SOAT
- EASY
- Elite / ARMY-14
- existing infrastructure already installed or proven

If the capability already exists: DO NOT reimplement it.
Only extract a proven-gap improvement, adapter, contract, test, implementation pattern, or missing integration.

## Readiness
All entries above start as PRESERVED/ON_SHELF candidates unless a separate evidence record proves a stronger state.
No installation, integration, runtime, human-ready, or production claim is made by this capture alone.

## Evidence anchors
- Microsoft GitHub organization: https://github.com/microsoft
- Google GitHub organization: https://github.com/google
- OpenAI GitHub organization: https://github.com/openai
- Cloudflare GitHub organization: https://github.com/cloudflare
- Vercel GitHub organization: https://github.com/vercel
- Uber GitHub organization: https://github.com/uber
- Stripe GitHub organization: https://github.com/stripe
- PyTorch GitHub organization: https://github.com/pytorch

## Next pass
1. Enumerate ALL public repositories for each account; 100-result pages are bounded, not exhaustive.
2. Continue pagination until exhausted.
3. Inspect repository families across all domains, not AI-only.
4. Expand newly discovered organizations/owners.
5. Preserve exact revision, license, dependencies, setup path and limitations.
6. Deep-extract only after account-wide enumeration and semantic dedupe.
