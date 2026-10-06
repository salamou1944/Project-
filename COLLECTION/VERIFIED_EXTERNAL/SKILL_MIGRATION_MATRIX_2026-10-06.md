# SKILL MIGRATION MATRIX — 2026-10-06

Status: ACTIVE

| Source | Former capability | Canonical Skill | State |
|---|---|---|---|
| OpenHands | engineering automation/control-plane evaluation | agent-skills/skills/engineering-agent-benchmark | EXTRACTED |
| LiteLLM | provider routing/fallback/budget/guardrail comparison | agent-skills/skills/provider-routing-benchmark | EXTRACTED |
| Ollama | local inference/provider verification | agent-skills/skills/local-provider-verification | EXTRACTED |
| OmniRoute | provider/free-tier/availability intelligence | agent-skills/skills/provider-free-tier-audit | EXTRACTED |

## Deduplication decisions

- OpenHands: do not replace Elite/ARMY-14.
- LiteLLM: do not create a second Salamou-31 gateway.
- Ollama: keep the existing verified local provider path.
- OmniRoute: keep provider intelligence, not the routing runtime.

## Next sweep

Apply the same process to remaining verified Collection domains: computer-use, browser automation, research/retrieval, memory/RAG, evaluation, document intelligence, media, and local-agent runtimes. Existing Skills must be checked before any new Skill is created.
