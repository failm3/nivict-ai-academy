# OpenCode — проверяемые engineering tickets для Nox R2

**Статус:** спецификации `PLANNED`; все указанные тесты `NOT_RUN`; это не разрешение на implementation/install/deploy. Все пути — относительно actual Nox cleanroom; перед каждым ticket fresh-read HEAD и delta от `68cc0ee20a25991ea275512e20ac521cc8f8234b`. Если код отличается, OpenCode обновляет call-sites, не следует слепо строкам baseline.

## Порядок и общий Definition of Done

`OC-01 → OC-02 → OC-03 → OC-04 → OC-05 → OC-06 → OC-07 → OC-08 → OC-09 → OC-10 → OC-11 → OC-12`. Небольшие reviewable diffs; существующие MM/Head/QA/memory сохраняются. Каждый PR: unit+integration+negative tests, exact candidate/ledger evidence, no paid/live calls unless separately authorized, docs of status not PASS, rollback rehearsal. Effort buckets: **S** один локальный seam, **M** несколько связанных модулей+state migration, **L** новый security-critical protocol; buckets не calendar/cost. Все доллары/calendar UNKNOWN.

## OC-01 — Canonical nested artifact identity (G0, I-01)

- **Objective/scope:** `file_write` сохраняет canonical workspace-relative path после safe-path validation; `product/app.js` не регистрируется как `app.js`.
- **Allowed:** `src/tools/index.ts` (baseline 365–439), `src/utils/storage.ts`, persistence instruction in `src/agents/specialists.ts` только если duplicate save semantics остаётся; focused tests.
- **Non-goals:** удаление historical root duplicates; новый artifact service; cross-tenant API.
- **Design:** atomic file+registration внутри existing `withMissionWrite`; stable id/path/hash/revision; backward reader для старых basename records.
- **Tests:** два legal dirs с одинаковым basename; one record/readback; modifications supersede; traversal, absolute, symlink, cross-mission denied; write failure leaves no phantom registry record; historical fixture readable.
- **Evidence:** before/after manifests+hashes, denied receipts; G0.1. **Effort S/M depending atomicity.**
- **Rollback:** revert tool diff, reader supports both schemas; no history rewrite. **Owner:** implementation only; no new package.

## OC-02 — CandidateEpoch and complete immutable EvidenceBundle (G0, I-02)

- **Objective:** MM owns epoch; QA gets total coverage, not first 6/12000/6000 prefix.
- **Allowed:** `src/agents/mission-manager.ts`, `src/utils/storage.ts`, `src/agents/{qa-agent,qa-gate,web-qa}.ts`, `src/capabilities/web-product.ts`, `src/types/index.ts`, versioned lifecycle serialization in `src/agents/lifecycle.ts`.
- **Contract:** epoch fields per validation-program §3.3; coverage `{artifact_id,revision,path,sha256,size,reader,chunks|binary_oracle,complete:boolean}`; all criteria explicit; no supplied solver claims.
- **Tests:** >6, >12KiB, >6000 output, binary, omitted file, stale parent/spec/plan, old receipt, changed current bytes; complete typed chunks; late PASS cannot terminalize paused mission.
- **Security:** verifier read-only, no credentials/oracle keys; hash is binding not issuer auth.
- **Effort L; depends OC-01. Rollback:** dual-read old state, append-only migrations, old evidence immutable.

## OC-03 — Inspection fence and preterminal revalidation (G0)

- **Objective:** settle parallel writers; deny candidate mutations during QA; recheck spec/plan/epoch/admission/lease/deadline/intents/hashes immediately before durable terminal write.
- **Allowed:** `src/security/tool-context.ts`, `src/tools/index.ts`, `src/utils/storage.ts`, `src/agents/{mission-manager,lifecycle,qa-agent}.ts`.
- **Non-goals:** global process-wide lock blocking other tenants; removing QA gates.
- **Tests:** mutation before/during/after review; revoke/cancel/lease expiry; parallel child late write; read verifier works; other mission unaffected; old/suspended/failed candidate cannot ACCEPTED.
- **Receipts:** fence acquire/release, denial reason, epoch, preterminal comparison, terminal fsync/readback. **Effort L; depends OC-02. Rollback** config off only after quiescence, never bypass existing security.

