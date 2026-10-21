# Resource inventory verification — 2026-10-22

## Purpose and method

This is a dated, evidence-backed inventory of the connected ChatGPT tool surface and the assets actually visible through the currently authorized connectors. It is not a claim that hidden account settings, billing plans, secret values, private browser sessions, or unconnected local machines were inspected. No secret values were read, copied, or stored. No paid service was activated, no deployment was triggered, no message was sent, and no Collection data was deleted or rebuilt during this audit.

## 1. Current verified account/resource state

### GitHub

- Owner-scoped query for `salamou1944` returned exactly 10 repositories: 9 public and 1 private (`local-bridge.`). The query used offset 0 and 100; offset 100 returned no further repositories.
- Repositories: [Salamou-31](https://github.com/salamou1944/Salamou-31), [agent-skills](https://github.com/salamou1944/agent-skills), [Easy-](https://github.com/salamou1944/Easy-), [AI_operating_memory](https://github.com/salamou1944/AI_operating_memory), [Astra](https://github.com/salamou1944/Astra), [Astra-](https://github.com/salamou1944/Astra-), [Files-](https://github.com/salamou1944/Files-), [Pastel-](https://github.com/salamou1944/Pastel-), [Project-](https://github.com/salamou1944/Project-), and private [local-bridge.](https://github.com/salamou1944/local-bridge.).
- Separate known organization repository: [Sssssssddddd/.github](https://github.com/Sssssssddddd/.github). Current owner/org-membership query does not establish broader organization access.
- [COLLECTION cycle 28](https://github.com/salamou1944/Project-/actions/runs/39676042890) succeeded: 68 refreshed, 32 blocked attempts preserved, 5,746 extracted artifacts / 5,778 source rows, 17,834 deferred. Audit: 13,738 JSON/JSONC files, zero parse failures, 1,011,256,549 bytes; capability/readiness groups 51,100; promotion-review items 35,112; restricted items 15,988. Install gate: `NO_APPROVED_CANDIDATES`, zero installed.
- COLLECTION harvesting is intentionally paused: `READY.json` is 89,789,053 bytes against a 95,000,000-byte guard; `CANONICAL-PROMOTION-PLAN.json` is 60,680,934 bytes; `PROMOTION-QUEUE.json` is 53,163,903 bytes. The isolated shard round-trip/hash/baseline test passed on [run 39678755963](https://github.com/salamou1944/Project-/actions/runs/39678755963), but full production-reader/writer migration and semantic equivalence are not proven. Do not trigger cycle 29 yet.
- The shard test branch is `feat/collection-json-shards-2026-10-22`. The passing run tests only the isolated JSON I/O helper, not the full collection pipeline.

### Railway

- Two projects, one workspace:
  - `EASY Runtime Production` — production environment ID `8d7d14f5-a795-462d-859e-2c3249bd82ee`
  - `EASY Developer Platform` — production environment ID `ae3d2189-2aa5-4c5e-8ee8-9bfdc45dc2a4`
- Five services total: `easy-runtime-current`, `salamou31-api-factory`, `easy-runtime`, `easy-platform-runtime-v3`, `soat-production-runtime`.
- Latest recorded deployments for all five services are FAILED; no volumes or buckets are attached. `EASY Runtime Production` has no shared variable names; `EASY Developer Platform` exposes the shared variable name `Easy_github_token` (value was not read).
- `salamou31-api-factory` is inside the EASY production project and its latest recorded deployment is failed. Do not redeploy it into EASY or modify its variables as a shortcut.
- The Railway token smoke failed with Unauthorized on [run 39679784463](https://github.com/salamou1944/Salamou-31/actions/runs/39679784463). The repository credential needs owner-controlled secure rotation; never paste it into chat.

### Supabase

- `salamou-31-api-factory` project `dyhkdijpkddfsrwruumc`: status `ACTIVE_HEALTHY`; table `public.api_factory_registry` exists with RLS enabled and 1 row; Edge Function `api-factory-storage` is ACTIVE at v3.
- `easy-platform-db` project `rdcodzowehzmwdxhztxe`: status `ACTIVE_HEALTHY`; table `public.pastel_orders` exists with RLS enabled and 41 rows; Edge Functions `easy-customer-auth`, `pastel-order`, `pastel-tts`, and `pastel-tts-v2` are ACTIVE.
- Database/project health is not proof that API Factory passes external readiness. Keep EASY state separate from API Factory state.

### Vercel

- One project visible: `salamou31-api-factory`.
- Latest listed production deployment `salamou31-api-factory-h82t0tc1b-bleu5.vercel.app` is marked READY; the latest listed staging deployment `salamou31-api-factory-6tnjvu6p2-bleu5.vercel.app` is marked READY. Recent staging deployments also include ERROR states.
- Deployment READY means build/deployment status only; configured environment, durable storage, correct request behavior, and external `/ready` have not been freshly proven. Team-scoped configuration access remains limited.

### Render

- Previously verified workspace: `Salamou's workspace`; two API Factory Free services are recorded:
  - Main: https://salamou-31-api-factory.onrender.com
  - Preview: https://salamou31-api-factory-preview.onrender.com
- Prior main readiness returned HTTP 503 `DURABLE_STORAGE_REQUIRED`; preview previously returned HTTP 200 for `/health`, but a fresh `/ready` pass was not established. Service presence/live labels do not establish readiness. No redeploy was made.

### Replit

- Three editable apps surfaced: `FragrantButteryApplicationframework`, `StarkImprobableText`, `PracticalPastelCalculator`.
- None is assumed to be the EASY prototype without identity/source verification.

### Notion

- Connected identity: workspace `Salamou Salamou’s Space`.
- A private page exists: [جرد الموارد المتاحة وخطة التنفيذ — 2026-10-21](https://app.notion.com/p/400791c044f98169a48cfb4482a298b6?pvs=204). It records the operating plan and previous evidence. A search is not a complete workspace export.
- Keep Notion as an operating notebook; GitHub remains canonical for code, test evidence, and versioned resource inventory.

### Termalin and browser/computer access

- Termalin returns zero reachable hosts and explicitly says saved hosts in the web cabinet are not automatically visible to this connector until a connector runs on the host.
- Private GitHub runner workflow [Local bridge one-shot machine inventory, run 39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143) remains QUEUED. Older bridge checks passed on 2026-10-13 but do not prove current access.
- Browser connector returns that access requires the originating browser context. No live desktop/browser control is established. Do not claim that the user's local PC, local Ollama, or a Windows shell is reachable.

### OpenAI Platform / ChatGPT

- OpenAI Platform key-setup target discovery returned 3 organization/project targets (`Team easy/Easy`, `PERSONEL/Default project`, `Personal/Default project`). No API key was created and no free API quota/billing entitlement was proven.
- A ChatGPT Free/Codex subscription may support local coding-agent work within plan limits, but it is not a general OpenAI API key or an always-on inference service.
- OmniRoute documents a Codex App-Server integration that uses the official Codex CLI app-server/device OAuth. This remains source-verified only: there is no currently verified host with persistent storage to run it privately. Do not use the separate token-replay mode, expose OAuth tokens, or present a ChatGPT subscription as unrestricted production API capacity.
- [Pollinations Classic candidate review](https://github.com/salamou1944/Salamou-31/blob/main/AI-API-HUB/api-factory/POLLINATIONS-CLASSIC-CANDIDATE-2026-10-21.md): source review supports a possible no-key Classic endpoint, but no live sentinel request has been verified. Anonymous endpoint privacy/rate limits are not suitable for sensitive data or unreviewed production routing.
- [Zero-cost runtime options](https://github.com/salamou1944/Salamou-31/blob/main/AI-API-HUB/api-factory/FREE-ZERO-COST-RUNTIME-OPTIONS-2026-10-21.md) ranks local Ollama for development/CI, then Google AI Studio/Groq/OpenRouter only after account-specific free-tier terms are confirmed. Recent safe provider probes made zero network requests when billing tier was unspecified. GitHub Models was retired on 2026-07-30.

## 2. Revenue/creator resources already inventoried

The latest read-only snapshot is [REVENUE_ASSET_INVENTORY_2026-10-21.md](./REVENUE_ASSET_INVENTORY_2026-10-21.md). Key facts:
- AgentMail: 3 inboxes; the two outreach inboxes had only delivery-failure/bounce threads in the latest review, no customer reply evidenced.
- Apollo: 80 lead credits, 150 conversation credits, 5,000 AI credits, 50,000 broadcast credits, 20 inbound visitor credits; export credits 0. Direct-dial counts disagree, so treat as unknown.
- Upwork: private profile, zero Connects, zero completed jobs.
- HubSpot: 2 contacts, 1 company, 0 deals, tickets, products, invoices.
- Shopify: one Algeria/DZD trial store, not ready for selling without upgrade.
- Wix: no sites returned.
- Canva: no indexed designs found in the queried search (not proof of none anywhere).
- Figma: Starter/View, one View seat; Code Layers and Specs disabled.
- Higgsfield: Free, 10 credits; eligible 100-credit trial pending and not started.
- GitLab: one private empty project.
- Metricool: one brand linked to a YouTube channel; this is not proof of published content or revenue.
- Automations: five jobs recorded; only `Revenue + leverage sweep` enabled, but next-run is null; scheduler reliability unknown.

No email was sent, no trial started, no purchase/upgrade made, and no creative credits spent during the prior inventory.

## 3. Available connected tool namespaces in this ChatGPT session

Tool-surface inventory below is generated from the currently exposed tool catalog at audit time. Presence means a connector/tool surface is exposed, not that the associated external account has resources or full permissions.

| Namespace | Exposed tools | Interpretation |
|---|---:|---|
| `AgentMail` | 51 | Available tool surface; account/resource access is verified separately |
| `Apollo_io` | 64 | Available tool surface; account/resource access is verified separately |
| `Automations` | 7 | Available tool surface; account/resource access is verified separately |
| `BetterMenu` | 62 | Available tool surface; account/resource access is verified separately |
| `Binance` | 90 | Available tool surface; account/resource access is verified separately |
| `Browser` | 2 | Available tool surface; account/resource access is verified separately |
| `Canva` | 40 | Available tool surface; account/resource access is verified separately |
| `Code_Tytor` | 11 | Available tool surface; account/resource access is verified separately |
| `Composio` | 11 | Available tool surface; account/resource access is verified separately |
| `Figma` | 44 | Available tool surface; account/resource access is verified separately |
| `GitBook` | 11 | Available tool surface; account/resource access is verified separately |
| `GitHub` | 89 | Available tool surface; account/resource access is verified separately |
| `GitLab` | 128 | Available tool surface; account/resource access is verified separately |
| `Higgsfield` | 143 | Available tool surface; account/resource access is verified separately |
| `HubSpot` | 34 | Available tool surface; account/resource access is verified separately |
| `LinkedIn` | 1 | Available tool surface; account/resource access is verified separately |
| `Metricool` | 9 | Available tool surface; account/resource access is verified separately |
| `Notion` | 91 | Available tool surface; account/resource access is verified separately |
| `OpenAI_Platform` | 3 | Available tool surface; account/resource access is verified separately |
| `Plugin_Management` | 6 | Available tool surface; account/resource access is verified separately |
| `Railway` | 69 | Available tool surface; account/resource access is verified separately |
| `Render` | 23 | Available tool surface; account/resource access is verified separately |
| `Replit` | 8 | Available tool surface; account/resource access is verified separately |
| `Shopify` | 43 | Available tool surface; account/resource access is verified separately |
| `Supabase` | 29 | Available tool surface; account/resource access is verified separately |
| `Termalin` | 16 | Available tool surface; account/resource access is verified separately |
| `TriAstra_Astrology` | 1 | Available tool surface; account/resource access is verified separately |
| `Upwork` | 50 | Available tool surface; account/resource access is verified separately |
| `Vercel` | 235 | Available tool surface; account/resource access is verified separately |
| `Wix` | 31 | Available tool surface; account/resource access is verified separately |

Other exposed surfaces include Browser (2 tools), local handoff, image generation, web search, Python, and file utilities. Browser access itself failed because the originating browser context was unavailable.

## 4. Current execution plan — evidence gates

### P0 — preserve state and stop uncontrolled growth

- Keep COLLECTION harvest paused while generated JSON files approach the 95 MB guard.
- Do not delete, rebuild, compact destructively, overwrite source records, or trigger cycle 29 until a reversible partitioning migration is proven.
- Preserve source order, IDs, hashes, blocked/deferred records, and exact semantic equivalence.

### P1 — finish COLLECTION partition migration

1. Review the passing isolated shard I/O implementation and its tests on `feat/collection-json-shards-2026-10-22`.
2. Inventory every writer and reader of `READY.json`, `CANONICAL-PROMOTION-PLAN.json`, `PROMOTION-QUEUE.json`, and related generated artifacts.
3. Integrate shard read/write support into all producers, validators, capability listing, installation-selection, and recovery paths.
4. Add full-scale migration tests: baseline vs sharded semantic equivalence; stable order and IDs; hash/count equality; empty/single/multi-shard behavior; interrupted write recovery; legacy reader compatibility; size guard.
5. Run the complete COLLECTION test matrix against a fixture and a copy of current generated state. Only then open/merge a reviewed PR and resume one bounded cycle.

### P2 — make API Factory actually ready

1. Keep API Factory separate from EASY production.
2. Verify the active Supabase gateway's auth boundary and storage write/readback without exposing credentials.
3. Resolve Render/Vercel configuration and run external `/health` and `/ready` checks against the intended isolated deployment.
4. Implement or verify the real provider execution adapter, quota/usage/idempotency persistence, and error behavior.
5. Only promote after an actual non-sensitive completion, durable read/write evidence, and endpoint smoke pass. CI-local Ollama is not production inference.

### P3 — free inference and ChatGPT/Codex

1. Treat OmniRoute/Codex App-Server as a candidate for coding-agent work, not a public ChatGPT API.
2. First establish a private persistent execution host; current Termalin and local-bridge evidence does not establish one.
3. If a host becomes available, inspect official Codex CLI/app-server support and OmniRoute's exact deployment/security model; use device OAuth, keep credentials private, and test only within the user's existing plan limits.
4. In parallel, select one provider with verified account-specific free tier; make one non-sensitive sentinel request with no paid fallback. Record `NOT_VERIFIED` if credentials/terms/host are missing.

### P4 — revenue path with no upfront spend

1. Resolve delivery failure causes before sending more outreach through AgentMail.
2. Use Apollo for qualified prospect discovery only after selecting one offer and verifying official recipient channels.
3. Build a minimal HubSpot deal pipeline only when qualified prospects exist; do not confuse sent outreach with delivery, response, conversion, or revenue.
4. Avoid Upwork proposals while Connects = 0; do not upgrade Shopify or start paid trials.

### P5 — complete account and plugin inventory

- Use the namespace table as the full currently exposed tool-surface list, then inspect actual account resources/permissions per connector before assigning it work.
- Prioritize remaining resource checks by whether they unblock P1/P2 or revenue; do not spend credits or alter services during inventory.
- Record any integration that cannot be inspected due to missing authorization/context as **not verified**, never silently treat it as empty.

## 5. Exit criteria for calling the inventory complete enough to plan

- Every currently exposed connector namespace is listed.
- Each priority asset has: identity, owner/workspace, current state, evidence URL/ID, cost/usage boundary, permissions/blocker, and next safe action.
- Every unknown is explicitly scoped (e.g. external account billing terms not visible, browser origin unavailable) rather than hidden behind a general "inventory incomplete" label.
- COLLECTION is paused safely, API Factory production claims are gated on external readiness, and no paid resource or credential has been activated by this audit.
