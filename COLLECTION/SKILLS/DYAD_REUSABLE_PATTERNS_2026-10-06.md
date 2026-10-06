# Dyad-sh Reusable Capability Extraction — 2026-10-06

## Account-wide result

The `dyad-sh` organization currently exposes **8 public repositories**. The account sweep covered all 8:

1. `dyad` — primary product; deepest capability source.
2. `nextjs-template` — Apache-2.0; AI-oriented project rules and Next.js starter conventions.
3. `tanstack-start-template` — currently empty; no reusable implementation evidence.
4. `react-vite-nitro` — Vite/React + Nitro starter; useful server-side capability pattern.
5. `portal-mini-store-template` — MIT; complete commerce/auth/admin/order template.
6. `supabase-management-js` — fork/package wrapper; typed Supabase Management API client.
7. `ollama-ai-provider-v2` — Apache-2.0 fork; Vercel AI SDK provider for Ollama, tool calling/streaming/thinking support.
8. `sandpack-bundler` — Apache-2.0 fork of CodeSandbox; client-side sandbox/bundler runtime.

## Candidate A — MCP Consent Boundary
**Family:** security_defense / agent_orchestration  
**Disposition:** UPGRADE candidate  
**Existing canonical overlap:** permission-aware-executor, action-approval-gate, evidence-backed-operator  
**Pattern:** typed MCP server/tool/input-schema context → independent consent decision → allow/ask/deny → controlled invocation → test evidence.  
**Do not copy:** source implementation.  
**Validation:** isolated MCP fixture with allow/ask/deny cases and evidence of blocked unauthorized execution.

## Candidate B — Independent Shell Review
**Family:** security_defense / agent_orchestration  
**Disposition:** UPGRADE candidate  
**Existing canonical overlap:** permission-aware-executor, action-approval-gate  
**Pattern:** independent non-executing reviewer returns structured allow/ask/block; separates authorization from safety; treats tool/repository text as untrusted evidence; blocks bypass, credential theft, privilege escalation and opaque destructive effects.

## Candidate C — State Mutation Capability Flag
**Family:** agent_orchestration / security_defense  
**Disposition:** UPGRADE candidate  
**Existing canonical overlap:** permission-aware-executor, delegated-user-operator  
**Pattern:** mutation capability is declared at the tool boundary and inherited by wrappers; read-only/plan-only filtering uses the same turn-scoped capability state.

## Candidate D — Fake Provider/MCP Evaluation Fixtures
**Family:** evaluation_reliability / ai_model_routing  
**Disposition:** MERGE/REFERENCE  
**Existing canonical overlap:** ai-evaluation-evidence + evaluation-fixture/v1  
**Pattern:** fake LLM, HTTP MCP, OAuth MCP and stdio MCP fixtures enable deterministic contract tests without provider spend.

## Candidate E — WAL-safe Backup Integrity
**Family:** evaluation_reliability / data_storage  
**Disposition:** MERGE/UPGRADE  
**Existing canonical overlap:** existing backup/recovery/evidence patterns  
**Pattern:** checkpoint WAL → SQLite backup API → checksum metadata → bounded retention → cleanup after failure.

## Candidate F — Provider/Model Registry
**Family:** ai_model_routing  
**Disposition:** MERGE/UPGRADE candidate  
**Existing canonical overlap:** multi-modal-provider-gateway  
**Pattern:** provider/model metadata, local Ollama and external providers, capability-aware selection, compatibility tests. Compare with OmniRoute/Hikhakk before changing canonical gateway.

## Candidate G — AI Project Rules / Repository-local Contract
**Family:** agent_orchestration / engineering_workflow  
**Disposition:** REFERENCE → possible UPGRADE  
**Sources:** `dyad/AGENTS.md`, `rules/*`, `nextjs-template/AI_RULES.md`  
**Pattern:** repository-local rules indexed by task area; agent must read relevant rules before changes; project-local AI rules encode stack, validation and architectural constraints.  
**Leverage:** strengthen Codex Engineering Workflow / knowledge-route-discovery so route selection includes repository-local contract discovery before execution.

## Candidate H — Server-side capability for Vite
**Family:** api_engineering / deployment_operations  
**Disposition:** REFERENCE/possible UPGRADE  
**Source:** `react-vite-nitro`  
**Pattern:** Nitro adds server-side routes/runtime to Vite/React projects, closing the gap between client-only Vite apps and database/API/secrets/webhook workloads.  
**Leverage:** useful for API Factory / EASY only if a concrete Vite deployment gap exists; no new standalone Skill.

## Candidate I — Ready commerce starter
**Family:** commerce_revenue  
**Disposition:** REFERENCE; not canonical Skill  
**Source:** `portal-mini-store-template`  
**Pattern:** auth + roles + catalog + media + cart/order flow + order status + admin CMS + price verification.  
**Leverage:** potentially useful as a low-cost reference/template for a customer-facing commerce proof, but it is not a replacement for EASY and should not be copied wholesale.

## Candidate J — Typed Supabase Management API wrapper
**Family:** api_engineering / data_storage  
**Disposition:** REFERENCE  
**Source:** `supabase-management-js`  
**Pattern:** generated OpenAPI types + typed Management API methods + structured error guard.  
**Leverage:** useful for Supabase control-plane automation; compare against our existing Supabase connector/tooling before integration.

## Candidate K — Ollama AI SDK Provider
**Family:** ai_model_routing / free_local  
**Disposition:** REFERENCE/MERGE candidate  
**Source:** `ollama-ai-provider-v2`, Apache-2.0  
**Pattern:** Vercel AI SDK provider abstraction for local Ollama; tool streaming/calling and thinking toggle.  
**Leverage:** reinforces local/free provider route; compare with existing Ollama/OmniRoute/provider-gateway assets before adoption.

## Candidate L — Sandpack client bundler
**Family:** execution_runtime / sandboxing  
**Disposition:** REFERENCE  
**Source:** `sandpack-bundler`, Apache-2.0 fork of CodeSandbox  
**Pattern:** client-side bundling/runtime for sandboxed frontend execution.  
**Leverage:** potentially relevant to EASY previews or browser-side project execution, but existing preview/sandbox infrastructure must be compared first.

## Low-value / no-action sources

- `tanstack-start-template`: empty at inspection time; no implementation to promote.
- `sandpack-bundler`: fork; preserve upstream provenance and do not treat the fork as an independent capability source.
- `supabase-management-js`: fork/package wrapper; useful as typed reference, not a new platform layer.
- Template repos are implementation references, not new Skills.

## Priority after account-wide sweep

**P0**
1. MCP consent boundary
2. independent shell review
3. mutation capability enforcement

**P1**
4. repository-local AI rules / contract discovery
5. deterministic fake provider/MCP fixtures
6. Ollama provider route

**P2**
7. WAL-safe backup/recovery
8. Vite + Nitro server capability
9. commerce starter
10. typed Supabase Management API wrapper
11. Sandpack bundler

## Canonical rule

No standalone Skill is created from these candidates unless semantic dedupe against `agent-skills`, Collection and AI Operating Memory proves a genuinely missing contract.

## License / provenance

The primary `dyad` repository explicitly distinguishes licensing inside/outside `src/pro`; the other repositories have their own licenses/fork provenance. Any implementation reuse requires path-level license verification.

## Evidence boundary

This is an account/repository source inspection and capability assessment. It is **not production proof** and does not claim that any extracted pattern is already deployed in our systems.
