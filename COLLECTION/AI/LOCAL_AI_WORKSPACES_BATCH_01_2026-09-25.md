# Local AI Workspaces — Batch 01 — 2026-09-25

## Collection rule
Retain distinct sources even when they perform overlapping functions. Do not collapse repositories merely because they are alternatives in the same category. Preserve each source when it contributes different architecture, license, runtime, integrations, security controls, operational tradeoffs, subscription-elimination value, or reusable implementation evidence.

## 1. SOMI — Somi-Project/Somi
Source: https://github.com/Somi-Project/Somi
Default branch: master
README SHA: 52ab8a7e821426f2ae61abefd26d73942e87a3a7
License: not established from repository LICENSE fetch
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository evidence:
- Fully self-hosted/local-first AI agent framework.
- Desktop PySide6 operator shell with Control Room, Coding Studio, Research Studio, speech controls and Node Manager.
- Local chat, persistent memory, research, coding, OCR, speech, browser automation, workflows and subagents.
- Approval-aware tools, sandboxed execution paths, audit/replay/freeze/release-gate tooling.
- Quick start requires Python 3.11+, Git and Ollama at 127.0.0.1:11434; README recommends 16GB RAM and optional NVIDIA GPU.
- License remains unknown; do not infer it from metadata or third-party listings.

Collection value: local operator/control-plane architecture with explicit audit/replay/security-gate concepts.

## 2. OpenEnsemble — openensemble/openensemble
Source: https://github.com/openensemble/openensemble
Default branch: main
License: pending direct LICENSE verification
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository evidence:
- Self-hosted multi-user AI assistant.
- Specialist agents and coordinator delegation with per-user isolation.
- Local and cloud model providers; local Ollama/LM Studio paths.
- Bundled local reasoning/embedding via node-llama-cpp.
- Deep research to persistent research documents.
- Gmail/Exchange/IMAP, calendar, expenses, documents and code projects.
- Background recurring and one-shot tasks.
- MCP, remote nodes, voice-device/ESP32 integration and skill builder.
- Node.js server.

Collection value: multi-user assistant/team architecture, local model path and recurring task/event integration.

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
- Durable recovery checkpoints.
- SSRF protections and workspace confinement; systemd hardening documented.
- Default web UI bind is 0.0.0.0, with login/TOTP recommended; trusted-network-only posture is explicitly stated.
- Cloud/provider integrations exist but local-first path is available.

Collection value: distinct focus on tool-budgeting, recovery checkpoints, idempotency, browser safety and resident coding-agent bridges.

## 4. Synapse — zai-org/Synapse
Source: https://github.com/zai-org/Synapse
Default branch: main
README SHA: 692022bf8b9ce37c3b8a0014b1016d00da357ca3
LICENSE SHA: Apache-2.0 license file fetched directly
License: Apache-2.0
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository evidence:
- Self-hosted AI workspace centered on conversations as the collaboration/runtime boundary.
- Native actors, bridged remote agents, external IM identities and human workspace members can share conversations.
- Remote-agent daemon bridges Codex CLI and Claude Code through an outbound WebSocket.
- Filesystem, command line, Chrome DevTools/browser and computer-use capabilities are exposed as governed MCP capabilities.
- Session-scoped sandbox options: local process, Docker, or off-box E2B-compatible/CubeSandbox endpoint; sandbox is opt-in and off by default.
- Explicit/revocable workspace resource grants and consume-once approvals.
- Durable schedules, webhooks and GitHub/GitLab event wakeups.
- Permissioned memory spaces with lexical retrieval plus embeddings.
- Provider architecture allows cloud APIs or self-hosted sidecars for embedding/OCR/document extraction/transcription/ASR; core defaults can operate without optional providers.
- Deployment uses Node.js 22, Docker Compose, PostgreSQL and Redis; external model credentials are required for real model operation unless a self-hosted model provider is configured.
- README explicitly labels the project early design/implementation and warns that schemas/runtime contracts may change.

Collection value: strong governed-agent/resource-grant model, remote coding-agent bridge, event-driven wakeups and capability-aware device runtime.

