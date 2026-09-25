# Object Storage / Self-hosted Storage Expansion — 2026-09-25

Status: DISCOVERY_CAPTURED

## SeaweedFS
- URL: https://github.com/seaweedfs/seaweedfs
- License: Apache-2.0.
- Capability: distributed object storage/S3, filesystem, WebDAV and lakehouse/Iceberg/Lance table support in one system.
- Observed: single-binary quick start, Docker/Compose/Kubernetes paths, horizontal scaling and S3 compatibility.
- Important: enterprise edition exists; distinguish OSS core from enterprise features.
- Potential value: self-hosted storage for generated assets, documents, media and AI datasets.
- Verification required: exact release, security/auth defaults, backup/recovery, resource requirements and production topology.

## Garage
- URL: https://github.com/deuxfleurs-org/garage
- License: AGPLv3.
- Capability: lightweight S3-compatible distributed object storage for small/medium self-hosted geo-distributed deployments.
- Potential value: low-cost S3-compatible storage.
- Verification required: current upstream source, feature set, resource profile, replication/recovery and AGPL implications.

## MinIO
- URL: https://github.com/minio/minio
- License: AGPLv3.
- Capability: S3-compatible object storage.
- Important current-source signal: public documentation/search results report changes in development/support posture; do not treat historical MinIO assumptions as current without release verification.
- Verification required before any new adoption: current upstream activity, release/security status and exact OSS/enterprise boundary.

## Buktio
- URL: https://github.com/buktio/buktio
- Capability: self-hosted web UI/REST/CLI control plane for S3-compatible storage, with Garage as default backend.
- Potential value: easier management layer over self-hosted object storage.
- Verification required: license, backend compatibility, authentication and current maturity.

## Security note
Object storage is infrastructure, not merely a free replacement. Validate authentication, encryption, network exposure, backups, deletion/recovery, retention and credential rotation before storing production data.
