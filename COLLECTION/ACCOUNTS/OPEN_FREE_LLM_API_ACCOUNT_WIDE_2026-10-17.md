# Account-wide source capture — open-free-llm-api — 2026-10-17

Status: OWNER_ENUMERATION_COMPLETE; ONE_REPOSITORY_REVIEWED; DEEP_SWEEP_OPEN
Owner: https://github.com/open-free-llm-api
Owner-scoped search: page 1 returned 1 public repository; page 2 returned 0.
Repository: https://github.com/open-free-llm-api/awesome-freellm-apis
Reviewed: README.md and LICENSE at revision `2a44aa956de7c683eaebbe6dbfe97561fafe9197` / license SHA `eac465657bf303c7359081715cec9a695c62f554`.

## Findings

- License: MIT.
- README reports 508+ free LLM API/model entries from 30 providers and says its data refreshes daily; visible update marker says `2026-10-16`.
- The directory separates "Permanent Free Tiers" from "Renewable Credits", and surfaces card/phone verification expectations, context limits, modalities, base URLs, model IDs, and config snippets for tools including Codex, Cursor and Claude Code.
- This is a provider-discovery/configuration directory, not an API host or proof that all entries are callable.
- The "508+" headline must not be interpreted as 508 distinct providers or guaranteed usable endpoints; README describes models/configurations and the provider directory is a maintained community list.
- No provider's quota, region eligibility, current terms, data retention or commercial-use rights were independently verified in this pass. No API keys were requested or copied.

## Value for Salamou-31 / API Factory

- Use as a second discovery source alongside `mnfst/awesome-free-llm-apis` and OmniRoute provider intelligence.
- Merge by canonical provider + model ID + base URL; deduplicate providers, free pools, and quota scope before any routing decision.
- Preserve `access_class`, `free_status`, quota basis, credit-card requirement, model lifecycle date, source timestamp and official terms URL.
- Keep "permanent free tier" and "renewable promotional credits" separate. A provider should not be considered zero-cost eligible solely because a directory labels it free.
- Require an official provider source and a no-paid-fallback hard stop before API Factory can select a provider automatically.

## Downstream graph

- README links to `freellm.net` as the companion live directory. Treat it as a related source/product, not proof of a separate GitHub owner.
- Provider entries lead to independent upstream provider accounts. Each provider owner must be enumerated separately when selected for deeper verification.

## Next actions

1. Compare the provider/model records against the existing `mnfst` extraction and OmniRoute provider-intelligence schema.
2. Select only providers that have an official current free-tier page, no unresolved card/region gate, and an explicit hard-stop against paid fallback.
3. Keep the account open for deeper source-level review; one README pass is not full account completion.
