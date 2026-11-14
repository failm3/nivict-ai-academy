# OPENCODE-HANDOFF-READYNESS

**Статус пакета:** `SPECIFICATION_HANDOFF_COMPLETE / ENGINEERING_BLOCKED_PENDING_OWNER_AND_FRESH_NOX`. Это не разрешение на implementation, install, paid/live test, deploy или publication. Сохранены без изменений все 12 tickets в `../15-OPENCODE-EXECUTION-PACK/OC-01.md`…`OC-12.md`; общий порядок и DoD — `README.md` §§«Порядок и общий Definition of Done».

## Общий обязательный preflight

Для **каждого** ticket до дизайна/диффа: owner разрешает конкретный ticket и read-only audit; зафиксировать actual branch/HEAD/status, package.json+lock+installed typings, hashes и delta от исторического `68cc0ee20a25991ea275512e20ac521cc8f8234b`; в конце second readback. Все paths/API ниже — **исторические предложения**, не current facts. Изменился код → пересмотреть allowed files/dependencies и ticket, не следовать старым строкам. Каждый PR: small diff, immutable spec/candidate evidence, unit+integration+negative tests, independent reviewer, no solver/oracle leakage, rollback rehearsal, actual costs или UNKNOWN.

Independent acceptance един для всех: reviewer отдельного authority context проверяет exact current CandidateEpoch/complete artifacts/receipts/grants/budget/terminal; product PASS не равен mission ACCEPTED. Mock/unit PASS — preliminary только; финальные claims требуют direct Nox и соответствующих T01–T12 в OC-12. Все тесты сейчас `NOT_RUN`.

## OC-01 — Canonical nested artifact identity

- **Проверенные факты:** ticket задаёт atomic file+registration, stable id/path/hash/revision и backward reader. Historical basename/root duplication зафиксирован в прежнем review, не подтверждён заново.
- **Неподтверждённое:** текущие `file_write`, `withMissionWrite`, storage schema и baseline lines 365–439; atomicity и duplicate-save semantics.
- **Fresh audit / integration / версии:** прочитать `src/tools/index.ts`, `src/utils/storage.ts`, `src/agents/specialists.ts`; текущие persistence APIs UNKNOWN. Новых packages нет.
- **Tests:** positive — два legal dirs с одинаковым basename, one record/readback, supersession, old fixture readable. Negative — traversal/absolute/symlink/cross-mission denied; write failure без phantom record. См. ticket §§Tests/Evidence.
- **Independent acceptance:** G0.1 — ровно canonical paths, no root copy, denied receipts и before/after hashes на sealed candidate; preliminary G0, не R2.
- **Rollback:** revert tool diff; dual reader старой/новой schema; history/root duplicates не удалять.
- **Owner permissions:** read+implementation ticket только; no new package/external effect.

**Readiness:** `BLOCKED_ON_FRESH_SOURCE_AND_OWNER_IMPLEMENTATION`.

## OC-02 — CandidateEpoch and complete immutable EvidenceBundle

- **Проверенные факты:** contract явно ссылается на `validation-program.md` §3.3; coverage включает path/revision/hash/size/reader/chunks/binary/complete. Historical truncation 6/12000/6000 не fresh.
- **Неподтверждённое:** текущие MM ownership, serialization compatibility, QA readers и способ обеспечить все binary artifacts.
- **Fresh audit / integration:** `mission-manager.ts`, `storage.ts`, `qa-agent.ts`, `qa-gate.ts`, `web-qa.ts`, `web-product.ts`, `types/index.ts`, `lifecycle.ts`; exact epoch serialization/version UNKNOWN. **Depends OC-01.**
- **Tests:** >6, >12KiB, >6000, binary, omitted file, stale spec/plan/parent, old receipt, changed bytes; late PASS не terminalizes PAUSED.
- **Independent acceptance:** reviewer получает 100% typed coverage/current sealed bytes, не solver claims; все mandatory criteria FINISHED и terminal semantics раздельно.
- **Rollback:** dual-read/versioned append-only migration; old evidence immutable.
- **Owner permissions:** implementation+schema migration; reviewer/evidence retention; no oracle keys/credentials for verifier.

**Readiness:** `BLOCKED_ON_OC01_FRESH_SCHEMA_AND_MIGRATION_AUTHORITY`.

## OC-03 — Inspection fence and preterminal revalidation

