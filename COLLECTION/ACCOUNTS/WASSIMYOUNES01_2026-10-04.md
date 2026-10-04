# Wassimyounes01 — account collection

Source: https://github.com/Wassimyounes01
Captured: 2026-10-04

## Account status
- GitHub profile currently reports 21 public repositories.
- This account was discovered through the verified repository qwen38-uncensored.
- Full 21-repository enumeration is pending; this is not marked exhausted until every public repository is inventoried and relevant sources are inspected.

## Primary verified repository
### qwen38-uncensored
https://github.com/Wassimyounes01/qwen38-uncensored
- Public, JavaScript, 8 commits at inspection; 0 open issues.
- Current repository metadata observed: 292 stars, 37 forks.
- Purpose: local Qwen 3.8 27B uncensored/abliterated serving harness.
- Cross-platform paths: Ollama on macOS/Windows; optional MLX path for Apple Silicon.
- Default quantization: Q3_K_M for the documented 48GB M5 Pro profile and Q4_K_M for documented Windows 24GB GPU profile; additional quants are supported.
- bin/install.cjs performs platform detection, quant selection, model acquisition, Modelfile generation, and Ollama model creation.
- lib/profile.cjs contains the harvested model profile, model-source metadata, system block, and Modelfile generator.
- Package has zero runtime dependencies and includes npm test / npm run check paths.
- License boundary: repository scripts/harness MIT; Qwen weights identified as Apache-2.0; model bytes are not redistributed by the repository.
- Research value: a concrete local-model provider path that can reduce dependence on paid hosted inference, especially for development/evaluation workloads where suitable local hardware exists.

## High-value adjacent repositories surfaced from the account
- cortex — self-supervising learning/preflight/re-optimization layer; health-gated improvement claims should be verified at repository level.
- event-driven-autonomous-loop — starter for waking a coding agent after task completion; relevant to autonomous execution-loop research.
- apify-replacement — self-hosted/free scraper replacement concept; relevant to reducing SaaS extraction costs.
- ai-video-studio-kit — AI-assisted short-form video production; relevant to the user's media pipeline.
- flywheel — dependency-free reinforcement-learning-style task strategy selector; implementation and evidence require repository inspection.
- agent-workbench — MIT starter for bounded multi-agent task routing with evidence before acceptance; README-level inspection confirms candidate/review separation and dependency-aware local runtime.
- agent-patterns-cookbook — MIT prompt-pattern collection covering chaining, routing, parallelization, reflection, tool use, planning, multi-agent, memory, MCP, monitoring, recovery, HITL, RAG, evaluation and prioritization.
- genesis-plan-graph — explicit dependency-ready work scheduling; surfaced through GitHub topic search and requires repository-level inspection.

## Collection priorities
1. Inspect all 21 public repositories and preserve provenance.
2. Prioritize local inference, autonomous loops, self-hosted replacements, agent orchestration/evidence, video/media tooling, and any zero-cost infrastructure.
3. Compare against existing agent-skills, Salamou-31/API Factory, ASTRA, COLLECTION, and current revenue infrastructure before adopting anything.
4. Do not duplicate an existing capability without measurable leverage.
5. Treat uncensored/local models as research or controlled infrastructure; any public-facing deployment needs an appropriate moderation/safety layer.

## Verification notes
- Repository README claims are recorded as claims, not independently reproduced model-performance benchmarks.
- The repository README states 30–50% faster MLX inference on Apple Silicon; this is an upstream claim and should not be treated as a measured result in our environment.
- The README describes the model as weight-level abliterated and references Arditi et al. (2024); this is provenance information, not independent verification of refusal-rate or capability benchmarks.

## Corrected account enumeration

The initial profile-level count of 21 is stale/incomplete. Owner-scoped GitHub repository search on 2026-10-04 returned 47 public repositories. The account is not exhausted.

