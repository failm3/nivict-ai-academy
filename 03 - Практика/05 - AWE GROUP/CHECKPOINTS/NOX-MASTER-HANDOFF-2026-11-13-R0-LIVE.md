# AWE GROUP / NOX — MASTER HANDOFF FOR NEXT CHAT
**Контрольная точка:** 2026-11-13, после передачи R0 в OpenCode (01:56 UTC / 04:56 МСК).
**Документ:** авторская точная реконструкция текущего обсуждения, проверенных журналов, ссылок и решений. В GitHub сохранён точный отправленный OpenCode prompt; этот документ НЕ притворяется машинным дословным экспортом всех сообщений ChatGPT.
**ВНИМАНИЕ:** у этого handoff есть важное обновление относительно прежнего HANDOFF-NOX-2026-11-13-OWNER-READINESS.md: **R0 УЖЕ БЫЛ ОТПРАВЛЕН в OpenCode и фактически начал исполняться**. Не говорить «ожидает запуска», не просить владельца отправить его снова.

## 0. Старт новому ассистенту — прочитать сначала

1. Этот `CHECKPOINTS/NOX-MASTER-HANDOFF-2026-11-13-R0-LIVE.md`.
2. `PROMPTS/NOX-R0-EXACT-SENT-TO-OPENCODE-2026-11-13-0156UTC.md` — **точный текст, фактически доставленный OpenCode**.
3. `REPORTS/NOX-OWNER-READINESS-REVIEW-01-2026-11-13.md` — полный независимый аудит с P0, QA и рисками.
4. `TESTS/AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md` — заранее созданный контракт приёмки из Academy, который локальный OpenCode ранее не нашёл.
5. `CHAT-LOGS/NOX-CURRENT-CHAT-CONTINUITY-2026-11-13.md` — хронология реплик и решений этого чата.
6. `IDEAS/NOX-MANDATORY-PROFESSIONAL-CAPABILITY-PACKS-CONCEPT-2026-11-13.md` — идея владельца, следующая к обсуждению после R0.
7. `RESEARCH/AWE-LLM-PROVIDER-MARKET-RESEARCH-2026-11-12.md` — полное исследование провайдеров (загруженное из пользовательского файла).
8. Регистр OpenCode: `https://github.com/failm3/awe-opencode-recordings/blob/main/LATEST.md`; наблюдатель: `https://github.com/failm3/awe-group-observer/blob/main/LATEST.md`.

## 1. О чём проект

AWE GROUP — универсальная автономная мультиагентная система. Основной автономный агент получил имя **Nox** от владельца. OpenCode является **инженером-разработчиком Nox**, а не пользовательским интерфейсом Nox и не его внутренним оркестратором.

Целевой рабочий путь: `владелец → Prompt Master → Head → динамические подагенты/команды → модели + реальные инструменты → независимый QA → артефакт + долгосрочная память + восстановление`. В итоге: **владелец напрямую ставит задачу Nox и получает проверяемый результат, OpenCode не обязателен для повседневного выполнения.**

Техническая база последнего наблюдаемого runtime: local Ubuntu WSL2 Node/TypeScript и Mastra, LibSQL/JSON mission state, PostgreSQL-backed Tool Intelligence с read-only API; OpenCode разрабатывает в `/home/nox/awe-group-cleanroom-20261112`. Оригинальная инженерная branch в аудите `hotfix/e1-recovery-hotfix-01`, commit `446adaea833b0ebade1a21fbda3f71118d19b0d6`. Локальные изменения по умолчанию **не доступны** в remote `failm3/awe-group-runtime`; GitHub observer скрывает имена веток и не может давать diff.

У владельца есть правило **не терять решения между чатами**, фиксировать значимые сообщения, идеи, задания и evidence в GitHub/Obsidian, с проверенным commit и обратным чтением; не считать запись в GitHub фактом исполнения программы.

## 2. История первой реальной миссии Nox и оценка владельца

