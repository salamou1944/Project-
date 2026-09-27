# COLLECTION — AI Index

Status: DISCOVERY_CAPTURED
Captured: 2026-09-25

Purpose: preserve AI/agent/model infrastructure sources now, before deeper recursive inspection. A captured source is not automatically verified or production-ready.

## Agent frameworks / orchestration
- LangGraph — https://github.com/langchain-ai/langgraph
- OpenAI Agents SDK — https://github.com/openai/openai-agents-python
- PydanticAI — https://github.com/pydantic/pydantic-ai
- smolagents — https://github.com/huggingface/smolagents
- CrewAI — https://github.com/crewAIInc/crewAI
- AG2 — https://github.com/ag2ai/ag2
- Microsoft Agent Framework — https://github.com/microsoft/agent-framework
- Google ADK — https://github.com/google/adk-python
- Haystack — https://github.com/deepset-ai/haystack
- LlamaIndex — https://github.com/run-llama/llama_index
- Mastra — https://github.com/mastra-ai/mastra

## Agent runtimes / control / execution
- AIOS — https://github.com/agiresearch/AIOS
- Hatchet — https://github.com/hatchet-dev/hatchet
- OpenHands — https://github.com/All-Hands-AI/OpenHands
- Open Interpreter — https://github.com/OpenInterpreter/open-interpreter
- Aider — https://github.com/Aider-AI/aider
- Continue — https://github.com/continuedev/continue

## Memory / knowledge / RAG
- Letta — https://github.com/letta-ai/letta
- Qdrant — https://github.com/qdrant/qdrant
- RAGFlow — https://github.com/infiniflow/ragflow
- GraphRAG — https://github.com/microsoft/graphrag
- Cognee — https://github.com/topoteretes/cognee
- Chroma — https://github.com/chroma-core/chroma
- Weaviate — https://github.com/weaviate/weaviate
- Milvus — https://github.com/milvus-io/milvus
- HelixDB — https://github.com/HelixDB/helix-db

## Local model serving / gateways
- Ollama — https://github.com/ollama/ollama
- llama.cpp — https://github.com/ggml-org/llama.cpp
- vLLM — https://github.com/vllm-project/vllm
- LocalAI — https://github.com/mudler/LocalAI
- LiteLLM — https://github.com/BerriAI/litellm
- GPT4All — https://github.com/nomic-ai/gpt4all
- Jan — https://github.com/janhq/jan
- Open WebUI — https://github.com/open-webui/open-webui
- exo — https://github.com/exo-explore/exo

## Agent applications / local-first assistants
- AnythingLLM — https://github.com/Mintplex-Labs/anything-llm
- Dify — https://github.com/langgenius/dify
- Flowise — https://github.com/FlowiseAI/Flowise
- Khoj — https://github.com/khoj-ai/khoj
- AutoAgent — https://github.com/HKUDS/AutoAgent
- nanobot — https://github.com/HKUDS/nanobot
- CoPaw — https://github.com/agentscope-ai/CoPaw

## Evaluation / safety / observability — discovery queue
- Inspect AI — https://github.com/UKGovernmentBEIS/inspect_ai
- DeepEval — https://github.com/confident-ai/deepeval
- promptfoo — https://github.com/promptfoo/promptfoo
- OpenTelemetry GenAI semantic conventions — https://github.com/open-telemetry/semantic-conventions

## Discovery references
- Awesome LLM Agents — https://github.com/kaushikb11/awesome-llm-agents
- Awesome Agent Frameworks — https://github.com/alexbevi/awesome-agent-frameworks
- Awesome AI Agents 2026 — https://github.com/caramaschiHG/awesome-ai-agents-2026
- Awesome Local AI Agents — https://github.com/Supersynergy/awesome-local-ai-agents

## Important rule
This file is a source-preservation layer. Before integration, inspect repository files, license, release activity, dependency/security posture, local execution path, and actual capabilities. Do not infer a paid-service replacement merely from an entry in an awesome list.


## harry0703 capability extraction — 2026-09-27

Source account: https://github.com/harry0703
Inventory status: 21 repositories discovered. Capability verification is repository/file specific; discovery indexes are not treated as verified implementations.

### VERIFIED_FROM_REPOSITORY_CONTENT

