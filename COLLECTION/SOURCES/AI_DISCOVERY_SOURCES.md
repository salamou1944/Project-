# AI Discovery Sources

Captured: 2026-09-25

These sources are preserved so future research can resume even if a page changes or disappears.

## Current web sources
- Awesome Local AI Agents (March 2026 edition): https://github.com/Supersynergy/awesome-local-ai-agents
- Awesome LLM Agent Frameworks: https://github.com/kaushikb11/awesome-llm-agents
- Awesome Agent Frameworks: https://github.com/alexbevi/awesome-agent-frameworks
- Awesome AI Agents 2026: https://github.com/caramaschiHG/awesome-ai-agents-2026
- Awesome AI Agents: https://github.com/aloth/awesome-ai-agents

## Observations captured from these sources
- The local AI ecosystem spans model runners, inference servers, agent frameworks, RAG, memory, coding agents, browser/computer-use agents, sandboxes, observability/evals and safety.
- Local/self-hosted infrastructure is broad enough to reduce dependence on metered cloud APIs, but every project must be checked individually for license, model licensing, hardware requirements and cloud-only features.
- Agent frameworks are changing quickly; repository activity and maintenance state must be rechecked before adoption.
- Awesome lists are discovery indexes, not verification evidence.

## Research policy
1. Capture source first.
2. Then inspect the repository recursively.
3. Preserve license and exact revision/release where relevant.
4. Separate open-source/local capability from hosted/free-tier capability.
5. Record limitations and hardware requirements.
6. Never mark a source VERIFIED solely because an aggregator lists it.


## Newly captured repository
- OmniRoute: https://github.com/diegosouzapw/OmniRoute
- Captured: 2026-09-27
- Classification: AI gateway / multi-provider routing / MCP / A2A / token compression / free-provider discovery.
- State: DISCOVERY_CAPTURED; not yet VERIFIED or adopted.

## harry0703 public repository source
- Account: https://github.com/harry0703
- Captured: 2026-09-27
- Discovery method: GitHub repository search for `user:harry0703` via authenticated GitHub connector.
- Public repositories discovered: 21
- Policy: treat each repository as an independent discovery source; deduplicate by canonical `owner/repo` identity; resolve and preserve the exact default-branch commit revision when the capability feed ingests it.

### Discovered repositories
- https://github.com/harry0703/MoneyPrinterTurbo
- https://github.com/harry0703/MangoDisk
- https://github.com/harry0703/AudioNotes
- https://github.com/harry0703/FlashVoice
- https://github.com/harry0703/claude-code
- https://github.com/harry0703/yt-dlp
- https://github.com/harry0703/go-admin
- https://github.com/harry0703/stopwords-zh
- https://github.com/harry0703/mpt-assets
- https://github.com/harry0703/go-openai
- https://github.com/harry0703/awesome-tauri
- https://github.com/harry0703/winget-pkgs
- https://github.com/harry0703/open-apps
- https://github.com/harry0703/awesome-windows
- https://github.com/harry0703/awesome-mac
- https://github.com/harry0703/harry0703
- https://github.com/harry0703/awesome-rust
- https://github.com/harry0703/homebrew-cask
- https://github.com/harry0703/homebrew-tap
- https://github.com/harry0703/open-source-mac-os-apps
- https://github.com/harry0703/awesome-rust-1

### Initial capability triage
- MoneyPrinterTurbo: AI video generation/media pipeline, WebUI/API/CLI, agent Skill, Docker.
- AudioNotes: local audio/video transcription, structured Markdown notes, local Ollama workflow, Docker.
- MangoDisk: local disk cleanup/storage analysis/optimization, desktop + CLI.
- FlashVoice: audio/voice capability source; requires repository-level verification before adoption.
- claude-code: coding-agent related source; requires repository-level verification and provenance checks before reuse.
- yt-dlp: media acquisition/downloading capability; security/legal/use-case gates required before operational reuse.
- go-admin: Go administration/application foundation; requires project-fit verification.
- go-openai: Go OpenAI client/library capability; verify upstream relationship/license before reuse.
- stopwords-zh: Chinese NLP stopword data.
- awesome-* / open-source-* repositories: discovery indexes, not proof of individual component capabilities.
- mpt-assets / homebrew-* / winget-pkgs: packaging/assets/catalog infrastructure; ingest as discovery metadata unless a concrete capability is verified.
- harry0703 profile repository: profile metadata only.
