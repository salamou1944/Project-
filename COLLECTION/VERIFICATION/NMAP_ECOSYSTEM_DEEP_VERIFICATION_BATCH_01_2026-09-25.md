# NMAP ECOSYSTEM DEEP VERIFICATION BATCH 01 — 2026-09-25

Status: VERIFIED_EVIDENCE_CAPTURED

Source scope: nmap organization repositories. Current organization page shows exactly 7 public repositories: nmap, npcap, ncrack, libdnet, libpcap, styrene, tcpdump.

## nmap/nmap
Repository evidence: default branch master; active source mirror; C; current repository metadata shows recent commits.
Root implementation areas include docs, fuzz, libdnet-stripped, liblinear, liblua, libnetutil, libpcap, libpcre, libssh2, libz, m4, macosx, mswin32, nbase, ncat, ndiff, nping, nselib, nsock, scripts, zenmap.
README SHA: 58c58fe4af0767049ce31b3b78affc0052c5eba9.
LICENSE SHA: captured from master.
License: Nmap Public Source License 0.95. It is based on GPLv2 but adds Nmap-specific terms. The license expressly distinguishes end-user use from commercial redistribution/integration and provides OEM licensing. It also imposes specific conditions for external deployment and references Npcap's separate license.
Capability evidence: network mapping, port/service discovery, version detection, scripting ecosystem, Ncat/Nping/Ndiff/Zenmap and related libraries/tools.
Reuse boundary: do not treat as ordinary permissive OSS; review NPSL obligations for any redistribution/integration.

## nmap/npcap
Repository metadata and README/docs inspected. Windows packet capture/transmission architecture with C source, driver, installer, examples, SDK, tests and documentation.
License metadata is Other/NOASSERTION; repository README explicitly states a separate Npcap License. Free end-user installation/use is described, including up to 5 systems in the current README; OEM provides enterprise/commercial features and support. Do not classify as permissive OSS.
docs/npcap-guide.xml SHA: 60d53a6c329071f6e91a5735338db3e6cf95ea01.
Operational dependency: Windows networking stack/NDIS/WFP and signed driver installation. Documentation includes troubleshooting for driver/service/filter issues.

## nmap/ncrack
README SHA: 9692a04277c197a4359199cf06d274d5481541e9.
Capability evidence: high-speed network authentication auditing tool, modular engine, dynamic behavior, command-line syntax similar to Nmap. README lists support for SSH, RDP, FTP, Telnet, HTTP(S), WordPress, POP3(S), IMAP, CVS, SMB, VNC, SIP, Redis, PostgreSQL, MQTT, MySQL, MSSQL, MongoDB, Cassandra, WinRM, OWA, DICOM.
Security category: password/authentication auditing and dual-use network security testing. Collection only; no live unauthorized targeting.

## nmap/libdnet
Repository is a fork of ofalk/libdnet according to current organization metadata. The attempted README path returned NOT_FOUND; status remains PARTIAL/UNVERIFIED at file level. Do not infer license/capabilities beyond repository description until the actual tree/files are inspected.

## nmap/libpcap
README SHA: 4bfa6ef0ace59306d409207d29c8e10df8f28fbc.
Capability evidence: system-independent low-level packet capture API; network monitoring, security monitoring and debugging. Supports BPF filtering and multiple platform-specific capture mechanisms. README explicitly notes Linux eBPF mechanisms are not supported by libpcap itself.
Important architecture relationship: Nmap/npcap and tcpdump depend on packet-capture concepts/components; Nmap bundles/uses libpcap-related components.

## nmap/styrene
README SHA: 48a54a6081569ead5cd6fb2981bdca046c8db831.
Capability: Windows app/package bundling around MSYS2 packages. Runtime/build dependencies include MSYS2, Python, GCC, NSIS, binutils, zip and git.
License evidence: GPLv3+ for the tool; CC0 for code templates/generated code inside bundles; contributor documentation separately licensed.
Status: repository is old relative to other Nmap projects; keep as reusable packaging reference, not assume current production suitability.

## nmap/tcpdump
README SHA: 7e381e17a72004cc1ff81a2390d29c0336d1f7e0.
Repository is a fork/mirror of the Tcpdump Group source. Capability: network monitoring/data acquisition and packet dissection; uses libpcap. README contains historical trace-analysis utilities and examples, including awk processing of captures.
Cross-source relationship: tcpdump -> libpcap; nmap organization mirror -> the-tcpdump-group upstream. The upstream organization currently has its own active libpcap/tcpdump repositories.

## Cross-links discovered
- Nmap -> Npcap on Windows for packet capture/transmission.
- Nmap -> libpcap/libdnet and bundled libraries.
- tcpdump -> libpcap.
- Ncrack shares Nmap ecosystem conventions but is a separate authentication auditing tool.
- Nmap repository contains fuzzing directory and multiple networking/security subsystems.
- Nmap organization contains mirrors/forks of upstream packet-capture projects; provenance must preserve upstream origin.

## Verification boundaries
Verified here: repository existence, key source-tree areas, README/license/document evidence, and explicit capability/license statements.
Not yet verified: exhaustive file-by-file extraction of all seven repositories, build reproducibility, runtime benchmarks, complete dependency graph, complete license inventory of every embedded component, and security testing.

## Next queue
1. Deep-inspect nmap/nmap scripts, nselib, docs, fuzz and build/configuration files.
2. Inspect nmap/npcap source/driver/test/build boundaries.
3. Inspect nmap/ncrack modules and build/config.
4. Resolve nmap/libdnet file-level 404 and inspect tree.
5. Follow upstream provenance for nmap/tcpdump and nmap/libpcap.
6. Continue aw-junaid 33 repos + 76 gists and mufeedvh 42 repos.