- **Проверенные факты:** ticket требует settle writers, запрет mutation во время QA, recheck spec/plan/epoch/admission/lease/deadline/intents/hashes до durable terminal.
- **Неподтверждённое:** текущий locking/lease/admission и distributed concurrency semantics; отсутствие side channels записи.
- **Fresh audit / integration:** `tool-context.ts`, `tools/index.ts`, `storage.ts`, MM/lifecycle/qa-agent; fence/lease API UNKNOWN. **Depends OC-02.**
- **Tests:** mutation before/during/after review; revoke/cancel/lease expiry; late parallel child write; verifier readable; other mission unaffected; old/suspended/failed not accepted.
- **Independent acceptance:** fence receipts, current epoch compare, no unresolved intent/in-flight writer, terminal fsync/readback совпадает.
- **Rollback:** config off только после quiescence; никогда не открывать bypass/не ослаблять existing security.
- **Owner permissions:** implementation security-critical lifecycle; тестовые revoke/cancel scopes; no production terminal changes beyond approved fixtures.

**Readiness:** `BLOCKED_ON_OC02_AND_CURRENT_CONCURRENCY_AUDIT`.

## OC-04 — Deterministic preflight, reservations, no-progress

- **Проверенные факты:** deterministic FAIL должен предшествовать model QA; QA/recovery/terminal входят в cumulative budget; model не продлевает лимиты.
- **Неподтверждённое:** текущие verifiers, clocks/resume/accounting, параллельные reservations и фактические thresholds.
- **Fresh audit / integration:** MM/lifecycle/qa-agent, `capabilities/*verifier*`, `model-ledger.ts`; numeric caps owner UNKNOWN. **Depends OC-03.**
- **Tests:** deterministic FAIL→0 model QA; exhausted resume→0 Head/specialist/tool routes; repeated failure cap; parallel no overrun; clock/error UNKNOWN not reset; terminal reserve sufficient.
- **Independent acceptance:** invocation trace доказывает нулевые routes, reservation+terminal receipts и PAUSED/BLOCKED/UNKNOWN без silent extension.
- **Rollback:** disable только новый advisory optimization; checkpoints/cumulative accounting остаются.
- **Owner permissions:** утвердить global/stage wall/token/spend/repair/no-progress/process caps и implementation; no paid stress без отдельного разрешения.

**Readiness:** `BLOCKED_ON_OC03_AND_NUMERIC_OWNER_BUDGETS`.

## OC-05 — Per-node ledger and truthful economics

- **Проверенные факты:** contract различает zero/missing/incomplete tokens и cost categories; historical 337014+UNKNOWN sixth не bill.
- **Неподтверждённое:** текущие SDK/provider callbacks, transport retry identity, invoice mapping и production callsite coverage.
- **Fresh audit / integration:** `model-ledger.ts`, production callsites, `config/models.ts` только route identity, exporter tests. **Prepare after OC-02; G4 depends all.**
- **Tests:** abort/missing finish→UNKNOWN; retry no double count; sibling same-role distinct; zero≠absent; subtotal excludes UNKNOWN; no dollars without invoice; old ledger readable.
- **Independent acceptance:** reconcile node/tool/QA/recovery/terminal traces и usage↔invoice; иначе cost UNKNOWN, не zero/free.
- **Rollback:** additive fields/dual reader; ledger/history не удалять.
- **Owner permissions:** implementation; доступ к sanitized provider usage/invoice отдельно; no new telemetry endpoint без approval.

**Readiness:** `BLOCKED_ON_CURRENT_CALLSITE_AND_LEDGER_ACCESS`.

## OC-06 — Native ToolSearch inside current grants

- **Проверенные факты:** historical pin `@mastra/core=1.82.0`; exact tarball SHA-512 в `../solutions-research.zip:sources/mastra/manifest.json` проверен. Source документирует search/load/active filters, dynamic resolved tools. Это не current install/wiring proof.
- **Неподтверждённое:** actual installed version/typings, `createSpecialist`, RequestContext/storage APIs, dynamic tool IDs и measured savings.
- **Fresh audit / integration:** `specialists.ts`, `models.ts`, `tools/index.ts`, `tool-context.ts`; package change отдельный gate. **Depends OC-01–05 for final acceptance.**
- **Tests T02:** correct actual schema/call/receipt; denied/unknown invisible-unloadable-uncallable; restart/trim/revoke/concurrency; malicious catalog no grants; equal-budget full-injection comparison.
- **Independent acceptance:** only `grants∩registered∩admitted`; actual call independent oracle, selection/safety/latency/tokens и no-benefit reported.
- **Rollback:** per-mission disable processor; static allowlist unchanged; active state rebuilt только current grants.
- **Owner permissions:** implementation; exact package change только если incompatibility доказана и отдельно approved; model/live comparison budget separately.

