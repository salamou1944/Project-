# ODYSSEUS DEEP CAPTURE — 2026-09-25

## Canonical source
- Repository: odysseus-dev/odysseus
- Branch inspected: dev
- README blob SHA: 72bd1303cfc41487a9b45eae73d1930a29bd5153
- Docker Compose blob SHA: 708e5df828a156b1c0452bf08c3da628e1510183
- License: AGPL-3.0-or-later
- Repository description: self-hosted AI workspace for chat, agents, research, documents, email, notes, calendar, and local model workflows.

## Verified capabilities from repository evidence
- Chat + agents with local/API models, tools, MCP, files, shell, skills, memory.
- Hardware-aware model cookbook, downloads, and serving.
- Multi-step deep research with source reading/report generation.
- Blind model comparison and synthesis.
- AI-assisted documents with Markdown/HTML/CSV/syntax highlighting.
- IMAP/SMTP email triage, tagging, summaries, reminders, reply drafts.
- Notes, tasks, calendar and CalDAV sync.
- Gallery/image editing, themes, uploads, web search, presets, sessions, 2FA.
- Docker-first self-hosting; default UI binding is localhost:7000.
- Local Ollama can be reached from the container through host.docker.internal.
- Bundled SearXNG, ChromaDB, and ntfy services.
- SQLite is the default database URL.
- Optional/provider integrations exist for OpenAI, Hugging Face, Brave, Google, Tavily, Serper, embeddings, etc.; these are external dependencies, not counted as subscription-free inference/search.

## Subscription-elimination relevance
Potentially replaces a broad hosted AI workspace/research/productivity stack when paired with local models:
- Chat/agent UI
- local model management/serving workflows
- research/search interface
- document workspace
- memory/vector store
- email/notes/tasks/calendar
- image/gallery tooling

The repository is therefore a high-value candidate for the collection's "replace paid SaaS with self-hosted/local" corpus.

## Cost/dependency boundary
- Software is open-source under AGPL-3.0-or-later.
- Local inference can use Ollama and other local runtimes, but hardware remains a real cost.
- Hosted model providers remain optional external costs.
- Search can be local/self-hosted via SearXNG in the supplied compose stack, reducing dependence on paid search APIs.
- ChromaDB is bundled for vector storage; SQLite is the default app database.
- Docker/host resources are required for the bundled deployment.
- No claim of zero operating cost: electricity/server/VPS/GPU, domains, email, or external providers may still cost money.

## Security observations
The project itself warns that it is a powerful local admin-like workspace. Authentication should remain enabled; localhost bypass should remain disabled outside local development; raw model/service ports should not be exposed publicly. Treat shell, file access, model downloads, web research, email/calendar and API-token capabilities as high-trust functions.

## Verification status
EXTRACTED_PENDING_DEEP_VERIFICATION

## Next verification
- Inspect setup/security documentation.
- Inspect dependency manifests and optional dependencies.
- Check release/version provenance and recent commits.
- Inspect model-serving/cookbook implementation and external-provider boundaries.
- Inspect search/research architecture and SearXNG integration.
- Inspect auth/privilege boundaries and 2FA implementation.
- Compare against Preloop/Agent Reach/other local agent workspaces for overlap.
