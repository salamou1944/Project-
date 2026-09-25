# COLLECTION — SHERLOCK OSINT CAPTURE — 2026-09-25

Status: EXTRACTED_PENDING_DEEP_VERIFICATION

## Canonical source
- Repository: sherlock-project/sherlock
- URL: https://github.com/sherlock-project/sherlock
- Public, non-fork, default branch: master
- Language: Python
- License: MIT
- Repository metadata observed: updated 2026-09-25, pushed 2026-09-24
- Repository size: ~19 MB
- Observed stars: 92,595; forks: 10,923
- Topics include OSINT, information gathering, reconnaissance, cybersecurity, forensics, pentesting and redteam.

## Capability
Sherlock is a username-focused OSINT CLI for checking whether a supplied username appears across many social-network/site endpoints. The upstream README advertises 400+ social networks.
It is not an email/phone enumeration engine. Results are detection claims based on site-specific request/response rules and can be affected by WAFs, network errors and false positives.

## Architecture evidence
- Main orchestration: sherlock_project/sherlock.py
- Site catalog/loader: sherlock_project/sites.py
- Default site manifest: https://data.sherlockproject.xyz
- Separate false-positive exclusions catalog.
- Concurrent requests via requests-futures, capped at 20 workers.
- Site-specific detection supports message, status-code and response-URL logic, plus WAF detection.
- Error contexts distinguish HTTP, proxy, connection, timeout, request and encoding failures.
- {?} expands a username into _, - and . variants.

## Package/deployment
- pyproject version: 0.16.2.
- Python: ^3.9.
- Dependencies include requests, requests-futures, PySocks, stem, pandas, openpyxl, colorama and tomli.
- CLI: sherlock = sherlock_project.sherlock:main.
- Dockerfile uses python:3.12-slim-bullseye and installs a specified sherlock-project package version.
- MIT source is self-hostable; no Sherlock SaaS subscription is required.
- External costs can still come from infrastructure, proxies/Tor, network limits or anti-bot controls.
- Default manifest is remote, so reproducible deployments should pin/capture its revision.

## Reusable patterns
1. Data-driven site adapters instead of hard-coded integrations.
2. Per-site detection strategies.
3. Explicit WAF/indeterminate states instead of converting blocked requests into negatives.
4. Bounded parallelism.
5. Remote catalog plus local/pinned catalog mode.
6. False-positive exclusion list.
7. Text/CSV/XLSX/JSON export paths.
8. Proxy support and Tor-related integration.
9. Separate search engine, result model and notification layer.

## Verification queue
- Pin and inspect the current data manifest; determine exact active site count.
- Inspect exclusions and false-positive test methodology.
- Inspect tests/CI coverage for detection rules.
- Inspect release/changelog and package provenance.
- Map site-specific dependencies/terms where relevant.
- Measure rate-limit/WAF behavior before persistent integration.
- Require secondary evidence before treating a username hit as identity proof.

## Dedup/provenance
Canonical identity: sherlock-project/sherlock.
Forks/wrappers/language rewrites are related projects, not duplicate identities.
A separately discovered Rust rewrite (sherlock-rs) is a distinct project and must be independently verified.

## Potential leverage
High-value candidate for the persistent research/OSINT intake layer because it can add broad username-presence discovery without a paid SaaS subscription. Keep it as a reusable component until evidence quality and false-positive handling are verified.

## Source revisions captured
- pyproject.toml: 3d1150fd84c974b13bc25c7fad9216c259abd186
- Dockerfile: ccdfbf23037f74d68c687e5f8c4ac10b73999a18
- LICENSE: 68306590d99e5c1e91fdb33d87228174b42b9558
- sherlock_project/sherlock.py and sherlock_project/sites.py inspected from current master.

## Status
Discovery and source extraction complete for this batch.
Deep verification remains pending.