- Первая попытка Stage4 с частично ручным fallback OpenCode НЕ доказывала автономность.
- Затем Nox действительно исполнял NIVICT landing mission `25be2dad-039c-4cb2-8667-d4184df47363` через Head→делегирование (design/coder/writer/devops/analyst) и resume; в артефактах реальный responsive HTML/CSS/JS, Chromium screenshot desktop 1280×720 и mobile 375×667, улучшены tap targets и CTA.
- Изначальный и targeted repair `e3bf9e21-15c4-4147-9275-c2064d2b475c` завершены **failed**: независимый QA GPT-6 Astra установил **13/14 PASS, overall FAIL**, поскольку требуемого README/manifest не было. `executeSpecialist` мог сообщить `success=true`, хотя обязательный артефакт отсутствовал.
- Владелец как профессиональный продуктовый дизайнер оценил **визуальный дизайн 2/10**, но признал, что появился работающий и последовательный первый прототип. 2/10 — **экспертная дизайн-оценка**, 13/14 — **технический QA**, их не смешивать.
- Пользователь **явно переключил фокус с дизайна на архитектуру**: когда сможет дать Nox поручение напрямую без OpenCode?
- Локальные пути: `/home/nox/awe-group-cleanroom-20261112/.awe-data/artifacts/25be2dad-039c-4cb2-8667-d4184df47363/nivict-landing/index.html` и `reports/E1-NIVICT-autonomous-final.md`. Известны локальные коммиты `bc4f57b`, `446adae`. Не утверждать, что они отправлены в GitHub.

## 3. Проведённый независимый аудит OpenCode

В 2026-11-13 01:16 UTC OpenCode получил `NOX — INDEPENDENT READINESS REVIEW`; завершил в 01:30 UTC. Полный отчёт из payload записи в Session Recorder реконструирован и проверенно сохранён в Academy: `REPORTS/NOX-OWNER-READINESS-REVIEW-01-2026-11-13.md`.

**Итог аудита: NO-GO для самостоятельной production-передачи Nox**; допустим только локальный контролируемый исследовательский режим.

Тестовая база в отчёте: TypeScript typecheck PASS и 68/68 узких offline регрессионных проверок — recovery 12/12, resume 16/16, QA gate 30/30, artifact reconciliation 10/10; **не полноценный acceptance**, не big stress. В 23 сохранённых миссиях 8 completed, 11 failed, 4 paused, но это разные версии runtime, нельзя вычислять текущую вероятность успеха.

### Пять конкретных критических P0

1. **P0-1 cancel/timeouts**: `withMissionTimeout()` использует `Promise.race` без реального AbortSignal; `/cancel` меняет статус, но agent/process/browser могут продолжать выполнение и запись.
2. **P0-2 state races**: `updateMission()` — read-modify-write без durable CAS/transaction; `runningMissions` only in-memory и unsafe orphan reconciliation; возможны double approve/resume, lost writes, foreign-process takeover.
3. **P0-3 excessive tools**: `src/agents/specialists.ts` имеет небезопасный fallback на allTools при непонятном tool match, shell `exec` без полноценной sandbox, Playwright `--allow-unrestricted-file-access`; нельзя разрешать внешнюю автономность до deny-by-default.
4. **P0-4 dishonest success and weak recursive orchestration**: `executeSpecialist` после `agent.generate()` может вернуть `success=true` без проверки артефакта; parallel recursion может запускать identical child request; реальная глубина рекурсивных подагентов в instrumented NIVICT mission = 0.
5. **P0-5 incomplete release QA**: нет воспроизводимого единого CI/test gate; QA анализирует усечённую выборку (до шести artifacts, ограниченная длина); обязательный acceptance plan не был доступен в локальном checkout (в Academy он есть).

Вывод OpenCode: **не переписывать всё; закрыть P0 сначала**, потом Tool Gateway/Capability Packs и платные испытания. В audit есть подробные evidence file anchors и hashes.

