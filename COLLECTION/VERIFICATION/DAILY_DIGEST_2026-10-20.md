# Daily Collection & Agent Skills Operating Digest — 2026-10-20

**Reporting cutoff:** 2026-10-20 00:52 Africa/Algiers. This report includes newly persisted or updated material observed since the previous 2026-10-19 digest. It distinguishes source preservation, CI validation, and production/runtime proof.

## Executive status

- **Account frontier:** 199 owners enumerated; 31,343 repository identities preserved in the deep inventory. The committed owner graph includes 151 distinct owner targets materialized from the account-completion register, plus the existing Layer A/Layer B frontier.
- **Deep extraction:** 200 high-priority repositories selected; 199 extracted successfully; one blocked; 7,220 source packets in the ready-for-dedupe queue. The other repository identities remain metadata-only/deferred/archived, not discarded.
- **Incremental Collection:** five bounded harvest runs completed successfully in the operating window. Latest run **39187362819** passed all steps and committed **726f7efa974b77c3d698135c4080ccbf2c53caff**.
- **Latest JSON audit:** 11,366 JSON/JSONC files, zero parse failures, 707,937,025 raw bytes in run 39187362819.
- **Canonical Skill:** `browser-runtime-verification` strengthened in `agent-skills@84b4732094d543410a9284ab687405b37fea8e4f`; no duplicate Skill created.
- **API Factory:** pinned CI-local SOAT/Ollama real completion passed again in run 39186226159. **Production readiness remains NOT PROVEN.**
- **Install/promotion boundary:** no approved install candidates; installed count 0; explicit declarations 0; runtime-readiness claims 0.
- **Important unresolved defect:** code inspection found that the deep extractor does not load its prior state from the packet files and does not apply the shared sensitive-path filter. A code update was blocked before any file update or commit; the defect remains open.

## 1. Accounts and repositories swept

### Connected first-party GitHub account

The connected account exposes 10 repositories. Latest observed commits:

