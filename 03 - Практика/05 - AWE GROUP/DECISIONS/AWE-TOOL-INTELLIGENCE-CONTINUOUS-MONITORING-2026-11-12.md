# AWE Tool Intelligence — approved continuous mode and proposed source classes

Date: 2026-11-12
Status: **Owner-approved scope**: continuously maintained catalogue sourced from at least two owner-supplied Telegram channels plus discovered sources; agents Codex and Manus should research, implement source collectors and incremental updates into structured DB. Detailed technical decisions below are recommendations, not yet final owner signoff.

## Owner request
- Discuss acceptable source types and source formats.
- Give Codex/Manus one research/build assignment combining historical full backfill, discovery of similar channels, extraction and validation of all tools, and an ongoing "bot" to ingest updates into DB.
- Distinguish paid and free; allow OpenCode to independently connect free tools after verification, and get owner approval before purchasing new external paid services. Router.Cheap already authorized paid API usage.
- Start anew with modern verified dataset, preserve 4504 old entries only as historical comparison, not as source of assumed truth.
- Review/discuss before drafting final prompt. At least two Telegram channel URLs to be supplied.

## Proposed classes
- A: official upstream canonical repos, documentation, source control release feeds, MCP Registry, Hugging Face Hub, package registries, official pricing.
- B: discovery, seed Telegram channels, discovered similar channels, forums/social media, newsletters, YouTube.
- C: curated indexes, awesome lists, third-party aggregators, archives and legacy 4504 file.
- Source registration: type, canonical ID/URL, trust tier, collection method, auth, update schedule, last cursor, accessibility, source approval status, terms and provenance.
- Persistent capture: Telegram MTProto user client (separate authorized account) for public and accessible history; Bot API for channels where bot is added and new-post updates. Bot API update backlog ≤24h, not a general arbitrary-channel historical archive. Sources should be permitted, no bypass.
- Lifecycle: discover -> staged/provenance -> deduplicate -> verify against primary source -> pricing/license/compatibility -> reviewed -> approved for AWE -> integrated/tested. Independent status per tool; never install scripts straight from third-party post.
- Storage proposal: isolated collector and PostgreSQL staging tables with immutable raw records, normalized resources, references, test results and pricing history; JSONL export with schema version; API/MCP integration boundary for OpenCode. Avoid concurrent writes to live cleanroom or existing AWE core DB.
- Initial backfill then incremental workers, retry/checkpoints/dedup, edit/delete checks, periodic official upstream revalidation, health metrics and lag.
- Telegram channels must be provided before active ingestion setup. No external purchases.
- Responsibilities: Manus discovery/source research; Codex data pipeline, connectors, DB/validation, health checks, integration contract; OpenCode consumes vetted catalog without interrupting existing AWE mission.

## Verified official technical references
- https://core.telegram.org/bots/api — channel_post, edited_channel_post, getUpdates/webhook, updates retained for up to 24h
- https://core.telegram.org/bots/faq — a bot receives channel messages only if member
- https://docs.telethon.dev/en/stable/modules/client.html — iter_messages for available history and rate-limit considerations
- https://docs.github.com/en/rest/activity/events — polling ETag and interval, limited event history
- https://huggingface.co/docs/hub/en/api — model/dataset/space APIs
