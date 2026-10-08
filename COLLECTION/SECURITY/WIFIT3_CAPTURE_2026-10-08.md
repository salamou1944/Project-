# wifit3 — Collection Capture

- Source: https://github.com/derv82/wifit3
- Repository: derv82/wifit3
- Captured: 2026-10-08
- Category: SECURITY / WIRELESS / NETWORK AUDIT
- License: GPL-2.0 for code; firmware/vendor blobs retain their respective licenses.
- Status: High-value technical asset; retain as a reusable reference/project candidate, not as an automatic production dependency.

## What it is

wifit3 is a standalone USB Wi-Fi auditing application for Linux, Windows, and macOS. It uses a user-space wireless stack and USB adapters rather than relying on the operating system's native Wi-Fi stack.

## Relevant capabilities

- Cross-platform USB Wi-Fi reconnaissance and auditing.
- Multi-adapter aggregation and channel scanning across 2.4 GHz / 5 GHz.
- Signal/encryption/WPA3 transition analysis.
- Access-point and client identification, including vendor/device categorization.
- Hidden-network/VAP decloaking analysis.
- Real-time packet/activity dashboard.
- PCAP/capture workflows and wireless-security assessment features.
- Built-in user-space driver ports for supported USB chipsets.
- Hardware support spanning Atheros, MediaTek, Realtek and Ralink USB adapters.
- Standalone binaries for Windows, Linux and macOS.

## Why it belongs in COLLECTION

1. Strong reusable wireless-security/audit capability.
2. Cross-platform implementation is unusually valuable for future security tooling.
3. User-space USB driver architecture can serve as an engineering reference for hardware-facing agents/tools.
4. The project is actively evolving and has a substantial contributor/PR stream.
5. It can become a building block or reference for authorized network-audit products, lab tooling, device inventory, and wireless observability.

## Current maturity signal

The repository has substantial history and recent releases. The latest listed release is v0.4.1 (BETA), and active pull requests in October 2026 include improvements around decloaking, cross-card deduplication/radio lifecycle, and additional driver support.

## Reuse / legal constraints

- Do not treat GPL-2.0 code as freely relicensable into proprietary products; preserve GPL obligations when redistributing derivative code.
- Firmware blobs have separate manufacturer licensing terms.
- Use only on networks/equipment owned by the operator or where explicit authorization exists.
- COLLECTION stores this as an asset/reference; no assumption is made that every offensive/audit feature should be exposed as an unrestricted automated capability.

## Suggested future extraction

Potential safe capability families for later review:
- wireless asset discovery
- AP/client inventory
- wireless telemetry and observability
- hardware/USB adapter detection
- PCAP acquisition and analysis
- authorized wireless-security audit workflows
- cross-platform USB driver abstraction

Source verification: GitHub repository README, release history, and current pull-request activity checked 2026-10-08.