## 4. Tool Intelligence ≠ реальные подключённые инструменты

Существующие каталоги: порядка 4504 кандидатов (исторический scope) и 3415 реестровых entries Manus/PG; частично реализованы `ti_search`, `manus_search`, provenance, approval workflow. Каталог/поиск есть, **но он не доказывает динамического MCP/API/CLI подключения к любому найденному инструменту**.

Пока отсутствует доказанная сквозная цепочка `discovered → approved → connected → mission-scoped granted → invoked by Head/child → result registered + QA`. Есть отдельные реальные file/shell/search/browser вызовы, но не универсальный connector gateway.

OpenCode предложил не второго AI-планировщика, а детерминированный **Tool Gateway** между TI registry и Nox: immutable digest+version, scoped grant, sandbox worker, invoke audit, abort/idempotency, typed artifact. Динамическое исполнение после R0 — приоритет **R1**.

## 5. Новая идея владельца: обязательные профессиональные плагины

Владелец выдвинул идею **«мультисистемы обязательных плагинов»**. Уточнение: речь не только о file/memory/search technical tools, а о **профессиональных стандартах качества по направлениям**. Для дизайн-миссий ключевой пример **Unslop** — бороться с AI-slop, помочь переходить к профессиональному интерфейсу; плюс профессиональные templates/starters, UI/a11y/audit навыки. Для coding — static analysis/tests/security; для marketing — источники, методики и проверка метрик.

Рабочее название **Professional Capability Packs / Mandatory Quality Contracts**: пакет за направлением или типом deliverable; Nox/Agent Factory выдаёт соответствующему специалисту approved skills/tools/templates, а QA контролирует реальное применение. **Не добавлять второй каталог или отдельный оркестратор**. Не приравнивать запуск Unslop к гарантии профессионального результата. Разделять skill-инструкции и настоящий MCP/API/CLI execute. Эта идея **не утверждена к реализации**, она отложена до завершения текущей R0 работы. Полный текст: `IDEAS/NOX-MANDATORY-PROFESSIONAL-CAPABILITY-PACKS-CONCEPT-2026-11-13.md` и исходное зерно `IDEAS/NOX-MULTISYSTEM-REQUIRED-PLUGINS-IDEA-SEED-2026-11-13.md`.

Пользователь сказал: **«Он закончил задачу, проверяет задачу, вот, и дальше потом продолжим обсуждать мои идеи»**, затем потребовал проверить журнал. Мы нашли readiness audit, после чего R0 запущен.

## 6. Предложенная последовательность развития

- **R0 (текущий, УЖЕ В ИСПОЛНЕНИИ)** — cancel propagation, durable mission owner/concurrency, fail-closed grants/sandbox, artifact-based success, общая воспроизводимая offline QA. Чистое и безопасное ядро; OpenCode с собственной командой разработчиков.
- **R1 (НЕ запущено)** — dynamic Tool Gateway: поиск→разрешение→подключение→выдача подагенту→real invoke→QA; затем профессиональные пакеты как domain-specific обязательные контракты.
- **R2 (НЕ запущено)** — большой supervised стресс-тест: бесплатные synthetic/chaos/fault injection, затем с отдельным разрешением бюджетный live sample (OpenCode предлагал до 30 live missions, $50 и 3M tokens, только после отдельных owner approvals). Цифры **предложения**, не разрешённые расходы.
- **R3 (НЕ запущено)** — владелец напрямую даёт поручения Nox, управляет approvals, видит tracing/cost/artifacts, без постоянного OpenCode. После полного P0+R1+stress нужна ограниченная пилотная эксплуатация/controlled soak (OpenCode предлагал семь дней).

Точнее: **R0 сам по себе не даёт production-ready Nox**. Решение GO принимается после evidence и owner acceptance, не на основе заявления агента.

## 7. Мультиагентная работа самого OpenCode

Владелец отдельно предложил, чтобы **OpenCode САМ вызывал параллельных LLM-субагентов** в помощь разработке Nox (два разных контура: OpenCode-build team / Nox operational agents).

