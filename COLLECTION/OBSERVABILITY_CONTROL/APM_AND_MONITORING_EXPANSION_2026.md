# APM / Monitoring / Error Tracking Expansion — 2026-09-25

Status: DISCOVERY_CAPTURED

## SigNoz
- https://github.com/SigNoz/signoz
- OpenTelemetry-native observability/APM platform.
- Potential replacement family for Datadog/New Relic/AppDynamics-style telemetry.
- Verification required: current license, self-hosting resources, ClickHouse architecture, alerting and retention.

## GlitchTip
- https://github.com/GlitchTip/glitchtip
- Open-source error tracking built around Sentry-compatible workflows.
- Potential replacement for hosted error tracking where self-hosting is acceptable.
- Verification required: current license, compatibility boundaries and deployment requirements.

## Uptime Kuma
- https://github.com/louislam/uptime-kuma
- Self-hosted monitoring/uptime dashboard.
- Potential replacement for simple Pingdom/UptimeRobot-style monitoring.
- Verification required: auth, notification channels, persistence and monitoring scale.

## OpenTelemetry
- https://github.com/open-telemetry/opentelemetry-collector
- Vendor-neutral telemetry collection layer.
- Potential value: avoid coupling applications to one paid observability vendor.
- Verification required: collector deployment/security, data routing, processors and backend compatibility.

## Hypertrace
- https://github.com/hypertrace/hypertrace
- OpenTelemetry-oriented observability platform.
- Potential value: self-hosted distributed tracing/APM.
- Verification required: current maintenance, dependency footprint and production deployment.
