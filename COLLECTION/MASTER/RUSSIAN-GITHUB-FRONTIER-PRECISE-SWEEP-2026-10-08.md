# RUSSIAN GITHUB FRONTIER — PRECISE HIGH-VALUE ACCOUNT SWEEP — 2026-10-08

## Scope
This sweep is **not AI/MCP-only**. It targets Russian-origin / Russia-based technical accounts across databases, developer tooling, infrastructure, observability, compilers, cloud, security, data, payments, automation, and agentic tooling.

Discovery rule:
**strong project → owner → all public repositories → valuable repos/components → downstream owners → repeat**

Russian origin is a discovery signal, not a quality verdict. Every candidate remains subject to provenance, license, activity, architecture, and reuse-value checks.

## Newly captured high-value accounts

| Account | Public repos observed | Why it matters | Classification |
|---|---:|---|---|
| ClickHouse | 381 | OLAP/database, connectors, operators, observability, agent/AI integrations, benchmarks and infrastructure | Russian-origin, now global |
| ydb-platform | 142 | Distributed SQL, SDKs, operators, connectors, CDC, MCP/AI skills, observability and tooling | Russian-origin / Yandex lineage |
| VKCOM | 134 | PHP compiler, distributed compiler, observability/TSDB, Kubernetes tooling, SDKs, networking and media | Russia-based |
| MAILRU | 65 | Go serialization, database tooling, Tarantool ecosystem, queues, streaming and infra utilities | Russia-based / VK lineage |
| JetBrains | 600 observed in current search | Kotlin, IntelliJ platform, compilers, static analysis, Qodana, TeamCity tooling, MCP/agent tooling, databases | Russian-origin/global |

## Highest-priority extraction frontier

### P0 — deep inspect first
1. ClickHouse/ClickHouse — core analytical DB architecture and operational patterns.
2. ydb-platform/ydb — distributed SQL / consistency / transactions.
3. ydb-platform/ydb-mcp — database ↔ agent boundary.
4. ydb-platform/ydb-ai-skills — reusable Skill patterns.
5. VKCOM/kphp — compiler/runtime engineering.
6. VKCOM/nocc — distributed compilation.
7. VKCOM/statshouse — high-scale observability/metrics.
8. VKCOM/vkompose — infrastructure/Kubernetes patterns.
9. MAILRU/easyjson — high-performance serialization.
10. MAILRU/dbr — database abstraction/tooling.
11. MAILRU/tarantool-authman — auth/security component.
12. MAILRU/surgemq — messaging/streaming.
13. JetBrains/koog — agent framework surface.
14. JetBrains/Qodana — code quality/security/static analysis.
15. JetBrains/youtrackdb — database/storage implementation.
16. JetBrains/mcp-server-plugin — IDE/MCP integration.
17. JetBrains/kotlin — language/compiler/toolchain.
18. JetBrains/intellij-community — IDE platform architecture.

## Red-line dedupe
Before extracting any candidate into Skills, Salamou-31, SOAT, Elite/ARMY-14, or other project infrastructure:
- compare against existing Collection capability groups;
- compare against canonical agent-skills;
- compare against existing API Factory / SOAT / runtime mechanisms;
- if the capability already exists, **do not reimplement it**;
- upgrade the existing contract only when the Russian source provides a genuinely new mechanism, stronger implementation, better evidence, or missing domain coverage.

## Important boundary
Account capture ≠ source extraction ≠ integration ≠ runtime proof.
No account/repository is marked READY_TO_USE or PRODUCTION_PROVEN merely because it is high-value.

## Next account expansion
The next sweep should follow the owners/contributors/dependencies discovered inside the P0 repositories, then enumerate those owners' full public repositories. Continue until the frontier stops producing high-value new owners, not merely until a fixed number of repos is found.
