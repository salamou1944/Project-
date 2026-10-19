# Daily Collection & Agent Skills Operating Digest — 2026-10-19

## Reporting boundary
This digest records changes executed in this continuation and the new frontier state carried forward from the prior digest. It distinguishes committed source changes from CI/runtime proof. Current date is 2026-10-19 (Algeria, UTC+02).

## Accounts/repositories swept
- Re-read `salamou1944/Project-` `COLLECTION/INDEX.md`, current workflow directory, deep-extraction workflow, JSON-diff audit workflow, and current Collection commit history.
- Re-read `salamou1944/Salamou-31` `AI-API-HUB/api-factory/provider.mjs`, `AI-API-HUB/api-factory/provider-policy-test.mjs`, `AI-API-HUB/free-provider-policy-fixture.json`, `AI-API-HUB/test-free-provider-policy.mjs`, `AI-API-HUB/FREE-PROVIDER-POLICY.md`, and `.github/workflows/soat-runtime-integration.yml`.
- Re-read `salamou1944/agent-skills` `skills/browser-runtime-verification/SKILL.md`.
- Existing recursive Layer A snapshot remains at `COLLECTION/ACCOUNTS/RECURSIVE_ACCOUNT_FRONTIER_LAYER_A_2026-10-18.json`, commit `ff4af71f9e5fab97c059321835aaf3d696c8ed34`: 220 repository identity records across eight owner-scoped searches. This is metadata preservation, not full source extraction.
- A new Markdown owner-scanner companion was committed at `Project-@f6393d2de1f95695ab0b09e381f64cdc211a1a18` (`COLLECTION/ACCOUNTS/RECURSIVE_FRONTIER_LAYER_A_B_2026-10-19.md`). It connects the eight Layer A owners and eleven observed Layer B owners to the existing Markdown-driven extraction scanner, while explicitly preserving incompleteness. Repository rows for Layer B are still not committed. Additional downstream owner searches remain partially unpersisted: jackwener (47), stickerdaniel (75), daytonaio (12), e2b-dev (85), ChromeDevTools (19), agentclientprotocol (15), and first-page-only 100-row results for jina-ai, nicobailon, kurtmckee, xpzouying, and vercel-labs. The 100-row searches require pagination; do not mark these accounts exhausted.

## Valuable assets preserved
- Existing Layer A metadata snapshot retained without deleting or replacing earlier snapshots.
- Source-level candidates from the prior digest remain on shelf: Agent-Reach, Browser Harness, agent-browser, OpenSandbox, Jina Reader, mcporter, and feedparser. No external source was installed or activated in this continuation.
- Preserved the source's explicit distinction between provider policy discovery metadata and the API Factory runtime's fail-closed enforcement.

## Skills created or strengthened
- Strengthened existing canonical Skill `browser-runtime-verification`; no new semantically overlapping Skill created.
- Added checks for redirects ending at disallowed domains, explicit authorization before using logged-in sessions, recording-off defaults, separation of generated helpers from protected harness core, and redacted reproducible redirect evidence.
- Commit: `agent-skills@84b4732094d543410a9284ab687405b37fea8e4f`.
- Validation status: source update committed; no post-change Skill CI or browser runtime run has yet been observed.

## Dedupe/merge decisions
- Browser automation projects remain separate source assets because Agent-Reach is a multi-channel capability router, Browser Harness is a real-Chrome CDP harness, and agent-browser is a browser automation CLI. Only shared safety/verification contracts were merged into the canonical Skill.
- Sandbox alternatives remain a single comparison cluster; no duplicate Skills were created.
- Jina Reader and feedparser remain complementary ingestion tools, not duplicates.
- No source material was deleted or promoted to production.

