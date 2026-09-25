# COLLECTION — Research Index

Status: INCREMENTAL_COLLECTION
Updated: 2026-09-25

## Purpose
Central collection of repositories, documentation, tools, and reusable implementation knowledge discovered during research. Priority: free/open-source/self-hosted capabilities that can reduce paid SaaS/API dependencies.

## Current research batch

### Web access / research
- Agent Reach — https://github.com/Panniantong/Agent-Reach
  - One-command setup for agent web/social access.
  - Routes through upstream tools such as Jina Reader, yt-dlp, GitHub CLI and platform-specific CLIs.
  - Research value: reusable access layer; no mandatory paid API keys for the listed backends.
  - Verification source: docs/README_en.md, inspected 2026-09-25.
- SearXNG — https://github.com/searxng/searxng
  - Self-hosted metasearch engine.
  - Useful as an independent search layer and fallback.
  - Verification source: official documentation, inspected 2026-09-25.
- Jina Reader — https://github.com/jina-ai/reader
  - URL-to-LLM-friendly content and web search capability.
  - Candidate fallback for URL reading/search where its current public service remains usable.

### Crawling / extraction
- Firecrawl — https://github.com/firecrawl/firecrawl
  - Open-source web scraping/crawling/extraction stack.
  - Self-hosting uses Docker Compose and includes API/workers/browser/queue/database components.
  - License: primarily AGPL-3.0; component licenses must be checked before reuse.
  - Production self-hosting requires security, persistence, backup and scaling work.
- Crawl4AI — https://github.com/unclecode/crawl4ai
  - Self-hosted crawling/data extraction.
  - Current self-hosting docs explicitly emphasize no per-request pricing and infrastructure ownership.
  - Security defaults changed in 0.9.0; pin/check revision before deployment.
- Scrapy — https://github.com/scrapy/scrapy
  - Mature Python crawling/extraction framework.
  - BSD-3-Clause.
  - Strong candidate for deterministic crawlers and structured extraction without SaaS metered requests.

### Browser automation
- Playwright — https://github.com/microsoft/playwright
  - Open-source browser automation for Chromium, Firefox and WebKit.
  - Playwright MCP exists for AI-agent browser control.
  - Apache-2.0.
- Browser Use — https://github.com/browser-use/browser-use
  - Open-source AI browser agent that can run locally with selectable LLMs.
  - Local browser path does not require Browser Use Cloud; cloud features are separate.
  - Open-weight browser model is documented for self-hosting.
  - Must distinguish local/open-source capability from paid cloud features.

### Documents / files
- Docling — https://github.com/docling-project/docling
  - Local document conversion and structured understanding.
  - Supports PDF, DOCX, PPTX, XLSX, HTML, images, audio/video and more.
  - Exports Markdown/JSON and supports RAG-oriented chunking.
  - MIT codebase.
- OCRmyPDF — https://github.com/ocrmypdf/OCRmyPDF
  - Local OCR for scanned PDFs, searchable PDF/A, multilingual Tesseract support.
  - MPL-2.0.
  - Useful for building a local document ingestion pipeline.

### AI memory / retrieval
- Qdrant — https://github.com/qdrant/qdrant
  - Open-source vector database/search engine.
  - Can run locally with Docker.
  - Candidate for local semantic index of the collection.

### Image / creative
- rembg — https://github.com/danielgatis/rembg
  - Local background removal via CLI/library/server/Docker.
  - Candidate for EASY Creative Engine; do not add to closure scope until an actual gap is proven.
- Upscayl — https://github.com/upscayl/upscayl
  - Free/open-source AI image upscaler.
  - Desktop/local processing; Vulkan-capable GPU required for the main workflow.
  - Candidate for EASY Creative Engine only when a real gap is demonstrated.

### Audio / video
- whisper.cpp — https://github.com/ggml-org/whisper.cpp
  - Local Whisper ASR implementation with CPU/GPU support.
  - Candidate for local transcription/subtitle/audio workflows.
- FFmpeg — https://github.com/FFmpeg/FFmpeg
  - Core multimedia processing stack for audio/video/subtitles/metadata.
  - Useful as foundational local media infrastructure.

## New 2026-09-25 discovery captures

### Self-hosted SaaS replacements
- COLLECTION/SELF_HOSTED/SAAS_REPLACEMENTS_INDEX.md
- Discovery sources include:
  - https://github.com/SolvoHQ/awesome-self-host-saas-alternatives
  - https://github.com/open-saas-directory/awesome-saas-directory
- Newly surfaced replacement families include Gitea/Forgejo/GitLab CE, Bruno/Hoppscotch, Umami/Plausible, Coolify/Dokku/CapRover, n8n/Activepieces/Huginn, Continue/Tabby/Aider, Ollama/vLLM/LiteLLM, and Headscale/NetBird.
- These are discovery candidates; license and current feature parity require per-project verification.

### Local AI runtime and agent expansion
- COLLECTION/AI/LOCAL_AI_RUNTIME_AND_AGENTS_2026.md
- New candidates:
  - LocalAI — multimodal local AI engine.
  - SOMI — local-first AI workstation/agent framework.
  - LibrAgent — local agent workspace with tools/MCP/browser.
  - Pan-Agent — self-hosted desktop/PC-control agent.
  - Pernix — self-hosted agent server; explicitly not production software.
