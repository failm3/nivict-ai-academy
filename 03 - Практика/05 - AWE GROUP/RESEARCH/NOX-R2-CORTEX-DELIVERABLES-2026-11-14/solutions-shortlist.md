# Nox R2 — ranked actionable shortlist

**Recommendation:** do not add a platform. First repair/bound the existing candidate and QA lifecycle (G0), then prove the already-installed Mastra `ToolSearchProcessor` at `1.82.0` over only granted tools (G1). The first external acquisition should be one exact, read-only, owner-approved adapter; Playwright MCP is the most concrete candidate, but its live Nox compatibility is UNKNOWN. Knowledge, evaluation and managed-account components follow only behind real mission needs.

**Evidence boundary:** all options below are research L1/L2. Nothing was installed, called, paid for, or accepted in Nox. Current Nox HEAD/source/config is UNKNOWN; module names refer to historical baseline `68cc0ee20a25991ea275512e20ac521cc8f8234b`. Rank is expected integration leverage under REUSE FIRST, not measured quality uplift.

## Fastest safe integration path

| Rank | Decision | Exact starting point | Why now | Evidence |
|---:|---|---|---|---|
| 1 | **Reuse and harden Nox G0; no dependency** | `src/tools/index.ts`, `src/utils/storage.ts`, `src/security/tool-context.ts`, `src/agents/{mission-manager,lifecycle,qa-agent,web-qa}.ts` | Existing finite oracles/lifecycle are closer than any replacement; root identity, candidate race and exhausted-resume behavior block trustworthy acceptance. | Historical bounded A; current UNKNOWN |
| 2 | **Configure native ToolSearch at the existing pin** | `@mastra/core=1.82.0`; `src/agents/specialists.ts` → existing `runWithToolContext`/grant checks | No new package or orchestrator; directly addresses large static tool context without expanding grants. | B, L2; no Nox test |
| 3 | **One pinned browser MCP adapter, only if a real browser mission requires it** | `@playwright/mcp=0.0.85` is the observed npm snapshot, not an automatic selected version; `src/config/mcp.ts`, `src/tools/browser.ts` | Existing MCP seam. Pinning removes the current unpinned bootstrap; independent browser oracle already exists but needs epoch binding. | D, L2; live UNKNOWN |
| 4 | **One bounded Docling ingestion adapter** | Observed PyPI `docling=2.150.0`; `src/tools/` + immutable KnowledgeRecords in `src/memory/` | Source-backed professional knowledge is the next distinct gap; can be evaluated on local documents without a new vector DB. | D, L2; quality UNKNOWN |
| 5 | **One read-only official Skill source** | `anthropics/skills` exact path/blob SHA; Mastra Workspace/SkillSearch at baseline | Reuses portable instructions/resources and native loading; no autonomous script execution. | B/D, L2; transfer UNKNOWN |
| 6 | **Promptfoo as external hidden-fixture harness, not production QA** | Observed npm `0.125.1`; independent host test directory | Small measurable evaluation layer for T02/T05/T11; Nox retains lifecycle and final acceptance. | D, L2; uplift UNKNOWN |
| 7 | **MCP Registry only as quarantined candidate metadata** | Official registry snapshot/API; `ti-search.ts`/`manus-search.ts` | Extends discovery without making registry entries executable or trusted. | C for metadata only |
| 8 | **MCP Inspector only in an isolated test harness** | Observed npm `2.15.0`; no production dependency | Useful schema/call debugging before Nox integration; avoid secret storage on headless Linux. | D test-only |
| 9 | **Langfuse optional export after ledger correctness** | Current scoped `@langfuse/tracing`/`@langfuse/otel` `6.1.1`; `src/utils/model-ledger.ts`. Do not use deprecated unscoped client. | Could add traces/analysis, but cannot repair incomplete provider usage or authorize cloud telemetry. | D/E; costs/privacy UNKNOWN |
| 10 | **Defer ToolHive, Composio, Arcade, Inspect AI and automatic Unslop adoption** | Exact upstreams in CSV | Each needs a demonstrated gap; adding them now increases infrastructure/account/eval surface before a single accepted vertical loop. | E/G/H by scope |

## Minimal integration tickets

These are specifications for a separately owner-approved implementation, not work performed.

### R2-S01 — G0 artifact/candidate correctness (first)

1. Fresh-read actual Nox and freeze HEAD/lock hashes; if changed from `68cc0ee…`, remap these callsites before editing.
2. In `file_write`, register the canonical workspace-relative path after existing containment checks, not `basename`; preserve legacy reads and old root artifacts.
3. Add candidate epoch/complete scoped manifest to existing MM/lifecycle/QA evidence; settle writers and deny candidate mutation during review; recheck bytes, admission, intents and cumulative budget before terminal write.
4. Add deterministic layout/integrity/oracle preflight before advisory model QA; insufficient budget produces PAUSED/BLOCKED, never an extended deadline.
5. **Independent oracle:** nested path once/no root copy, same basename in two directories, all-file and binary coverage, mutation/stale receipt rejection, aborted effect unresolved, exhausted resume yields zero model/tool routes. Product PASS and mission verdict remain separate.
6. **Rollback:** revert only this change set; append-only mission/evidence history remains; do not delete historical duplicates or relabel FAILED/PAUSED missions.