Последний актуальный owner prompt прямо требует:
- Primary OpenCode — главный инженер и интегратор.
- **Агент A Runtime Engineer**: lifecycle, storage/CAS/leases, cancellation, crash/recovery.
- **Агент B Security & Tools Engineer**: deny-by-default grants, shell/browser/MCP isolation.
- **Агент C Independent QA Engineer**: независимые negative/chaos/integration tests, неизменяемый oracle.
- Максимум **3 одновременно работающих LLM-субагента**, выбранные реально доступные модели, isolated worktrees/branches; no concurrent write to same file; real child IDs + model/tool/time/cost traces.
- Функциональность subagents зависит от установленной версии OpenCode. Не имитировать текстовыми «ролями». При отсутствии штатной поддержки — честно BLOCKED или safe fallback. Не добавлять ещё один оркестратор.
- OpenCode может вести обычную инженерную работу через существующие ключи/лимиты, но **не** запускать платный большой stress, увеличивать бюджет, менять keys, ставить неизвестные packages, push/merge/deploy без отдельного владельческого решения.
- Нельзя менять первоначальный `/goal`, уничтожать текущие/старые mission evidence и untracked файлы.
- Требуемый финальный artefact: `NOX-R0-FINAL-ENGINEERING-REPORT.md`, P0 по отдельности PASS/PARTIAL/FAIL/BLOCKED, независимый QA, evidence, SHA, costs, actual child sessions. Не продолжать самовольно к R1.
- **Первая черновая версия prompt** лежит `PROMPTS/NOX-R0-SUPERVISED-MULTIAGENT-IMPLEMENTATION-2026-11-13.md` (с ней linked GitHub issue `https://github.com/failm3/awe-group-runtime/issues/14`).
- **Владелец потребовал переписать промпт** — черновик показался «странно написанным». Ассистент написал новый более прямой и понятный.
- **ИСТИННОЙ фактически отправленной версией** является `PROMPTS/NOX-R0-EXACT-SENT-TO-OPENCODE-2026-11-13-0156UTC.md`, которая содержит **13 237 символов оригинального пользовательского ввода** без ручной переформулировки.

## 8. Последнее LIVE состояние — критически важно

В 2026-11-13 **01:56 UTC (04:56 МСК)** OpenCode Recorder зафиксировал `session.inbox.enqueued` с последним владельческим prompt `# AWE GROUP / NOX — R0: УКРЕПЛЕНИЕ АВТОНОМНОЙ СИСТЕМЫ`. Сессия `ses_e32ac7a53ffe6UVPua2Nam7Gmu`, каталог `/home/nox/awe-group-cleanroom-20261112`. Источник:
`https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/01-56/part0000.txt`

В 2026-11-13 **01:57 UTC** первичный OpenCode написал: «I'll first snapshot the current tree and verify the supported subagent/model mechanisms. Then I'll run the three engineering tracks in isolated copies, integrate only disjoint changes, and require independent negative-test evidence before any final verdict.» Далее в журнале зафиксированы реальные tool calls, в т.ч. shell для git branch/HEAD.
Источники: `https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/01-57/part0000.txt` и `LATEST.md`, где уже есть части за 01:58 UTC.

**Статус:** R0 **STARTED / RUNNING OR STATUS NOT YET VERIFIED**. Доказаны получение задания и первые действия по baseline. Ещё НЕ доказаны: созданные реальные child sessions, параллельные LLM, code patch, PASS P0, стоимость или итоговый отчёт. При новом запросе «проверь работу» следует читать новые Recorder minute parts, финальный отчёт и Observer. Не утверждать, что OpenCode завершил или что он точно всё время работает только из факта `PROCESS_PRESENT`.

Последний прочитанный Observer срез 2026-11-13T01:55:07 UTC `#670`, процесс OpenCode `PROCESS_PRESENT`; stale после 15 мин; HEAD observer `29db82e7...` но это может быть другой локальный snapshot. Последний Recorder индекс на момент этого handoff содержал до `01:58 UTC`. Новая сессия может продолжиться, журнал обновляется.