### Complete repository inventory
1. qwen38-uncensored
2. cortex
3. event-driven-autonomous-loop
4. ai-video-studio-kit
5. apify-replacement
6. agent-os
7. sentience-loop
8. telegram-command-bridge
9. flywheel
10. genesis-task-context
11. genesis-repo-atlas
12. dual-uncensored
13. genesis-prompt-kit
14. genesis-evidence-collector
15. genesis-change-impact
16. genesis-verified-reuse
17. genesis-regression-memory
18. genesis-batch-drafts
19. genesis-constraint-compiler
20. genesis-context-graph
21. genesis-worker-router
22. genesis-charter-lab
23. genesis-night-research
24. whatsapp-command-channel
25. genesis-task-adaptation
26. cursor-uncensored
27. genesis-task-ledger
28. genesis-source-packets
29. genesis-suite
30. genesis-routing-metrics
31. genesis-paired-experiments
32. genesis-release-integrity
33. genesis-review-gate
34. prompt-engineer
35. genesis-plan-graph
36. output-speed
37. context-budget
38. agent-pipeline
39. memory
40. fusion
41. bugbot
42. autonomous-loop
43. llm-split
44. myriad
45. megacycle
46. agent-patterns-cookbook
47. agent-workbench

### High-value findings
- agent-os: self-hostable kernel concept with capability-seat routing by task kind, cycles, JSONL-backed memory/ledger/state and per-kind token budgets.
- sentience-loop: prediction, maturation, scoring against observed outcomes, surprise, reflection and append-only audit; useful as a calibration/evidence pattern.
- event-driven-autonomous-loop: durable queue, completion-event wake and stop-hook continuation; strong fit for long-running execution.
- genesis-task-context + genesis-source-packets: bounded context/source packets with explicit evidence and gaps.
- genesis-repo-atlas: bounded, symlink-aware repository metadata census.
- genesis-prompt-kit: explicit acceptance criteria and stopping rules before dispatch.
- genesis-evidence-collector: aggregates tests, artifacts and review into structured completion evidence.
- genesis-change-impact: reverse dependency analysis after edits.
- genesis-verified-reuse: fingerprinted reuse without inheriting approval.
- genesis-regression-memory: durable regression records and reopening stale resolutions.
- genesis-constraint-compiler: turns declared effects into concrete review checks; advisory, not execution authority.
- genesis-context-graph: provenance, freshness and approval-aware reusable context.
- genesis-worker-router: bounded provider routing with deadline, attempt, concurrency, account-cap and output controls.
- genesis-task-adaptation: durable plan-bound revisions and recheck requirements.
- genesis-task-ledger: immutable task contracts, current artifact hashes, reviewer receipt and deduplicated credit.
- genesis-suite: bundles 21 bounded workflow components; compare against existing agent-skills before adoption.
- genesis-routing-metrics + genesis-paired-experiments: matched task-history measurement and missing-cost preservation.
- genesis-release-integrity: explicit release-byte inventory and verification.
- genesis-review-gate: strict review/refutation receipt with incomplete-state semantics.
- prompt-engineer: scored, gated, versioned and lineage-tracked machine-authored prompts.
- genesis-plan-graph: dependency/ownership-safe ready-wave scheduling.
- output-speed + context-budget: free token, latency and context-pressure controls.
- agent-pipeline: local coordination from task contract through routing, review evidence and controlled improvement.
- memory: zero-dependency persistent agent memory with core blocks plus append-only archive.
- fusion: cost-aware lane selection with deterministic checks and model adapters.
- bugbot: finder/refuter adversarial diff review with CI-gating of confirmed criticals.
- autonomous-loop + flywheel + megacycle + myriad: task selection, reward/policy updates, continuous codebase scanning and verifier-based self-play patterns.
- llm-split: provider/plan traffic-share balancing with a daily ledger and kill switch.
- ai-video-studio-kit: self-hosted short-form video pipeline relevant to YouTube/media work.
- apify-replacement: self-hosted scraper/enrichment pipeline relevant to prospecting; production use still requires terms/robots/reliability checks.
- telegram-command-bridge + whatsapp-command-channel: remote command channels to a local agent; useful pattern but requires authentication and provider/account setup.
- qwen38-uncensored: local Qwen 3.8 27B serving path for controlled local inference where hardware permits.

### Empty/placeholder repositories
- dual-uncensored
- cursor-uncensored

### Duplication / adoption rule
The Genesis family is unusually repetitive by design. Do not copy all components into Salamou-31. Compare exact contracts against existing agent-skills, Delivery Gate, ASTRA and COLLECTION, then extract only missing primitives with measurable leverage.

### Safety / provenance boundary
qwen38-uncensored is treated as local-model infrastructure, not as a blanket recommendation to remove safety controls. Public-facing use retains application-level safety, authorization and abuse controls.
