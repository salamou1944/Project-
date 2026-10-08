# DARK WEB OSINT / THREAT INTELLIGENCE — COLLECTION CAPTURE — 2026-10-08

Status: DISCOVERY_CAPTURED / VERIFIED_SOURCE_METADATA
Class: CAPABILITY / THREAT_INTELLIGENCE / OSINT
Purpose: preserve high-leverage open-source dark-web OSINT and defensive threat-intelligence sources for later semantic dedupe, Skill extraction, and bounded integration.

## Primary verified sources

### 1. osintph/darkweb-observatory
- Source: https://github.com/osintph/darkweb-observatory
- Current observed: public, 40 stars, 13 forks; 3 commits in the surfaced snapshot.
- Capability: self-hosted monitoring of configurable .onion sites through Tor; uptime/history; IOC extraction; deep scans; change detection; threat-intelligence feeds.
- Extractable primitives:
  - onion availability monitoring
  - email / crypto-wallet / onion-link extraction
  - page-content hashing and change detection
  - target configuration and scheduled scans
  - remote CTI seed ingestion
  - risk/alert dashboards
- Security boundary: source itself recommends outbound Tor, no inbound exposure, non-root operation, local-only manager access, and defensive OSINT use.
- Readiness: discovery evidence only; do not claim production readiness without independent runtime verification.

### 2. osintph/threatintel-platform
- Source: https://github.com/osintph/threatintel-platform
- Current observed: public, AGPL-3.0, 142 stars, 24 forks, 130 commits; version 1.1.0 in surfaced README.
- Capability: self-hosted threat-intelligence platform combining .onion crawling, keyword monitoring, Telegram monitoring, ransomware intelligence, IOC feeds, quick OSINT scans, dashboards and daily intelligence digest.
- Architecture evidence: Docker Compose, PostgreSQL, Tor SOCKS/control, Flask dashboard, optional Web Check.
- Security-relevant implementation evidence:
  - safe_fetch allowlist
  - IP blocklist
  - TLS enforcement
  - redirect re-validation
  - IPv4-mapped IPv6 blocking
  - SSRF guard
  - request-scoped DB sessions
  - tests reported in README: 135 passed, 2 skipped at capture time.
- Extractable primitives:
  - bounded Tor crawler
  - keyword hit engine
  - IOC normalization/filtering/confidence
  - quick-scan orchestration
  - daily digest/report generation
  - multi-source CTI feed adapters
- License boundary: AGPL-3.0; any reuse must preserve license obligations.

### 3. Kirov-Dynamics-Technology/kirov-osint-intelligence
- Source: https://github.com/Kirov-Dynamics-Technology/kirov-osint-intelligence
- Capability claimed by repository: open-source collection across dark web, social media, repositories, domains and breach archives; AI-assisted entity/relationship extraction; STIX 2.1 export; MISP/TAXII integration.
- Architecture evidence: collectors -> queue -> normalize -> dedupe -> enrich -> NER/NLP -> graph/profile -> reports/STIX.
- Potential leverage:
  - normalized intelligence objects
  - entity/relationship extraction
  - threat-actor profiling
  - STIX 2.1 evidence interchange
  - MISP/TAXII integration boundary
- Status: discovery capture only; implementation and license/runtime claims require repository-level verification before reuse.

### 4. spideydotjs/gengar
- Source: https://github.com/spideydotjs/gengar
- Capability claimed: Tor-routed dark-web search/probing, onion snapshots, crypto-wallet extraction, PGP/WKD intelligence, entity graphing, STIX 2.1 export, evidence hashing/chain-of-custody concepts and multi-chain intelligence.
- Priority: high research value for evidence/provenance and crypto-intelligence adapters.
- Status: discovery capture only. Treat all court-ready/evidence claims as implementation claims requiring independent verification.

## Supporting discovery index
### osintshifu/awesome-osint-repos
- Source: https://github.com/osintshifu/awesome-osint-repos
- Surfaced dark-web catalogue includes Robin, TorBot, OnionSearch, darkdump, AIL Framework, Ahmia, VoidAccess, Darkus, Darknet MCP Server, darc, OnionClaw, onion-lookup, DarkSpider, Sicry, PyAhmia and LeakRecon.
- Use as a discovery index, not as runtime evidence. Each candidate requires independent repository/license/status verification.

### djbpm/osint-toolkit
- Source: https://github.com/djbpm/osint-toolkit
- Surfaces Ahmia, OnionSearch and other dark-web / leak-monitoring references.
- Treat aggregator entries as leads only; do not promote them to canonical Skills without direct source verification.

## Initial semantic capability map
1. ONION_DISCOVERY
2. TOR_BOUNDED_COLLECTION
3. ONION_AVAILABILITY_MONITORING
4. DARKWEB_KEYWORD_MONITORING
5. IOC_EXTRACTION
6. CONTENT_CHANGE_DETECTION
7. ENTITY_RELATIONSHIP_EXTRACTION
8. THREAT_ACTOR_PROFILING
9. CTI_FEED_NORMALIZATION
10. STIX_EXPORT
11. MISP_TAXII_INTEROP
12. EVIDENCE_HASHING_PROVENANCE
13. ALERTING_DAILY_DIGEST
14. QUICK_SCAN_ORCHESTRATION

## Dedupe / integration decision
Do NOT import a complete dark-web platform into Project-, Salamou-31, ASTRA, or agent-skills at this stage.

The strongest reusable contracts are:
- bounded Tor collection with explicit allowlists and SSRF protections;
- IOC/entity normalization and dedupe;
- evidence hash + timestamp + source provenance;
- STIX/MISP/TAXII interchange;
- scheduled monitoring and alert/digest generation.

These should be compared against existing COLLECTION/SOAT/agent-skills/API Factory capabilities before creating new Skills.

## Safety / legal boundary
This collection is for defensive OSINT, threat intelligence, exposure monitoring and security research. Do not purchase from, transact with, or facilitate illicit dark-web marketplaces. Do not collect credentials/secrets or private personal data beyond what is necessary and lawful for the defined investigation.