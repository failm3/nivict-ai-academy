# Четыре контура Nox R2: применимые enterprise-паттерны

**Дата:** 2026-11-14 UTC. **Статус:** RESEARCH DESIGN / NOT_IMPLEMENTED / ALL NOX TESTS NOT_RUN.  
**Доказательства:** `[E##]` → `enterprise-evidence.csv`; сравнение систем — `enterprise-practices.md`.  
**Nox paths:** исторический baseline `68cc0ee…`, current source UNKNOWN. Ниже — seam для будущего fresh-read и маленького owner-approved ticket, не assertion о существующем wiring.

## 0. Сквозной принцип

Четыре контура не должны стать четырьмя автономными оркестраторами. Они публикуют **предложения и версии активов** в один host-controlled lifecycle:

`ApprovedSpec → authorized Recipe → CandidateEpoch → Tool/Knowledge/Skill pins → Invocation/Effect ledger → immutable EvidenceBundle → independent verdict → durable terminal → scoped Experience`.

Модель может предложить изменение любого контура; она не может сама изменить spec, grants, oracle, candidate, runtime или terminal. Общие статусы из 06 обязательны. `L2` внешнего компонента не повышает Nox до `CONFIGURED/WIRED`.

---

## A. Tool / Capability Intelligence

### A1. Подтверждённые практики

- OpenAI: MCP filters, per-tool approvals, nested interruption, server-owned RunState и явное предупреждение об отсутствии exactly-once [E01–E03].
- Anthropic: deny/ask/hook/mode/callback pipeline; allowlist = auto-approval, не обязательно visibility; sandbox для scripts/OS [E06–E10].
- AWS/Microsoft: policy на внешней границе, deny-by-default, per-user partition, downstream enforcement и запрет обхода [E15, E19, E20, E22].
- Mastra: native BM25 search/load, search/load/active filter, dynamic toolName, fail-closed filter и context state [E26, E27].

### A2. Целевой lifecycle и transition contract

| Переход | Actor / authority | Обязательная persistent запись и I/O | Failure / idempotency / evidence |
|---|---|---|---|
| NEED | PM/owner | `need_id`, approved spec hash, required input/output, oracle | Вне spec → owner decision; no discovery как выполнение |
| DISCOVER | TI/Manus/native search | query, index snapshot/time, raw candidate refs | Metadata untrusted; partial/failed discovery ≠ empty universe |
| COMPARE/VET | Research + host policy | source/release/commit/package digest/LICENSE/deps/OS/schema/egress/auth/limits | Неизвестное поле UNKNOWN; не подбирать install command из имени |
| AUTHORITY | Owner/host, не model | exact acquisition/action scope, approver identity, expiry | Acquisition ≠ execution; deny/expiry stops |
| PIN/INSTALL | отдельно авторизованный sandbox | lock/integrity, environment/process/network/secrets config | Missing/tampered package → quarantine; rollback/removal |
| REGISTER/GRANT | trusted registry + host | stable `tool_id`, adapter version, dynamic schema/name, requested/actual grants | Collision/stale schema → deny; registry ≠ grant |
| DISCOVER ACTIVE | per-delegation processor | `grants ∩ registered ∩ admitted`, request/node/thread identity | Filter error → disallow; restore только current grants |
| INVOKE | existing execution wrapper | call ID, args hash, actual toolName/schema, durable intent, idempotency key | Timeout/cancel/orphans/unknown remote outcome; no auto replay |
| RECEIPT/QA | artifact store + independent reviewer | destination receipt + artifact + current EvidenceBundle | Local receipt ≠ destination effect; old receipt не accept |
| REUSE/REVOKE | host policy + revalidation schedule | success/failure scope, version, revocation, dependency health | Revoked/stale grant cannot search/load/invoke; data retained by policy |

### A3. Минимальный ToolCard

