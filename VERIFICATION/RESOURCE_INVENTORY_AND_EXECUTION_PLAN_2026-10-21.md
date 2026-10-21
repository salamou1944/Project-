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

- Latest successful bounded incremental run: [cycle 28, run 39676042890](https://github.com/salamou1944/Project-/actions/runs/39676042890).
- Cycle 28 selected 100 repositories; refreshed 68; preserved 32 blocked attempts; retained 5,746 extracted artifacts / 5,778 source rows; 17,834 repositories remain deferred.
- Current-main JSON audit: 13,738 JSON/JSONC files, zero parse failures, 1,011,256,549 bytes. Capability/readiness groups: 51,100; promotion-review items: 35,112; restricted items: 15,988.
- Installation result: `NO_APPROVED_CANDIDATES`; zero installed. This is a correct fail-closed outcome, not installation success.
- Cumulative cycles 1–28: 2,275 refreshed sources and 525 blocked attempts preserved.
- Harvesting is paused intentionally because generated JSON is approaching the 95 MB guard: `READY.json` 89,789,053 bytes; `CANONICAL-PROMOTION-PLAN.json` 60,680,934 bytes; `PROMOTION-QUEUE.json` 53,163,903 bytes. Do not trigger cycle 29 until non-destructive partitioning is integrated and verified end-to-end.
- Isolated JSON shard I/O tests passed on [run 39678755963](https://github.com/salamou1944/Project-/actions/runs/39678755963). Earlier attempts [39678601654](https://github.com/salamou1944/Project-/actions/runs/39678601654), [39678581571](https://github.com/salamou1944/Project-/actions/runs/39678581571), and [39677250418](https://github.com/salamou1944/Project-/actions/runs/39677250418) failed before the latest test passed. The passing isolated test is not yet proof that every large generated artifact and its readers/writers have been migrated safely.
- Current status pointer: [COLLECTION/INDEX-CURRENT.md](../COLLECTION/INDEX-CURRENT.md). Preserve blocked/deferred records and source order; do not install any asset unless the explicit policy gate approves it.

## 4. API Factory — verified state and actual ceiling

- Latest API Factory test passed: [run 39673899087](https://github.com/salamou1944/Salamou-31/actions/runs/39673899087). Provider contract passed: [run 39673899241](https://github.com/salamou1944/Salamou-31/actions/runs/39673899241). SOAT integration smoke passed: [run 39673899084](https://github.com/salamou1944/Salamou-31/actions/runs/39673899084), including a CI-local Ollama completion `4`. These are CI test evidence, not production inference.
- Supabase project `salamou-31-api-factory` (`dyhkdijpkddfsrwruumc`) reports `ACTIVE_HEALTHY`, with `public.api_factory_registry` (RLS enabled, one row) and active Edge Function `api-factory-storage` v3. This proves the resources exist, not that the deployed API passes external readiness.
- Render has two Free services: [preview](https://salamou31-api-factory-preview.onrender.com) and [main](https://salamou-31-api-factory.onrender.com). Preview logs previously showed process startup and `GET /health` HTTP 200, but no fresh `/ready` pass was observed in the latest recorded log window. Main service is listed live but had no logs in the queried window; prior readiness returned HTTP 503 `DURABLE_STORAGE_REQUIRED`. Neither endpoint is currently proven production-ready.
- Railway has five services across `EASY Runtime Production` and `EASY Developer Platform`. Environment checks report no active deployments and no attached volumes; latest recorded deployments failed. The API Factory Railway service is inside the EASY production project, with no attached volume and no production shared variables. Do not redeploy or change it as a shortcut.
- Vercel project `salamou31-api-factory` has a latest production deployment object in `READY` state, and recent staging deployments include both `READY` and `ERROR`. The project metadata reports `live:false`; team-scope environment inspection remains blocked/unknown. A successful build does not prove configured secrets, durable state, or correct request handling.
- Railway Token Access Smoke failed with `Unauthorized` on [run 39673899369](https://github.com/salamou1944/Salamou-31/actions/runs/39673899369). The stored repository token is invalid, expired, or lacks access. Never paste a token into chat; owner must rotate it through secure service/repository settings.
- Free inference candidate: [Pollinations Classic review](https://github.com/salamou1944/Salamou-31/blob/main/AI-API-HUB/api-factory/POLLINATIONS-CLASSIC-CANDIDATE-2026-10-21.md). Official source evidence exists, but a live sentinel and exact quota behavior are not verified. Keep the provider fail-closed and do not route sensitive data to anonymous endpoints.
- Local bridge inventory workflow [39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143) is still queued; Termalin currently reports zero reachable hosts. Local Ollama on the user's PC is therefore not proven available.
- The real deployment adapter, externally verified `/ready`, durable API usage/quota/idempotency state, live hosted-provider completion, and revenue from a usable API remain unproven.

## 5. Free model / “ChatGPT account” finding

- Supported ChatGPT Free Codex access can be useful for local coding-agent work subject to plan limits; it is not a general OpenAI API key, free API quota, or always-on inference endpoint.
- GitHub Models inference was retired on 2026-07-30; do not use old GitHub Models examples as a live runtime.
- Ollama is the most direct no-hosted-API-bill test path, but local hardware/installation is unverified through the current Termalin/browser connections.
- Next hosted candidates are Gemini free tier, Groq free plan, and OpenRouter `:free` models, but each current probe deliberately skipped requests because account/model free-tier eligibility was not explicitly confirmed. No live hosted completion is proven. Never send secrets/customer/confidential data to a free tier with data-use terms not approved; no paid fallback.
- [OmniRoute](https://github.com/diegosouzapw/OmniRoute) is an open-source OpenAI-compatible router, not a provider quota grant. It requires user-owned provider accounts/keys; the ChatGPT Web/Codex adapter is not accepted as a supported production inference route without code and terms review.
- [awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) is a discovery list (CC0-1.0); provider entries and quotas must be independently revalidated against official pricing/terms.

## 6. Execution plan, ordered by dependency

1. **Finish the safe inventory delta first:** the owner repository query confirms 10 repositories (9 public, 1 private: `local-bridge.`). The separate known organization repository `Sssssssddddd/.github` is not included in that owner-only list. Do not infer more organization access from it. Current inventory still needs explicit checks for every relevant repository's current workflow/runner and project-specific runtime behavior.
2. **Resolve the COLLECTION file-size risk before more harvesting:** cycle 28 is the latest successful harvest. The isolated shard I/O test now passes, but the full partition/manifest migration, source-order preservation, read compatibility, and round-trip verification across the actual large generated files must pass before cycle 29 is triggered. Keep all blocked/deferred records; no destructive rebuild.
3. **Prove one API Factory path without spending:** use the existing Render Free preview plus its dedicated Supabase gateway as the leading candidate. The next acceptance gate is an external `/ready` success that proves registry and artifact write/read verification, followed by one harmless factory request. Current recorded evidence is not sufficient to call it ready.
4. **Verify a genuinely free inference path:** Pollinations Classic is a candidate, not a live-verified provider. Use a single non-sensitive deterministic sentinel only when a safe execution path exists; paid fallback must be disabled. Keep Gemini, Groq, OpenRouter, and other tiers unverified until account eligibility and official terms are confirmed.
5. **Restore secure deployment access only through owner-controlled settings:** Railway workflow token smoke currently fails Unauthorized. Do not copy tokens from connected services, reveal secrets, or redeploy into EASY production. Vercel environment inspection remains blocked by team-scope authorization.
6. **Close the product and revenue path after runtime acceptance:** implement a real deployment adapter with completion polling, URL discovery, and post-deploy smoke; implement durable generated-API usage/quota/idempotency state; publish one minimal API; verify a real user-facing request, then perform targeted outreach and measure a real conversion.
7. **Operating rule:** after each phase, record exact evidence and only then advance. Distinguish CI pass, external smoke pass, live-provider completion, durable-state pass, and revenue observed. No paid upgrades, paid resources, real trading, destructive rebuilds, or bypass of approval gates.

## 7. Evidence and safety rules

- A listed project/service, green CI, successful build, or HTTP health response is not by itself production readiness.
- Distinguish `PASS in CI`, `external smoke PASS`, `provider live completion PASS`, `durable state PASS`, and `revenue observed`.
- Do not store or expose API keys, tokens, passwords, raw environment values, or browser sessions in this document.
- Do not spend, upgrade plans, attach paid resources, deploy into EASY production, enable real trading, or bypass installation/provider gates without explicit approval.
- Every future inventory update must include: timestamp, source/tool evidence, counts/IDs, observed status, unknowns, and next action.