## 9. Контроль бюджета и безопасности

- Исходная история Router.Cheap содержала ключевые лимиты порядка $0.80 *accounting units* в отдельном контуре, **фактический текущий лимит и баланс неизвестны**, нельзя обещать API-комфорт или делать auto-top-up.
- Пользователь разрешил обычную разработку через разрешённые модели и бесплатные offline tests, **не разрешил** платный большой load/stress, установку новых внешних packages, расширение rights, изменение секретов, push/merge/deploy.
- Ранее в recorder выявлялись потенциально чувствительные значения; избегать воспроизведения, требуется отдельная безопасная ревизия/ротация по согласованию.

## 10. GitHub фиксации, уже выполненные в этом чате

Ранее создано и проверено:
- `DECISIONS/NOX-READINESS-TOOLS-AND-STRESS-PLAN-DRAFT-2026-11-13.md` — обоснование приоритетов и стресс-плана.
- `RESEARCH/AWE-LLM-PROVIDER-MARKET-RESEARCH-2026-11-12.md` — полный исходный report по LLM providers из вложения.
- `PROMPTS/NOX-OWNER-READINESS-REVIEW-01-2026-11-13.md` — read-only аудит OpenCode, затем действительно отправлен.
- `REPORTS/NOX-OWNER-READINESS-REVIEW-01-2026-11-13.md` — точная копия full report, восстановлена из Session Recorder write tool.
- `CHECKPOINTS/HANDOFF-NOX-2026-11-13-OWNER-READINESS.md` — предыдущая точка передачи, **устарела в части запуска R0**.
- `CHAT-LOGS/NOX-READINESS-STRATEGY-DIALOGUE-2026-11-13.md` — обсуждение и цитаты владельца.
- `IDEAS/NOX-MULTISYSTEM-REQUIRED-PLUGINS-IDEA-SEED-2026-11-13.md` и `IDEAS/NOX-MANDATORY-PROFESSIONAL-CAPABILITY-PACKS-CONCEPT-2026-11-13.md` — идея профессиональных плагинов.
- `DECISIONS/NOX-IDENTITY-AND-OWNER-DESIGN-FEEDBACK-2026-11-13.md` — имя Nox и экспертная оценка прототипа.
- `PROMPTS/NOX-R0-SUPERVISED-MULTIAGENT-IMPLEMENTATION-2026-11-13.md` — первоначальный вариант R0.
- `https://github.com/failm3/awe-group-runtime/issues/14` — GitHub issue-трекер R0, был создан и проверен.
- `PROMPTS/NOX-R0-EXACT-SENT-TO-OPENCODE-2026-11-13-0156UTC.md` — ТОЧНЫЙ последний текст, отправленный в OpenCode. **Главный source of truth по R0 prompt.**

## 11. Как продолжать в следующем чате

Владелец хочет **без потери контекста** и без необходимости повторять информацию. Когда он придёт, открой этот файл, точный R0 prompt, readiness report и свежие Recorder/Observer. Скажи главное: **R0 уже запущен в OpenCode; идёт инженерное укрепление пяти P0; Tool Gateway/Unslop — следующий этап, не текущий**. Если пользователь говорит «проверь работу», смотри журнал текущей сессии, реальные child sessions, changes/tests и блокеры. Если хочет обсуждать свои новые идеи, возвращайся к профессиональным обязательным плагинам после понимания R0 статуса.

**Не обещать автоматическую запись каждого будущего сообщения или работу в фоне, если автоматизации не реализованы.** Все фактически выполненные GitHub writes — только с commit SHA и обратным чтением. Здесь содержательная полнота истории, оригинальное отправленное задание, причинно-следственные решения и ссылки; не утверждать, что этот документ содержит побуквенный экспорт всех assistant/user turns.
