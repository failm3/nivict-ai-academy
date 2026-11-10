# AWE GROUP — полный аудит владельца, v2

**Источник текущего состояния:** локальный архив `awe-full-snapshot-20261110-210707.tar.gz`, SHA-256 `870c364d37cbd3352a5cb01cc8d0f191a65071ec59f2f4c644bbc3b0d41c588c`, 59 entries, собран из проекта `/home/nox/awe-e1-launch-20261110`. Доказательства относятся к **моменту снимка**, а не к вечному онлайн-состоянию. Сверено с предшествующим архивом `awe-full-snapshot-20261110-204749.tar.gz` и исходным `/goal`.

**Метод:** чтение в ChatGPT архивированных AUDIT/CHECKPOINT, runtime-status, session-index, Telegram bridge events, test evidence; сопоставление с историей `nivict-ai-academy` и `awe-group-runtime`. Читались свидетельства тестов, но **не запускался код в пользовательском WSL**. Диагностический архив не содержит полного незакоммиченного исходного дерева и raw session-list API JSON, так что независимую кодовую приёмку и полное восстановление сессий по нему нельзя объявлять завершёнными.

## Короткий вывод

**OpenCode действительно продолжал разрабатывать AWE; сама AWE ещё не показала реальную автономную мультиагентную миссию.** После предыдущего снимка инженер завершил офлайн-проверку схемы LLM-маршрута/бюджета и начал разрабатывать offline `cloud-envelope`. Первая контрольная точка исходного /goal всё ещё `NOT MET`: `real_llm_vertical_slice=NOT_RUN`, `independent_agent_qa=NOT_RUN`.

Второй скрипт v2 выполнил запросы в **правильных проектных каталогах**; `session-active.json` и `original-session-active.json` оба вернули `{"data":{}}`, `session-index.txt` сообщил `LIST_ENTRIES=0` по обеим областям. **Но** raw ответ `GET /api/session` не сохранён сборщиком, и процесс OpenCode работал; свежие исходники обновлялись непосредственно перед архивированием. Невозможно доказать ни активное исполнение именно /goal, ни исчезновение сессии: сначала проверить список в Telegram `/recent` и корректность API метода. Предыдущее утверждение «сессия потеряна» было ошибочно сильным.

## История от начала, без потери границ

1. **Концепция NIVICT/AWE:** корпоративная агентная платформа, Head, Prompt Master, проектные линии, инструменты/registry, оркестратор, память, QA. Архитектура и Canvas — проект; не считать все блоки работающими.
2. **E0:** завершённый узкий контролируемый runtime сценарий — D03 PostgreSQL commit 54, readback, QA 7/7, `OWNER_ACCEPTED`. Это надёжный транзакционный фундамент, не автономный Head.
3. **Astra audit:** установлено отсутствие реального E1 на тот момент, рекомендовала повторно использовать native coordinator вместо второго конкурирующего scheduler.
4. **E1 до текущего /goal:** есть локальные модельные попытки (G1 Python SyntaxError, четыре repair attempts исчерпаны и завершились неуспехом), ограниченные синтетические recruiting испытания, broker и заготовка Router.Cheap, каталог около 4504 кандидатов-инструментов — не активных tool capabilities.
5. **Единый большой /goal E1-LIVE:** сохранить/аудировать → сквозная реальная LLM+tool+memory+independent QA миссия → динамические команды, безопасная параллельность, маршрутизация и приобретение возможностей → реальные испытания → разрешённые восемь направлений CAREER-01. Это не «сделай один тест». 
6. **В течение текущего /goal:** изолирован worktree, сделаны native bridge, durable file journal, agent cursor, lifecycle, agent/task authority, sandbox reviewer, RPC, negative disposition, terminal cancellation; теперь добавлены offline LLM budget/route contracts и незавершённый `cloud-envelope`.

## Кто сейчас работает и как связаны компоненты

```text
Владелец → Telegram bridge [Node PID 113, service active]
                        ↓
              OpenCode server [PID 361, loopback 49374]
                   │ внешняя инженерная LLM
                   ├─ анализирует/пишет код AWE в launch worktree
                   ├─ запускает отдельные тесты E1
                   └─ читает evidence → корректирует реализацию
                                   ↓
                    AWE E1 тестовый runtime
 mission → ограниченный Head → native coordinator (PG fixture 5545)
             → worker/tool/file journal/cursor
             → sandbox reviewer → durable verdict/terminal receipt
```