## Validation evidence
- Prior successful Collection full-cycle run: `38841155076` (historical; not a new run against today's Layer A snapshot).
- Prior large-JSON audit unit-test run: `39002889620` (historical unit tests passed; no fresh full-data audit result claimed).
- API Factory deterministic tests, provider probe contract, Railway token-access smoke, and Free Resource Operator runs were reported as passed in the prior digest; these do not establish a successful real completion or production deployment.
- SOAT runtime integration run `39057060893` failed with `ProviderUnavailableError: Provider rejected by zero-cost policy: free_policy_incomplete`.
- Inspected failure cause: the CI-only local Ollama policy fixture omitted required `officialSourceVerified` and hard-coded `sourceLastResearched: "2026-10-05"`. The fixture was corrected to explicitly supply the verification field and a current synthetic local-only fixture date. This does not attest any hosted provider's free quota or billing terms.
- Workflow fix commit: `Salamou-31@bada4b0feede31853b4afd246deb0b514a5e1ed0`. A fresh run must pass before claiming runtime success.
- Collection index correction commit: `Project-@9d51d58aed9c079dd1ac55c03de4c0c10d9234cb`.
- Owner-scanner companion commit: `Project-@f6393d2de1f95695ab0b09e381f64cdc211a1a18`.
- Index follow-up linking the owner-scanner companion: `Project-@8e2df699cc59053532ab672985adb9eb18e11b92`.
- Fresh SOAT workflow run `39179590053` for commit `bada4b0feede31853b4afd246deb0b514a5e1ed0` was observed in progress during this digest; no conclusion yet.
- No production deployment was performed or proven.

## Ready-to-use assets/projects
- Collection Layer A JSON remains available for metadata lookup and later extraction.
- Canonical browser verification Skill now contains stronger written checks, ready for controlled use once its CI is validated.
- The API Factory test harness remains runnable in GitHub Actions, but real completion is unverified until the new SOAT workflow run completes successfully.

## Blocked or unverified
- Full Collection deep-extraction cycle has not been rerun against the new frontier.
- Additional downstream Layer B owner/repository records were not committed; several search pages require pagination.
- Fresh full-data large-JSON audit is unproven.
- API Factory runtime fix awaits a fresh SOAT workflow result.
- API Factory stable production deployment and durable registry/artifact storage remain unverified.
- No current runtime evidence proves a production-ready external asset or hosted provider.
- No MONY payment integration, paid conversion, commission, or payout was proven.

## Downstream accounts opened
- Committed Layer A: Panniantong, pietrozullo, browser-use, safishamsi, metorial, opensandbox-group, public-clis, yt-dlp.
- Additional observed but incompletely persisted: jackwener, stickerdaniel, daytonaio, e2b-dev, ChromeDevTools, agentclientprotocol, jina-ai, nicobailon, kurtmckee, xpzouying, vercel-labs.
- Microsoft remains targeted-repository-only (Playwright and Playwright MCP); not an account-wide sweep.

## Exact GitHub commits/evidence
- Frontier snapshot: `Project-@ff4af71f9e5fab97c059321835aaf3d696c8ed34`.
- Browser verification Skill strengthening: `agent-skills@84b4732094d543410a9284ab687405b37fea8e4f`.
- SOAT local-only fixture correction: `Salamou-31@bada4b0feede31853b4afd246deb0b514a5e1ed0`.
- Collection index reconciliation: `Project-@9d51d58aed9c079dd1ac55c03de4c0c10d9234cb`.
- Prior SOAT failing run: https://github.com/salamou1944/Salamou-31/actions/runs/39057060893
- Prior audit unit-test run: https://github.com/salamou1944/Project-/actions/runs/39002889620
- Current Layer A file: https://github.com/salamou1944/Project-/blob/main/COLLECTION/ACCOUNTS/RECURSIVE_ACCOUNT_FRONTIER_LAYER_A_2026-10-18.json

## Current verdict
Preserved/discovered: yes, including the committed frontier snapshot and updated canonical Skill.
Source-level fix committed: yes, for the local-only SOAT smoke fixture.
Runtime-proven/production-ready: no new proof in this continuation. Wait for the fresh SOAT workflow result; do not relax the zero-cost gate or treat the fixture as production provider attestation.


## Additional connected-app and repository sweep — 2026-10-19
- Read-only inventory confirmed the GitHub connector exposes exactly 10 repositories under `salamou1944` and no organization memberships: `Salamou-31`, `agent-skills`, `Easy-`, `AI_operating_memory`, `Astra-`, `Astra`, `Files-`, `Project-`, `Pastel-`, and `local-bridge.`. Root entry points were inspected for all ten; detailed account/application findings are preserved in [CONNECTED_APP_FRONTIER_AUDIT_2026-10-19.md](../VERIFICATION/CONNECTED_APP_FRONTIER_AUDIT_2026-10-19.md).
- Additional useful project-state evidence: ASTRA's research gate remains failed for profitability/alpha and live execution remains OFF; EASY's own boundary explicitly forbids production claims before provider, persistence, auth, integrity and deployed E2E proof; local-bridge requires a real Windows runner registration.
- Read-only connected-app checks: Railway has two projects; API Factory service currently has no direct service variable names and its latest five listed deployment records are removed. Supabase shows only the EASY database, which must not be reused for API Factory. Termalin reports zero reachable hosts; Vercel reports no teams; GitLab's sole owned project is empty.
- Commerce/design/workspace checks: Shopify store is on trial; Wix lists no sites; Canva search returned no matching designs; Notion is connected but the relevant project search returned no results; Figma account is View-seat with Code Layers disabled.
- AgentMail checked `api-pilot@agentmail.to`, `easy@agentmail.to`, and `pastel-realtime-e2e@agentmail.to`: current visible API Pilot/EASY threads are delivery failures/bounces; PASTEL test inbox has no threads. No reply, acceptance, payment, or revenue proof. No outbound messages were sent and no paid prospecting credits were spent.
- Workflow wiring fixes committed: `Project-@91881560d9a6abf7ac1a3df57a524beeb192e05a` (frontier-triggered deep extraction), `Project-@ecffc50fe490de89b63e3dfba87efe72f52ea6af` (JSON diff audit trigger/fallback SHA), `Project-@b36a1fc3aee466c9b4a7e9a83eb25cc4b94b0226` (current Collection JSON audit script), and `Project-@857010f226ccd7efdde94a22297d19ed32237053` (frontier commit that started run `39180002514`).
- Connected-app audit report commit: `Project-@f2fc1a3519629d1ad00ab5050679b91243e150dc`.
- Run `39180002514` was still pending at last poll; no extraction count or JSON audit output is yet claimed.
- SOAT run `39179590053` has passed the dedicated real AI completion through the local Ollama provider, but the overall workflow remains in progress while the official SOAT smoke and downstream evidence gates execute.


## Critical supply-chain finding — free LLM API catalogue — 2026-10-19
- Inspected the latest `mnfst/awesome-free-llm-apis` commit history and current `.github/workflows/` directory.
- Found historical commit `48fcbe86582e16b7b746fee52e5512a891a8db76` adding a malicious “Security Audit” workflow: it searched the current repository and Git history for credential patterns and POSTed findings to hard-coded external HTTP endpoint `193.32.204.199:8080`.
- The workflow was removed in commit `cf97c32fec1b2e96e9936746e2731a81bd5ea33f`. Current workflow listing contains only `generate-readme.yml`. No Security Audit run appeared in the latest 30 visible Actions runs, so execution is not evidenced but cannot be ruled out.
- Preserved this as a supply-chain warning in `COLLECTION/ACCOUNTS/MNFST_ACCOUNT_WIDE_2026-10-16.md` and the canonical monetization ledger. The catalogue remains a discovery source only; never run its workflows/scripts or pass secrets to it. No secrets were searched for or transmitted.
- Commit review links: https://github.com/mnfst/awesome-free-llm-apis/commit/48fcbe86582e16b7b746fee52e5512a891a8db76 and https://github.com/mnfst/awesome-free-llm-apis/commit/cf97c32fec1b2e96e9936746e2731a81bd5ea33f.


## API Factory local-runtime verification completed — 2026-10-19
- Fresh run [39179590053](https://github.com/salamou1944/Salamou-31/actions/runs/39179590053) is now **completed / success** (workflow run #115).
- Verified inside GitHub Actions: API Factory deterministic tests; system-message mapping; pinned SOAT health/auth; authenticated local Ollama provider; API Factory provider probe; real chat completion; official SOAT smoke suite; execution-contract validation; verification-record persistence; evidence consumption; business outcome gate; artifact upload; runtime cleanup.
- Official SOAT smoke evidence: `status=passed`, `exitCode=0`, `timedOut=false`, `durationMs=296089`. Business gate returned `ENTRY_POINT_VERIFIED`; consumed evidence has `verified=true` and `productionStatus=not_proven`.
- Artifact `soat-verification-39179590053` ID `12155088912`, SHA-256 `4b7a721294b6e53086e2e89a65c71231906029487383ceeb6ce3dd79b7f0faf5`; expires 2027-01-17. Permanent summary at [API_FACTORY_SOAT_LOCAL_RUNTIME_2026-10-19.md](API_FACTORY_SOAT_LOCAL_RUNTIME_2026-10-19.md), commit `Project-@4d871be4d16af72105699b97077e3cdfe41870e1`.
- This is valid CI-pinned local-runtime proof, not production deployment/storage proof or a commercial/free-quota attestation for hosted providers. The explicit `production_status=not_proven` was preserved.
- Collection automation: created a current-main JSON audit that stores byte sizes, SHA-256 hashes, root shapes and record counts; the extractor now runs on recursive frontier changes. Full extraction run `39179989521` remained in progress at last poll; queued follow-up run `39180283329` is pending. No extraction count or audit result has been claimed yet.
- Free-provider security review found the removed credential-exfiltration workflow in `mnfst/awesome-free-llm-apis`; preserved it in the MNFST account capture and canonical monetization ledger. No credentials were searched for or transmitted.


## Frontier expansion correction — 2026-10-19
- Rechecked the active extraction graph against `COLLECTION/MASTER/ACCOUNT_COMPLETION_REGISTER_2026-10-06.md`. The prior companion listed only the 8 Layer A and 11 Layer B targets; it did not materialize the register's broader 138+ owner frontier.
- Fixed that gap: 40 enumerated-account rows plus 116 newly exposed names normalized to 151 distinct GitHub owner targets; all 151 URLs are now committed in the scanner's Markdown input graph at `Project-@0d5c7a50ddfc503de0ac39ba12b42683ebe82f14`.
- Updated the scanner to deduplicate mixed-case owner logins: `Project-@4a5011bd27c8ce3558e298b99f2669b07d875b51`. Updated workflow concurrency so the newest frontier supersedes stale queued work: `Project-@dc8ffb98b59d0e51313749917310048b5d33f2e4`.
- The new full-frontier run `39180598182` was pending at last poll. Earlier run `39179989521` started before the 151-owner materialization and must not be used as the final extraction proof even if it finishes successfully. Use the newest full-frontier run's manifest and JSON audit output.
- Next step after that run succeeds: trigger the full Collection workflow via `.github/COLLECTION_SAFE_INCREMENTAL_ONCE`, then inspect all test, policy, install and persisted-evidence gates. The full Collection workflow has not yet been triggered because it must check out the completed extraction commit.


## Connected workspace follow-up and revenue sweep request — 2026-10-19
- Extended Notion inventory (private sidebar, favorites, recent pages) returned zero pages/databases through these read tools; Canva searches for EASY and API Factory returned zero matching designs. These are access-surface results, not proof that all connected workspaces are empty.
- AgentMail inbox inventory confirms three inboxes and zero signed-in AgentMail app accounts. Existing visible outreach threads are bounces, not customer replies.
- Requested an immediate run of the enabled `Revenue + leverage sweep` automation (`6ab730fda9948191a73f262cdb30fa92`). The request was accepted, but execution is asynchronous; results are not yet available and no completion is claimed.


## Outreach suppression evidence — 2026-10-19
- Persisted 11 observed failed-delivery recipients in the canonical monetization ledger with dates and suppression guidance. Do not retry without independent address verification and a fresh check that the opportunity is still active.
- This prevents duplicate/spammy outreach. Bounces do not count as leads; no outbound email was sent in this sweep.


## OmniRoute source recheck — 2026-10-19
- Inspected the current `release/v3.8.52` README, `FREE_TIERS.md`, `.env.example`, `SECURITY.md`, Docker Compose, package manifest, postinstall helper and workflow directory.
- README figures moved from the prior capture's 372 providers / 485 entries / 35 pools to 375 providers / 468 entries / 34 pools. The current free-tier document is marked updated 2026-10-18 but still describes full research from 2026-06-17 and partial re-audit 2026-09-02; no automatic zero-cost routing from these aggregate claims.
- Repo is MIT but ~1.76 GB. It requires unique `JWT_SECRET` and `API_KEY_SECRET`, warns the sample `INITIAL_PASSWORD=CHANGEME` is public, and relies on SQLite persistence. No installation or runtime import performed.
- Preserved as provider-intelligence only; the gateway remains on the shelf until per-provider official terms/quota/eligibility/hard-stop checks are current.


## Owner URL parsing hardening — 2026-10-19
- Found a second extraction gap: the original URL regex only recognized raw owner URLs followed by whitespace or a slash, so it could miss GitHub URLs embedded in Markdown links with closing punctuation.
- Fixed the scanner to accept URL terminators, strip trailing punctuation, and deduplicate owners case-insensitively: commit `Project-@79604426ec98243c0bcef7c5e7c4ecf49a2599e5`.
- Run `39180598182` began before this fix and must not be the final proof. Run `39180853004` is the queued run with both the 151-owner frontier and corrected parser; await its final result and persisted manifest/audit before triggering full Collection.


## PR #45 state and deployment boundary reconciliation — 2026-10-19
- Verified PR #45 is merged, not open: merge commit `172328b929513d4a5909a22da4954cd988aa2343`, merged 2026-10-17T18:12:09Z. Its body contains a stale “open and unmerged” line; the GitHub API merge metadata wins.
- PR body records a historical Vercel deployment `dpl_4vmQMfn4hr5SahXSJxf1ruh8pbYs` as READY at merge time. Current connected Vercel context returns no teams, so current alias/management access is not re-proven.
- Railway API Factory service config is wired to the feature branch and has a domain/health path, but direct service variable names are empty and its latest five deployment records are removed. This is not a live-production proof.
- The only visible Supabase project is EASY's healthy database; do not reuse it for API Factory. Separate durable storage, service secrets, migration and cross-invocation persistence remain blockers. Successful CI-pinned SOAT/Ollama proof is recorded separately and does not close production gates.


## MNFST provider-data freshness recheck — 2026-10-19
- Latest visible provider/model refresh was 2026-10-05; later commits only added and then removed the malicious security-audit workflow. Current workflow directory has a README generator triggered by `data.json` changes, not an observed nightly provider-sync workflow.
- The Oct 5 refresh contains useful updates (including retired NVIDIA NIM rows and changes to Gemini, Cloudflare, Groq, Kilo, LLM7, OpenRouter and OVHcloud) but also unprobed entries and an explicit human-review queue. No post-Oct-5 provider/model refresh is evidenced in the latest 10 commits.
