# NOX-OWNER-READINESS-REVIEW-01

**Дата среза:** 2026-11-13  
**Объект:** самостоятельная передача Nox владельцу без обязательного посредничества OpenCode  
**База кода:** `446adaea833b0ebade1a21fbda3f71118d19b0d6`, ветка `hotfix/e1-recovery-hotfix-01`  
**Режим проверки:** read-only; без платных API/LLM, новых миссий, установки пакетов, deployment и изменения реальных `.awe-data`

## 1. Решение

**NO-GO для самостоятельной production-передачи владельцу.** Nox уже содержит работающий исследовательский backend и отдельные доказанные end-to-end цепочки, но не имеет достаточных гарантий отмены, изоляции, конкурентной целостности, динамического подключения инструментов и воспроизводимой приёмки.

**Допустимый сейчас режим:** локальная исследовательская эксплуатация разработчиком, в отдельной копии данных, с ручным контролем каждого действия. Это не эквивалент самостоятельной передаче и не production readiness.

Переписывание продукта не оправдано текущими наблюдениями. Рациональнее сохранить полезные Prompt Master, registry/approval TI, artifact model, browser verification и QA gate, а сначала устранить ограниченный набор P0-дефектов runtime.

### Количественная оценка среза

| Наблюдение | Результат | Что это доказывает / не доказывает |
|---|---:|---|
| Сохранённые mission records | 23: 8 `completed`, 11 `failed`, 4 `paused` | Историю запусков, а не 34,8% надёжности текущего кода |
| Свежие бесплатные regression checks | 68/68: recovery 12, resume 16, QA gate 30, artifacts 10 | Узкие offline-инварианты; не полный mission loop |
| `npm run typecheck` | PASS | TypeScript согласованность, не runtime correctness |
| Общая test команда / CI | отсутствует / не найдена | Нет воспроизводимого release gate |
| Текущие checkpoint files | 0 | Нет сохранённого active recovery state на момент среза |
| Доказанная глубина recursive delegation | 0 в единственной instrumented NIVICT-записи | Код recursion есть; реальный дочерний вызов не доказан |
| Доказанная NIVICT browser capture | PASS по сохранённым PNG и `verification.json` | Конкретный Chromium script сработал; не все generic MCP browser wrappers |
| Требуемый acceptance plan | не найден в дереве и Git index | Соответствие ему нельзя ни подтвердить, ни опровергнуть |

Исторические `completed` не повышались автоматически до REAL: формат runtime и tests менялись, повторной независимой проверки этих миссий на текущем HEAD не было.

## 2. Метод и свежие наблюдения

Проверены исходники `src/`, `ti-service/`, package scripts, README, 23 JSON mission records, log files, artifacts, screenshots и сохранённые verification data. Отдельно сверены фактические tool wiring и пути сохранения результатов.

Свежо выполнены только бесплатные offline-команды:

```text
npm run typecheck                              PASS
npx tsx src/tests/lifecycle-recovery.test.ts  12/12 PASS
npx tsx src/tests/resume-policy.test.ts       16/16 PASS
npx tsx src/tests/qa-gate.test.ts             30/30 PASS
npx tsx src/tests/artifact-reconciliation.test.ts 10/10 PASS
```

Эти suites используют временные каталоги/локальные doubles и не вызывают модели. `stage1-integration.test.ts` не запускался: он пишет тестовый artifact в реальный `.awe-data`. `ti-integration.ts`, `probe-usage.ts` и новые миссии не запускались, поскольку требуют live services/API.

До review уже существовали untracked `design-spec.md`, `screenshots/`, `scripts/capture-viewports.cjs`, `scripts/dbg.cjs`, `scripts/verify-nivict.cjs`, `tokens.css`, `tokens.json`. Они не изменялись. Единственный созданный этим review файл — настоящий отчёт.

## 3. Пять главных блокеров передачи

