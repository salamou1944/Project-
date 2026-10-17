# Account-wide source capture — doobidoo — 2026-10-17

Status: OWNER_ENUMERATION_COMPLETE; PRIORITY_REPOSITORIES_TRIAGED; DEEP_SWEEP_OPEN
Owner: https://github.com/doobidoo
Enumeration method: GitHub owner-scoped repository search `user:doobidoo`, page 1 returned 53 public repositories and page 2 returned 0 on 2026-10-17.
Source graph: existing COLLECTION frontier record plus current owner-scoped search.
Scope limit: README/manifest/license review of priority memory/MCP projects; this is not a full source-tree audit of all 53 repositories.

## Enumerated public repositories

1. https://github.com/doobidoo/mcp-memory-service
2. https://github.com/doobidoo/MCP-Context-Provider
3. https://github.com/doobidoo/claude-memory-context
4. https://github.com/doobidoo/mcp-memory-dashboard
5. https://github.com/doobidoo/shodh-cloudflare
6. https://github.com/doobidoo/ChatExporter
7. https://github.com/doobidoo/mac-ai-setup
8. https://github.com/doobidoo/AgentNexus
9. https://github.com/doobidoo/obsidian-shodh-sync
10. https://github.com/doobidoo/ESP32-Uptime-Monitor
11. https://github.com/doobidoo/n8n-claude-memory-agent
12. https://github.com/doobidoo/mcp-memory-service-rs
13. https://github.com/doobidoo/iMacBrightness
14. https://github.com/doobidoo/iMacDimmerUbuntu
15. https://github.com/doobidoo/onetimesecret-mcp
16. https://github.com/doobidoo/midi-shimmer
17. https://github.com/doobidoo/MicroDashboard
18. https://github.com/doobidoo/worshiptools-display-switcher
19. https://github.com/doobidoo/ghome-web
20. https://github.com/doobidoo/doobidoo
21. https://github.com/doobidoo/outlook-ai-agent
22. https://github.com/doobidoo/azure-sftp-automation
23. https://github.com/doobidoo/FreeSong
24. https://github.com/doobidoo/outlook-ai-assistant
25. https://github.com/doobidoo/awesome-machine-learning
26. https://github.com/doobidoo/mcp-apps-renderer
27. https://github.com/doobidoo/chord-progression-generator
28. https://github.com/doobidoo/dokuwiki-plugin-aichatlocal
29. https://github.com/doobidoo/dokuwiki-mcp-server
30. https://github.com/doobidoo/dokuwiki2markdown
31. https://github.com/doobidoo/gemini-voice
32. https://github.com/doobidoo/claude-cli
33. https://github.com/doobidoo/KnowledgeGraph
34. https://github.com/doobidoo/datasciencecoursera
35. https://github.com/doobidoo/awesome
36. https://github.com/doobidoo/nanobot-fork
37. https://github.com/doobidoo/speedtest-monitor
38. https://github.com/doobidoo/dual-release-project
39. https://github.com/doobidoo/doobidoo.github.io
40. https://github.com/doobidoo/paypalcurrencyconverterpro-revamp
41. https://github.com/doobidoo/dokuwiki-plugin-radarchart
42. https://github.com/doobidoo/freesong-backup
43. https://github.com/doobidoo/Getting-and-Cleaning-Data
44. https://github.com/doobidoo/loveable
45. https://github.com/doobidoo/claude-voice-server
46. https://github.com/doobidoo/PerfectEQ
47. https://github.com/doobidoo/dokuwiki-plugin-knowledgegraph
48. https://github.com/doobidoo/vacationplaner
49. https://github.com/doobidoo/tinyclaw-docs
50. https://github.com/doobidoo/voice-mode
51. https://github.com/doobidoo/EarPlayer
52. https://github.com/doobidoo/mcplex
53. https://github.com/doobidoo/sse-test-worker

## Priority findings for ASTRA / AI Operating Memory / MCP integration

### P1 — mcp-memory-service

- Source: https://github.com/doobidoo/mcp-memory-service
- Current manifest version observed: `12.1.1`; Python `>=3.10`; Apache-2.0.
- README describes a self-hosted semantic memory service with REST API, MCP transport, OAuth 2.0/Dynamic Client Registration, CLI and dashboard. The repository describes shared persistent memory across agents and a knowledge graph/consolidation features.
- Its package dependency set is nontrivial (FastAPI, SQLite/SQLite-vec, OAuth/security, PDF processing, schedulers, etc.). Treat "zero cloud cost" as self-hosting/no required external API claim, not zero compute/storage cost.
- Best use: reference for ASTRA's long-lived project memory, remote MCP transport, and a memory-service boundary. Do not import wholesale until storage backend, default authentication, data deletion, backup/restore, upgrade migration, and resource footprint are audited.
- Remote MCP docs recommend Streamable HTTP and OAuth DCR for hosted clients; temporary Cloudflare tunnels change URL and are not a durable production endpoint.
- License is permissive Apache-2.0, subject to preserving notices.

