# Current resource and Collection status — 2026-10-27

This page is the current operational status pointer. Historical notes remain in [COLLECTION/INDEX.md](./INDEX.md).

## COLLECTION — latest status (cycle 31)

- Latest full cycle: [cycle 31 — success](https://github.com/salamou1944/Project-/actions/runs/40562723175).
- The approved MIT `mnfst/modelparams.dev` source is installed at exact revision `0d09d9a3fb642770430fb357e3c72f8e7d9f1f67` and is now `PROVEN_CALLABLE` in CI; 1 proven callable, 0 awaiting verification, 0 size-blocked. See [installed queue](./VERIFICATION/INSTALLED-QUEUE.json) and [callable evidence](./VERIFICATION/MODELPARAMS-CALLABLE-EVIDENCE.json).
- Verification: exact source comparison, 77 tests on upstream and installed copy, both builds passed, 0 production dependency vulnerabilities, source-boundary checks passed, and installed runtime smoke passed: [review run](https://github.com/salamou1944/Project-/actions/runs/40561509691). Real Gemini completion through API Factory also passed: [run](https://github.com/salamou1944/Salamou-31/actions/runs/40560609748).
- Production deployment remains **NOT_DEPLOYED**: Railway services are offline and the Railway account trial has expired. No paid upgrade was made. A free Render path is prepared but requires explicit workspace selection before provisioning.
- Full results: [CYCLE-31-RESULT.md](./CYCLE-31-RESULT.md). Cycle 30 and 29 details remain below as historical evidence.


- Latest full cycle: [cycle 30 — success](https://github.com/salamou1944/Project-/actions/runs/40445025946); install-selection contract: [PASS](https://github.com/salamou1944/Project-/actions/runs/40445025703).
- One exact-revision MIT asset is installed: `mnfst/modelparams.dev` at `0d09d9a3fb642770430fb357e3c72f8e7d9f1f67`. Installation outcome: 1 installed, 1 ready for verification, 0 size-blocked.
- Important distinction: installed does not mean callable. The verification queue still marks the asset `NOT_CALLABLE_UNTIL_RUNTIME_ENTRYPOINT_AND_EXECUTION_EVIDENCE`. The installed-copy gate passed in [run 40561005649](https://github.com/salamou1944/Project-/actions/runs/40561005649): byte-for-byte source comparison passed, 77 tests passed on both source and installed copy, both builds succeeded, production dependency audit found 0 vulnerabilities, and the runtime-source boundary scan passed. This proves CI-callable library execution, not a production deployment.
- API Factory integration has a successful real Gemini completion after fixing missing dependency installation in the workflow: [run evidence](https://github.com/salamou1944/Salamou-31/actions/runs/40560497900).
- Full cycle result: [CYCLE-30-RESULT.md](./CYCLE-30-RESULT.md). Cycle 29 details remain below as historical evidence.

## COLLECTION — cycle 29

- Latest completed full cycle: [cycle 29 — success](https://github.com/salamou1944/Project-/actions/runs/40436631814).
- Run scope: 100 repositories selected; 76 refreshed; 24 blocked attempts preserved; 5,846 source rows; 5,822 extracted artifacts; 31,513 repositories in inventory; 18,593 deferred repositories; 1,735 prior sources preserved but not selected.
- Manifest repair: 5,822 extracted artifacts validated; 0 invalid artifacts blocked; license metadata is carried forward from revision-validated extraction artifacts.
- Current-main JSON audit: 13,846 JSON/JSONC files, zero parse failures, 1,023,124,539 bytes.
- Latest semantic regression audit: [PASS](https://github.com/salamou1944/Project-/actions/runs/40438267766). It verifies 243 prior evidence records against exact historical source packets; 0 prior evidence identities are missing. Sixty-seven old BLOCKED_EXTERNAL_ACCESS inventory rows had no revision or artifact path and were correctly classified as metadata-only blocked discovery records, not extracted evidence.
- Large-state storage: READY.json has 51,667 decisions in 11 verified shards (90,695,293 bytes total; largest physical file 8,388,320 bytes). PROMOTION-QUEUE.json has 35,484 items in 7 shards (53,640,665 bytes total; largest 8,388,131 bytes). CANONICAL-PROMOTION-PLAN.json has 35,484 items in 8 shards (61,237,277 bytes total; largest 8,388,520 bytes). Shard hashes, item counts, semantic round trips, and JSON parse audit pass.
- Historical cycle 29 install result was NO_APPROVED_CANDIDATES. Cycle 30 later installed one approved asset; see the current status section and [cycle 30 result](./CYCLE-30-RESULT.md).
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
