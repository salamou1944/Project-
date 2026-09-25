# DevSecOps / Security Pipeline Expansion — 2026-09-25

Status: DISCOVERY_CAPTURED

## Awesome Security Pipeline
- URL: https://github.com/rezmoss/awesome-security-pipeline
- Discovery/verification value: claims 92 metadata-verified repositories and a tested GitHub Actions recipe using Gitleaks, Semgrep CE, OSV-Scanner, Trivy, Syft and Cosign.
- The repository states its catalog was verified July 16, 2026 and methodology is public.
- Treat its tested recipe as an evidence lead, not as our own execution result.

## Gitleaks
- URL: https://github.com/gitleaks/gitleaks
- Capability: detect secrets in git repos/files/stdin; supports Docker, Go, pre-commit and GitHub Actions.
- Important current status: project README says feature-complete and future releases are security patches, with development focus shifting to Betterleaks.
- Therefore capture both Gitleaks and the Betterleaks transition as a current maintenance signal.
- Verification required: current release, Betterleaks repository, false-positive behavior and CI integration.

## Trivy
- URL: https://github.com/aquasecurity/trivy
- Capability observed: vulnerability and license scanning; can scan SBOM inputs including CycloneDX and SPDX.
- Potential value: dependency/container/SBOM security gate.
- Verification required: current license, scanner coverage, policy configuration and CI performance.

## Broader pipeline candidates surfaced by the discovery source
- Semgrep Community Edition
- OSV-Scanner
- Grype
- Syft
- Cosign
- CodeQL
These must be inspected individually before marking verified/reusable.
