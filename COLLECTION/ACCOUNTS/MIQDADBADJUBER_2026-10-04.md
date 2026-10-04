# miqdadbadjuber — Account Capture — 2026-10-04

Source: https://github.com/miqdadbadjuber
Owner: miqdadbadjuber (Miqdad Badjuber)
Status: ACCOUNT-WIDE SOURCE ADDED / ENUMERATION QUEUED
Captured: 2026-10-04

## Account evidence
- GitHub public profile currently reports 11 public repositories.
- The account is now a permanent COLLECTION account-wide source.
- Per COLLECTION policy, repository count is discovery metadata; it is not proof that every repository has been inspected.
- The full 11-repository inventory must be enumerated and then processed recursively.

## Verified/high-value repositories currently identified
- anti-slop — https://github.com/miqdadbadjuber/anti-slop
  - MIT.
  - Latest inspected release: v3.2.20.
  - Agent-skills / coding-quality / delivery-gate / cross-agent plugin-door source.
  - Existing extraction: `docs/COLLECTION-MIQDADBADJUBER-ANTI-SLOP.md` in salamou1944/agent-skills.
  - Adoption already implemented in agent-skills through the Delivery Gate; do not duplicate the capability.
- portfolio — https://github.com/miqdadbadjuber/portfolio
  - Personal portfolio/source index.
  - Its project list identifies ContextForge, DiagramPilot-AI and OpenFolio-AI as additional repositories requiring independent verification.
- contextforge — https://github.com/miqdadbadjuber/contextforge
  - Identified by the author's portfolio as a context-engineering / prompt-architecture toolkit.
  - Repository-level verification required before adoption.
- DiagramPilot-AI — https://github.com/miqdadbadjuber/DiagramPilot-AI
  - AI architecture-diagram generator using Gemini and Mermaid.
  - MIT per repository metadata surfaced during discovery.
  - Repository-level verification required before adoption.
- OpenFolio-AI — https://github.com/miqdadbadjuber/OpenFolio-AI
  - Identified by the author's portfolio as an open portfolio generator.
  - Repository-level verification required before adoption.

## Account expansion queue
1. Enumerate all 11 public repositories from the account.
2. Deduplicate by canonical owner/repository identity.
3. Inspect each repository at repository/file level according to COLLECTION rules.
4. Capture license, revision/version, dependencies, capabilities, security boundaries and limitations.
5. Follow relevant releases/tags/workflows/issues/PRs where they materially affect adoption.
6. Recursively add newly discovered owner accounts and repositories to the same COLLECTION queue.
7. Cross-link overlapping capabilities with existing COLLECTION entries before proposing implementation.
8. Promote only evidence-backed leverage; do not duplicate the already-adopted Anti-Slop Delivery Gate.

## Provenance
- Account profile: https://github.com/miqdadbadjuber
- Anti-Slop: https://github.com/miqdadbadjuber/anti-slop
- Portfolio: https://github.com/miqdadbadjuber/portfolio
- Additional project references were taken from the author's public portfolio and remain discovery evidence until independently inspected.