## 5. OpenAgents — openagents-org/openagents
Source: https://github.com/openagents-org/openagents
Default branch: develop
LICENSE SHA: 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64
License: Apache-2.0
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from public source discovery:
- Collaboration-oriented open-source/self-hosted workspace for humans and AI agents.
- Shared conversations, files/context and connected agents.
- Self-hosting path is advertised as the full platform with workspace, launcher and CLI.
- Roles, membership and access control are part of the self-hosted model.
- Hosted mode exists separately; hosted availability is not counted as a free local dependency.

Collection value: team collaboration boundary and shared human/agent workspace model distinct from single-user local assistants.

## 6. PolyRob — theselfruleorg/polyrob
Source: https://github.com/theselfruleorg/polyrob
Default branch: main
LICENSE SHA: 9987b4d833ed6a597a7ef9470b2ecbfabc96a21e
License: MIT
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from public repository evidence:
- Self-hosted autonomous AI agent intended to pursue goals, learn from experience and run locally.
- Core install can be used with zero cloud dependencies according to the project documentation.
- Optional browser automation via Playwright and optional FastAPI/web console.
- Docker Compose deployment persists memory, sessions and skills across restarts.
- Explicit deployment posture distinguishes local loopback mode from public/owner-authenticated mode; public binding upgrades to an authenticated posture.

Collection value: goal-driven autonomous agent with a clearly separated zero-cloud core and browser/server extras.

## 7. Jarvis — dev-core-busy/jarvis
Source: https://github.com/dev-core-busy/jarvis
Default branch: master
LICENSE SHA: eb17f6a0cfb9da71e073b5bc720c4ad32d8745e6
License: Apache-2.0
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from public repository evidence:
- Self-hosted autonomous Linux agent.
- Multi-LLM and multi-user architecture.
- Web chat plus Outlook/Excel task surface and WhatsApp entry point.
- Browsing, file read/write, code execution, spreadsheet editing, Office documents/diagrams, rule-based email responses, read-only SAP data access and calendar management.
- Optional VNC view exposes the desktop while the agent operates.
- README describes a security layer and sandboxed execution.

Collection value: enterprise/workplace automation surface spanning email, Office, SAP read-only data, calendar and desktop control.

## 8. Ptylon — alexfrmn/ptylon
Source: https://github.com/alexfrmn/ptylon
Default branch: main
README SHA: f7bef03be0ee54f5d6df667b76d4dfa76767d27d
LICENSE SHA: a21feb4c3af58e4f7508cc896dc40a63b22b4c21
License: MIT
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from public repository evidence:
- Self-hosted browser-native terminal workspace for coding agents such as Claude Code and Codex.
- Persistent PTY sessions, server-side browser panels, files and Monaco editor in one authenticated URL.
- Docker Compose and systemd deployment.
- Separate authenticated WebSocket gateway and localhost-only PTY daemon; browser control uses CDP.
- Workspace/file access boundaries and explicit secret configuration.
- Browser regression tests, PTY gateway tests, TypeScript/lint/build verification and localhost admin browser automation.
- Current limitations explicitly include headless-browser/IP-reputation blocking and PTY state loss on host reboot.

Collection value: reusable remote coding-agent workstation pattern with persistent terminal/browser state and strong process-boundary lessons.

## Cross-source note
All eight sources above are intentionally retained separately despite substantial overlap with Odysseus and each other. Functional overlap is not a deduplication reason.

## Verification queue
For each source, deep-verify dependency manifests, current revision/commit provenance, complete license files, tests/CI, deployment path, external-cost boundaries, optional cloud dependencies, security controls, and operational limitations before any VERIFIED classification.


