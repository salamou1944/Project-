# COLLECTION — DEDUPLICATION AND PROVENANCE AUDIT — 2026-09-25

Status: AUDITED_PARTIAL

## Scope
Recursive Project- collection tree review for duplicate files, repeated source references, canonical source identity, cross-references, and user-repository role separation.

## Findings
- Current collection tree was inspected recursively.
- No identical Markdown blob SHA was observed among the collection files inspected.
- Repeated project references are generally intentional cross-references between discovery indexes, evidence records, queues, and dedicated captures.
- Agent-Reach, SearXNG, Nmap, aw-junaid, and mufeedvh recur across documents, but are not treated as separate project identities.
- Discovery references and verification records are kept distinct; discovery is not promoted to verified merely because it appears in multiple documents.

## Canonical identity rule
Canonical source identity = upstream owner/repository or canonical website, plus path and revision when available.

When a source already exists:
1. add new evidence to the existing identity;
2. preserve discovery provenance;
3. record fork/mirror relationships explicitly;
4. do not create a second project identity;
5. never replace stronger evidence with weaker discovery evidence.

## User repository role map
- salamou1944/Astra- = ASTRA bot implementation.
- salamou1944/Astra = ASTRA storage/evidence.
- salamou1944/Project- = Free Project / central collection store.
- salamou1944/Files- = collected files/materials.
- salamou1944/agent-skills = engineering/control-plane.
- salamou1944/Easy- = EASY product.
- salamou1944/AI_operating_memory = canonical machine-readable state.
- salamou1944/Salamou-31 = AI/API hub.

No role collision was found in the inspected Project- corpus.

## Stale metadata found
COLLECTION/INDEX.md contains an outdated statement that the ASTRA prospective validation result was pending. The dedicated ASTRA state records run 36086735104 as completed/success, while correctly stating that CI success does not itself prove forward-sample sufficiency or profitability. The index needs synchronization.

## Important overlap classes
The following are expected overlaps, not duplicates:
- AI candidates across AI indexes and broad collection batches.
- Browser/research candidates across browser, intake, and master documents.
- Self-hosted candidates across category files and replacement maps.
- Nmap/account sources across account capture and verification records.

## Collection remains open
This audit does not close collection. Remaining work includes account-wide repository and public-gist exhaustion, remaining Nmap source inspection, remaining mufeedvh repositories, high-value verification, source-graph exhaustion, and final consistency checks.
