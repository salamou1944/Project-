# Paid SaaS Replacement Map — Discovery Capture 2026-09-25

Status: DISCOVERY_CAPTURED

This is a broad map of paid-service categories and candidate OSS/self-hosted replacements. It is intentionally not an adoption ranking.

## Discovery sources
- https://github.com/SolvoHQ/awesome-self-host-saas-alternatives
- https://github.com/open-saas-directory/awesome-saas-directory
- https://selfhosttools.com/
- https://ideaproof.io/open-source/self-hosted
- https://github.com/spinov001-art/free-developer-tools-2026

Recent 2026 discovery sources expose large replacement catalogs; one directory reports 102 actively maintained projects and another self-hosted directory reports 225 curated tools. These counts are discovery snapshots, not verification of every entry.

## Categories to recursively inspect

### Product / project management
- Linear / Jira / Trello → Plane, OpenProject, Vikunja
- Notion / Confluence → AppFlowy, AFFiNE, Outline, Wiki.js, BookStack, Documenso where applicable
- Whiteboards → Excalidraw, tldraw, Penpot

### CRM / sales / customer support
- HubSpot / Salesforce → Twenty, EspoCRM, SuiteCRM, Odoo
- Intercom / Zendesk → Chatwoot, Zammad
- Calendly → Cal.com / cal.diy
- E-signature → Documenso

### Analytics / product telemetry
- Google Analytics → Matomo, Plausible, Umami
- Amplitude / Mixpanel → PostHog, RudderStack, OpenPanel
- APM / Datadog-style observability → SigNoz, Apache SkyWalking, Hypertrace, OpenTelemetry ecosystem

### Communication / collaboration
- Slack / Teams → Mattermost, Rocket.Chat
- Zoom / meeting stack → Jitsi Meet
- Dropbox / Drive / collaboration files → Nextcloud, Seafile
- Password managers → Vaultwarden, Bitwarden self-hosting where applicable

### Developer / API
- Postman → Hoppscotch, Bruno, Yaak, HTTPie, Restfox
- GitHub/GitLab hosted workflows → Gitea, Forgejo, GitLab CE
- CI/CD → Woodpecker CI, Drone, GitLab CI, Jenkins where appropriate
- Platform-as-a-Service → Coolify, Dokku, CapRover
- Error tracking → GlitchTip, Sentry self-hosted where edition permits
- Uptime monitoring → Uptime Kuma
- Remote dev / coding → code-server, OpenVSCode Server, Coder

### Email / marketing
- Mailchimp / ConvertKit → Mautic, Listmonk, Sendy (license differs)
- Transactional email providers → Postal, Mailpit for development/testing
- Email inbox / webmail → Roundcube, SnappyMail
- Forms → Formbricks, OhMyForm, Form.io depending license/edition

### CMS / commerce
- Shopify / WooCommerce components → Medusa, Saleor, Vendure, PrestaShop
- Content / CMS → Strapi, Directus, Payload, Ghost
- Headless commerce → Medusa, Saleor, Vendure
- E-learning / LMS → Moodle, Open edX

### Databases / backend
- Firebase / Backend-as-a-Service → Appwrite, PocketBase, Parse Platform, Supabase
- Airtable → NocoDB, Baserow
- Redis cloud → Valkey, Dragonfly (license/project boundaries require verification)
- Managed Postgres → PostgreSQL + operator/self-hosted hosting
- Object storage → SeaweedFS, Garage, MinIO

### Infrastructure / networking
- Cloudflare-like functions/proxy pieces → Caddy, Traefik, HAProxy, Nginx; Cloudflare services are not one-to-one replacements.
- VPN / zero trust → Headscale, NetBird, Authentik/Authelia combinations
- Secrets → Infisical self-hosted, OpenBao
- DNS → Technitium DNS Server, AdGuard Home for applicable use cases

### Security / research
- Snyk / dependency security → Trivy, OSV-Scanner, Grype, Syft, Semgrep CE
- Secret scanning → Gitleaks, Betterleaks
- SIEM / security analytics → Wazuh, OpenSearch Security
- Network IDS → Suricata, Zeek
- Recon / research → ProjectDiscovery tools, Amass, SpiderFoot (license/activity must be checked)

## Critical licensing rule
A project can be free to download but not equivalent to an unrestricted open-source SaaS replacement. Record OSI license, source-available/fair-code status, enterprise-only features, cloud-only limits, and commercial-use restrictions separately.