**OpenCode не является Head AWE.** Telegram не является AWE runtime. Отдельные AWE worker/reviewer процессы возникают в тестах, но **нет доказательства**, что непрерывная многосоставная AWE миссия реально работает в фоне. Пользователь может видеть активный инженерный OpenCode, не означающий, что AWE уже автономна. AWE пока не управляет OpenCode; внешний инженер развивает систему и тестирует её.

Процессы в снимке: Node PID 113, OpenCode PID 361 с CWD `/home/nox`, PostgreSQL PID 266 и 2008; TCP слушали 5432 и 49374. Production E1 5433 не был доказан доступным; синтетическая тестовая PG 5545 использовалась только внутри fixture. Обычная локальная Ollama не слушала 11434. `opencode service status` возвращал локальный сервис на 28894.

## Новые факты по сравнению с v1

### A. Новый завершённый offline маршрут моделей и бюджета

- `E1/launch/ROUTE-BUDGET-AUDIT.md`, `route-budget-dry-run.mjs`, `run-route-budget-dry-run.mjs`, `evidence/route-budget.json` и `evidence/route-budget-rehearsal.json`.
- **56/56 новых контрактных проверок**, **96/96 combined cloud/QA3 checks**, **442/442 baseline**; zero fail/skips, `source_stable=true` по свидетельствам.
- Проверялась **одна выдуманная модель для четырёх ролей**: Head, worker, reviewer, repair; варианты трактовки общего/дополнительного `$20`; freshness, единая сумма/reservations, запрет при UNKNOWN/HOLD; 10 сценариев порядка reserve → markSending → settle с in-memory accounting spies.
- Результаты `SIMULATED_ADMIT_ONLY`; model `launch/synthetic-single-model`; `paid_send_enabled=false`, `real_network_calls=0`, `native_D09_verified=false`. Это **не** подключённый Router.Cheap, не реальная маршрутизация и не доказанное финансирование.

### B. Начат bounded cloud-envelope adapter

В `runtime-status.txt` появились новые `E1/live/cloud-envelope.mjs`, `cloud-envelope.test.mjs`, `E1/launch/cloud-envelope-cold.test.mjs`, test-only `envelope-child/journal/fixture`. Файлы изменялись вплоть до времени записи снимка.

План в `CHECKPOINT.json`: host-owned single allowlisted route + versioned full transcript/tool envelope + строго ограниченные роли и отклонение попыток изменить модель/route до reserve. **Готового cloud-envelope evidence и завершённой проверки в этом снимке нет**. Считать `IN_PROGRESS`, не `PASS`.

### C. Ранее завершённый QA / terminal contour

- Базовая offline регрессия: **442/442 PASS**.
- `review-terminal`: **307/307 PASS**, включая атомарный host-only terminal receipt/cancellation в частном тестовом PG, 14 окон SIGKILL и UNKNOWN=HOLD. По умолчанию реальное включение отключено; native acceptance не выдано.
- Все earlier combined counts (31,48,61,81,93,126,154,169,197,236,262,268,307,96) могут пересекаться и не суммируются.
- В public scripted holdouts **три смыслово неправильных PASS** прошли технический RPC/hash gate, внешний evaluator их обнаружил. Технические хеши не доказывают качество реального semantic reviewer.

## Файлы и состояние Git

- Original `/home/nox/awe-e1-live-runtime`, ветка `opencode/e1-live`, HEAD `29db82e`.
- Launch `/home/nox/awe-e1-launch-20261110`, ветка `awe/e1-autonomous-launch-20261110`, HEAD всё ещё `29db82e`, **259 untracked files** (в предыдущем диагностическом снимке было 242). Tracked diff (23 files) вырос до 2 392 insertions / 127 deletions, но этот stat **не включает untracked**.
- Не зафиксирован новый Git commit из-за отсутствующего configured author identity по AUDIT. Подготовленные приватные архивы/patch в backup не заменяют обычную проверяемую историю Git. `failm3/awe-group-runtime` main не равен нынешнему локальному worktree.
- Последний локальный checkpoint изменялся перед записью снимка; после него обновлялись cloud-envelope тестовые файлы. Поэтому статусы из checkpoint и свежих файлов необходимо различать.

