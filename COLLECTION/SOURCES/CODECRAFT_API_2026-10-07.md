# CodeCraft API — 2026-10-07

Status: SOURCE_CAPTURED

Official site: https://codecraftapi.com/

CodeCraft API is documented as an OpenAI-compatible hosted AI gateway. Current official documentation exposes /v1, chat completions, streaming, models, embeddings, tool calling, vision and reasoning. The models page currently lists 33 models and states that GET /v1/models returns capabilities and pricing metadata. The pricing page currently advertises a free tier of 1M tokens/month without a card, with 60 requests/minute and chat, streaming, tools and vision.

GitHub account/organization: no official one identified from the accessible official site navigation. GitHub search results named codecraftapi were not treated as official.

Decision: KEEP IN COLLECTION; SOURCE EVIDENCE ONLY. Do not mark runtime verified until an authenticated request and /v1/models response are independently captured.

Reuse boundary: compare against Salamou-31/API Factory and existing OmniRoute-derived provider policy. Extract only narrow provider metadata/adapter patterns; do not import another gateway wholesale.
