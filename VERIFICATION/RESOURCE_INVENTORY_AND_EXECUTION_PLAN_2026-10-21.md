# Resource inventory and execution plan — 2026-10-21

**Purpose:** establish an evidence-backed baseline before choosing the next project actions. This is a live snapshot of connected tools and service metadata, not a claim that every external account, billing entitlement, machine, or secret has been exhaustively inspected.

## 1. Verified account and tool surfaces

| Surface | Verified facts | Boundary / next verification |
|---|---|---|
| GitHub | Authenticated as `salamou1944`; 10 repositories returned for the owner; a separate organization-owned `Sssssssddddd/.github` was previously verified in the existing inventory record. No organization memberships were returned by the current org-membership query. | Enumerate owner and org repositories separately; inspect runner status, workflows, secrets presence only by names/status (never values), permissions, and current CI. |
| Railway | 2 projects, 1 personal workspace; 5 services across the two projects. No volumes or buckets attached to either production environment. Production environment shared-variable names are empty for EASY Runtime Production; EASY Developer Platform exposes a shared variable name `Easy_github_token` (value not read). Latest service deployment summaries include failures; recent deployment list also contains skipped/removed states. | Check per-service runtime status and deployment logs. Do not deploy API Factory into EASY production or alter existing secrets. |
| Render | Workspace `Salamou's workspace`; two API Factory services exist on Free plan: main `https://salamou-31-api-factory.onrender.com` (main branch) and preview `https://salamou31-api-factory-preview.onrender.com` (branch `fix/api-factory-live-storage-readiness-2026-10-20`). | Main API Factory is not production-ready: latest documented readiness smoke was HTTP 503 `DURABLE_STORAGE_REQUIRED` because registry/artifact modes were `local-file`. Preview has prior verified durable registry + artifact read/write-back through the dedicated Supabase gateway; free service may sleep. Re-run external smoke before relying on either endpoint. |
| Supabase | 2 projects both report `ACTIVE_HEALTHY`: `salamou-31-api-factory` (`dyhkdijpkddfsrwruumc`) and `easy-platform-db` (`rdcodzowehzmwdxhztxe`). API Factory project has `public.api_factory_registry` with RLS enabled and 1 row, plus active Edge Function `api-factory-storage` v3. EASY project has `public.pastel_orders` (41 rows, RLS enabled) and active functions `easy-customer-auth`, `pastel-order`, `pastel-tts`, `pastel-tts-v2`. | Database project health is not application readiness. Review Edge Function authorization and test endpoint contracts without reading or exposing secrets. Never use the EASY project for API Factory state. |
| Vercel | One project `salamou31-api-factory`; 10 recent deployments include both READY and ERROR states. Latest listed production deployment was READY; latest staging entries included READY and ERROR. | A READY build is not proof of correct environment variables or durable storage. The documented Vercel runtime is fail-closed until gateway URL/key are configured and readiness passes. Verify with the exact deployment URL and `/ready`. |
| Replit | 3 editable apps surfaced: `FragrantButteryApplicationframework`, `StarkImprobableText`, `PracticalPastelCalculator`. | Their titles do not prove they are EASY or production apps. Resolve app identity, inspect status and source before editing. |
| Notion | A private page already exists: [جرد الموارد المتاحة وخطة التنفيذ — 2026-10-21](https://app.notion.com/p/400791c044f98169a48cfb4482a298b6?pvs=204). It already records free-model/provider research and prior collection evidence. Search for other pages is not a complete workspace export. | Keep Notion as planning/operating notes; GitHub is canonical for code, workflow evidence, and versioned inventory. |
| Termalin | Current connector returns zero reachable hosts and explicitly says saved servers in the Termalin web cabinet are not visible until the connector runs on the host. | Do not claim local PC/server access. The connected Windows runner workflow was queued in the earlier audit; recheck runner/workflow evidence before claiming hardware or Ollama is available. |
| Browser | The browser connector returned “requires the originating browser context”; no usable browser tabs were returned through the current connection. | No computer/browser automation is proven available from this session at the moment. |
| OpenAI Platform | Key-setup and organization/project-target discovery tools are available. | This is separate from ChatGPT subscription access. No API key was created; no free API quota or billing entitlement has been proven. |
| Other available connector namespaces | Tool surfaces include GitLab, Supabase, Vercel, Render, Railway, Notion, GitHub, Replit, Termalin, OpenAI Platform, Canva, Figma, Higgsfield, Apollo, HubSpot, LinkedIn, Upwork, Shopify, Wix, Automations, Files, and Plugin Management. | A tool namespace existing does not mean every service is connected, authorized, or has usable account resources. Verify each integration before assigning it work. |

## 2. GitHub repository inventory

The current owner-only connector query returned these 10 repositories (all reported public except `local-bridge.`, which is private):

- [Salamou-31](https://github.com/salamou1944/Salamou-31) — API Factory and runtime integrations.
- [agent-skills](https://github.com/salamou1944/agent-skills) — skills, supervisors, automation, and MONY-related workflows.
- [Easy-](https://github.com/salamou1944/Easy-) — EASY product/runtime code.
- [AI_operating_memory](https://github.com/salamou1944/AI_operating_memory) — operating memory and project rules.
- [Astra](https://github.com/salamou1944/Astra) — research/quant evidence; live trading remains off according to existing project evidence.
- [Astra-](https://github.com/salamou1944/Astra-) — trading execution boundary; paper-only according to existing project evidence.
- [Files-](https://github.com/salamou1944/Files-) — file/collection assets.
- [Pastel-](https://github.com/salamou1944/Pastel-) — QR concierge / order flow.
- [Project-](https://github.com/salamou1944/Project-) — COLLECTION source inventory and extraction.
- [local-bridge.](https://github.com/salamou1944/local-bridge.) — private Windows-runner diagnostics/bridge.

Additional previously verified repository: [Sssssssddddd/.github](https://github.com/Sssssssddddd/.github), an organization-level community/documentation repository. Current GitHub org-membership enumeration returned empty, so do not infer access to additional organization repositories from that one known repository.

## 3. COLLECTION state — current verified main

- Latest successful bounded incremental run: [39533389021](https://github.com/salamou1944/Project-/actions/runs/39533389021), cycle 18.
- Selected 100 repositories; refreshed 79; preserved 21 blocked source attempts.
- 5,029 extracted source artifacts / 5,050 manifest source rows; 18,551 repositories remain deferred.
- Current-main JSON audit: 13,021 JSON/JSONC files; zero parse failures; 916,967,626 bytes. Validator passed.
- Capability/readiness groups: 45,415; promotion-review items: 31,108; restricted items: 14,307.
- Installation result: `NO_APPROVED_CANDIDATES`; zero installed. This is a correct fail-closed outcome, not installation success.
- Large JSON files remain a maintenance risk: `READY.json` and `CANONICAL-PROMOTION-PLAN.json` exceed GitHub's recommended 50 MB file size, though below the repository's explicit 95 MB guard.
- Cycle 19 was triggered by marker commit [46b3afe](https://github.com/salamou1944/Project-/commit/46b3afe3c55f1b1648c3d3d0b703f592c55a1784); workflow [39671402767](https://github.com/salamou1944/Project-/actions/runs/39671402767) is currently `in_progress`. Recheck the run, extract counts from logs, update the index, and only then trigger the next bounded cycle. Inspect/install an asset only if explicit policy approval is generated.

## 4. API Factory — verified state and actual ceiling

- Current API Factory test: [run 39535393169](https://github.com/salamou1944/Salamou-31/actions/runs/39535393169), passed.
- SOAT integration smoke with a real Ollama completion in CI: [run 39535393138](https://github.com/salamou1944/Salamou-31/actions/runs/39535393138), passed. This is CI-local inference evidence, not proof that Ollama is installed on the user's PC or exposed as a production service.
- Dedicated Supabase registry + active storage gateway are present. The preview has prior external durable-storage verification; the main Render endpoint's documented readiness response was HTTP 503.
- Railway's `salamou31-api-factory` service has no attached volume; latest deployment summary is failed and it has no environment variables in the Railway production environment. Do not use it as the deployment target without an isolated, verified configuration.
- Vercel has successful builds, but durable readiness/configuration is not proven. The deployment adapter in API Factory remains a planner, not a real Railway/Vercel deploy executor.
- Generated API business state, usage ledger, quota state, and idempotency state are not automatically durable. Do not call generated APIs production-durable until separately implemented and tested.

## 5. Free model / “ChatGPT account” finding

- Supported ChatGPT Free Codex access can be useful for local coding-agent work subject to plan limits; it is not a general OpenAI API key, free API quota, or always-on inference endpoint.
- GitHub Models inference was retired on 2026-07-30; do not use old GitHub Models examples as a live runtime.
- Ollama is the most direct no-hosted-API-bill test path, but local hardware/installation is unverified through the current Termalin/browser connections.
- Next hosted candidates are Gemini free tier, Groq free plan, and OpenRouter `:free` models, but each current probe deliberately skipped requests because account/model free-tier eligibility was not explicitly confirmed. No live hosted completion is proven. Never send secrets/customer/confidential data to a free tier with data-use terms not approved; no paid fallback.
- [OmniRoute](https://github.com/diegosouzapw/OmniRoute) is an open-source OpenAI-compatible router, not a provider quota grant. It requires user-owned provider accounts/keys; the ChatGPT Web/Codex adapter is not accepted as a supported production inference route without code and terms review.
- [awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) is a discovery list (CC0-1.0); provider entries and quotas must be independently revalidated against official pricing/terms.

## 6. Execution plan, ordered by dependency

1. **Complete inventory before further architecture changes:** verify all owner/org repos, current workflows, Render deploy/smoke state, Railway service status, Supabase functions/policies, Vercel environment/readiness, Replit app identities, and available runners. Record unknowns explicitly; never fill gaps with assumptions.
2. **Restore one proven execution path:** use the existing Render Free preview + dedicated Supabase gateway as the current best zero-upfront-cost API Factory candidate; re-run external `/ready` and a harmless factory smoke. Do not modify the main service or EASY resources until state migration and gateway configuration are verified.
3. **Establish free inference evidence:** confirm an existing provider account and its official free tier before setting any billing-tier guard. Run exactly one non-sensitive deterministic sentinel request with paid fallback disabled. If no account is verified, use CI-local Ollama for development and continue provider-neutral work.
4. **Finish COLLECTION safely:** run cycle 19 as bounded incremental only, preserve blocked/deferred records, audit generated JSON and file-size guard, update the index with actual logs, and repeat until there is a deliberate stopping criterion. Do not auto-install when `NO_APPROVED_CANDIDATES`.
5. **Close the product path:** implement a real deployment adapter with completion polling, URL discovery, and post-deploy smoke; design durable state for generated APIs; publish one minimal API; verify a real user-facing request and a clear pricing/usage limit.
6. **Revenue validation:** select one product with a reachable, tested user path; do customer discovery/outreach only after the endpoint is usable; measure a real conversion before scaling or adding tools.

## 7. Evidence and safety rules

- A listed project/service, green CI, successful build, or HTTP health response is not by itself production readiness.
- Distinguish `PASS in CI`, `external smoke PASS`, `provider live completion PASS`, `durable state PASS`, and `revenue observed`.
- Do not store or expose API keys, tokens, passwords, raw environment values, or browser sessions in this document.
- Do not spend, upgrade plans, attach paid resources, deploy into EASY production, enable real trading, or bypass installation/provider gates without explicit approval.
- Every future inventory update must include: timestamp, source/tool evidence, counts/IDs, observed status, unknowns, and next action.
