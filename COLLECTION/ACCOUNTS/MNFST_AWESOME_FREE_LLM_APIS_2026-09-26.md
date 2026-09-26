# SOURCE CAPTURE — mnfst/awesome-free-llm-apis

Status: DISCOVERY_CAPTURED
Source type: GitHub repository
Source owner: mnfst
Source repository: https://github.com/mnfst/awesome-free-llm-apis
Added to permanent daily collection: 2026-09-26

## Purpose
Track free/permanent-free LLM API providers and inference providers, with special attention to OpenAI-compatible endpoints, quotas, model availability, modality, commercial-use restrictions, and whether a provider can reduce paid API dependence.

## Initial evidence
- The repository describes itself as a list of LLM APIs with permanent free tiers for text inference.
- Its README states that endpoints are generally OpenAI SDK-compatible unless noted.
- Current repository structure includes `data.json`, verification tooling, scripts, and generated README material.
- The repository currently lists providers including Aion Labs, Cohere, Google Gemini, Mistral AI, Z AI, Cerebras, Cloudflare Workers AI, Groq, Hugging Face, Kilo Code and others.
- The README explicitly distinguishes provider APIs from third-party inference providers.
- Free access is not equivalent to unrestricted commercial use: for example, the README marks Cohere's listed trial as non-commercial and marks some providers as requiring a payment method or using credit-metered access.

## Immediate relevance
1. Salamou-31 / AI-API-HUB: candidate provider pool and routing fallback discovery.
2. EASY: possible external AI dependency alternatives, subject to capability and license/terms verification.
3. Elite / ARMY-14: provider-neutral routing and fail-closed external dependency handling.
4. Subscription elimination: identify usable free cloud tiers before paying for API capacity.

## Verification rule
Do not promote any provider to VERIFIED or integrate it solely because it appears in this list. For each candidate, verify current provider documentation, quota, authentication, model availability, geographic restrictions, commercial terms, privacy/data-use terms, reliability, and actual API behavior.

## Daily collection rule
Refresh this source daily for changes to providers, models, quotas, free-tier conditions, verification status, and newly discovered providers. Preserve prior revisions and provenance; do not duplicate providers already captured from other sources.

## Current state
Useful source for collection and candidate discovery. No provider from this repository is counted as an integrated or production dependency yet.
