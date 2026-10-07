# CodeCraft API — Collection Capture — 2026-10-07

Source: https://codecraftapi.com

## Classification
- Category: AI API / OpenAI-compatible gateway
- State: ADAPTABLE
- Priority: HIGH
- Primary leverage: low-cost model/provider option for PASTEL Host intelligence and other provider-neutral AI adapters.

## Captured capability
- OpenAI-compatible API surface.
- Candidate use cases: chat/reasoning, tool calling, vision and streaming.
- Intended architecture: provider adapter, not application-specific coupling.

## Safety / operational boundary
- Credentials must remain server-side.
- Do not commit API keys.
- Do not expose provider credentials in browser code.
- Free-tier/quota and model availability must be verified live before promotion to READY.

## Downstream candidates
1. PASTEL Host intelligence
2. AI Operating / capability broker
3. Elite / ARMY-14 provider routing
4. Salamou-31 AI API Hub / API Factory

## Evidence status
Resource captured from the official site. Live production verification of quota, model availability and tool-calling is still required.

## Downstream implementation evidence found
A public third-party client, AIM-IT4/craftcode-CLI, implements CodeCraft as a thin OpenAI-compatible adapter:
- `src/providers/codecraft.mjs` sets `https://codecraftapi.com/v1` and derives a plan hint from the observed `X-RateLimit-Limit` value.
- `src/config.mjs` keeps the API key in an environment variable (`CODECRAFT_API_KEY`) and supports a provider-neutral config boundary.
- The client also contains token-budget/plan resolution and request guardrails.

Collection interpretation:
- The adapter shape is useful reference evidence for API Factory.
- The plan mapping is third-party application logic, not official CodeCraft truth. We must not promote inferred plan/token values to provider policy without live official evidence.
- Existing OmniRoute/free-provider policy remains canonical for free-tier classification.

## Verification state update
SOURCE_EVIDENCE_PLUS_THIRD_PARTY_ADAPTER_REFERENCE. Still not runtime VERIFIED. No API key was collected or used.