### P0-1 — Timeout/cancel не останавливает работу

- `withMissionTimeout()` делает `Promise.race`, но не передаёт `AbortSignal` и не отменяет `fn()` (`src/agents/lifecycle.ts:128-151`).
- `/cancel` лишь меняет JSON-статус (`src/api/server.ts:166-175`); manager, LLM request, subprocess и browser продолжают работу.
- После `cancelled`/`paused` старый agent может записать artifact или внешний эффект. Нет проверки quiescence и durable ownership по процессу/lease.

**Последствие:** владелец не может надёжно остановить расход, запись или внешнее действие. Это самостоятельный блокер передачи.

### P0-2 — Конкурентное хранилище и ownership небезопасны

- `updateMission()` — read-modify-write без CAS/transaction/lock; одинаковый `.tmp` и `rename` не защищают от lost update (`src/utils/storage.ts:25-29, 68-83`).
- `_missionLocks` объявлен, но не используется; межпроцессной блокировки нет.
- `runningMissions` существует только в одном Node process (`src/api/server.ts:18-19`). Startup reconciliation может принять `running` миссию другого живого процесса за orphan (`src/agents/lifecycle.ts:173-200`; `src/index.ts:15-16`).

**Последствие:** двойной approve/resume, потерянные статусы, смешение результатов и ложное recovery. Atomic rename защищает от частичного файла, но не от гонки состояний.

### P0-3 — Нет deny-by-default исполнения и изоляции

- Specialist при пустом/неизвестном tool match получает **все** инструменты (`src/agents/specialists.ts:125-131`).
- `shell` выполняет произвольную команду через `exec`; `cwd` не проходит `assertSafePath` (`src/tools/index.ts:90-120`). README-утверждение об `execFile` не соответствует этому пути.
- Playwright MCP запускается с `--allow-unrestricted-file-access` (`src/config/mcp.ts:152-169`). Отдельного sandbox runner для discovered tools нет.
- Web fetch общего runtime не имеет защит уровня `ti-service/awe_ti/network.py`; нельзя переносить TI security claims на Node tools.

**Последствие:** ошибка модели или вредоносный ресурс может получить чрезмерные filesystem/network/process возможности. Наличие path check у некоторых file tools не образует sandbox.

### P0-4 — «Success» и оркестрация не связаны с наблюдаемым результатом

- После обычного `agent.generate()` `executeSpecialist()` безусловно возвращает `success: true`; наличие нужного artifact и вызов tool не проверяются (`src/agents/specialists.ts:185-235`).
- `planMission()` просит JSON; direct tool execution Head не становится результатом миссии. При parse failure создаётся fallback executor (`src/agents/head-agent.ts:95-159`).
- `runDelegateCall()` не имеет checkpoint/durable job semantics. При `parallel=true` одинаковый request повторяется несколько раз; массива разных child tasks нет (`src/agents/recursion.ts:235-339`).
- Наблюдаемая NIVICT `delegation_tree.max_depth=0`; реальный recursive child на текущем evidence set не показан.

**Последствие:** запись `success` не доказывает deliverable, повторные дочерние вызовы могут дублировать эффекты, а заявленная recursive autonomy остаётся непроверенной.

### P0-5 — Приёмка и QA неполны и невоспроизводимы как release gate

- `npm test` намеренно завершается ошибкой; CI workflow не найден (`package.json:7-16`).
- QA получает не более 6 artifacts и до 12 000 символов каждого, execution output — до 6 000 (`src/agents/qa-agent.ts:107-120`). Для больших миссий это выборка, не полный аудит.
- Обязательный `AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md` отсутствует в рабочем дереве и Git index.
- TI README ссылается на `tests/test_core_*.py`, но каталог tests в поставленном `ti-service/` отсутствует; заявленный TI suite здесь невоспроизводим.

**Последствие:** зелёные точечные tests нельзя принять за общий допуск; владелец не получает повторяемый процесс release/no-release.