## 9. Agency Agents — msitarzewski/agency-agents
Source: https://github.com/msitarzewski/agency-agents
Default branch: main
README SHA: a3a6c65b8eb5a3b0722ab504eed00e2d06494720
LICENSE SHA: 523078c01624b9b1b1c551e75054b9d3a9f953ab
License: MIT
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository evidence:
- Large collection of specialized AI-agent personas organized by divisions such as engineering, security, marketing, product, project management, support, testing, strategy, and specialized roles.
- Agent files are intended as reusable role/workflow definitions with identity, mission, workflows, deliverables, examples, success metrics and communication guidance.
- Native/scripted integration paths for Claude Code, GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Kimi, Codex, Osaurus, Hermes and Mistral Vibe are documented.
- Installer supports selecting tools, divisions or individual agents and dry-run/listing modes.
- Repository README documents an OpenCode runtime limit of approximately 119 agents and warns that excess agents may be silently dropped; this is an operational limitation, not a claim that the collection itself is limited to that number.
- A separate native Agency Agents app repository exists and is advertised as a local-first installer/control surface; it is a distinct source and will be collected separately rather than merged into this repository.
- MIT license confirmed directly from LICENSE.

External-cost boundary:
- The agent definitions themselves are open-source and local files.
- Actual execution still depends on the selected host/LLM/tool; local or no-key model paths must be verified separately and are not assumed from this repository.

Collection value: reusable specialist-agent corpus and multi-tool conversion/install patterns. It is retained as an independent source even though it overlaps with other agent/workspace projects.


## 10. Dagents — dagents/dagents
Source: https://github.com/dagents/dagents
Default branch: main
README SHA: 2ab7b925ec580113a10490c97237298d50184dd8
LICENSE SHA: c5fb83242f44aeb962255574afcf802bd02ec0ed
License: Apache-2.0
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository evidence:
- Local-first orchestration workbench for heterogeneous CLI coding agents including Claude, Codex and Qwen plus community adapters.
- Workflow engine exposes a 14-node DAG with parallel waves, condition routing, loops and human-in-the-loop; runs stream node results and retain run links/history.
- Can mount agency-agents-style persona libraries from the filesystem, enable personas on demand and detect upstream drift.
- Docker Compose stack provides Postgres, gateway and console; local bindings default to 127.0.0.1.
- HTTP LLM providers are optional rather than the baseline execution dependency; local CLI agents can run the workbench without a provider configured.
- Gateway/console architecture uses Next.js, Hono and a workflow package; remote execution is supported through a pull-based daemon.
- LLM API keys are documented as encrypted at rest; repository states no telemetry/accounts/callbacks home for the local-first mode.
- External costs remain possible where selected CLI agents or LLM providers themselves require paid access; this must not be counted as eliminated by Dagents.

Collection value: potentially important orchestration layer for combining Agency Agents/personas with multiple local coding CLIs while retaining durable workflow assets. Retained as an independent source despite overlap.


## 11. OpenCode — anomalyco/opencode
Source: https://github.com/anomalyco/opencode
Default branch: dev
README SHA: b5a4c8ddd9794e8c20bd287603bfa0c336522796
LICENSE SHA: 6439474beed8e0271df9862eff97ffd70ec2464c
SECURITY SHA: e7e59f4a27ac2bd2ed5005f8851dcb946c08f914
License: MIT
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository evidence:
- Open-source AI coding agent with terminal UI, desktop application, and IDE-oriented ecosystem.
- Built-in build agent (full access), plan agent (read-only by default) and general subagent.
- Provider-agnostic architecture; official documentation states API keys are required for configured LLM providers, while repository/docs support local models and multiple providers.
- Installation supports npm/bun/pnpm/yarn, Homebrew, Arch, Windows package managers, Nix and Docker.
- Repository explicitly describes OpenCode as local software with shell, file and web access.
- Security model is important: permissions are UX awareness/confirmation, NOT a security sandbox. For real isolation, project security guidance recommends Docker or VM.
- Opt-in server mode can require HTTP Basic Auth via OPENCODE_SERVER_PASSWORD; unauthenticated server mode is possible if enabled without the password.
- Distinct related repositories found under anomalyco include opencode-sdk-python, opencode-sdk-go, opencode-sdk-js, opencode-bench, opencode-copilot-auth, opencode-voice, and opencode-beta; these should be retained as separate sources where relevant rather than merged into the core repository.

External-cost boundary:
- OpenCode software is MIT and can run locally, but model inference may require paid provider access unless a suitable local/free model path is used. Provider cost is therefore not eliminated automatically.

Collection value: major open-source coding-agent baseline; relevant to subscription elimination, local development, agent orchestration, and integration with the previously collected Agency Agents/Dagents ecosystem.
