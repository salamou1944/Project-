# ASTRA / FREE / PROJECT CONTINUATION STATE — 2026-09-25

## Repository identity
- Canonical ASTRA implementation: `salamou1944/Astra`
- `salamou1944/Astra-`: separate minimal "Bot" repository; it currently contains README.md plus a collection/aw-junaid tree. It is not the canonical quant research implementation.
- `salamou1944/Project-`: public central collection repository. Its README/description currently identify it as "Free".
- A separate repository literally named `Free` was not found in the current GitHub account repository search. Therefore "Free" is currently mapped to the Project- repository unless a different repository is created/renamed later.

## ASTRA verified current state
Source commit/file evidence:
- README: v1.7.0; 49/49 local regression; REAL_DATA proven through GitHub-hosted runner using Kraken public REST; 721 daily rows per asset; BTC/USD, ETH/USD, SOL/USD, LTC/USD; dataset SHA-256 persisted.
- Research gate: FAIL. BTC-only candidate tournament: 123 candidates, gate failed.
- Cross-asset research: 4 assets x 4 chronological folds; equal-weight aggregate -6.8715%; positive asset-fold ratio 25%; max asset drawdown 37.3515%; gate failed.
- Untouched 100-bar holdout exists; selected long_momentum result remained below buy-and-hold benchmark; statistical reality check did not establish profitability/alpha.
- Risk/shadow evidence: max-drawdown halt, 0 broker orders.
- Live-money execution: OFF.
- HANDOVER requires continued prospective observation; current prospective workflow must report INSUFFICIENT_FORWARD_SAMPLE until every asset has at least 30 post-holdout daily bars.
- Required live gates remain DATA_VALID, STRATEGY_VALID, RISK_VALID, EXECUTION_VALID, RECONCILIATION_VALID, KILL_SWITCH_VALID, HUMAN_APPROVAL, LIVE_ENABLED; human approval cannot be inferred.

## Next ASTRA execution frontier
1. Continue real-data/prospective evidence accumulation without touching the final holdout.
2. Inspect the prospective validation script and CI workflow for actual data boundary, freshness, per-asset coverage and failure handling.
3. Inspect evidence JSON artifacts and source/data fingerprints.
4. Attack the data/verification boundary for false-positive states before any strategy changes.
5. Keep live execution disabled unless every explicit gate is independently proven.

## FREE / Project collection state
Project- remains the central store for the broad collection. Preserve:
- free/open-source/self-hosted candidates;
- licensing and cloud/paid boundaries;
- dependencies, deployment, security and limitations;
- reusable implementation patterns;
- provenance and revision;
- discovered -> inspected -> extracted -> verified -> reusable state separation.

No completion claim is made here. Collection remains active.
