# OpenClaw API List — Operational Capture (2026-09-27)

Source: cporter202/openclaw-api-list
Revision inspected/pinned: 3afa19dd12f3cdc6bc2e297e9b6945059ada0cae
Purpose: discovery source for the AI Operating Operator, not an execution trust boundary.

## Verified source structure
- Curated OpenClaw list: ~100 APIs in OPENCLAW_RECOMMENDED.md.
- Operator category coverage: recommended, MCP, integrations, automation, open-source, agents, AI, developer tools, ecommerce, jobs, lead generation, news, SEO, social, travel, videos, other.
- Categories include MCP servers, integrations, automation, AI, agents, travel, jobs, news, ecommerce, lead generation, social media, SEO, videos, and open-source.
- Focus document states that APIs are intended to be callable by skills, MCP-compatible, webhook-friendly, or integration-ready.
- MCP is identified as a first-class integration path.
- The repository also contains large category catalogs; entries may be third-party/paid and require separate terms, quota, privacy, geography, and license review.

## High-value operator use
1. API discovery: search the catalog before inventing a provider/integration.
2. MCP discovery: identify candidate tool servers for research, documents, browser, productivity, CRM, and automation.
3. Free/self-hosted filtering: prefer candidates that can be run without a paid subscription when a real capability gap exists.
4. Promotion gate: catalog presence is DISCOVERY only; executable capability requires adapter, authorization, reachability, operation test, and independent verification.
5. Security: never import catalog credentials, bypass controls, solve CAPTCHA/MFA, or execute a third-party API solely because it is listed.

## Operator integration
Implemented in salamou1944/agent-skills:
- capability: research.api_catalog
- adapter: apps/ai-operating-operator/adapters/api-catalog-adapter.mjs
- actions: health, search, category
- authorization: explicit task action api_catalog_read
- source restricted to the pinned raw.githubusercontent.com/cporter202/openclaw-api-list revision
- independent verifier: api-catalog-independent-verifier-v1
- self-test includes live catalog retrieval, pinned-revision provenance, structured provider URLs, AI/Agents category coverage, and authorization denial.

## Verified live use
The operator self-test retrieves OPENCLAW_RECOMMENDED.md from the pinned source revision and searches for "MCP"; it also checks AI and Agents category coverage.
Observed 5 results:
- Brave Search MCP Server
- Google Search MCP Server
- Tavily MCP Server
- Exa MCP Server
- Firecrawl MCP Server
The response is independently verified with status 200, executionId, and matching sourceRevision.

## Status
DISCOVERY SOURCE -> ADAPTER_READY -> TESTED (pinned, bounded, read-only catalog discovery).
This capture does not promote any listed third-party API to HUMAN_READY. Each future provider must pass its own license/terms, cost/quota, security, reachability, operation, and independent-verification gates.