## OC-04 — Deterministic preflight, reservations, no-progress (G0/G4)

- **Objective:** fail deterministic defects before paid model QA; cumulative budget/resume zero-route; reserve QA/recovery/terminal.
- **Allowed:** `src/agents/{mission-manager,lifecycle,qa-agent}.ts`, existing `src/capabilities/*verifier*`, `src/utils/model-ledger.ts` only interfaces needed.
- **Tests:** deterministic FAIL yields 0 model QA calls; exhausted resume yields 0 Head/specialist/tool calls; repeated identical failure reaches cap; parallel reservation no overrun; clock/error UNKNOWN not reset; terminal reserve enough.
- **Policy:** repair limits/no-progress thresholds host-owned per spec, no model self-extension. **Effort M/L; depends OC-03. Rollback:** retain checkpoints and existing cumulative accounting, disable only new advisory optimization.

## OC-05 — Per-node ledger and truthful economics (G4)

- **Objective:** invocation lifecycle `{node,role,plan_step,route,model,provider,start/end,retry_of,tokens_status,cost_status}`; separate zero/missing/incomplete; acquisition/build/QA/runtime/maintenance categories.
- **Allowed:** `src/utils/model-ledger.ts`, production call sites, `src/config/models.ts` only route identity, report/exporter tests.
- **Tests:** abort/missing finish=>UNKNOWN; transport retry no double count; sibling same-role nodes distinct; zero vs absent; subtotal excludes UNKNOWN; dollars remain UNKNOWN without invoice; old ledgers readable.
- **Effort M; can prepare parallel after OC-02 but G4 depends all. Rollback additive fields; no ledger deletion.**

## OC-06 — Native ToolSearch inside current grants (G1, I-04)

- **Precondition:** actual installed `@mastra/core` API confirmed; historical pin 1.82.0, no upgrade implicit.
- **Allowed:** `src/agents/specialists.ts`, `src/config/models.ts` only node identity if needed, `src/tools/index.ts`, `src/security/tool-context.ts`, focused tests.
- **Design:** fresh per-delegation `inputProcessors`; `tools=grants∩registered∩admitted actual toolSet`, `includeResolvedTools:true`, trusted RequestContext filters search/load/active; map dynamic tool.id/name; context storage per mission/node. Execute path retains `runWithToolContext/assertToolAllowed/withEffect/ledger`.
- **Tests T02:** correct actual call/schema; denied/unknown invisible/unloadable/uncallable; restart/trim/revoke/concurrency; malicious catalog no grants; compare full exposure equal budget, report savings or no-benefit.
- **Effort M; depends OC-01–05 for final acceptance. Rollback:** per-mission disable processor, static allowlisted tools unchanged, state derived only current grants. **Owner:** implementation; package change separately if actual version incompatible.

## OC-07 — One pinned read-only external adapter (G2, I-05)

- **Precondition:** owner names exact candidate/version/digest/license and grants install+call separately. Candidate UNKNOWN here; do not default install Playwright MCP.
- **Allowed:** one new `src/tools/<adapter>.ts`, registry in `src/tools/index.ts`, `src/config/mcp.ts` only if selected MCP, MM admission/effect records, lockfile after approval.
- **Design:** minimal env allowlist, no inherited host secrets, schema validation, egress allowlist, sandbox/cgroup/process tracking, durable intent/idempotency/reconcile, timeout/cancel/disconnect telemetry, independent artifact oracle.
- **Tests T03:** tamper/missing/schema drift/malicious metadata/network/account/OAuth/revoke/cancel/orphan/unknown effect; real read-only useful call only after approval; quarantine/remove.
- **Effort M/L depending runtime. Rollback:** revoke/disable registration, stop processes, retain logs/quarantine; no automatic duplicate external action. **Owner:** exact acquisition, secrets/OAuth, egress and real call.

## OC-08 — Immutable source-bound KnowledgeRecord and ACL (G3)

