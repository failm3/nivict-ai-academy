# NOX-R0 — supervised multiagent implementation via OpenCode

Дата: 2026-11-13. Статус: **AUTHORIZED ENGINEERING TASK PREPARED AFTER OWNER'S "ПОГНАЛИ"**, однако этот файл сам по себе **не запускает локальную сессию OpenCode** и не санкционирует платный стресс-тест, деплой, расширение внешних прав или автопополнение Router.Cheap.

## Исходная задача владельца

Начать R0 («single-owner, cancellable, fail-closed runtime»), чтобы привести Nox к безопасному самостоятельному использованию **без OpenCode как пользовательского посредника**. Владелец дополнительно требует, чтобы **сам OpenCode** использовал параллельных специализированных LLM-субагентов для инженерной разработки, а не исполнял всю работу одной моделью. Nox и OpenCode — **разные контуры агентности**.

## Обязательный baseline

1. Прочитай перед началом:
   - \`REPORTS/NOX-OWNER-READINESS-REVIEW-01-2026-11-13.md\`
   - \`CHECKPOINTS/HANDOFF-NOX-2026-11-13-OWNER-READINESS.md\`
   - \`TESTS/AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md\`
   - \`PROMPTS/AWE-E1-PRODUCT-LAUNCH-01-2026-11-12.md\`
   - \`IDEAS/NOX-MANDATORY-PROFESSIONAL-CAPABILITY-PACKS-CONCEPT-2026-11-13.md\`
   Из корня в GitHub \`failm3/nivict-ai-academy/03 - Практика/05 - AWE GROUP/\`.
2. Определи действительный локальный проект, branch, HEAD, git status, незакоммиченные изменения; сохрани manifest и hashes до правок. Учитывай, что код cleanroom может отсутствовать на remote GitHub. Не переписывай исходный \`/goal\`.
3. Проверь версию OpenCode и доступность **нативных subagents**, agent configs, routing по моделям, параллельности, permissions и task/subagent tool. Не предполагается, что возможности документированной новой версии совпадают с текущей установленной. При отсутствии возможности — честно BLOCKED или реализуй безопасный штатный workaround, но не создавай второй runtime-оркестратор ради самого OpenCode.

## Параллельная команда OpenCode

**Выступай как ведущий инженер и интегратор.** При наличии native child sessions запусти разделённые независимые исследовательские подзадачи параллельно, с ограничением числа одновременно запущенных LLM (первоначально ≤3), бюджета и прав. Каждому назначь подходящую из **фактически доступных** модель по работе, без выдуманных model IDs. При сомнении выбирай менее затратную достаточно сильную модель, но security/QA — независимую от автора кода, когда это возможно.

Распределение:

- **R0-A — Lifecycle/Concurrency Engineer**: \`src/agents/lifecycle.ts\`, \`src/utils/storage.ts\`, \`src/api/server.ts\`, \`src/agents/mission-manager.ts\`. Durable single owner/lease, CAS или транзакции, abort propagation, terminal-state write fencing, корректный cancel/resume/recovery; test-first.
- **R0-B — Tool Security Engineer**: \`src/agents/specialists.ts\`, \`src/tools/*\`, \`src/config/mcp.ts\`. Deny-by-default grants (никакого \`allTools\` fallback), безопасная изоляция shell/browser, минимальные права, fail-closed unknown tool, negative tests. Не подключать новые найденные tools и не устанавливать сторонний код до отдельного owner approval.
- **R0-C — QA/Verification Engineer**: сначала read-only audit and independent test design; затем обособленные tests/fixtures на cancel, races, duplicate ownership, dishonest success, tool grant denial, crash-recovery. Для negative tests проверяет реальный код, а не только заглушки. Не смягчать обязательные criteria. Автор production patch не утверждает сам свой QA.
- **OpenCode primary**: координация, artifact-based success, адаптация \`src/agents/recursion.ts\` при необходимости R0 gate, conflict-resolution, интеграция branches/worktrees, единственная проверка end-to-end, финальный отчёт и evidence; **не делай работу Nox вручную**.

Сначала при необходимости один общий небольшой read-only pass, затем параллельная разработка только **независимых** участков. Не позволяй нескольким агентам писать в один файл/worktree одновременно. При пересечении интерфейсов сначала зафиксируй контракт/ownership; работа в изолированных git worktrees или отдельных ветках, затем контролируемая интеграция. Субагентам запрещено самостоятельно менять исходный \`/goal\`, менять секреты, выполнять \`git push\`, \`merge\`, \`deploy\`, запускать платные массовые tests или расширять network permissions. Не отдавай им полные credentials.

Не создавать рекурсивное дерево ради красивой структуры; если в установленной версии subagents не могут порождать потомков — достаточно одному primary OpenCode запускать нескольких sibling-subagents параллельно. Все реальные child sessions, role/model selection, tool actions, durations, token/cost counters и результаты должны оставлять проверяемый trace.

## Scope и приёмка R0 — зафиксированы ДО правок

**P0-1:** Команда cancel/timeout действительно прекращает LLM, subprocess и browser либо fenced их результаты и внешние действия; после завершения kill/cancel нет новых записи/действий от старой миссии. Не обещай невозможного отменить уже принятый внешний side effect: используй idempotency и outcome unknown.

**P0-2:** Два одновременных процесса не получают право завершить/перезапустить одну миссию; нет lost update, двойного resume, ложного orphan и гонок при atomic file rename. Durable ownership/lease/CAS или проверенный transactional alternative.

**P0-3:** Неизвестная capability/tool не даёт \`allTools\`. Нужен минимальный tool grant policy, безопасные sandbox/permission controls для shell/browser, reject unknown/unapproved. Если полноценная изоляция отсутствует — NO-GO, не маскировать частичным allowlist.

**P0-4:** Не считать \`agent.generate()\` успешным deliverable. Проверять реальные вызовы нужных tools, required files, hashes, provenance и исходные acceptance. Исправить повторение identical child request в параллельной рекурсии, если code-level repro подтверждает дефект. Нет ложных COMPLETE.

**P0-5:** Единая offline test command/CI или доказуемая эквивалентная locally reproducible check; неизменяемые acceptance и независимый QA. Доступ к существующему архитектурному плану из Academy не считать отсутствующим только потому, что он не скопирован в локальную папку.

Требуемые тесты: позитивный путь, отрицательные сценарии, cancel на разных фазах, SIGKILL/restart, concurrent approve/resume, denied tool, incomplete artifact, tool timeout, duplicate side effects. Сначала isolated workspace; реально сохранённые \`.awe-data\` не изменять. Baseline и изменения сравнивать на одном замороженном наборе тестов. Результаты кодовых и нагрузочных тестов показывать отдельно. Не выдавать 68/68 narrow tests за full release acceptance.

## Предельные ограничения

- **Никакого платного R0 acceptance/stress** до отдельного согласования владельца. Разрешена только обычная инженерная работа в рамках *уже существующих* Router.Cheap ключей и лимитов. Не увеличивать расходы, auto-top-up, quota или число попыток; соблюдай текущий ключевой предел (в прошлом сообщался $0.80 accounting units), но считай фактический остаток/текущие limits неизвестными до проверки; не печатай secrets.
- Максимум 3 одновременно работающих LLM субагента на первом этапе. Изолировать дорогостоящие child loops; лимиты на retries/calls/tokens, показывать фактическое потребление. Если budget depleted — остановись и отчитайся; не обойти лимиты через новый ключ.
- Не переписывать всю платформу, не добавлять второго planner/agent framework, не менять невиновные модули.
- Не менять чужие незакоммиченные файлы, локальные mission results и их прошлые verdicts.
- Не запускать unsafe real external side effects, installer неизвестных plugins, не выдавать новые OAuth/API grants.
- Без явного одобрения владельца: не push/merge в main, не deploy, не публиковать demo.
- Проверь/redact/rotate по согласованию владельца ранее раскрытые секреты, но не выводи их в logs или GitHub.

## Граница между R0 и Tool Intelligence / профессиональными пакетами

Tool Gateway и dynamic connect/execute, capability-pack (Unslop и др.) — **следующий этап R1**, сразу после R0. R0 должен обеспечить безопасные grants и реальные evidence, которые нужны Gateway; не делай отдельный огромный TI rollout сейчас. В финальном отчёте явно передай R1 adapter interfaces/contracts, иначе R0 будет тупиком.

## Выходные материалы OpenCode

1. Версии OpenCode и реальных native subagents, screenshot/trace или IDs child sessions; количество, роли и фактически вызванные модели.
2. Изменения по файлам и git commits (в безопасной рабочей ветке), список untouched/untracked.
3. Каждое P0: исходный воспроизводимый дефект → патч → негативный тест → PASS/FAIL/BLOCKED.
4. Результаты offline suite со счётчиками, отдельные недоказанные cases, fixture hashes, checkpoint/recovery traces.
5. Независимый reviewer по коду и test oracle, отдельный verdict и остаточные риски.
6. Сводка токенов/стоимости включая subagents, отсутствие неразрешённых расходов.
7. Честный статус \`R0: PASS/PARTIAL/FAIL/BLOCKED\` и рекомендации для R1 Tool Gateway/Capability Packs; никакого self-assessed production READY.
8. Handoff в GitHub/Obsidian с проверенным commit/readback, если доступ есть; если нет — подготовленный файл и явный BLOCKED.

**Не запускай платный большой стресс-тест в рамках R0.** Когда R0 закончен — остановись и предъяви доказательства владельцу перед продолжением.
