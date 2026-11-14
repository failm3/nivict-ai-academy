# Nox R2: реальные практики enterprise AI-agent систем

**Наблюдение:** 2026-11-14 UTC. **Тип:** независимый desk research, не fresh runtime audit и не R2 acceptance.  
**Источники:** официальные документы и pinned source trees; машинный реестр — `enterprise-evidence.csv`. Ссылки `[E##]` разрешаются там.  
**Главная граница:** текущий Nox недоступен для чтения; `68cc0ee…` и перечисленные ниже paths — **исторический baseline OpenCode**, не подтверждённый current state. Никакие испытания Nox, новые provider calls, installs или сравнительные измерения в этой работе **не выполнялись**.

## 1. Краткий вывод

Enterprise практика не сводится к «сильной модели + много агентов». Устойчивый общий каркас:

1. **Контракт поведения и зоны ответственности** до выбора модели: допустимый результат, обязательные доказательства, запреты, пределы, stop/escalation.
2. **Host-enforced authority**: модель только предлагает действие; приложение/gateway/downstream service повторно проверяет identity, resource, operation, arguments и approval.
3. **Разделение discovery, authority и execution**: registry/tool search уменьшает поиск, но не выдаёт grant и не подтверждает trust.
4. **Типизированный durable lifecycle** вокруг недетерминированной работы: candidate identity, checkpoints, approvals, timeout, cancellation, quiescence, terminal state; для внешних эффектов — отдельные idempotency и reconciliation.
5. **Два вида оценки**: trajectory/tool-use и результат; deterministic preflight там, где возможен, LLM judge только с проверенной методикой и domain expert для профессиональных решений.
6. **Knowledge, memory, skill, experience и runtime change — разные активы** с версией, provenance, ACL и отдельной проверкой; retrieval/сохранённый lesson не равен приросту компетентности.
7. **Простейшая подходящая route выигрывает по умолчанию**: deterministic/script/fixed workflow до agent/team; multiagent только для независимых ветвей или доказанного качества, с включёнными QA/recovery затратами.

Это подтверждает направление G0→G5 из 06, а не заменяет его обязательные проверки.

## 2. RANKED ACTIONABLE SHORTLIST

Ранги отражают ожидаемое снижение текущего интеграционного риска при `REUSE FIRST`, а не качество vendor’ов. Все Nox verdicts — **H / PLANNED до fresh read**; внешний evidence — максимум **L2**.

| # | Практика и доказательство | Предлагаемый Nox seam (исторический baseline) | Минимальный proof / rollback |
|---|---|---|---|
| 1 | **Behavior contract + operating envelope + protected release set** [E20, E21]. Это сильнее простого rubric: явно включает missing evidence, prohibited effects и лимит ожидания/стоимости. | PM typed spec → `src/utils/spec-binding.ts`; MM candidate/review; QA oracle. | Owner-approved один bounded low-risk mission; проверить stale spec, missing evidence, неизменённые oracle и budget. Rollback: новая config/schema version, старые спецификации и receipts не переписывать. |
| 2 | **Approval — capability привязанная к server-owned state; per-call по умолчанию; exactly-once не обещать** [E01, E22, E24]. | `src/security/tool-context.ts`, `src/agents/lifecycle.ts`, MM intent/effect ledger, API approval endpoint. | Управляемый локальный effect с durable intent и stable idempotency key; прерывания до/после вызова; concurrent/replayed approval; неизвестный remote outcome → UNKNOWN без retry. Rollback запрещает новые effects и сохраняет intents. |
| 3 | **CandidateEpoch + полный EvidenceBundle + preterminal revalidation** [E20, E22]. | `src/tools/index.ts`, `src/utils/storage.ts`, MM/lifecycle/QA/web-qa. | Mutation во время QA, >6 artifacts, >12k, одинаковые basename в двух dirs, late PASS, exhausted budget. Откат — только новый candidate path, история immutable. |
| 4 | **Native ToolSearch только над `grants ∩ registered ∩ admitted`** [E26, E27]. Mastra 1.82.0 pinned tag `6e8dfcb…`; отдельные фильтры search/load/active и fail-closed filter. | `src/agents/specialists.ts`, `src/security/tool-context.ts`, actual resolved `toolName`. | Один delegated agent, distractors и denied tool; dynamic MCP names; revoke/restart/trim/concurrency; full injection baseline. Rollback — удалить inputProcessor из одного delegation, grants остаются прежними. |
| 5 | **Deterministic gateway/control plane с deny-by-default и проверкой на каждом handoff** [E06, E16, E19, E20]. | existing `tool-context` + downstream checks, не второй permission framework. | Злоумышленный metadata/web/tool output, cross-tenant id, direct path вокруг gateway, revoked grant/OAuth, duplicate tool name. Rollback не должен открыть прямой bypass. |
| 6 | **Полный per-node invocation/effect/QA ledger; replay для разработки** [E20, E28, E39]. | `src/utils/model-ledger.ts`, MM checkpoints, artifact storage. | Сохранить transport retries, routing/planning calls, QA/recovery/terminal, missing vs zero tokens. Сравнить paired baseline/treatment с frozen oracle. Rollback не стирает прежний ledger. |
| 7 | **Один source-bound KnowledgeRecord/CapabilityPack и held-out fresh-agent transfer** [E07, E17, E20, E23, E32]. | `src/memory/index.ts` — решение только после fresh read; отдельный маленький store, LibSQL message history сохранить. | Источник/права/ACL/page anchor; stale/retracted/tainted/cross-tenant negatives; equal-budget baseline/treatment, changed case и fresh agent. Rollback: revoke pack/index, provenance и отрицательные результаты сохранить. |
| 8 | **Route selection: code/fixed workflow/single agent/team/blocked** [E04, E18, E20]. | Head advisory + host-owned recipe у PM/MM; models отдельно через `src/config/models.ts`. | Одна и та же задача/authority/budgets/oracle; metrics accepted rate, repair, latency, полный usage. Rollback — прежняя route table; никакого автоматического escalation. |

