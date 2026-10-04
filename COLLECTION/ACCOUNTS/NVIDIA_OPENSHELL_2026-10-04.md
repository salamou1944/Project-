# NVIDIA/OpenShell — Collection Capture — 2026-10-04

Source: https://github.com/NVIDIA/OpenShell
Discovery reason: documented weekly star-growth momentum.
GitHub snapshot: 14,684 stars; 1,681 forks.
License: Apache-2.0.
Status: active, not archived; latest update 2026-10-04.
Runtime/deployment: local runtime for autonomous-agent sandboxes; Linux, macOS Apple Silicon, Windows WSL2 experimental; Docker/Podman/host virtualization; Kubernetes gateway deployment via Helm.
Core capabilities: kernel-level policy enforcement, sandbox isolation, network/file/process controls, formal verification of policy changes, credential binding to approved endpoints.
Dependencies: container/virtualization stack; Python/TypeScript/Go/Rust SDK options.
Paid/cloud/external: runtime is open source; underlying model/provider services can remain external. A documented first-agent path can use a free OpenRouter model.
Security/operational: security-critical infrastructure. Policy, sandbox, credentials, network and kernel assumptions must be tested before production.
Maintenance: active; stable 0.1.x release cadence documented.
Cancellation value: potentially high for replacing paid agent isolation/governance layers, subject to environment fit.
Assessment: DISCOVERY_CAPTURED — not a production security certification.