`tool_id`, upstream owner/repo/package, kind, exact version/commit/digest, license per component, actual dynamic `toolName`+schema, when/when_not, OS/Node/WSL, dependencies, preconditions, minimal grants, user/service identity, network/data flow, secrets/OAuth, read/effect class, idempotency/reconciliation, timeout/cancel, process/resource sandbox, failure/rollback/remove, health evidence, compatibility, L1–L4 refs. Поле отсутствует → UNKNOWN, не «safe/free».

### A4. Минимальный R2 / anti-patterns

**R2:** один уже разрешённый tool с правильным выбором/args/receipt и один отдельно approved новый read-only adapter.  
**Запрещено:** wide MCP installation, default host env, unpinned npx как production acquisition, broad autoLoad, search index как permission source.  
**Nox checks:** T02/T03/T09/T10 + NV-02/03/04. **Rollback:** revoke/disable adapter, remove exact dependency/adapter after quiescence; history/effects не удалять.

---

## B. Knowledge & Competence Intelligence

### B1. Подтверждённые практики

- LangGraph разделяет thread checkpoint и cross-thread Store [E28].
- AWS Memory может формировать episodes/reflections, но это model-derived assets; AWS требует tenant/policy boundaries и признаёт ограничения batch policy [E17, E25].
- Agent Skills — metadata+instructions+resources, progressive disclosure; SDK permission/execution отдельны [E07, E08, E29].
- ABE требует source authority/freshness/ACL, SME-validated ground truth, отдельные development/regression/release sets [E20].
- Devin публично предлагает useful/misleading knowledge review по траектории [E32].

### B2. Разные объекты, разные доказательства

| Объект | Минимальная identity | Что доказывает | Чего НЕ доказывает |
|---|---|---|---|
| KnowledgeRecord | canonical location, immutable bytes/pointer+hash, edition/effective/observed dates, rights, ACL, anchors, transformations | Поддержку конкретного claim указанной редакцией | Correct action/competence/current truth |
| SkillRecord | stable ID/version/digest, instruction/resources refs, prerequisites, scope, when_not | Воспроизводимое содержимое pack | Grants, execution safety, transfer |
| CapabilityPack | Knowledge+Skill+Tool+deliverable+oracle+eval+requested grants+expiry | Проверенный bounded профиль при указанных условиях | Universal profession |
| ActualExperience | spec/candidate/pins/context/cost/artifacts/oracle/outcome/failures/reuse | Что случилось в конкретном run | Общую safety/quality или будущий uplift |
| EvaluationFixture/Oracle | independent owner/version/scope/ground-truth method/hidden keys | Как проверяется outcome | Свою собственную полноту без review |

### B3. Pipeline

1. **Trigger:** approved mission gap или source/release/retraction/failure; не continuous Internet crawl.
2. **Acquire:** legal read/use rights и tenant/owner ACL до ingestion; exact source identity/bytes.
3. **Extract:** format-specific parser/OCR/transcription; сохранить page/section/figure/table/timecode/byte anchors, completeness/errors и model/cost/UNKNOWN.
4. **Qualify:** authority/trust rationale, independent corroboration где нужно; contradictions сохранить с scope.
5. **Index:** rebuildable index с теми же ACL; immutable originals/evidence отдельно. No mandatory PG/vector DB.
6. **Pack:** versioned references, bounded task/deliverable/oracle, requested grants only.
7. **Practice/transfer:** baseline/treatment equal model/tools/budgets; changed case + hidden held-out + fresh agent/context.
8. **Publish scoped experience:** independent verdict, exact conditions, no-benefit сохранить.
9. **Refresh/revoke/delete:** release/expiry/retraction/tool/model change; удалить/unshare index+prompt caches+derived artifacts по policy, не только original.

### B4. Минимальный R2 / anti-patterns

