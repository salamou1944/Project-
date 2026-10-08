# Juspay Hyperswitch — verified source capture

- Source: https://github.com/juspay/hyperswitch
- Owner: juspay
- Repository: hyperswitch
- Captured: 2026-10-08
- Main revision inspected: `1d71d94d2e2e1c72f3ede13abebc24132997685f`
- License: Apache-2.0
- Language: Rust
- Status: PRESERVED / READY_FOR_DEEP_EXTRACTION

## What it provides

Hyperswitch is an open-source composable payments infrastructure stack. The official README describes:
- payment routing across 100+ processors;
- retries/revenue recovery;
- PCI-oriented vaulting;
- reconciliation;
- alternate payment methods;
- payment cost observability;
- connector abstraction;
- merchant control center;
- checkout SDKs;
- self-hosted deployment;
- modular components including Prism and a standalone Decision Engine.

The repository also documents the wider ecosystem:
- core backend;
- card vault;
- encryption service;
- Prism connector library;
- Decision Engine;
- Control Center;
- web/mobile SDKs;
- Helm and full-suite deployment tooling.

## Setup boundary

The official README provides a Docker/local setup path and explicitly separates:
- Standard: app server + Control Center;
- Full: monitoring + schedulers;
- Minimal: standalone app server.

A payment connector must then be configured and a payment tested. This is activation evidence from the upstream project, not evidence of execution in our environment.

## Reuse boundary

Do not import the entire platform into our systems.

Extract narrow reusable contracts only after semantic dedupe against:
- existing API Factory/provider adapters;
- SOAT/runtime verification;
- MONY revenue infrastructure;
- existing Lago/Kill Bill billing candidates;
- existing Collection Skills.

## Evidence

Current main commit is `1d71d94d2e2e1c72f3ede13abebc24132997685f`, with a verified GitHub commit signature. The source remains actively maintained.

## Readiness

Collection state:
- source: PRESERVED
- extraction: READY_FOR_DEEP_EXTRACTION
- runtime in our environment: NOT CLAIMED
- production: NOT PROVEN