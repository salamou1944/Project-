# ACCOUNT DEEP EXTRACTION — aw-junaid + mufeedvh BATCH 02 — 2026-09-25

Status: EXTRACTED_PENDING_DEEP_VERIFICATION
Scope: repository-level metadata and source identity for the next account batch.

## aw-junaid

### aw-junaid/self-hostable-services
- Public, non-fork, default branch main.
- GPL-3.0.
- Description: self-hostable network services and web apps, with setup guides and Docker support.
- Topics include Docker, email, monitoring, proxy, self-hosted, VPN.
- Collection value: strong candidate index for subscription-elimination research.
- Reuse status: discovery/extracted; individual service licenses and deployment details still require inspection.

### aw-junaid/Security-and-Hacking
- Public, non-fork, default branch main.
- GPL-3.0.
- Description covers security testing, vulnerability scanning and hands-on security labs.
- Collection value: security research patterns and tool inventory.
- Handling: source/research material only; no live-target operation.

### aw-junaid/Machine-Learning-For-Security
- Public, non-fork, default branch main.
- GPL-3.0.
- Description covers ML for security, anomaly detection, malware classification and threat prediction.
- Collection value: security/ML research patterns and dataset/model references.
- Reuse status: repository-level evidence only.

### aw-junaid/eBPF-in-Security
- Public, non-fork.
- Description covers eBPF security monitoring, detection and kernel-level tracing.
- Collection value: host/kernel observability and security research.
- Reuse status: repository-level extraction; source files and license boundaries remain queued.

## mufeedvh

### mufeedvh/moonwalk
- Public, non-fork, default branch master.
- MIT license.
- Rust project with security-tool topics and a large fork network.
- Collection value: Rust security tooling and implementation patterns.
- Reuse status: repository-level extraction; inspect source before any reuse.

### mufeedvh/pdfrip
- Public, non-fork, default branch main.
- MIT license.
- Rust utility for PDF password recovery.
- Collection value: document-security research and Rust CLI patterns.
- Handling: research/source material; no unauthorized credential recovery.

### mufeedvh/basecrack
- Public, non-fork, default branch master.
- MIT license.
- Python utility for decoding base-encoded data.
- Collection value: reusable decoding/CLI implementation patterns.
- Reuse status: repository-level extraction.

### mufeedvh/seclip
- Public, non-fork, default branch main.
- MIT license.
- Rust CLI for protected clipboard handling of secrets.
- Collection value: local secret-handling and privacy patterns.
- Reuse status: repository-level extraction.

## Account inventory snapshot

aw-junaid: 33 public repositories currently returned by the GitHub repository search.
mufeedvh: 42 public repositories currently returned.
Nmap: 7 public repositories currently returned.

Previously extracted repositories are not reclassified as new identities. This batch adds only repositories not present in the prior dedicated extraction batch.

## Next
- Continue aw-junaid repositories and public gists.
- Continue mufeedvh repositories.
- Deep-inspect high-value source trees rather than treating metadata as verification.
- Keep one canonical source identity per upstream repository and preserve cross-references.
