# Current resource and Collection status — 2026-10-21

This short page is the live status pointer. The older [COLLECTION/INDEX.md](./INDEX.md) remains the long historical log; use this page for the current snapshot.

## COLLECTION
- Latest completed: [cycle 24 — success](https://github.com/salamou1944/Project-/actions/runs/39674187945).
- Cycle 24: 70 refreshed, 30 blocked attempts preserved; 5,501 source rows; 5,471 extracted artifacts; 18,109 repositories deferred.
- Current-main JSON audit: 13,463 JSON/JSONC files, zero parse failures, 976,652,278 bytes.
- 49,020 capability/readiness groups; 33,658 promotion-review items; 15,362 restricted items.
- Install result: `NO_APPROVED_CANDIDATES`; zero installed.
- Cumulative cycles 1–24: 2,000 refreshed sources, 400 blocked attempts preserved.
- Current cycle: [cycle 25, run 39674669139](https://github.com/salamou1944/Project-/actions/runs/39674669139), currently in progress. Do not publish counts until its logs finish.
- Size warning: `READY.json` 85.9 MB, `CANONICAL-PROMOTION-PLAN.json` 58.1 MB, `PROMOTION-QUEUE.json` 50.9 MB. The 95 MB hard guard is still passing; a non-destructive partitioning plan is needed before approaching it.

## Canonical inventory documents
- [Full resource inventory and execution plan](../VERIFICATION/RESOURCE_INVENTORY_AND_EXECUTION_PLAN_2026-10-21.md)
- [Resource verification delta](../VERIFICATION/RESOURCE_INVENTORY_DELTA_2026-10-21.md)
- [Revenue and creator account inventory](../VERIFICATION/REVENUE_ASSET_INVENTORY_2026-10-21.md)
- [Railway runtime triage](../VERIFICATION/RAILWAY_RUNTIME_TRIAGE_2026-10-21.md)
- [Railway authorization boundary](../VERIFICATION/RAILWAY_AUTH_BOUNDARY_2026-10-21.md)
- [Railway authorization boundary](../VERIFICATION/RAILWAY_AUTH_BOUNDARY_2026-10-21.md)
- [API Factory runtime observations](../VERIFICATION/API_FACTORY_RUNTIME_OBSERVATIONS_2026-10-21.md)
- [ChatGPT plugin discovery](../VERIFICATION/CHATGPT_PLUGIN_DISCOVERY_2026-10-21.md)
- [Historical Collection log](./INDEX.md) — latest completed cycle is summarized above.

## API Factory / zero-cost model path
- API Factory Test passed on [run 39673899087](https://github.com/salamou1944/Salamou-31/actions/runs/39673899087).
- P1 Provider Probe Contract passed on [run 39673899241](https://github.com/salamou1944/Salamou-31/actions/runs/39673899241).
- These are contract/test evidence, not a production deploy or live hosted-provider completion.
- [Pollinations Classic candidate review](https://github.com/salamou1944/Salamou-31/blob/main/AI-API-HUB/api-factory/POLLINATIONS-CLASSIC-CANDIDATE-2026-10-21.md): official source reviewed; live sentinel and exact quota behavior not verified; provider remains fail-closed.
- Local Ollama completion `4` is proven in CI only, not on the user's PC. Local bridge runner is queued; Termalin has no reachable hosts.
