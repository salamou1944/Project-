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

## Layer B — repository identity snapshot persisted (2026-10-20)

The previously uncommitted Layer B repository identities are now persisted in [RECURSIVE_ACCOUNT_FRONTIER_LAYER_B_2026-10-20.json](./RECURSIVE_ACCOUNT_FRONTIER_LAYER_B_2026-10-20.json). The snapshot contains **1,523 public repository identity records across 11 owners**. Queries were paginated until the returned page contained fewer than 100 records for each owner.

| Owner | Repository records | Pages | Search pagination |
|---|---:|---:|---|
| [jackwener](https://github.com/jackwener) | 47 | 1 | Complete by page size |
| [stickerdaniel](https://github.com/stickerdaniel) | 76 | 1 | Complete by page size |
| [daytonaio](https://github.com/daytonaio) | 12 | 1 | Complete by page size |
| [e2b-dev](https://github.com/e2b-dev) | 85 | 1 | Complete by page size |
| [ChromeDevTools](https://github.com/ChromeDevTools) | 19 | 1 | Complete by page size |
| [agentclientprotocol](https://github.com/agentclientprotocol) | 15 | 1 | Complete by page size |
| [jina-ai](https://github.com/jina-ai) | 267 | 3 | Complete by page size |
| [nicobailon](https://github.com/nicobailon) | 134 | 2 | Complete by page size |
| [kurtmckee](https://github.com/kurtmckee) | 227 | 3 | Complete by page size |
| [xpzouying](https://github.com/xpzouying) | 252 | 3 | Complete by page size |
| [vercel-labs](https://github.com/vercel-labs) | 389 | 4 | Complete by page size |

**Authority boundary:** these are GitHub repository-search results scoped by `user:<owner>`, not authoritative owner API enumerations. Pagination reached a short final page for each owner, but repository search/indexing semantics can still omit results. Treat these records as discovery inventory; the deep-extraction workflow must independently enumerate and inspect source files. This snapshot does not claim that extraction has completed.

## Targeted repository references (not account-wide sweeps)

- [microsoft/playwright](https://github.com/microsoft/playwright) — targeted browser automation reference only.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) — targeted MCP reference only.

## Extraction rules

The existing workflow pins each extraction to the enumerated repository commit, redacts common credential patterns, and writes source packets under `COLLECTION/AUTO/DEEP-EXTRACTED`. A valid extraction packet is source preservation only, not runtime proof or production readiness. The JSON audit report excludes itself to avoid recursive self-hashing.


## Master account-completion register frontier — owner URLs added to active scanner (2026-10-19)

The existing deep-extraction scanner reads GitHub owner URLs from `COLLECTION/ACCOUNTS/*.md`; it does not directly read the master register. This section materializes the current owner frontier from `COLLECTION/MASTER/ACCOUNT_COMPLETION_REGISTER_2026-10-06.md` into that scanner's input graph.

- Source register lists 40 accounts with owner-scoped enumeration and 116 newly exposed owner names.
- After case-insensitive deduplication, this section preserves **151 distinct owner targets** from that register. The earlier register's “at least 138” is a historical lower bound; this parsed list is the current extracted target set, not proof that the global frontier is closed.
- The 8 Layer A and 11 Layer B owners listed earlier remain preserved. The owner scanner now deduplicates GitHub logins case-insensitively to avoid duplicate API sweeps caused by mixed-case references.
- Each entry below is a discovery target, not a claim that all repositories have been enumerated or deeply inspected. Continue following downstream owners found during extraction.

- https://github.com/achref-soua
- https://github.com/activepieces
- https://github.com/actualbudget
- https://github.com/agent0ai
- https://github.com/airbytehq
- https://github.com/alexbevi
- https://github.com/amardeeplakshkar
- https://github.com/apache
- https://github.com/ArchiveBox
- https://github.com/ARPAHLS
- https://github.com/aw-junaid
- https://github.com/awesome-ai-tools
- https://github.com/awesome-selfhosted
- https://github.com/BerriAI
- https://github.com/bitwarden
- https://github.com/borgbackup
- https://github.com/browser-use
- https://github.com/browserable
- https://github.com/bytedance
- https://github.com/caprover
- https://github.com/caramaschiHG
- https://github.com/Cbrock84
- https://github.com/charlie947
- https://github.com/cloudflare
- https://github.com/comfyanonymous
- https://github.com/cporter202
- https://github.com/debpalash
- https://github.com/deuxfleurs-org
- https://github.com/diegosouzapw
- https://github.com/DietrichGebert
- https://github.com/discourse
- https://github.com/DIYgod
- https://github.com/dlt-hub
- https://github.com/docker-mailserver
- https://github.com/docling-project
- https://github.com/documenso
- https://github.com/docusealco
- https://github.com/dokku
- https://github.com/Dokploy
- https://github.com/doobidoo
- https://github.com/duckdb
- https://github.com/dyad-sh
- https://github.com/element-hq
- https://github.com/eternity4719
- https://github.com/faucetdb
- https://github.com/firefly-iii
- https://github.com/flawiddsouza
- https://github.com/formbricks
- https://github.com/frappe
- https://github.com/FreshRSS
- https://github.com/gepa-ai
- https://github.com/gitleaks
- https://github.com/gitroomhq
- https://github.com/GlitchTip
- https://github.com/h-guo18
- https://github.com/harry0703
- https://github.com/hecatehq
- https://github.com/HelixDB
- https://github.com/Hikhakk
- https://github.com/hoarder-app
- https://github.com/huggingface
- https://github.com/imranraufbm
- https://github.com/Infisical
- https://github.com/inovector
- https://github.com/kaushikb11
- https://github.com/KazKozDev
- https://github.com/KDE
- https://github.com/KKKKhazix
- https://github.com/kopia
- https://github.com/mail-in-a-box
- https://github.com/mailcow
- https://github.com/MariaDB
- https://github.com/matomo-org
- https://github.com/mattpocock
- https://github.com/maybe-finance
- https://github.com/meilisearch
- https://github.com/meltano
- https://github.com/Mem0ai
- https://github.com/microsoft
- https://github.com/milvus-io
- https://github.com/miqdadbadjuber
- https://github.com/mizorewww
- https://github.com/mnfst
- https://github.com/mountain-loop
- https://github.com/mudler
- https://github.com/mufeedvh
- https://github.com/n8n-io
- https://github.com/nanobrowser
- https://github.com/Niko1221
- https://github.com/nmap
- https://github.com/NVIDIA
- https://github.com/obra
- https://github.com/ocrmypdf
- https://github.com/off-grid-ai
- https://github.com/ohmyform
- https://github.com/ollama
- https://github.com/open-free-llm-api
- https://github.com/open-saas-directory
- https://github.com/openai
- https://github.com/openbao
- https://github.com/openclaw
- https://github.com/OpenCut-app
- https://github.com/openensemble
- https://github.com/opensearch-project
- https://github.com/Pablostanley
- https://github.com/Panniantong
- https://github.com/plausible
- https://github.com/postalserver
- https://github.com/postgres
- https://github.com/PostHog
- https://github.com/postmill-ai
- https://github.com/Preloop
- https://github.com/proffesor-for-testing
- https://github.com/pydantic
- https://github.com/Reality-Shifting-Tech
- https://github.com/relayroom
- https://github.com/restic
- https://github.com/rezmoss
- https://github.com/RocketChat
- https://github.com/rohitg00
- https://github.com/ruvnet
- https://github.com/seaweedfs
- https://github.com/senamakel
- https://github.com/sgl-project
- https://github.com/sherlock-project
- https://github.com/shihabshahrier
- https://github.com/shobhitagnihotri69
- https://github.com/SigNoz
- https://github.com/SolvoHQ
- https://github.com/Somi-Project
- https://github.com/sqlite
- https://github.com/stablyai
- https://github.com/stanfordnlp
- https://github.com/steel-dev
- https://github.com/superloglabs
- https://github.com/temporalio
- https://github.com/thekaveh
- https://github.com/trycua
- https://github.com/twentyhq
- https://github.com/typesense
- https://github.com/umami-software
- https://github.com/unslothai
- https://github.com/usebruno
- https://github.com/usewrit
- https://github.com/varun29ankuS
- https://github.com/Wassimyounes01
- https://github.com/weaviate
- https://github.com/windmill-labs
- https://github.com/xihongshichaojidan8
- https://github.com/zeenie-ai
- https://github.com/zulip
