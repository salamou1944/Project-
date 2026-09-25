# COLLECTION — MUFEEDVH DEEP EXTRACTION BATCH 02 — 2026-09-25

Status: EXTRACTED_PENDING_DEEP_VERIFICATION
Source identity: mufeedvh (public GitHub account)
Collection rule: canonical owner/repo + revision; no duplicate project identity.

## Scope completed in this batch

Repository inventory search confirmed a broad public repository set under `mufeedvh`. This batch deep-extracted the following previously not deeply captured candidates:

### 1. mufeedvh/code2prompt
Canonical: `mufeedvh/code2prompt`
Default branch: `main`
README blob SHA: `70bb36263b10e3db52b7ec8f07d3b790d739cdb7`
LICENSE blob SHA: `77c409fafd9fc0da6d7b0bee4215602458b7b2a9`
Cargo.toml blob SHA: `ba708798bbd38683cae2d7209dd09aa41ab1bec5`
License: MIT.
Capability: local codebase context-engineering pipeline for LLMs. The repository currently combines a Rust core, CLI/TUI, Python bindings, and a local MCP server.
Important implementation patterns:
- secure file traversal;
- `.gitignore`-aware filtering;
- configurable include/exclude globs;
- Git metadata/diff/log/branch context;
- Handlebars templates;
- token estimation;
- structured handling of CSV, notebooks and JSONL;
- optional clipboard output;
- agent skill for scoped repository navigation;
- local MCP-server mode.
Dependencies observed in Cargo workspace include git2 with vendored libgit2/OpenSSL, ignore, globset, rayon, handlebars, pyo3, tokio, serde/serde_json, ratatui and tokenization support.
Reuse value: strong candidate for reducing repository-context transfer cost and repeated agent exploration; can run locally and does not require a hosted SaaS subscription. External LLM/model costs remain separate.
Verification remaining: inspect core crate implementation, MCP server, skill files, tests/CI, release provenance and dependency/security boundaries.

### 2. mufeedvh/binserve
Canonical: `mufeedvh/binserve`
Default branch: `master`
README blob SHA: `dfa499ee6a5ab26a4aa0f21c1f69def0d3ffb60d`
LICENSE blob SHA: `3310a5bbf870ee2555f26499df94eaf7337aa641`
Cargo.toml blob SHA: `56144bb7602acf59a7d1268603dab368045c8010`
License: MIT.
Capability: portable single-binary static web server with TLS, routing, hot reload, caching, templating and security protections.
Observed dependencies: Actix Web/files, rustls, Handlebars, DashMap, serde, notify-debouncer and related Rust crates.
Subscription boundary: core OSS server is self-hostable; README separately advertises a paid `binserve+` product with DDoS protection, rate limiting and Prometheus metrics. Do not treat those paid features as part of the free replacement.
Reuse value: lightweight static hosting/runtime primitive for self-hosted projects.
Verification remaining: current runtime behavior, security tests, TLS defaults, release status and exact paid/free boundary.

### 3. mufeedvh/gisture
Canonical: `mufeedvh/gisture`
Default branch: `main`
README blob SHA: `7254251bbeea244eccf21984cb654cb33d5d46e2`
LICENSE blob SHA: `e09bcd15225bc02415949bf21f84c3451652f57e`
Cargo.toml blob SHA: `59cf929ede40e9b696c1f3bbe1a63c3be651321e`
License: MIT.
Capability: minimal blog generator driven by GitHub Gists, with SEO files, Handlebars templating, syntax highlighting, metadata and disk caching.
Observed dependency families: Handlebars, pulldown-cmark, syntect, sitemap, warp, ureq and cache support.
Reuse value: historical/simple content publishing pattern; Git-backed revision transparency and cache-aware builds.
Verification remaining: maintenance status, current GitHub API assumptions and dependency freshness.

### 4. mufeedvh/log4jail
Canonical: `mufeedvh/log4jail`
Default branch: `main`
README blob SHA: `1f38cc816cbb44f9ad846c8b823ef46d22eb8074`
LICENSE blob SHA: `e09bcd15225bc02415949bf21f84c3451652f57e`
Cargo.toml blob SHA: `f8a294962ef0568e0f07ad884bf2952797bc99de`
License: MIT.
Capability: reverse-proxy firewall intended to block Log4Shell payloads by scanning request bodies, headers and parameters.
Observed dependencies: warp TLS, warp-reverse-proxy, regex, tokio, serde/serde_json.
Reuse value: security-gateway pattern for defensive filtering and lab testing.
Boundary: use only for defensive/authorized environments; this capture does not operationalize attacks.
Verification remaining: test suite, bypass coverage, current Log4Shell relevance, TLS/proxy behavior and maintenance state.

### 5. mufeedvh/gofindapis
Canonical: `mufeedvh/gofindapis`
Default branch: `master`
README blob SHA: `4a4eae9f70be525aa5a4d2b9e21b921dd34092d2`
go.mod blob SHA: `68e06b7daf058959ad8789c0ffa4a6b4428523e3`
License: not established in this extraction; do not assume one.
Capability: recursively scans project files for API keys using regex; README records a completed pre-commit-hook TODO.
Reuse value: secret-leak detection pattern for local repositories/CI.
Verification remaining: source implementation, regex coverage, false positives, secret types, tests, and license.

### 6. mufeedvh/BrokenLinkHijacking
Canonical: `mufeedvh/BrokenLinkHijacking`
Default branch: `master`
README blob SHA: `8898961957c79c1ec399a89abcd81e6b9a0ad963`
go.mod blob SHA: `857d8d38331b791bc1fbe9fc5b23c2f46bb24c01`
License: not established in this extraction; do not assume one.
Capability: Go-based recursive website crawler for finding broken links.
Reuse value: lightweight broken-link discovery primitive for authorized websites.
Verification remaining: source, crawler scope, concurrency, URL handling, tests and license.

## Account-level finding

The current public repository inventory is substantially broader than the previously captured four `mufeedvh` projects. Repository search returned additional projects including `mnmlang`, `regretti`, `l33tmario`, `maram`, `okjson`, `website`, `notes`, `cheatsheets`, `huntr`, `SubCalc`, `rc-zip`, `x86doc`, `axum`, `pcb`, `mlmorph`, `cado-nfs`, `superpowers`, `schemes`, and others. These are inventory discoveries only until individually inspected.

## Deduplication / provenance

- Previously captured: `moonwalk`, `pdfrip`, `basecrack`, `seclip`, `code2prompt` inventory.
- This batch adds deeper evidence for code2prompt and new evidence for binserve, gisture, log4jail, gofindapis and BrokenLinkHijacking.
- No fork was promoted to a new canonical identity.
- No credentials or private data were copied.

## Next queue

1. Inspect code2prompt core/MCP/skill/tests and release provenance.
2. Continue mufeedvh account repository inventory until all relevant public repos are classified.
3. Continue public Gist inventory separately from repositories.
4. Continue Nmap source-level verification.
5. Continue aw-junaid remaining repositories/Gists.
6. Follow discovered projects only when they provide reusable evidence or a new capability family.

Collection remains open.