### R2-S02 — Native granted ToolSearch (after S01)

1. Keep `@mastra/core=1.82.0`; inspect its exact packaged typings, not latest docs.
2. In `createSpecialist`, create a fresh processor per delegation with tools `grants ∩ registered ∩ admitted`; trusted host RequestContext filters apply at `search`, `load`, and `active`.
3. Map the actual resolved dynamic tool name/schema; retain existing execution-time `assertToolAllowed`, effect and invocation ledger. Use context storage tied to mission/node identity; reconstruct active tools from current grants after restart.
4. **Independent oracle:** held-out correct call among plausible distractors, denied tool invisible/unloadable/uncallable, schema mismatch, revoke, trimming, concurrent tenants, restart. Compare against static full-tool exposure with equal model/task/budget; measure tokens, latency, time-to-first-correct-call and accepted result, including no-benefit outcome.
5. **Rollback:** remove processor wiring and restore static granted tool set; retain existing tool registry, security checks and logs.

### R2-S03 — One permission-safe browser adapter (after S02, only on mission demand)

1. Owner selects exact version after compatibility review; npm `0.0.85` is only the observed snapshot. Record its package integrity and dependency tree in an isolated proposed lockfile; do not use `npx ...@latest` or inherit host environment.
2. Add a thin config/wrapper in `src/config/mcp.ts`/`src/tools/browser.ts`; register minimal allowed operations, isolated browser profile, no secrets, explicit network target, tracked descendants and durable call/effect receipts.
3. **Independent oracle:** harmless read-only page returns grounded evidence; malicious page cannot install/write/exfiltrate; missing browser/package, wrong schema, no network, timeout, cancel, orphan process and unknown external effect all fail closed/reconcile. Exact candidate bytes pass existing browser checks plus required visual/accessibility human review.
4. **Rollback:** disable adapter/revoke grants, stop/quiesce process and restore config/lock; retain evidence. Remote effects are not assumed undone.

### R2-S04 — Source-bound document knowledge (after S01; parallel only in separate sandbox)

1. Select a real bounded low-risk document mission and exact source rights/ACL before selecting Docling. Pin approved PyPI artifacts/hashes; use read-only files, no optional network/model calls.
2. Write source bytes hash/edition/rights/page anchors and parse completeness to immutable KnowledgeRecords; keep the retrieval index rebuildable and separate from LibSQL chat history.
3. **Independent oracle:** specimen ground truth including tables and partial failures; supported claim-to-page mapping, false/stale/injected/unsupported sources blocked or qualified, cross-tenant retrieval denied; baseline comparison measures answer correctness and citation completeness.
4. **Rollback:** remove adapter/index/pack version; retain raw source/evidence and existing chat memory; revoke derived packs rather than silently mixing partial ingestion.

### R2-S05 — One held-out Skill transfer (after S04 and native Workspace smoke)

1. Choose one low-risk skill with exact path, blob SHA and license. Validate native Workspace/SkillSearch at the installed pin; treat all text/resources as untrusted and do not run scripts.
2. Create an immutable CapabilityPack with scope, `when_not`, sources/rights, requested—not self-issued—grants, deliverable and frozen oracle.
3. **Independent oracle:** equal baseline/treatment model/tools/budget, changed task then hidden variant with fresh agent/context; criteria hidden from solver; no authority gain, injection, fixture/oracle leakage; revocation and source-change revalidation. No improvement is reported honestly.
4. **Rollback:** remove/revoke pack and index entry; retain both successful and failed evaluation evidence.

### R2-S06 — Independent evaluation before optimization

1. Use deterministic fixtures first. If Promptfoo adds value, pin `0.125.1` or a later reviewed exact version in a separate test-only harness, with no production credentials/network.
2. Bind every result to approved spec, exact candidate epoch, complete artifact manifest, tools/models/prompts and all attempts. It cannot override Nox terminal state.
3. **Independent oracle:** known-good/known-bad outputs, oracle leakage attempt, candidate mutation, provider failure and unknown token/cost fields. Compare deterministic/single/team/hybrid only under equal authority and budgets.
4. **Rollback:** delete the test-only dependency/config; production QA and original evidence remain unchanged.

## Security gates common to every external candidate

- Explicit owner approval for exact acquisition/install, account/OAuth, secrets, external effect and deployment; each is a separate decision.
- Source/version/integrity/dependency/license review covers scripts, resources and assets, not only root code.
- Minimal host-provided grants; no child env inheritance, untrusted registry/skill/web text as policy, implicit network or automatic retries of unknown remote effects.
- Sandbox, resource limits, tracked descendants, cancellation, durable intent/receipt, independent current-snapshot QA, revocation and evidence-preserving removal.
- Full cost per accepted result remains UNKNOWN until complete ledger/provider reconciliation; OSS license fee zero is not zero TCO.

## Explicit deferrals and stopping rules

Stop a branch at L2 when its question is answered and no real mission demands deeper testing. Do not install the entire MCP Registry, auto-load all skills, create a second orchestrator/memory, mandate PG/fine-tuning or adopt ToolHive/managed OAuth before a measured gap. The minimal R2 target is one specification-bound independently accepted direct-Nox loop; open-world professional graph, generalized transfer and regulated-domain work remain R2.x/R3. T01–T12 and complete acceptance are NOT_RUN here.
