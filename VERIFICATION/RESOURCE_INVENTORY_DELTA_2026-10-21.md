# Current resource verification — 2026-10-21

Supplement to [the full inventory and plan](./RESOURCE_INVENTORY_AND_EXECUTION_PLAN_2026-10-21.md).

## New observations

- Railway environment-status checks show all five services offline, with no active deployments and no attached volumes. The EASY Developer Platform environment reports warnings on both services.
- Render lists both API Factory services as live deployments. This is not enough to prove runtime readiness. Existing documented evidence says the preview previously passed durable-storage verification and the main endpoint previously returned HTTP 503 `DURABLE_STORAGE_REQUIRED`. The available web connector could not fetch the public runtime endpoints, so no fresh HTTP success is claimed.
- Vercel production and staging deployment objects queried are `READY` at build level. Environment metadata access returned HTTP 403 for team scope `bleu5`; the configuration audit is blocked and remains unknown.
- The OpenAI Platform connector listed three selectable targets: `Team easy / Easy`, `PERSONEL / Default project`, and `Personal / Default project`. This is account-target metadata, not proof of usable free inference.
- Termalin reports zero reachable hosts. Local bridge inventory run [39519079143](https://github.com/salamou1944/local-bridge./actions/runs/39519079143) remains queued; the machine inventory has not executed. Browser access also requires the originating browser context.
- Groq and OpenRouter probes [39515881263](https://github.com/salamou1944/Salamou-31/actions/runs/39515881263) passed as safe no-ops: `NOT_VERIFIED`, free-tier eligibility not explicitly confirmed, zero network requests. No live hosted-model completion is proven.

## COLLECTION continuation

- Cycle 19 run [39671402767](https://github.com/salamou1944/Project-/actions/runs/39671402767) completed successfully. It selected 100 repositories, refreshed 76, preserved 24 blocked attempts, and left 18,475 repositories deferred; 5,105 artifacts / 5,129 source rows were retained. The current-main audit passed for 13,097 JSON/JSONC files, zero parse failures, and 927,313,684 bytes. Capability/readiness groups: 46,015; promotion-review items: 31,525; restricted items: 14,490. Installation returned `NO_APPROVED_CANDIDATES` (zero installed).
- Cycle 20 was triggered by marker commit [4477f0f](https://github.com/salamou1944/Project-/commit/4477f0fab550a5a5796a925f98cd1b7dfc2a366b); verify its final logs before publishing counts.
- Cycle-18 baseline: 79/100 refreshed, 21 blocked attempts preserved, 5,029 extracted artifacts / 5,050 source rows, 18,551 deferred repositories, 13,021 JSON/JSONC files audited, zero parse failures, and `NO_APPROVED_CANDIDATES`.

## Next actions

1. Verify cycle 19 from its final workflow logs.
2. Diagnose why all Railway services are offline; do not redeploy into EASY production.
3. Resolve Vercel team-scope authorization through an approved flow before inspecting configuration.
4. Re-run durable-readiness smoke against the existing Render preview before relying on it.
5. Keep provider eligibility guards unchanged until official free eligibility is confirmed.
6. Treat local inference as unavailable until the local runner executes or Termalin reports a reachable host.
