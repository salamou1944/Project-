# Agent Reach — Captured Source Map

Status: DEEP_INSPECTED
Captured: 2026-09-25
Source: https://github.com/Panniantong/Agent-Reach
Revision observed: main @ a19a171fa980a0785849596492e0af4db800c82f

## Why this source matters
Agent Reach is an orchestration/selection layer around upstream internet-access tools rather than a single web-scraping engine. Its docs describe free/open-source routes for web reading, GitHub, YouTube, RSS, Reddit, Bilibili and optional authenticated channels, with health checking via `agent-reach doctor`. citeturn0search1

## Documentation tree captured
- docs/README_en.md — SHA `b15b3ce6a807af6980202c09a00b6d197f0a6ded`
- docs/install.md — SHA `91ca53f8a1cbeff4da75dda3687f7dd8d958d523`
- docs/troubleshooting.md — SHA `e89bb474637af510c230080a3f898f5effa77249`
- docs/update.md — SHA `2ef00bb90690e54faaff4e138ffbde5e8119e56f`
- docs/cookie-export.md — SHA `5f7fb98cb2c941720bf9ac5844022fbdb9ce608d`
- docs/dependency-locking.md — SHA `23a3fdb4cb0c75cc8f6199a38946d2f042019088`
- docs/README_ja.md — SHA `aea5aa8b4a44c44c04293fce4fe43967b8e7a976`
- docs/README_ko.md — SHA `56ef7ff663463badd8cb31e85c824fb8eed666be`

## High-value implementation observations
1. Safe default: install checks dependencies without system changes; system installation requires explicit approval.
2. Agent Reach keeps its files under `~/.agent-reach/` rather than polluting a project workspace.
3. It delegates to upstream tools such as `gh`, `yt-dlp`, `feedparser`, Jina Reader, `rdt-cli`, `bili`, OpenCLI and mcporter instead of pretending to replace them.
4. `doctor` is a useful health/evidence gate: channel availability is checked and failures are surfaced rather than treated as success.
5. Authenticated channels have explicit credential/cookie boundaries; credentials should not be collected into the research repository.
6. Some channels are not zero-cost in every deployment: the docs explicitly distinguish local/free paths from optional proxy or free-key requirements.

## Reusable patterns for our projects
- Capability router + upstream adapters
- Health/diagnostic command as a runtime evidence gate
- Per-channel fallback backends
- Explicit distinction between zero-config, user-authenticated, and externally dependent capabilities
- Keep credentials outside source-collection storage
- Pin important upstream versions/commits where reproducibility matters

## Fresh verification evidence — 2026-09-25
- `pyproject.toml` at observed revision declares version `1.5.0`, Python `>=3.10`, and MIT license.
- `docs/README_en.md`, `docs/install.md`, `docs/troubleshooting.md`, `docs/update.md`, `docs/cookie-export.md`, `agent_reach/core.py`, `agent_reach/doctor.py`, `agent_reach/config.py`, `agent_reach/skill/SKILL_en.md`, `tests/test_channel_contracts.py`, `tests/test_skill_command.py`, `llms.txt`, `CLAUDE.md`, and `CHANGELOG.md` were directly inspected.
- The inspected implementation exposes `doctor()` through the core API and a diagnostic engine that aggregates per-channel checks.
- The inspected docs distinguish zero-config channels from cookie/authenticated or externally dependent channels; therefore `one install, zero API fees` is not equivalent to zero external operating cost for every channel.
- Adapter discovery is explicitly not proof that authentication or target-content access works.

## Verification status
DEEP_INSPECTED. This is source/documentation verification, not a claim that the repository was executed in this ChatGPT runtime or that every channel was independently tested.

