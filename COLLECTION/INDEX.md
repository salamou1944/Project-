# COLLECTION — Research Index

Status: INCREMENTAL_COLLECTION
Updated: 2026-10-19


## 2026-10-19 operating update
- Recursive frontier Layer A snapshot committed: `COLLECTION/ACCOUNTS/RECURSIVE_ACCOUNT_FRONTIER_LAYER_A_2026-10-18.json`, commit `ff4af71f9e5fab97c059321835aaf3d696c8ed34`. It records 220 repository identities across 8 owner-scoped searches; it is a metadata snapshot, not full source extraction.
- Additional owner searches (jackwener, stickerdaniel, daytonaio, e2b-dev, ChromeDevTools, agentclientprotocol, jina-ai, nicobailon, kurtmckee, xpzouying, vercel-labs) remain partly unpersisted. The five 100-result pages need pagination. Do not count them as a committed complete inventory.
- Browser runtime verification Skill strengthened with redirect/domain-filter failure semantics, explicit logged-in-session authorization, recording-off defaults, protected harness boundaries, and redacted reproducible evidence. Commit: `agent-skills@84b4732094d543410a9284ab687405b37fea8e4f`. No post-change CI/runtime run is yet claimed.
- SOAT runtime smoke workflow fixture corrected at `Salamou-31@bada4b0feede31853b4afd246deb0b514a5e1ed0`. The fixture is explicitly local-only and synthetic; this does not attest a hosted provider's free quota or billing terms. Await fresh workflow evidence.
- The large-JSON audit utility's unit-test CI passed historically in run `39002889620`; a fresh full-data audit of current generated JSON remains unproven.
- Runtime/deployment gates remain strict: health alone is not readiness; API Factory needs durable registry and artifact storage, and no current stable production deployment has been proven.

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
