# AWE GROUP — Codex / Manus tooling research handoff

**Status:** prepared, NOT yet launched in Codex/Manus by assistant. Requires owner to attach local ZIP and submit instructions in external runner. Current OpenCode runtime and recorder unmodified.

## Delivered to current ChatGPT conversation

- ZIP file: `AWE-MANUS-CODEX-TOOLING-HANDOFF-2026-11-12.zip` (917729 bytes)
- SHA256: `2281ac4d2d3c2d8cfba8cf226f232eda23af8ab980cb7542479c53fb5166218d`
- ZIP entries: CATALOG-ORIGINAL-4504.csv, TRIAGE-ALL-4504.csv, PRIORITY-SOURCES-38.csv, TELEGRAM-SOURCES.csv, TASK-FOR-CODEX-OR-MANUS.md, README.md, scripts/audit_links.py, MANIFEST.json.
- Original user Library source: NIVICT-Tools-Catalog-4504.csv, all 4504 rows; 1331 from iirepresent and 3173 from Радар; categories and provenance maintained, original unchanged. The original file is also already present in AWE cleanroom data/tool-catalog according to earlier import reports, but exact current host bytes not rechecked in this session.
- 38 curated priority sources, 36 official pages located/reviewed through current web research; do NOT equate this with an exhaustive HTTP audit, installation, license or runtime test for all 4504 links.
- Public Telegram previews confirmed for @iirepresent, @neural, @vami_eventbot. @c_research and @otklicker_bot not web-verifiable in the review, retained as candidates.
- Source pages include official MCP Registry, Playwright MCP, browser-use, LiteLLM, Langfuse, n8n, Composio, Ollama, OpenClaw, Hermes, Eigent, HeadHunter API, Tavily, etc.

## Proposed task for Codex/Manus

1. Preserve full original catalog, deduplicate links without removing original records; extract description URLs and Telegram-source attribution.
2. Online-verify all links in controlled batches, record HTTP status, canonical URL/redirects, license, costs, dependencies, official docs/install, security, release health, WSL compatibility. Unknown remains unknown; 403/429 is not DEAD.
3. Prioritize integration for current AWE gaps (HH API, web search & verify, browser, MCP, model routing, memory, independent QA, observability, tool registry). Choose 1-2 tools per capability.
4. Independently build and run 8-12 isolated PoCs with reproducible evidence and safe credentials. Stage 3-5 adapters in a separate worktree/PR, no direct modification to running OpenCode cleanroom, Recorder, or keys.
5. Deliver audited full CSV, P0 shortlist, free-vs-paid/license report, Telegram list, setup playbooks, proof files, PR, owner actions and report.

## Owner's authorization boundary

- Existing Router.Cheap paid calls unrestricted for necessary testing under existing key limits. Free tools may be independently tested and installed into isolation. New paid add-ons/subscriptions/hosting require specific owner approval; never expose secrets. HH external application submission requires authorized account/access and agreed rules.

The file ZIP link exists in the generating ChatGPT conversation. This GitHub note is an audit/handoff index, not the attachment itself, and must not be mistaken for the full 4504 catalog.
