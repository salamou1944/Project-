# VERIFIED EXTERNAL — REUSE / GAP MATRIX — 2026-10-05

Status: VERIFIED_COMPARISON_COMPLETE
Scope: OpenHands, LiteLLM, Ollama, canonical diegosouzapw/OmniRoute
Internal comparison targets: salamou1944/Salamou-31, salamou1944/agent-skills, salamou1944/Astra
Rule: do not duplicate an internal capability merely because an external project is more complete.

## Evidence boundary

The GitHub code-search endpoint returned no matches for the tested capability queries in the three internal repositories, so absence below is recorded as no direct code-search evidence, not as proof that the capability does not exist. Stronger evidence was obtained from inspected repository-native documents and directory structure.

## Decision matrix

| External | Capability | Internal evidence | Gap / overlap | Decision | Priority |
|---|---|---|---|---|---|
| OpenHands | Agent execution/control center, automations, multiple coding-agent backends | agent-skills/AGENTS.md defines Elite/ARMY-14 as the autonomous engineering core; .github/agents, .github/workflows, .agents/skills are present. | High architectural overlap. OpenHands would duplicate the control-plane role. | REFERENCE ONLY now. Do not import wholesale. Extract only a narrowly superior capability after a task-specific benchmark. | P2 |
| LiteLLM | OpenAI-compatible gateway, multi-provider routing, fallbacks, spend/guardrail controls | Salamou-31/AI-API-HUB/API-CATALOG.md has a provider catalog; it also states the API Factory provider boundary is verified against SOAT with a real local Ollama completion. | Gateway/provider-boundary capability is already an explicit internal surface. Adding LiteLLM wholesale risks creating a second provider-control plane. | DO NOT INTEGRATE WHOLE PROJECT. Revisit only for isolated routing/cost/guardrail primitives that beat the existing boundary. | P1 research |
| Ollama | Local model runtime / provider | AI-API-HUB/API-CATALOG.md explicitly records a real local Ollama completion as SOAT runtime proof. | Capability is already operationally represented and verified; no need to add a second local runtime abstraction. | KEEP AS VERIFIED PROVIDER PATH. No new integration required. | P0 retained |
| OmniRoute | Broad provider catalog, fallback/routing, free-tier/provider availability intelligence | AI-API-HUB/API-CATALOG.md contains a curated provider catalog, but no evidence was found for OmniRoute-scale provider availability intelligence. | Potential non-duplicative value is provider/free-tier intelligence, not another gateway. | EXTRACT/ADAPT ONLY the provider-intelligence dataset/logic if it can be isolated and tested without importing the router runtime. | P1 |
| ASTRA | Evidence-first data/research and verification | Astra/README.md, VERIFICATION.md, REAL_DATA_RUNBOOK.md, astra/evidence.py and data pipeline are dedicated to evidence-bound quantitative research. | No meaningful overlap with the four external projects' core capability. | KEEP SEPARATE. ASTRA remains canonical for research/evidence storage and validation. | P0 boundary |

## Integration order

1. No new gateway. Salamou-31/API Factory already has a provider boundary and real SOAT/Ollama proof.
2. No new local runtime. Ollama is already the verified local provider path.
3. No OpenHands wholesale adoption. Elite/ARMY-14 already owns the autonomous engineering control plane.
4. OmniRoute is the only immediate extraction candidate. Isolate provider catalog/free-tier/availability intelligence from routing/runtime code.
5. LiteLLM remains a benchmark/reference. Compare only narrowly scoped routing, fallback, budget, and guardrail primitives against the existing API Factory before any code import.

## Concrete next extraction

Target: COLLECTION/VERIFIED_EXTERNAL/OMNIROUTE_PROVIDER_INTELLIGENCE_2026-10-05.md

Required evidence before implementation:
- exact canonical OmniRoute revision;
- provider/free-tier source files identified;
- license boundary recorded;
- smallest standalone extraction identified;
- no credential harvesting or secret material;
- isolated test proving the extracted intelligence is more useful than the existing API-CATALOG;
- only then propose an integration PR in Salamou-31/API Factory.

## Non-duplication verdict

- OpenHands: overlap — reject wholesale integration
- LiteLLM: overlap — reject wholesale integration
- Ollama: already integrated/verified — no-op
- OmniRoute: specific gap exists — extract intelligence only
- ASTRA: separate evidence domain — preserve boundary

Recorded from live repository inspection on 2026-10-05.