## 3. FASTEST SAFE INTEGRATION PATH

Это **предложение порядка**, не implementation authorization.

1. **Fresh source gate:** read-only `/home/nox/awe-group-cleanroom-20261112`, `r1/dev`, начальный/конечный HEAD/status/hash и package lock. Если недоступно — integration остаётся H/UNKNOWN.
2. **G0 перед intelligence:** исправить canonical nested identity и закрыть current candidate/QA race; реализовать полный manifest/coverage, deterministic preflight, budget reservations и terminal settlement. Не добавлять новый orchestrator.
3. **G1:** один native `ToolSearchProcessor` из **уже установленного/подтверждённого pin** над granted actual tools. Доказать invocation, не только search; если search дороже/хуже — оставить full injection.
4. **G2:** один полезный **read-only** внешний adapter с exact release/digest/license, least grant, sandbox, receipt, revoke/remove. Не разворачивать marketplace; отдельно решить historical unpinned Playwright MCP.
5. **G3:** одна ограниченная low-risk предметная задача с authoritative source + pack + independent oracle; измерить held-out transfer, включая «нет улучшения».
6. **G4:** host-owned typed route и ledger economics. Не новый scheduler до доказанного MM gap.
7. **G5:** прямой Nox, T01–T12, independent QA/domain review; OpenCode не участвует в solver loop.

**Ожидаемые затраты и календарь — UNKNOWN.** Внешние SDK/license не дают оценки Nox engineering/QA/run cost; полный usage/invoice требуется отдельно.

## 4. Метод и шкала доказательств

- **OFFICIAL / CODE_PRESENT / DOCUMENTED:** вендор опубликовал API, контракт или утверждение. Это не значит, что исследователь вызвал API.
- **VENDOR_REPORTED:** метрика/case от вендора или его customer story; независимость и переносимость ограничены указанной методикой.
- **RESEARCHER_INFERENCE:** вывод из нескольких источников; требует проверки именно в Nox.
- **L1** найдено; **L2** проверены первичный source/API/version/license; **L3** отдельный adversarial executable test; **L4** independent equal-task uplift. Здесь для Nox только L1/L2, никаких L3/L4.
- Для OSS проверены pinned repos: OpenAI Agents Python `0.24.0` @ `64fbde5…`; Claude Agent SDK Python `0.2.182` @ `4720d367…`; Google ADK @ `12aab4aa…` (version dynamic в pyproject, **release UNKNOWN**); Microsoft Agent Framework Python `1.26.0` @ `92838b60…`; LangGraph Python `1.2.22` @ `08a20169…`; Mastra tag `@mastra/core@1.82.0` @ `6e8dfcb…`. HEAD не считается release, если tag не доказан. Лицензии применимы только к указанному repo/package, не к hosted service и assets по умолчанию.

