# COLLECTION — Research Index

Status: INCREMENTAL_COLLECTION
Updated: 2026-10-21


## 2026-10-20 operator update

- **Collection path/policy repair:** `COLLECTION/AUTO/process_collection.py` anchors generated paths to repository root (commit `909f8781c77143e950600fdbb54a8e6c0666fb72`). Path/quarantine and full policy regression passed in [run 39360757036](https://github.com/salamou1944/Project-/actions/runs/39360757036).
- **Layer B frontier persisted:** [snapshot](./ACCOUNTS/RECURSIVE_ACCOUNT_FRONTIER_LAYER_B_2026-10-20.json) contains 1,523 public repository-search identities across 11 owners. The companion [recursive frontier](./ACCOUNTS/RECURSIVE_FRONTIER_LAYER_A_B_2026-10-19.md) is the active Markdown owner graph; it currently exposes 168 distinct owner targets. The snapshot is discovery metadata, not proof that every repository was deeply extracted.
- **Deep extraction succeeded:** [run 39477969342](https://github.com/salamou1944/Project-/actions/runs/39477969342) selected 200 repositories across 199 owners, successfully extracted 199, preserved 1 blocked source, and retained 7,230 extraction packets.
- **Eighteen bounded incremental Collection cycles completed:** [cycle 1](https://github.com/salamou1944/Project-/actions/runs/39479259044) refreshed 97/100; [cycle 2](https://github.com/salamou1944/Project-/actions/runs/39479747706) refreshed 95/100; [cycle 3](https://github.com/salamou1944/Project-/actions/runs/39480516260) refreshed 93/100; [cycle 4](https://github.com/salamou1944/Project-/actions/runs/39481555664) refreshed 93/100; [cycle 5](https://github.com/salamou1944/Project-/actions/runs/39481898485) refreshed 92/100; [cycle 6](https://github.com/salamou1944/Project-/actions/runs/39482419900) refreshed 92/100; [cycle 7](https://github.com/salamou1944/Project-/actions/runs/39482839422) refreshed 90/100; [cycle 8](https://github.com/salamou1944/Project-/actions/runs/39483313802) refreshed 90/100; [cycle 9](https://github.com/salamou1944/Project-/actions/runs/39488759316) refreshed 85/100; [cycle 10](https://github.com/salamou1944/Project-/actions/runs/39489208896) refreshed 84/100; [cycle 11](https://github.com/salamou1944/Project-/actions/runs/39510398181) refreshed 83/100; [cycle 12](https://github.com/salamou1944/Project-/actions/runs/39515408033) refreshed 83/100; [cycle 13](https://github.com/salamou1944/Project-/actions/runs/39515767352) refreshed 81/100; [cycle 14](https://github.com/salamou1944/Project-/actions/runs/39516131418) refreshed 81/100; [cycle 15](https://github.com/salamou1944/Project-/actions/runs/39516867197) refreshed 80/100; [cycle 16](https://github.com/salamou1944/Project-/actions/runs/39517215028) refreshed 80/100; [cycle 17](https://github.com/salamou1944/Project-/actions/runs/39517526827) refreshed 80/100 and preserved 20 blocked attempts; [cycle 18](https://github.com/salamou1944/Project-/actions/runs/39533389021) refreshed 79/100 and preserved 21 blocked attempts. Across these cycles: 1,558 refreshed sources, 242 blocked source attempts preserved, and 5,029 extracted source artifacts (5,050 manifest source rows). The deferred queue contains 18,551 repositories; each run remains deliberately bounded at 100 selected repositories.
- **Generated JSON size remediation:** cycle 16 preserved all records with one decision per line. Current sizes after cycle 17: `READY.json` 78,438,820 bytes (GitHub still warns above its recommended 50 MB); `PROMOTION-QUEUE.json` 46,401,101; `CANONICAL-PROMOTION-PLAN.json` 52,974,530; `READINESS-QUEUE.json` 19,810,106; `VALUE-OPERATOR-QUEUE.json` 17,911,012; `RESTRICTED-QUEUE.json` 32,037,473. The post-generation size guard passed; it blocks a commit at 95,000,000 bytes before the GitHub hard limit.
- **Latest current-main JSON audit:** [report](./VERIFICATION/CURRENT_MAIN_JSON_AUDIT.json) covers 12,942 JSON/JSONC files, 0 parse failures, and 907,402,672 bytes; audit validation passed in cycle 17 (run 39517526827). The latest cycle also passed promotion/readiness/callable-policy checks: 44,828 capability/readiness groups, 30,691 promotion-review items, 14,137 restricted items, and 55 skill definitions.
- **Installation policy remains fail-closed:** cycle 17 reported `NO_APPROVED_CANDIDATES`; 0 assets were installed or promoted, 0 items were marked ready for verification, and 0 runtime-readiness claims were emitted. This is an explicit safe no-op; the large review queue is not an install approval.
- **Secret-safe extraction hardening:** follow-up workflow [39498298198](https://github.com/salamou1944/Project-/actions/runs/39498298198) was blocked by GitHub push protection after a generated source packet matched Google OAuth access-token detection; no bypass was used, and the rejected packet is not present on `main`. Shared sanitization now redacts the Google `ya29.` access-token format, and deep extraction uses the shared sanitizer while preserving source hash and redacted-content hash. Regression workflow [39510149336](https://github.com/salamou1944/Project-/actions/runs/39510149336) passed, and the post-fix cycle 11 rerun [39510398181](https://github.com/salamou1944/Project-/actions/runs/39510398181) passed. Cycle 10 remains historical evidence from the earlier sanitizer version.
- **API Factory / Render state:** the dedicated Supabase project `dyhkdijpkddfsrwruumc` has active `api-factory-storage` Edge Function version 3 with a compare-and-swap registry readiness probe. [Latest dual-endpoint smoke](https://github.com/salamou1944/Salamou-31/actions/runs/39481681851) verified the preview as `DURABLE_STORAGE_VERIFIED` (HTTP 200) and the main Render service as `DURABLE_STORAGE_REQUIRED` (HTTP 503; both stores still `local-file`). The main service is live on runtime commit `83f69126689eaac920f044b1e54cb8878d52fffc`, but it is **not production-ready** until its gateway key/configuration and any existing local registry/artifacts are safely verified and migrated. The EASY Supabase project was not reused, and no new paid resource was created.
- **API Factory safety gates:** PRs [#46](https://github.com/salamou1944/Salamou-31/pull/46), [#47](https://github.com/salamou1944/Salamou-31/pull/47), [#48](https://github.com/salamou1944/Salamou-31/pull/48), [#49](https://github.com/salamou1944/Salamou-31/pull/49), and [#50](https://github.com/salamou1944/Salamou-31/pull/50) are merged. The local SOAT/Ollama real-completion smoke passed in [run 39479201839](https://github.com/salamou1944/Salamou-31/actions/runs/39479201839), but that evidence explicitly says `productionStatus: not_proven`. Deployment execution remains unimplemented, and generated runtime quota/usage/idempotency state is still not durable by default.
- **Provider-cost guard:** real provider probes now require provider-specific repository billing-tier variables explicitly set to `free`; otherwise they emit `NOT_VERIFIED` with `network_requests_made: 0`. This is not a real-completion claim.

## 2026-10-19 operating update

> Historical snapshot: run states below reflect what was known when this section was written. Later completed outcomes and the 2026-10-20 repair are recorded in subsequent entries; use those later records for current status.

- **Frontier preserved:** Layer A snapshot `COLLECTION/ACCOUNTS/RECURSIVE_ACCOUNT_FRONTIER_LAYER_A_2026-10-18.json` contains 220 repository identities across 8 owners; it is metadata, not deep source extraction. Commit: `ff4af71f9e5fab97c059321835aaf3d696c8ed34`.
- **Extraction graph corrected:** the Markdown owner companion now materializes 151 case-insensitively distinct owner targets from the master account register plus the 8 Layer A and 11 observed Layer B targets. Owner parsing now handles raw URLs, Markdown links, closing punctuation, repository paths, and mixed-case duplicates. Commits: `0d5c7a50ddfc503de0ac39ba12b42683ebe82f14`, `4a5011bd27c8ce3558e298b99f2669b07d875b51`, `79604426ec98243c0bcef7c5e7c4ecf49a2599e5`. Parser/batch tests passed in [run 39181762906](https://github.com/salamou1944/Project-/actions/runs/39181762906).
- **Scalable extraction:** source-packet extraction is now bounded to 200 high-priority repos per run (max 2 per owner, 24 files/repo, 50 KB/file, 300 KB source bytes/repo), while full public repo metadata is preserved in `REPO-INVENTORY.json` and deferred work is retained in `DEFERRED-REPOSITORY-QUEUE.json`. This avoids dumping thousands of repos into GitHub while losing no discovered repo identities. Code commit: `76f9944042481a0a8d1e4cb332a46326e078f288`.
- **Current run:** [bounded deep extraction 39181614341](https://github.com/salamou1944/Project-/actions/runs/39181614341) is in progress. Earlier unbounded run `39180853004` was cancelled before commit. Do not claim full inventory/extraction counts or audit hashes until the bounded run finishes and its manifest/report are committed.
- **Canonical extraction is now bounded too:** `intelligent_extract.py` reuses `DEEP-EXTRACTED/REPO-INVENTORY.json` rather than repeating the owner/repository enumeration; it selects at most 100 additional repos per run and at most 1 per owner, skips current cached packets and successful deep packets, caps new source packets at 300 KB/repo, and writes a canonical deferred queue. The full workflow requires the shared inventory and fails closed if it is missing/empty. The state guard now reconciles processed rows plus preserved prior rows without weakening the 2,500-row safety floor. Tests passed in [run 39183464384](https://github.com/salamou1944/Project-/actions/runs/39183464384).
- **Force-refresh semantics fixed:** a force-refresh run remains capped at 100 repos / 1 per owner and prioritizes the oldest cached packets, so repeated runs advance through the cache rather than repeatedly refreshing the same top batch. The workflow input description now reflects this bounded behavior. Test run [39183664442](https://github.com/salamou1944/Project-/actions/runs/39183664442) passed.
- **JSON audit:** `audit_current_collection_json.py` now inventories file sizes, SHA-256, root shapes, array counts and parse failures. `validate_current_collection_json_audit.py` checks report integrity. Workflows preserve the report before enforcing parse-failure gates. The full Collection workflow has **not** yet been triggered; update the existing `.github/COLLECTION_SAFE_INCREMENTAL_ONCE` marker only after the bounded extraction commit.
- **Install safety:** `install_assets.py` now requires explicit `INSTALL_APPROVED`, `install_approval=APPROVED`, `integration_gate=PASS`, and `security_gate=PASS`; legacy source notes and deep-extraction packets no longer feed automatic installation. With no approved queue items, the workflow records `NO_APPROVED_CANDIDATES` rather than inventing an install success. Selection/outcome tests passed in [latest run 39182760594](https://github.com/salamou1944/Project-/actions/runs/39182760594); earlier run 39182669136 also passed. Existing Hyperswitch source remains preserved and not runtime-promoted: [legacy install boundary](VERIFICATION/LEGACY_INSTALLED_ASSETS_2026-10-19.md).
- **API Factory:** PR #45 is merged at `172328b929513d4a5909a22da4954cd988aa2343`. The corrected local-only Ollama/SOAT smoke [39179590053](https://github.com/salamou1944/Salamou-31/actions/runs/39179590053) passed through real chat completion and persisted evidence, but this is CI proof only. Stable production deployment and durable registry/artifact storage remain unverified.
- **Browser Skill:** canonical `browser-runtime-verification` strengthened at `agent-skills@84b4732094d543410a9284ab687405b37fea8e4f`; no duplicate Skill. No check runs or post-change browser-runtime test were observed.
- **Supply-chain risk:** `mnfst/awesome-free-llm-apis` briefly added a credential-exfiltration workflow, then removed it. No run was visible in the latest 30 Actions runs, but execution remains unverified. The provider catalogue has no evidenced data refresh after 2026-10-05.
- **Revenue boundary:** MONY remains blocked until a real billing provider and qualifying event are verified. Upwork currently has 0 Connects and a private/incomplete profile; Apollo balances were inspected read-only and no credits were spent. See [connected app audit](VERIFICATION/CONNECTED_APP_FRONTIER_AUDIT_2026-10-19.md), [Upwork/Apollo readiness](VERIFICATION/UPWORK_REVENUE_READINESS_2026-10-19.md), and [daily digest](VERIFICATION/DAILY_DIGEST_2026-10-19.md).

## Purpose
Central collection of repositories, documentation, tools, and reusable implementation knowledge discovered during research. Priority: free/open-source/self-hosted capabilities that can reduce paid SaaS/API dependencies.

## API Factory deployment and persistence gate
- Latest recovery attempt: [API Factory deployment recovery — 2026-10-17](VERIFICATION/API_FACTORY_DEPLOYMENT_RECOVERY_2026-10-17.md). A preview-only workflow was added and run; it safely skipped because GitHub Actions secret `VERCEL_TOKEN` is absent. Vercel connector scope `bleu5` still returns 403; no production alias changed.

- Latest operator recheck: [API Factory operator recheck — 2026-10-17](VERIFICATION/API_FACTORY_OPERATOR_RECHECK_2026-10-17.md). Confirms current smoke run #44 correctly rejects degraded HTTP 200, the latest listed Vercel deployment source differs from the PR head, and Vercel scope access is blocked by 403; no EASY resources or paid services were touched.

- Current source commit: `salamou1944/Salamou-31@172328b929513d4a5909a22da4954cd988aa2343` (PR #45 is merged). Latest SOAT integration run `39057060893` failed closed with `free_policy_incomplete`; workflow fixture omitted `officialSourceVerified` and carried a stale hard-coded research date. The CI-only local Ollama fixture was corrected in `Salamou-31@bada4b0feede31853b4afd246deb0b514a5e1ed0` to supply the explicit verification field and a current synthetic fixture date. This is a source fix only until a fresh workflow run passes; it is not production provider attestation.
- Runtime smoke history and latest correction: [API Factory Vercel smoke evidence](VERIFICATION/API_FACTORY_VERCEL_SMOKE_2026-10-16.md).
- Important: health success does not prove persistent registry/artifacts. Source now requires durable registry + artifact storage for `/ready` to return HTTP 200; ephemeral Vercel `/tmp` must return HTTP 503.
- Deterministic API Factory test suite passed in runs #413 and #414. The stricter live-smoke workflow failed run #44 for the correct reason: the stable Vercel alias still returns HTTP 200 while `degraded: true` and both persistence checks are false. This is a deployment/storage blocker, not a test assertion to weaken. Vercel environment names confirm only `/tmp` registry/artifact paths and no durable Supabase adapter variables.
- Blocker: no reusable Render service/database/Key Value instance was found. Do not reuse EASY Supabase; no new resource or paid plan was created.

## Permanent agentic AI discovery sources
- Agent Zero — https://github.com/agent0ai/agent-zero
- cporter202/openclaw-api-list — https://github.com/cporter202/openclaw-api-list
- openclaw/mcporter — https://github.com/openclaw/mcporter
- agentic-ai-apis — https://github.com/cporter202/agentic-ai-apis
- ruvnet/ruflo — https://github.com/ruvnet/ruflo

## Permanent account-wide collection sources
- Mem0ai — https://github.com/mem0ai/mem0
  - Permanent AI-memory/retrieval source added for ASTRA/AI Operating Memory comparison.
  - Priority leverage: long-term agent memory, multi-signal retrieval, temporal/entity-aware memory, deduplication and memory lifecycle/evaluation.
  - Rule: inspect Mem0 primitives against existing ASTRA/TinyCortex/agent-skills before adopting; do not duplicate existing capabilities.

- senamakel — https://github.com/senamakel
  - Account-wide source added: COLLECTION/ACCOUNTS/SENAMAKEL_2026-10-04.md
  - High-priority verified repositories: openhuman, opencompany, medulla, tinyagents, tinyinference, tinycortex, tinysearch, openhuman-skills, agent-ctrl, tinyhivemind, tinyflows, tinymcp, tinymemory, tinyjuice.
  - Strategic relevance: agent orchestration, durable execution/state, memory/provenance, provider routing, search/evidence, parallel agent operations and one-person-company automation.
  - Inventory discrepancy is recorded: profile view showed 71 repositories while connected GitHub search returned 89 accessible public records; full enumeration must reconcile this before exhaustion.

- Mattpocock — https://github.com/mattpocock
  - Account-wide capture: COLLECTION/ACCOUNTS/MATTPOCOCK_2026-10-08.md
  - Enumerated: 223 public repositories on 2026-10-08.
  - Primary high-value source: mattpocock/skills — MIT, verified package version 1.3.1.
  - Priority leverage: composable engineering Agent Skills, research/evidence, TDD, code review, diagnosis, domain modeling, architecture, triage, ticket/spec generation, handoff and human-only setup boundaries.
  - Reuse rule: semantic dedupe against existing agent-skills/SOAT/ASTRA capabilities; extract only materially stronger or missing contracts; preserve MIT provenance.\n- miqdadbadjuber — https://github.com/miqdadbadjuber
  - Account-wide source added: COLLECTION/ACCOUNTS/MIQDADBADJUBER_2026-10-04.md
  - GitHub profile currently reports 11 public repositories.
  - Primary verified source: anti-slop — https://github.com/miqdadbadjuber/anti-slop — MIT, latest inspected release v3.2.20.
  - Additional repositories surfaced by the author's portfolio: portfolio, contextforge, DiagramPilot-AI, OpenFolio-AI; each requires independent repository-level verification.
  - Priority leverage: agent quality/delivery gates, cross-agent skill distribution, context engineering, architecture-diagram generation, portfolio tooling.
  - Enumeration rule: all 11 public repositories must be inventoried and processed before the account is considered exhausted.

- Panniantong — https://github.com/Panniantong
  - Account capture: COLLECTION/ACCOUNTS/PANNIANTONG_2026-10-04.md
  - Enumerated: 38 public repositories.
  - High-value sources include Agent-Reach, last30days-skill, new-api-neo, CLIProxyAPI, sub2api, xfetch, skillshare, openclaw.
  - Downstream account discovered: mvanhorn; full enumeration pending.
- Cbrock84 — https://github.com/Cbrock84
  - Account target discovered and enumerated: 57 public repositories.
  - Intended capture: COLLECTION/ACCOUNTS/CBROCK84_2026-10-04.md
  - High-value sources inspected: gstack, superpowers, strix, prowler, aikido-safe-chain, tradingagents, lumibot, freqtrade.
  - Persistent account capture write was blocked by the GitHub tool security layer during this cycle; therefore this entry records the account as a discovered/queued source, not as a falsely claimed completed capture.
- OpenCut-app — https://github.com/OpenCut-app
  - Account-wide source discovered and enumerated: 4 public repositories.
  - High-value sources: OpenCut, opencut-classic, ffmpeg-rust.
  - OpenCut is MIT-licensed; current rewrite targets a Rust core, Editor API, plugin architecture, MCP server, headless/batch rendering, and scripting.
  - opencut-classic is archived; retain it as historical/implementation reference.
- Pablostanley — https://github.com/pablostanley
  - Account capture: COLLECTION/ACCOUNTS/PABLOSTANLEY_2026-10-04.md
  - Enumerated in the current GitHub collection pass: 37 public repositories.
  - Immediate high-value queue: yoinks, squig, efecto-plugin, hilos-agents, pixabots, typexperiments, designteam-app/designteam, vgpu, vercel-slides.
- debpalash — https://github.com/debpalash
  - Account-wide source discovered and enumerated: 37 public repositories in the current GitHub collection pass.
  - Account capture: COLLECTION/ACCOUNTS/DEBPALASH_2026-10-04.md
  - Immediate high-value queue: VoiceStudio, OpenGTM, Friday, Opal, agentwork, awesome-mcp-servers, remotions-video, open-agi.
  - Priority leverage: local-first voice/audio, self-hosted GTM/lead enrichment, MCP/agent tooling, media/browser infrastructure.
- h-guo18 — https://github.com/h-guo18
  - Account-wide source discovered and enumerated: 20 public repositories in the current GitHub collection pass.
  - Account capture: COLLECTION/ACCOUNTS/H-GUO18_2026-10-04.md
  - Immediate high-value queue: vllm-kimidumper, Model-Optimizer, SnapKV, stablehlo, TensorRT-LLM, FinancialDatasets, ZhWiki-Retrieval-System, fewshotgen.
  - Priority leverage: inference optimization, quantization/KV-cache efficiency, ML compiler portability, retrieval and financial-data research.
- ARPAHLS — https://github.com/ARPAHLS
  - Account-wide source discovered and enumerated: 19 public repositories in the current GitHub collection pass.
  - Account capture: COLLECTION/ACCOUNTS/ARPAHLS_2026-10-04.md
  - Immediate high-value queue: skillware, rooms, aura, mnemolink, micro-f1-mask, avatar, vic_aisaq_demo, lc0_vic, OPSIE, gatekeeper.
  - Priority leverage: modular skills, local-first multi-agent orchestration, agent-loop runtime, agent memory/personas, PII scrubbing, local avatar/agent UI, storage-aware retrieval and policy/security tooling.
- zeenie-ai — https://github.com/zeenie-ai
  - Account-wide source discovered and enumerated: 6 public repositories.
  - Account capture: COLLECTION/ACCOUNTS/ZEENIE-AI_2026-10-04.md
  - Immediate high-value queue: OpenCompany, docs-OpenCompany, edgymeow, AgentEmpire, temporal-server, Kimi-K3.
  - Priority leverage: AI employees/workflow orchestration, approvals and bounded execution, skills/memory, browser/WhatsApp integrations, Temporal workflow runtime, and open-weight agentic models.
- rohitg00 — https://github.com/rohitg00
  - Account-wide source discovered; GitHub profile currently reports 320 public repositories.
  - Account capture: COLLECTION/ACCOUNTS/ROHITG00_2026-10-04.md
  - Current high-value queue: agentmemory, pro-workflow, skillkit, agentbrain, ai-engineering-from-scratch, rimuru, kubectl-mcp-server, awesome-claude-code-toolkit, awesome-openclaw.
  - Priority leverage: persistent agent memory, self-correcting workflows, portable skills, evidence-first agent operation, MCP/infrastructure control, agent observability/cost control, and reusable AI-engineering artifacts.
  - P0 leverage assessment: COLLECTION/VERIFICATION/ROHITG00_P0_LEVERAGE_ASSESSMENT_2026-10-04.md
  - Full account enumeration: COMPLETE for 320 public repositories returned by four owner-scoped search pages on 2026-10-04; downstream account expansion remains pending.

- Wassimyounes01 — https://github.com/Wassimyounes01
  - Account-wide source added: COLLECTION/ACCOUNTS/WASSIMYOUNES01_2026-10-04.md
  - Initial profile view reported 21, but owner-scoped GitHub repository search on 2026-10-04 returned 47 public repositories; the discrepancy is recorded rather than hidden.
  - Primary verified source: qwen38-uncensored — local Qwen 3.8 27B abliterated/uncensored serving harness with Ollama and optional MLX paths.
  - High-value sources inspected include agent-os, event-driven-autonomous-loop, Genesis evidence/context/routing/review components, memory, fusion, bugbot, autonomous-loop, megacycle, ai-video-studio-kit, apify-replacement, and agent-workbench.
  - Priority leverage: free/local inference, autonomous execution, evidence-bound orchestration, self-hosted prospecting, media tooling, routing/cost control and persistent memory.
  - Enumeration rule: all 47 repositories returned by the current owner-scoped search are inventoried; repository-level inspection is now broad but account exhaustion still requires checking newly appearing repositories in future collection passes.

- charlie947 — https://github.com/charlie947
  - Account-wide source added: COLLECTION/ACCOUNTS/CHARLIE947_2026-10-04.md
  - Enumerated: 19 public repositories in the current owner-scoped GitHub search.
  - High-value sources: social-media-skills, ai-second-brain, show-me, motion-graphics-skills, life-automation-skills, close, save-progress, codex-task-router, mod-maker, automation-audit, choose-and-compare-models.
  - Priority leverage: task-scoped skills, evidence-bound completion, persistent operating memory, deterministic routing, local safety/resource guards, visual proof, media generation and automation auditing.
  - Repository-level reuse requires comparison against existing agent-skills/ASTRA/COLLECTION before implementation.

- dyad-sh — https://github.com/dyad-sh
  - Primary source: dyad — https://github.com/dyad-sh/dyad
  - Account capture: COLLECTION/ACCOUNTS/DYAD-SH_2026-10-06.md
  - Revision inspected: 701d9179b43773a9c654014975ebc699a32fd500
  - Priority leverage: MCP consent/typed tool contracts, independent shell-review policy, read-only/plan-only capability enforcement, WAL-safe backup/checksums, fake-provider/MCP evaluation fixtures, provider-neutral model registry and deployment integration patterns.
  - License caution: repo root states Apache-2.0 outside src/pro; src/pro is Functional Source License 1.1 + Apache-2.0 terms. Reuse must respect the boundary.

- reticlehq — https://github.com/reticlehq
  - Primary source: reticle — https://github.com/reticlehq/reticle
  - Account/source capture: COLLECTION/ACCOUNTS/RETICLEHQ_RETICLE_2026-10-07.md
  - Skill extraction: COLLECTION/SKILLS/RETICLE_REUSABLE_VERIFICATION_PATTERNS_2026-10-07.md
  - Priority leverage: runtime proof, PASS/FAIL/UNKNOWN verdicts, look→act→observe→assert, first-divergence diagnosis, file:line repair signals, replayable regression flows, structured runtime evidence and local/MCP verification.
  - Reuse decision: extract/upgrade narrowly; do not import the whole project or duplicate existing SOAT/evidence infrastructure.

- Hikhakk — https://github.com/Hikhakk
  - Account capture: COLLECTION/ACCOUNTS/HIKHAKK_2026-10-06.md
  - Primary verified source: higgsfield-mcp-unified — https://github.com/Hikhakk/higgsfield-mcp-unified — MIT.
  - Priority leverage: provider adapters, MCP typed contracts, model registry/confidence, preflight validation, retry/backoff/jitter, circuit breaker, idempotency and structured provider errors.
  - Reuse decision: extract implementation patterns only; do not adopt the experimental private web-backend automation.
  - Skill extraction: COLLECTION/SKILLS/HIGGSFIELD_RELIABILITY_PATTERNS_2026-10-06.md

- tester-army — https://github.com/tester-army
  - Account-wide source added and enumerated: 7 public repositories.
  - Account capture: COLLECTION/ACCOUNTS/TESTER-ARMY_2026-10-07.md
  - P0 sources: e2e and scout.
  - P1 sources: cli, unbox-ai, mobile-github-action.
  - Priority leverage: agentic E2E action/assert/replay, authorization-safe API verification, mutation gates, request budgets, structured findings, coverage/CI evidence, Agent Skills/MCP integration, bounded AI trace/cost/tool analysis, and mobile CI automation.
  - Reuse decision: extract/upgrade narrowly after semantic dedupe; preserve source provenance; do not wholesale import TesterArmy.

- JCodesMore — https://github.com/JCodesMore
  - Account-wide capture: COLLECTION/ACCOUNTS/JCODEMORE_2026-10-07.md
  - 18 public repositories returned by owner-scoped search on 2026-10-07.
  - Highest-value current sources: ai-website-cloner-template, youtube-for-ai-agents, fix-claude-code, starry-ai-bookmark-search, slack-for-ai-agents, Powerful-Websites-You-Should-Know-About.
  - New extracted pattern: COLLECTION/SKILLS/WEBSITE_REVERSE_ENGINEERING_CLONE_2026-10-07.md — Map → Observe → Build → Compare with source/local matched-state evidence and production+rendered-comparison completion gate.
  - Reuse rule: semantic dedupe against browser/SOAT/agent-skills; no wholesale project import.
- APILayer — https://github.com/apilayer
  - Account-wide source added: COLLECTION/ACCOUNTS/APILAYER_2026-10-07.md
  - 72 public repositories returned by owner-scoped search on 2026-10-07.
  - High-value sources inspected: aerostack, ipwiz, privycheck, mail-wiz, collabfab, rent-scam-detector and global-rates.
  - Priority leverage: evidence-backed scoring, graceful degradation, quota-aware batching/deduplication, server-side credential isolation, multi-provider composition, honest comparison and cached fallback.
  - Reuse decision: retain account provenance; extract narrow patterns only after semantic dedupe against existing COLLECTION/SOAT/agent-skills/API Factory infrastructure.

- yihui-dev — https://github.com/yihui-dev
  - Account-wide source captured: COLLECTION/ACCOUNTS/YIHUI-DEV_2026-10-07.md
  - 16 public repositories returned by owner-scoped search on 2026-10-07.
  - Highest-value sources: yh-chatcut-skills (independent Agent Skills + staged media workflow), dify (self-hosted LLM app/workflow/RAG/agent platform; use upstream langgenius/dify as canonical), free-ai-tools-directory (discovery index requiring independent verification), awesome-opus5-5-videos and awesome-fable5-5-videos (prompt/video reference corpora), image (Nuxt image optimization).
  - Reuse rule: extract narrow contracts/patterns and upgrade existing Skills after semantic dedupe; do not wholesale import or treat directories/prompts as runtime proof.

## Latest high-leverage account captures
- agent-sandbox — https://github.com/agent-sandbox
  - Account-wide capture: COLLECTION/ACCOUNTS/AGENT-SANDBOX_2026-10-07.md
  - 2 public repositories enumerated.
  - Primary source: agent-sandbox (Apache-2.0).
  - Priority leverage: E2B-compatible self-hosted sandboxing, multi-tenant isolation, browser/computer/shell execution, pre-warmed pools, pause/resume, snapshots, scale-to-zero and lifecycle observability.
  - Extracted contract: COLLECTION/SKILLS/AGENT_SANDBOX_LIFECYCLE_CONTRACT_2026-10-07.md
  - Reuse rule: merge into existing OpenShell/CUA/AI Operating execution-boundary work; no wholesale import.
- the-open-agent — https://github.com/the-open-agent
  - Account-wide capture: COLLECTION/ACCOUNTS/THE-OPEN-AGENT_2026-10-07.md
  - 11 public repositories enumerated.
  - High-value sources: openagent, oss-skills, agentbench, office-tool-use.
  - Priority leverage: self-hosted agent runtime, progressive-disclosure maintainer Skills, reproducible agent benchmarking, and bounded PPTX/OOXML automation.
  - Reuse rule: semantic dedupe against agent-skills/SOAT/API Factory; upgrade existing contracts rather than duplicate systems.

## Additional account targets discovered
- sherlock-project — https://github.com/sherlock-project
  - Account-wide source discovered and enumerated: 5 public repositories.
  - Account capture: COLLECTION/ACCOUNTS/SHERLOCK-PROJECT_2026-10-04.md
  - High-value: sherlock (MIT username OSINT engine), sherlockproject.xyz, api, build.
  - Integration: optional username-discovery adapter in Salamou-31/API Factory; discovery is not identity verification.
- cporter202 — https://github.com/cporter202 — 24 public repositories discovered; high-value: API-mega-list, agentic-ai-apis, automate-for-growth, automate-faceless-content, job-data-apis-and-scrapers, ai-agent-tools.
- trycua — https://github.com/trycua — 45 public repositories discovered; high-value: cua, acu, e2e-test-agent, terraform-provider-fleets, cua-driver-fps-bench, gameworld-autoresearch, packer-plugin-lume.
- shobhitagnihotri69 — https://github.com/shobhitagnihotri69 — account target; high-value trail: mercor-grpo-agent, CUA contributions, hflow, graph extraction, LangGraph examples; full enumeration pending.
- proffesor-for-testing — https://github.com/proffesor-for-testing — account target via agentic-qe; high-value: verification/governance, browser QE, RVF memory, adversarial quality gates, skills; full enumeration pending.
- mizorewww — https://github.com/mizorewww — account target via laya-coreml; high-value: Apache-2.0 local Apple Core ML/Neural Engine typed decision inference; full enumeration pending.
- stablyai — https://github.com/stablyai — account target via Orca; high-value: MIT multi-agent orchestration, isolated Git worktrees, remote execution, browser/design, MCP/hooks/skills; full enumeration pending.

## Current research batch

### Web access / research
- Agent Reach — https://github.com/Panniantong/Agent-Reach
- SearXNG — https://github.com/searxng/searxng
- Jina Reader — https://github.com/jina-ai/reader

### Crawling / extraction
- Firecrawl — https://github.com/firecrawl/firecrawl
- Crawl4AI — https://github.com/unclecode/crawl4ai
- Scrapy — https://github.com/scrapy/scrapy

### Browser automation
- Playwright — https://github.com/microsoft/playwright
- Browser Use — https://github.com/browser-use/browser-use

### OSINT / identity discovery
- Sherlock — https://github.com/sherlock-project/sherlock
  - MIT; username discovery across 400+ social networks.
  - Use only as discovery evidence; results are not identity verification.
  - Integrated into Salamou-31/API Factory as a bounded local adapter.

### Documents / files
- Docling — https://github.com/docling-project/docling
- OCRmyPDF — https://github.com/ocrmypdf/OCRmyPDF

### AI memory / retrieval
- Qdrant — https://github.com/qdrant/qdrant

### Image / creative
- rembg — https://github.com/danielgatis/rembg
- Upscayl — https://github.com/upscayl/upscayl

### Audio / video
- whisper.cpp — https://github.com/ggml-org/whisper.cpp
- FFmpeg — https://github.com/FFmpeg/FFmpeg

- CodeCraft API — https://codecraftapi.com/
  - Source capture: COLLECTION/SOURCES/CODECRAFT_API_2026-10-07.md
  - Current official docs expose an OpenAI-compatible /v1 gateway, model capability/pricing metadata, streaming, tools, vision, reasoning and embeddings.
  - Current pricing page advertises a free tier of 1M tokens/month without a card; this remains source evidence, not runtime verification.
  - No official GitHub account/organization was identified from the accessible official site navigation; unrelated GitHub search matches were not treated as official.
  - Reuse boundary: benchmark against Salamou-31/API Factory and existing OmniRoute-derived provider policy; extract only narrow provider metadata/adapter patterns.

## Verified external ready projects
- `COLLECTION/VERIFIED_EXTERNAL/READY_EXTERNAL_PROJECTS_2026-10-05.md`
  - Verified external-only ready set: OpenHands, LiteLLM, Ollama, canonical diegosouzapw/OmniRoute.
  - Explicitly excludes user-owned projects and keeps discovery/verification separate from integration.
  - TossErp remains excluded from READY pending independent license/release verification.
- `COLLECTION/VERIFIED_EXTERNAL/CAPABILITY_MATRIX_2026-10-05.md`
  - Capability matrix and integration order for the verified external set.

- `COLLECTION/VERIFIED_EXTERNAL/REUSE_GAP_MATRIX_2026-10-05.md`
  - Live comparison of OpenHands/LiteLLM/Ollama/canonical OmniRoute against Salamou-31/API Factory, agent-skills/Elite, and ASTRA; rejects wholesale duplication and identifies OmniRoute provider-intelligence extraction as the only immediate gap.


- Juspay — https://github.com/juspay
  - Account capture: COLLECTION/ACCOUNTS/JUSPAY_2026-10-08.md
  - Payment infrastructure family captured from the current owner-scoped inventory: hyperswitch, hyperswitch-suite, hyperswitch-control-center, card-vault, encryption-service, prism, decision-engine, checkout SDKs, Helm/deployment tooling, WooCommerce/Saleor/Kill Bill integrations and client libraries.
  - Primary source: COLLECTION/SOURCES/JUSPAY_HYPERSWITCH_2026-10-08.md
  - Exact main revision inspected: 1d71d94d2e2e1c72f3ede13abebc24132997685f.
  - Priority leverage: payment routing/orchestration, connector abstraction, retries/revenue recovery, reconciliation, vault/encryption boundaries, cost observability and self-hosted payment infrastructure.
  - Reuse rule: Hyperswitch is distinct from existing Lago/Kill Bill billing candidates. Do not wholesale import or create duplicate Skills; extract only missing contracts after semantic dedupe.

## Collection rules
1. Discovery != production-ready without verification.
2. Preserve source URL, revision/version, license, setup method, dependencies and limitations.
3. Prefer local/self-hosted/free paths before paid APIs.
4. Separate free/open-source from free cloud tiers.
5. Do not copy credentials, secrets or private user data.
6. Preserve distinct source records/provenance even when they provide the same function; deduplicate and merge at the canonical Skill layer, not by deleting historical source evidence.
7. The Top Five rule selects five repositories each week by fresh star-growth evidence and permanently adds them to the collection queue.
8. Do not mark COMPLETE until the agreed source graph and requested repository/file sets are actually inspected and verified.
9. Every discovered repository expands to its owning account/organization; enumerate all public repositories and recursively add newly discovered accounts to the collection queue.

## Permanent account-wide expansion rule
ACCOUNT TARGET → ALL PUBLIC REPOSITORIES → ALL RELEVANT CONTENT/SOURCES → NEW ACCOUNTS → REPEAT

Daily collection must expand every discovered repository to its owning account/organization and inspect ALL public repositories of that owner, not only pinned, popular, or first-page repositories. Relevant docs, releases/tags/branches, workflows/actions, issues/PRs, and linked sources are inspected when useful. New repositories and accounts discovered from this graph enter the same collection queue; historical captures and provenance are preserved.

Full rule: COLLECTION/CONTROL/ACCOUNT_REPOSITORY_EXPANSION_RULE.md

## Current frontier
Continue weekly Top Five selection, free/self-hosted replacement discovery, account-wide collection, downstream account expansion, Agent Reach adapters/dependencies, OpenCut video/editor capabilities, Pablostanley design/agent/video tooling, debpalash voice/GTM/agent/video tooling, h-guo18 inference/model optimization, ARPAHLS agent/retrieval/privacy/security tooling, zeenie-ai OpenCompany/AgentEmpire/WhatsApp/Temporal, rohitg00 agent memory/workflow/skills/evidence tooling, and high-value verification under COLLECTION/VERIFICATION.

No completion claim is made. Collection remains active.

### xihongshichaojidan8 — 2026-10-04
- https://github.com/xihongshichaojidan8
- 5 public repositories captured in the current owner-scoped pass.
- Priority: AgentScope Java event/permission/middleware/distributed-agent patterns; DeerFlow super-agent harness, skills, memory, scheduling and sandbox patterns.
- Account record: COLLECTION/ACCOUNTS/XIHONGSHICHAOJIDAN8_2026-10-04.md


## Dark Web OSINT / Threat Intelligence — 2026-10-08
- Source capture: COLLECTION/SOURCES/DARKWEB_OSINT_TOOLS_2026-10-08.md
- Candidate Skill: COLLECTION/SKILLS/DARKWEB_OSINT_DEFENSIVE_COLLECTION_2026-10-08.md
- Primary sources captured: osintph/darkweb-observatory, osintph/threatintel-platform, Kirov-Dynamics-Technology/kirov-osint-intelligence, spideydotjs/gengar.
- Discovery indexes retained as leads: osintshifu/awesome-osint-repos and djbpm/osint-toolkit.
- Priority leverage: bounded Tor/onion collection, IOC extraction/normalization, entity/relationship correlation, evidence hashing/provenance, STIX/MISP/TAXII interoperability, monitoring/alerts/digests.
- Promotion status: candidate only; semantic dedupe and isolated runtime verification required before canonical Skill promotion.


## Internal runtime verification — API Factory — 2026-10-16
- Evidence record: `COLLECTION/VERIFICATION/API_FACTORY_VERCEL_SMOKE_2026-10-16.md`.
- Vercel health and readiness endpoints passed a rerun of the live-smoke workflow against the stable alias after a deployment adapter/storage fix.
- Scope is deliberately limited: health/readiness is verified; persistent registry storage, authenticated business routes, generated API execution and automatic Git deployment remain open gates.


## Account-wide expansion update — mnfst — 2026-10-16
- Enumerated 25 public repositories for the `mnfst` owner; page 2 of the owner-scoped repository search returned no additional repositories.
- Account record: `COLLECTION/ACCOUNTS/MNFST_ACCOUNT_WIDE_2026-10-16.md`.
- Highest-value non-duplicative candidates for API Factory: model parameter validation (`modelparams.dev`), model lifecycle/deprecation data (`modeldeprecations.dev`), and narrow request repair (`autofix`). No code has been imported; each still requires a controlled benchmark and privacy/terms review.
- `mcp-server-generator` is explicitly marked WIP/non-verified by its README; do not use it in production. The account-wide collection remains active and incomplete.


## Account-wide expansion update — diegosouzapw — 2026-10-16
- Re-enumerated 71 public repositories under `diegosouzapw`; page 2 returned no additional results. The account-completion register already records the owner as enumerated; this capture adds the current repository list and relevance triage without replacing historical records.
- Account record: `COLLECTION/ACCOUNTS/DIEGOSOUZAPW_ACCOUNT_WIDE_2026-10-16.md`.
- API Factory priorities: keep OmniRoute as provider-intelligence reference only; evaluate OpenSandbox for isolated generated-code execution; compare selected `awesome-omni-skills` against the existing agent-skills repository before reuse.
- Reject `openclaw-billing-proxy` as an integration candidate because it manipulates billing identifiers/OAuth tokens; treat `ag-local-bridge` as high-risk pending security/terms review. Empty repos remain unverified.


## API Factory persistence/export hardening — 2026-10-17
- Added a Supabase REST registry adapter and private Supabase Storage artifact adapter, with a dedicated migration and fail-closed tests. Durable mode remains inactive until a separate Salamou-31 Supabase project is approved/configured; do not reuse EASY's project.
- Added authenticated `GET /v1/factory/export/:name` to return a generated API bundle and explicit degraded storage checks in `/ready`.
- Evidence record: `COLLECTION/VERIFICATION/API_FACTORY_PERSISTENCE_EXPORT_2026-10-17.md`. Latest CI and deployment alias must be rechecked before marking this gate complete.


## Account-wide expansion — doobidoo — 2026-10-17
- Owner-scoped search enumerated 53 public repositories (page 2 empty); priority README/manifest/license triage completed for memory/MCP sources.
- Capture: `COLLECTION/ACCOUNTS/DOOBIDOO_ACCOUNT_WIDE_2026-10-17.md`.
- Highest-value memory candidate: `doobidoo/mcp-memory-service` (Apache-2.0; REST + MCP + OAuth, self-hosted) for ASTRA/AI Operating Memory comparison. `doobidoo/shodh-cloudflare` is an MIT Worker/D1/Vectorize option requiring existing Cloudflare access and official quota revalidation.
- `mcp-memory-service-rs` is not approved for commercial adoption: its README states PolyForm Noncommercial unless separately licensed.
- Downstream owner `varun29ankuS` added for recursive account-level enumeration; account remains deep-sweep open.


## Account-wide expansion — varun29ankuS — 2026-10-17
- Enumerated 27 public repositories (page 2 empty) from the downstream owner exposed by SHODH sources.
- Capture: `COLLECTION/ACCOUNTS/VARUN29ANKUS_ACCOUNT_WIDE_2026-10-17.md`.
- Highest-value candidate: `shodh-memory` (Apache-2.0, local-first persistent memory, MCP/HTTP); benchmark against ASTRA using synthetic data and verify security/backup/restore before adoption.
- `shodhRAG` is a distinct local RAG desktop app; `shodh-redb` is an embedded Rust DB and is not a direct Node.js storage replacement.
- Account remains deep-sweep open; no source code or service was deployed.


## API Factory evidence refresh — 2026-10-17
- API Factory Test run `38988302697` passed the full npm test suite on code commit `52600d2563172bd6400e87bc2a8d335b9075c24b` after fixing malformed escaped newlines in the test harness.
- Vercel deployment `dpl_GYsFPaaL2PjQiARhnakjRDfYjkeS` is `READY`; stable alias now points to it. Live smoke run `38988360990` passed health and the readiness/degraded-state contract.
- Latest documentation-only commit test run `38988360987` was still running at index refresh. Durable Supabase registry/artifact storage remains unconfigured; current runtime reports degraded state rather than pretending persistence exists.


## Account-wide expansion — open-free-llm-api — 2026-10-17
- Owner search returned one public repository; README and MIT license reviewed.
- Capture: `COLLECTION/ACCOUNTS/OPEN_FREE_LLM_API_ACCOUNT_WIDE_2026-10-17.md`.
- Its directory reports 508+ model/API entries across 30 providers and distinguishes permanent free tiers from renewable credits. Treat counts as maintainer-provided directory entries, not distinct providers or guaranteed capacity.
- Added as a second free-provider discovery source alongside `mnfst/awesome-free-llm-apis`; dedupe by canonical provider/model/base URL and require official terms before routing.


## Account-wide expansion — ollama — 2026-10-17
- Owner-scoped search enumerated 4 repositories (page 2 empty); README/LICENSE triage completed for runtime and SDKs.
- Capture: `COLLECTION/ACCOUNTS/OLLAMA_ACCOUNT_WIDE_2026-10-17.md`.
- Local Ollama is a no-per-request-cost inference candidate only if a reachable machine exists; no reachable Ollama host was verified. Cloud models are a separate access/billing class and are not presumed free.


## Free-provider eligibility hardening — 2026-10-17
- API Factory zero-cost routing now fails closed unless a provider-owned HTTPS source is explicitly attested, the hard-stop is true, access/status enums are valid, and the source audit is within 30 days. Community catalogue URLs cannot be the official source.
- Google Gemini live probe now requires an explicit `GOOGLE_AI_STUDIO_BILLING_TIER=free` preflight before any request; this does not replace checking the actual key/project billing state.
- Evidence and official Google billing/pricing URLs recorded in `COLLECTION/VERIFICATION/API_FACTORY_PERSISTENCE_EXPORT_2026-10-17.md`.


## Account frontier refresh — 2026-10-17
- Added account-level captures for `doobidoo` (53 repositories), `varun29ankuS` (27), `open-free-llm-api` (1), and `ollama` (4); `mnfst` and `diegosouzapw` were also refreshed.
- The owner frontier is now at least 138, not closed; enumeration does not equal deep-sweep completion.
- Updated master register: `COLLECTION/MASTER/ACCOUNT_COMPLETION_REGISTER_2026-10-06.md`.


## OpenShell source refresh — 2026-10-17
- Refreshed the existing `NVIDIA/OpenShell` capture against README revision `e0aaa43641b41a8e7cd4a2f8ffcb345a356e754b` and its Apache-2.0 license.
- OpenShell is a potential isolated generated-code runtime, not a hosting service. It requires a reachable Linux/macOS/WSL2 plus Docker/Podman/virtualization environment; no such gateway was verified or deployed here.
- Capture: `COLLECTION/ACCOUNTS/NVIDIA_OPENSHELL_2026-10-04.md` (refreshed 2026-10-17).


## API Factory provider-policy verification refresh — 2026-10-17
- Strict zero-cost provider policy test passed in API Factory Test run `38989110726`; the latest live smoke run `38989207054` passed health, readiness/degraded state, capabilities/export metadata, and unauthenticated export rejection.
- Latest deployment `dpl_4vmQMfn4hr5SahXSJxf1ruh8pbYs` is `READY` and owns the stable alias.
- A newer API Factory test run `38989207081` is rechecking the dynamic test-date change; do not treat it as finished until status completes.


## Account-wide expansion — unslothai — 2026-10-17
- Enumerated 13 public repositories (page 2 empty); triaged the local inference/training runtime and related model/SDK sources.
- Capture: `COLLECTION/ACCOUNTS/UNSLOTHAI_ACCOUNT_WIDE_2026-10-17.md`.
- `unsloth` is Apache-2.0 and supports local OpenAI-compatible API serving, but it is not hosted compute. `unsloth-zoo` and `notebooks` are LGPL-3.0; review redistribution obligations. Local hardware is not confirmed reachable.
- Deduplicate the `unslothai/llama.cpp` and `unslothai/gpt-oss` forks against `ggml-org/llama.cpp` and `openai/gpt-oss` upstreams.


## Owner count reconciliation — 2026-10-17
- Rechecked `debpalash` (35), `Wassimyounes01` (47), `cporter202` (41), `miqdadbadjuber` (10), and `mufeedvh` (43); page 2 was empty for all five searches.
- Updated existing account records with current repository inventories and added `COLLECTION/ACCOUNTS/MUFEEDVH_ACCOUNT_WIDE_2026-10-17.md`.
- The cporter202 baseline is now 41 (older sources said 34/24); mufeedvh is 43 (older source said 42). Historical discrepancies are retained rather than overwritten.


## Owner count refresh — senamakel and Cbrock84 — 2026-10-17
- `senamakel`: current owner-scoped search 94 (historical profile 71, previous search 89); account record refreshed with current inventory.
- `Cbrock84`: current owner-scoped search 72 (prior register 57); new account-wide inventory record created. Deep sweep remains open.


## Gist coverage spot-check — 2026-10-17
- Confirmed `aw-junaid` 76 public gists and `mufeedvh` 8 public gists via their public Gist pages; `cporter202` page fetch remained inaccessible.
- The historical 21-owner Gist enumeration failure count remains open; this spot-check does not falsely mark those failures resolved. Details are in `COLLECTION/MASTER/DAILY-DIGEST-2026-10-09.md` and the account completion register.


## Connected application and account frontier audit — 2026-10-19
- Full read-only audit: [CONNECTED_APP_FRONTIER_AUDIT_2026-10-19.md](VERIFICATION/CONNECTED_APP_FRONTIER_AUDIT_2026-10-19.md), commit `Project-@f2fc1a3519629d1ad00ab5050679b91243e150dc`.
- GitHub connector currently exposes one authenticated account (`salamou1944`), no organization memberships, and 10 repositories. The account-wide external frontier remains a separate Collection queue.
- Railway exposes two projects. The API Factory service `salamou31-api-factory` has no direct service variable names and its five latest listed deployment records are removed; production deployment is not proven. EASY's service is separate and untouched.
- Supabase exposes only `easy-platform-db` (ACTIVE_HEALTHY); do not reuse it for API Factory. Termalin exposes zero reachable hosts; Vercel deployment context exposes no teams; the GitLab project is empty.
- AgentMail API Pilot/EASY visible threads show delivery failures/bounces, not customer replies. No reply, acceptance, payment, commission, or revenue evidence was found. Fix deliverability and verify active contacts before any new outreach.
- Shopify's connected Algeria store is on a trial plan; it is not a verified live sales channel. Wix returned zero sites; Canva search returned zero matches; Notion search returned no matches (not proof of an empty workspace); Figma seat is View-only with Code Layers disabled.
- Collection extraction automation and current JSON audit are now linked to the frontier update trigger. Current run: [39180002514](https://github.com/salamou1944/Project-/actions/runs/39180002514), pending at last observation.
- API Factory local SOAT run [39179590053](https://github.com/salamou1944/Salamou-31/actions/runs/39179590053): dedicated real local Ollama completion step passed, while the official smoke suite and evidence persistence remained in progress/pending. No overall success claim yet.


## Free-provider source security gate — 2026-10-19
- A critical historical workflow was found in `mnfst/awesome-free-llm-apis`: commit `48fcbe86582e16b7b746fee52e5512a891a8db76` added a push/manual workflow that searched the checkout and Git history for credential patterns and POSTed matches/context to hard-coded external HTTP endpoint `193.32.204.199:8080`.
- The workflow was removed in `cf97c32fec1b2e96e9936746e2731a81bd5ea33f`. Current workflow listing contains only the README generator. No “Security Audit” run appeared in the latest 30 visible Actions runs; actual execution remains unverified.
- Decision: preserve the catalogue as discovery evidence, but never execute its historical workflow/scripts or expose credentials to it. Verify providers independently from official sources. Account capture and detail: [MNFST account-wide capture](ACCOUNTS/MNFST_ACCOUNT_WIDE_2026-10-16.md).


## API Factory local SOAT runtime proof — 2026-10-19
- Fresh SOAT Runtime Integration Smoke run [39179590053](https://github.com/salamou1944/Salamou-31/actions/runs/39179590053) completed **success** on source commit `Salamou-31@bada4b0feede31853b4afd246deb0b514a5e1ed0`.
- The dedicated real completion path through API Factory → pinned SOAT → local Ollama passed, as did the official SOAT smoke suite (`status=passed`, exit code 0, not timed out, 296089 ms). Execution-contract validation, evidence consumption, and business-outcome gate passed; the outcome was `ENTRY_POINT_VERIFIED`.
- Uploaded artifact `soat-verification-39179590053` (artifact ID `12155088912`, SHA-256 `4b7a721294b6e53086e2e89a65c71231906029487383ceeb6ce3dd79b7f0faf5`) contains the verification record/evidence and expires 2027-01-17.
- Permanent evidence record: [API_FACTORY_SOAT_LOCAL_RUNTIME_2026-10-19.md](VERIFICATION/API_FACTORY_SOAT_LOCAL_RUNTIME_2026-10-19.md), commit `Project-@4d871be4d16af72105699b97077e3cdfe41870e1`.
- Boundary remains strict: evidence scope is `ci-pinned-local-runtime`; record explicitly says `production_status=not_proven`. This is not proof of a reachable user-hosted Ollama server, a production Railway deployment, durable registry/artifact storage, or a hosted provider's zero-cost terms.
- Collection automation commits: frontier-triggered workflow `Project-@91881560d9a6abf7ac1a3df57a524beeb192e05a`; current-main JSON inventory audit script `Project-@b36a1fc3aee466c9b4a7e9a83eb25cc4b94b0226`; JSON diff audit workflow `Project-@ecffc50fe490de89b63e3dfba87efe72f52ea6af`; manual audit now defaults to the current commit `Project-@600adc8e998a75c57bf75732c9a991c7e8719e51`; frontier trigger narrowed to recursive frontier changes `Project-@1ce70edb065526beeee2bb48aee58de887a26c06`.
- Full Collection extraction run `39179989521` remains in progress at last check. Run `39180002514` was cancelled; run `39180283329` is queued/pending after the later account capture update. Wait for the active extraction's manifest and audit report before marking Collection complete.


## Full account frontier materialized for deep extraction — 2026-10-19
- The master account-completion register's 40 enumerated accounts plus 116 newly exposed owner names were parsed and normalized case-insensitively to **151 distinct owner targets**.
- Those 151 GitHub owner URLs are now committed into the Markdown input graph used by `COLLECTION/AUTO/deep_extract.py`; the existing eight Layer A and eleven observed Layer B targets remain in the same companion. Commit: `Project-@0d5c7a50ddfc503de0ac39ba12b42683ebe82f14`.
- Owner scanner now deduplicates case-insensitively: `Project-@4a5011bd27c8ce3558e298b99f2669b07d875b51`. Workflow concurrency was adjusted to prefer the newest frontier: `Project-@dc8ffb98b59d0e51313749917310048b5d33f2e4`.
- Current full-frontier extraction run: [39180598182](https://github.com/salamou1944/Project-/actions/runs/39180598182), pending at last observation. Earlier runs were triggered before all 151 targets were materialized; do not use them to claim complete frontier extraction.
- After this full-frontier run completes, trigger the full Collection workflow using the safe incremental marker so it checks out the extracted frontier and then runs the existing large-JSON audit, policy tests, value queue, bounded installation and verification gates.


## OmniRoute provider-intelligence refresh — 2026-10-19
- Revisited the exact `diegosouzapw/OmniRoute` release branch and source docs. Current README: 375 providers, 468 free-tier entries, 34 recurring pools, ~1.62B estimated tokens/month. Older account capture said 372 / 485 / 35; this drift is now recorded rather than silently merged.
- `FREE_TIERS.md` has `version 3.8.50` and a 2026-10-18 update date, but its full research note remains 2026-06-17 with partial re-audit 2026-09-02 and selected checks 2026-10-08. Treat provider budgets as discovery evidence, not verified free capacity.
- MIT license, but full repository is ~1.76 GB. Keep it on the shelf; reuse provider-intelligence schema/pool-deduplication only. `.env.example` requires strong `JWT_SECRET` and `API_KEY_SECRET`; never use `INITIAL_PASSWORD=CHANGEME`; SQLite requires durable volume. Browser/web-cookie/OAuth paths need separate security/terms review.
- Updated canonical capture: [OMNIROUTE_PROVIDER_INTELLIGENCE_2026-10-05.md](VERIFIED_EXTERNAL/OMNIROUTE_PROVIDER_INTELLIGENCE_2026-10-05.md); upstream account capture: [DIEGOSOUZAPW_ACCOUNT_WIDE_2026-10-16.md](ACCOUNTS/DIEGOSOUZAPW_ACCOUNT_WIDE_2026-10-16.md).


## Owner-link parser correction — 2026-10-19
- The owner scanner now recognizes GitHub URLs inside Markdown links and strips trailing punctuation, in addition to case-insensitive owner deduplication. Commit: `Project-@79604426ec98243c0bcef7c5e7c4ecf49a2599e5`.
- Run `39180598182` was triggered before this parser correction and is not the final parser-evidence run. The next queued run [39180853004](https://github.com/salamou1944/Project-/actions/runs/39180853004) has the corrected scanner and the 151-owner frontier in its checkout; use its final manifest and JSON audit report as the definitive extraction evidence.


## PR #45 merged-state reconciliation — 2026-10-19

- GitHub API confirms [Salamou-31 PR #45](https://github.com/salamou1944/Salamou-31/pull/45), “feat(api-factory): add deployable Railway container,” is **merged** at `2026-10-17T18:12:09Z`, merge commit `172328b929513d4a5909a22da4954cd988aa2343`. The PR body still contains a stale line saying it remains open/unmerged; API merge metadata is authoritative.
- PR body records Vercel deployment `dpl_4vmQMfn4hr5SahXSJxf1ruh8pbYs` as READY at the time of the merge, plus a stable alias. The 2026-10-19 connected Vercel context returned no teams, and project/environment management was previously blocked by connector scope. Therefore the historical deployment record is preserved, but current alias resolution and deployability are not independently re-proven in this sweep.
- Current Railway inventory shows service `salamou31-api-factory` sourced from branch `feat/api-factory-railway-deployable-2026-10-16`, root `AI-API-HUB/api-factory`, Dockerfile build, health path `/health`, and domain `salamou31-api-factory-production.up.railway.app`. However its direct service variable-name list is empty and its five latest listed deployment records are removed. The existence of a domain/configuration is not evidence of a live deployment.
- Durable registry/storage adapters and migration exist in code, but the only visible Supabase project is EASY's `easy-platform-db`; it remains intentionally excluded. A separate Salamou-31 database/storage project, variables, migration, and cross-invocation persistence test are still required.
- Latest API Factory evidence is the successful CI-pinned local SOAT/Ollama run [39179590053](https://github.com/salamou1944/Salamou-31/actions/runs/39179590053), documented in [API_FACTORY_SOAT_LOCAL_RUNTIME_2026-10-19.md](VERIFICATION/API_FACTORY_SOAT_LOCAL_RUNTIME_2026-10-19.md). It does not close production deployment/storage gates.


## MNFST provider catalog freshness — 2026-10-19
- Latest visible provider/model data refresh: `41197cb7d053680daf808d6618142045e961caaa` (2026-10-05), with data-sync merge `b25c0395fe1e7628ecc99bf119a40365801c6fb4`. No newer provider/model refresh appeared in the latest 10 commits.
- Newer history consists of the credential-exfiltration workflow addition/removal (Oct 10–11). Current workflows show only a README generator triggered by `data.json` changes; no current nightly provider-sync workflow was found. Treat the advertised refresh cadence as unverified.
- The Oct 5 refresh includes both live/deprecation findings and explicitly unprobed or human-review entries; preserve those evidence classes. No provider has been promoted to production or marked zero-cost from this source alone.


## Persisted current-main JSON audit gate — 2026-10-19
- Added `COLLECTION/AUTO/validate_current_collection_json_audit.py` (commit `Project-@80a2c9815f248bfe328d628c164d48491bacad1f`) to validate report schema, row counts, total bytes, SHA-256 format and parse-failure counts.
- Updated deep extraction to write the audit report even when JSON parse failures are found, commit it, and then fail the final gate after persistence: `Project-@0eacd07b4ac4fbe82541f647bc3d666f6fb4d694`.
- Updated the full Collection workflow to run the all-JSON inventory after state generation/installation and before commit, then validate the persisted report after commit: `Project-@42dca1510a4295bf993c41d356ee7a3edd773b6b`, ordering fix `Project-@b100aa7fd22306bb83f03a65d4d985a69fdbcd2a`, and conflict-recovery audit fix `Project-@e971fed597e052cb02acd7ec41255b2977577469`.
- The full-frontier extraction run [39180853004](https://github.com/salamou1944/Project-/actions/runs/39180853004) remains the run to evaluate for the corrected owner parser. Full Collection has not been triggered yet; wait for that run's extraction commit first.


## Browser Skill validation boundary — 2026-10-19
- Canonical `skills/browser-runtime-verification/SKILL.md` was strengthened at `agent-skills@84b4732094d543410a9284ab687405b37fea8e4f`; no duplicate Skill was created.
- GitHub reports zero check runs for that commit. The sole status context is a Railway watcher saying “No deployment needed - watched paths not modified.” That is not a Skill test pass or browser-runtime verification. The content change is preserved; runtime/domain-redirect/session safety remains unverified until a dedicated browser test executes.


## Owner parser regression test — passed
- Run [39181282587](https://github.com/salamou1944/Project-/actions/runs/39181282587) completed success after wiring `test_deep_extract_owner_parser.py` into `collection-install-selection-test`.
- The test covers raw owner URLs, Markdown link closers, repository paths, trailing punctuation, mixed-case duplicates, and excluded `salamou1944`/reserved paths. This validates the parser fix, not the full account extraction run.


## Bounded, metadata-complete deep extraction — 2026-10-19
- Reworked `COLLECTION/AUTO/deep_extract.py` so the full owner sweep preserves metadata for every discovered repository in `REPO-INVENTORY.json` and queues all deferred/blocked/archived repositories in `DEFERRED-REPOSITORY-QUEUE.json`.
- To avoid an unbounded source dump and GitHub Actions/API exhaustion, each run deep-extracts at most 200 high-priority repositories, no more than two per owner, with 24 files/repo, 50 KB/file and 300 KB source bytes/repo. All other active repo identities remain preserved and deferred, not discarded.
- File-byte budgets now keep deterministic relevance order instead of whichever parallel fetch finishes first.
- Commit: `Project-@76f9944042481a0a8d1e4cb332a46326e078f288`.
- New bounded run [39181614341](https://github.com/salamou1944/Project-/actions/runs/39181614341) is queued; older run `39180853004` is using the pre-budget strategy and is superseded.


## Bounded extractor verification — run active
- The unbounded pre-budget run `39180853004` was cancelled before commit.
- The bounded inventory-first run [39181614341](https://github.com/salamou1944/Project-/actions/runs/39181614341) is running against `76f9944042481a0a8d1e4cb332a46326e078f288`.
- Regression/compile run [39181614379](https://github.com/salamou1944/Project-/actions/runs/39181614379) passed. This validates the parser/bounded code compiles, not the actual owner inventory/extraction result.


## Safe incremental Collection trigger status
- The marker `.github/COLLECTION_SAFE_INCREMENTAL_ONCE` already exists from 2026-10-16. Do not create a duplicate file; update its content only after bounded extraction commits, so the full Collection workflow checks out the new inventory and source packets.


## Upwork and Apollo revenue readiness
- Read-only findings: [UPWORK_REVENUE_READINESS_2026-10-19.md](VERIFICATION/UPWORK_REVENUE_READINESS_2026-10-19.md).
- Upwork has zero Connects, no proposals/contracts/invitations, a private low-quality profile, no portfolio, and zero completed jobs/reviews. The inspected active AI-automation job requires 14 Connects and the client has no hiring history. No application or purchase was made.
- Apollo shows 80 lead credits and 5,000 AI credits remaining with zero used; direct-dial counters are inconsistent, so do not treat them as spendable capacity. No enrichment/search was run.


## Storage baseline for bounded extraction
- `Project-` repository size before the new bounded batch: 317,118 KB (~310 MiB) per GitHub repository metadata. Recheck after run `39181614341`; no post-run size is claimed yet.


## HubSpot pipeline status — 2026-10-19
- Read-only CRM inventory: 0 deals, 2 sample contacts, 1 company record. No writes.
- Records: [Brian Halligan (Sample Contact)](https://app.hubspot.com/contacts/149568666/record/0-1/894044249312?utm_source=app_12360546_mcp&utm_medium=ai_agent&utm_campaign=search), [Maria Johnson (Sample Contact)](https://app.hubspot.com/contacts/149568666/record/0-1/894054999231?utm_source=app_12360546_mcp&utm_medium=ai_agent&utm_campaign=search), [HubSpot / hubspot.com](https://app.hubspot.com/contacts/149568666/record/0-2/453775516896?utm_source=app_12360546_mcp&utm_medium=ai_agent&utm_campaign=search).
- Treat as seed/demo records, not a real sales pipeline, until independently verified.


## Installed asset shelf check
- Current `COLLECTION/INSTALLED/` contains only `juspay__hyperswitch`; no browser/sandbox candidate is installed.
- Hyperswitch remains source-only, not runtime-promoted. New installations require explicit approval and both integration/security gates.


## Legacy Hyperswitch storage note
- `juspay/hyperswitch@1d71d94d2e2e1c72f3ede13abebc24132997685f` is preserved as vendored source only; its marker reports 393 MB. GitHub API reports the containing repository at 317,118 KB before the new batch; these metrics are not directly comparable. Do not delete without an explicit backup/retention decision.


## Connected-app sweep — 2026-10-19
- Updated [CONNECTED_APP_FRONTIER_AUDIT_2026-10-19.md](VERIFICATION/CONNECTED_APP_FRONTIER_AUDIT_2026-10-19.md) with read-only inventory across GitHub, Railway, Supabase, Vercel, GitLab, Replit, Notion, Canva, Wix, Render, HubSpot, AgentMail, Apollo and Upwork.
- GitHub exposes 10 first-party repositories, separate from the 199 external owner targets. Railway latest status reports five services with failed latest deployments; API Factory Railway source uses a feature branch and no service variables. Vercel has a READY production-target deployment but from the same feature branch while project metadata says `live:false`. Supabase EASY database is healthy but must not be reused for other projects.
- Other connected app findings and safe boundaries are recorded in the audit file. No secrets were read, no deployment or environment mutation was made, and no paid credits were spent.


## First-party asset triage — 2026-10-19
- Preserved first-party source manifests and state boundaries in [connected-app audit](VERIFICATION/CONNECTED_APP_FRONTIER_AUDIT_2026-10-19.md): `Files-/collection/mufeedvh` inventory of 43 repos (content/history/Gists incomplete); `Astra-/collection/aw-junaid` inventory of 33 repos (content verification required); separate `Astra/collection` lanes; EASY API discovery bank and 10 pilot hypotheses; existing revenue service pack; canonical operating memory; ASTRA research gates failing/live OFF.
- No duplicate Skill was created and no source assets were promoted/installed. Continue per-repo license/security checks and semantic dedupe before promotion.


## Extraction audit resolution — 2026-10-19
- JSONC compatibility fix preserved the third-party devcontainer source unchanged; the current-main audit passed at [run 39185928703](https://github.com/salamou1944/Project-/actions/runs/39185928703): 10,877 files, zero parse failures, 595,154,410 bytes.
- Regression suite [39185928757](https://github.com/salamou1944/Project-/actions/runs/39185928757) passed.
- Corrected counts: 200 selected, 199 successful source packets, 1 blocked; 31,343 repo identities, 8,800 archived metadata-only, 22,344 deferred/blocked, 7,220 dedupe-ready records.
- The safe-incremental Collection harvest is the next execution step. Do not treat audit success as canonical promotion or production readiness.


## Full safe-incremental harvest — passed 2026-10-19
- Workflow [39186272221](https://github.com/salamou1944/Project-/actions/runs/39186272221) passed all steps and persisted generated state at `Project-@0cf97579f587c06a0a51bcf2fad1ae5e09fadb66`.
- Current-main audit: 10,975 JSON/JSONC files, zero parse failures, 626,208,456 raw bytes. The run refreshed 99 of 100 selected repos; one source was blocked. It preserved 31,343 repo metadata rows, 2,985 extracted source records, 2,396 cached records, 490 prior sources not selected and 20,048 deferred repos.
- Resulting state: 24,535 capability groups, 17,298 promotion-review items, 7,237 restricted items. Runtime-readiness claims = 0, explicit declarations = 0, install result `NO_APPROVED_CANDIDATES`, installed = 0. All evidence is preserved on shelf; no unapproved asset was installed.
- Canonical OmniRoute source record refreshed at `Project-@0bb911fd2359e6d0017fde44827a2a4a1d029666`. Upstream is MIT and actively maintained, but free-tier totals are third-party account estimates, not guaranteed capacity; provider terms are stale/partially audited. Existing API Factory adopts schema/rules only, not OmniRoute runtime.
- API Factory's successful local SOAT proof is now recorded at `Salamou-31@f2e0b8c73979189555a8583361a5f8d547766033` in `AI-API-HUB/api-factory/SOAT-RUNTIME-VERIFIED-2026-10-19.md`. CI local-Ollama proof is not production proof.


## New-source-first extraction follow-up — 2026-10-19
- The bounded incremental selector now ranks `NEW` repositories ahead of `NEEDS_REFRESH` cached sources in normal mode; explicit force-refresh mode retains its separate stale-cache rotation. Code commit: `Project-@9c3d8e0263eaba904aaabc890dc01138e41d18ba`; regression commit: `Project-@97bafc7f5b36685ac2be7531bceee808cc920f78`; test run [39186643182](https://github.com/salamou1944/Project-/actions/runs/39186643182) passed.
- Batch run [39186698910](https://github.com/salamou1944/Project-/actions/runs/39186698910) passed and added 98 source records from 100 selected repositories, preserving 2 blocked sources. Total extracted source records: 3,083; inventory remains 31,343 repository identities.
- Updated JSON/JSONC audit: 11,073 files, zero parse failures, 649,132,457 raw bytes. Generated-state commit: `Project-@4ec33a90e736ba961e470f7441e61cc45350415e`.
- Next bounded batch [39186862522](https://github.com/salamou1944/Project-/actions/runs/39186862522) is queued from marker commit `1361748647284429f234734cfaa0a6fa6ac2daee`. No assets were installed; the readiness gate continues to report no approved candidates.


## Second bounded new-source batch — 2026-10-19
- [Run 39186862522](https://github.com/salamou1944/Project-/actions/runs/39186862522) passed. It added 98 source records from 100 selected repos; two blocked sources remain explicitly recorded. Total source records: 3,181.
- Current-main audit: 11,171 JSON/JSONC files, zero parse failures, 668,043,719 raw bytes. Generated-state commit: `Project-@60502ad15f35d970a267a8d0c3c23fc15bd18301`.
- Capability output: 27,056 groups, 18,774 promotion-review items, 8,282 restricted items. Install gate remains `NO_APPROVED_CANDIDATES`; no runtime-readiness claims.
- Fourth bounded batch [39187362819](https://github.com/salamou1944/Project-/actions/runs/39187362819) is queued from marker commit `32592180403bfe1a75115c3723ba27f71c1ebbb1`.


## High-value bounded source packets — 2026-10-19
- The recent bounded source batch preserved `microsoft/mcp-gateway`, `BerriAI/liteagents`, `OpenAI/openai-agents-js`, `PostHog/pi-posthog-llm-gateway`, `cloudflare/mcp`, `MariaDB/mcp`, `SigNoz/signoz-mcp-server`, `n8n-io/n8n-docs`, `stripe/openapi`, `ollama/ollama-python`, `openclaw/mcporter`, `Infisical/ai-skills`, `vercel-labs/skills`, browser harness candidates, `opensandbox-group/fast-sandbox`, and `cisco-ai-defense/defenseclaw`.
- These remain source-only. PostHog's gateway bills through PostHog, so it is not eligible for zero-cost routing; Microsoft/BerriAI authorization tests are useful references for the existing API Factory boundary; no duplicate Skill or gateway was created.


## Third new-source batch — 2026-10-19
- [Run 39187054275](https://github.com/salamou1944/Project-/actions/runs/39187054275) passed. It added 98 source records from 100 selected repositories and preserved 2 blocked sources. Total extracted source records: 3,279.
- Current JSON/JSONC audit: 11,269 files, zero parse failures, 687,515,190 raw bytes. Generated-state commit: `Project-@749649b9b35b0104328cf2dafafd4db40e38fc00`.
- Capability output: 28,195 groups, 19,440 promotion-review items, 8,755 restricted items. No asset was auto-installed or promoted to runtime readiness.
- High-value source packets include `apache/casbin-mcp-gateway`, `cisco-ai-defense/litellm`, `agentclientprotocol/codex-acp`, `n8n-io/self-hosted-ai-starter-kit`, `openai/openai-cua-sample-app`, `pietrozullo/browser-use`, `browser-use/benchmark`, `Infisical/agent-vault`, `openbao/openbao-plugins`, `ollama/ollama-js`, `anomalyco/opencode`, and `vercel-labs/coding-agent-template`. These remain source-only pending security/license/dedupe review.
- Fourth bounded batch [39187362819](https://github.com/salamou1944/Project-/actions/runs/39187362819) is queued from marker commit `e3c161936e1796cb5140acde439718bd3b653e0e`.


## Verified update — 2026-10-21 02:30 UTC (cycle 18)
- [Cycle 18](https://github.com/salamou1944/Project-/actions/runs/39533389021) completed successfully. It selected 100 repositories, refreshed 79, preserved 21 blocked attempts, and left 18,551 repositories deferred. The manifest contains 5,050 source rows and 5,029 extracted artifacts.
- The current-main JSON audit passed: 13,021 JSON/JSONC files, zero parse failures, 916,967,626 bytes. The persisted audit validator passed.
- Capability/readiness groups: 45,415; promotion review items: 31,108; restricted items: 14,307. Historical evidence reconciliation passed with zero unrecoverable prior evidence records.
- Install gate returned `NO_APPROVED_CANDIDATES`: zero assets installed and zero ready for verification. This is a safe no-op, not a completed installation.
- Generated files remain large: `READY.json` 79,542,593 bytes and `CANONICAL-PROMOTION-PLAN.json` 53,727,383 bytes; both exceed GitHub's recommended 50 MB size. The JSON validity and size-budget guards passed, but file-size optimization remains open.