| Repository | Latest observed commit | Update since prior digest |
|---|---|---|
| `Salamou-31` | [f1333c69d30c6d763e61c232e456c4f2890fc55a](https://github.com/salamou1944/Salamou-31/commit/f1333c69d30c6d763e61c232e456c4f2890fc55a) | Added/updated the repeat SOAT runtime verification evidence note |
| `agent-skills` | [84b4732094d543410a9284ab687405b37fea8e4f](https://github.com/salamou1944/agent-skills/commit/84b4732094d543410a9284ab687405b37fea8e4f) | Strengthened canonical browser verification Skill |
| `Easy-` | [735f2ab5c26d411d3f1886e4b75493405dc756ac](https://github.com/salamou1944/Easy-/commit/735f2ab5c26d411d3f1886e4b75493405dc756ac) | No newer commit observed; provider initialization remains gated |
| `AI_operating_memory` | [618a9ff156a531114f50de7ff170ee090afc339d](https://github.com/salamou1944/AI_operating_memory/commit/618a9ff156a531114f50de7ff170ee090afc339d) | No newer commit observed |
| `Astra-` | [67c11fe9b58929799b61eaf6717d8f756da7e27d](https://github.com/salamou1944/Astra-/commit/67c11fe9b58929799b61eaf6717d8f756da7e27d) | No newer commit observed |
| `Astra` | [11a42643279e7323097cec4b845bf6d0cc179144](https://github.com/salamou1944/Astra/commit/11a42643279e7323097cec4b845bf6d0cc179144) | No newer commit observed |
| `Files-` | [ebde21ee2230f80b0d6c632757b3854b8022679a](https://github.com/salamou1944/Files-/commit/ebde21ee2230f80b0d6c632757b3854b8022679a) | No newer commit observed |
| `Project-` | [aababb5da0b9ecd3808ed0b247887cd1bfac24ce](https://github.com/salamou1944/Project-/commit/aababb5da0b9ecd3808ed0b247887cd1bfac24ce) | Added sensitive-path exclusion and token-literal redaction to the normal Collection extractor |
| `Pastel-` | [827b7f3b985201394d4e15097b469a72608cb06a](https://github.com/salamou1944/Pastel-/commit/827b7f3b985201394d4e15097b469a72608cb06a) | No newer commit observed |
| `local-bridge.` | [2b7fb712601d27885e6da29436b246b9b8baf5db](https://github.com/salamou1944/local-bridge./commit/2b7fb712601d27885e6da29436b246b9b8baf5db) | No newer commit observed |

This is a latest-commit sweep, not a claim that every file in all ten repositories was exhaustively reviewed in this run.

### Recursive external frontier

The current persisted deep manifest at [MANIFEST.json](https://github.com/salamou1944/Project-/blob/main/COLLECTION/AUTO/DEEP-EXTRACTED/MANIFEST.json) records:

- 199 owners; owner-discovery errors: 0.
- 31,343 repository metadata rows.
- 200 selected for deep extraction; 199 successfully extracted; one blocked.
- 7,220 source packets.
- 22,344 deferred repositories; 8,800 archived repositories retained as metadata-only.
- Inventory SHA-256: `a266b7c1e7e5498c2907d710f042b90789de90066a0bc53878aa55c899093c07`.
- Deferred queue SHA-256: `7dd76e5a4fa2d2865d904bcc14dded15b75a9b24cb625f0289699f0a5a8e7d4b`.

The deep extractor's selection budget is 200 repositories per run, at most two per owner, 24 files per repository, 50 KB per file and 300 KB of source bytes per repository. This is bounded source extraction, not a claim that every file in 31,343 repositories has been read.

The previous ad-hoc Layer B search produced 1,522 search-result rows across 11 owners. Those rows were not committed as a standalone search-results JSON. The canonical current frontier is the 31,343-row REST-enumerated metadata inventory; search-page counts are discovery evidence, not authoritative owner inventories.

## 2. Valuable assets preserved

### Deep extraction batch

The deep-extraction commit [64bcccff18bd36e321e69e46146aec8955e05894](https://github.com/salamou1944/Project-/commit/64bcccff18bd36e321e69e46146aec8955e05894) changed 204 files: 199 repository packet files plus inventory, deferred queue, manifest, extraction-ready queue and audit output.

High-value preserved source packets include:

- `Panniantong__Agent-Reach.json`, `jackwener__opencli-mcp.json`, `ChromeDevTools__chrome-devtools-mcp.json`, `browser-use__browser-use.json`, `browser-use__browserable.json`.
- `e2b-dev__runtime.json`, `opensandbox-group__OpenSandbox.json`, `cloudflare__sandbox-sdk.json`, `agent-sandbox__agent-sandbox.json`.
- `diegosouzapw__OmniRoute.json`, `mnfst__awesome-free-llm-apis.json`, `amardeeplakshkar__awesome-free-llm-apis.json`, `open-free-llm-api__awesome-freellm-apis.json`.
- `n8n-io__n8n.json`, `n8n-io__n8n` source families, `n8n-io__n8n.json`, `n8n-io__automation-mining-skill.json`, `n8n-io__skills.json`.
- `pydantic__pydantic-ai.json`, `mattpocock__skills.json`, `PatternsDev__skills.json`, `trailofbits__skills.json`, `mongodb__agent-skills.json`, `SigNoz__agent-skills.json`.
- `openai__tunnel-client.json`, `openai_codex-security.json` in the separate incremental batch, `cisco-ai-defense__mcp-scanner.json`, `gitleaks__gitleaks.json`, `openbao__openbao.json`.
- `prime-radiant-inc__streamlinear.json`, `prime-radiant-inc_agentic-usage-meter.json`, `doobidoo__mcp-memory-service.json`, `mudler__LocalAI.json`, `mem0ai__mem0.json`, `varun29ankuS__shodh-memory.json`.
- `agentclientprotocol__python-sdk.json`, `agentclientprotocol_rust-sdk.json`, `agentclientprotocol_codex-acp.json`, `nicobailon__pi-mcp-adapter.json`, `nicobailon_pi-interactive-shell.json`.

The full exact packet-path inventory is included in Appendix B and the commit diff. Every extracted packet is source evidence only, marked for dedupe/adaptation and kept on the shelf.

### Five bounded incremental Collection batches

The following generated commits preserve the complete file-level diff for each run:

- Run [39186272221](https://github.com/salamou1944/Project-/actions/runs/39186272221) → [`0cf97579f587c06a0a51bcf2fad1ae5e09fadb66`](https://github.com/salamou1944/Project-/commit/0cf97579f587c06a0a51bcf2fad1ae5e09fadb66): 99 of 100 selected repositories refreshed; one blocked; total source rows 2,985; 490 earlier sources preserved but not selected; 20,048 deferred.
- Run [39186698910](https://github.com/salamou1944/Project-/actions/runs/39186698910) → [`4ec33a90e736ba961e470f7441e61cc45350415e`](https://github.com/salamou1944/Project-/commit/4ec33a90e736ba961e470f7441e61cc45350415e): 98 source packets added/updated from 100 selected; two blocked sources retained.
- Run [39186862522](https://github.com/salamou1944/Project-/actions/runs/39186862522) → [`60502ad15f35d970a267a8d0c3c23fc15bd18301`](https://github.com/salamou1944/Project-/commit/60502ad15f35d970a267a8d0c3c23fc15bd18301): 98 source packets added/updated; total source rows 3,181.
- Run [39187054275](https://github.com/salamou1944/Project-/actions/runs/39187054275) → [`749649b9b35b0104328cf2dafafd4db40e38fc00`](https://github.com/salamou1944/Project-/commit/749649b9b35b0104328cf2dafafd4db40e38fc00): 98 source packets added/updated; total source rows 3,279.
- Run [39187362819](https://github.com/salamou1944/Project-/actions/runs/39187362819) → [`726f7efa974b77c3d698135c4080ccbf2c53caff`](https://github.com/salamou1944/Project-/commit/726f7efa974b77c3d698135c4080ccbf2c53caff): 97 successful source packet files refreshed; three source rows blocked/preserved; total source rows 3,379; 3,376 extracted sources; 2,789 cached sources; 490 prior sources not selected; 31,343 repository identities; 19,657 deferred in this pipeline.

These are two separate pipelines with different manifest semantics. Do not add their counts as if every record were unique across both.

### Full source packet path ledger

The complete changed-file ledger for the five incremental runs is in Appendix A. It includes source packets and historical packet snapshots, not just headline/high-value projects.

## 3. Skills created or strengthened

No new Skill was created in this window. The canonical Skill was strengthened instead of creating a semantic duplicate:

- Commit [`84b4732094d543410a9284ab687405b37fea8e4f`](https://github.com/salamou1944/agent-skills/commit/84b4732094d543410a9284ab687405b37fea8e4f).
- File: [`skills/browser-runtime-verification/SKILL.md`](https://github.com/salamou1944/agent-skills/blob/main/skills/browser-runtime-verification/SKILL.md); current blob SHA `5878a77ab934e48a27f309850bc9ca346aef2358`.
- Added redirect/final-URL allowlist enforcement, explicit authorization for logged-in browser sessions, no secret-bearing session evidence, capture-off-by-default, protected harness boundaries and reproducible redirect-failure records.
- Validation boundary: no Skill-specific test run was found for this commit; a Railway watcher reporting “no deployment needed” is not a Skill test or runtime proof.

## 4. Dedupe and merge decisions

Latest Collection run 39187362819 recorded:

- 3,376 source records with files scanned.
- 54,491 evidence records.
- 29,422 capability groups.
- 20,208 promotion-review items.
- 9,214 restricted/quarantined items.
- 1,773 `review_merge_or_upgrade` items and 18,435 `review_new_or_upgrade` items.
- 162 prior evidence identities absent from the current generated view were checked against history; zero were unrecoverable.
- Policy gate passed with zero runtime-readiness claims and zero explicit readiness declarations.
- Installation outcome: `NO_APPROVED_CANDIDATES`; installed = 0.

No source was deleted to simplify the catalogue. Archived, blocked, deferred and unselected repositories remain represented by metadata/queues. Existing capabilities are candidates for merge/upgrade review, not automatic promotion.

## 5. Validation evidence

### Collection and JSON

- **Deep extraction run [39181614341](https://github.com/salamou1944/Project-/actions/runs/39181614341):** extraction and packet validation succeeded; 7,220 packets were produced. The run then failed the persisted JSON audit because one JSON/JSONC file did not parse. It committed the audit report before failing.
- **Audit-only run [39185928703](https://github.com/salamou1944/Project-/actions/runs/39185928703):** passed after JSONC compatibility handling; 10,877 files, zero parse failures, 595,154,410 raw bytes.
- **Owner URL parser regression [39181282587](https://github.com/salamou1944/Project-/actions/runs/39181282587):** passed. This validates parsing of owner URLs/Markdown punctuation and dedupe cases, not full frontier completeness.
- **Install-selection regression [39181165014](https://github.com/salamou1944/Project-/actions/runs/39181165014):** passed. It validates bounded/license-gated selection and persisted install-outcome contracts.
- **Latest full safe-incremental Collection run [39187362819](https://github.com/salamou1944/Project-/actions/runs/39187362819):** all steps passed, including compilation, extractor/state guards, policy/readiness/callable validation, install-selection, final persisted JSON audit and installation outcome. Current-main audit: 11,366 files, zero parse failures, 707,937,025 bytes.
- GitHub warned that `COLLECTION/MASTER/READY.json` was 65.28 MB, above the recommended 50 MB file size. The run succeeded, but storage/clone cost remains a maintenance concern.

### API Factory local runtime — not production

- Initial CI-local SOAT/Ollama run [39179590053](https://github.com/salamou1944/Salamou-31/actions/runs/39179590053) passed.
- Repeat run [39186226159](https://github.com/salamou1944/Salamou-31/actions/runs/39186226159) passed all deterministic API Factory tests, pinned SOAT health/auth, authenticated local Ollama bootstrap/probe, real completion, official SOAT smoke, evidence contract, persistence/consumption and business-outcome gate.
- Latest artifact [12158456947](https://github.com/salamou1944/Salamou-31/actions/runs/39186226159/artifacts/12158456947), SHA-256 `e05b92477f7f4a3e8caea1a18db3c5c8758c2283181474349802e5de78f64d6a`.
- The deterministic completion was `"4"`; this is a connectivity/contract smoke, not a model-quality benchmark.
- The evidence explicitly records `production_status: not_proven`. Railway deployment health, current Vercel production branch, durable cross-process registry/artifact persistence and production-provider configuration remain unverified.

### Source redaction changes — tests not yet verified

Commits:
- [`a50e88c6772f58a8f84aab842d4bdab7dd662cc5`](https://github.com/salamou1944/Project-/commit/a50e88c6772f58a8f84aab842d4bdab7dd662cc5) — shared content-safety helpers.
- [`ea82df3dd22f4246e5b68a8a670604778fd7e2c1`](https://github.com/salamou1944/Project-/commit/ea82df3dd22f4246e5b68a8a670604778fd7e2c1) — non-destructive derived-packet sanitizer.
- [`f4edbb47debc1a0bf65a84b97e1f765b8d62071c`](https://github.com/salamou1944/Project-/commit/f4edbb47debc1a0bf65a84b97e1f765b8d62071c) — tests for credential-path and token redaction.
- [`e7a2935f93ac9b1e47b4c8c75cfdb6e606fc79e7`](https://github.com/salamou1944/Project-/commit/e7a2935f93ac9b1e47b4c8c75cfdb6e606fc79e7) — CI test gating for source redaction and manifest policy.
- [`aababb5da0b9ecd3808ed0b247887cd1bfac24ce`](https://github.com/salamou1944/Project-/commit/aababb5da0b9ecd3808ed0b247887cd1bfac24ce) — normal Collection extractor excludes sensitive paths and redacts high-confidence token literals.

The tests cover `.env`, service-account JSON, AWS credentials, private-key/terraform-state paths, safe example files, token literals and recursive packet sanitization. **A passing CI run for this newly added safety suite was not verified in this report.**

## 6. Ready-to-use assets/projects

- **Ready for controlled dedupe/adaptation:** 7,220 deep extraction packets and the newly refreshed incremental source packets. They are source-only and remain on shelf.
- **Ready as a CI-local integration path:** API Factory through pinned SOAT + local Ollama. This is not a hosted service or production-ready provider path.
- **Ready as a canonical procedure:** the updated browser-runtime-verification Skill; its newly added rules still need a Skill-specific regression run.
- **Not installed:** no browser, sandbox, MCP, gateway or provider candidate from this collection was promoted/installed by these runs.
- **No customer/revenue proof was created by these Collection runs.** A source packet, API schema, README or passing local smoke is not a customer event.

## 7. Blocked or unverified items

### Critical deep-extractor defects found by code inspection

Current `COLLECTION/AUTO/deep_extract.py` blob SHA: `5f6583fff515b8a205720a8d79677280b0fbad33`.

1. The script attempts to recover previous state from `MANIFEST.json` using `prior.get("repos", [])`, but the current manifest schema does not contain a `repos` array. The script also does not reconstruct previous rows from existing per-repository packet files. **Likely consequence:** future bounded runs may treat all repositories as new and repeatedly select the same top-priority batch rather than progressing through the 31,343-repository inventory. This is a code-inspection finding; no second deep run has yet been used to confirm the repetition.
2. The deep extractor still uses its older local `redact()` function and does not import the shared `source_content_safety.py` helper or exclude sensitive source paths. The normal incremental extractor has the newer protection, but the deep extraction path does not yet have equivalent defense in depth. This is a potential exposure path, not evidence that a secret was actually disclosed.
3. The deep extraction failure for `awesome-ai-tools/awesome-ai-tools` was `github_api_http_404` because branch `main` was not found. The owner inventory was preserved; do not guess a replacement branch without fresh metadata.

A proposed code update to fix state recovery and apply the shared sensitive-path policy was blocked by the write safety layer before any file update or commit. An empty branch, [`fix/deep-extract-frontier-progress-and-redaction-2026-10-20`](https://github.com/salamou1944/Project-/tree/fix/deep-extract-frontier-progress-and-redaction-2026-10-20), was created from `aababb5da0b9ecd3808ed0b247887cd1bfac24ce`; it contains no committed fix or PR. No alternate write path was attempted.

### Other boundaries

- 22,344 deep-inventory repositories remain deferred; 8,800 archived repositories are metadata-only.
- The normal incremental pipeline has 19,657 deferred repositories in its own queue. This is a different queue from the deep-extraction queue.
- New source redaction tests were added, but their CI result was not confirmed.
- The browser Skill commit has no Skill-specific test evidence.
- API Factory remains `production_status: not_proven` despite successful CI-local completion.
- No new production runtime was installed or verified.

## 8. Downstream accounts opened

The active owner graph includes the original Layer A owners, the 11 Layer B owners and the materialized owner URLs from the account-completion register. The deep inventory now enumerates 199 owners and 31,343 repository identities.

Layer B owners carried forward from the previous search sweep:
`jackwener`, `stickerdaniel`, `daytonaio`, `e2b-dev`, `ChromeDevTools`, `agentclientprotocol`, `jina-ai`, `nicobailon`, `kurtmckee`, `xpzouying`, `vercel-labs`.

The ad-hoc search result counts are not used as the canonical inventory because one committed note recorded `stickerdaniel` at 75 while the later search summary recorded 76. The owner REST inventory is the authoritative record for this run.

## 9. Exact commits and evidence

- Layer A snapshot: [`ff4af71f9e5fab97c059321835aaf3d696c8ed34`](https://github.com/salamou1944/Project-/commit/ff4af71f9e5fab97c059321835aaf3d696c8ed34).
- Full 151-owner materialization: [`0d5c7a50ddfc503de0ac39ba12b42683ebe82f14`](https://github.com/salamou1944/Project-/commit/0d5c7a50ddfc503de0ac39ba12b42683ebe82f14).
- Bounded deep-extraction logic: [`76f9944042481a0a8d1e4cb332a46326e078f288`](https://github.com/salamou1944/Project-/commit/76f9944042481a0a8d1e4cb332a46326e078f288).
- Deep extraction + initial audit report: [`64bcccff18bd36e321e69e46146aec8955e05894`](https://github.com/salamou1944/Project-/commit/64bcccff18bd36e321e69e46146aec8955e05894).
- New-source-first selector: [`9c3d8e0263eaba904aaabc890dc01138e41d18ba`](https://github.com/salamou1944/Project-/commit/9c3d8e0263eaba904aaabc890dc01138e41d18ba); regression commit [`97bafc7f5b36685ac2be7531bceee808cc920f78`](https://github.com/salamou1944/Project-/commit/97bafc7f5b36685ac2be7531bceee808cc920f78).
- Full safe-incremental generated states: [`0cf97579f587c06a0a51bcf2fad1ae5e09fadb66`](https://github.com/salamou1944/Project-/commit/0cf97579f587c06a0a51bcf2fad1ae5e09fadb66), [`4ec33a90e736ba961e470f7441e61cc45350415e`](https://github.com/salamou1944/Project-/commit/4ec33a90e736ba961e470f7441e61cc45350415e), [`60502ad15f35d970a267a8d0c3c23fc15bd18301`](https://github.com/salamou1944/Project-/commit/60502ad15f35d970a267a8d0c3c23fc15bd18301), [`749649b9b35b0104328cf2dafafd4db40e38fc00`](https://github.com/salamou1944/Project-/commit/749649b9b35b0104328cf2dafafd4db40e38fc00), [`726f7efa974b77c3d698135c4080ccbf2c53caff`](https://github.com/salamou1944/Project-/commit/726f7efa974b77c3d698135c4080ccbf2c53caff).
- Canonical browser Skill: [`84b4732094d543410a9284ab687405b37fea8e4f`](https://github.com/salamou1944/agent-skills/commit/84b4732094d543410a9284ab687405b37fea8e4f).
- API Factory repeat evidence note: [`f1333c69d30c6d763e61c232e456c4f2890fc55a`](https://github.com/salamou1944/Salamou-31/commit/f1333c69d30c6d763e61c232e456c4f2890fc55a).
- Source safety commits: [`a50e88c6772f58a8f84aab842d4bdab7dd662cc5`](https://github.com/salamou1944/Project-/commit/a50e88c6772f58a8f84aab842d4bdab7dd662cc5), [`ea82df3dd22f4246e5b68a8a670604778fd7e2c1`](https://github.com/salamou1944/Project-/commit/ea82df3dd22f4246e5b68a8a670604778fd7e2c1), [`f4edbb47debc1a0bf65a84b97e1f765b8d62071c`](https://github.com/salamou1944/Project-/commit/f4edbb47debc1a0bf65a84b97e1f765b8d62071c), [`e7a2935f93ac9b1e47b4c8c75cfdb6e606fc79e7`](https://github.com/salamou1944/Project-/commit/e7a2935f93ac9b1e47b4c8c75cfdb6e606fc79e7), [`aababb5da0b9ecd3808ed0b247887cd1bfac24ce`](https://github.com/salamou1944/Project-/commit/aababb5da0b9ecd3808ed0b247887cd1bfac24ce).

## 10. Next execution order

1. Repair deep-extractor state recovery so it loads prior packet revisions from preserved packet files and advances through new/stale repository candidates.
2. Apply shared sensitive-path exclusion and token redaction to the deep extraction path; preserve raw path, blob SHA and content hash metadata without preserving secret contents.
3. Add focused tests for cache progression and sensitive-path handling, and require a passing PR CI run before merge.
4. Run the next bounded deep extraction and confirm that the selected repositories differ from the previous 200 while all 31,343 identities remain in the inventory/deferred queues.
5. Re-run the current-main JSON audit and verify manifest inventory/deferred hashes after the run.
6. Keep all new assets on shelf until dedupe, license/security and integration gates pass. Do not treat packet presence, CI-local completion or a ready queue as production readiness.

## Appendix A — all incremental Collection packet paths

### Run 39186272221 — first full safe-incremental harvest
Commit: [0cf97579f587c06a0a51bcf2fad1ae5e09fadb66](https://github.com/salamou1944/Project-/commit/0cf97579f587c06a0a51bcf2fad1ae5e09fadb66)
Changed files: 128; source/history packet files: 117.

**Packet paths under `COLLECTION/AUTO/EXTRACTED/`**

- `ARPAHLS_skillware.json`
- `ArchiveBox_abx-dl.json`
- `BerriAI_litellm.json`
- `ChromeDevTools_chrome-devtools-mcp.json`
- `Comfy-Org_ComfyUI.json`
- `DietrichGebert_ponytail.json`
- `Graphify-Labs_graphify.json`
- `HISTORY/ARPAHLS_skillware__54f3325ef60960a57ed8c437268084061dac26d8.json`
- `HISTORY/Hikhakk_higgsfield-mcp-unified__e00e05c6f2fd901206816b6cbf853f18ab5a567a.json`
- `HISTORY/NVIDIA_SkillSpector__240421219409dc0bafef9f618a10d80c2d7e83a3.json`
- `HISTORY/Niko1221_Strata__296b59d2f73c8f04a805df29c2fa97655adace78.json`
- `HISTORY/cbrock84_headcount__98d1c17d480f606060102a781f9a8601690685f7.json`
- `HISTORY/cporter202_agentic-ai-apis__58f8741188ffa9fe17d601f37d18ed6b33c3a2d8.json`
- `HISTORY/dyad-sh_dyad__93d96347a97a60a241575001147913d5eecc8d7c.json`
- `HISTORY/juspay_neurolink__7bf7d398cb39678d9a92e16a9b7f0dccf9177672.json`
- `HISTORY/open-free-llm-api_awesome-freellm-apis__9f78c9c4de978a0ca5fe4e0f93fd3cd0040036f8.json`
- `HISTORY/proffesor-for-testing_agentic-qe__445495e556cd8cac68326090e8f58d0287e0a36b.json`
- `HISTORY/reticlehq_reticle__64dda69d7d48721f90ae3635d914e7fd995abd23.json`
- `HISTORY/rohitg00_ai-engineering-from-scratch__1a8c4fd5f5b3012e50e111f694b4d84df8a4eb1e.json`
- `HISTORY/ruvnet_ruflo__1882006a02487590c8c66a7eec8d7504f6af33c3.json`
- `HISTORY/stablyai_orca__7a78dbd3c74eb67b6fb4f691fce69dbe6c408faf.json`
- `HISTORY/stuinfla_ruvnet-brain__b44f51ccefe15432d0ba4c5bfffe39aa10bbf6d0.json`
- `HISTORY/the-open-agent_openagent__9140e8b063b7d06d02c4e010d7d01f7be6aa0197.json`
- `HISTORY/trycua_cua__384077f579b2229c428b16ddd2f0c2eb3ea33906.json`
- `HISTORY/yihui-dev_awesome-gemini4-argon-videos__2d8103dae39bcbebdbbc0fdbc1803873087846c7.json`
- `HelixDB_helix-db.json`
- `Hikhakk_higgsfield-mcp-unified.json`
- `KazKozDev_WebOperator.json`
- `MariaDB_server.json`
- `NVIDIA_SkillSpector.json`
- `Niko1221_Strata.json`
- `PostHog_posthog.json`
- `SigNoz_agent-skills.json`
- `Somi-Project_Somi.json`
- `achref-soua_quiver.json`
- `activepieces_activepieces.json`
- `agentclientprotocol_python-sdk.json`
- `ai-forever_gpt2giga.json`
- `airbytehq_airbyte-agent-sdk.json`
- `alexbevi_EDDI.json`
- `alibaba_qz-browser-agent.json`
- `apache_casbin-gateway.json`
- `browser-use_browser-use.json`
- `bytedance_deer-flow.json`
- `cbrock84_headcount.json`
- `cisco-ai-defense_mcp-scanner.json`
- `cloudflare_sandbox-sdk.json`
- `cporter202_agentic-ai-apis.json`
- `debpalash_OpenGTM.json`
- `diegosouzapw_OmniRoute.json`
- `docling-project_docling-mcp.json`
- `doobidoo_mcp-memory-service.json`
- `dyad-sh_dyad.json`
- `e2b-dev_runtime.json`
- `faucetdb_faucet.json`
- `gitleaks_gitleaks.json`
- `gitroomhq_postiz-agent.json`
- `google_mantis.json`
- `harry0703_MoneyPrinterTurbo.json`
- `hecatehq_hecate.json`
- `huggingface_pytorch-image-models.json`
- `jackwener_opencli-mcp.json`
- `jina-ai_cli.json`
- `juspay_neurolink.json`
- `matomo-org_device-detector.json`
- `mcp-use_mcp-use.json`
- `meilisearch_meilisearch-mcp.json`
- `mem0ai_mem0.json`
- `metorial_metorial.json`
- `microsoft_Dataverse-skills.json`
- `milvus-io_bootcamp.json`
- `mnfst_awesome-free-llm-apis.json`
- `mongodb_agent-skills.json`
- `mudler_LocalAI.json`
- `n8n-io_n8n.json`
- `nanobrowser_nanobrowser.json`
- `nicobailon_pi-mcp-adapter.json`
- `obra_superpowers.json`
- `off-grid-ai_OGAD.json`
- `ollama_ollama.json`
- `open-free-llm-api_awesome-freellm-apis.json`
- `openai_tunnel-client.json`
- `openclaw_clawscan.json`
- `openensemble_openensemble.json`
- `opensandbox-group_OpenSandbox.json`
- `postmill-ai_postmill-app.json`
- `preloop_preloop.json`
- `proffesor-for-testing_agentic-qe.json`
- `pydantic_pydantic-ai.json`
- `repoprompt_repoprompt-ce.json`
- `reticlehq_reticle.json`
- `rohitg00_ai-engineering-from-scratch.json`
- `ruvnet_ruflo.json`
- `safishamsi_FirstSight.json`
- `sazonovanton_SirChatalot.json`
- `sgl-project_sglang.json`
- `stablyai_orca.json`
- `steel-dev_steel-browser.json`
- `stickerdaniel_browserjack.json`
- `stripe_ai.json`
- `stuinfla_ruvnet-brain.json`
- `superloglabs_superlog.json`
- `temporalio_sdk-go.json`
- `the-open-agent_openagent.json`
- `thekaveh_rag-showcase.json`
- `trailofbits_skills.json`
- `trycua_cua.json`
- `uber_ADR.json`
- `unslothai_unsloth.json`
- `usebruno_bruno.json`
- `usewrit_writ-plugins.json`
- `varun29ankuS_shodh-memory.json`
- `vercel-labs_agent-browser.json`
- `vercel_ai.json`
- `weaviate_docs.json`
- `yihui-dev_awesome-gemini4-argon-videos.json`
- `zulip_zulipmcp.json`

**Manifest/deferred files**
- `COLLECTION/AUTO/EXTRACTED/DEFERRED-REPOSITORY-QUEUE.json`
- `COLLECTION/AUTO/EXTRACTED/MANIFEST.json`

**Other generated state files**
- `COLLECTION/MASTER/CANONICAL-PROMOTION-PLAN.json`
- `COLLECTION/MASTER/INSTALLATION-REPORT.json`
- `COLLECTION/MASTER/PROMOTION-QUEUE.json`
- `COLLECTION/MASTER/READINESS-QUEUE.json`
- `COLLECTION/MASTER/READY.json`
- `COLLECTION/MASTER/VALUE-OPERATOR-QUEUE.json`
- `COLLECTION/VERIFICATION/CURRENT_MAIN_JSON_AUDIT.json`
- `COLLECTION/VERIFICATION/INSTALLED-QUEUE.json`
- `COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json`

### Run 39186698910 — first new-source-first batch
Commit: [4ec33a90e736ba961e470f7441e61cc45350415e](https://github.com/salamou1944/Project-/commit/4ec33a90e736ba961e470f7441e61cc45350415e)
Changed files: 107; source/history packet files: 98.

**Packet paths under `COLLECTION/AUTO/EXTRACTED/`**

- `ArchiveBox_browser-session-autohealer.json`
- `BerriAI_litellm-skills.json`
- `Dokploy_dokploy.json`
- `HelixDB_graphify-v8.json`
- `Infisical_infisical.json`
- `KDE_kdenlive.json`
- `KazKozDev_NovelGenerator.json`
- `PostHog_context-mill.json`
- `Reality-Shifting-Tech_OpenMeerkat.json`
- `SigNoz_signoz.json`
- `VersinoPsiOmega_semvec-mongodb-atlas.json`
- `addyosmani_agent-skills.json`
- `agent0ai_spynel.json`
- `agentclientprotocol_claude-agent-acp.json`
- `ai-forever_gigachain.json`
- `airbytehq_airbyte.json`
- `alexbevi_awesome-agent-frameworks.json`
- `alibaba_zvec.json`
- `anomalyco_browser-control.json`
- `apache_syncope.json`
- `better-world-ai_x-cli.json`
- `bitwarden_server.json`
- `block_codecrucible.json`
- `browser-use_browser-harness.json`
- `browserable_browserable.json`
- `bytedance_UI-TARS-desktop.json`
- `caramaschiHG_awesome-ai-agents-2026.json`
- `cisco-ai-defense_skill-scanner.json`
- `cline_cline.json`
- `cloudflare_cf.json`
- `deuxfleurs-org_garage.json`
- `diegosouzapw_awesome-omni-skills.json`
- `docling-project_docling-java.json`
- `docusealco_docuseal-agent-skills.json`
- `doobidoo_MCP-Context-Provider.json`
- `duckdb_duckdb-wasm.json`
- `e2b-dev_open-computer-use.json`
- `element-hq_element-x-ios.json`
- `faucetdb_homebrew-tap.json`
- `flawiddsouza_Restfox.json`
- `frappe_frappe.json`
- `ggml-org_llama.cpp.json`
- `gitleaks_gitleaks-action.json`
- `gitroomhq_agent-media.json`
- `google_adk-go.json`
- `huggingface_funes.json`
- `imranraufbm_youtube-automation-agent.json`
- `jackwener_OpenCLI.json`
- `jina-ai_meta-prompt.json`
- `kaushikb11_awesome-llm-agents.json`
- `kopia_kopia.json`
- `mail-in-a-box_mailinabox.json`
- `matomo-org_matomo-java-tracker.json`
- `maxkru92_OpenViking.json`
- `meilisearch_meilisearch.json`
- `meltano_meltano.json`
- `mem0ai_dolphinbench.json`
- `metorial_metorial-platform.json`
- `microsoft_mcp-for-beginners.json`
- `milvus-io_milvus.json`
- `mountain-loop_yaak.json`
- `mudler_cogito.json`
- `n8n-io_automation-mining-skill.json`
- `nicobailon_surf-cli.json`
- `off-grid-ai_OGAM.json`
- `open-free-llm-api_free-llm-models.json`
- `openai_openai-agents-python.json`
- `openclaw_Peekaboo.json`
- `opensearch-project_opensearch-agent-skills.json`
- `pietrozullo_mcp-hubspot.json`
- `plausible_analytics.json`
- `prime-radiant-inc_streamlinear.json`
- `pydantic_logfire.json`
- `pytorch_rl.json`
- `restic_rest-server.json`
- `rezmoss_cloud-provider-ip-addresses.json`
- `ruvnet_agentic-flow.json`
- `seaweedfs_seaweedfs.json`
- `senamakel_openintents.json`
- `sgl-project_sglang-omni.json`
- `stanfordnlp_dspy.json`
- `steel-dev_awesome-web-agents.json`
- `stickerdaniel_linkedin-mcp-server.json`
- `stripe_link-cli.json`
- `temporalio_sdk-java.json`
- `thekaveh_atlas.json`
- `trailofbits_calcifier.json`
- `twentyhq_favicon.json`
- `typesense_typesense.json`
- `uber_causalml.json`
- `unslothai_notebooks.json`
- `usewrit_writ.json`
- `varun29ankuS_shodhRAG.json`
- `vercel-labs_agent-skills.json`
- `vercel_workflow.json`
- `weaviate_weaviate.json`
- `xpzouying_xiaohongshu-mcp.json`
- `yt-dlp_yt-dlp.json`

**Manifest/deferred files**
- `COLLECTION/AUTO/EXTRACTED/DEFERRED-REPOSITORY-QUEUE.json`
- `COLLECTION/AUTO/EXTRACTED/MANIFEST.json`

**Other generated state files**
- `COLLECTION/MASTER/CANONICAL-PROMOTION-PLAN.json`
- `COLLECTION/MASTER/PROMOTION-QUEUE.json`
- `COLLECTION/MASTER/READINESS-QUEUE.json`
- `COLLECTION/MASTER/READY.json`
- `COLLECTION/MASTER/VALUE-OPERATOR-QUEUE.json`
- `COLLECTION/VERIFICATION/CURRENT_MAIN_JSON_AUDIT.json`
- `COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json`

### Run 39186862522 — second new-source batch
Commit: [60502ad15f35d970a267a8d0c3c23fc15bd18301](https://github.com/salamou1944/Project-/commit/60502ad15f35d970a267a8d0c3c23fc15bd18301)
Changed files: 107; source/history packet files: 98.

**Packet paths under `COLLECTION/AUTO/EXTRACTED/`**

- `Aider-AI_aider.json`
- `ArchiveBox_good-karma-kit.json`
- `BerriAI_liteagents.json`
- `Dokploy_mcp.json`
- `Infisical_ai-skills.json`
- `KDE_falkon.json`
- `KazKozDev_llmflow-search.json`
- `MariaDB_mcp.json`
- `PostHog_pi-posthog-llm-gateway.json`
- `RocketChat_Rocket.Chat.json`
- `SigNoz_signoz-mcp-server.json`
- `VKCOM_vk-bridge.json`
- `ace-step_ACE-Step-1.5.json`
- `actualbudget_browser-app-demo.json`
- `addyosmani_web-quality-skills.json`
- `agent0ai_agent-zero.json`
- `agentclientprotocol_typescript-sdk.json`
- `ai-forever_giga_agent.json`
- `airbytehq_terraform-provider-airbyte.json`
- `alexbevi_ruby_llm.json`
- `alibaba_webmcp-nexus.json`
- `alphavantage_alpha_vantage_mcp.json`
- `anomalyco_models.dev.json`
- `apache_doris-skills.json`
- `awesome-selfhosted_awesome-selfhosted.json`
- `bitwarden_agent-access.json`
- `block_model-ledger.json`
- `borgbackup_borgstore.json`
- `browser-use_macos-harness.json`
- `bytedance_SALMONN.json`
- `caprover_caprover.json`
- `cisco-ai-defense_defenseclaw.json`
- `cline_kanban.json`
- `cloudflare_mcp.json`
- `cporter202_open-creator.json`
- `diegosouzapw_OmniCopilot.json`
- `discourse_discourse-mcp.json`
- `docling-project_docling-serve.json`
- `docusealco_docuseal-cli.json`
- `doobidoo_n8n-claude-memory-agent.json`
- `duckdb_duckdb.json`
- `e2b-dev_surf.json`
- `element-hq_ess-helm.json`
- `faucetdb_mcp-db-benchmark.json`
- `frappe_frappectl.json`
- `gepa-ai_gepa.json`
- `ggml-org_whisper.cpp.json`
- `gitroomhq_postiz-app.json`
- `google_agents-cli.json`
- `harry0703_AudioNotes.json`
- `huggingface_pwc-cli.json`
- `imranraufbm_openclaude.json`
- `jackwener_boss-cli.json`
- `jina-ai_MCP.json`
- `localai-org_vllm.cpp.json`
- `matomo-org_matomo.json`
- `meilisearch_meilisearch-go.json`
- `mem0ai_memory-benchmarks.json`
- `mem7ai_mem7.json`
- `metorial_metorial-python.json`
- `microsoft_mcp-gateway.json`
- `milvus-io_milvus-model.json`
- `mudler_LocalAGI.json`
- `n8n-io_n8n-docs.json`
- `nicobailon_visual-explainer.json`
- `obra_superpowers-chrome.json`
- `off-grid-ai_OGAC.json`
- `ollama_ollama-python.json`
- `open-free-llm-api_free-llm-models-python.json`
- `openai_openai-agents-js.json`
- `openbao_openbao.json`
- `openclaw_mcporter.json`
- `opensandbox-group_fast-sandbox.json`
- `opensearch-project_skills-eval.json`
- `prime-radiant-inc_scribble.json`
- `pydantic_genai-prices.json`
- `pytorch_benchmark.json`
- `relayroom_relayroom.json`
- `rezmoss_axios4go.json`
- `ruvnet_ruos.json`
- `senamakel_agent-browser.json`
- `sgl-project_genai-bench.json`
- `steel-dev_cli.json`
- `stickerdaniel_line-mcp-server.json`
- `stripe_openapi.json`
- `superloglabs_skills.json`
- `temporalio_temporal.json`
- `thekaveh_LinguAI.json`
- `trailofbits_algo.json`
- `uber_athenadriver.json`
- `unslothai_llama.cpp.json`
- `usewrit_writ-mcp.json`
- `varun29ankuS_Roshera-CAD.json`
- `vercel-labs_skills.json`
- `vercel_eve.json`
- `weaviate_recipes.json`
- `windmill-labs_windmill-cli-docs.json`
- `zulip_zulipbot.json`

**Manifest/deferred files**
- `COLLECTION/AUTO/EXTRACTED/DEFERRED-REPOSITORY-QUEUE.json`
- `COLLECTION/AUTO/EXTRACTED/MANIFEST.json`

**Other generated state files**
- `COLLECTION/MASTER/CANONICAL-PROMOTION-PLAN.json`
- `COLLECTION/MASTER/PROMOTION-QUEUE.json`
- `COLLECTION/MASTER/READINESS-QUEUE.json`
- `COLLECTION/MASTER/READY.json`
- `COLLECTION/MASTER/VALUE-OPERATOR-QUEUE.json`
- `COLLECTION/VERIFICATION/CURRENT_MAIN_JSON_AUDIT.json`
- `COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json`

### Run 39187054275 — third new-source batch
Commit: [749649b9b35b0104328cf2dafafd4db40e38fc00](https://github.com/salamou1944/Project-/commit/749649b9b35b0104328cf2dafafd4db40e38fc00)
Changed files: 107; source/history packet files: 98.

**Packet paths under `COLLECTION/AUTO/EXTRACTED/`**

- `ArchiveBox_ArchiveBox.json`
- `BerriAI_litespeed.json`
- `ChromeDevTools_vite-plugin-devtools-json.json`
- `DIYgod_RSSHub-Radar.json`
- `Dokploy_cli.json`
- `FreshRSS_FreshRSS.json`
- `GlitchTip_anysearch-mcp-server.json`
- `Infisical_agent-vault.json`
- `KDE_krita.json`
- `KazKozDev_cbt-assistant.json`
- `MariaDB_skills.json`
- `PatternsDev_skills.json`
- `PostHog_posthog-dotnet.json`
- `RocketChat_Rocket.Chat-Open-API.json`
- `SolvoHQ_dependency-migration-mcp.json`
- `VKCOM_vk-ios-sdk.json`
- `addyosmani_clarity.json`
- `agent0ai_a0-plugins.json`
- `agentclientprotocol_codex-acp.json`
- `ai-forever_gigachat.json`
- `airbytehq_fastmcp-extensions.json`
- `alexbevi_MemOS.json`
- `alibaba_nacos.json`
- `anomalyco_opencode.json`
- `apache_casbin-mcp-gateway.json`
- `bitwarden_passwordless-server.json`
- `block_me.md.json`
- `borgbackup_borg.json`
- `browser-use_benchmark.json`
- `bytedance_vArmor.json`
- `caprover_one-click-apps.json`
- `cisco-ai-defense_litellm.json`
- `cline_clinerules.json`
- `cloudflare_security-audit-skill.json`
- `deuxfleurs-org_aerogramme.json`
- `diegosouzapw_OmniGlyph.json`
- `discourse_discourse-steam-login.json`
- `docker-mailserver_docker-mailserver.json`
- `docling-project_docling-agent.json`
- `documenso_documenso.json`
- `docusealco_rllama.json`
- `dokku_sshcommand.json`
- `doobidoo_mcplex.json`
- `duckdb_duckdb-rs.json`
- `e2b-dev_awesome-ai-sdks.json`
- `element-hq_matrix-authentication-service.json`
- `frappe_skills.json`
- `ggml-org_llama.vim.json`
- `google_adk-java.json`
- `huggingface_transformers.json`
- `imranraufbm_strands-decider.json`
- `jackwener_llm-wiki.json`
- `jina-ai_clip-as-service.json`
- `localai-org_ced.cpp.json`
- `mailcow_mailcow-dockerized.json`
- `mailru_FileAPI.json`
- `matomo-org_matomo-php-tracker.json`
- `meilisearch_meilisearch-dotnet.json`
- `metorial_metorial-node.json`
- `microsoft_skills.json`
- `milvus-io_pymilvus.json`
- `mudler_nib.json`
- `n8n-io_self-hosted-ai-starter-kit.json`
- `nicobailon_mcp-gemini-server.json`
- `obra_private-journal-mcp.json`
- `ocrmypdf_OCRmyPDF.json`
- `ollama_ollama-js.json`
- `open-saas-directory_awesome-native-macosx-apps.json`
- `openai_openai-cua-sample-app.json`
- `openbao_openbao-plugins.json`
- `openclaw_lobster.json`
- `opensearch-project_observability-stack.json`
- `pietrozullo_browser-use.json`
- `postalserver_postal.json`
- `pydantic_monty.json`
- `pytorch_vision.json`
- `rezmoss_js-cloudip.json`
- `ruvnet_agenticow.json`
- `sgl-project_rbg.json`
- `stanfordnlp_axbench.json`
- `steel-dev_steel-python.json`
- `stickerdaniel_CLIProxyAPI.json`
- `stripe_stripe-node.json`
- `superloglabs_responder-oss.json`
- `temporalio_sdk-rust.json`
- `thekaveh_NNx.json`
- `trailofbits_slither-mcp.json`
- `typesense_typesense-js.json`
- `uber_motif.json`
- `unslothai_stable-diffusion.cpp.json`
- `usewrit_writ-agent.json`
- `varun29ankuS_mif-spec.json`
- `vercel-labs_coding-agent-template.json`
- `vercel_vercel-plugin.json`
- `weaviate_typescript-client.json`
- `windmill-labs_windmill.json`
- `xpzouying_homebrew-agent-cli.json`
- `zulip_zulip.json`

**Manifest/deferred files**
- `COLLECTION/AUTO/EXTRACTED/DEFERRED-REPOSITORY-QUEUE.json`
- `COLLECTION/AUTO/EXTRACTED/MANIFEST.json`

**Other generated state files**
- `COLLECTION/MASTER/CANONICAL-PROMOTION-PLAN.json`
- `COLLECTION/MASTER/PROMOTION-QUEUE.json`
- `COLLECTION/MASTER/READINESS-QUEUE.json`
- `COLLECTION/MASTER/READY.json`
- `COLLECTION/MASTER/VALUE-OPERATOR-QUEUE.json`
- `COLLECTION/VERIFICATION/CURRENT_MAIN_JSON_AUDIT.json`
- `COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json`

### Run 39187362819 — fourth bounded incremental batch
Commit: [726f7efa974b77c3d698135c4080ccbf2c53caff](https://github.com/salamou1944/Project-/commit/726f7efa974b77c3d698135c4080ccbf2c53caff)
Changed files: 106; source/history packet files: 97.

**Packet paths under `COLLECTION/AUTO/EXTRACTED/`**

- `ArchiveBox_abx-plugins.json`
- `BerriAI_liteadmin-mcp.json`
- `ChromeDevTools_awesome-chrome-devtools.json`
- `DIYgod_RSSHub.json`
- `FreshRSS_Extensions.json`
- `HelixDB_helix-foundry.json`
- `Infisical_infisical-mcp-server.json`
- `KDE_plasma-browser-integration.json`
- `KazKozDev_footnote-mcp.json`
- `MariaDB_TAF.json`
- `PostHog_llm-analytics-apps.json`
- `RocketChat_EmbeddedChat.json`
- `Shubhamsaboo_google-memorybank-plugin.json`
- `SigNoz_dashboards.json`
- `VKCOM_devicehub.json`
- `actualbudget_actual.json`
- `addyosmani_chatty.json`
- `agent0ai_code-execution-mcp.json`
- `agentclientprotocol_rust-sdk.json`
- `ai-forever_SMITH.json`
- `airbytehq_PyAirbyte.json`
- `alexbevi_bytechef.json`
- `alibaba_page-agent.json`
- `anomalyco_sst.json`
- `apache_magpie.json`
- `awesome-selfhosted_awesome-selfhosted-data.json`
- `bitwarden_clients.json`
- `block_ai-rules.json`
- `browser-use_browser-use-pi.json`
- `bytedance_PatchEval.json`
- `cisco-ai-defense_model-provenance-kit.json`
- `cline_skills.json`
- `cloudflare_agents.json`
- `diegosouzapw_code.json`
- `discourse_discourse.json`
- `dlt-hub_dlt.json`
- `docling-project_docling-ibm-models.json`
- `docusealco_docuseal-php.json`
- `dokku_lambda-builder.json`
- `doobidoo_shodh-cloudflare.json`
- `duckdb_duckdb-sqlite.json`
- `e2b-dev_fragments.json`
- `element-hq_element-web.json`
- `firefly-iii_firefly-iii.json`
- `formbricks_formbricks.json`
- `frappe_mcp.json`
- `ggml-org_Llama-macOS.json`
- `google_lightflow.json`
- `harry0703_MangoDisk.json`
- `huggingface_text-embeddings-inference.json`
- `imranraufbm_everything-claude-code.json`
- `jackwener_xhs-cli.json`
- `jina-ai_agentchain.json`
- `kurtmckee_feedparser.json`
- `kvesteri_sqlalchemy-utils.json`
- `localai-org_apex-quant.json`
- `matomo-org_tag-manager.json`
- `meilisearch_meilisearch-ruby.json`
- `metorial_metorial-index.json`
- `microsoft_thinkingbox.json`
- `milvus-io_milvus-sdk-java.json`
- `mudler_LocalRecall.json`
- `n8n-io_skills.json`
- `nicobailon_pi-interactive-shell.json`
- `obra_lace.json`
- `ollama_ollama-vscode.json`
- `openai_codex-security.json`
- `openclaw_crabbox.json`
- `opensearch-project_opensearch-mcp-server-py.json`
- `pietrozullo_mcp-server-neon.json`
- `postgres_postgres.json`
- `prime-radiant-inc_agentic-usage-meter.json`
- `pydantic_skills.json`
- `pytorch_ao.json`
- `restic_restic.json`
- `rezmoss_awesome-security-pipeline.json`
- `ruvnet_rupixel.json`
- `scummvm_scummvm.json`
- `sgl-project_SpecForge.json`
- `sqlite_sqlite.json`
- `stanfordnlp_CoreNLP.json`
- `steel-dev_leaderboard.json`
- `stickerdaniel_post-no-bills.json`
- `stripe_stripe-php.json`
- `temporalio_sdk-php.json`
- `trailofbits_coop.json`
- `twentyhq_twenty.json`
- `typesense_typesense-python.json`
- `uber_kraken.json`
- `umami-software_umami.json`
- `unslothai_audio.cpp.json`
- `usewrit_writ-for-websites.json`
- `varun29ankuS_shodh-redb.json`
- `vercel-labs_github-tools.json`
- `vercel_storage.json`
- `weaviate_agent-skills.json`
- `zulip_zulip-desktop.json`

**Manifest/deferred files**
- `COLLECTION/AUTO/EXTRACTED/DEFERRED-REPOSITORY-QUEUE.json`
- `COLLECTION/AUTO/EXTRACTED/MANIFEST.json`

**Other generated state files**
- `COLLECTION/MASTER/CANONICAL-PROMOTION-PLAN.json`
- `COLLECTION/MASTER/PROMOTION-QUEUE.json`
- `COLLECTION/MASTER/READINESS-QUEUE.json`
- `COLLECTION/MASTER/READY.json`
- `COLLECTION/MASTER/VALUE-OPERATOR-QUEUE.json`
- `COLLECTION/VERIFICATION/CURRENT_MAIN_JSON_AUDIT.json`
- `COLLECTION/VERIFICATION/RESTRICTED-QUEUE.json`


## Appendix B — all deep extraction packet paths

### Deep extraction commit — 64bcccff18bd36e321e69e46146aec8955e05894
Commit: [64bcccff18bd36e321e69e46146aec8955e05894](https://github.com/salamou1944/Project-/commit/64bcccff18bd36e321e69e46146aec8955e05894)
Changed files: 204; source packet files: 199.

**Packet paths under `COLLECTION/AUTO/DEEP-EXTRACTED/`**

- `ARPAHLS__OPSIE.json`
- `Aider-AI__aider.json`
- `ArchiveBox__abx-dl.json`
- `BerriAI__litellm.json`
- `ChromeDevTools__chrome-devtools-mcp.json`
- `Comfy-Org__ComfyUI.json`
- `DietrichGebert__ponytail.json`
- `Dokploy__dokploy.json`
- `FreshRSS__FreshRSS.json`
- `GlitchTip__anysearch-mcp-server.json`
- `Graphify-Labs__graphify.json`
- `HelixDB__helix-db.json`
- `Hikhakk__higgsfield-mcp-unified.json`
- `Infisical__infisical.json`
- `JCodesMore__ai-website-cloner-template.json`
- `KDE__kdenlive.json`
- `KKKKhazix__khazix-skills.json`
- `KazKozDev__WebOperator.json`
- `MariaDB__server.json`
- `NVIDIA__SkillSpector.json`
- `Niko1221__Strata.json`
- `OpenCut-app__OpenCut.json`
- `Panniantong__Agent-Reach.json`
- `PatternsDev__skills.json`
- `PostHog__posthog.json`
- `Reality-Shifting-Tech__OpenMeerkat.json`
- `RocketChat__Rocket.Chat.json`
- `Shubhamsaboo__google-memorybank-plugin.json`
- `SigNoz__agent-skills.json`
- `SolvoHQ__dependency-migration-mcp.json`
- `Somi-Project__Somi.json`
- `VKCOM__vk-bridge.json`
- `VersinoPsiOmega__semvec-mongodb-atlas.json`
- `Wassimyounes01__genesis-worker-router.json`
- `Yupcha__memXT.json`
- `ace-step__ACE-Step-1.5.json`
- `achref-soua__quiver.json`
- `activepieces__activepieces.json`
- `actualbudget__browser-app-demo.json`
- `addyosmani__agent-skills.json`
- `agent-sandbox__agent-sandbox.json`
- `agent0ai__spynel.json`
- `agentclientprotocol__python-sdk.json`
- `ai-forever__gpt2giga.json`
- `airbytehq__airbyte-agent-sdk.json`
- `alexbevi__EDDI.json`
- `alibaba__qz-browser-agent.json`
- `alphavantage__alpha_vantage_mcp.json`
- `amardeeplakshkar__awesome-free-llm-apis.json`
- `anomalyco__browser-control.json`
- `apache__casbin-gateway.json`
- `aw-junaid__bug-bounty.json`
- `awesome-selfhosted__awesome-selfhosted.json`
- `better-world-ai__x-cli.json`
- `bitwarden__server.json`
- `block__codecrucible.json`
- `borgbackup__borgstore.json`
- `browser-use__browser-use.json`
- `browserable__browserable.json`
- `bytedance__deer-flow.json`
- `caprover__caprover.json`
- `caramaschiHG__awesome-ai-agents-2026.json`
- `cbrock84__headcount.json`
- `charlie947__motion-graphics-skills.json`
- `cisco-ai-defense__mcp-scanner.json`
- `cline__cline.json`
- `cloudflare__sandbox-sdk.json`
- `cporter202__agentic-ai-apis.json`
- `debpalash__OpenGTM.json`
- `deuxfleurs-org__garage.json`
- `diegosouzapw__OmniRoute.json`
- `discourse__discourse-mcp.json`
- `docker-mailserver__docker-mailserver.json`
- `docling-project__docling-mcp.json`
- `documenso__documenso.json`
- `docusealco__docuseal-agent-skills.json`
- `dokku__sshcommand.json`
- `doobidoo__mcp-memory-service.json`
- `duckdb__duckdb-wasm.json`
- `dyad-sh__dyad.json`
- `e2b-dev__runtime.json`
- `element-hq__element-x-ios.json`
- `faucetdb__faucet.json`
- `flawiddsouza__Restfox.json`
- `frappe__frappe.json`
- `gepa-ai__gepa.json`
- `ggml-org__llama.cpp.json`
- `gitleaks__gitleaks.json`
- `gitroomhq__postiz-agent.json`
- `google__mantis.json`
- `h-guo18__TensorRT-LLM.json`
- `harry0703__MoneyPrinterTurbo.json`
- `hecatehq__hecate.json`
- `huggingface__pytorch-image-models.json`
- `iii-experimental__agentos.json`
- `imranraufbm__youtube-automation-agent.json`
- `jackwener__opencli-mcp.json`
- `jina-ai__cli.json`
- `juspay__neurolink.json`
- `kaushikb11__awesome-llm-agents.json`
- `kopia__kopia.json`
- `localai-org__vllm.cpp.json`
- `mail-in-a-box__mailinabox.json`
- `mailcow__mailcow-dockerized.json`
- `mailru__FileAPI.json`
- `matomo-org__device-detector.json`
- `mattpocock__skills.json`
- `maxkru92__OpenViking.json`
- `mcp-use__mcp-use.json`
- `meilisearch__meilisearch-mcp.json`
- `meltano__meltano.json`
- `mem0ai__mem0.json`
- `mem7ai__mem7.json`
- `metorial__metorial.json`
- `microsoft__Dataverse-skills.json`
- `milvus-io__bootcamp.json`
- `miqdadbadjuber__anti-slop.json`
- `mizorewww__laya-mlx.json`
- `mnfst__awesome-free-llm-apis.json`
- `mongodb__agent-skills.json`
- `mountain-loop__yaak.json`
- `mudler__LocalAI.json`
- `mufeedvh__code2prompt.json`
- `n8n-io__n8n.json`
- `nanobrowser__nanobrowser.json`
- `nicobailon__pi-mcp-adapter.json`
- `nmap__nmap.json`
- `obra__superpowers.json`
- `ocrmypdf__OCRmyPDF.json`
- `off-grid-ai__OGAD.json`
- `ollama__ollama.json`
- `open-free-llm-api__awesome-freellm-apis.json`
- `open-saas-directory__awesome-native-macosx-apps.json`
- `openai__tunnel-client.json`
- `openbao__openbao.json`
- `openclaw__clawscan.json`
- `openensemble__openensemble.json`
- `opensandbox-group__OpenSandbox.json`
- `opensearch-project__opensearch-agent-skills.json`
- `pablostanley__efecto-plugin.json`
- `pietrozullo__mcp-hubspot.json`
- `plausible__analytics.json`
- `postalserver__postal.json`
- `postmill-ai__postmill-app.json`
- `preloop__preloop.json`
- `prime-radiant-inc__streamlinear.json`
- `proffesor-for-testing__agentic-qe.json`
- `pydantic__pydantic-ai.json`
- `pytorch__rl.json`
- `relayroom__relayroom.json`
- `repoprompt__repoprompt-ce.json`
- `restic__rest-server.json`
- `reticlehq__reticle.json`
- `rezmoss__cloud-provider-ip-addresses.json`
- `rohitg00__pro-workflow.json`
- `ruvnet__ruflo.json`
- `safishamsi__FirstSight.json`
- `saiyam1814__memwarden.json`
- `sazonovanton__SirChatalot.json`
- `seaweedfs__seaweedfs.json`
- `senamakel__openintents.json`
- `sgl-project__sglang.json`
- `sherlock-project__sherlock.json`
- `shihabshahrier__freelm.json`
- `shobhitagnihotri69__preloop.json`
- `skillrecordings__products.json`
- `stablyai__orca.json`
- `stanfordnlp__dspy.json`
- `steel-dev__steel-browser.json`
- `stickerdaniel__browserjack.json`
- `stripe__ai.json`
- `stuinfla__ruvnet-brain.json`
- `superloglabs__superlog.json`
- `temporalio__sdk-go.json`
- `tester-army__scout.json`
- `the-open-agent__openagent.json`
- `thekaveh__rag-showcase.json`
- `theshiphq__claw-spark.json`
- `trailofbits__skills.json`
- `trycua__cua.json`
- `twentyhq__favicon.json`
- `typesense__typesense.json`
- `uber__ADR.json`
- `unslothai__unsloth.json`
- `usebruno__bruno.json`
- `usewrit__writ-plugins.json`
- `varun29ankuS__shodh-memory.json`
- `vercel-labs__agent-browser.json`
- `vercel__ai.json`
- `vibld__vibld.json`
- `weaviate__docs.json`
- `windmill-labs__windmill-cli-docs.json`
- `xihongshichaojidan8__deer-flow.json`
- `xpzouying__xiaohongshu-mcp.json`
- `yihui-dev__awesome-opus5-5-videos.json`
- `yt-dlp__yt-dlp.json`
- `zackchewa__awesome-china-mcp.json`
- `zeenie-ai__OpenCompany.json`
- `zulip__zulipmcp.json`

**Deep extraction metadata/audit files**
- `COLLECTION/AUTO/DEEP-EXTRACTED/DEFERRED-REPOSITORY-QUEUE.json`
- `COLLECTION/AUTO/DEEP-EXTRACTED/EXTRACTION-READY-QUEUE.json`
- `COLLECTION/AUTO/DEEP-EXTRACTED/MANIFEST.json`
- `COLLECTION/AUTO/DEEP-EXTRACTED/REPO-INVENTORY.json`
- `COLLECTION/VERIFICATION/CURRENT_MAIN_JSON_AUDIT.json`
