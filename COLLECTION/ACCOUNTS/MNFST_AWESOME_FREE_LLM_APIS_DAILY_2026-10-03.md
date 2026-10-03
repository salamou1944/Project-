# mnfst/awesome-free-llm-apis — daily monitoring capture
Date: 2026-10-03
Status: DISCOVERY_CAPTURED — NOT_VERIFIED

## Source / provenance
- Repository: https://github.com/mnfst/awesome-free-llm-apis
- Default branch: main
- Repository snapshot checked: 2026-10-03
- Repository pushed_at: 2026-10-02T04:07:08Z
- Current GitHub stars: 9,027
- Forks: 926
- License: CC0-1.0
- README blob: ae5f31b3db07083458fa3149772cc98ebb5329c4
- data.json blob: 5929dd7170c5f0440bcaa31e8675a87621cb4172
- data.json lastUpdated: 2026-08-21

## Inventory captured from data.json
- Providers: 16
- Model entries: 118
- Categories: provider_api, inference_provider
- The repository states that endpoints are OpenAI SDK-compatible unless noted.
- Provider examples currently listed: Aion Labs, Cohere, Google Gemini, Mistral AI, Z AI, Cloudflare Workers AI, Groq, Hugging Face, Kilo Code, LLM7.io, ModelScope, NVIDIA NIM, Ollama Cloud, OpenRouter, OVHcloud AI Endpoints, SiliconFlow.

## Important tracked fields
- Quotas/rate limits vary by provider/model: examples include Aion 15 RPM/20K TPD, Groq 30 RPM/1,000 RPD, Cloudflare 10K neurons/day shared, Kilo Code 200 req/hr, OpenRouter 20 RPM/50 RPD, OVHcloud 2 RPM/IP/model.
- Geography/identity constraints appear in the source: e.g. ModelScope requires Alibaba Cloud account binding + real-name verification; SiliconFlow requires identity verification.
- Commercial terms are not uniform: Cohere is explicitly listed as non-commercial on the free trial; other providers require direct terms verification before commercial use.
- Privacy/training caveats are present in source descriptions: Google free-tier prompts may be used to improve products; Mistral free-mode prompts may be used to train models unless opted out.
- Reliability: source data is a discovery index, not an SLA or uptime guarantee. Ollama Cloud limits are described as session/weekly limits that are unpublished.
- Paid/cloud/external dependencies: most entries are hosted APIs; some require account/program membership or identity checks. Self-hosting is not implied by inclusion.
- Security/operational: API keys, rate limits, provider policy changes, data handling, and regional access must be checked against official provider documentation before production.
- Endpoint status: no authenticated endpoint test was performed in this run.

## Verification gate
No provider is marked VERIFIED or a production alternative from this capture alone.
Required before VERIFIED/production:
1. Direct official provider documentation for current quota, geography, commercial terms, privacy/data retention and acceptable use.
2. Live endpoint test where technically possible.
3. Record date/time, model ID, HTTP outcome and observed limits.
4. Re-check when provider terms or endpoints change.

## Change signal
The repository itself was pushed on 2026-10-02 and currently reports 9,027 stars. The structured data still declares lastUpdated=2026-08-21, so freshness of individual provider records is NOT_VERIFIED despite the repository being recently pushed.

## Action value
High discovery value for reducing paid LLM/API subscriptions, but only after provider-by-provider verification. Keep permanently in the collection and compare future snapshots rather than overwriting history.
