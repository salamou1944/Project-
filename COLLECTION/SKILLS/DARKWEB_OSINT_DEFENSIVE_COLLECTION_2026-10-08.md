# DARKWEB_OSINT_DEFENSIVE_COLLECTION — Skill Candidate — 2026-10-08

Status: CANDIDATE / NOT_PROMOTED
Source capture: COLLECTION/SOURCES/DARKWEB_OSINT_TOOLS_2026-10-08.md

## Goal
Provide a bounded, evidence-first capability for defensive dark-web OSINT and threat-intelligence collection.

## Contract
INPUT:
- domain
- company/brand
- email
- username
- known onion service
- IOC / threat actor identifier

PROCESS:
1. validate scope and lawful defensive purpose;
2. route onion collection only through an explicitly configured Tor boundary;
3. apply URL/redirect/IP/SSRF controls;
4. collect only allowed public content;
5. normalize URLs, onions, domains, emails, wallets and other IOCs;
6. deduplicate observations;
7. attach source URL, collection timestamp, content hash where appropriate and confidence;
8. correlate with existing CTI sources;
9. emit structured findings and uncertainty;
10. optionally export STIX/MISP-compatible objects.

OUTPUT:
- findings[]
- indicators[]
- entities[]
- relationships[]
- evidence[]
- confidence
- collection_timestamp
- limitations

## Hard gates
- Never treat discovery as identity proof.
- Never claim a source is live without a fresh check.
- Never expose Tor management/control interfaces publicly.
- Never bypass authentication, access controls or private areas.
- Never purchase or facilitate illicit goods/services.
- Never copy credentials or unnecessary personal data.
- Production readiness requires runtime evidence separate from source inspection.

## Candidate implementation sources
- osintph/darkweb-observatory
- osintph/threatintel-platform
- Kirov-Dynamics-Technology/kirov-osint-intelligence
- spideydotjs/gengar

## Promotion gate
Before promotion to canonical agent-skills:
- semantic dedupe against existing OSINT, SOAT, evidence/provenance and API Factory Skills;
- verify repository license and current revision;
- independently test bounded collection in an isolated environment;
- prove evidence schema and failure handling;
- prove no clearnet leakage for onion retrieval;
- preserve source provenance.