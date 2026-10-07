# the-open-agent — Account Capture — 2026-10-07

Status: ACCOUNT_CAPTURED / SELECTED HIGH-VALUE SOURCES

## Owner
- https://github.com/the-open-agent
- Public repositories enumerated: 11

## Repositories
1. openagent
2. openagent-website
3. oss-skills
4. agentbench
5. dashscope-go-sdk
6. office-tool-use
7. openagent-miniprogram
8. openagent-chrome
9. data
10. static
11. openagent-helm

## Primary sources inspected
### openagent
- Apache-2.0.
- Single-binary/self-hostable AI assistant with model-provider switching, RAG, autonomous agent loops, browser-use, web search/fetch, shell, Office automation and MCP.
- Workflow automation: visual multi-step pipelines, conditional/parallel execution, schedules, usage analytics.
- Multi-tenancy, audit logs, REST API/Swagger, file/media management and request/tool logs.
- Discovery evidence only; runtime claims require independent validation.

### oss-skills
- Apache-2.0.
- 18 progressive-disclosure Agent Skills focused specifically on open-source maintenance.
- Strong patterns: decision tables, explicit anti-patterns, trigger-based loading, strict skill validation, release engineering, supply-chain security, API design, CI, benchmarking, contributor experience and sustainability.
- Semantic overlap with agent-skills is high; preserve as a source for targeted upgrades rather than duplicate skills.

### agentbench
- Apache-2.0.
- Lightweight benchmark framework using Python standard library plus optional PyYAML.
- Eight suites: performance, dialogue, long-horizon, tool invocation, startup, memory, throughput and reliability.
- Reproducible runs with report.md, summary.json, details.jsonl and 95% bootstrap confidence intervals.
- Optional server-log verification for tool invocation.
- Strong candidate for upgrading existing evaluation/SOAT benchmark contracts.

### office-tool-use
- Apache-2.0.
- Standalone Go library for bounded OOXML/PPTX package handling.
- Analyze -> scaffold -> check -> fill pipeline with bounded OPC/ZIP access, atomic writes and support for text/tables/images/charts/notes/transitions/SmartArt.
- Strong reusable asset for document/presentation automation.

## Semantic comparison
- openagent: broad overlap with existing local AI workspace/agent-runtime collection; no wholesale adoption.
- oss-skills: upgrade existing agent-skills only where concrete decision tables or maintainer workflows are missing.
- agentbench: likely merge/upgrade candidate for evaluation confidence intervals, repeated-run reliability and load suites.
- office-tool-use: concrete reusable library candidate for Salamou-31 document/presentation services.

## License / cost
All selected sources above are Apache-2.0 according to repository README/license badges inspected.

## Boundary
Discovery is not production proof. Preserve source revisions and inspect implementation/tests before integrating.