## 4. Что Tool Intelligence реально умеет

### REAL по коду, с указанными ограничениями наблюдения

1. **Read-only поиск из Nox:** `ti_search` обращается к приватному API с Bearer token и поддерживает фильтр approved (`src/tools/ti-search.ts`). `manus_search` — отдельный read-only catalog adapter.
2. **Registry/provenance:** PostgreSQL backend хранит ресурсы, источники, assertions, версии, этапы, тесты и approvals.
3. **Поиск:** lexical fallback реализован; optional local Model2Vec semantic ranking ограничен первыми 5000 кандидатами (`ti-service/awe_ti/registry.py:42-83`; README TI:67-73).
4. **MCP metadata discovery:** official MCP Registry импортируется как metadata; явно не install/invoke (`ti-service/awe_ti/mcp_discovery.py:1-16, 72-75`).
5. **Approval lifecycle:** последовательные этапы, human-attested live tests, свежесть и fingerprint проверяются перед export (`registry.py:126-171`; `exporting.py:8-20`).
6. **Ограниченные collector adapters:** trusted local collector запускается с `shell=False`, allowlisted env и ограниченным набором modes (`ti-service/awe_ti/adapters.py`). Это сбор данных, не runner найденных инструментов.

### PARTIAL / NOT_VERIFIED

- **PARTIAL:** исследовательский control plane и approval registry реализованы, но их live deployment/PostgreSQL health в этом review не проверялись.
- **NOT_VERIFIED:** фактический поиск на текущем service, semantic model, MCP refresh и полный TI tests — сетевые/БД вызовы не выполнялись, tests отсутствуют в срезе.
- **NOT_IMPLEMENTED:** автоматическая установка discovered resource, изолированный функциональный runner, runtime grant для конкретного child, dynamic MCP connect и автоматическая регистрация вызова/результата в Nox.
- **NOT_IMPLEMENTED:** цепочка `discovered → approved → connected → granted → invoked by child → result registered`. Manifest сам указывает `contains_executable_code: false` и не запускает код (`exporting.py:18-20`).

Следовательно, TI — полезный **исследовательский и разрешительный control plane**, а не готовый механизм автономного пополнения исполняемых инструментов.

## 5. Безопасное подключение без второго оркестратора

Не нужно добавлять ещё один planner/agent loop. Рекомендуемая топология:

```text
Owner approval
     ↓
Nox MissionManager (единственный orchestrator)
     ↓ mission-scoped ToolProvider
Deterministic Tool Gateway (не agent и не planner)
     ├─ read: TI approved manifest + exact version/digest
     ├─ check: mission grant, network/filesystem/process policy
     ├─ run: отдельный sandbox worker с timeout/AbortSignal
     └─ emit: invocation, digest, stdout/result, artifact registration

TI registry → только metadata/evidence/approval; не планирует миссии
```

Минимальный контракт:

1. Head просит capability, а не произвольный executable.
2. Gateway возвращает только approved record с immutable version, digest и declared permissions.
3. Владелец/политика выдаёт одноразовый `mission_id + capability + digest` grant; discovered metadata никогда не является grant.
4. Новый код запускается только в sandbox: отдельный пользователь/container, read-only root, явные writable mounts, network deny-by-default, resource/time/output limits.
5. Дочерний agent получает временный narrowly scoped tool handle, не общий `allTools` и не секреты registry.
6. Каждый вызов имеет idempotency key, abort propagation и durable audit; результат становится typed artifact с digest.
7. Ревокация/смена digest немедленно закрывает grant. Скачивание, HTTP 200 и запись в MCP Registry не считаются live test.

Это расширение текущего Nox через детерминированный adapter, а не второй оркестратор. До появления такого контура разрешён только read-only TI search и ручная интеграция reviewed adapters.

## 6. Самостоятельность компонентов

