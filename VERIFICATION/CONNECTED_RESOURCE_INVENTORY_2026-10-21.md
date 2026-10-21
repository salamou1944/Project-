# Connected Resource Inventory — 2026-10-21

Scope: all resources returned by the currently connected GitHub, Railway, Supabase, Render, Vercel, Replit, Notion, Termalin and browser connectors. This records the connected surface and its verified status, not every external account that may exist outside these connections. No secret values are recorded.

## Executive decision

1. Keep the Render preview as the current best zero-upfront-cost hosted API Factory test target; repository evidence records a successful durable-storage smoke. Render Free can sleep while idle, so this is not an uptime guarantee.
2. Do not call the Render main service production-ready: its latest recorded smoke returned HTTP 503 DURABLE_STORAGE_REQUIRED, with registry and artifact stores configured as local files.
3. Do not deploy API Factory into Railway's EASY Runtime Production project. The service has no variables or volume in the prior inspection and its latest known build failed during image preparation.
4. Use Ollama for local/CI development tests only. A GitHub Actions completion passed, but that is not proof of a public inference endpoint.
5. Gemini, Groq, OpenRouter free models, Mistral and Hugging Face remain unverified hosted options until the actual account/model eligibility is confirmed. Never use paid fallback.
6. Do not install OmniRoute yet. Its repository is MIT-licensed and it can simplify routing, but it does not grant free provider capacity; users supply their own provider accounts and keys.

## 1. GitHub repositories

The connected account returned admin/push permissions for these 10 repositories:

