# Current resource and Collection status — 2026-10-27

This page is the current operational status pointer. Historical notes remain in [COLLECTION/INDEX.md](./INDEX.md).

## COLLECTION — cycle 29

- Latest completed full cycle: [cycle 29 — success](https://github.com/salamou1944/Project-/actions/runs/40436631814).
- Run scope: 100 repositories selected; 76 refreshed; 24 blocked attempts preserved; 5,846 source rows; 5,822 extracted artifacts; 31,513 repositories in inventory; 18,593 deferred repositories; 1,735 prior sources preserved but not selected.
- Manifest repair: 5,822 extracted artifacts validated; 0 invalid artifacts blocked; license metadata is carried forward from revision-validated extraction artifacts.
- Current-main JSON audit: 13,846 JSON/JSONC files, zero parse failures, 1,023,124,539 bytes.
- Latest semantic regression audit: [PASS](https://github.com/salamou1944/Project-/actions/runs/40438267766). It verifies 243 prior evidence records against exact historical source packets; 0 prior evidence identities are missing. Sixty-seven old BLOCKED_EXTERNAL_ACCESS inventory rows had no revision or artifact path and were correctly classified as metadata-only blocked discovery records, not extracted evidence.
- Large-state storage: READY.json has 51,667 decisions in 11 verified shards (90,695,293 bytes total; largest physical file 8,388,320 bytes). PROMOTION-QUEUE.json has 35,484 items in 7 shards (53,640,665 bytes total; largest 8,388,131 bytes). CANONICAL-PROMOTION-PLAN.json has 35,484 items in 8 shards (61,237,277 bytes total; largest 8,388,520 bytes). Shard hashes, item counts, semantic round trips, and JSON parse audit pass.
- Install result remains NO_APPROVED_CANDIDATES: 0 installed; 0 ready for verification; 0 size-blocked. This is fail-closed because candidate approval and integration/security gates are still unverified, not because the installer crashed. No asset was falsely marked usable.
- Weekly full-cycle schedule is enabled for Sundays at 05:20 UTC on main, after the deep-extraction refresh at 03:20 UTC. Marker-triggered runs and the writer job are now restricted to main; see [workflow scheduling PR #50](https://github.com/salamou1944/Project-/pull/50).
- Implementation and verification PRs: [#48 — shard I/O + license repair](https://github.com/salamou1944/Project-/pull/48), [#51 — historical semantic audit recovery](https://github.com/salamou1944/Project-/pull/51). Detailed evidence: [cycle 29 result](./CYCLE-29-RESULT.md).

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
