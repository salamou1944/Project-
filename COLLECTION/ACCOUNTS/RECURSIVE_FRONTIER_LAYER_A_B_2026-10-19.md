# Recursive account frontier — Layer A and queued Layer B (2026-10-19)

This Markdown companion intentionally feeds the existing `COLLECTION/AUTO/deep_extract.py` owner scanner, which discovers owners from GitHub URLs in `COLLECTION/ACCOUNTS/*.md`.

**Execution update**
- The Collection deep-extraction workflow now triggers when account Markdown, the frontier snapshot, or the extraction/audit scripts change.
- The workflow runs the extractor, validates the ready queue, and writes a current-main JSON inventory report with SHA-256 hashes, byte sizes, JSON root shapes, top-level array lengths, and common record counts.
- The first run against this frontier is initiated by this commit. Its result, extraction counts, external-access failures, and audit report must be read from the resulting workflow run; this file does not pre-claim success.

**Evidence boundary**
- Layer A is committed in `RECURSIVE_ACCOUNT_FRONTIER_LAYER_A_2026-10-18.json` (commit `ff4af71f9e5fab97c059321835aaf3d696c8ed34`): 220 repository identity records across the first eight owners below.
- Layer B entries were observed in owner-scoped GitHub searches but their repository records were not committed in the previous write attempt. Counts below are discovery notes only; do not treat them as committed exhaustive inventories.
- Owner-scoped search results under 100 rows are not authoritative proof of all repositories. The five 100-result pages are explicitly incomplete and require pagination.
- This file preserves targets and allows the existing extraction workflow to discover owner URLs. It does not claim that extraction has already succeeded.

## Layer A — repository identity snapshot committed

- [Panniantong](https://github.com/Panniantong) — 38 rows observed.
- [pietrozullo](https://github.com/pietrozullo) — 55 rows observed.
- [browser-use](https://github.com/browser-use) — 57 rows observed.
- [safishamsi](https://github.com/safishamsi) — 12 rows observed.
- [metorial](https://github.com/metorial) — 37 rows observed.
- [opensandbox-group](https://github.com/opensandbox-group) — 3 rows observed.
- [public-clis](https://github.com/public-clis) — 4 rows observed.
- [yt-dlp](https://github.com/yt-dlp) — 14 rows observed.

## Layer B — discovered, repository rows not yet persisted

- [jackwener](https://github.com/jackwener) — 47 search results observed; inventory not committed.
- [stickerdaniel](https://github.com/stickerdaniel) — 75 search results observed; inventory not committed.
- [daytonaio](https://github.com/daytonaio) — 12 search results observed; inventory not committed.
- [e2b-dev](https://github.com/e2b-dev) — 85 search results observed; inventory not committed.
- [ChromeDevTools](https://github.com/ChromeDevTools) — 19 search results observed; inventory not committed.
- [agentclientprotocol](https://github.com/agentclientprotocol) — 15 search results observed; inventory not committed.
- [jina-ai](https://github.com/jina-ai) — 100 results on first page only; more pages may exist.
- [nicobailon](https://github.com/nicobailon) — 100 results on first page only; more pages may exist.
- [kurtmckee](https://github.com/kurtmckee) — 100 results on first page only; more pages may exist.
- [xpzouying](https://github.com/xpzouying) — 100 results on first page only; more pages may exist.
- [vercel-labs](https://github.com/vercel-labs) — 100 results on first page only; more pages may exist.

## Targeted repository references (not account-wide sweeps)

- [microsoft/playwright](https://github.com/microsoft/playwright) — targeted browser automation reference only.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) — targeted MCP reference only.

## Extraction rules

The existing workflow pins each extraction to the enumerated repository commit, redacts common credential patterns, and writes source packets under `COLLECTION/AUTO/DEEP-EXTRACTED`. A valid extraction packet is source preservation only, not runtime proof or production readiness. The JSON audit report excludes itself to avoid recursive self-hashing.
