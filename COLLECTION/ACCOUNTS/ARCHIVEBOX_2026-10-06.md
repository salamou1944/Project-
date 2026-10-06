# COLLECTION — ArchiveBox account sweep
Updated: 2026-10-06

## Account
- Owner/org: ArchiveBox
- Scope: all public repositories returned by owner-scoped GitHub enumeration on 2026-10-06
- Enumeration result: 25 public repositories
- Completion state: DEEP SWEEP COMPLETE for the enumerated 25-repository frontier
- Important: downstream owners discovered below are new collection targets; this does not close the global Collection frontier.

## Repository inventory
1. ArchiveBox/ArchiveBox — core self-hosted web archiving app; MIT; dev branch.
2. ArchiveBox/archivebox-browser-extension — browser capture/submission extension.
3. ArchiveBox/good-karma-kit — Docker Compose spare-compute project; independent project/reference.
4. ArchiveBox/electron-archivebox — desktop client; GPL-3.0.
5. ArchiveBox/abx-dl — all-in-one URL downloader/extractor CLI.
6. ArchiveBox/docker-archivebox — Docker deployment definitions.
7. ArchiveBox/readability-extractor — JS CLI wrapper around Mozilla Readability.
8. ArchiveBox/pocket-exporter — historical Pocket export utility; DEAD/unsupported; preserve as historical reference only.
9. ArchiveBox/archivebox-proxy — mitmproxy-based URL-to-ArchiveBox proxy; old/contributed.
10. ArchiveBox/abxpkg — runtime dependency/package detection and installation library + CLI.
11. ArchiveBox/homebrew-archivebox — Homebrew packaging wrapper.
12. ArchiveBox/DigestBox — design mockup only; preserve as product concept, not production-ready.
13. ArchiveBox/abx-spec-behaviors — draft cross-browser automation behavior specification.
14. ArchiveBox/docs — documentation repository; no README surfaced in current fetch.
15. ArchiveBox/internet-archiving-talk — educational/reference material on internet archiving.
16. ArchiveBox/pip-archivebox — obsolete packaging repo; preserve historical provenance.
17. ArchiveBox/abxbus — multi-runtime in-memory typed event bus.
18. ArchiveBox/community — curated web-archiving ecosystem/community index.
19. ArchiveBox/debian-archivebox — Debian/Ubuntu package wrapper with exact wheel/hash verification and real install smoke checks.
20. ArchiveBox/monorepo — cross-repo workspace/coordinator.
21. ArchiveBox/android-archivebox — Android client; GPL-3.0-only.
22. ArchiveBox/ios-archivebox — Apple/iOS/macOS client; enumeration only in this pass.
23. ArchiveBox/githubusers — GitHub contribution dashboard/mining system using GitHub Actions + Cloudflare Worker/static assets.
24. ArchiveBox/archivebox-js — browser capture + WACZ portable archive/replay + plugin architecture.
25. ArchiveBox/browser-session-autohealer — alpha browser-session checking/healing with reusable repair scripts and multiple browser-provider adapters.

## High-value preserved assets

### A. Deterministic real-artifact capture pipeline
ArchiveBox preserves URLs into durable standard formats (HTML, PNG, PDF, TXT, JSON, WARC, SQLite) and exposes CLI, REST API, filesystem, and web interfaces. Its agent guide explicitly requires real CLI/API/browser/subprocess/DB/filesystem verification and rejects mocks, fake binaries, fake hooks, shortcuts, weakened assertions, and paper-over retries.
Reuse targets: evidence-backed operator; collection/evidence preservation; artifact verification; AI Operating Memory evidence capture.

### B. Plugin contract and composable execution
abx-plugins defines a declarative plugin contract with config schemas, required binaries, crawl/snapshot hooks, output paths, presentation metadata, and generic host orchestration. abx-dl executes the same plugin ecosystem in phases and records plugin-level output/status.
Reuse targets: provider-neutral adapters; capability/plugin registries; SOAT/API Factory execution stages; deterministic artifact/evidence capture.