## 5. Сравнение систем — что реально переносить

### 5.1 OpenAI Codex / Agents SDK

**Официально подтверждено.** Agents SDK предоставляет tool filters, MCP approvals, serializable `RunState`, tracing и guardrails [E01, E02]. Approval callable fail-closed при malformed args; nested approvals всплывают в outer run. Codex cloud ограничивает agent network по умолчанию, удаляет secrets до agent phase, checkout привязан к branch/SHA [E05]. OpenAI production harness публично описывает mechanical architectural constraints и acceptance-driven review [E04].

**Важные границы.** Serialized `RunState` не аутентифицирует snapshot/человека. Approval не равен exactly-once: после effect и до state save повтор возможен; нужен destination-enforced key или authoritative reconciliation [E01]. Sticky shell/file approval может быть шире, чем ожидает другой agent/executor. Parallel input guardrail не предотвращает уже начавшиеся side effects — для таких действий blocking preflight [E02]. MCP annotations advisory, если нет доверия server classification [E03].

**Для Nox:** взять server-owned approval и idempotency protocol как **поведенческий контракт**, не переписывать MM под Python SDK. Trace не заменяет acceptance. Equal-task T02/T09/T10 обязательны.

### 5.2 Anthropic Claude Code / Agent SDK / Skills

**Официально подтверждено.** Шестиступенчатый permission pipeline: hooks → deny → ask → mode → allow → `canUseTool`; deny имеет приоритет, а allow не означает удаление tool из toolset [E06]. `PreToolUse` нужен для контроля auto-approved calls. `bypassPermissions` не ограничивается `allowed_tools`; subagent bypass — критический риск. Sandboxing нужен для OS enforcement, потому что path rule не ограничивает произвольный script. Skills содержат `SKILL.md` и resources; progressive loading не доказывает права или компетенцию [E07, E08].

**Источник кода.** Python SDK `0.2.182` @ `4720d367…` содержит callback/hook control protocol; README прямо различает auto-approval и availability [E09]. Официальные managed-agent docs дополнительно предупреждают: tool input/output могут уходить в control plane, sandbox limits не защищают custom MCP/self-hosted infra [E10].

**Для Nox:** отдельные *visible/searchable/loadable/authorized/invocable* состояния; central hook дополняет grant check, не заменяет его. Не наследовать broad mode в child. Skill pack получает лишь requested grants; scripts проходят tool acquisition pipeline. Проверить нежелательное скрытие denied tools: security через obscurity не допускается как единственная защита.

### 5.3 Google ADK / Agent Engine

**Официально подтверждено.** ADK разделяет session, artifacts, memory, credentials и plugin manager в Runner [E11]. Рекомендации включают agent-auth vs user-auth, developer-controlled ToolContext, reusable plugins, sandbox, network perimeter и eval [E12]. Agent-auth подходит для общего уровня доступа; при пользовательских различиях нужна user auth/дополнительные ограничения. OAuth scopes могут быть шире фактической потребности. ADK evaluation отдельно измеряет trajectory/tool use и final response [E13].

**Границы.** Framework callback может не видеть необходимой semantics в arguments; тогда enforcement переносится в tool/downstream. Model guardrail не гарантирует authority. In-memory auth/session не является persistence. Публичный source @ `12aab4aa…` не равен подтверждённому release; installed Nox compatibility UNKNOWN. Сохранение истории диалога в CLI не следует путать с transaction-safe long-running recovery; последняя требует отдельной проверки.

**Для Nox:** не создавать второй planner. Применить host-controlled RequestContext и per-handoff reauthorization, source-bound evidence вместо «embedding similarity = истина». T04 и T09 должны проверять indirect injection и неправомерный identity passthrough.

### 5.4 Microsoft Agent Framework / Azure ABE

**Официально подтверждено.** Workflow поддерживает checkpoint/resume, human requests, sequential/concurrent/handoff patterns и observability [E14]. ABE даёт наиболее полный найденный lifecycle: behavior contract, scenario library, operating envelope, replay, verify, observe [E20]. Ground truth — domain-validated result, а не прошлый output агента; protected release set отделён от tuning/regression. Delegate не расширяет authority, approvals/mandatory steps/envelope исполняются системой.

**Границы из source.** ADR 0035 показывает необходимость физической partition по agent/user/context в дополнение к identity check; local mode ослабляет hosted guarantees [E22]. ADR 0049 **proposed**, не release proof: unanswered approvals auto-reject, но явно признаёт возможность repeated execution и отсутствие атомарности effect/history [E24]. Checkpoint не даёт exactly-once.

