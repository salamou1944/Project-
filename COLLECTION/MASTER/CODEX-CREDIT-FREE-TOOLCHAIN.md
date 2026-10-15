# Codex-credit-free development path

Updated: 2026-10-15

## Objective

Keep engineering work moving when Codex/API credit is unavailable. Prefer the existing local Git checkout, local shell, tests, and deterministic scripts first. Add an AI coding agent only when its model can run locally or is already included in an existing free entitlement.

**Cost rule:** an open-source agent is free software, but a hosted model may still charge for inference. A local model avoids API charges; it uses the computer's RAM/VRAM, CPU/GPU, storage, and electricity. Do not configure a paid provider or create a new subscription for this path.

## Options to evaluate

| Option | Best use | Model cost boundary | Git / execution fit | Official source |
|---|---|---|---|---|
| Git + PowerShell / Bash + repository tests | Reliable work that does not need an LLM; reproductions, patches, CI triage | No model required | Full native Git; directly runs project test commands | [Git](https://git-scm.com/), [PowerShell](https://github.com/PowerShell/PowerShell) |
| Aider | Small, reviewable edits in existing repositories | Local Ollama or another already-authorized model; hosted APIs can cost money | Terminal-first, Git-aware, supports reviewable diffs and commits | [Aider](https://github.com/Aider-AI/aider) |
| OpenCode | Terminal-based agent for multi-file repository work | Use a local provider/model; provider availability and defaults must be checked before use | Terminal workflow, tool execution, model-provider flexibility | [OpenCode](https://github.com/anomalyco/opencode) |
| Cline for VS Code | Interactive Windows development with explicit tool approval | Configure a local Ollama model; do not select a paid API provider | Reads/edits repository files and can run terminal commands after approval | [Cline](https://github.com/cline/cline) |
| Goose | General-purpose local agent and MCP workflows | Supports different providers; use a local provider to avoid API billing | Desktop/CLI agent with extensible tool integrations | [Goose](https://github.com/block/goose) |
| OpenHands | Larger autonomous tasks that benefit from an isolated agent workspace | Local model support must be validated against available hardware; containers may add disk/compute overhead | Self-hosted agent workspace and SDK | [OpenHands](https://github.com/All-Hands-AI/OpenHands) |
| Ollama | Local model runtime, not a coding agent by itself | No per-token API charge for models run locally | Supplies a local model endpoint to compatible coding tools | [Ollama](https://github.com/ollama/ollama) |

## Recommended order for this workspace

1. **Start now with Git + shell + tests.** Keep a clean branch per task, inspect `git status`, make a narrow patch, run the relevant tests, inspect `git diff --check` and `git diff`, then commit. This works without any model credit.
2. **Install Ollama only after checking machine capacity.** Check free disk, RAM, and whether a supported GPU is available before downloading a model. Start with a small coding model that fits; do not assume the machine can run a 30B+ model.
3. **Pilot one agent, not all of them.** First choice for Git-first changes: Aider + a local Ollama model. First choice for VS Code interactive command approval: Cline + Ollama. Compare on one disposable branch with a small test-driven change.
4. **Keep a strict verification loop.** Require tests and actual command output; inspect every diff; never let an agent deploy, change secrets, delete data, or merge automatically. For COLLECTION, installed third-party source must not be promoted to callable until a specific local entrypoint and smoke-test evidence exist.
5. **Use existing GitHub Actions only as a verifier.** Keep workflows bounded and fail-closed. A successful code-writing session is not production evidence; the target test or runtime smoke must pass.

## Current execution limitation

The connected Termalin tool currently reports **no connected hosts**, so it cannot run shell commands on the user's machine from this ChatGPT session. GitHub repository changes can still be prepared through the GitHub integration, but that is not equivalent to having executed local Git or tests. To enable direct local execution later, connect the machine through the existing Termalin connector; do not send passwords or API keys in chat.

## Selection checklist before installing anything

- [ ] Check `git --version`, Python/Node versions required by the repository, free disk, RAM, and GPU/VRAM.
- [ ] Confirm the agent's official repository/license and active maintenance.
- [ ] Confirm the model endpoint is local (for example, Ollama on localhost), not a paid hosted endpoint.
- [ ] Run a small task on a disposable branch; verify it can edit files, execute the intended tests, and show a truthful diff.
- [ ] Record model name, approximate hardware demand, successful test commands, and limitations in the existing Free/Files inventory when those repositories are reachable.