**R2:** одна low-risk source-bound компетенция с независимым held-out результатом; LibSQL history сохранить, retrieval только measured fit.  
**Запрещено:** summary как evidence, read right = redistribute/fine-tune, post-hoc-only ACL, Skill scripts без sandbox, reflection как ground truth, universal parser.  
**Nox checks:** T04/T05/T08/T09 + NV-05/06. **Rollback:** revoke pack version/index и доступ к derived contexts, сохранить provenance/eval history; source deletion/rights может требовать более сильного purge.

---

## C. Execution Strategy Intelligence

### C1. Подтверждённые практики

- Salesforce официально описывает deterministic path без LLM после routing и LLM только для judgment [E36].
- Microsoft ABE выбирает deterministic/fixed/agentic по measured value и задаёт operating envelope [E20].
- Anthropic «Building effective agents» рекомендует простые composable patterns вместо преждевременной сложности [E40].
- OpenAI harness и Devin подчёркивают objective checks, bounded tasks, review capacity; Cognition отдельно показывает влияние harness на scores [E04, E31, E33, E42].
- MM в historical baseline уже имеет DAG/parallel groups; это не current proof и не причина переписывать его.

### C2. Decision matrix

| Route | Использовать когда | Обязательные предпосылки | Не использовать / stop |
|---|---|---|---|
| Existing deterministic function | Input/output известны, oracle вычислим | versioned recipe, expected result, idempotence | Ambiguous input; неправомерный output |
| Small script/program | Повторяемая операция, важны reliability/reuse | sandbox, deps pin, tests, lifecycle cleanup | Одноразовое judgment или unbounded effects |
| CLI/API/fixed workflow | Существует typed API/последовательность | auth, schemas, timeout/retry/reconcile | Скрытая ambiguity требует improvisational loop |
| Persistent service/bot | Есть sustained triggers, uptime/latency/audit need | owner deploy approval, queue/idempotence/retention | Единичная задача, нет sustained need |
| Single LLM/agent | Требуется bounded judgment/generation | input/output schema, oracle, budget | Известный deterministic repeat |
| Parallel/nested team | Независимые evidence/work branches или measured quality need | disjoint writes, aggregate budget, per-child grants, independent QA | Shared mutable product race; more agents как KPI |
| Hybrid | Разные steps реально имеют разные routes | typed per-step handoffs/evidence, no authority expansion | «Hybrid» как ответ по умолчанию |
| BLOCKED | Missing safe scope/oracle/authority/capability | reason, exact owner decision/NEXT_TEST | Не маскировать fallback’ом FAILED/UNKNOWN |

### C3. Recipe contract

`recipe_id/version`, mission/step scope, immutable spec hash, preconditions, route and separate model route, exact tool/knowledge/skill pins, per-stage+global wall/token/spend limits, expected artifact/oracle/reviewer, retry/idempotency/cancel, checkpoints, approval touchpoints, denial/fallback, recovery/terminal semantics, ledger fields, rollback. Fallback должен оставаться в approved spec и current grants; иначе BLOCKED/owner.

### C4. Измерение до принятия

Paired cases: same inputs, fresh contexts, equivalent tools/authority, wall/token/spend budget, frozen hidden independent oracle. Сохранить все attempts/failures. Метрики: independently accepted mission rate, criterion/quality, tool selection/first correct call, repairs/productivity, first/steady latency, full tokens+USD или UNKNOWN, recovery/unresolved effects, build+maintenance+failed attempts. Результат может быть `no-benefit/cannot-conclude`.

**Minimal R2:** T01 no-LLM proof после route и T11 comparison; T07 bot/script/workflow. **Anti-patterns:** new scheduler, model chosen by planner string, «parallel всегда быстрее/дешевле», tokens как полный invoice. **Rollback:** прежняя host route table/config version, ledger сохранить.

---

## D. Meta-Intelligence / Controlled Improvement

### D1. Подтверждённые практики

