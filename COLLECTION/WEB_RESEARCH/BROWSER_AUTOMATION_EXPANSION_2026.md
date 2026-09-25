# Browser Automation Expansion — 2026-09-25

Status: DISCOVERY_CAPTURED

## Writ
- URL: https://github.com/usewrit/writ
- Capability observed: self-hosted browser workflow recorder/replayer, REST API, MCP tools, OCR/document reading, monitoring, scheduling and crawl coordination.
- Architecture observed: Python coordinator + separate Rust browser agent; SQLite storage.
- License observed in README: AGPL-3.0.
- Notable property: replayed workflows do not require AI tokens according to project documentation.
- Verification required: security model, agent enrollment, browser isolation, persistence, scaling and license implications.

## WebOperator
- URL: https://github.com/KazKozDev/WebOperator
- Capability: local-first Chrome browser agent + MCP server; can use Ollama/MLX and existing browser sessions.
- Potential value: authenticated browser reuse without moving session state to a separate cloud browser.
- Verification required: extension permissions, session security, browser isolation, license and current code quality.

## WebNav
- URL: https://github.com/rahulcvwebsitehosting/WebNav
- Capability: local AI browser agent as Chrome extension; supports Ollama, LM Studio and vLLM through local OpenAI-compatible endpoints.
- Potential value: lightweight local browser automation.
- Verification required: extension security, model/tool boundaries and maintenance status.

## AgentBrowser
- URL: https://github.com/smouj/agent-browser
- Capability: REST/WebSocket browser control with dashboard, Playwright and vision-oriented extraction.
- Potential value: service boundary for agents needing real browsers.
- Verification required: license, auth model, container/browser isolation and production maturity.

## Rule
Browser candidates are discovery leads until permissions, auth/session handling, isolation, failure behavior and current source are inspected.