**Readiness:** `BLOCKED_ON_FRESH_MASTRA_PIN_AND_G0_EVIDENCE`.

## OC-07 — One pinned read-only external adapter

- **Проверенные факты:** L2 candidate choices/oracles собраны; **никакой candidate не выбран/не approved**. Playwright не default. Exact package/digest/license обязательны.
- **Неподтверждённое:** candidate identity/version/transitive deps/OS/browser compatibility, MCP API, egress/secrets/process containment.
- **Fresh audit / integration:** один новый `src/tools/<adapter>.ts`, registry `tools/index.ts`, `config/mcp.ts` только если MCP, MM admission/effects, proposed lockfile. **After G0/G1.**
- **Tests T03:** useful read-only receipt; tamper/missing/schema drift/malicious metadata/no network/missing account/revoked OAuth/timeout/cancel/orphan/unknown effect; quarantine.
- **Independent acceptance:** exact artifact+digest, independent useful-result oracle, zero unauthorized effect/secret/escalation/orphan, grant revoke works.
- **Rollback:** revoke/disable registration, quiesce/stop tracked processes, retain logs/quarantine; UNKNOWN external effect reconcile, no auto duplicate.
- **Owner permissions:** exact acquisition+install и real call **отдельно**; secrets/OAuth/egress/sandbox/resources отдельно; no purchase/deploy.

**Readiness:** `BLOCKED_ON_EXACT_OWNER_ACQUISITION_AND_G0_G1`.

## OC-08 — Immutable source-bound KnowledgeRecord and ACL

- **Проверенные факты:** KnowledgeRecord fields/ACL pipeline определены; existing LibSQL history сохранить; universal parser/PG не требуются.
- **Неподтверждённое:** current memory architecture/storage API, tenant identity, corpus rights/ACL, deletion/export semantics.
- **Fresh audit / integration:** decision-bound `src/memory/index.ts`, small additive store после read; no DB choice предопределён. **Prepare after G0; feeds OC-09.**
- **Tests:** ACL before index/retrieval/prompt/cache/artifact; cross-tenant denied; stale/retracted/unlicensed blocked/qualified; partial ingest not complete; contradictions retained; delete/export/rebuild provenance.
- **Independent acceptance T04:** source-to-claim+citation completeness by independent/domain reviewer, no unsupported claim или cross-tenant leakage.
- **Rollback:** revoke records/packs; rebuild/delete derived indexes по policy; immutable source evidence retained, deletion/rights complaint escalation.
- **Owner permissions:** exact sources/read/use rights, tenant ACL, retention/export/delete, implementation и expert.

**Readiness:** `BLOCKED_ON_CURRENT_MEMORY_AND_SOURCE_RIGHTS_ACL`.

## OC-09 — Versioned CapabilityPack and fresh-agent transfer harness

- **Проверенные факты:** pack contract и held-out design заданы; готовых accepted packs нет. `allowed-tools`/loaded skill не grant/competence.
- **Неподтверждённое:** selected domain/pack/skill versions, Workspace/SkillSearch installed API, leakage-free fresh solver и measurable uplift.
- **Fresh audit / integration:** store OC-08, fresh specialist construction/oracle harness; historical Mastra 1.82.0 только после fresh pin. **Depends OC-08.**
- **Tests T05:** equal baseline/treatment fresh contexts, changed+hidden held-out, leakage/carry-over/wrong tenant/malicious instructions/revoked source-tool-pack; NO_BENEFIT preserved; revalidate on change.
- **Independent acceptance:** predeclared quality/safety/tool metrics by uninvolved reviewer/expert; pack/digest/oracle hidden appropriately; no broad qualification.
- **Rollback:** revoke pack version+derived caches; old evidence readable; scripts/processes quiesce separately if ever authorized.
- **Owner permissions:** domain/pack/oracle/expert/model budget/source rights; implementation; no scripts/new grants by pack itself.

**Readiness:** `BLOCKED_ON_OC08_OWNER_PACK_AND_INDEPENDENT_TRANSFER_PROTOCOL`.

## OC-10 — Typed host-owned execution recipes

