# Agent Zero — Capture 2026-09-27

## Source
- Repository: https://github.com/agent0ai/agent-zero
- Inspected revision: e3051fb584b1a36be2b0a0c90606f1c2c2d356ec
- Repository default branch: main
- Upstream description: Agent Zero AI framework
- Language: Python
- GitHub license metadata: Other / NOASSERTION. Do not assume a permissive license for code reuse; perform exact license/terms review before copying code.

## Why it matters to AI Operating Operator
Agent Zero exposes several patterns that directly complement the Operator:
1. Dockerized Linux desktop and browser as a computer-use surface.
2. Browser DOM annotation and screenshot/history concepts for UI inspection.
3. Projects with isolated files, instructions, memory, secrets, repositories and model presets.
4. Skills, plugins, MCP and A2A extension points.
5. Multi-agent delegation to focused subagents.
6. Time Travel: workspace snapshots, diff, preview, travel and revert.
7. Host-machine bridge with explicit access, reinforcing the need for explicit workspace boundaries.

## Highest-value extraction
### A. Workspace isolation
Adopt the invariant that every execution has an explicit project/workspace identity and that filesystem mutations are restricted to an approved root. Never inherit access merely because a tool is discoverable.

### B. Recoverability
Use the Time Travel design as a reference for a bounded workspace-recovery layer:
- snapshot before/after mutation boundaries;
- inspect diff before destructive restore;
- preserve metadata such as task/context/project/trigger/timestamp;
- keep recovery storage separate from the managed workspace;
- reject paths outside the managed workspace root;
- exclude secrets and runtime caches from snapshots.

### C. Computer-use layering
Use Agent Zero as a complementary source to Cua/Browser Use:
- Browser = structured web surface;
- Cua = native desktop surface;
- Agent Zero = Linux workspace/desktop architecture and recovery patterns.
Do not collapse these into one unrestricted capability.

### D. Multi-agent delegation
Extract the architectural pattern only:
planner/supervisor -> focused subagent -> report -> independent verification.
Subagents must not inherit evidence or permissions automatically.

## Security constraints for promotion
- No unrestricted host filesystem access.
- No credential extraction or secret harvesting.
- No MFA/CAPTCHA/RBAC bypass.
- No hidden persistence.
- Project/workspace allowlist required.
- Snapshot/revert must be fail-closed outside the managed root.
- Secrets such as .env, credentials and private memory must not enter recovery snapshots.
- External capabilities remain blocked until runtime reachability and independent verification are proven.

## Promotion path
DISCOVERY -> source inspection -> exact license/terms review -> design extraction -> adapter/contract -> local regression -> runtime test -> independent verification -> HUMAN_READY.

## Current decision
Status: VERIFIED_SOURCE_CAPTURED; ARCHITECTURE_PATTERNS_SELECTED; NOT_YET_INTEGRATED_AS_AGENT_ZERO_RUNTIME.

Immediate Operator leverage:
- strengthen project/workspace isolation;
- add bounded workspace recovery/snapshot capability where it is demonstrably useful;
- use Agent Zero's multi-agent pattern only behind existing Operator evidence/permission gates;
- keep Cua and Browser adapters as separate capabilities.

## Evidence inspected
- README.md
- plugins/_time_travel/AGENTS.md
- plugins/_time_travel/helpers/time_travel.py