**Для Nox:** поведенческий contract не обязан быть новой платформой: тонкие поля в ApprovedSpec/EvidenceBundle достаточны. Golden/regression/release fixtures должны иметь отдельные IDs и versions. Domain failures становятся reviewed regression assets, а не самописывающимся policy.

### 5.5 AWS Bedrock AgentCore

**Официально подтверждено.** Runtime использует per-session microVM, immutable runtime versions и endpoints для rollout/rollback; session state ephemeral, до 8 часов, не long-term durability [E15]. Gateway/Policy предлагает deterministic external controls и deny-by-default [E16]. Memory поддерживает semantic/user/summary/episodic strategies; episodes/reflections генерируются моделью из прошлых взаимодействий [E17]. Evaluation поддерживает online/on-demand/batch и built-in/custom/third-party metrics [E18]; trajectory exact-order может быть programmatic, correctness/goal assertions — LLM judge.

**Критические границы.** AWS сам указывает: backend обязан связывать user↔session; code внутри VM может получить execution role credentials через metadata endpoint; gateway бесполезен при direct bypass [E19]. Fine-grained memory gateway policy не поддерживает batch operations [E25]. Reflection — **сгенерированная гипотеза опыта**, не independent competence proof.

**Для Nox:** deploy rollback отделить от mission rollback: восстановление version не отменяет внешний effect. Не принимать managed episodic extraction как ground truth. При отсутствии AWS account/need — G/H, не добавлять платформенный слой только ради memory.

### 5.6 LangGraph

**Официально/source подтверждено.** Checkpointer хранит thread state, Store — cross-thread application data [E28]. Interrupt сохраняет state и возобновляет node с начала; код содержит явное `re-executing all logic` [E28]. Python `1.2.22` @ `08a20169…`, MIT для package; sync/async/exit durability modes и retry/cache types существуют.

**Границы.** In-memory checkpoints исчезают при restart; накопление checkpoints требует retention. Exact sequence не всегда подходит: contract определяет обязательный path, а не любой trajectory. Replay/resume требует deterministic tasks и обёртывания side effects; «durable» не значит atomic external effect.

**Для Nox:** G/E: использовать MM DAG/recovery до доказанного gap. Не мигрировать ради checkpoint brand. Из LangGraph перенести разделение thread state / scoped knowledge store и явную семантику replay. T10 — прямой Nox, не LangGraph demo.

### 5.7 Mastra

**Официально/source подтверждено.** Pinned `@mastra/core@1.82.0` tag `6e8dfcb…`, Apache-2.0 для core package [E26]. ToolSearch — BM25 + `search_tools`/`load_tool`, фильтры search/load/active, `includeResolvedTools`, context/in-memory state. Filter errors fail closed [E27]. `injectCatalog`/autoLoad — явный trade-off между schema tokens и extra turns. SkillSearch загружает instructions/resources; cached catalog может отставать, `blockingRefresh` влияет на freshness [E29].

**Границы.** Это search/index над supplied/resolved tools, не discovery marketplace, grant, sandbox или vetting. Context loaded state основан на messages; restore требует current grants. Skill load не competence. Mastra repo имеет отдельную `ee/` source-available license, не распространять Apache-2.0 на него [E30]. Соответствие исторически установленным memory/libsql/mcp pins требует fresh lock, не latest docs.

**Для Nox:** B кандидат **только после fresh pin/wiring proof**. Минимальный diff: per-delegation processor + trusted filter + existing execution wrappers. Не строить новый search engine или загружать весь 4504 registry в prompt.

### 5.8 Cognition Devin

**Официально/VENDOR_REPORTED.** Devin docs рекомендуют независимые повторяемые задачи с объективной проверкой, узкие sessions, code review/CI и разбор траектории [E31]. Session Insights различает useful и misleading knowledge, высокие ACU/retries и частые corrections [E32]. Enterprise docs заявляют 6–12× efficiency gains, но общей controlled methodology/denominator там не дано — не переносить число в Nox [E31]. Старый SWE-bench report: 79/570=13.86% на случайных 25% и отдельный test-driven 23/100; это 2024 task-specific vendor evaluation, не current Devin/universal autonomy [E33].

