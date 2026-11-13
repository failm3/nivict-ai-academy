# R1-01 — Candidate service and capability queue

**Status:** sourced candidate inventory, NOT installed/connected/approved. No releases, tokens, keys, pricing or environments verified here. This queue specifically reuses the previously recorded [4504-candidate first-pass screening](../../02%20-%20%D0%90%D1%83%D0%B4%D0%B8%D1%82%204504%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2.md), rather than claiming a new mass audit.

## Market-first shortlist (official APIs documented, local integration NOT TESTED)

| Reuse option | Why prioritize | Operational caution |
|---|---|---|
| [Mastra ToolSearchProcessor](https://mastra.ai/blog/introducing-tool-search-processor), [MCPClient](https://mastra.ai/docs/connections/mcp), [HITL](https://mastra.ai/docs/agents/human-in-the-loop) | Native to existing framework, likely avoids custom discovery/approval engine | Requires compatible local package and **already authorized tools**; no unrestricted allTools |
| [Composio Mastra adapter](https://docs.composio.dev/docs/providers/mastra) | Prebuilt OAuth/session/tool routing for apps with TypeScript provider | Cloud vendor, user-scoped auth/cost/privacy and live availability to check |
| [Pipedream Connect](https://pipedream.com/connect) | Alternative managed OAuth/API/MCP with existing app connectors | Cloud dependence and source-available license; compare with Composio on the **same** task |
| [Arcade](https://docs.arcade.dev/en/home) | Additional actions/OAuth/policy provider | Only if first two show gaps; avoid duplicate providers |
| [Stacklok ToolHive](https://docs.stacklok.com/toolhive) | Optional self-hosted MCP management and isolation | Evaluate against existing R0 sandbox first; don't deploy a second tool registry |

[Source-backed independent R1 reuse research](../RESEARCH/MARKET-REUSE-AUDIT-2026-11-13.md).

## First: check native runtime functionality

| Capability | Existing source to audit | Readiness evidence needed |
|---|---|---|
| `filesystem.workspace_read/write` | existing Nox file tools in local Mastra/TS | scoped path and symlink rejection, real artifact hash, cancel |
| `shell.test_runner` | existing shell tool, R0 sandbox improvements | child process kill, bounded commands, resource limits, no arbitrary host access |
| `browser.screenshot` | existing Playwright/Chromium in NIVICT mission | real desktop/mobile screenshot, no unrestricted host file access |
| `http.public_read` | existing web/fetch/browser | SSRF/network boundary, citations/provenance, output truncation |
| `tool_catalog.search` | TI `ti_search`, Manus `manus_search`, PG API | real search, source version, candidate state, no implicit grant |

## Third-party candidates already present in 4504 screening

| Candidate (historical ID) | Intended role | Selection reason | Current verdict |
|---|---|---|---|
| [ToolHive](https://github.com/stacklok/toolhive) — Радар-2978 | MCP workload isolation / catalogue | Evaluate as adapter/sandbox helper; avoid duplicating existing TI | CANDIDATE_NOT_TESTED |
| [MCP Inspector](https://github.com/modelcontextprotocol/inspector) — Радар-1349 | MCP interface smoke/evidence | Test real server handshake/schema/invoke in isolation | CANDIDATE_NOT_TESTED |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) — Радар-3084 | Browser actions and screenshots | Reuse if existing browser tooling insufficient | CANDIDATE_NOT_TESTED |
| [Context7](https://github.com/upstash/context7) — Радар-3106 | Up-to-date version-specific docs | Read-only knowledge/tool documentation provider | CANDIDATE_NOT_TESTED |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) — Радар-1491 | Browser debugging/performance | Optional complement to one existing browser executor | CANDIDATE_NOT_TESTED |
| [Trivy](https://github.com/aquasecurity/trivy) — Радар-0766 | Dependency/config security | Secondary QA scanner, not a mission planner | CANDIDATE_NOT_TESTED |
| [GitHub MCP Server](https://github.com/github/github-mcp-server) — Радар-3090 | Read repo/PR metadata | Scope to read-only initially; avoid unnecessary credentials | CANDIDATE_NOT_TESTED |
| [Supermemory](https://github.com/supermemoryai/supermemory) — iirepresent-0059 | Memory/semantic retrieval | Candidate for R1-02, **not execution gateway** | CANDIDATE_NOT_TESTED |

**Separate domain skill, not an executable tool by default:** [Unslop Skill](https://github.com/0design/unslop-skill) → R1-04 professional pack / QA; audit behavior, license and version in isolation.

## Entry checklist for any candidate

- [ ] Actual repo/package URL/maintainer/license/version/digest checked
- [ ] Install scope and blast radius bounded; no changes to R0
- [ ] Why native Mastra/Nox/TI feature not enough documented
- [ ] MCP/API/CLI protocol and complete input/output schemas verified
- [ ] Auth and secrets method least-privilege; no token copied into prompt
- [ ] Compatibility with WSL2/Node/TS checked on isolated environment
- [ ] Sandbox policy, abort, timeouts and resource limits verified
- [ ] Real smoke invocation evidence with receipt, test ID, artifact hash
- [ ] Negative test and independent QA verdict
- [ ] Owner authorizes any new install, external side effect and budget

Do not fill the checklist merely from GitHub README descriptions. After R0 acceptance, OpenCode/Nox engineer should produce real inventory table with versions, environment IDs and PASS/FAIL proofs, then choose minimal tool set.
