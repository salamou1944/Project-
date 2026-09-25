# Accelerated AI + Browser Collection — Batch 02 — 2026-09-25

## Sources captured

### 1. Browserable — browserable/browserable
Source: https://github.com/browserable/browserable
Default branch: main
README SHA: 854d0bd53818b1f935710d414eb8e545c4a0b056
LICENSE SHA: 952ed0cf86e01d1f314d8d0cb75d34fd40585ad8
License: MIT
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

- Open-source/self-hostable browser automation library for AI agents.
- Browser navigation, form filling, clicking and extraction.
- Docker Compose stack includes UI, task API, MongoDB, Redis, MinIO and DB Studio.
- SDK/API surface available.
- README currently requires an LLM provider key and a remote-browser provider key for the documented setup, with free-plan provider options mentioned; therefore it is not yet classified as fully subscription-free.
- Acknowledges Bull, Mongo Express, Stagehand and Supabase among dependencies/inspiration.
- Collection value: full browser-agent application stack and useful integration/deployment reference.

### 2. UI-TARS Desktop — bytedance/UI-TARS-desktop
Source: https://github.com/bytedance/UI-TARS-desktop
Default branch: main
License: Apache-2.0
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

- Multimodal GUI-agent stack covering terminal, computer and browser operation.
- Agent TARS includes CLI/Web UI, MCP integration, GUI/vision workflow and headful/headless execution.
- UI-TARS Desktop provides local and remote computer operators and browser operators.
- Repository documents a local operator path and remote operator path.
- Node.js >=22 is required for Agent TARS CLI.
- External model/provider requirements vary by deployment; local model path requires separate verification.
- Collection value: major multimodal computer-use architecture with local operator capability.

### 3. Browser Agent — magnitudedev/browser-agent
Source: https://github.com/magnitudedev/browser-agent
Default branch: main
License: Apache-2.0
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

- Dedicated autonomous browser-agent repository.
- TypeScript implementation and browser automation focus.
- Retained separately from Browserable, Nanobrowser and Steel because the agent layer is distinct from browser-runtime infrastructure.
- External model/browser requirements and current maintenance state require deeper verification.

### 4. Browser4 — platonai/Browser4
Source: https://github.com/platonai/Browser4
Default branch: main
LICENSE SHA: ebc34324d0fd0bc25aeb2c317e8eef685b453bef
License: Apache-2.0
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

- AI-native browser engine with Rust CLI, MCP and agentic backend.
- Deterministic extraction via X-SQL/CSS and zero-token extraction paths.
- Hybrid LLM/ML extraction, selector learning, stateful sessions and swarm/batch automation.
- Includes a programming-agent kernel with sandboxed shell/filesystem, validation, scaffolding and repository-protection concepts.
- Modules include browser core, agentic integration, REST layer, examples and tests.
- Collection value: unusually broad browser + extraction + agent-kernel architecture; should be deeply verified rather than treated as a simple browser library.

### 5. Singulary — sammwyy/singulary
Source: https://github.com/sammwyy/singulary
Default branch: main
README SHA: 12345dc59fc72868a899621f6c71c19803e9fd49
LICENSE SHA: 4b317a17b178cec607ad23dbabd42e27fe0c16ec
License: MIT
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

- Self-hosted AI application builder positioned as an alternative to closed AI app builders.
- Docker-isolated project workspaces with agent file/shell/runtime tools.
- BYOK supports multiple providers and OpenAI-compatible local endpoints including Ollama/LM Studio.
- Built-in service catalog can provision PostgreSQL, MySQL/MariaDB, MongoDB, Redis, MinIO, RabbitMQ and Meilisearch.
- Single production container architecture with SQLite metadata; WebSocket/SSE streaming.
- Provider keys and service credentials encrypted at rest; audit logging and approval flow for dangerous agent calls.
- Security caveat: Docker socket access can amount to host-root control; repository explicitly warns about the trust boundary.
- Collection value: direct candidate for replacing hosted AI app-builder subscriptions and a reusable isolated agent workspace pattern.

## Acceleration note
These sources were discovered from current public web research and then matched against exact public GitHub repositories before collection. They are retained independently despite overlap.
