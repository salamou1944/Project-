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
- Jina Reader — https://github.com/jina-ai/reader
  - URL-to-LLM-friendly content and web search capability.
  - Candidate fallback where its current public service remains usable.

### Crawling / extraction
- Firecrawl — https://github.com/firecrawl/firecrawl
  - Open-source web scraping/crawling/extraction stack; self-hosting requires security, persistence, backup and scaling work.
- Crawl4AI — https://github.com/unclecode/crawl4ai
  - Self-hosted crawling/data extraction; pin/check revision before deployment.
- Scrapy — https://github.com/scrapy/scrapy
  - Mature Python crawling/extraction framework; BSD-3-Clause.

### Browser automation
- Playwright — https://github.com/microsoft/playwright
- Browser Use — https://github.com/browser-use/browser-use

### Documents / files
- Docling — https://github.com/docling-project/docling
- OCRmyPDF — https://github.com/ocrmypdf/OCRmyPDF

### AI memory / retrieval
- Qdrant — https://github.com/qdrant/qdrant

### Image / creative
- rembg — https://github.com/danielgatis/rembg
- Upscayl — https://github.com/upscayl/upscayl

### Audio / video
- whisper.cpp — https://github.com/ggml-org/whisper.cpp
- FFmpeg — https://github.com/FFmpeg/FFmpeg

## New 2026-09-25 discovery and verification captures
The detailed collection corpus is stored under COLLECTION/ and includes AI, browser automation, documents/OCR, self-hosted SaaS replacements, observability/control, storage, security, automation, communication, CRM/support, developer tooling, search/indexing, databases, analytics/BI, forms/e-sign/scheduling, backup/DR and data pipelines.

### Deep verification
- COLLECTION/VERIFICATION/DEEP_VERIFICATION_BATCH_2026-09-25.md
- COLLECTION/VERIFICATION/VERIFICATION_QUEUE_NEXT.md
- COLLECTION/VERIFICATION/NMAP_ECOSYSTEM_DEEP_VERIFICATION_BATCH_01_2026-09-25.md

### OSINT
- COLLECTION/OSINT/SHERLOCK_CAPTURE_2026-09-25.md
  - Sherlock username-focused OSINT discovery; MIT; self-hostable; deep verification pending.

### Account/Nmap collection
- COLLECTION/ACCOUNTS/NMAP_AND_ACCOUNT_SOURCES_CAPTURE_2026-09-25.md
- COLLECTION/ACCOUNTS/AW_JUNAID_DEEP_EXTRACTION_BATCH_01_2026-09-25.md
- COLLECTION/ACCOUNTS/ACCOUNT_DEEP_EXTRACTION_BATCH_02_2026-09-25.md
- COLLECTION/ACCOUNTS/MUFEEDVH_DEEP_EXTRACTION_BATCH_02_2026-09-25.md
- Scope includes aw-junaid, mufeedvh, Nmap ecosystem and previously identified account/repository sources.

### ASTRA / Free / Project continuation
- COLLECTION/ASTRA_FREE_PROJECT_STATE_2026-09-25.md
- Canonical ASTRA repo: salamou1944/Astra.
- salamou1944/Astra- is a separate minimal Bot repository and is not the canonical ASTRA quant implementation.
- No separate repository literally named Free is currently present in the salamou1944 account search; Project- currently has description/README "Free" and is the central collection store.
- ASTRA current evidence: REAL_DATA proven, but strategy/profitability/alpha remain unverified; live-money execution is OFF.
- A real defect was found and patched in the prospective-paper validator: it previously measured forward data using a fixed row index against a bounded current Kraken OHLC response. It is now anchored to the fixed holdout timestamp and requests data from that boundary with lookback context.
- Patch commit: 881a240b68b81ea4f3183c852d22bf8c4158cd99.
- GitHub Actions prospective validation run for that commit was observed queued; CI result must be treated as pending until completed.
- Do not interpret workflow success as profitability evidence.

## Collection rules
1. Discovery != production-ready without verification.
2. Preserve source URL, revision/version, license, setup method, dependencies and limitations.
3. Prefer local/self-hosted/free paths before paid APIs.
4. Separate free/open-source from free cloud tiers.
5. Do not copy credentials, secrets or private user data.
6. Do not mark COMPLETE until the agreed source graph and requested repository/file sets are actually inspected and verified.

## Current frontier
Continue:
- ASTRA prospective real-data evidence and verification boundary.
- ASTRA-/collection provenance where it adds reusable research material.
- Free/self-hosted replacement discovery and verification.
- aw-junaid remaining repositories/gists, mufeedvh repositories, Nmap ecosystem and other previously supplied accounts.
- Agent Reach adapters/dependencies and persistent research intake.
- High-value verification queue under COLLECTION/VERIFICATION/VERIFICATION_QUEUE_NEXT.md.

No completion claim is made. Collection remains active.


## Provenance audit
- COLLECTION/MASTER/DEDUPLICATION_AND_PROVENANCE_AUDIT_2026-09-25.md
