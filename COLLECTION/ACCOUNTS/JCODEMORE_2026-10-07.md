# JCodesMore — Account Collection Capture

Date: 2026-10-07
Account: https://github.com/JCodesMore
Rule: ACCOUNT TARGET → ALL PUBLIC REPOSITORIES → RELEVANT CONTENT/SOURCES → NEW ACCOUNTS → REPEAT

## Enumeration
Owner-scoped GitHub search returned 18 public repositories in this pass:

1. JCodesMore/ai-website-cloner-template
2. JCodesMore/youtube-for-ai-agents
3. JCodesMore/ai-animated-website
4. JCodesMore/Powerful-Websites-You-Should-Know-About
5. JCodesMore/fix-claude-code
6. JCodesMore/jcodesmore-plugins
7. JCodesMore/agent-recall
8. JCodesMore/ai-chrome-extension-template
9. JCodesMore/discord-for-ai-agents
10. JCodesMore/orca
11. JCodesMore/movies-for-ai-agents
12. JCodesMore/jobs-for-ai-agents
13. JCodesMore/claude-code-visualizer
14. JCodesMore/starry-ai-bookmark-search
15. JCodesMore/slack-for-ai-agents
16. JCodesMore/artemis-2-arow-data
17. JCodesMore/OpenSpace-for-Artemis-II
18. JCodesMore/.github

## P0 — deep reusable-value candidates

### ai-website-cloner-template
Revision evidence:
- default branch: master
- README SHA: 4ed16fd46744c8939f1f70045824f31511daae1c
- package.json SHA: 520ca195c6c37c0a6912bc90acb3669e7e700fe4
- .agents/skills/clone-website/SKILL.md SHA: 20d3332dcd10b6e99f9aeac777f5f59d35d7321c
- references/inspection-guide.md SHA: c4de3176d0c9b1d822520722182b042fb6c180f2
- references/framer-and-motion.md SHA: 37c59fb766095cbbda12dc82bfd48025e4ba22dd
- AGENTS.md SHA: 82b1ecf0ea5b2994f6a4b4b81cf55dd2f1da5470
- License: MIT

Verified reusable contract:
Map → Observe → Build → Compare.
The canonical Agent Skill requires route mapping, preservation of existing authored routes, desktop/mobile/state inspection, real asset/font extraction, trigger/state evidence, matched source/local comparison, repair of largest visual deltas first, real interaction checks, runtime/missing-asset/overflow checks, and a successful production check plus rendered comparison before claiming completion.

Important evidence discipline:
- screenshots/iframes/downloaded bundles are references, not implementation
- DOM dumps do not replace visual/state inspection
- a successful build alone is insufficient; rendered comparison is required
- remaining differences must be named rather than calling an unchecked result pixel-perfect

References include specific handling for Framer, sticky scenes, animated media, responsive variants, SVG dependencies, scroll/click/hover/time drivers, and motion verification.

### youtube-for-ai-agents
README inspected. Apache-2.0. MCP server exposes YouTube search/watch/transcript/download/clip/reel capabilities through two skills and one agent; anonymous search is advertised as requiring no API key, with optional cookie-based personalization. High relevance to media research and the user's YouTube work. Requires separate license/runtime verification before extraction.

### fix-claude-code
README inspected. MIT. Single interactive /fixclaude skill that detects settings, applies bounded configuration changes, optionally installs companion tools, and reports a summary. Useful pattern for inspect → explain → selectively mutate → summarize, but configuration-specific claims must be independently verified.

### starry-ai-bookmark-search
README inspected. Local-first Chrome extension with local embeddings, hybrid semantic/exact search, optional permission-gated page crawling, incremental indexing, local feedback learning, and a measured quality gate. High relevance to ASTRA/AI Operating Memory/collection search. Do not duplicate existing memory/retrieval capabilities; extract only measurable local-search/evaluation patterns after semantic dedupe.

### slack-for-ai-agents
README inspected. Agent/skill pattern for tool routing, setup verification, workspace identity pinning, preview-before-mutation, and rollback logs paired with destructive operations. High-value bounded mutation/rollback pattern. Do not import Slack-specific implementation.

### Powerful-Websites-You-Should-Know-About
README inspected. Automated YouTube Shorts discovery/transcription/vision extraction into structured CSV. Requires paid OpenAI and AssemblyAI keys in the documented setup. Useful as a pipeline pattern only; free/local replacements should be preferred.

## P1 / retained inventory
- ai-animated-website — Next.js/Tailwind/Framer Motion animated hero reference.
- jcodesmore-plugins — plugin distribution source; inspect with the dependent plugins.
- agent-recall — likely memory/recall source; requires deeper file-level inspection before extraction.
- ai-chrome-extension-template — browser extension template; relevant to browser/agent surfaces.
- discord-for-ai-agents — Discord agent integration candidate.
- orca — large source repository; requires targeted inspection rather than wholesale import.
- movies-for-ai-agents — AI-agent movie/resource source; inspect if media research becomes relevant.
- jobs-for-ai-agents — job discovery/resource source; inspect if prospecting/revenue workflows need it.
- claude-code-visualizer — visualization/observability candidate for agent workflows.
- artemis-2-arow-data — large telemetry archive/data source; retained as data/provenance reference, not agent infrastructure.
- OpenSpace-for-Artemis-II — MIT custom OpenSpace mission tracker with live/fallback telemetry pipeline and 3D visualization; useful as resilient-data-source and visualization pattern, not current revenue priority.
- .github — account profile/meta repository; retain for provenance.
- Remaining repositories are retained in the account inventory even when no immediate reusable contract was established.

## Extraction decision
New canonical Skill candidate:
COLLECTION/SKILLS/WEBSITE_REVERSE_ENGINEERING_CLONE_2026-10-07.md

Why new rather than duplicate:
Existing collection has browser, runtime-proof and verification sources, but this source provides a distinct end-to-end reverse-engineering contract centered on source-to-local route mapping, evidence-backed visual/state inspection, asset provenance, matched-state comparison, repair ordering, and production+rendered-comparison completion. It should upgrade existing verification systems rather than replace them.

No external project is copied wholesale.

## Account status
Account-wide enumeration: captured for 18 repositories returned by the current owner-scoped search.
Repository-level inspection: broad README triage completed; deep file extraction is prioritized for P0/P1 sources.
Discovery is not treated as runtime/production proof.
Historical provenance is retained.
