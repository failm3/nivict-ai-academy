# Nox — inventory of actually present capabilities before R1 market selection

**Date 2026-11-13.** **Nature:** read-only source audit from OpenCode Session Recorder, **not** runtime test or final integrated R0 release certification. Owner correction: **verify existing code first, then suggest external integrations**. No installations, secrets, live API calls, changes to OpenCode or R0. Distinguish `DEFINED` (code exists), `USED_IN_MISSION` (actual call evidence), `PASS_ISOLATED`, `INTEGRATED_QA_PASS`, `NOT_VERIFIED`.

## Access boundary

Actual working copy is **local** `/home/nox/awe-group-cleanroom-20261112`. Remote `failm3/awe-group-runtime` main is a **different, older, exported baseline**, and it does not contain the active cleanroom `src/` tree. The evidence below is from recorder's actual `read` tool outputs, not a direct current filesystem mount. At 03:15 UTC 2026-11-13, the primary OpenCode integrator was still editing `src/agents/mission-manager.ts`; **do not treat this report as an R0 release snapshot or verified final SHA**.

## Exact Nox package dependencies confirmed

Read of local `package.json` at **02:49:07 UTC**, recorded in [02-49/part0000.txt](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/02-49/part0000.txt):

- `@mastra/core: 1.82.0` — already direct dependency. **Do NOT propose installing Mastra as a new framework.**
- `@mastra/mcp: 2.8.0` — existing MCP client integration.
- `@mastra/memory: 1.41.0` and `@mastra/libsql: 1.29.0` — existing packages for memory/storage.
- `@playwright/test: 1.49.1`, `@ai-sdk/openai: 4.0.115`, Node/TypeScript/tsx, Express, Zod.
- `npm run typecheck`, `npm test`, `npm run build` scripts already exist.
Package pin is direct source evidence; it is not on its own proof that every package/API call works at runtime.

## Component inventory — source-backed

| Component | Local source anchor / evidence | Confirmed state | Actual gap |
|---|---|---|---|
| **Mastra framework** | `package.json`, `src/agents/head-agent.ts` imports `@mastra/core/agent`; `src/tools/index.ts` imports `@mastra/core/tools` | **ALREADY IN USE** | Confirm precise API usage & compatibility of any suggested newer feature |
| **Prompt Master** | `src/api/server.ts:14,98-126`: `createSpecification(request)`, `/specify`, saved mission `pending_approval`; `src/index.ts:56-90`: CLI calls same function | **IMPLEMENTED ENTRYPOINT + CALL PATH**; not mere drawing | No demonstrated independent PM-01 dialog/oracle acceptance. CLI one-shot builds `approved` mission immediately: check approval behavior before production |
| **Head** | `src/agents/head-agent.ts:38-90,93+`: actual `new Agent`, `planMission`, JSON delegation contract | **IMPLEMENTED CODE** | Breadth and full autonomy in live work not release certified |
| **Dynamic Agent Factory (partial)** | `src/agents/specialists.ts:141-185`: `createSpecialist`, `new Agent`, role instructions, model selection, task context, selected tools | **IMPLEMENTED CODE** | Does not prove robust general factory/multi-domain orchestration |
| **Recursive delegation** | `src/agents/recursion.ts`: `runDelegateCall`, depth/children/max concurrency and duplication prevention | **IMPLEMENTED CODE** | Real deep production delegation not release accepted |
| **Mission Manager** | `src/agents/mission-manager.ts`; CLI run and resume; API approve/cancel; R0 modifications current | **IMPLEMENTED + R0 HARDENING** | Cancellation/CAS/lease/replay/independent gate still under R0 acceptance |
| **File/Shell/HTTP/Search tools** | `src/tools/index.ts:134-602`: `shell`, `file_read/write/list`, `web_fetch/search/extract`, `save_artifact` | **IMPLEMENTED Mastra createTool()** | Per-agent permission enforcement and actual smoke must be tested after R0 |
| **Playwright MCP** | `src/config/mcp.ts:115-215`: `MCPClient`, lazy singleton, stdio `npx @playwright/mcp`, tool discovery; `src/tools/browser.ts` wrapper | **ALREADY CONNECTOR CODE**, evidence of actual browser screenshot on earlier NIVICT mission | More general vendor-neutral MCP registry, external accounts and approvals not proven |
| **Tool Intelligence** | `src/tools/ti-search.ts`; `src/tools/manus-search.ts` using approved/read-only catalog APIs | **CATALOG SEARCH CODE** | Search results not approved connected/invoked adapters |
| **Tool grants (R0)** | `src/security/tool-context.ts`, `src/agents/specialists.ts:145-150`: deny unknown/ungranted names, no allTools fallback | **DEFINED / isolated negative security 4/4 PASS** | Durable per-mission capability grant, revocation and external identity not release tested |
| **Memory** | `@mastra/memory`, `@mastra/libsql` in package, `head-agent.ts:6,90` imports/uses `createAgentMemory` | **MEMORY ADAPTER PRESENT** | Cross-project ACL, trusted knowledge ingestion, source citations and long-term outcome not independently verified |
| **Independent QA** | `src/agents/qa-agent.ts`, `qa-gate.ts`, offline tests, prior NIVICT 13/14 PASS/overall FAIL | **IMPLEMENTED + UNDER R0 HARDENING** | Final mandatory release QA, verified artifact integrity for every result |
| **ToolSearchProcessor** | Version supports it in vendor docs; **no confirmed import, configuration or runtime invocation in inspected local source** | **AVAILABLE IN LIBRARY IS NOT SAME AS WIRED IN NOX** | Check installed package APIs and existing tool registries before suggesting a new broker |
| **SkillSearchProcessor** | Vendor docs describe it; **no confirmed usage in current local modules** | **NOT_VERIFIED AS CONFIGURED** | Inventory local skills, loader, role packs first |
| **Composio/Pipedream/ToolHive/Arcade** | Market candidates, no current source proof | **NOT VERIFIED / MAY BE UNNECESSARY** | Only compare after precise missing external actions proven |

