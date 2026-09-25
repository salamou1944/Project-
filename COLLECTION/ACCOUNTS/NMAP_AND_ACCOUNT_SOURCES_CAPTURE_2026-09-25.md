# ACCOUNT / NMAP COLLECTION CAPTURE — 2026-09-25

Status: EXTRACTED_PENDING_DEEP_VERIFICATION

## Scope correction
This capture records the external GitHub account/repository sources included in COLLECTION, including Nmap-related material and previously identified account collections. It is not limited to Project-, agent-skills, or Agent-Reach.

## aw-junaid
Profile exposes 33 public repositories and 76 public gists in the current public profile views.

Priority repositories already inspected:
- aw-junaid/bug-bounty
- aw-junaid/Kali-Linux

Nmap/security evidence found across the two repositories includes Nmap, masscan, NSE references, web-service enumeration, scanning methodology, and security-testing material. Preserve exact source paths and revisions when extracting.

Gists are now explicitly part of the discovery queue. Public profile evidence shows 76 gists; examples include XSS, computer networking, algorithms/data structures, assembly language and other technical/security material. Gists must be inventoried before the account is considered exhausted.

## mufeedvh
Profile exposes 42 public repositories in the current public profile view.

Priority repository already inspected:
- mufeedvh/code2prompt

code2prompt evidence includes Rust workspace code, file processors, prompt/session rendering, token maps/counting, Python bindings, website documentation, and agent skill files. Continue across the remaining repositories.

## Nmap ecosystem
The official nmap organization currently exposes 7 public repositories:
- nmap/nmap
- nmap/npcap
- nmap/ncrack
- nmap/libdnet
- nmap/libpcap
- nmap/styrene
- nmap/tcpdump

Repository-level inspection must proceed beyond profile metadata. Current web evidence confirms nmap/ncrack and nmap/npcap have substantial source trees and active/current documentation; this is discovery evidence until source-level extraction is performed.

## Collection state rules
discovered -> inspected -> extracted -> verified -> reusable

Account profile counts are discovery metadata, not proof of repository/file completion.
README/marketing/awesome-list evidence is not sufficient for production-readiness, security, licensing, or feature-parity claims.

## Security boundary
Security and dual-use tools may be collected as authorized research/defensive source material. Do not operationalize unauthorized intrusion, credential theft, malware deployment, or exploitation.

## Remaining account extraction queue
1. aw-junaid: inventory and process all 33 repositories.
2. aw-junaid: inventory and process all 76 public gists.
3. mufeedvh: inventory and process all 42 repositories.
4. nmap organization: process all 7 repositories.
5. Preserve provenance for every extracted batch in Project-.
6. Cross-link overlapping tools, implementations, dependencies, licenses and replacement opportunities.
