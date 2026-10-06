# Dyad Reusable Capability Extraction — 2026-10-06

Source: `dyad-sh/dyad@701d9179b43773a9c654014975ebc699a32fd500`

## Candidate A — MCP Consent Boundary
**Family:** security_defense / agent_orchestration  
**Disposition:** UPGRADE candidate  
**Existing canonical overlap:** permission-aware-executor, action-approval-gate, evidence-backed-operator  
**Pattern:** typed MCP server/tool/input-schema context → independent consent decision → allow/ask/deny → controlled invocation → test evidence.  
**Do not copy:** source implementation.  
**Validation required:** isolated MCP fixture with allow/ask/deny cases and evidence of blocked unauthorized execution.

## Candidate B — Independent Shell Review
**Family:** security_defense / agent_orchestration  
**Disposition:** UPGRADE candidate  
**Existing canonical overlap:** permission-aware-executor, action-approval-gate  
**Pattern:** independent non-executing reviewer returns structured allow/ask/block; separates authorization from safety; treats tool/repository text as untrusted evidence; blocks bypass, credential theft, privilege escalation and opaque destructive effects.  
**Validation required:** safe/review/blocked command corpus with false-positive and false-negative checks.

## Candidate C — State Mutation Capability Flag
**Family:** agent_orchestration / security_defense  
**Disposition:** UPGRADE candidate  
**Existing canonical overlap:** permission-aware-executor, delegated-user-operator  
**Pattern:** mutation capability is declared at the tool boundary and inherited by wrappers; read-only/plan-only filtering uses the same turn-scoped capability state.  
**Validation required:** wrapper tool cannot expose writes in Ask/Plan mode.

## Candidate D — WAL-safe Backup Integrity
**Family:** evaluation_reliability / data_storage  
**Disposition:** MERGE/UPGRADE candidate  
**Existing canonical overlap:** ai-evaluation-evidence and recovery/backup patterns  
**Pattern:** checkpoint WAL → SQLite backup API → checksum metadata → bounded retention → cleanup after failure.  
**Validation required:** crash/WAL fixture, restore, checksum comparison.

## Candidate E — Fake Provider/MCP Evaluation Fixtures
**Family:** evaluation_reliability / ai_model_routing  
**Disposition:** REFERENCE/MERGE  
**Existing canonical overlap:** ai-evaluation-evidence + evaluation-fixture/v1  
**Pattern:** fake LLM, HTTP MCP, OAuth MCP and stdio MCP fixtures enable deterministic contract tests without provider spend.  
**Validation required:** adapt one fixture to evaluation-fixture/v1 and run in CI.

## Candidate F — Provider Model Registry
**Family:** ai_model_routing  
**Disposition:** MERGE/UPGRADE candidate  
**Existing canonical overlap:** multi-modal-provider-gateway  
**Pattern:** provider/model metadata, local Ollama and external providers, capability-aware selection, compatibility tests.  
**Validation required:** compare semantics with OmniRoute and Hikhakk before changing the canonical gateway.

## Priority

A → B → C → E → D → F

No new standalone Skills should be created unless semantic dedupe proves an uncovered contract.
