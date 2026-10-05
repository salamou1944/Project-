# VERIFIED EXTERNAL READY PROJECTS — 2026-10-05

Status: VERIFIED_EXTERNAL_READY
Scope: External projects only. This registry is deliberately separate from user-owned projects.
Rule: repository presence alone is not enough; license/provenance/current repository identity were checked before admission.
Important: VERIFIED_EXTERNAL_READY means the external asset is ready for evaluation/adaptation. It does NOT mean it is integrated into EASY, MONY, Salamou-31, ASTRA, agent-skills, Elite/ARMY-14, or deployed in our production.

## Priority order

| Priority | Project | Canonical source | License | Ready capability | Current use decision |
|---|---|---|---|---|---|
| P0 | OpenHands | https://github.com/OpenHands/OpenHands | MIT | AI-driven development / agent execution | First external implementation candidate for engineering acceleration |
| P0 | LiteLLM | https://github.com/BerriAI/litellm | MIT (enterprise/ subtree has its own license) | Multi-provider LLM gateway, OpenAI-compatible routing, cost/guardrail/load-balancing primitives | Candidate gateway/control layer; compare against existing Salamou-31/API Factory before duplication |
| P0 | Ollama | https://github.com/ollama/ollama | MIT | Local model runtime | Free/local inference fallback; candidate for provider-independent testing |
| P1 | OmniRoute | https://github.com/diegosouzapw/OmniRoute | MIT | Unified AI gateway, provider routing/fallback, free-tier catalog, CLI/MCP/A2A capabilities | Keep as external source; canonical repo is diegosouzapw/OmniRoute, not the previously inspected clone |

## Verification evidence

### OpenHands
- Canonical repository: OpenHands/OpenHands.
- License file explicitly grants MIT rights.
- Repository is public and active.
- Use boundary: external reusable asset only; no claim of integration.

### LiteLLM
- Canonical repository: BerriAI/litellm.
- LICENSE explicitly states content outside `enterprise/` is MIT; enterprise content has its own license.
- Repository is public and active.
- Use boundary: gateway capability candidate; must not duplicate existing API Factory capabilities without comparison.

### Ollama
- Canonical repository: ollama/ollama.
- LICENSE explicitly states MIT.
- Repository is public and active.
- Use boundary: local/self-hosted inference path; no paid-provider dependency assumed.

### OmniRoute
- Canonical repository verified directly as diegosouzapw/OmniRoute.
- LICENSE explicitly states MIT.
- Default branch currently reported as `release/v3.8.52`.
- The earlier `laconrep/OmniRoute` record is treated as a clone/fork and is NOT the canonical source.
- Use boundary: external gateway/source material only; no integration claim.

## Excluded from READY

- Toss-Online-Services/TossErp — retained as a discovered external repository, but not admitted to READY because its repository metadata did not expose a declared license in the verification pass and it has open issues. Re-evaluate only after independent license/release verification.
- OpenHands SDK/CLI — retained as candidates, but not separately admitted here until repository-level verification establishes the exact component and current revision needed for reuse.

## Collection → Repair pipeline

COLLECTION → VERIFIED_EXTERNAL_READY → capability comparison → smallest reusable extraction → independent test → integration PR → production evidence

No external project is copied into a user-owned project merely because it is listed here.
