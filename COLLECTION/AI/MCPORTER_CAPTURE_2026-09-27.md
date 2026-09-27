# openclaw/mcporter — Capture 2026-09-27

## Source
- Repository: https://github.com/openclaw/mcporter
- Revision inspected: current main on 2026-09-27.
- License: MIT (repository metadata and README).
- Purpose: TypeScript runtime/CLI for discovering and calling MCP servers.

## High-value leverage for AI Operating Operator
1. MCP capability transport: discover tools, inspect schemas, call tools, and read resources through a common protocol boundary instead of building one adapter per service.
2. Explicit server definitions: support HTTP and stdio MCP servers while keeping endpoint/process configuration explicit.
3. Reproducibility: record/replay MCP sessions is a useful evidence and regression pattern.
4. Typed surfaces: generated TypeScript clients/CLIs can preserve tool schemas and reduce ad-hoc invocation.
5. Config provenance: import existing MCP client configurations, but the Operator must not silently inherit credentials or permissions.
6. Fail-closed auth: OAuth/interactive requests must remain explicit; headless execution should decline interactive elicitation rather than bypassing it.

## Integration decision
- Status: VERIFIED_SOURCE_CAPTURED; ARCHITECTURE_SOURCE.
- Do not copy the entire runtime.
- Prefer a bounded MCP adapter/gateway only after the Operator has:
  - explicit server allowlist;
  - tool allowlist;
  - per-task authorization;
  - schema validation;
  - timeout/cancellation;
  - secret redaction;
  - execution/evidence IDs;
  - independent verification;
  - record/replay fixtures.
- The existing OpenAPI-to-MCP adapter remains generation/inspection only; it does not claim to execute MCP tools.

## Relationship to cporter202/openclaw-api-list
The catalog identifies MCP servers and OpenAPI-to-MCP as discovery paths. MCPorter supplies a concrete MIT-licensed implementation pattern for the transport/runtime boundary. Provider-specific licensing, quotas, privacy, and authorization remain separate gates.

## Safety boundary
Never import credentials from OpenClaw/MCP client configuration automatically. Never use MCP to bypass MFA/CAPTCHA/RBAC, extract secrets, or expand beyond the task/resource allowlist.
