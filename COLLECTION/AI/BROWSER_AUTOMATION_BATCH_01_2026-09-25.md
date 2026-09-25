# Browser Automation — Batch 01 — 2026-09-25

## Collection rule
Retain distinct browser/desktop automation sources even when they overlap. Preserve each repository when it contributes a different runtime, browser-control model, deployment mode, license, security boundary, integration surface, or subscription-elimination value.

## 1. Nanobrowser — nanobrowser/nanobrowser
Source: https://github.com/nanobrowser/nanobrowser
Default branch: master
README SHA: 2a33c4cbb09b2775272b4e359d10ab12e3e28074
LICENSE SHA: 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64
License: Apache-2.0
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository evidence:
- Open-source browser-based AI web-automation Chrome extension positioned as a free alternative to hosted operator products.
- Multi-agent architecture with specialized Navigator and Planner roles.
- Runs locally in the browser; credentials are intended to remain local rather than being sent to a Nanobrowser cloud.
- Supports OpenAI, Anthropic, Gemini, Ollama, Groq, Cerebras, Llama and custom OpenAI-compatible providers.
- Local-model path through Ollama/custom providers can remove model API cost when suitable local inference is available.
- Chrome and Edge are officially supported; Firefox/Safari and other Chromium variants are not officially supported.
- Build from source requires Node.js 22.12+ and pnpm 9.15.1+.
- Apache-2.0 license confirmed directly.
- README states there are no Nanobrowser subscription fees, but provider/model usage can still create external cost unless a local model is used.

Collection value: lightweight local browser-agent/Chrome-extension architecture and a direct subscription-elimination path for operator-style browser workflows.

## 2. Steel Browser — steel-dev/steel-browser
Source: https://github.com/steel-dev/steel-browser
Default branch: main
README SHA: eb876f2b6e5784a32f1e3a76300068bb1f89c4d1
LICENSE SHA: 261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64
License: Apache-2.0
Status: EXTRACTED_PENDING_DEEP_VERIFICATION

Verified from repository evidence:
- Open-source browser infrastructure intended as a self-hostable browser runtime/API for AI agents and automation.
- Docker Compose development deployment and direct Node.js/Chrome deployment paths are documented.
- REST API exposes browser sessions plus quick actions such as scrape, screenshot and PDF.
- Stateful sessions can preserve browser state and accept custom options/extensions and proxies.
- Compatible with Puppeteer, Playwright and Selenium workflows.
- Python and Node SDKs support a configurable base URL, including self-hosted Steel instances.
- Local instance is documented on localhost:3000, with UI on 5173 for development.
- Apache-2.0 license confirmed directly.
- Cloud and self-hosted modes coexist; cloud-specific services are not counted as eliminated by the self-hosted source.

Collection value: browser-runtime infrastructure layer rather than a complete agent, useful for replacing hosted browser-session infrastructure and for making agent/browser workflows reproducible and self-hosted.

## Verification queue
Deep-verify dependency manifests, current revision provenance, tests/CI, Docker production path, cloud-vs-self-hosted boundaries, browser isolation/security controls, proxy requirements, and operational limitations before VERIFIED classification.