- **Проверенные факты:** routes и contract определены; Head advisory, host authorizes, MM сохраняется; model route отдельна.
- **Неподтверждённое:** current PM/Head/MM types/config, feasible deterministic/program routes, provider/model routes и winner.
- **Fresh audit / integration:** `prompt-master.ts`, `head-agent.ts`, `mission-manager.ts`, `types/index.ts`, `config/models.ts`, ledger OC-05. **Depends OC-04/05.**
- **Tests T01/T07/T11:** actual zero-LLM after deterministic route; unsupported input BLOCKED; persistent-vs-one-shot calibration; parallel conflicts/no-progress; paired equal budgets; hidden inferior route.
- **Independent acceptance:** frozen route matrix/oracle и actual traces; quality first, accepted rate/repairs/time/tokens/USD или UNKNOWN; no-benefit/cannot-conclude допустимы.
- **Rollback:** disable versioned recipes by policy; previous checkpoints/route logs retained; fallback no authority expansion.
- **Owner permissions:** route policies/numeric budgets/provider routes/model use; bot/external deploy отдельно.

**Readiness:** `BLOCKED_ON_OC04_OC05_AND_ROUTE_BUDGET_AUTHORITY`.

## OC-11 — Adversarial acquisition/knowledge security pack

- **Проверенные факты:** fixture coverage и zero-privileged-effect target заданы; это tests/fixtures, не новая permission framework.
- **Неподтверждённое:** actual enforcement points, containment, telemetry sufficiency и benign overblock rate.
- **Fresh audit / integration:** tests/fixtures+telemetry adapters only; relevant paths OC-06–09; policy fixes separate minimal tickets after findings.
- **Tests T09:** malicious web/doc/registry/Skill/MCP/output/name-schema collision/poisoned cache/canary secrets/local sink; denied install/purchase/env/cross-tenant/external write/spec-oracle-QA mutation; benign lookalike.
- **Independent acceptance:** independent red-team verifies fs/net/process/policy/candidate diff: 0 privileged effect/leak/mutation; quarantine evidence; scoped benign usability. Не exhaustive security proof.
- **Rollback:** remove fixtures/telemetry adapter после evidence export; no weakening policy; security findings remain tracked.
- **Owner permissions:** independent red-team, canary/local sink, harmless external target только если необходим и отдельно approved; no live attack/purchase.

**Readiness:** `BLOCKED_ON_RELEVANT_OC06_OC09_AND_INDEPENDENT_RED_TEAM`.

## OC-12 — Independent direct-Nox acceptance harness

- **Проверенные факты:** `validation-program.md`+`test-matrix.csv` полностью задают T01–T12; OpenCode не solver/orchestrator/repair после start. Все actual verdicts отсутствуют.
- **Неподтверждённое:** actual direct host/harness, owner novel mission, reviewers/experts, hidden fixture custody, real recovery/effect target и feasibility all previous gates.
- **Fresh audit / integration:** approved direct Nox host, external evidence collector/reviewer package, no production deploy. **Depends all OC-01–11 relevant scope.**
- **Tests:** every T01–T12 row и TR01–TR09 negatives, real kill/recovery at T10 boundaries, current epoch/terminal, intervention audit, all attempts/cost statuses, rollback rehearsal.
- **Independent acceptance:** `R2_ACCEPTED(scope)` только если every mandatory criterion FINISHED/PASS, current sealed epoch/live grants/no unresolved effect/budget/durable terminal и independent/domain signoff. Иначе `R2_NOT_ACCEPTED`.
- **Rollback:** stop run/revoke test grants/quiesce, no release; preserve failures/PAUSED/UNKNOWN/evidence; external effects reconcile не auto undo.
- **Owner permissions:** final novel Approved Spec, caps, reviewers/experts, permissible effects, evidence retention и release decision отдельно.

**Readiness:** `BLOCKED_ON_ALL_PREVIOUS_GATES_AND_FULL_OWNER_ACCEPTANCE_PACKAGE`.

## Итоговая готовность handoff

| Что готово | Что блокирует execution |
|---|---|
| 12/12 tickets сохранены; dependency order, allowed historical files, positive/negative tests и rollback заданы | Fresh current Nox audit и owner authorization каждого ticket |
| G0–G5/T01–T12 protocol, independent evidence/terminal boundary | Реализация, L3/L4, live calls, full ledger/invoice и direct-Nox acceptance |
| Exact upstream L2 для отобранных candidates | Actual installed pins/API/compat и owner exact acquisition |
| Этот документ дополняет independent acceptance/permissions, не переписывая tickets | Numeric budgets, domains/oracles/experts, rights/ACL/accounts/effects/release decisions |

**Максимально допустимый handoff claim:** спецификации готовы для owner review и fresh-source refinement. **Недопустимо:** «OpenCode может безопасно реализовать всё без уточнения», «R2 accepted», «tests passed», «current Nox compatible».