### P1 — SHODH on Cloudflare

- Source: https://github.com/doobidoo/shodh-cloudflare
- License: MIT according to its LICENSE.
- Architecture: Cloudflare Workers API, D1 SQLite for memory content/metadata, Vectorize for semantic search, plus a Node.js MCP bridge.
- Its prerequisites document says the Cloudflare free tier is sufficient for typical personal use and lists D1/Workers/Vectorize quotas. These are maintainer-documented limits; verify current Cloudflare official limits before deploying or routing production data.
- Setup requires creating D1 and Vectorize resources, Wrangler authentication, a Worker deployment and an API key. This is a plausible no-upfront-cost hosted memory candidate only if the existing Cloudflare account is available and current quota/terms fit.
- Best use: low-cost distributed memory reference for ASTRA; do not claim deployed or connected.

### P2 — MCP-Context-Provider

- Source: https://github.com/doobidoo/MCP-Context-Provider
- Manifest version observed: `2.0.0-beta.3`; Node.js `>=20`; Apache-2.0.
- Describes persistent Contexts and confidence-scored Instincts with MCP tools and an optional bridge to mcp-memory-service.
- Status is explicitly beta/API stabilizing. The canonical repository URL in its package manifest is Codeberg: https://codeberg.org/doobidoo/MCP-Context-Provider.
- Best use: compare its static context vs learned-rule lifecycle against `salamou1944/agent-skills` and AI Operating Memory. Avoid creating a second overlapping memory/control plane without a measurable benefit.

### P2 — mcp-memory-service-rs

- Source: https://github.com/doobidoo/mcp-memory-service-rs
- Status explicitly M0 scaffold: boots over stdio MCP and opens the shared SQLite schema, but the README says core memory tools are still future M1–M3.
- License is PolyForm Noncommercial for noncommercial use; commercial use requires a separate commercial license. **Not eligible for a commercial revenue product without separate permission.**
- Decision: reference only; do not adopt into revenue-generating infrastructure.

### P3 — n8n-claude-memory-agent

- Source: https://github.com/doobidoo/n8n-claude-memory-agent
- README declares MIT and describes an n8n workflow joining Claude Code CLI, SSH and MCP Memory Service.
- This is a workflow example, not a replacement runtime or durable memory database. SSH private-key and CLI-account handling require security review before reuse.

### Deprecated / secondary

- `mcp-memory-dashboard` explicitly says deprecated and points to the main service's embedded dashboard.
- `claude-memory-context` is a local Claude Desktop project-knowledge implementation; its examples use machine-specific paths and should not be copied verbatim.
- The remaining enumerated repositories span utilities, music, dashboards, hardware and older personal projects; they remain indexed but are not yet deep-audited for current ASTRA/API Factory relevance.

## Downstream owner expansion

- `varun29ankuS/shodh-memory`: https://github.com/varun29ankuS/shodh-memory — upstream implementation referenced by SHODH on Cloudflare. README advertises Apache-2.0, local-first persistent memory, no required external API, and a single-binary path. Add `varun29ankuS` to the next account-level sweep.
- `doobidoo/MCP-Context-Provider` canonical upstream is hosted on Codeberg; record Codeberg as an additional source host for the same account, not a duplicate GitHub owner.
- Cloudflare is a deployment platform dependency for SHODH; Cloudflare owner/account sources are already in the master frontier.

## Reuse decision

- **Candidate to benchmark first:** mcp-memory-service, because its REST + MCP boundary and remote OAuth transport are the closest fit for multi-agent shared project memory.
- **Candidate for a free-tier remote prototype:** SHODH on Cloudflare, only after checking the existing Cloudflare account and current official quotas.
- **Do not use commercially without a separate license:** mcp-memory-service-rs.
- No source code was imported, no memory service was deployed, and no credentials were copied during this pass.

## Remaining work

1. Inspect actual storage backend defaults, backup/restore, deletion and security configuration in mcp-memory-service.
2. Compare the REST/MCP contracts with ASTRA/AI Operating Memory and existing MCP connections.
3. Enumerate `varun29ankuS` repositories and relevant SHODH source graph.
4. Continue the global owner frontier; enumeration alone is not deep-sweep completion.
