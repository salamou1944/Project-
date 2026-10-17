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


## 2026-10-17 source refresh

- Current README revision inspected: `e0aaa43641b41a8e7cd4a2f8ffcb345a356e754b`; LICENSE remains Apache-2.0 (SHA `f13d24c3fa482d61605d600e5ac1248799bd4107`).
- README describes OpenShell 0.1.x as a stable release line with kernel-level file/system-call/network enforcement, sandbox policy, credential binding at egress, and formal verification before policy changes.
- Runtime prerequisites remain local virtualization/container infrastructure: Linux, macOS Apple Silicon, or Windows WSL2 (experimental), plus Docker/Podman/host virtualization. Kubernetes installation requires a CNI that enforces NetworkPolicy.
- OpenShell is a **sandbox/governance runtime, not a hosted deployment provider or durable database**. It cannot replace Railway/Vercel hosting by itself. It may isolate execution of generated API code if an operator-controlled host is available.
- README states anonymous operational telemetry is enabled by default and can be disabled via `OPENSHELL_TELEMETRY_ENABLED=false` or Helm config; verify the installed version's setting before using it in sensitive environments.
- No local host, Docker daemon, OpenShell gateway, or cloud sandbox was connected/verified in this pass. No sandbox was created and no code was deployed.
- Decision remains `DISCOVERY_CAPTURED`; before production adoption, run isolation/escape tests, verify network-egress and credential policies, and establish backups/updates. The repository's own disclaimer says it is provided AS IS.
