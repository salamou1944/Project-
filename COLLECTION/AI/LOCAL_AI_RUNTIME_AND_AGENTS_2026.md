# Local AI Runtime / Agent Expansion — 2026-09-25

Status: DISCOVERY_CAPTURED

## High-value discovery candidates

### LocalAI
- URL: https://github.com/mudler/LocalAI
- Capability: local AI engine covering LLM, vision, voice, image and video workloads.
- Observed 2026 release notes: 4.x adds distributed/cluster features, OpenAI-compatible APIs, multimodal capabilities, agentic orchestration and additional backends.
- Potential value: one self-hosted multimodal control point instead of multiple hosted APIs.
- Verification required: current release, backend support, model licenses, hardware requirements, security and production topology.

### SOMI
- URL: https://github.com/Somi-Project/Somi
- Capability: local-first AI agent framework/workstation with memory, research, coding, OCR, speech, automation and tool/skill system.
- Claims fully self-hosted via Ollama and local operation.
- Potential value: integrated local operator stack and architecture patterns.
- Verification required: repository structure, license, dependencies, supported hardware and actual offline paths.

### LibrAgent
- URL: https://github.com/fritzprix/libr-agent
- Capability: local-first desktop agent with file access, shell, browser automation, MCP and multi-agent workflows.
- Supports local runtimes such as Ollama.
- Verification required: license, sandbox/security boundaries and current runtime maturity.

### Pan-Agent
- URL: https://github.com/Euraika-Labs/pan-agent
- Capability: self-hosted desktop agent, PC control, browser, persistent memory, bots and HTTP API.
- Observed architecture: Go binary + Tauri desktop app.
- Security claim includes approval patterns for dangerous commands.
- Verification required: threat model, permission model, license, dependencies and actual isolation.

### Pernix
- URL: https://github.com/calvincs/Pernix
- Capability: self-hosted agent server with persistent memory, tool execution, web UI and REST API.
- Important limitation explicitly observed: executes shell commands/writes files and README warns it is not production software.
- Potential value: research/reference architecture only until hardened and independently verified.

## Discovery index
- https://github.com/Supersynergy/awesome-local-ai-agents
- Local model/runtime families surfaced: Ollama, llama.cpp, vLLM, Jan, GPT4All, LM Studio.
- Treat model availability and model-license terms separately from software license.

## Status rule
None of the above is VERIFIED solely by discovery. Preserve as candidates and inspect source/docs before adoption.
