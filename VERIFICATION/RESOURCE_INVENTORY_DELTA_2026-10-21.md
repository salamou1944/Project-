# Resource inventory verification delta — 2026-10-21

This is a fresh verification delta from connected GitHub, Railway, Supabase, Render, Vercel, Replit, Notion, Termalin, and Plugin Management calls. It supplements [the canonical resource inventory and execution plan](./RESOURCE_INVENTORY_AND_EXECUTION_PLAN_2026-10-21.md). Secrets and raw environment values were not read.

## GitHub and execution

- Authenticated GitHub owner query returned exactly 10 repositories: 9 public and 1 private (`salamou1944/local-bridge.`). The separate known org repository `Sssssssddddd/.github` is not part of the owner-only list. This is a query-scope count, not a claim that the entire organization was exhaustively enumerated.
- The local machine inventory workflow [39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143) remains queued; older bridge diagnostics succeeded in October 13, but they do not prove a current machine runner is available.
- Termalin connector returns zero reachable hosts. No current local PC, Windows shell, or local Ollama access is proven.
- Latest COLLECTION harvest is [cycle 28, run 39676042890](https://github.com/salamou1944/Project-/actions/runs/39676042890): 68 refreshed, 32 blocked attempts preserved, 5,746 artifacts / 5,778 source rows, 17,834 deferred. Current-main audit: 13,738 JSON/JSONC files, zero parse failures, 1,011,256,549 bytes. The install gate is `NO_APPROVED_CANDIDATES`, zero installed.
- Large-file risk remains critical: `READY.json` is 89,789,053 bytes against a 95,000,000-byte guard. The isolated JSON shard I/O workflow [39678755963](https://github.com/salamou1944/Project-/actions/runs/39678755963) passed after earlier failures, but full migration/round-trip of production generated files and their readers is not yet proven. Keep harvest paused; do not trigger cycle 29 until end-to-end partitioning is integrated and verified.

## Runtime services

### Railway

- Two projects are visible: `EASY Runtime Production` and `EASY Developer Platform`; five services total.
- Environment descriptions show no attached volumes and no active deployment evidence; the latest recorded deployment for each service is failed. The service metadata's `state: live` field must not be mistaken for an active healthy deployment.
- `salamou31-api-factory` is located inside EASY Runtime Production. Its latest recorded deployment failed at `BUILD_IMAGE`; it has no attached volume and no production shared variables. Do not redeploy there or modify EASY production as an API Factory shortcut.
- The Railway Token Access Smoke [39673899369](https://github.com/salamou1944/Salamou-31/actions/runs/39673899369) failed with `Unauthorized`. The repository-stored token is invalid, expired, or lacks scope. Only the account owner should rotate it through secure Railway/GitHub settings; no token was read, copied, or changed.

### Render

- Workspace: `Salamou's workspace`.
- Two Free services exist:
  - Preview: [salamou31-api-factory-preview.onrender.com](https://salamou31-api-factory-preview.onrender.com), branch `fix/api-factory-live-storage-readiness-2026-10-20`.
  - Main: [salamou-31-api-factory.onrender.com](https://salamou-31-api-factory.onrender.com), branch `main`.
- Preview logs previously showed process startup and `GET /health` HTTP 200, but no fresh `/ready` success is evidenced in the latest queried window. Main is listed live but the queried window returned no application logs; prior readiness evidence was HTTP 503 `DURABLE_STORAGE_REQUIRED`. Neither service is currently proven production-ready. Free instances may sleep.

### Supabase

- `salamou-31-api-factory` (`dyhkdijpkddfsrwruumc`) reports `ACTIVE_HEALTHY`; `public.api_factory_registry` exists with RLS enabled and one row; active Edge Function `api-factory-storage` is version 3.
- `easy-platform-db` (`rdcodzowehzmwdxhztxe`) reports `ACTIVE_HEALTHY`; `public.pastel_orders` has 41 rows with RLS enabled; active Edge Functions are `easy-customer-auth`, `pastel-order`, `pastel-tts`, and `pastel-tts-v2`.
- These facts verify resource presence only. They do not prove API Factory production readiness, policy correctness, or that customer-facing endpoints work. Keep API Factory state separate from EASY data.

### Vercel

- Project `salamou31-api-factory` exists. Its latest listed production deployment is `READY`; recent staging deployments include both `READY` and `ERROR`. Project metadata reports `live:false`.
- Team-scope environment inspection remains blocked/unknown. A `READY` build is not evidence of correct runtime secrets, durable storage, or successful API requests.

## Apps, notes, and local access

- Replit lists three editable apps: `FragrantButteryApplicationframework`, `StarkImprobableText`, and `PracticalPastelCalculator`. Titles alone do not establish that these are the intended EASY prototype or production assets; resolve identity before edits.
- Notion has an existing private page, [جرد الموارد المتاحة وخطة التنفيذ — 2026-10-21](https://app.notion.com/p/400791c044f98169a48cfb4482a298b6?pvs=204), containing the current operating snapshot and historical notes. The shared-page query returned no pages; this does not prove the workspace is empty.
- Browser connector could not provide usable tabs because it requires the originating browser context. This session has not demonstrated desktop automation.
- Relevant connected tool surfaces successfully queried include GitHub, Railway, Supabase, Render, Vercel, Replit, Notion, Termalin, and Plugin Management. Additional namespaces exist, but a namespace or marketplace listing alone does not prove account access, quotas, or entitlement.
- Plugin discovery record [CHATGPT_PLUGIN_DISCOVERY_2026-10-21.md](./CHATGPT_PLUGIN_DISCOVERY_2026-10-21.md) is explicitly a targeted snapshot, not a complete export of every marketplace plugin. It records TinyFish as available but not installed/connected; it must not be counted as usable until connected and verified.

## API Factory and free inference

- API Factory Test [39673899087](https://github.com/salamou1944/Salamou-31/actions/runs/39673899087), P1 Provider Probe Contract [39673899241](https://github.com/salamou1944/Salamou-31/actions/runs/39673899241), and SOAT Runtime Integration Smoke [39673899084](https://github.com/salamou1944/Salamou-31/actions/runs/39673899084) passed. The SOAT completion `4` is a CI-local Ollama result, not proof of local PC access or production inference.
- [Pollinations Classic review](https://github.com/salamou1944/Salamou-31/blob/main/AI-API-HUB/api-factory/POLLINATIONS-CLASSIC-CANDIDATE-2026-10-21.md) records a plausible no-key candidate, but a live sentinel and exact quotas remain unverified. Keep it fail-closed and send no sensitive data to anonymous providers.
- [OmniRoute](https://github.com/diegosouzapw/OmniRoute) is a router, not free model entitlement. [awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) is a discovery list; every quota and term must be revalidated with the provider. ChatGPT subscription access does not automatically create a free API key or hosted inference endpoint.
- Real deployment adapter, externally verified `/ready`, durable usage/quota/idempotency state, a live hosted-model completion, and revenue from a usable API remain unproven.

## Ordered next steps

1. Keep COLLECTION harvesting paused; complete integrated, non-destructive JSON partitioning and prove round-trip compatibility against the actual large artifacts before resuming.
2. Verify the Render preview's external `/ready` and harmless factory request; do not claim readiness before both pass.
3. Resolve Vercel scope and Railway credential issues only through owner-controlled secure settings. Do not expose or copy secrets.
4. Execute one non-sensitive, no-paid-fallback inference sentinel only after an authorized execution path is available. Keep provider eligibility unknown until confirmed.
5. Continue remaining account/repository/service checks as explicit deltas; mark unknowns rather than filling gaps with assumptions.
6. Only after runtime acceptance, finish deployment execution + durable state, publish a usable API path, and measure a real customer conversion.

