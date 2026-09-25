# ACCOUNT / NMAP COLLECTION CAPTURE — 2026-09-25

Status: EXTRACTED_PENDING_DEEP_VERIFICATION

## Scope correction
This capture records the external GitHub account/repository sources the user explicitly asked to include in the collection, including the Nmap-related material and the previously identified account collections. It is not limited to Project-, agent-skills, or Agent-Reach.

## aw-junaid — confirmed
Profile: https://github.com/aw-junaid
The profile currently exposes 33 public repositories.

Relevant repositories inspected:
- https://github.com/aw-junaid/bug-bounty
- https://github.com/aw-junaid/Kali-Linux

### Nmap-related evidence found in bug-bounty
- resources/cheatsheets/ports.md
- resources/cheatsheets/Tomcat Security Testing.md
- resources/cheatsheets/WAFs.md
- resources/cheatsheets/Joomla.md
- tools/README.md
- tools/personal-script/readme.md
- tools/personal-script/8-Hour Challenge.md
- methodologies/web penetration/Webshell.md

The repository contains Nmap references across scanning, service/version enumeration, NSE usage, web-service discovery and methodology material. Collection must preserve the source files rather than reducing the source to a single Nmap link.

### Nmap-related evidence found in Kali-Linux
- Kali Linux Tools/Nmap.md
- Kali Linux Tools/masscan.md
- book/3.md
- book/24.md
- book/25.md
- book/26.md
- book/27.md

This source is valuable not only for Nmap itself but also for adjacent reconnaissance/scanning workflow knowledge, including masscan-to-Nmap relationships and operational notes.

## mufeedvh — confirmed
Profile: https://github.com/mufeedvh
The profile currently exposes 42 public repositories.

Relevant repository inspected:
- https://github.com/mufeedvh/code2prompt

Current repository evidence includes:
- Rust workspace structure under crates/
- file processors for CSV, TSV, JSONL, Jupyter notebooks and default text
- prompt rendering/session code
- token counting and token-map code
- agent skill files
- Python bindings
- website documentation
- active issue/PR activity

This is a high-value source for local codebase-to-prompt generation, structured file processing, token estimation, agent skills and reusable code-intelligence patterns.

## Collection rule for these account sources
1. Preserve repository + exact file path + revision/commit when extracted.
2. Treat account profile counts as discovery metadata, not as proof that every repository has been inspected.
3. Continue recursively through the identified account repositories rather than stopping at profile pages.
4. For security material, retain it as authorized defensive/research knowledge; do not operationalize it against systems without authorization.
5. Do not copy credentials, secrets, private data or unrelated personal information.

## Current evidence references
- aw-junaid profile: 33 public repositories.
- mufeedvh profile: 42 public repositories.
- Nmap material is confirmed in both aw-junaid/bug-bounty and aw-junaid/Kali-Linux.
- code2prompt currently contains substantial prompt/file-processing/token/agent-skill implementation material.

## Next extraction targets
- Complete the previously identified aw-junaid repository set, not only the two Nmap-related repositories.
- Continue the previously identified mufeedvh repository set, not only code2prompt.
- Resolve the remaining Nmap ecosystem repositories/accounts previously supplied by the user.
- Store each verified batch in Project- with provenance and status.
