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


## 2026-10-16 refresh

- Upstream was re-inspected on 2026-10-16. The repository revision captured in the current extraction is `cf97c32fec1b2e96e9936746e2731a81bd5ea33f`; the repository metadata reports an update at `2026-10-16T02:34:29Z`.
- Current upstream `data.json` reports `lastUpdated: 2026-10-05`. The repository's recent update timestamp must not be mistaken for a fresh quota audit.
- Current README still labels the list as permanent-free-tier inference APIs and describes OpenAI SDK compatibility as the default, with exceptions. This is source-owner documentation, not independent provider verification.
- Status remains `DISCOVERY_CAPTURED`; provider quota, terms, region eligibility, endpoint reliability and commercial-use constraints remain unverified unless independently checked against each provider's official source.


## 2026-10-16 extraction comparison

- Current upstream revision captured: `cf97c32fec1b2e96e9936746e2731a81bd5ea33f` (repository metadata updated `2026-10-16T02:34:29Z`). Previous extraction revision: `b25c0395fe1e7628ecc99bf119a40365801c6fb4`.
- The two extraction records each contain 15 tracked files; the current extraction has zero fetch errors and no tracked file-content differences from the prior snapshot. The repository update timestamp alone does not mean provider data changed.
- Upstream `data.json` now reports `lastUpdated: 2026-10-05`; quotas and terms remain discovery-only until provider-official revalidation.