### C. Runtime dependency resolution
abxpkg provides a typed abstraction over multiple package managers/providers, runtime detection/installation, binary lookup, and executable invocation.
Reuse targets: local/free dependency bootstrap; provider-neutral capability activation; deployment/runtime preparation.

### D. Multi-runtime event bus
abxbus provides typed events across Python/TypeScript/Rust/Go, async execution, nested event tracking, OTEL, concurrency controls, and deterministic event lifecycle tests.
Reuse targets: agentic orchestration; execution event/evidence pipeline; cross-runtime integration boundaries.

### E. Portable archive artifact
archivebox-js uses WACZ as a portable capture unit with WARC records, CDX indexes, metadata, integrity hashes, HTTP Range access, offline replay, and plugin-generated artifacts.
Reuse targets: durable evidence bundle; portable artifact handoff; provenance/integrity preservation.

### F. Browser-session healing
browser-session-autohealer checks and repairs browser sessions, uses AI only for novel failures, stores reusable repair scripts to reduce repeated LLM calls, and supports multiple browser providers.
Reuse targets: browser-presence-operator; failure-recovery-operator; persistent-task-operator; cost-aware repair/retry logic.

### G. Exact packaging verification
debian-archivebox resolves a specific PyPI wheel and SHA-256 at build time, installs it into a controlled runtime, and CI verifies actual package installation plus real archive output/filesystem state.
Reuse targets: evidence-driven release/deployment verification; artifact checksum verification.

### H. On-demand user mining architecture
githubusers uses a single GitHub Action plus Cloudflare Worker/static assets, deduplicates GitHub contribution data across forks, canonicalizes renamed/transferred repos, generates self-contained HTML, and exposes a refresh path.
Reuse targets: evidence/collection mining; low-cost serverless control plane; asynchronous user-triggered refresh workflows.

## Project/asset classification
- READY/NEAR-READY candidates: ArchiveBox core, archivebox-js, abx-dl, abxpkg, abxbus, githubusers, browser-session-autohealer.
- Component/pattern assets: abx-plugins, docker-archivebox, packaging repos, browser extension.
- Historical/reference: pocket-exporter, pip-archivebox, DigestBox, internet-archiving-talk, community index.
- Draft specification: abx-spec-behaviors.
- License-sensitive: GPL desktop/mobile/package clients; preserve provenance and do not merge code into MIT Skills without license review.

## Downstream owner targets exposed
At minimum: mozilla, mitmproxy, webrecorder, internetarchive, pywb, cloudflare, pydantic, browser-use, browserbase, kernel.sh, anchorbrowser, browserless, zenrows, gildas-lormeau, yt-dlp, gallery-dl, puppeteer, playwright.
These are collection targets, not claims of completion.

## Agent-Skills promotion decisions
1. Do not create a duplicate generic event-bus Skill from abxbus. First compare with agentic-orchestration and adaptive-orchestrator; strengthen existing canonical Skill if execution boundary matches.
2. Do not create a duplicate browser automation Skill from browser-session-autohealer. Compare with browser-presence-operator and failure-recovery-operator; merge only verified unique contracts.
3. Do not create a generic dependency-installation Skill from abxpkg until compared with existing runtime/bootstrap/deployment Skills.
4. Treat archivebox-js WACZ/fixity as an evidence/artifact pattern candidate; integrate only into the existing evidence layer if its implementation is inspected and validation is available.
5. Treat githubusers mining architecture as a reusable collection/mining pattern, not as production proof for our own collection system.
6. Preserve every source and historical project even when the current activation decision is negative.

## Verification boundary
This account sweep is evidence-backed at repository/README/agent-guide inspection level. It does not claim runtime execution of the external ArchiveBox projects. Runtime readiness remains subject to each project's own tests, dependencies, licenses, and environment.

## Next actions
- Sweep downstream owners recursively.
- Compare the high-value implementation clusters against canonical agent-skills.
- Strengthen existing Skills rather than adding semantic duplicates.
- Update the account register from ENUMERATED to DEEP SWEEP COMPLETE for ArchiveBox, while keeping downstream targets open.