| Repository | Known role | Access |
|---|---|---|
| [Salamou-31](https://github.com/salamou1944/Salamou-31) | API Factory, provider gates, SOAT tests and deployment docs | Admin/push |
| [Project-](https://github.com/salamou1944/Project-) | COLLECTION extraction, queues, audits and research index | Admin/push |
| [agent-skills](https://github.com/salamou1944/agent-skills) | Control plane, skills and automation | Admin/push |
| [Easy-](https://github.com/salamou1944/Easy-) | EASY platform / creative engine | Admin/push |
| [AI_operating_memory](https://github.com/salamou1944/AI_operating_memory) | Canonical operating memory | Admin/push |
| [Astra](https://github.com/salamou1944/Astra) | ASTRA knowledge/evidence project | Admin/push |
| [Astra-](https://github.com/salamou1944/Astra-) | Separate ASTRA-related repository | Admin/push |
| [Files-](https://github.com/salamou1944/Files-) | File/resource project | Admin/push |
| [Pastel-](https://github.com/salamou1944/Pastel-) | Pastel project | Admin/push |
| [local-bridge.](https://github.com/salamou1944/local-bridge.) | Private repository; runner/share-metadata diagnostics workflows | Admin/push |

### GitHub execution evidence

- COLLECTION cycle 17 passed: [run 39517526827](https://github.com/salamou1944/Project-/actions/runs/39517526827). It selected 100 repos, refreshed 80, preserved 20 blocked attempts, reached 4,950 extracted source artifacts and 4,970 manifest source rows. Deferred queue: 18,630 repositories.
- Current-main JSON audit: 12,942 JSON/JSONC files, 0 parse failures, 907,402,672 bytes; status PASS.
- Latest installation gate: NO_APPROVED_CANDIDATES; 0 assets installed/promoted, 0 ready for verification, 0 runtime-readiness claims. Safe no-op, not installation success.
- API Factory CI at commit eb27d486bad2fff97802743ea727f8fa13ee491a: [API Factory Test](https://github.com/salamou1944/Salamou-31/actions/runs/39517350761), [SOAT Runtime Integration Smoke](https://github.com/salamou1944/Salamou-31/actions/runs/39517350895), [P1 Provider Probe Contract](https://github.com/salamou1944/Salamou-31/actions/runs/39517350886), [Railway Token Access Smoke](https://github.com/salamou1944/Salamou-31/actions/runs/39517350831) all passed. These prove tests/token access, not a production deployment or live provider access.
- Canonical COLLECTION index: [COLLECTION/INDEX.md](https://github.com/salamou1944/Project-/blob/main/COLLECTION/INDEX.md).

## 2. Railway

Workspace: salamou1944's Projects. Two projects and five services are visible.

| Project | Service | ID | Decision |
|---|---|---|---|
| EASY Runtime Production | easy-runtime-current | 520d3a93-7c36-4231-b172-05fb3685e96e | EASY runtime; do not disturb for API Factory |
| EASY Runtime Production | easy-runtime | 88769852-0456-478b-b453-b80bc3953231 | Existing EASY service; inspect before changing |
| EASY Runtime Production | salamou31-api-factory | 7e7bb8b8-25ff-43f5-a822-83983555812c | Poor isolation boundary; prior inspection found no variables/volume; latest known build failed during image preparation |
| EASY Developer Platform | soat-production-runtime | 27547a74-4179-4178-97e3-ce0b216103c2 | SOAT runtime |
| EASY Developer Platform | easy-platform-runtime-v3 | 721280c9-8045-4bcb-a932-3455866bae2b | EASY runtime v3 |

Both projects expose an environment named production. Railway Token Access Smoke passing does not mean a deployment succeeded. Do not deploy API Factory into the EASY project without an isolated service and verified storage/configuration.

## 3. Supabase

### Dedicated API Factory project
- Name: salamou-31-api-factory; ref: dyhkdijpkddfsrwruumc; region: eu-west-1; status reported ACTIVE_HEALTHY.
- Table: public.api_factory_registry; RLS enabled; one singleton row.
- Edge Function: api-factory-storage; ACTIVE version 3; JWT verification disabled, with its own internal key gate.
- Role: durable registry/artifact gateway for the Render preview. Readiness probes registry compare-and-swap/read-back and artifact upload/download.
- Never expose its internal key or service-role credential.

### EASY project
- Name: easy-platform-db; ref: rdcodzowehzmwdxhztxe; region: eu-west-1; status reported ACTIVE_HEALTHY.
- Table: public.pastel_orders; RLS enabled; 41 rows at inventory time.
- Active Edge Functions: easy-customer-auth v3, pastel-order v1, pastel-tts v1, pastel-tts-v2 v2.
- This is not the API Factory storage target. Do not mix EASY and API Factory credentials or data.

## 4. Render

Workspace ID: tea-daeb5h0n74is73d3qirg. Both services use the Salamou-31 repository and AI-API-HUB/api-factory Docker context. Auto-deploy on commit is enabled.

| Service | URL | Branch | Plan | Evidence / status |
|---|---|---|---|---|
| salamou31-api-factory-preview | https://salamou31-api-factory-preview.onrender.com | fix/api-factory-live-storage-readiness-2026-10-20 | Free | Repository records latest dual-endpoint smoke as DURABLE_STORAGE_VERIFIED / HTTP 200. Best current low-cost hosted test candidate; may sleep while idle. |
| salamou-31-api-factory | https://salamou-31-api-factory.onrender.com | main | Free | Latest recorded smoke: HTTP 503 DURABLE_STORAGE_REQUIRED, both stores local-file. Not production-ready; do not switch to the gateway until existing state and matching key are verified and safely migrated. |

## 5. Vercel

- Project: salamou31-api-factory; deployment URLs show team slug bleu5.
- The latest deployment list contained a production deployment in READY state and several staging deployments in ERROR state.
- READY means deployment provider status only; it does not prove app configuration or durable storage.
- Repository docs say Vercel remains fail-closed until the gateway URL and matching internal key are configured. Vercel /tmp is not durable.
- Decision: not the primary runtime until authenticated durable-storage readiness and external smoke pass.

## 6. Replit

The connected app listing currently exposes three editable apps:
- [FragrantButteryApplicationframework](https://replit.com/@salamou1944s/FragrantButteryApplicationframework), updated 2026-10-02.
- [StarkImprobableText](https://replit.com/@salamou1944s/StarkImprobableText), updated 2026-09-12.
- [PracticalPastelCalculator](https://replit.com/@salamou1944s/PracticalPastelCalculator), updated 2026-09-11.

A title search for EASY did not surface the known EASY creative prototype. These three results do not prove the prototype is absent from the Replit account.

## 7. Notion, Termalin and browser

- Notion: searches for COLLECTION and API Factory returned no matching pages; the page-list calls did not produce a usable content inventory. Do not treat Notion as the current source of project state; GitHub remains canonical.
- Termalin: connected host listing returned no hosts, so no server is available for command execution through this connector. This does not prove there are no saved hosts in the Termalin website account.
- Browser: the browser connector reported that access requires the originating browser context. No browser automation was counted as performed.

## 8. Free AI runtime options

| Option | Current status | What it offers | Boundary |
|---|---|---|---|
| Ollama | CI-local real completion passed | Local model inference for tests/dev when a reachable machine has sufficient resources | Not a public endpoint; CI-local is not the user's local machine |
| Google AI Studio / Gemini | NOT_VERIFIED | Possible hosted free-tier inference for eligible models/accounts | Probe made zero network requests because GOOGLE_AI_STUDIO_BILLING_TIER was empty |
| Groq | NOT_VERIFIED | Potential OpenAI-compatible hosted free-plan inference | Probe made zero network requests because GROQ_BILLING_TIER was empty |
| OpenRouter free models | NOT_VERIFIED | Routing to models explicitly listed as free | Requires account/key; limits change; no paid fallback |
| Mistral | NOT_VERIFIED | Possible limited/free tier depending on account/model | No live provider request proven |
| Hugging Face Inference Providers | NOT_VERIFIED | Potential limited credits/free access | Requires an explicitly verified free model/provider |
| OmniRoute | Source reviewed; not installed | MIT-licensed OpenAI-compatible router | Does not grant capacity; requires users' own provider accounts/keys; security/dependency/terms review still required |
| ChatGPT Free + Codex local | Supported coding route subject to plan limits | Coding agent in supported local/CLI/IDE client with ChatGPT sign-in | Not a general OpenAI API key, API quota or always-on endpoint; Codex Cloud is not included on Free/Go |
| GitHub Models | RETIRED | Do not use for new runtime work | GitHub announced inference API retirement on 2026-07-30 |

Full evidence and official sources: [API Factory zero-cost runtime options](https://github.com/salamou1944/Salamou-31/blob/main/AI-API-HUB/api-factory/FREE-ZERO-COST-RUNTIME-OPTIONS-2026-10-21.md).

## 9. What can be done now

### Without a new paid resource
- Continue bounded COLLECTION extraction, audits, classification and policy tests.
- Continue API Factory code/test work and provider adapters.
- Use the verified Render preview for limited external tests, with Free-tier sleep/availability limits.
- Use the dedicated Supabase gateway for preview registry/artifact persistence.
- Use Ollama for local/CI inference tests.
- Run hosted provider probes only after actual account/model free eligibility is confirmed and the corresponding billing-tier gate is explicitly set to free.

### Not yet proven ready
- API Factory main Render service with durable persistence.
- Vercel API Factory with configured durable storage.
- Railway API Factory deployment execution.
- A general ChatGPT-backed API or free OpenAI API quota.
- Live hosted completions on Gemini, Groq, OpenRouter, Mistral or Hugging Face.
- Durable per-generated-API business data, usage, quota and idempotency state.
- Any new COLLECTION installation: the latest gate approved no candidates.

## 10. Next execution order

1. Recheck the Render preview's live readiness and durable storage before relying on it.
2. Review provider probes and official terms; select one hosted provider only if account and model eligibility are confirmed, then run a real sentinel completion and save evidence.
3. Finish API Factory persistence for generated API usage/quota/idempotency/business state and test persistence across process restart.
4. Keep main Render and Vercel fail-closed until existing state/configuration is safely migrated and externally verified.
5. Continue COLLECTION in bounded cycles; reconcile each successful run's logs into the index. Do not promote assets unless the gate emits actual approved candidates.
6. Review OmniRoute's dependencies, security and provider terms before deciding whether to integrate it.

## Evidence policy

No secret values were recorded. No service was upgraded, no payment method was added, and no paid provider fallback was enabled for this inventory. Mutable provider terms and deployment status must be rechecked before production decisions.
