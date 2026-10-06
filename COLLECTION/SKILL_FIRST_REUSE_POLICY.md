# COLLECTION → SKILL-FIRST REUSE POLICY

Status: ACTIVE

## Rule

Every reusable Capability found in COLLECTION must be converted into a canonical Skill unless the finding is actually Knowledge, a Service/Runtime, an Adapter, a Tool, a Reference/Pattern, or another non-procedural asset.

Existing reusable capabilities are migrated as well; this is not only a rule for future discoveries.

## Required pipeline

COLLECTION → VERIFY → CLASSIFY → DEDUPE → EXTRACT SKILL → TEST → REGISTER → PROMOTE

## Promotion contract

A Skill requires:
- exact source/revision when external;
- license and dependency boundary;
- explicit input/action/output contract;
- evidence and acceptance criteria;
- failure and security boundaries;
- deduplication check against agent-skills;
- isolated or repository-native verification;
- provenance back to the Collection source.

## Current mapped migrations

| Capability | Skill | Boundary |
|---|---|---|
| OpenHands engineering automation evaluation | engineering-agent-benchmark | benchmark/extract only |
| LiteLLM routing/fallback/cost/guardrails comparison | provider-routing-benchmark | benchmark/extract only |
| Ollama local provider execution | local-provider-verification | verified local lane; no duplicate runtime |
| OmniRoute provider/free-tier intelligence | provider-free-tier-audit | intelligence only; no gateway import |

## Classification

- repeatable method → Skill
- knowledge/data → Knowledge
- runtime/infrastructure → Service
- external API/provider → Adapter
- small executable utility → Tool
- framework/architecture → Reference/Pattern
- evaluator/checker → Verification Skill

## Architectural ownership

COLLECTION is external intelligence.
agent-skills is the canonical reusable operational Skill layer.
Elite/ARMY-14/Operator consume verified Skills.
SOAT verifies execution and integration behavior.
ASTRA remains the evidence/research boundary.

## Hard rule

Do not create a second control plane merely because an external project contains a larger implementation. Extract the smallest verified procedure that closes a real gap.
