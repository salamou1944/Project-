# COLLECTION — xihongshichaojidan8 — 2026-10-04

Source: https://github.com/xihongshichaojidan8

## Public repository inventory
Current owner-scoped GitHub repository search returned 5 repositories:
1. agentscope-java
2. deer-flow
3. first_test
4. claude-code
5. feng-ge-skill

agentscope-java and deer-flow are the highest-priority technical sources. first_test did not expose a README through the connector and remains unverified beyond discovery.

## High-value findings

### agentscope-java
AgentScope Java 2.0 is an enterprise/distributed agent framework. README documents:
- 31 typed events for real-time rendering and human-in-the-loop.
- Permission gating: allow / require user approval / deny.
- Middleware around the reasoning/acting loop.
- Isolated workspace/sandbox support across local, Docker, Kubernetes and cloud sandbox paths.
- Multi-agent orchestration with subagent spawning/sending and event forwarding.
- Distributed session and memory management with cross-replica recovery.
- Agent observability/auditing, evaluation/experimentation and asset optimization.
- v2 also documents async tools, scheduled wakeups, subagent routing/session recovery, A2A and AG-UI support.

Priority comparison: Elite event/evidence contract, permission gates, long-running execution, distributed recovery, subagent orchestration, and human-in-the-loop controls.

### deer-flow
DeerFlow 2.0 is an open-source super-agent harness built around sub-agents, memory, sandboxes and extensible skills.
README documents:
- subagents and skills/tools
- sandbox and filesystem
- context engineering
- long-term memory
- scheduled tasks
- terminal workbench
- MCP server and multiple model providers
- request-admission controls for provider RPM limits
- real demos / case studies through the project website

Priority comparison: existing Elite/ASTRA/agent-skills architecture, especially skills, memory, scheduling, context compaction, sandboxing and evidence-backed execution.

### claude-code
This repository is a Python porting workspace, not an official Anthropic repository. README explicitly states it is not affiliated with Anthropic and that the exposed snapshot is no longer the tracked source tree. Current focus is Python port metadata, CLI summaries and tests.

Priority: architecture/reference only; do not treat it as official Claude Code source or as a production replacement.

### feng-ge-skill
A MIT skills.sh-compatible personality/analysis skill distilled from public material. It demonstrates a source-backed persona skill with explicit research files and an honesty-boundary section. This is more relevant to skill provenance/content architecture than to the core agent runtime.

### first_test
Repository discovered, but README fetch returned 404 through the connected GitHub interface. Treat as unverified until contents are directly inspected.

## Immediate leverage order
1. AgentScope Java event + permission + middleware model.
2. DeerFlow skills + memory + scheduling + sandbox/context model.
3. Compare both against existing agent-skills/Elite before implementing anything.
4. Preserve claude-code only as a non-official Python porting reference.
5. Inspect feng-ge-skill only for provenance-aware skill packaging patterns.

## Verification boundary
README claims are upstream claims until independently reproduced. Do not copy code or architecture wholesale where existing COLLECTION sources already cover the capability. Preserve licenses, versions and source provenance before adoption.
