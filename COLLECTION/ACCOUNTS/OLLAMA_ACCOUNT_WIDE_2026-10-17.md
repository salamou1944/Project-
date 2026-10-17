# Account-wide source capture — ollama — 2026-10-17

Status: OWNER_ENUMERATION_COMPLETE; FOUR_REPOSITORIES_TRIAGED; DEEP_SWEEP_OPEN
Owner: https://github.com/ollama
Owner-scoped search: page 1 returned 4 public repositories; page 2 returned 0.
Reviewed README and LICENSE for the four returned repositories; README revisions are recorded below.

## Enumerated public repositories

1. https://github.com/ollama/ollama
2. https://github.com/ollama/ollama-python
3. https://github.com/ollama/ollama-js
4. https://github.com/ollama/ollama-vscode

## Findings for API Factory / $0 inference

### P1 — ollama/ollama

- Source: https://github.com/ollama/ollama
- README revision: `6ccf0acbeff491cfffdd6fc972109801fd68fe36`; MIT license.
- Provides a local model runtime and REST API (default local endpoint shown in docs at `http://localhost:11434`) and an official Docker image.
- Local inference avoids per-request provider charges but still costs hardware, electricity, storage, and operational maintenance. It is not hosted Railway-like compute by itself.
- The README also describes cloud model access; cloud entries are a separate access/billing class and must not be assumed free.
- Best fit: local provider adapter for ASTRA/API Factory when a reachable operator-controlled machine has enough resources.

### P1 — ollama/ollama-python

- Source: https://github.com/ollama/ollama-python
- MIT license according to LICENSE.
- Python client for the Ollama API, including local model usage and separate cloud-model flows. Useful as an integration reference; it does not itself host a model.

### P1 — ollama/ollama-js

- Source: https://github.com/ollama/ollama-js
- MIT license according to LICENSE; README revision `ffe1249382b7e88a389d955479da602f9675f24c`.
- JavaScript/TypeScript client. Potential fit for a local provider adapter; verify API compatibility and version before adding a dependency.

### P2 — ollama/ollama-vscode

- Source: https://github.com/ollama/ollama-vscode
- MIT license according to LICENSE; package version observed `0.0.13`.
- Editor integration, not a hosting or API Factory runtime replacement.

## Decision

- Treat local Ollama as a no-per-request-cost inference option only if an existing machine/runtime is reachable and provisioned; no such reachable Ollama host was verified during this pass.
- Keep Ollama Cloud models separate from local inference. A model name containing `-cloud` or a cloud API path does not establish zero-cost eligibility.
- Do not install or deploy an Ollama service to an unknown or paid host as part of this collection pass.
- No code imported, no model pulled, and no provider request made.

## Remaining work

1. Check whether the user's existing local environment or connected hosts already run Ollama; do not assume the user's Windows machine is reachable through ChatGPT.
2. If a reachable host exists, run a local-only smoke test and add an API Factory provider adapter only after authentication/network boundaries are defined.
3. Deep-audit releases, model license/usage terms and security defaults before production adoption.
