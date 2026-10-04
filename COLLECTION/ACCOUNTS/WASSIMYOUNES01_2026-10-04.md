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