- Microsoft ABE: production evidence → classification → reviewed contract/knowledge/engineering change → replay/eval/release gate [E20].
- AWS: continuous online/on-demand/batch evaluation; built-in judges имеют фиксированные конфигурации, ground-truth поддерживается не для всех online cases [E18, E41].
- OpenAI/Anthropic: systematic eval, trajectory+outcome, human review и bounded agent harness [E39, E40].
- Devin: useful/misleading knowledge и repeated failures как сигнал изменить environment/context, не автоматическое самообучение [E32].
- OpenAI RunState и Microsoft ADR: approvals/recovery требуют version compatibility и не гарантируют atomic external effect [E01, E24].

### D2. Пять типов изменений — пять authority paths

| Тип | Разрешённый автоматический результат | Обязательный gate | Expiry/rollback |
|---|---|---|---|
| Knowledge acquisition | Новый versioned record в scoped quarantine | rights/ACL/authority/freshness/claims | retraction/edition/ACL; revoke index+refs |
| Skill acquisition | Versioned untrusted/validated pack после eval | source review + sandbox + held-out independent QA | tool/source/model change; revoke pack |
| Tool acquisition | Research candidate only | exact owner acquisition + pin/install/grant/call tests | schema/health/OAuth/license; disable/remove |
| Strategy learning | Recommended recipe rank в experiment | paired equal-task evidence + host policy approval | drift/regression/cost threshold; old route restore |
| Runtime improvement | Ticket/patch proposal, не runtime mutation | code review, owner, security, tests, staged release | code/config rollback; external effects отдельно |

### D3. ExperienceRecord и контролируемый цикл

Хранить: spec/scope/preconditions, initializer/context, exact sources/tools/models/prompts/templates/digests, candidate/artifact hashes, time/cost/UNKNOWN, full ledger, outcome+independent oracle, failure classes, retries/repairs/recovery, superseded/revoked, actual reuse. Personal/tenant records не объединять автоматически; redaction/retention и provider limits явно.

Цикл:

1. Обнаружить no-progress/failure/near-miss через ledger и independent outcome.
2. Классифицировать: unclear contract, knowledge, tool, strategy, model/provider, dependency, lifecycle/oracle.
3. Сформулировать одну falsifiable гипотезу и smallest change; predeclare stop/no-benefit.
4. Провести offline replay/sandbox для diagnostics; он не заменяет real direct Nox.
5. Paired baseline/candidate с frozen oracle, protected release set, all negatives.
6. Independent/domain review и owner approval по типу изменения.
7. Versioned rollout + observation; rollback/revoke без переписывания прошлого.
8. Continuous background generation только при доказанной event/mission-driven пользе.

### D4. Минимальный R2 / anti-patterns

**R2:** calibrated abstention/BLOCKED, no-progress + cumulative budget stop, scoped experience, one before/after eval, revocation/rollback.  
**Запрещено:** lesson меняет policy/runtime, fine-tuning по умолчанию, LLM majority как независимый oracle, personal→shared auto merge, отбрасывание failed/no-benefit, вечный repair.  
**Nox checks:** T05/T09/T10/T11/T12 + ledger/oracle negatives. **Rollback:** конкретный asset/config version; unresolved external effects не «откатываются» молча, а reconciled/escalated.

---

## 1. Минимальная dependency graph для будущих tickets

`Fresh-read + owner scope → G0 artifact/candidate/lifecycle → G1 granted ToolSearch → G2 one vetted read-only adapter → G3 source/pack held-out transfer → G4 route/economics → G5 direct Nox T01–T12`.

Каждый ticket обязан назвать: allowed files, current/pinned deps, non-goals, spec/evidence interfaces, sandbox/egress/secrets, positive+negative tests, independent oracle artifact, logs/ledger/receipts, migration/readback, rollback, effort assumptions/UNKNOWN, owner decisions. Enterprise source не является основанием пропустить G0 или acceptance.

## 2. Главный выбор владельца

Для первого vertical slice выбрать один **низкорисковый домен с объективным deliverable/oracle**, bounded source rights и допустимыми read-only tools; назначить independent reviewer/expert, global budget и no-external-effects policy. Без этого все контура остаются design/PLANNED, а не executable R2.
