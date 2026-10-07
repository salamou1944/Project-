# Agent Sandbox Lifecycle Contract — 2026-10-07

Status: EXTRACTED / MERGE-UPGRADE CANDIDATE

Source:
- https://github.com/agent-sandbox/agent-sandbox
- Revision evidence: 6f7b273ea80732b063d1d1a914b7138780fa83a0
- License: Apache-2.0

## Contract
Provide an isolated, stateful execution boundary for an agent where sandbox lifecycle is explicit and independently observable.

### Required lifecycle
CREATE -> READY -> EXECUTE -> OBSERVE -> PAUSE/RESUME or SNAPSHOT -> CLEANUP

### Required controls
- Per-agent/per-user isolation.
- Explicit resource/template selection.
- Bounded idle/lifetime reclamation.
- Pause/resume without losing intended state.
- Snapshot/restore semantics for resumable work.
- Optional pre-warmed pool for latency-sensitive allocation.
- Explicit cleanup and deletion.
- Events/metrics/logs for independent verification.
- API/MCP/SDK boundary so the agent does not require direct cluster administration.

### Compatibility leverage
Where an E2B-compatible interface already exists, keep the agent-facing contract stable while replacing the backend with a self-hosted runtime.

### Evidence gate
A successful sandbox-create response is not proof of isolation or restored state. Verification must inspect:
1. sandbox identity,
2. tenant/agent ownership,
3. resource limits,
4. execution result,
5. persisted/restored state,
6. cleanup result,
7. event/log evidence.

## Merge decision
This is not a new generic sandbox capability. It is a concrete lifecycle contract that strengthens existing COLLECTION/OpenShell/CUA/AI Operating execution-boundary material.
