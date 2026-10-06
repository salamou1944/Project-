# TesterArmy Account Capture — 2026-10-07

## Source
- Account: https://github.com/tester-army
- Type: GitHub organization
- Capture date: 2026-10-07
- Enumeration status: CURRENT PASS ENUMERATED
- Public repositories found: 7

## Public repository inventory

| Repository | Priority | Collection assessment |
|---|---:|---|
| tester-army/e2e | P0 | High-value agentic E2E testing: natural-language agent actions, assertions, replay, web/mobile engines, model-provider neutrality |
| tester-army/scout | P0 | High-value API verification: OpenAPI-driven testing, host lock, mutation gate, budgets, rate limits, redaction, findings, coverage and CI gates |
| tester-army/cli | P1 | CLI, Agent Skill installation, hosted MCP integration and cloud test execution |
| tester-army/unbox-ai | P1 | AI trace inspection, token/cost/latency/tool analysis, A/B comparison, trajectory comparison, bounded read-only agent interface |
| tester-army/mobile-github-action | P1 | GitHub Actions integration for mobile app upload/testing and dynamic PR-agent execution |
| tester-army/mobile-example | P2 | Mobile integration/example source; inspect when extracting concrete patterns |
| tester-army/.github | P3 | Organization/community metadata; retain for provenance, not as a primary capability source |

## High-value extraction

### e2e
- Natural-language agent action followed by explicit assertions.
- Records/replays agent steps so later runs can avoid model calls until the application changes.
- Web and mobile execution.
- Browser/mobile engine abstraction.
- GitHub reporting.
- Decision-model package for bounded semantic actions/assertions.
- Apache-2.0 according to repository README.

### scout
- OpenAPI-driven API execution and realistic user-flow testing.
- Host-locking to prevent requests escaping the authorized target.
- Mutations blocked by default; explicit opt-in required.
- Method/path restrictions, rate limits and request budgets.
- Credential resolution from environment and output redaction.
- Multiple authentication profiles and tenant-isolation testing.
- Structured findings with confirm/dismiss lifecycle.
- Coverage and CI gates.
- Explicit distinction between candidate findings and verified findings.
- MIT according to repository README.

### cli
- Agent Skill installation path.
- TesterArmy hosted MCP server integration.
- JSON-first CLI suitable for coding agents.
- Cloud run queueing plus explicit distinction between queued and completed execution.
- MIT according to repository README.

### unbox-ai
- Read-only, bounded agent trace exploration.
- Token/cost/latency/tool-call analysis.
- Prompt/tool-set diffs.
- A/B run comparison and content-aligned trajectory comparison.
- Machine-readable JSON output.
- Trace adapters as an extensibility pattern.
- MIT according to repository README.

### mobile-github-action
- GitHub Actions upload → test → optional dynamic PR agent → cleanup flow.
- Explicit split-job model for parallel defined tests and dynamic agent execution.
- MIT according to repository README.

## Integration / dedupe boundary

Do NOT wholesale import TesterArmy.

Compare extracted patterns against:
- SOAT
- agent-skills
- Elite / ARMY-14
- AI Operating Memory
- ASTRA
- COLLECTION verification/evidence contracts

Expected strongest upgrades:
1. SOAT: API authorization boundaries, mutation gates, request budgets, structured findings, coverage/CI gates.
2. SOAT + Elite/ARMY-14: agent action → observation → assertion → replay contracts.
3. AI Operating Memory: bounded trace/cost/tool trajectory evidence.
4. GitHub control plane: reusable mobile CI/action integration patterns.

## Verification boundary

Repository inspection establishes source evidence only. It does not establish that these components are integrated or production-proven in our systems.

Any promoted capability must retain:
- source repository and revision
- license boundary
- implementation path
- adapter/contract boundary
- tests
- runtime/reachability evidence where applicable
- independent verification result

## Account expansion rule

This account must be re-enumerated in future collection passes. Any newly appearing public repository is automatically added to the inventory and inspected under the same account-wide expansion rule.

## Current decision

KEEP IN COLLECTION.

Priority: P0/P1 source account.

Reuse strategy: extract narrow Skills/contracts and upgrade existing systems after semantic dedupe; preserve TesterArmy provenance even when functionality overlaps.
