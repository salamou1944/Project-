# ChatGPT plugin discovery — 2026-10-21

This is a discovery snapshot from a targeted search for browser automation and development tools. It is **not a complete export of every plugin available in the marketplace**.

| Plugin | Discovery state | Potential use for our work |
|---|---|---|
| TinyFish | Enabled and available, not installed/connected | Cloud browser agent for account portals and web automation. This is the closest match to the missing browser/desktop-access path; it still requires the user to connect it. |
| OpenAI Developers | Installed | OpenAI development documentation and best practices; not an inference endpoint and does not grant API quota. |
| Vercel | Installed connector | Existing deployment metadata and project operations, but the current team-scope permission error blocks environment-variable inspection. |
| Webflow | Available, not installed | Website/CMS work; not a substitute for local machine access. |
| Zoho CRM | Available, not installed | Alternative CRM, but we already have a connected HubSpot account, so adding it now would create unnecessary duplication. |
| monday.com | Available, not installed | Project tracking/CRM; not needed while GitHub and Notion already hold the operating plan. |
| MagicPath | Available, not installed | Design/prototyping; not a runtime or inference provider. |
| Oracle Analytics / Power BI | Available, not installed | Analytics/reporting; no evidence yet that either is needed for the current blockers. |
| Databricks Genie | Disabled by administrator | Not currently available for use. |

## Decision

- Do not add more planning/design tools just because they are listed.
- TinyFish is the one relevant optional connection because the current browser connector cannot access the originating browser context and Termalin reports zero reachable hosts.
- TinyFish does not give local Ollama access or make a model free; it only offers a possible cloud-browser path after the user connects it.
- Continue independent GitHub/Render/Supabase/Notion work while that connection is pending.
