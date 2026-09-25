# Browser Automation — Discovery Capture

Status: DISCOVERY_CAPTURED
Captured: 2026-09-25

## Sources

### Playwright
https://github.com/microsoft/playwright
- Browser automation foundation supporting Chromium, Firefox and WebKit.
- Candidate base layer for deterministic browser execution and verification.
- Verify license, current release, browser installation requirements and agent-facing wrappers before production use.

### Browser Use
https://github.com/browser-use/browser-use
- AI-agent-oriented browser automation built around browser interaction.
- Candidate for higher-level computer-use workflows.
- Verify current architecture, model/provider dependencies, license and self-hosting requirements before treating it as a paid-tool replacement.

### Open Browser
https://github.com/ntegrals/openbrowser
- TypeScript autonomous web-browsing framework built on Playwright.
- Repository currently exposes a substantial package structure and active history; treat as a candidate implementation source, not automatically production-ready. citeturn0search13

### OpenBrowser broker
https://github.com/floomhq/openbrowser
- Open-source browser infrastructure for AI agents with persistent Chrome profiles, remote API, MCP surfaces, human-auth handoff, telemetry and audits.
- MIT license is stated in the repository.
- Useful architectural pattern for isolated browser sessions and auditable agent browser infrastructure. citeturn0search8

### Browserable
https://github.com/browserable/browserable
- Open-source/self-hostable browser automation library for AI agents.
- Uses Docker Compose for deployment and supports LLM-provider API keys.
- Candidate for comparison against Browser Use/Playwright stacks. citeturn0search9

### AgentBrowser
https://github.com/smouj/agent-browser
- Open-source browser automation platform with REST API, WebSocket control, Playwright-backed browsers, persistent sessions, screenshots/DOM/accessibility-tree style inputs and dashboard.
- Small current footprint; preserve as a discovery candidate rather than selecting it automatically. citeturn0search2

## Reusable patterns to inspect later
- Deterministic browser layer (Playwright)
- Agent-facing abstraction layer
- Persistent/isolated browser profiles
- Human authentication handoff
- MCP/A2A interfaces
- Session leasing and concurrency control
- Browser telemetry/audit trail
- Accessibility tree + screenshot/DOM extraction
- Explicit separation between testing automation and autonomous agent automation

## Verification rule
No item above is marked VERIFIED solely from README/search results. Recursive repository inspection is required before adoption.
