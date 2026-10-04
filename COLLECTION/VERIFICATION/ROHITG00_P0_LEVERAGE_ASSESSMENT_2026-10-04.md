# ROHITG00 — P0 LEVERAGE ASSESSMENT — 2026-10-04

Status: FILE-LEVEL INSPECTION COMPLETE FOR P0 SET
Account: https://github.com/rohitg00
Scope: agentmemory, pro-workflow, skillkit, agentbrain, ai-engineering-from-scratch

## Evidence boundary

This document records only inspected public repository content. Repository discovery is not treated as production proof. Claims below are source-derived and must be validated again before promoting code into production.

## P0 findings

### 1. agentmemory
Source: https://github.com/rohitg00/agentmemory
License: Apache-2.0
Inspected: README.md
Key mechanisms:
- persistent memory server for multiple coding-agent runtimes
- BM25 + vector + graph retrieval with provenance/lifecycle concepts
- automatic capture through hooks
- MCP + REST interfaces
- local/keyless operation with BM25; optional local embeddings
- replay/import of agent sessions
- local viewer and explicit health/status probes
- documented restart-persistence verification path

Leverage target:
AI_operating_memory / Elite persistent learning.

Important constraint:
Do not copy its runtime wholesale before dependency, license, data-layout, and integration-boundary review. Prefer extracting neutral interfaces and evidence patterns.

### 2. pro-workflow
Source: https://github.com/rohitg00/pro-workflow
License: MIT (README badge and repository license)
Inspected: README.md
Key mechanisms:
- self-correction loop
- SQLite + FTS5 durable learning store
- persistent research wiki
- budget-capped auto-research
- Research -> Plan -> Implement -> Review gates
- parallel worktrees and agent teams
- deterministic git/secret/destructive-operation guards
- compaction-aware state
- cost tracking and MCP audit
- 22 hook events and cross-agent skill distribution

Leverage target:
Salamou-31 execution loop, Elite/ARMY-14 correction capture, and COLLECTION research/evidence lifecycle.

Important constraint:
Budget-capped research and LLM-backed hooks must remain fail-closed and must never invent evidence.

### 3. skillkit
Source: https://github.com/rohitg00/skillkit
License: Apache-2.0
Inspected: README.md and LICENSE
Key mechanisms:
- portable skill package/distribution model
- translation between agent-specific skill formats
- 40+ agent-host adapters
- repository-aware skill recommendations
- REST/MCP runtime discovery
- local installation path and optional components

Leverage target:
agent-skills control plane and future cross-runtime skill normalization.

Important constraint:
Treat external skill sources as untrusted inputs; scan/validate before installation or promotion.

### 4. agentbrain
Source: https://github.com/rohitg00/agentbrain
License: MIT (repository metadata)
Inspected: AGENTBRAIN.md, PRINCIPLES.md, docs/state-machine.md, README.md
Key mechanisms:
- explicit lifecycle state machine: intake -> research -> grill -> brief -> design -> plan -> build -> verify -> review -> ship -> learn
- evidence-before-confidence
- non-agent alternative review
- explicit approval gates for destructive/financial/credential/privacy/production actions
- artifact contracts and exit criteria per state
- mandatory verification evidence
- targeted exact-name scrub for public-copy changes
- harness-effect gate for tool-output presentation parity

Leverage target:
Elite/ARMY-14 control-plane governance and the current SOAT/API Factory execution lifecycle.

Highest-value immediate pattern:
State + required artifact + exit criteria + evidence gate, instead of relying on a single global prompt.

### 5. ai-engineering-from-scratch
Source: https://github.com/rohitg00/ai-engineering-from-scratch
License: MIT
Inspected: README.md
Key mechanisms:
- 523 lessons / 20 phases
- reusable prompts, skills, agents, and MCP artifacts
- agent engineering, MCP, Agent Skills, product judgment and delivery paths
- explicit evidence discipline for lessons: command, working directory, exit code, output, artifact
- production-oriented learning paths

Leverage target:
Source of implementation patterns and reusable artifacts, not a runtime dependency.

## Cross-project synthesis

The strongest non-duplicative combination is:

COLLECTION source
-> evidence-backed research
-> explicit lifecycle state
-> durable selective memory
-> correction capture
-> skill normalization
-> implementation
-> verification artifact
-> review/ship gate
-> learning capture

Recommended ownership boundaries:
- Project-/COLLECTION: provenance, source captures, leverage assessments, verification records.
- AI_operating_memory: durable facts, corrections, reusable procedures.
- agent-skills: portable skills and execution procedures.
- Salamou-31: API Factory/runtime execution and production-facing evidence.
- Elite/ARMY-14: decision/control/governance layer.

## Immediate implementation candidates

P0-A: Add an explicit state/exit/evidence contract to the SOAT/API Factory execution path.
P0-B: Add selective correction capture to AI_operating_memory; do not persist transient chatter.
P0-C: Add a portable skill normalization contract in agent-skills.
P0-D: Require evidence artifact presence before a project can advance from verify -> review -> ship.
P0-E: Preserve tool-output/citation parity when retrieved evidence is surfaced through different presentation modes.

## Non-goals

- No blind copying of external frameworks.
- No production claim based on README claims.
- No new paid dependency.
- No credentials copied into collection.
- No replacement of existing working components merely for architectural similarity.

## Next verification queue

1. Inspect P1 repositories: rimuru, kubectl-mcp-server, ai_computer_use, agentgateway, github-mcp-server, mcp-agent, browser-tools-mcp.
2. Resolve downstream owner accounts from the P0/P1 dependency graph.
3. Compare P0 patterns against current Salamou-31 SOAT failures and existing evidence contracts.
4. Promote only the smallest tested slice into the owning repository.
