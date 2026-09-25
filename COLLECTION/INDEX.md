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

## Collection rules
1. Do not treat a discovery as production-ready without verification.
2. Preserve source URL, revision/version where relevant, license, setup method, and limitations.
3. Prefer local/self-hosted/free paths before paid APIs.
4. Separate "free/open-source" from "free cloud tier".
5. Do not copy credentials, secrets, private user data, or unrelated sensitive material.
6. Do not mark an item COMPLETE until the actual repository/file set has been recursively inspected and verified when file collection is requested.

## Next collection frontier
Continue repository/document research broadly, with special priority:
- Agent Reach docs and upstream channel implementations.
- Firecrawl self-hosting and dependency architecture.
- Search/retrieval stack: SearXNG + Jina + local indexes.
- Browser automation: Playwright + Browser Use.
- Document ingestion: Docling + OCRmyPDF.
- Creative/media: rembg + Upscayl + whisper.cpp + FFmpeg.
- Free/self-hosted replacements for recurring paid developer SaaS.


## AI capture added 2026-09-25
The first AI source-preservation batch is now stored before deep verification:
- COLLECTION/AI/AI_INDEX.md — agent frameworks, runtimes, memory/RAG, local inference, AI applications, evals/safety.
- COLLECTION/SOURCES/AI_DISCOVERY_SOURCES.md — preserved discovery sources and research rules.
- 50+ named AI repositories/entry points were captured for subsequent recursive inspection.
- These entries are DISCOVERY_CAPTURED, not automatically VERIFIED.


## Web research capture added 2026-09-25
- COLLECTION/WEB_RESEARCH/AGENT_REACH_CAPTURE.md — Agent Reach documentation tree, installation/safety/diagnostic patterns and reusable routing concepts.
- COLLECTION/WEB_RESEARCH/BROWSER_AUTOMATION_INDEX.md — Playwright, Browser Use, Open Browser, OpenBrowser broker, Browserable and AgentBrowser discovery candidates.
- COLLECTION/DOCUMENTS/DOCUMENT_OCR_INDEX.md — OCRmyPDF, Docling and Tesseract document/OCR candidates.
- These additions are DISCOVERY_CAPTURED unless an entry was explicitly supported by inspected repository documentation; discovery is not an adoption decision.