- Discovery source: https://github.com/Supersynergy/awesome-local-ai-agents

### Browser automation expansion
- COLLECTION/WEB_RESEARCH/BROWSER_AUTOMATION_EXPANSION_2026.md
- New candidates:
  - Writ — self-hosted record/replay browser workflows, REST/MCP, OCR and monitoring.
  - WebOperator — local Chrome agent/MCP with existing browser sessions.
  - WebNav — local AI browser extension.
  - AgentBrowser — REST/WebSocket browser control with dashboard and vision-oriented extraction.
- These require security/session/isolation/license verification before reuse.

## Collection rules
1. Do not treat a discovery as production-ready without verification.
2. Preserve source URL, revision/version where relevant, license, setup method, and limitations.
3. Prefer local/self-hosted/free paths before paid APIs.
4. Separate "free/open-source" from "free cloud tier".
5. Do not copy credentials, secrets, private user data, or unrelated sensitive material.
6. Do not mark an item COMPLETE until the actual repository/file set has been recursively inspected and verified when file collection is requested.

## Next collection frontier
Continue repository/document research broadly, with special priority:
- Agent Reach upstream channel implementations and dependency tree.
- Firecrawl self-hosting/dependency architecture.
- Search/retrieval stack: SearXNG + Jina + local indexes.
- Browser automation and authenticated-session security.
- Document ingestion/OCR and local multimodal processing.
- Local AI inference and multimodal runtimes.
- Self-hosted SaaS replacements and recurring developer-tool bills.
- Automation/orchestration, API gateways, databases, security, evals/observability and coding-agent ecosystems.
- Continue following references from high-value discovery indexes rather than stopping at their first page.

## AI capture added 2026-09-25
The first AI source-preservation batch is stored before deep verification:
- COLLECTION/AI/AI_INDEX.md — agent frameworks, runtimes, memory/RAG, local inference, AI applications, evals/safety.
- COLLECTION/SOURCES/AI_DISCOVERY_SOURCES.md — preserved discovery sources and research rules.
- 50+ named AI repositories/entry points were captured for subsequent recursive inspection.
- These entries are DISCOVERY_CAPTURED, not automatically VERIFIED.

## Web research capture added 2026-09-25
- COLLECTION/WEB_RESEARCH/AGENT_REACH_CAPTURE.md — Agent Reach documentation tree, installation/safety/diagnostic patterns and reusable routing concepts.
- COLLECTION/WEB_RESEARCH/BROWSER_AUTOMATION_INDEX.md — Playwright, Browser Use, Open Browser, OpenBrowser broker, Browserable and AgentBrowser discovery candidates.
- COLLECTION/DOCUMENTS/DOCUMENT_OCR_INDEX.md — OCRmyPDF, Docling and Tesseract document/OCR candidates.
- COLLECTION/SELF_HOSTED/SAAS_REPLACEMENTS_INDEX.md — recurring SaaS replacement discovery.
- COLLECTION/AI/LOCAL_AI_RUNTIME_AND_AGENTS_2026.md — local multimodal AI/runtime expansion.
- COLLECTION/WEB_RESEARCH/BROWSER_AUTOMATION_EXPANSION_2026.md — additional local browser-agent candidates.
- These additions are DISCOVERY_CAPTURED unless an entry was explicitly supported by inspected repository documentation; discovery is not an adoption decision.


## Paid-service elimination expansion — 2026-09-25
A broad paid-SaaS replacement sweep was captured into dedicated indexes:
- COLLECTION/SELF_HOSTED/PAID_SAAS_REPLACEMENT_MAP_2026.md
- COLLECTION/OBSERVABILITY_CONTROL/APM_AND_MONITORING_EXPANSION_2026.md
- COLLECTION/COMMUNICATION/COMMUNICATION_AND_COLLABORATION_EXPANSION_2026.md
- COLLECTION/CRM_SUPPORT/CRM_SUPPORT_MARKETING_EXPANSION_2026.md
- COLLECTION/DEVTOOLS/DEVELOPER_SAAS_REPLACEMENTS_EXPANSION_2026.md

Discovery sources used for this sweep:
- https://github.com/SolvoHQ/awesome-self-host-saas-alternatives
- https://github.com/open-saas-directory/awesome-saas-directory
- https://selfhosttools.com/
- https://ideaproof.io/open-source/self-hosted
- https://github.com/spinov001-art/free-developer-tools-2026

Current scope now includes project management, CRM/support, marketing/email, analytics/APM, collaboration, API clients, git/forge, CI/CD/PaaS, remote development, secrets/identity, storage, security and networking. All newly captured entries remain DISCOVERY_CAPTURED until individually verified.


## Deep verification added — 2026-09-25
Repository-level evidence has now been persisted under COLLECTION/VERIFICATION/:
- COLLECTION/VERIFICATION/DEEP_VERIFICATION_BATCH_2026-09-25.md
- COLLECTION/VERIFICATION/VERIFICATION_QUEUE_NEXT.md
Verified/partially verified evidence currently covers Preloop, Agent Reach, Activepieces, Windmill, Hatchet, LiteLLM, Restic, Plakar and Ollama. The files explicitly distinguish repository evidence from production/runtime validation and record paid/cloud/external-cost boundaries.
