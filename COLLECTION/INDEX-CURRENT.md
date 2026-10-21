# Current resource and Collection status — 2026-10-21

This short page is the live status pointer. The long [COLLECTION/INDEX.md](./INDEX.md) contains the historical log through cycle 23; this page supersedes it for the current snapshot.

## COLLECTION
- Latest completed: [cycle 28 — success](https://github.com/salamou1944/Project-/actions/runs/39676042890).
- Cycle 27: 69 refreshed, 31 blocked attempts preserved; 5,709 source rows; 5,678 extracted artifacts; 17,902 repositories deferred.
- Current-main JSON audit: 13,670 JSON/JSONC files, zero parse failures, 1,003,679,370 bytes.
- 50,600 capability/readiness groups; 34,751 promotion-review items; 15,849 restricted items.
- Install result: `NO_APPROVED_CANDIDATES`; zero installed.
- Cumulative cycles 1–27: 2,207 refreshed sources, 493 blocked attempts preserved.
- Current cycle: paused after [cycle 28 success](https://github.com/salamou1944/Project-/actions/runs/39676042890); see [detailed cycle 28 result](./CYCLE-28-RESULT.md). Do not trigger another harvest until partitioning is implemented and tested.
- Size warning: `READY.json` 88.9 MB, `CANONICAL-PROMOTION-PLAN.json` 60.1 MB, `PROMOTION-QUEUE.json` 52.6 MB. The 95 MB hard guard is still passing. Cycle 28 is the last bounded cycle before pausing extraction to implement and test non-destructive partitioning.

## Canonical inventory documents
- [Full resource inventory and execution plan](../VERIFICATION/RESOURCE_INVENTORY_AND_EXECUTION_PLAN_2026-10-21.md)
- [Resource verification delta](../VERIFICATION/RESOURCE_INVENTORY_DELTA_2026-10-21.md)
- [Revenue and creator account inventory](../VERIFICATION/REVENUE_ASSET_INVENTORY_2026-10-21.md)
- [Railway runtime triage](../VERIFICATION/RAILWAY_RUNTIME_TRIAGE_2026-10-21.md)
- [Railway authorization boundary](../VERIFICATION/RAILWAY_AUTH_BOUNDARY_2026-10-21.md)
- [API Factory runtime observations](../VERIFICATION/API_FACTORY_RUNTIME_OBSERVATIONS_2026-10-21.md)
- [ChatGPT plugin discovery](../VERIFICATION/CHATGPT_PLUGIN_DISCOVERY_2026-10-21.md)
- [Historical Collection log](./INDEX.md) — latest completed cycle is summarized above.

## API Factory / zero-cost model path
- API Factory Test passed on [run 39673899087](https://github.com/salamou1944/Salamou-31/actions/runs/39673899087).
- P1 Provider Probe Contract passed on [run 39673899241](https://github.com/salamou1944/Salamou-31/actions/runs/39673899241).
- SOAT Runtime Integration Smoke passed on [run 39673899084](https://github.com/salamou1944/Salamou-31/actions/runs/39673899084), including a real CI-local Ollama completion `4` and verified execution-contract transition. This is CI-local evidence, not production inference.
- These are contract/test evidence, not a production deploy or live hosted-provider completion.
- [Pollinations Classic candidate review](https://github.com/salamou1944/Salamou-31/blob/main/AI-API-HUB/api-factory/POLLINATIONS-CLASSIC-CANDIDATE-2026-10-21.md): official source reviewed; live sentinel and exact quota behavior not verified; provider remains fail-closed.
- Local Ollama completion `4` is proven in CI only, not on the user's PC. Local bridge runner is queued; Termalin has no reachable hosts.
