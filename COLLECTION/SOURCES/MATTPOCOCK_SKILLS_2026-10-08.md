# SOURCE — mattpocock/skills — 2026-10-08

Source: https://github.com/mattpocock/skills
Owner: mattpocock
License: MIT
Verified package version: 1.3.1
Collection status: DISCOVERY_VERIFIED / DEEP-HARVEST-QUEUED

## Why collected
High-value Agent Skills source for engineering execution, research, diagnosis, architecture, TDD, code review, requirements discovery, ticket decomposition, handoff, and agent-oriented documentation.

## Verified source characteristics
- Public GitHub repository.
- MIT license.
- Small, editable, composable, model-agnostic skills.
- Supports Codex and other agents through skills.sh installation.
- Current repository structure includes .agents, skills, docs, scripts and Claude plugin metadata.
- README distinguishes user-invoked orchestration skills from model-invoked reusable skills.

## Current skill families observed
User-invoked:
- ask-matt
- grill-with-docs
- triage
- improve-codebase-architecture
- setup-matt-pocock-skills
- to-spec
- to-tickets
- implement
- wayfinder
- grill-me
- handoff
- teach
- to-questionnaire
- wait-what

Model-invoked:
- prototype
- diagnosing-bugs
- research
- tdd
- domain-modeling
- codebase-design
- code-review
- resolving-merge-conflicts
- wizard
- grilling
- writing-for-agents

## Collection decision
Do not install wholesale into agent-skills. Treat this as a capability mine:
- semantic-dedupe against canonical Skills
- extract materially stronger contracts only
- preserve provenance/license
- integrate useful patterns into SOAT/evidence gates where applicable
- runtime-verify before READY_TO_USE

## High-priority extraction candidates
1. Research → cited evidence artifact generation.
2. TDD → explicit red/green/refactor execution loop.
3. Code review → independent standards/spec axes.
4. Diagnosing bugs → reproduce/minimize/hypothesize/instrument/fix/regression loop.
5. Domain modeling → terminology/edge-case/domain-state discipline.
6. Codebase design → deep module/small interface seam discipline.
7. Wizard → human-only external setup/action boundary.
8. Handoff → compact continuation state for another agent/session.
9. Triage → explicit state-machine workflow.
10. To-spec/to-tickets → conversation-to-executable-work conversion.

## Verification boundary
This source record verifies repository/license/package metadata and README-described capabilities. It does NOT claim that every skill has been independently runtime-tested. Deep extraction and READY_TO_USE promotion require separate verification.
