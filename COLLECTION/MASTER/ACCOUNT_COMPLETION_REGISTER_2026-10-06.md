# COLLECTION — Account Completion Register
Updated: 2026-10-06

## Operating rule

Any repository, GitHub URL, project, source, or collection item supplied by the user is treated as an **account/organization entry point**. The repository itself is not the collection boundary.

Required path:
**item → owner/org → all public repositories → relevant files/code/docs/assets → downstream owners → preserve → dedupe/merge → extract Skills → shelf → reuse**

No valuable material is discarded merely because it is not immediately useful.

## Current audit result

The previous register claiming 16 accounts was incomplete and is superseded.

A repository/source graph sweep of `salamou1944/Project-` found **at least 136 distinct GitHub owners/organizations** in the first 100 matching source records. This is a **frontier count, not a final global account total**; additional source records can expose more owners.

Therefore:
- **Final account total: NOT CLOSED YET**
- **Minimum currently identified owner frontier: 136**
- The 136 includes accounts already captured plus newly discovered owners from COLLECTION source indexes.
- Repeated repositories/daily captures do not create duplicate accounts.
- A repository-level capture does not count as a completed account sweep.

## Accounts with owner-scoped repository enumeration already performed

| Account | Current repository search result | Status |
|---|---:|---|
| Panniantong | 38 | ENUMERATED |
| OpenCut-app | 4 | ENUMERATED |
| Pablostanley | 37 | ENUMERATED |
| debpalash | 35 | ENUMERATED / prior capture said 37; reconcile |
| h-guo18 | 20 | ENUMERATED |
| ARPAHLS | 19 | ENUMERATED |
| zeenie-ai | 6 | ENUMERATED |
| rohitg00 | 320 | ENUMERATED |
| Wassimyounes01 | 47 | ENUMERATED / reconcile prior profile count |
| charlie947 | 20 | ENUMERATED |
| dyad-sh | 8 | ACCOUNT CAPTURED |
| Hikhakk | 6 | OWNER ENUMERATED; primary capture exists |
| sherlock-project | 5 | ENUMERATED |
| cporter202 | 34 | ENUMERATED / prior capture said 24; reconcile |
| trycua | 45 | ENUMERATED |
| xihongshichaojidan8 | 5 | ENUMERATED |
| senamakel | 89 | ENUMERATED / prior profile discrepancy recorded |
| miqdadbadjuber | 10 | ENUMERATED / prior capture said 11; reconcile |
| Cbrock84 | 57 | ENUMERATED; capture-write history must not be mistaken for completion |
| shobhitagnihotri69 | 76 | ENUMERATED |
| proffesor-for-testing | 25 | ENUMERATED |
| mizorewww | 49 | ENUMERATED |
| stablyai | 23 | ENUMERATED |
| KKKKhazix | 4 | ENUMERATED |
| Niko1221 | 1 | ENUMERATED |
| eternity4719 | 10 | ENUMERATED |
| NVIDIA | 700+ confirmed through page 7; enumeration continues | OPEN / LARGE ACCOUNT |
| shihabshahrier | 120 | ENUMERATED |
| open-free-llm-api | 1 | ENUMERATED |
| amardeeplakshkar | 66 | ENUMERATED |
| aw-junaid | 33 repos + 76 public gists previously captured | ENUMERATED / gists included |
| mufeedvh | 43 current search result; prior capture said 42 | RECONCILE |
| mnfst | 25 | ENUMERATED |
| nmap | 7 | ENUMERATED |
| Mem0ai | 12 | ENUMERATED |
| diegosouzapw | 71 | ENUMERATED |

## Newly exposed owners from the source graph

The following owners were exposed by repository/source records and are now **account-level collection targets**, even when only one repository was originally supplied or cited:

ArchiveBox, BerriAI, DIYgod, DietrichGebert, Dokploy, FreshRSS, GlitchTip, HelixDB, Infisical, KDE, KazKozDev, MariaDB, PostHog, Preloop, Reality-Shifting-Tech, RocketChat, SigNoz, SolvoHQ, Somi-Project, achref-soua, activepieces, actualbudget, agent0ai, airbytehq, alexbevi, apache, awesome-ai-tools, awesome-selfhosted, bitwarden, borgbackup, browser-use, browserable, bytedance, caprover, caramaschiHG, cloudflare, comfyanonymous, deuxfleurs-org, discourse, dlt-hub, docker-mailserver, docling-project, documenso, docusealco, dokku, duckdb, element-hq, faucetdb, firefly-iii, flawiddsouza, formbricks, frappe, gepa-ai, gitleaks, gitroomhq, harry0703, hecatehq, hoarder-app, huggingface, imranraufbm, inovector, kaushikb11, kopia, mail-in-a-box, mailcow, matomo-org, mattpocock, maybe-finance, meilisearch, meltano, microsoft, milvus-io, mountain-loop, mudler, n8n-io, nanobrowser, obra, ocrmypdf, off-grid-ai, ohmyform, ollama, open-saas-directory, openai, openbao, openclaw, openensemble, opensearch-project, pablostanley, plausible, postalserver, postgres, postmill-ai, pydantic, relayroom, restic, rezmoss, ruvnet, seaweedfs, sgl-project, sqlite, stanfordnlp, steel-dev, superloglabs, temporalio, thekaveh, twentyhq, typesense, umami-software, unslothai, usebruno, usewrit, weaviate, windmill-labs, zulip.

## Important normalization rules

- `debpalash/VoiceStudio` → account `debpalash`
- `NVIDIA/OpenShell` → account `NVIDIA`
- `diegosouzapw/OmniRoute` → account `diegosouzapw`
- `MNFST/awesome-free-llm-apis` daily captures → one account `mnfst`
- `sherlock-project/sherlock` → account/org `sherlock-project`
- `cporter202/agentic-ai-apis` → account `cporter202`
- `Panniantong/*` → account `Panniantong`

## Completion semantics

**ENUMERATED** = all repositories returned by the current owner-scoped enumeration have been recorded/targeted.

**ACCOUNT CAPTURED** = account-level provenance exists.

**DEEP SWEEP COMPLETE** = repositories have actually been inspected for reusable value, relevant material preserved, downstream owners extracted, and the account has been closed for the current collection cycle.

Enumeration alone is never represented as deep completion.

## Next execution frontier

1. Reconcile all owner counts against existing captures.
2. Enumerate every newly exposed owner.
3. Inspect every repository in each account, preserving small valuable assets.
4. Extract downstream owners recursively.
5. Dedupe only at the canonical Skill layer.
6. Close an account only after its full public repository/source graph is exhausted for the current pass.
7. Keep the frontier open until no new owners are exposed.

This register is deliberately conservative: it will not claim the final total until the source graph itself has been exhausted.


## Completed account sweep: ArchiveBox

- Account: ArchiveBox
- Owner-scoped enumeration: 25 public repositories on 2026-10-06
- Account state: DEEP SWEEP COMPLETE for the enumerated 25-repository frontier
- Capture record: COLLECTION/ACCOUNTS/ARCHIVEBOX_2026-10-06.md
- New downstream collection targets exposed: Mozilla/Readability, mitmproxy, Webrecorder/WACZ ecosystem, Internet Archive, pywb, Cloudflare, Pydantic, browser-use, Browserbase, Kernel, Anchor Browser, Browserless, ZenRows, gildas-lormeau, yt-dlp, gallery-dl, Puppeteer, Playwright.
- These downstream owners remain OPEN targets and must be swept recursively before they can be considered complete.
- ArchiveBox itself is closed for the current collection cycle; it may be reopened only if new public repositories or materially new source graph nodes appear.
