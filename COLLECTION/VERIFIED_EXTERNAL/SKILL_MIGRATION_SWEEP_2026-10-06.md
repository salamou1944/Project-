# COLLECTION → SKILL MIGRATION SWEEP — 2026-10-06

Status: ACTIVE / SWEEP-02

## Canonical rule
Every reusable Capability in COLLECTION is migrated to a canonical Skill after deduplication against the existing agent-skills tree. Non-procedural assets retain their correct classification.

## Existing migrations
- OpenHands → engineering-agent-benchmark
- LiteLLM → provider-routing-benchmark
- Ollama → local-provider-verification
- OmniRoute → provider-free-tier-audit

## Sweep-02 migrations

| Collection capability | Canonical Skill | Deduplication result |
|---|---|---|
| CUA / bounded computer-use execution and verification | computer-use-verification | No dedicated computer-use verification Skill found; browser-runtime-verification is complementary |
| Browser/web research collection | browser-research-collection | Browser-runtime-verification is application testing, not research collection |
| Durable automation: persistence/retry/idempotency/recovery | durable-workflow-recovery | Existing orchestration Skills retained; this is a recovery pattern |
| DevSecOps secret/dependency/SBOM/policy gate | devsecops-security-gate | Existing MCP/security Skills do not cover repository security scanning |
| Document/PDF/OCR structured extraction | document-intelligence-extraction | No dedicated document extraction Skill found |
| Agent state backup and disaster recovery | agent-state-backup-recovery | No dedicated state-backup/recovery Skill found |

## Explicit non-migrations
- ASTRA remains the evidence/research storage and validation boundary.
- Existing browser-runtime-verification, repository-retrieval-verification, source-grounded-knowledge-base, source-grounded-video-overview, agentic-evaluation, evidence-driven-agent-evaluation, and multi-modal-provider-gateway remain canonical where their scope already covers the Collection finding.
- External runtimes/frameworks are not imported merely because they expose similar capabilities.

## Promotion states
DISCOVERED → CLASSIFIED → DEDUPED → EXTRACTED → VERIFIED → PROMOTED

The new Skills in this sweep are EXTRACTED. They are not claimed as externally verified execution results until repository-native tests and task-specific evidence pass.

## Next targets
Remaining Collection candidates are checked against this matrix and the complete agent-skills tree before creating anything new. Priority areas: browser/desktop runtimes, research/retrieval stacks, local agent workspaces, security scanners, document/media pipelines, and durable automation.

## Ownership
- COLLECTION: external intelligence and provenance
- agent-skills: canonical reusable operational Skills
- Elite / ARMY-14 / Operator: Skill selection and execution
- SOAT: integration and behavioral verification
- ASTRA: research/evidence storage and validation
