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

## Additional search results

A second search for local-computer coding and remote shell tools surfaced Replit and Figma as already installed, plus Context7, Superpowers, Webflow, MagicPath, and ThoughtSpot as available but not installed. A search for SSH/terminal access did not surface a currently available remote-shell plugin; dbt, Snowflake, and Metabase appeared disabled by administrator. These are search results, not a complete marketplace export.

Replit can build and host app projects through its connected service, but it is not evidence of access to the user's local Windows machine. Figma is connected with a Starter/View seat; its account metadata says Code Layers and Specs are disabled. TinyFish remains the most relevant optional cloud-browser route discovered so far.

## OpenAI account clarification — official policy checked 2026-10-21

- Codex is included across ChatGPT plans, including Free and Go, but usage is limited by plan. **Codex Cloud is not included with Free or Go**; see the [OpenAI Help Center](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan).
- ChatGPT subscription billing and API Platform billing are separate; a ChatGPT account does not automatically provide free API credits or an API key. See [OpenAI's billing guidance](https://help.openai.com/en/articles/9039756-managing-billing-settings-on-chatgpt-web-and-platform).
- Practical consequence: ChatGPT/Codex can help with coding within its own usage limits, but it is not a free always-on provider endpoint for API Factory. Using the local Codex CLI would require a reachable user machine or an authorized execution environment; the current local bridge is queued and Termalin has zero reachable hosts.
