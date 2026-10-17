# Free Development and Completion Tooling Alternatives
**Reviewed:** 2026-10-16  
**Purpose:** Continue engineering work while Codex credits are unavailable, without confusing free software with free model inference.

## Executive decision

Do not migrate the Collection pipeline away from GitHub Actions. Its existing incremental run `38841155076` completed successfully, including harvest, state validation, prioritized installation, post-install queue generation, and persisted evidence checks. Keep that as the execution backbone; add a coding agent only where it creates measurable value.

**Recommended order**
1. **Use existing GitHub Actions + repository scripts first.** This is the strongest zero-model-cost route for repeatable tests, JSON validation, builds, and reports. It already runs real code on hosted runners.
2. **Use the connected GitHub integration for repository work** (inspect files, review diffs, create branches/PRs, and verify Actions). This is repository automation, not an LLM and does not replace model reasoning.
3. **Try Gemini CLI only against an actually available free quota or existing authorized credential.** A key alone does not prove free quota; stop if the provider reports quota/billing limits.
4. **For recurring work without cloud credits, evaluate Ollama + OpenCode or Aider locally.** The agent software can be free, but model quality depends on local hardware; downloading/running a model has compute, storage, and electricity costs.
5. **Do not add several agents at once.** Pick one, test it on a disposable branch, and require tests + diff review before opening a PR.

## Alternatives by role

| Tool | Best role | What is free | Hidden constraint / verdict |
|---|---|---|---|
| GitHub Actions | CI, tests, scripts, scheduled/manual workflows | Existing workflows and repository scripts; hosted runner usage is subject to account quota | **Use now.** It already executed the Collection pipeline successfully. Monitor included minutes and concurrency. |
| GitHub connected integration | Inspect/update repository files, branches, PRs, statuses | Existing connected app actions, within permissions | **Use now.** No model credits required for direct API operations; complex reasoning still needs an agent/human. |
| Gemini CLI | Terminal coding agent | Official quota docs currently list up to **250 requests/day for an unpaid Gemini API key (Flash models only)**; Google-account Gemini Code Assist Individual sign-in lists up to 1,000/day. Limits are subject to per-minute caps and availability. | **First cloud-agent candidate** because a Gemini credential was previously reported available. Since the existing credential is described as an API key, assume the 250/day Flash-only path unless its account/quota page proves otherwise; verify before use and never enable billing by assumption. |
| OpenCode — https://github.com/anomalyco/opencode | Provider-flexible terminal/desktop coding agent | Agent software | Good general option, but it needs a model endpoint, free-tier provider, or local model. |
| Aider — https://github.com/Aider-AI/aider | Git-centric edits and small, reviewable commits | Agent software | Strong fit for controlled repository patches. Model/API usage is separate; local model is possible. |
| Goose — https://github.com/block/goose | General local agent and MCP-heavy workflows | Agent software | Useful if one tool should handle coding plus MCP workflows. Still needs a model/provider or local inference. |
| Cline — https://github.com/cline/cline | Supervised coding inside VS Code | Extension/software | Good when approval per action is important; bring a model/provider or local inference. |
| Roo Code — verify the current official repository before adoption | Multiple coding modes inside VS Code | Extension/software | Flexible but avoid adding it alongside Cline until one has been tested. Requires model access. |
| OpenHands — https://github.com/All-Hands-AI/OpenHands | Delegated/self-hosted engineering tasks | Open-source platform/agent components | More infrastructure than needed for the immediate Collection fixes; model and compute are separate costs. |
| Ollama — https://github.com/ollama/ollama | Run models locally | Runtime software and open model options | **Enabler for no-API inference**, not a coding agent by itself. RAM/VRAM and model quality are limiting factors. |
| LiteLLM — https://github.com/BerriAI/litellm | Route multiple model providers through one interface | Open-source proxy | Useful only after at least one viable provider/local endpoint exists; routing does not create free tokens. |
| Playwright — https://github.com/microsoft/playwright | Browser and end-to-end tests | Open-source testing framework | Valuable for EASY/web-app smoke tests, not a replacement for coding inference. |
| pytest / Python standard library | Deterministic tests and validators | Open-source tools included in common Python setups | **Prefer for Collection.** Most of the pipeline is Python and can be tested without an LLM. |

## Free-model and API discovery

- Existing collected source: `mnfst/awesome-free-llm-apis` (captured under `COLLECTION/ACCOUNTS/MNFST_AWESOME_FREE_LLM_APIS_2026-09-26.md`). Treat it as a **discovery list**, not proof that any provider is currently free, available in Algeria, or suitable for private source code.
- Before using any hosted free endpoint, verify current rate limits, region access, retention/training terms, required payment method, and whether a free quota is still active. Never send secrets, keys, production customer data, or private repository content to an unvetted endpoint.
- A provider's free quota may expire or change. The fallback should be deterministic local/CI work, not a chain of unverified free API claims.

## Useful assets already discovered in Collection

These are candidates to inspect, not automatic install/promote recommendations:

- Agent workflow/skills: https://github.com/obra/superpowers ; https://github.com/addyosmani/agent-skills ; https://github.com/vercel-labs/agent-skills
- MCP safety: https://github.com/google/mcp-security ; https://github.com/trailofbits/mcp-context-protector ; https://github.com/cisco-ai-defense/mcp-scanner
- Browser automation: https://github.com/vercel-labs/agent-browser ; https://github.com/microsoft/playwright
- Free-model/API discovery: https://github.com/mnfst/awesome-free-llm-apis

Collection's own `CAPABILITY_SEARCH_SWEEP_2026-10-16.json` explicitly labels its results as discovery-only, not exhaustive or runtime evidence. Apply the same rule to these candidates.

## Operating pattern for zero-credit completion

1. Convert each task into a deterministic script/test whenever possible.
2. Run existing workflow checks on a branch; use Actions logs as execution evidence.
3. Keep changes small and reversible. Never overwrite large generated queues by hand.
4. For code changes, use one coding agent only if model access is available; require a minimal diff, tests, and independent review.
5. For external services, use the connected Railway/Vercel/Supabase/Replit tools only when the exact project/service is identified and the action is authorized. A connected app is not proof that a deployment or runtime is healthy; verify its reported result.
6. Record separate statuses: discovered, installed, tested, callable, production-proven. Do not promote one state into another.

## Evidence and boundaries

- Collection incremental workflow run: https://github.com/salamou1944/Project-/actions/runs/38841155076
- Run result: success; all listed harvest-job steps completed successfully.
- Hyperswitch deterministic test evidence is limited to the specific library/routing/unit-test entrypoints recorded in the verification JSON. It does **not** prove live payment processing.
- The current installed queue's `READY_FOR_VERIFICATION` status describes the installed asset as a whole. Narrow callable entries in `CALLABLE-REGISTRY.json` describe specific tested entrypoints; these states are not interchangeable.
- No agent has been installed or run on the user's machine by this report. This is a researched shortlist and operating plan, not a claim of local setup or deployment.