**Для Nox:** ценность в операционном feedback: ошибка → отсутствующее environment/knowledge/tool → reviewed change. Parallel только для изолированных задач; review capacity входит в cost. Не внедрять proprietary Devin и не предполагать internal architecture.

### 5.9 Intercom Fin

**Официально.** Fin Procedures эксплуатируют состояния Triggered/Pending/Resolved/Handed off/Escalated/Failure; failure drill-down включает broken connector/code condition [E34]. Handoff — отдельный предусмотренный outcome с контекстом, не скрытый fallback [E35]. Resolution зависит от customer feedback/отсутствия просьбы о human help; это **business-specific oracle**, не universal correctness [E35].

**Для Nox:** distinguish finished/resolved/pending/handoff/failure, сохранить conversation/evidence/context при escalation. Не использовать resolution rate как professional acceptance. Требуются Nox-specific hidden cases с фактически правильным результатом и authority checks.

### 5.10 Salesforce Agentforce

**Официально/VENDOR_REPORTED.** Hybrid Agent Script/Atlas разделяет deterministic path без LLM после routing и probabilistic path; deterministic code предпочтителен там, где решение можно выразить как logic [E36]. Platform permissions касаются records/fields; Testing Center и Trust Layer заявлены [E37]. Customer stories содержат конкретные показатели, но это vendor-published cases без общего Nox-like controlled setup [E38].

**Границы.** Внутренний proprietary runtime не выводится из marketing; trust layer не заменяет domain correctness. Salesforce customer metrics не evidence для Nox.

**Для Nox:** typed recipe deterministic/hybrid/BLOCKED — у PM/Head/MM; сохранять actual zero-LLM execution trace после route для T01. Не переносить platform/CRM, если нужна только route policy.

## 6. Сквозное сравнение

| Вопрос | Что объединяет сильные подходы | Что Nox не должен копировать |
|---|---|---|
| Tool discovery | Search/load сокращает context; actual schema/identity разрешаются перед call | Registry listing = trusted/installed/granted; unconditional autoLoad |
| Authority | Deny/approval/limits исполняет host/gateway/downstream | Prompt instruction или model classifier как единственный security boundary |
| Identity | Per-call/agent/user/tenant binding, partition и проверка на handoff | Sticky global approval; service account при разных user ACL |
| Durable work | Checkpoint + version + pending intent + quiescence + terminal | Resume = exactly-once; retry при UNKNOWN effect |
| Knowledge | Immutable source/version/rights/ACL/freshness отдельно от index | Unbounded scrape, post-hoc ACL filter, embedding = authoritative |
| Skills | On-demand, scoped resources, source digest, revalidation | SKILL.md/scripts = validated competence или permission grant |
| Strategy | Deterministic/fixed workflow для известного, LLM для judgment | Multiagent/parallel по умолчанию; model routing как strategy |
| Learning | Production failure → reviewed case → paired eval → controlled release | Lesson/reflection автоматически меняет runtime/policy |
| Evaluation | Output + trajectory + negative controls + cost + domain signoff | Single PASS, majority LLM vote, vendor metric как Nox result |
| Economics | Cost per accepted outcome incl QA/repairs/failed attempts | Tokens subtotal = invoice; OSS license = zero TCO |

## 7. Антипаттерны, которые проверки должны ловить

1. **Approval laundering:** reuse approved snapshot/старый grant после изменения tool schema/args/executor.
2. **Gateway bypass:** side effect возможен напрямую, минуя central policy.
3. **Approval ≠ idempotency:** crash после payment/write, затем автоматический replay.
4. **Parallel guardrail:** input check ещё идёт, а tools уже выполнились.
5. **Discovery escalation:** tool/skill metadata или web content добавляет себе permissions.
6. **Shared in-memory leakage:** anonymous/default thread или singleton memory provider смешивает tenants.
7. **Checkpoint authenticity gap:** хеш/JSON schema выдаётся за аутентификацию issuer/reviewer.
8. **Late acceptance:** новый snapshot PASS меняет terminal прежней paused mission.
9. **Coverage truncation:** фиксированные 6 файлов/prefix текста приняты за полный evidence.
10. **Generated ground truth:** старый output/LLM reflection становится oracle без SME validation.
11. **Leaked held-out:** fixture/criteria/oracle keys попадают solver; transfer на самом деле recall.
12. **Metric substitution:** resolution/trajectory match/LLM score выдаётся за mission accepted или профессиональную квалификацию.
13. **Platform overbuild:** новый scheduler/vector DB/MCP fleet/continuous trainer до доказанного gap.
14. **Hidden fallback:** denied/failed/unknown route превращается в другой tool или расширенную authority без owner.