## Не готово

1. Реальный authorised Router.Cheap transport через native D09 actual-spend и принятый ресурс PG 5433. `new_paid_generations_initiated_by_tools=0` относится только к текущему launch tooling; это **не** стоимость разработки OpenCode и не история всех локальных LLM-попыток.
2. Полный real-LLM Head → worker → tool → независимый semantic reviewer → cold PG readback acceptance.
3. Dynamic team generation, safe parallel workspace owner/leases, task-dependent model/tool routing, bounded self-extension, реальная прикладная CAREER-01.
4. Независимо доказанное качество семантического QA, отдельные адекватные holdout-проверки.
5. Полная фиксация/публикация текущего рабочего дерева и подтверждённое исполнение конкретного OpenCode /goal session из API.

## Каким маршрутом идёт разработчик

Разработчик последовательно делает safety/persistence/QA, затем QA fail/terminal close, теперь **переходит к финансовой авторизации и формату безопасного модельного запроса**. Это технически объяснимый маршрут: нельзя платить, повторять отклики, принимать ложный PASS без ledger/QA. В то же время бизнес-ценность ещё не получена; нужно не позволять бесконечное расширение offline протоколов вместо первой реальной end-to-end миссии. Первая checkpoint `first_checkpoint_met=false`.

## Где уже требуется участие владельца

**Сейчас:**
- Выбрать **один точный разрешённый Router.Cheap key file path** локально (сам токен не передавать), **точный model ID**, и означает ли бюджет `$20` **TOTAL_KEY_SPEND** или **INCREMENTAL_ALLOWANCE**. OpenCode правомерно не запускает платное E1 без этих условий. Срок жизни/текущий расход самого инженерного OpenCode отдельно уточнять в его провайдере.
- Для Git выбрать реальный `user.name` и `user.email` для этого worktree, не назначать выдуманный email, безопасно коммитить scoped файлы без `.private`/ключей/PGDATA.
- В Telegram проверить `/recent` или `/status`, увидеть конкретную активную сессию /goal и её рабочую папку. **Не запускать ещё один /goal, не делать /abort по этому снимку.** Скрипт v2 работал в нужных CWD, но API list не был сохранён и возвращал нулевое число отобранных сессий; причина неизвестна.

**Позднее:** approve production E1 resource/credential binding и реальные outbound действия CAREER-01 (отклики/письма/публикации), CV/портфолио и scope аккаунтов.

**Не требуется:** вручную кодить вместо OpenCode, сбрасывать исторические E0/G1 попытки, создавать новые глобальные поручения, принудительно выключать агента или включать unrestricted browser/shell.

## Следующие контрольные рубежи

1. Зафиксировать/продолжить текущую OpenCode работу без потери контекста; завершить, протестировать и отчитаться по `cloud-envelope`; корректно коммитить изменения.
2. Со стороны владельца дать Router.Cheap grant (path/model/total-vs-incremental) и разрешённый ресурс; со стороны инженера — actual-spend provider ACK, input-token bound, одна модель/роут, native D09 ledger/UNKNOWN safe.
3. **Первая реальная LLM вертикаль** на безопасных публичных или синтетических данных с проверенным readback и реальным независимым reviewer. Только это закроет checkpoint 1.
4. Динамические подагенты, параллельность, маршрутизатор моделей/инструментов и ограниченное приобретение новых возможностей.
5. Разрешённые прикладные направления CAREER-01 с реестром вакансий, CV/портфолио, QA, согласованными внешними действиями и мониторингом.

**Итог:** OpenCode продолжал вносить новые файлы и расширять E1 safety/cloud contracts. Саму AWE нельзя пока назвать запускающей самостоятельные миссии. Сессию OpenCode нельзя считать «утраченной» на основании этого снимка; API session discovery остаётся отдельной задачей диагностики. До реальной LLM-вертикали owner needs key/model/$20, а разработчик — cloud envelope + D09.
