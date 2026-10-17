# Account-wide source capture — unslothai — 2026-10-17

Status: OWNER_ENUMERATION_COMPLETE; LOCAL-INFERENCE SOURCES_TRIAGED; DEEP_SWEEP_OPEN
Owner: https://github.com/unslothai
Owner-scoped search: page 1 returned 13 public repositories; page 2 returned 0.
Scope: README and root LICENSE review of the main training/runtime, model tooling, notebooks and forked inference projects. Not a full audit of all 13 repositories.

## Enumerated public repositories

1. https://github.com/unslothai/unsloth
2. https://github.com/unslothai/notebooks
3. https://github.com/unslothai/hyperlearn
4. https://github.com/unslothai/unsloth-zoo
5. https://github.com/unslothai/llama.cpp
6. https://github.com/unslothai/cut-cross-entropy
7. https://github.com/unslothai/stable-diffusion.cpp
8. https://github.com/unslothai/transformers
9. https://github.com/unslothai/gpt-oss
10. https://github.com/unslothai/whisper.cpp
11. https://github.com/unslothai/unsloth-staging-1
12. https://github.com/unslothai/audio.cpp
13. https://github.com/unslothai/.github

## Highest-value candidates

### P1 — unsloth

- Source: https://github.com/unslothai/unsloth
- README revision: `8db45e3224061b1d883cfc168b0ef6eaeb73d451`; root LICENSE is Apache-2.0.
- Provides local model inference/fine-tuning tooling, an OpenAI-compatible local API, agent/MCP integrations, Docker support and remote/LAN access to a local runtime.
- Supports Windows, Linux, WSL and macOS according to README; actual performance depends on model size, CPU/GPU backend, RAM/VRAM and drivers.
- Best fit: local inference for API Factory/ASTRA only if the existing computer can run the chosen model. It does not supply free hosted compute, and remote access still requires a reachable host/network boundary.
- README's speed/VRAM claims are upstream claims; benchmark against the actual machine before planning around them.

### P1 — unsloth-zoo

- Source: https://github.com/unslothai/unsloth-zoo
- Root LICENSE is LGPL-3.0. Review file-level licenses and redistribution obligations before embedding or distributing modified code in a commercial product.
- Includes model training helpers and free notebook recipes. Colab/Kaggle free compute is subject to those platforms' availability, limits and session expiry; it is not a persistent API host.

### P1 — notebooks

- Source: https://github.com/unslothai/notebooks
- Root LICENSE is LGPL-3.0.
- Large catalogue of fine-tuning/inference examples, including small models and local Ollama/GGUF workflows. Useful for experiments and model-selection, not a production service by itself.

### P2 — hyperlearn

- Source: https://github.com/unslothai/hyperlearn
- README describes optimized numerical/statistical routines; README states Apache-2.0. Default branch is `master`, so the failed `main` license lookup is not evidence of a missing license.
- Not directly relevant to API Factory unless a measured numerical workload appears.

### P2 — llama.cpp fork

- Source: https://github.com/unslothai/llama.cpp
- README advertises an OpenAI-compatible API server and multiple local hardware backends; LICENSE is MIT.
- Canonical upstream is https://github.com/ggml-org/llama.cpp. Treat the Unsloth copy as a fork/variant, not a new independent runtime to adopt without comparing patches and release cadence.

### P2 — gpt-oss fork

- Source: https://github.com/unslothai/gpt-oss
- Root LICENSE is Apache-2.0; README discusses local `gpt-oss-20b` inference and a much larger 120B option requiring high-end hardware.
- Canonical model source is https://github.com/openai/gpt-oss. Model hardware requirements and model license must be checked separately from repository code licensing.

## Cost / execution decision

- Local inference has no per-request hosted-provider bill but still requires hardware, electricity, disk and maintenance.
- Free notebooks are useful for short experiments, not a persistent production endpoint.
- No existing reachable local GPU/Unsloth host was verified in this pass; no model was downloaded and no training job was started.
- Do not replace the API Factory's provider boundary with another router. Add a local-provider adapter only after a reachable local endpoint and hardware budget are verified.

## Downstream owner expansion

- Canonical upstreams: `ggml-org/llama.cpp` and `openai/gpt-oss` are already known source owners and should be deduplicated with their fork records.
- Cloudflare remote-access documentation links are deployment guidance, not proof of a connected Cloudflare account or a hosted free service.
- The remaining enumerated repositories include transformer/model forks, diffusion, speech and audio projects; they remain open for source-level review.

## Remaining work

1. Check whether the user's local Windows/WSL environment has enough RAM/VRAM and an accessible runtime; do not assume local resources are reachable from this chat.
2. Benchmark a small quantized model locally before any API Factory adapter is selected.
3. Audit model licenses and external dependencies per model/repository before commercial use.
4. Keep account deep sweep open.