## 8. Минимальный R2 против R2.x/R3

### Minimal R2 — только доказанный bounded loop

Один owner-approved, низкорисковый, реально полезный профиль: typed immutable spec → gap/strategy → reuse или один vetted read-only adapter → действие в current grants → exact candidate/полный evidence → independent acceptance → durable terminal → scoped experience. Все обязательные T01–T12 из 06 остаются программой R2; один vertical slice **не принимает R2 заранее**. Максимальный claim: named task/domain/scope и условия проверки.

### R2.x — масштабирование после доказательств

- повторяемые source/pack acquisition и revocation в нескольких названных доменах;
- tenant-scoped transfer, version migration, production-derived reviewed regression;
- Windows/browser/new runtimes только с отдельными sandbox/oracles;
- visual/accessibility rubric с qualified human review;
- route learning и более широкий tool catalog, если paired eval показал net benefit.

### R3 — open-world, не ранний deliverable

Новые профессии с prerequisites/authority/oracle/expert gates, generalized competence graph, source/tool/model drift management, controlled runtime improvement. Нет continuous fine-tuning/self-modifying scheduler по умолчанию: это отдельные высокорисковые programs, а не следствие сохранённого lesson.

## 9. Точные будущие проверки Nox

Все ниже — **NOT_RUN**, после отдельного owner approval. Общие prerequisites: fresh current HEAD/status/hash, installed lock/typings, immutable approved spec, equal budgets, direct Nox production path, independent reviewer, complete ledger и rollback.

| ID | Проверка и falsification | Требуемый результат |
|---|---|---|
| NV-01 | Nested `a/x` и `b/x`, >6 files, >12k, binary, mutation during QA, stale receipt | Canonical path/identity, complete typed coverage; stale/mutated candidate не accepted |
| NV-02 | Approval replay/concurrency, changed executor/schema/grant, tampered snapshot | Server-owned current request, одна atomic decision; нет execution при tamper/deny |
| NV-03 | T02 search/load/active + denied/distractors/dynamic IDs + revoke/restart/trim | Только current granted actual tool; valid schema и receipt; measured net cost/latency |
| NV-04 | G2 missing/tampered package, schema drift, no network, revoked OAuth, cancel | Quarantine/deny/cleanup; нет host secrets, orphan process или silent install |
| NV-05 | T04 false/stale/contradictory/retracted/unlicensed/cross-tenant source | Block/qualify с source refs; no unsupported claim, ACL до index/prompt/cache |
| NV-06 | T05 baseline/treatment, changed + hidden held-out fresh agent | Frozen quality/safety/tool metrics; uplift или no-benefit, не recall-only |
| NV-07 | T09 malicious registry/skill/MCP/doc/tool output + benign lookalike | Ни нового grant/effect/secret leak; quarantine + audit; нет глобального overblock |
| NV-08 | T10 interruptions на каждом effect/review/terminal boundary | Cumulative budget, quiescence, no auto duplicate; UNKNOWN reconcile явно |
| NV-09 | T01/T11 deterministic/single/team/hybrid при same input/oracle/budget | Actual call traces и accepted-result economics; no forced winner |
| NV-10 | T12 direct Nox без OpenCode | PM→approval→Head→MM→tools→QA→terminal на novel owner spec; весь scope явно назван |

**Stop conditions:** current source/authority/oracle/budget unavailable; evidence unreadable; external outcome UNKNOWN; protected criteria изменены после результата; любой unresolved effect. В этих случаях BLOCKED/PAUSED/UNKNOWN, не PASS.

## 10. Что остаётся недоказанным

- Current Nox code/wiring/health/acceptance, installed Mastra compatibility, provider health, live schemas и full costs — **UNKNOWN**.
- Ни один внешний framework не был испытан здесь на Nox task; никакой uplift dynamic search, skills, multiagent или route learning не установлен.
- Fin/Devin/Agentforce production numbers — опубликованные vendor/customer outcomes, не независимый Nox benchmark.
- Проприетарные internals Codex/Devin/Fin/Agentforce не восстанавливались; используются только публичные контракты.
- Права на OSS code не равны правам на hosted data, model, docs, examples, enterprise `ee/` или third-party skills.

Сопроводительный `four-contours.md` превращает эти практики в transition-level контракты и будущие gates.
