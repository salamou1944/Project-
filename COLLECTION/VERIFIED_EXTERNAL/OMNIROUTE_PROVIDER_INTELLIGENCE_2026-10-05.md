# OmniRoute Provider Intelligence — 2026-10-05

Status: EXTRACTED_REFERENCE_DATA
Source: canonical `diegosouzapw/OmniRoute`
Inspected revision: `release/v3.8.52`
Primary source files: `docs/reference/FREE_TIERS.md`, `src/shared/constants/providers.ts`, `src/shared/constants/providers/apikey/*`
License boundary: OmniRoute is MIT; this file stores a small factual intelligence snapshot and source references, not copied source code.

## Why this exists

Salamou-31/API Factory already owns the provider boundary and has real SOAT/Ollama verification. Therefore the reusable OmniRoute value is **provider intelligence**, especially free-tier classification and quota semantics, not another gateway/router.

## Extracted schema

A provider-intelligence record should preserve:

- `provider_id`
- `access_class`: no-auth / OAuth / API-key / local / other
- `free_status`: recurring / one-time / uncapped / discontinued / unknown
- `quota_basis`: monthly / daily / RPM / RPD / uncapped / unknown
- `estimated_monthly_tokens`: only when a documented recurring token figure exists
- `hard_stop`: true only when provider evidence establishes that exceeding the allowance refuses the request instead of billing
- `eligibility_gate`: none / regional-identity / payment / KYC / other
- `tos_risk`: normal / caution / avoid / unknown
- `source_last_researched`
- `source_url`

## Verified examples from the inspected OmniRoute catalog

| Provider | Access | Free classification | Important constraint | Use in API Factory |
|---|---|---|---|---|
| Gemini | API/OAuth variants | recurring free family; no current published token figure in OmniRoute's latest audit | quota/rate limits apply; do not invent a token total | candidate free fallback; reverify before runtime use |
| Groq | API key | recurring per-model caps | OmniRoute documents multiple per-model daily caps and pool-dedupes them | candidate free fallback |
| Cloudflare AI | API key | recurring | 10K neurons/day in OmniRoute's documented audit | candidate free fallback |
| Mistral | API key | recurring | OmniRoute notes the 1B figure is visible in the account console; evidence quality differs from public hard limits | discovery only until independently verified |
| Kilo Gateway | gateway/free access | recurring-uncapped | no published token ceiling; rate/concurrency limits still apply | discovery candidate; never treat as unlimited capacity |
| OpenCode Zen | free service | recurring-uncapped | no published token ceiling | discovery candidate; verify terms/availability before use |
| Z.AI / GLM-CN | free | recurring-uncapped plus signup bonus | no published token ceiling; signup bonus is separate from recurring access | discovery candidate; region/terms must be checked |
| Pollinations | no-key/public access | free/keyless | no key does not imply uptime, privacy, or unlimited capacity | experimental fallback only |
| LongCat | no-key/signup | one-time signup grant in OmniRoute's audited data | KYC-gated and not recurring | do not count as recurring capacity |
| Cerebras | API key | one-time signup credit in OmniRoute's 2026-09 correction | requires payment method according to OmniRoute's audit | do not count as recurring free capacity |

## Critical rules extracted from OmniRoute

1. `hasFree` is discovery metadata, not proof of unlimited access.
2. `recurring-uncapped` means no published token ceiling was available; rate and concurrency limits still apply.
3. One-time signup credits must not be counted as recurring monthly capacity.
4. Shared provider pools must be deduplicated before calculating aggregate free capacity.
5. Regional/KYC/payment gates must be represented explicitly instead of hidden inside a headline quota.
6. `hard_stop` is unknown unless provider evidence proves that exceeding the free allowance cannot turn into billable usage.
7. Discontinued providers remain historical evidence and must not be presented as currently free.
8. Provider intelligence must be re-audited before being used for an automatic production routing decision.

## API Factory adoption decision

**Adopt the schema and decision rules, not OmniRoute's gateway runtime.**

The immediate reusable unit is a provider-intelligence registry that can feed discovery, cost planning and safe fallback selection. It must remain separate from the actual credential store and provider execution adapters.

## Next implementation gate

Before modifying Salamou-31/API Factory:

1. Compare this schema against the existing `AI-API-HUB/API-CATALOG.md`.
2. Add only fields that are genuinely absent internally.
3. Create an isolated provider-intelligence fixture/test.
4. Require explicit `free_status`, `eligibility_gate`, and `hard_stop` semantics before a provider can enter a zero-cost routing policy.
5. Never infer current quota from this snapshot alone; revalidate the provider's own documentation at decision time.

## Provenance

- OmniRoute repository: https://github.com/diegosouzapw/OmniRoute
- Free-tier methodology: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.52/docs/reference/FREE_TIERS.md
- Provider registry: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.52/src/shared/constants/providers.ts

This record is an evidence-backed extraction/reference artifact, not a claim that every listed provider is currently available to the user or safe for production routing.