| Repository | Exact revision | Capability | Evidence level |
|---|---|---|---|
| harry0703/MoneyPrinterTurbo | 8e259e9f072c9e08464f040cd658d4eb046a57d0 | AI short-video generation pipeline; Agent/WebUI/API/CLI; script generation; material search; subtitles; BGM; video composition; multiple LLM/TTS/media providers; Docker; Redis; LiteLLM; FFmpeg integration; path-security helper | VERIFIED_FROM_README/TREE/FILES |
| harry0703/AudioNotes | 9a580707eb9258ce53c59a5edd70e834a5d8098d | Local-first audio/video transcription; FunASR; local Ollama Q&A/note generation; Markdown notes; browser recording; Docker; local storage | VERIFIED_FROM_README |
| harry0703/MangoDisk | 3b83950053d9ed4cd9a6c7577d2f1cb7a05f83a1 | Cross-platform storage analysis/cleanup; duplicate/large-file cleanup; privacy cleanup; application uninstall; startup/system maintenance; AI explanations; Tauri 2 + Rust core | VERIFIED_FROM_README |
| harry0703/FlashVoice | 599b1aa2c9054d2488f85fd78411a404fac6c626 | Local real-time voice input/transcription; SenseVoice; offline file transcription; system/mic audio; optional local Ollama/OpenAI-compatible proofreading; macOS/Windows desktop | VERIFIED_FROM_README |
| harry0703/claude-code | 7af07613ac688bfd9ba2cb2b72d7973378cfc317 | Coding-agent related repository | VERIFIED_IDENTITY; capability details require deeper file-level inspection |
| harry0703/go-openai | 38b16a3c413a3ea076cf4082ea5cd1754b72c70f | Go OpenAI client/library source | VERIFIED_IDENTITY; integration suitability requires license/API inspection |
| harry0703/go-admin | 8bc57590ab57df9d09930a774014421d0a82a2f2 | Go web/admin application foundation; admin UI, database/config/upload patterns | VERIFIED_FROM_REPOSITORY_CONTENT |
| harry0703/awesome-tauri | c17a8b9583201ed61608b1bb2365e2ceebaf9161 | Curated Tauri ecosystem discovery: templates, plugins, integrations, applications | DISCOVERY_INDEX |
| harry0703/open-apps | 109c1965ba0123b5d62db69cb50e937a003bc7cb | Curated production open-source application discovery directory | DISCOVERY_INDEX |
| harry0703/awesome-windows | 20520c38de56b5cb0e9eb757ef138c5e5fa1f99d | Curated Windows applications/tools discovery | DISCOVERY_INDEX |

### DISCOVERY_ONLY_PENDING_DEEP_INSPECTION

- harry0703/yt-dlp — media acquisition/download source; operational reuse requires security/legal/use-case gate.
- harry0703/stopwords-zh — Chinese NLP data.
- harry0703/mpt-assets — assets repository; inspect concrete contents before reuse.
- harry0703/winget-pkgs — packaging/catalog infrastructure.
- harry0703/awesome-mac — macOS software discovery index.
- harry0703/harry0703 — profile metadata repository.
- harry0703/awesome-rust — Rust ecosystem discovery index.
- harry0703/homebrew-cask — package catalog infrastructure.
- harry0703/homebrew-tap — personal Homebrew tap; inspect manifests before reuse.
- harry0703/open-source-mac-os-apps — open-source macOS app discovery index.
- harry0703/awesome-rust-1 — duplicate/variant Rust discovery index; dedupe before treating as a separate knowledge source.

### Reuse gate
No item above is promoted automatically into executable capability. Adoption requires: canonical identity + exact revision + license/security review + compatibility check + independent verification + project-specific test.


## harry0703 deep inspection — 2026-09-27

Deep inspection completed for the remaining 10 repositories. Default branches and repository content were inspected through the GitHub connector. Exact commit SHAs were not exposed by the branch endpoint, so no fabricated SHA is recorded; README blob SHAs are preserved as file-level evidence where available.

| Repository | Branch | Capability / role | License evidence | Evidence level | Dedupe result |
|---|---|---|---|---|---|
| harry0703/yt-dlp | master | Feature-rich CLI audio/video downloader; extractors, subtitles, post-processing, plugins, embedding | Unlicense/public-domain dedication | VERIFIED_FROM_README + LICENSE | Capability overlaps with existing Agent-Reach intake; exact repo was not already indexed as a canonical source |
| harry0703/stopwords-zh | master | Chinese/English stopword datasets and filtering helpers; Baidu/HIT/ICT/SCU/CN/Marimo/ISO sources | MIT | VERIFIED_FROM_README + LICENSE | No exact canonical match found in Project- code search |
| harry0703/mpt-assets | main | Media assets for MoneyPrinterTurbo | No LICENSE file found at inspected path | VERIFIED_FROM_README | Companion asset source; linked to already-collected MoneyPrinterTurbo, not a new general capability |
| harry0703/winget-pkgs | master | Windows package-manager manifest/catalog infrastructure | MIT | VERIFIED_FROM_README + LICENSE | Discovery/infrastructure; not an executable capability for the operator |
| harry0703/awesome-mac | master | Curated macOS software discovery index | CC0-1.0 | DISCOVERY_INDEX | No exact canonical match found in Project- code search |
| harry0703/homebrew-cask | main | Homebrew Cask package/catalog infrastructure for GUI apps, CLI tools, fonts and plugins | BSD 2-Clause | VERIFIED_FROM_README + LICENSE | Discovery/package infrastructure; adoption requires package-level verification |
| harry0703/homebrew-tap | main | Personal Homebrew tap; MangoDisk cask + CLI formula with pinned SHA-256 release artifacts | No LICENSE file found at inspected path | VERIFIED_FROM_README | Direct companion to MangoDisk; no new general capability |
| harry0703/open-source-mac-os-apps | master | Curated macOS open-source application discovery index | CC0-1.0 | DISCOVERY_INDEX + LICENSE | No exact canonical match found in Project- code search |
| harry0703/awesome-rust | main | Curated Rust ecosystem index spanning AI, observability, security, deployment, web, databases and more | License file not found at inspected path | DISCOVERY_INDEX | No exact canonical match found in Project- code search |
| harry0703/awesome-rust-1 | master | Alternate/older Rust ecosystem discovery index | License file not found at inspected path | DISCOVERY_INDEX | Treat as possible duplicate/variant of awesome-rust; do not count as a distinct capability source |

### Security / reuse gates
- yt-dlp remains gated for operational media acquisition: use only for authorized content and explicit project use-cases.
- Package/catalog repositories are metadata sources, not automatically trusted installers.
- Discovery indexes are never promoted to executable capabilities without resolving the linked project, license, security posture, exact revision and compatibility.