| Компонент | Статус | Основание и граница |
|---|---|---|
| Prompt Master → structured spec | **REAL** | Реализован и виден в исторических mission traces; текущий live rerun не выполнялся |
| Explicit approval | **PARTIAL** | Interactive CLI/API approval есть; one-shot CLI auto-approves (`src/index.ts:48-90`) |
| Head planning | **PARTIAL** | JSON plan/fallback реализован; direct result/tool outcome не является durable mission result |
| Mission Manager | **PARTIAL** | Sequential/batch execution и traces есть; cancel/ownership/success semantics не завершены |
| Recursive specialist factory | **PARTIAL / NOT_VERIFIED** | Код и limits есть; observed NIVICT depth=0, parallel duplicate semantics небезопасны |
| File/shell/web/artifact tools | **PARTIAL** | Использовались в traces; нет общей изоляции и fail-closed grant policy |
| Browser | **PARTIAL** | Сохранённые Chromium screenshots/verification реальны; generic MCP wrappers полностью не приняты |
| MCP | **PARTIAL** | Один статический Playwright client и отдельный TI metadata feed; dynamic registry→connect отсутствует |
| Tool Intelligence | **PARTIAL** | Registry/search/approval код есть; live deployment и исполняемая интеграция не подтверждены |
| QA + gate | **PARTIAL** | 30/30 gate tests и сохранённые verdicts; truncation и LLM dependence ограничивают полноту |
| Persistence/recovery | **PARTIAL** | 12/12 recovery + 16/16 resume tests; нет multiprocess transactionality и durable worker queue |
| Memory | **NOT_VERIFIED** | LibSQL/Mastra configuration есть; cross-resume recall и concurrency не проверены |
| Owner UI | **PARTIAL** | CLI + JSON API; нет полноценного mission/control UI и воспроизводимого owner runbook |
| Windows computer-use | **NOT_IMPLEMENTED** | Указано в roadmap |
| Image generation/visual QA как общая capability | **NOT_IMPLEMENTED** | Screenshots существуют, но не general image-generation/verification pipeline |
| Production deployment/CI | **NOT_IMPLEMENTED / NOT_VERIFIED** | Локальные templates не равны deployed и monitored service |

## 7. Что ломается при параллельных миссиях

| Сценарий | Ожидаемый дефект |
|---|---|
| Два процесса approve/resume одной миссии | Два исполнителя; lost update и повторные внешние эффекты |
| Startup второго Nox при активной миссии | Живая `running` миссия может быть помечена `paused` как orphan |
| Timeout/cancel во время tool call | Старый tool/agent продолжает писать и тратить API после нового статуса |
| Параллельные одноимённые artifacts | Общий tmp filename и отсутствие имени версии допускают перезапись/неоднозначную ссылку |
| Несколько recursive `parallel=true` | Одинаковый child request дублируется; общий in-memory session не durable |
| Большие параллельные deliverables | QA видит только первые/ограниченные fragments; полнота снижается с ростом числа файлов |
| Общий browser/MCP singleton | Нет mission-scoped session/permission isolation; abort одной миссии не изолирован |
| Concurrent memory/mission stores | Нет end-to-end теста SQLite/JSON consistency и recovery после kill |

Это преимущественно код-доказанные риски, а не утверждение, что каждый уже наблюдался в production. Отдельные concurrency failures в сохранённых 23 missions нельзя надёжно отличить от model/provider failures.

## 8. Большой стресс-тест и пределы расходов

Стресс-тест имеет смысл **после** P0-1…P0-4. Запуск текущего опасного concurrency path на реальных инструментах только увеличит риск и расход.

### A. Бесплатный контур — обязательный, лимит $0

Во временном workspace, с fake model provider, local HTTP fixtures и sandbox; без Router.Cheap, внешней сети и реальных `.awe-data`.