Main source recordings:
- [02:49 direct local package read](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/02-49/part0000.txt)
- [02:51 specialists/recursion/README direct source reads](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/02-51/part0000.txt)
- [02:54 tools, MCP, API, CLI direct source reads](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/02-54/part0000.txt)
- [03:03 Head direct source read](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/03-03/part0000.txt)
- [03:15 active R0 edits](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/03-15/part0000.txt)

## Corrected Build/Buy stance

1. **Do not install or “introduce” Mastra, @mastra/mcp, Playwright MCP, memory/libsql, custom Agent Factory, Prompt Master or tools that are already in Nox code**.
2. **First measure actual gaps**: dynamic selection of *already granted tools*, central approval for each action, reconnect and healthcheck across multiple MCP servers, external OAuth/account isolation, source-backed knowledge ingestion, versioned skills/packs, independent QA integration.
3. Attempt **native configuration** of existing @mastra packages and current adapters before selecting Composio, Pipedream, ToolHive, new memory or another framework. Mastra ToolSearchProcessor (docs mention >= 1.58) may be compatible with 1.82, **but a version number is not an executed test**.
4. Explain real remaining gap with `EXISTS_IN_SOURCE / ACTUAL_LIVE_CALL / GAP / RECOMMENDED_ACTION / REQUIRED_TEST` per module. Only then request owner approval for installation/new dependencies/paid evaluation.
5. **Prompt Master disambiguation:** owner said “Master”; both Mastra (framework) and Prompt Master (application function) have source evidence. They must not be called absent; strict PM acceptance remains NOT_VERIFIED.
6. Do not infer zero provider costs from recorder's `cost:0` metadata. Do not claim R0 complete or restart it.

## Next recommended controlled investigation (after R0 acceptance)

- Have OpenCode generate a direct source/import inventory of the final R0 SHA and use `rg` for: `ToolSearchProcessor`, `SkillSearchProcessor`, `MCPClient`, `requireToolApproval`, `requireApproval`, `createSpecification`, `createSpecialist`, `runDelegateCall`, `createAgentMemory` and actual tool/grant paths.
- Confirm packages from lockfile/node_modules and tested API signatures, not only package.json; record whether built-in functionality is `EXISTS_NOT_WIRED` versus `NO_NATIVE_SUPPORT`.
- Produce first minimal one-capability smoke with deny/no-grant and real receipt, then reconsider vendor integrations **only if a measurable gap remains**.

**No R1 implementation authorization is implied.**
