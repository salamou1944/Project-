# Account-wide source capture — mnfst — 2026-10-16

Status: ACCOUNT_ENUMERATED; RELEVANT_REPOSITORIES_REVIEWED; SELECTED_CANDIDATES_NEED_DEEPER_VERIFICATION
Owner: https://github.com/mnfst
Discovery path: `mnfst/awesome-free-llm-apis` → owner-wide expansion rule
Method: GitHub repository search for `user:mnfst`, page 1 at 100/page returned 25 repositories; page 2 returned 0. Date: 2026-10-16.
Scope limit: repository names were enumerated; README-level triage was performed for the existing free-API source and the relevant model-parameter, deprecation, gateway, autofix, SDK, MCP-generator and agent-integration projects. This is not a claim that all source files, releases, issues or workflows across all 25 repositories were exhaustively audited.

## Enumerated public repositories

1. https://github.com/mnfst/awesome-free-llm-apis
2. https://github.com/mnfst/llm-gateway
3. https://github.com/mnfst/manifest-ui
4. https://github.com/mnfst/manifest-baas
5. https://github.com/mnfst/modelparams.dev
6. https://github.com/mnfst/startup-info
7. https://github.com/mnfst/mcp-server-generator
8. https://github.com/mnfst/wordpress-agentic-ui-generator
9. https://github.com/mnfst/vc-info
10. https://github.com/mnfst/openclaw-model-router
11. https://github.com/mnfst/autofix
12. https://github.com/mnfst/wingman
13. https://github.com/mnfst/docs
14. https://github.com/mnfst/docs-baas
15. https://github.com/mnfst/website-baas
16. https://github.com/mnfst/modeldeprecations.dev
17. https://github.com/mnfst/vscode-theme-manifest
18. https://github.com/mnfst/manifest-php
19. https://github.com/mnfst/mistral-vibe
20. https://github.com/mnfst/.github
21. https://github.com/mnfst/playground-wrapper
22. https://github.com/mnfst/manifest-hermes
23. https://github.com/mnfst/manifest-node
24. https://github.com/mnfst/mintlify-docs
25. https://github.com/mnfst/manifest-python

## Highest-value candidates for Salamou-31 / API Factory

### P1 — modelparams.dev

- Source: https://github.com/mnfst/modelparams.dev
- README describes a community-maintained model/API-parameter catalog, TypeScript and Python packages, request validation, model lifecycle metadata, and an MCP server.
- License: MIT according to repository README.
- Potential use: prevent invalid model/provider parameters before making a billable request; compare its catalog/schema against the existing API Factory validation boundary.
- Boundary: hosted catalog/API and package data can become stale; validate source freshness and pin/version the data before relying on it for production decisions.
- Decision: benchmark/adapt the schema or validator only if it materially exceeds the existing provider boundary. Do not add a second routing plane.

### P1 — modeldeprecations.dev

- Source: https://github.com/mnfst/modeldeprecations.dev
- README describes a model deprecation/shutdown/replacement catalog, public JSON API, schemas, and date-stamped provider documentation.
- License: MIT according to repository README.
- Potential use: model lifecycle checks in provider selection and stale-model prevention.
- Boundary: verify dates against the underlying provider documentation before an automatic routing or migration decision.
- Decision: use as a reference/feed candidate; no dependency added.

### P1 — autofix

- Source: https://github.com/mnfst/autofix
- License: MIT according to repository README.
- README describes repair/retry for invalid LLM parameters and deprecated models. It states the heal API receives settings, not prompt data.
- Potential use: recover from provider HTTP 400/model-parameter errors without introducing another gateway.
- Risks/gates: independently inspect privacy contract and retry semantics; preserve provider choice, reject silent paid fallback, avoid unsafe retry behavior, and test only against a controlled fixture first.
- Decision: isolated benchmark candidate, not yet integrated.

### P2 — llm-gateway

- Source: https://github.com/mnfst/llm-gateway
- License: MIT according to repository README; Docker self-hosting documented.
- Capability: OpenAI-compatible gateway, routing/fallback, spend controls, and self-healing.
- Boundary: overlaps the existing Salamou-31/API Factory provider boundary and LiteLLM/OmniRoute. README advertises full-body logs, which requires explicit payload-privacy review.
- Decision: reference only; reject wholesale adoption.

### P2 — manifest-node / manifest-python / manifest-php

- Sources: https://github.com/mnfst/manifest-node, https://github.com/mnfst/manifest-python, https://github.com/mnfst/manifest-php
- Capability: API observability and repair SDKs.
- Boundary: README says request metadata is reported and failed requests may be sent in full for repair. This is a material data-exposure/cloud-dependency boundary.
- Decision: do not add to sensitive paths without a privacy review and explicit allow/deny policy.

### P3 / reject for production now

- `mcp-server-generator`: README explicitly labels it Work In Progress/non-verified and says not to use in production; documented feature table still marks access-control/authentication and self-hosted Docker capabilities incomplete.
- `manifest-baas`: README says pivot in progress; not a stable backend choice for this work.
- `openclaw-model-router`: OpenClaw-specific routing setup; duplicates the existing provider-routing surface and is not an API Factory replacement.
- `wingman`: useful LLM API client for manual testing, not a hosting/runtime solution.
- `manifest-ui`: UI component library, not a backend/deployment replacement.
- `manifest-hermes`: Hermes-specific integration; only relevant if Hermes becomes an explicit target.
- `startup-info`, `vc-info`: MIT agent skills for startup/VC research; possible GTM research assets, not runtime blockers.
- `wordpress-agentic-ui-generator`, `docs`, `docs-baas`, `website-baas`, `vscode-theme-manifest`, `mistral-vibe`, `.github`, `playground-wrapper`, `mintlify-docs`: secondary to the current API Factory / free-provider work; not yet deeply audited.

## Upstream refresh delta — awesome-free-llm-apis

- Captured upstream repository revision: `cf97c32fec1b2e96e9936746e2731a81bd5ea33f`, repository metadata updated at `2026-10-16T02:34:29Z`.
- Previous extracted revision: `b25c0395fe1e7628ecc99bf119a40365801c6fb4`, generated `2026-10-10T05:55:37Z`.
- Both extraction records contain 15 tracked files; the current extraction reports zero fetch errors and no tracked file-content differences against the prior extracted snapshot.
- Upstream `data.json` itself reports `lastUpdated: 2026-10-05`. A newer repository timestamp is not evidence of a newer provider quota audit.
- Existing free-API source remains `DISCOVERY_CAPTURED`; no provider is promoted to verified/production-ready from this list alone.

## Next actions

1. Compare `modelparams.dev` and `modeldeprecations.dev` against existing API Factory schema/model-selection code and keep only non-duplicative fields.
2. Read the full `autofix` privacy/contract and test a narrow, no-paid-fallback fixture.
3. Continue owner-wide expansion for the next high-priority account from `COLLECTION/INDEX.md`; preserve each repository and account's provenance.
4. Do not mark the overall Collection complete: the wider account graph and remaining production verification work are still open.