- **Objective:** additive store for source bytes/pointer/hash, rights, owner/tenant ACL, edition/effective date, page/figure/timestamp anchors, contradictions/retraction/freshness; no universal parser/new PG.
- **Allowed:** decision-bound `src/memory/index.ts`, small new knowledge/pack store after current architecture read, types/tests; existing LibSQL message memory remains.
- **Tests:** ACL enforced before index/retrieval/prompt/cache/artifact; cross-tenant denied; stale/retracted/unlicensed qualified/blocked; partial ingest never complete; conflicting sources both retained; delete/export/rebuild index provenance.
- **Evidence T04:** source-to-claim independent review, citation completeness. **Effort L. Rollback:** revoke records/packs, rebuild/delete derived indexes, immutable source evidence retained. **Owner:** sources/rights/retention/expert.

## OC-09 — Versioned CapabilityPack and fresh-agent transfer harness (G3)

- **Objective:** immutable pack refs sources/skills/adapters/oracles/requested-not-granted permissions; exact digest/scope/expiry/revocation; hidden frozen equal-task harness.
- **Allowed:** pack store from OC-08, fresh specialist construction/oracle harness; no global skill auto-load or runtime self-edit.
- **Tests T05:** baseline/treatment fresh contexts, changed+held-out tasks, leakage/carry-over, wrong tenant, malicious instructions, revoked source/tool/pack; no improvement retained as NO_BENEFIT; revalidate on version change.
- **Effort L; depends OC-08. Rollback:** revoke version and derived caches; old evidence readable. **Owner:** domain/pack/oracle/expert and model budget.

## OC-10 — Typed host-owned execution recipes (G4)

- **Objective:** route contract near PM/spec→Head→MM for deterministic/program/API/service-or-bot/single/team/hybrid/BLOCKED; no third orchestrator.
- **Allowed:** `src/agents/{prompt-master,head-agent,mission-manager}.ts`, `src/types/index.ts`, `src/config/models.ts` only trusted host routes, ledger OC-05.
- **Contract:** recipe id/version, input/preconditions, exact tools/models/program, stage/global budgets, output/oracle, idempotency/cancel/checkpoints, denial/fallback. Fallback never expands authority/hides FAILED/UNKNOWN.
- **Tests T01/T07/T11:** deterministic zero-LLM after route; unsupported input BLOCKED; persistent vs one-shot calibration; parallel conflicts and no-progress; paired equal budgets; no invented model winner.
- **Effort L; depends OC-04/05. Rollback:** versioned recipes disabled by policy, prior checkpoints and route logs retained. **Owner:** route policies/budgets/provider routes.

## OC-11 — Adversarial acquisition/knowledge security pack (G5 support)

- **Objective:** reusable local corpus+harness for T09, not a new permission framework.
- **Allowed:** tests/fixtures and telemetry adapters only; policy fixes separately minimal after findings.
- **Coverage:** malicious web/doc/registry/Skill/MCP/output, name/schema collision, poisoned cache, canary secrets, local sink, benign injection-like text; fs/net/process/policy/candidate diff.
- **Pass:** 0 privileged effect/leak/mutation; quarantine and evidence; benign usable or documented scoped reason. No exhaustive security claim.
- **Effort M; depends OC-06–09 relevant paths. Rollback:** fixtures removable, evidence retained. **Owner:** red-team independence, external target if any.

## OC-12 — Independent direct-Nox acceptance harness (G5)

- **Objective:** owner-only launcher/frozen spec, external evidence collector and reviewer package; no solver assistance or OpenCode runtime control after start.
- **Allowed:** approved direct Nox host/harness, evidence exporters, independent test code; no production deployment.
- **Tests:** all T01–T12 rows, interruption OC real kill/recovery, current epoch/terminal, intervention audit, full attempt index/cost statuses, rollback rehearsal.
- **Effort M/L; depends all previous. Rollback:** stop run/revoke test grants, no release; preserve evidence. **Owner:** final novel mission, caps, reviewers/experts, permissible external effects and release decision.

## Owner decisions that block engineering

Current source access; authorize each ticket; exact dependencies/install; domains/oracles/experts; numerical model/token/time/USD caps; source rights/tenancy/retention; accounts/OAuth/secrets/egress; harmless external effect target; final independent reviewers and release scope. No ticket authorizes purchases, Nox/OpenCode interference, publishing or production changes.
