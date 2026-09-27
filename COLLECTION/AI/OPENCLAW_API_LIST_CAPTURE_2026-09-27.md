# cporter202/openclaw-api-list — Capture 2026-09-27

## Source
- Repository: https://github.com/cporter202/openclaw-api-list
- Purpose: catalog of agent-callable APIs, MCP servers, integrations and automation endpoints for OpenClaw.
- Inspected: OPENCLAW_FOCUS.md and OPENCLAW_RECOMMENDED.md on 2026-09-27.
- Upstream currently exposes category directories including agents, AI, automation, integrations, developer tools, ecommerce, jobs, lead generation, MCP servers, news, open-source, SEO, social, travel and videos.

## Direct leverage for AI Operating Operator

### 1. API -> capability discovery
Use the catalog as a discovery index only. Each candidate must independently pass:
DISCOVERY -> source/docs -> exact license/terms -> cost/quota -> security/privacy -> adapter contract -> reachable runtime -> operation test -> independent verifier -> promotion.

### 2. OpenAPI -> MCP
The recommended list contains an OpenAPI-to-MCP converter. This is a high-leverage architecture pattern:
- accept a validated OpenAPI document;
- generate a bounded MCP tool surface;
- preserve schemas and operation IDs;
- attach explicit auth references without exposing secrets;
- require host/path allowlists;
- generate an independent verification contract.
Do not automatically expose every operation from an imported OpenAPI document.

### 3. MCP as a capability transport
MCP servers can become registered Operator capabilities rather than bespoke integrations. Preserve:
- server identity/version;
- tool schemas;
- required permissions;
- endpoint/process provenance;
- allowed operations;
- independent verification;
- timeout/retry/cancellation policy.

### 4. Free/self-hosted first
The catalog has an open-source category and many API entries. Prefer self-hosted/open-source or genuinely free endpoints before paid SaaS. Do not treat a catalog entry as proof of free pricing, reliability, legality, geography, or production availability.

### 5. Useful candidate families for current Operator
- Search/research
- browser automation
- documents and conversion
- developer/API documentation
- MCP registries/servers
- webhooks/automation
- CRM/support
- ecommerce
- analytics/SEO
- video/transcript extraction
These should be promoted only when a concrete capability gap exists.

## Important provenance/risk note
The curated entries heavily link to Apify actors and include affiliate-style referral parameters. The repository therefore remains useful as a discovery catalog, but links must not be treated as neutral vendor recommendations or proof of underlying API ownership. Inspect the underlying provider independently before integration.

## Decision
Status: VERIFIED_SOURCE_CAPTURED; PERMANENT_DISCOVERY_SOURCE.

No mass import. Extract only candidates that close a demonstrated Operator/EASY/MONY/Salamou-31/ASTRA capability gap.
