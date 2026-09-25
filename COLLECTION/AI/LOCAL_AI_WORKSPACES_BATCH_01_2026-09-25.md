# ALTERNATIVE SOURCE FAMILY — LOCAL AI WORKSPACES BATCH 01 — 2026-09-25

Rule: collect distinct sources even when they overlap in function. Do not collapse candidates merely because they perform the same job.

## 1. SOMI — Somi-Project/Somi
Source: https://github.com/Somi-Project/Somi
Branch: master
README SHA: 52ab8a7e821426f2ae61abefd26d73942e87a3a7
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository README:
- Fully self-hosted/local-first AI agent framework.
- Desktop PySide6 control surface.
- Local chat, persistent memory, coding workspace, research workspace.
- OCR and structured extraction.
- Local STT/TTS.
- Tool/skill registry, workflows, subagents.
- Browser automation and research stacks.
- Approval-aware execution, audit trails, node/gateway foundations.
- Release gate, freeze artifacts, replay harness and security audit tooling.
- Requires local Ollama for quick start; Python 3.11+ and Git.
- Repository README states no subscriptions/forced SaaS; this is a project claim and still requires dependency verification.
- License file was not resolved in the inspected repository path; do not infer license.

Collection value: distinct architecture emphasizing local desktop operator, evidence workflows, security controls and skill expansion.

## 2. OpenEnsemble — openensemble/openensemble
Source: https://github.com/openensemble/openensemble
Default branch: main
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository README:
- Self-hosted multi-user AI assistant platform.
- Specialist agents and coordinator delegation.
- Per-user isolation for agents, skills, sessions, files and settings.
- Providers include local Ollama/LM Studio plus numerous cloud providers.
- Bundled local reasoning and embedding models via node-llama-cpp.
- Deep research saved as persistent research documents.
- Gmail/Exchange/IMAP email integration.
- Calendar, expenses, documents, code projects.
- Background recurring/one-shot tasks.
- MCP, remote nodes and voice-device support.
- Open-hardware ESP32-S3 voice satellite repository.
- Built-in skill builder.
- Node.js server architecture.
- Important: cloud provider options remain external costs; local model path can reduce these but hardware is still required.

Collection value: distinct multi-user/team + voice-satellite + specialist-agent architecture, not collapsed into Odysseus.

## 3. Oceano — Hugofsco/oceano
Source: https://github.com/Hugofsco/oceano
Default branch: main
README SHA: b8597f09445f18b8aab685ba8e2f8bdda0eeae78
LICENSE SHA: 1a9a11514945c08db16870ad3e6ac288d5945fd1
License: MIT
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository evidence:
- Self-hosted local-first AI agent with workspace, browser control, memory and tools.
- 100+ built-in tools/MCP including filesystem, shell, Python, git/ripgrep/tests, media, web search, headless browser, HTTP/REST/RSS, DuckDB analysis, RAG, scheduling, workflows, calendar, Kanban/notebook, SSH keychain, IMAP/SMTP email and desktop actions.
- Multiple sub-agents/background jobs and delegation.
- SearXNG integration.
- Local model serving/inference path with llama-swap and Hugging Face model catalog.
- Configurable tool loading budgets and discovery.
- Typed tool outcomes, verification evidence, operation IDs and idempotent replay protections.
- Durable content-free recovery checkpoints.
- SSRF protections and workspace confinement; systemd hardening documented.
- Default web UI bind is 0.0.0.0, with login/TOTP recommended; trusted-network-only posture is explicitly stated.
- MIT license confirmed.
- Cloud/provider integrations exist but local-first path is available.

Collection value: distinct focus on tool-budgeting, recovery checkpoints, idempotency, browser safety and resident Claude/Codex bridges.

## Cross-source note
These three are intentionally retained as separate candidates despite overlap with Odysseus. Functional overlap is useful because architecture, license, local-runtime assumptions, security controls and operational tradeoffs differ.

## Next
Deep-verify dependencies, licenses where missing, release provenance, deployment path, external-cost boundaries, security model and tests before any VERIFIED classification.
