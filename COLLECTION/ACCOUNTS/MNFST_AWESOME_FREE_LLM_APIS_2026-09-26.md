# SOURCE CAPTURE — mnfst/awesome-free-llm-apis

Status: DISCOVERY_CAPTURED
Source: https://github.com/mnfst/awesome-free-llm-apis
Added to permanent daily collection: 2026-09-26
Latest upstream refresh checked: 2026-09-30
Default branch: main
README revision: ae5f31b3db07083458fa3149772cc98ebb5329c4
data.json revision: 5929dd7170c5f0440bcaa31e8675a87621cb4172
data.json lastUpdated: 2026-08-21

## Monitoring scope
Track providers, models, quotas, geography and identity requirements, commercial-use terms, privacy and training use, endpoint reliability, deprecations, and self-hosted alternatives.

## Current evidence
- The upstream README describes permanent free tiers for text inference and says endpoints are generally OpenAI SDK-compatible unless noted.
- The upstream data contains provider category, country, base URL, model IDs, context, output limits, modalities, rate limits, and footnotes.
- Example current entry observed directly in data.json: Aion Labs, permanent free tier, no credit card, 15 RPM and 20K tokens/day; this remains unverified until checked against the provider's own current documentation and endpoint.
- The source contains both provider APIs and third-party inference providers; preserve that distinction.

## Gate
No provider is VERIFIED or production-ready from this list alone. Require current official provider documentation and direct API verification where available.

## Operational watch
For each refresh, diff:
- provider additions/removals and model retirement
- RPM/RPD/TPM/TPD and concurrency changes
- geography, identity and commercial-use restrictions
- privacy, logging and training-use terms
- endpoint reachability and error rates
- OpenAI SDK compatibility
- self-hosted replacements and subscription-elimination value