| Поток | Объём | Обязательный gate |
|---|---:|---|
| Deterministic mission matrix | 200 миссий × 10 mocked delegations; 20 параллельно | 100% expected state transitions; 0 lost updates; 100% artifact hash/index match |
| Cancel/timeout | 50 вызовов в каждой фазе: model/tool/subprocess/browser | Все execution contexts завершены ≤5 с; 0 записей/сетевых эффектов после cancel |
| Crash/recovery | 50 × SIGKILL + restart на каждой durable boundary | Нет двойного externally visible effect; recovery одним owner; понятный audit |
| Recursive delegation | depth 0–4, fan-out 1–8, repeated/failing children | Distinct tasks, exact limits, нет duplicate execution, durable tree |
| Artifact stress | 1000 mixed text/binary files, collisions, large files | Нет silent overwrite; registry полнота 100%; QA знает omissions |
| Security | 50 malicious manifests/URLs/paths/tool args | 0 unapproved exec/write/network; secrets отсутствуют в logs/artifacts |
| TI contract | 100 synthetic registry records, revocation/digest changes | Metadata никогда не исполняется; revoked/stale/different digest всегда denied |
| Browser | 20 локальных pages, 2 viewports, dialogs/navigation/abort | PNG + trace + console evidence; session и permissions изолированы |
| CI/reproducibility | clean checkout → один documented test command | Все suites воспроизводимы; skipped integration не маскируется под PASS |

### B. Платный контур — только после бесплатного PASS и отдельного разрешения владельца

| Поток | Объём | Жёсткий предел |
|---|---:|---|
| Provider contract smoke | 6 маленьких missions, по одной на основной archetype | ≤$10 и ≤300k total tokens |
| Управляемый stress | 24 missions: research/code/content/data/browser/tool-denial; 4 повторa каждого archetype | ≤$40 и ≤2,7M total tokens |
| Независимая приёмка | Только финальные artifacts + trace; reviewer без права repair | В пределах тех же $50; без скрытого repair loop |

**Общий максимум: $50 и 3M tokens, без auto-top-up.** Если актуальная смета Router.Cheap выше, объём сокращается, а лимит не увеличивается автоматически. Это capped acceptance sample, не статистическая гарантия для всех будущих миссий. Текущие тарифы не запрашивались, фактических новых расходов в review не было.

### Общие release metrics

- 100% миссий имеют spec/approval/model/tool/artifact/cost/final-verdict trace.
- 0 ложных `completed` при отсутствии обязательного deliverable; 0 unauthorized effects.
- 100% cancel/crash tests проходят; flaky retry не засчитывается как чистый PASS.
- В платном sample ≥90% missions полностью принимаются независимым reviewer с первого раза; оставшиеся имеют честный FAIL, а не скрытый repair.
- Для production handoff дополнительно требуется 7-дневный controlled soak с owner-defined лимитом; его стоимость отдельно не утверждать внутри $50.

## 9. P0/P1/P2 и измеримый допуск к передаче

### P0 — до любой самостоятельной передачи

1. Единый durable owner/lease для mission, transactional storage/CAS, защита от double approve и foreign-process reconciliation.
2. End-to-end AbortSignal + subprocess/browser cleanup + terminal-state fencing; cancel проверен отсутствием последующих writes.
3. Deny-by-default tools; никакого fallback на `allTools`; изолированный execution policy и безопасные browser permissions.
4. Success только по наблюдаемому contract: required tool/deliverable/artifact hash; distinct recursive jobs без дублирования.
5. Восстановить/утвердить acceptance plan, собрать единый offline test command и CI; P0 бесплатный stress PASS.

### P1 — после P0, до широкого применения

1. ToolProvider/Gateway + sandbox + scoped grants + invocation audit для TI.
2. Полный evidence index вместо молчаливого QA truncation; targeted verifier по типам artifacts.
3. Воспроизводимый owner runbook, backup/restore drill, cost caps, dashboard и secrets policy.
4. Платный acceptance sample и controlled soak.

