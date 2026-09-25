# COLLECTION — PLATFORM/AGENT INTEGRATION SWEEP
Date: 2026-09-25
Scope: collected source material in Project- (source layer), not project implementation repositories.

## Purpose
This record consolidates the results of the platform-focused sweep so the same source material is not re-collected. It is an index/decision record, not a replacement for source captures.

## Verified source-layer findings

### ChatGPT / OpenAI
- Project- already contains captured ChatGPT/OpenAI material, including AUTO/EXTRACTED/Panniantong_WechatBot.json and Panniantong_WechatBot2.json.
- The captured material includes ChatGPT integration, OpenAI account/API handling, retry handling, Docker deployment, and Railway deployment.
- Treat account-pool/session-token/credential-based automation as historical source material only; do not reuse credentials or bypass provider controls.
- Existing collection material also covers OpenAI-compatible provider patterns and local/self-hosted alternatives.

### Codex / agent skills
- The collection scope already contains agent/skill/MCP research.
- External source verification identified the official railwayapp/railway-skills repository as directly relevant: it packages Railway support for OpenAI Codex and exposes a Railway Agent Skill plus hosted MCP.
- This is a high-leverage integration pattern for the engineering/control-plane work because it combines skill routing, MCP access, deployment/status operations, and infrastructure troubleshooting.

### Railway
- Official railwayapp/railway-skills exposes:
  - use-railway skill
  - hosted Railway MCP
  - Codex plugin manifest
  - Claude Code, Cursor and Grok packaging
  - CLI/agent setup
- The skill explicitly separates local CLI, remote MCP, and GraphQL paths and requires verification after mutations.
- This pattern is relevant to deployment provenance and evidence-gated operations in EASY/ARMY-14/Elite.

### MCP
- Existing Project- collection contains MCP/local-agent/browser/AI gateway material.
- MCP should be treated as an integration transport/capability layer, not proof that a target service is authenticated or operational.
- Preserve the existing evidence rule: discovery != authentication != successful execution.

### Local/self-hosted AI and free-cost reduction
- Existing collection records already cover Ollama, llama.cpp, vLLM, LocalAI, LiteLLM, Open WebUI, Jan, OpenRouter and OpenAI-compatible endpoints.
- These are relevant for reducing dependence on paid model APIs when local inference is practical.
- Gate adoption on measured capability, hardware/resource cost, latency, quality, and compatibility; do not label a provider as a free replacement merely because it exposes an OpenAI-compatible API.

### Security
- Existing collection contains AI-security and general security material.
- The collected AI-security source set includes agent auditing, MCP security, prompt/jailbreak research, and AI coding-agent security tooling.
- Use these as defensive verification inputs for Elite/ARMY-14/EASY rather than importing offensive capabilities into production.

## Deduplication rule
- Raw source captures remain in their existing AUTO/EXTRACTED or topic-specific collection files.
- This file is only an index of the platform integration findings.
- Do not create second copies of the same upstream repository capture.
- If a source already exists, update/link the existing record rather than recapturing it.

## Immediate leverage identified
1. Railway official agent-skill + hosted MCP pattern.
2. Codex plugin/marketplace packaging pattern.
3. Evidence-gated MCP/tool routing pattern.
4. OpenAI-compatible provider abstraction already present in Salamou-31/AI_operating_memory.
5. Local/self-hosted inference options already collected for reducing paid API dependency.
6. AI-agent security/audit tooling already collected for defensive verification.

## Evidence status
COLLECTED_AND_INDEXED.
No claim is made that every upstream repository in the entire historical collection universe has been exhaustively re-inspected in this single sweep. The platform-focused sources found in the current Project- collection were indexed without duplicating raw captures.
