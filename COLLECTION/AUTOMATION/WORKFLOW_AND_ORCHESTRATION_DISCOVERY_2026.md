# Workflow / Automation / Orchestration Discovery — 2026-09-25

Status: DISCOVERY_CAPTURED

## Candidate families to inspect recursively
- n8n — https://github.com/n8n-io/n8n
- Activepieces — https://github.com/activepieces/activepieces
- Windmill — https://github.com/windmill-labs/windmill
- Temporal — https://github.com/temporalio/temporal
- Apache Airflow — https://github.com/apache/airflow
- Dagster — https://github.com/dagster-io/dagster
- Kestra — https://github.com/kestra-io/kestra
- Huginn — https://github.com/huginn/huginn

## Collection focus
For each candidate inspect:
- OSS/core license versus enterprise/cloud features
- local/self-hosted deployment
- webhook/API/queue/event capabilities
- retries, idempotency, scheduling and durable execution
- secrets/authentication
- observability and audit
- worker/scaling model
- resource footprint
- limits that force paid cloud usage

## Why this batch matters
Workflow engines can replace recurring automation SaaS and provide durable execution primitives for acquisition, research, deployment, collection and agent orchestration without coupling those flows to one hosted vendor.
