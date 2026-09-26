# WEEKLY TOP FIVE — 2026-09-26
Status: DISCOVERY_CAPTURED_PENDING_DEEP_VERIFICATION
Evidence window: latest attributable weekly-growth evidence located during this run (source snapshot dated 2026-09-23; fresh search on 2026-09-26 did not return a newer ranked weekly table).

## Selection
1. cloudflare/security-audit-skill — +15,381 stars in the cited weekly snapshot
2. alibaba/open-code-review — +12,590
3. affaan-m/ECC — +6,904
4. stablyai/orca — +6,205
5. Tencent/WeKnora — +5,303

## Provenance
- Primary weekly ranking snapshot: Git-Homed weekly top-100 page, last updated 2026-09-23.
- Secondary corroboration: TechTarget article published 2026-09-21, which independently highlighted Alibaba/open-code-review and Cloudflare/security-audit-skill as major weekly gainers.
- The ranking is a discovery signal only. Star counts may be noisy or artificially inflated; repository evidence is required before any VERIFIED status.

## Exact GitHub identity verification
- cloudflare/security-audit-skill — default branch main; README blob c80305c88cd5087db37f76a0d230c1fc092c864c; LICENSE blob 6dbc9ecb3a5b9080e95b962869e8c7ab16cfdc20; MIT.
  - Function: coding-agent security audit skill with reconnaissance, coverage-led hunting, candidate validation, structured findings, independent verification, and target-neutral reporting.
  - External dependencies/limits: agent runtime/orchestration is required; target-specific execution and model/runtime costs remain external.
- alibaba/open-code-review — default branch main; README blob 45618b0b4a0e4549e3fc3371cb5b075b225b5cc4; LICENSE blob 5db038258492ce47a5f3d27d78562c90d3f78331; Apache-2.0; package.json a9cf671cb2b5c1cc454f87e79c42c54abb5b6069; go.mod cf1d1266b1404c871d4a854e65f57502753181a0.
  - Function: AI-powered code review CLI; Node >=14 launcher with platform packages, Go 1.25.5 core; integrates Anthropic/OpenAI/AWS/MCP/OpenTelemetry.
  - External dependencies/limits: model-provider credentials and release artifact downloads are external; telemetry/configuration require review.
- affaan-m/ECC — default branch main; README blob 117552c2bc78b4ed5897eacec23a173b2b4e5e8e; LICENSE blob b832b6f642312312367c07688dc7426db40a82ed; MIT; package.json 6a53ed2f59df0a617d4311e91014c8ab3168d6c8.
  - Function: multi-harness agent operating system with skills, hooks, rules, MCP conventions, memory, control-plane patterns, and adapters for Codex/OpenCode/Cursor/Gemini/Claude Code.
  - External dependencies/limits: optional cloud model providers, GitHub App/website integrations, and local runtime tooling remain external.
- stablyai/orca — exact GitHub identity verified; deep file capture deferred to next batch because the run hit the connector call budget.
- Tencent/WeKnora — exact GitHub identity verified; deep file capture deferred to next batch because the run hit the connector call budget.

## Queue action
All five are permanent members of the continuous collection queue. Do not remove them due to overlap. Continue deep extraction next run for stablyai/orca and Tencent/WeKnora, then capture README/license/manifests, runtime, paid/cloud dependencies, security/operational limitations, maintenance state, and subscription-elimination value.

## Boundary
This weekly Top Five is separate from the total-star Top 10 queue. Do not merge the two rankings.