### P2 — расширение, не блокер базового контура

Dynamic MCP catalog UX, semantic ranking improvements, Windows computer-use, image generation, production cloud/PostgreSQL migration и дополнительные UI.

### GO-критерий владельцу

Передача допустима только когда все P0 имеют автоматические regression tests, бесплатный stress полностью зелёный, платный capped sample соответствует metrics, владелец самостоятельно по runbook выполняет start → approve → monitor → cancel → recover → export, а независимый reviewer не находит critical/high defects. До этого статус остаётся NO-GO.

## 10. Альтернативы

| Вариант | Оценка |
|---|---|
| **A. Укрепить текущий Nox (рекомендуется)** | Сохраняет доказанные компоненты; наименьший путь к безопасному runtime. Сначала P0, затем TI Gateway |
| **B. Ограниченная owner-supervised передача** | Только local single process, read-only TI, allowlisted tools, отдельные данные и ручной контроль. Дешевле, но не autonomous/production handoff |
| **C. Заменить custom lifecycle на durable execution engine** | Оправдано, если после P0-прототипа CAS/lease/abort всё ещё требуют сложного custom кода. TI остаётся control plane; engine заменяет manager, а не добавляется вторым planner |
| **D. Оставить TI отдельным research registry** | Минимальный риск и стоимость; никакого автономного tool installation. Подходит как безопасная промежуточная эксплуатация |

## 11. Один рекомендуемый следующий этап

**R0 — «Single-owner, cancellable, fail-closed runtime»:** ограниченный vertical slice из одной mocked и одной локальной mission, реализующий durable lease/CAS, abort propagation, terminal-state fencing, deny-by-default tool grant и наблюдаемый deliverable success. Завершается соответствующим бесплатным fault-injection suite и единой CI-командой. TI dynamic installation, Windows и новые UI в этот этап не входят.

Реализация и бюджет остаются решением владельца; в рамках этого review код не изменялся.

## Приложение A. Проверяемые evidence anchors

| Evidence | SHA-256 |
|---|---|
| `.awe-data/25be2dad-039c-4cb2-8667-d4184df47363.log` | `db5c7e82aaf6594971203b7e330b3789c6f5f2f2f6e6572ea4752e7147726d37` |
| `.awe-data/missions/25be2dad-039c-4cb2-8667-d4184df47363.json` | `af02af05a899cf20d07fe2f3f47e3c6e1686ab8c22b9df8dac14aba49d981c29` |
| `.awe-data/missions/e3bf9e21-15c4-4147-9275-c2064d2b475c.json` | `c470a6ef7e3cdfff559d21a3ee7fb28c20f32554b234408503f42751390b2148` |
| NIVICT `verification.json` | `2292933896e731bdf6aba67d54b51fce5fb47345cad989c8c07c63bd55da3542` |
| NIVICT desktop PNG | `41f89291175d60b28dd29b0436194d201e0a194ecd9fca60d7d1789209310a60` |
| NIVICT mobile PNG | `a4132eff2287d8fda7c38cae78ad4e63a8ae2b6dbddda43029157cb2d5b5e177` |

Исходные blob SHA на HEAD зафиксированы для ключевых модулей: lifecycle `75016e2d7b6d0d532eab73d5783379c771d4b79f`, storage `db871eaec06f26e8426d35b8fb5615e93057a4e6`, specialists `b17badac2f75941fd06a65a3735d613fe5e66611`, mission manager `11ccde516900d07f6b31a7e5abca790ea1a933bf`.

**Границы доказательства:** это audit snapshot, а не сертификация безопасности. Сохранённые traces могут относиться к более раннему runtime; новые live LLM, network, PostgreSQL, Docker, Windows и production deployment проверки специально не выполнялись. Прежние отчёты OpenCode использовались только как вторичные указатели, не как независимое доказательство готовности.
