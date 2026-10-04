# Panniantong Account Execution Capture — 2026-10-04

## Account-first discovery

Target account: `Panniantong`
Public repositories enumerated through the linked GitHub connection: **38**.

This capture is an account-level source record, not a duplicate repository catalog. Existing Agent-Reach material remains authoritative where already captured; this record adds the account-wide execution result and the newly extracted capability.

## Highest-value reusable sources

- `Panniantong/Agent-Reach` — multi-platform research routing and backend health/selection patterns.
- `Panniantong/last30days-skill` — multi-source recent research, recency windows, deduplication, relevance/engagement scoring, cross-source convergence, grounded citations.
- `Panniantong/new-api-neo` — provider normalization/gateway architecture; study before any code reuse.
- `Panniantong/CLIProxyAPI` — compatibility/proxy architecture; security, authentication and provider terms require review before reuse.
- `Panniantong/sub2api` — unified AI relay architecture; source is an LGPL-3.0 fork and should be treated as an architectural reference unless licensing obligations are explicitly satisfied.
- `Panniantong/xfetch` — X/Twitter retrieval capability; cookie/auth handling requires strict isolation.
- `Panniantong/skillshare` — skill distribution/management architecture; compare with existing `agent-skills` before adopting.
- `Panniantong/openclaw` — large agent orchestration source; architecture study only until a bounded component is identified.

## Execution result

The first Agent-Reach-derived research routing boundary was already merged into `salamou1944/Salamou-31`.

The next bounded capability was extracted from the `last30days-skill` research pattern and implemented as:

`AI-API-HUB/api-factory/research-evidence.mjs`

It provides:
- configurable freshness windows;
- canonical URL normalization and deduplication;
- `fresh` / `stale` / `undated` / `future` evidence classification;
- retrieval timestamps;
- source tracking;
- fail-closed minimum-fresh-evidence enforcement;
- isolated tests.

Merged PR: `salamou1944/Salamou-31#12`
Merge commit: `3be66f53000bdaa871eabaa0593ab3b7ad8b566e`

Local isolated execution of the new evidence contract test passed:
`research evidence ledger: PASS`

The implementation intentionally does **not** perform external network fetching and does not invent citations. It is a contract boundary for observed research results.

## Downstream account discovered

`Panniantong/last30days-skill` is a fork of `mvanhorn/last30days-skill`. Per the permanent account-first rule, `mvanhorn` is now a downstream source account and must be enumerated before further reuse from that repository is treated as complete.

## Status

ACCOUNT_ENUMERATED → CAPABILITY_EXTRACTED → IMPLEMENTED → TESTED → MERGED

Next account-first target: `mvanhorn`, followed by the next highest-value non-duplicate capability.
