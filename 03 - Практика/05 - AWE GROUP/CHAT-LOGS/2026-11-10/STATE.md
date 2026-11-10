## Исправление к предыдущему выводу об OpenCode-сессии

**Внимание:** при последующей проверке выявлена ошибка диагностического скрипта `awe_full_snapshot_readonly.sh`: проектный каталог `$R` был указан для чтения файлов, но скрипт не выполнял `cd "$R"` перед вызовами `opencode api`. При запуске из Windows CMD запросы могли работать в другом контексте проекта. Проверялся старый ID, а новые ID не перечислялись. **Пустой `/api/session/active` и 404 в том архиве нельзя использовать как доказательство потери или остановки /goal.** Исправлен v2 скрипт, который сначала переходит в worktree и проверяет список/active для launch и original. Требуется повторный срез. Не предпринимать восстановление/abort без новой проверки.

# AWE GROUP — checkpoint, 2026-11-10 (на момент введения CHAT-LOGS)

Источник: ранее переданные пользователем диагностические логи и AUDIT/CHECKPOINT в ChatGPT; это **срез**, не онлайн-проверка GitHub-версии E1 runtime.

- Цель действующего большого `/goal`: построить реальную автономную мультиагентную AWE GROUP на основе E0/E1, затем передать CAREER-01 (8 направлений). Не подменять большой /goal одним тестовым заданием.
- OpenCode: сессия `ses_e3a47ffd4ffeQRGUXN5dr8rOk6`, рабочая область `/home/nox/awe-e1-launch-20261110`, ветка `awe/e1-autonomous-launch-20261110`. Подтверждено API: `running` и `location.directory` указывает на новую рабочую область.
- Telegram мост после `/detach` и `/recent` вновь отображает новую рабочую область и продолжение вывода.
- Аудит E1/launch/AUDIT.md: `PARTIAL / NO-GO real LLM launch`; `first_checkpoint_met=false`; реальные платные вызовы E1 и полноценная реальная LLM vertical-slice-миссия не подтверждены.
- Последний локальный checkpoint: базовая офлайн-регрессия 442 PASS; task-admission combined 126 PASS; process-review / отдельный QA OS process — разработка на тот момент продолжается. Эти счётчики пересекаются, не складывать.
- OpenCode сообщил о приватном архиве и рабочем worktree. На локальном E1 worktree Git-коммит ещё не создан из-за отсутствия Git author identity; не выдавать файлы worktree за опубликованные в GitHub.
- Для платного теста в AUDIT указаны блокеры: точная авторизация ключа Router.Cheap, model ID и определение общего/дополнительного лимита $20. Нельзя делать вывод, что тесты с fixture доказывают real LLM autonomy.
- **Оригинал большого /goal получен от владельца и сохранён дословно** в `03 - Практика/05 - AWE GROUP/E1-LIVE-AUTONOMOUS-LAUNCH-ORIGINAL-GOAL-2026-11-10.md`; исходное сообщение: `CHAT-LOGS/2026-11-10/0003-user.md`. Этот текст — первоисточник, пересказы не должны ему противоречить.
- В оригинале ровно 7 пунктов плана и **отдельная первая контрольная точка** (аудит + блокеры + реальный LLM → инструмент → память → независимый QA); достижение checkpoint **не завершает** задачу: далее динамические команды, параллельность, маршрутизация, самодоработка, real-world проверки и начало CAREER-01. Восемь направлений CAREER-01 в оригинале не перечислены; их нужно извлечь из утверждённых материалов, не придумывать.
- В оригинале лимит Router.Cheap `$20` и «только разрешённая модель», однако **не указаны** точные file path ключа, model ID и трактовка дополнительного/общего лимита; платные операции блокируются по состоянию аудита до явного выбора полномочий.
- Новое требование владельца: сохранять каждое сообщение в отдельной папке GitHub, владелец согласен на публичный риск. Реальный постоянно работающий auto-collector **не установлен**.

## Дополнение: текущий срез 2026-11-10 19:50 МСК

Источник: переданная владельцем команда чтения активной сессии и `E1/launch/CHECKPOINT.json`; оригинальный вывод сохранён в `CHAT-LOGS/2026-11-10/0005-user.md`. Обновлённый отчёт: `REPORTS/2026-11-10-E1-LIVE-TEAM-STATUS-1950-MSK.md`.

- Сессия OpenCode `ses_e3a47ffd4ffeQRGUXN5dr8rOk6` возвращена `running`; `first_checkpoint_met=false`; `status=PARTIAL_BLOCKED_PAID_IDENTITY_AND_MODEL`.
- Новая QA работа: `process-review` combined 154 PASS; `semantic-review` 169; `review-transition` 197; `reviewer-rpc` 236; `review-disposition` 262. Это пересекающиеся наборы тестов; последние evidence 19:50, `skips=0` по checkpoint.
- Изоляция: отдельные QA процессы, в поздних проверках bwrap namespaces + read-only snapshot; техническая изоляция не доказывает семантическую независимость модели. `semantic_review_quality=SCRIPTED_TRANSPORT_ONLY_REAL_LLM_SEMANTIC_ACCURACY_NOT_TESTED`.
- `real_llm_vertical_slice=NOT_RUN`; `independent_agent_qa=NOT_RUN`; `new_paid_generations_initiated_by_tools=0`, стоимость OpenCode сессии `NOT_MEASURED`.
- Три явных блокера: локальный путь разрешённого Router.Cheap ключа, model ID, трактовка $20 лимита (общий/дополнительный). Никаких платных операций E1 до явного разрешения.
- Worktree содержит неотслеживаемые QA файлы; их существование не подтверждает commit/push. Не останавливать исходный большой /goal, по-прежнему не завершены этапы 3–6.

## Дополнение: события исполнителя 2026-11-10, 20:11–20:25 МСК

Дословное Telegram-сообщение пользователя: `CHAT-LOGS/2026-11-10/0006-user.md`. Инженерная оценка: `REPORTS/2026-11-10-E1-LIVE-STATUS-UPDATE-2025-MSK.md`.

- OpenCode сообщил о sandbox holdouts, scripted четырёхходовых проверках Head → worker → reviewer tool read → reviewer verdict; три **семантически неверных PASS** прошли RPC/hash gate, но были выявлены evaluator. Принцип: hash integrity не эквивалентен correctness, фиксировать критический gap до real LLM acceptance.
- Новая проверка: **268/268 PASS**, 0 FAIL / 0 SKIP; baseline **442/442 PASS**. Наборы пересекаются, не суммировать. По сообщению агента приватный проверенный архив — 258 файлов. Это self-reported результаты, самостоятельный запуск тестов из ChatGPT не выполнялся.
- Native cancellation тесты: отдельно авторизованные root и child с известным результатом допускают CANCELLED, без каскада; UNKNOWN/SENDING остаётся HOLD. Автоматический terminal lifecycle ещё не подключён. Агент приступил к host-only terminal port и receipt для atomic FAIL/BLOCKED + root/children native cancellation; документ `E1/launch/TERMINAL-LIFECYCLE.md`.
- В 20:11 и 20:24 возникало `ECONNRESET`; сообщения с новым прогрессом и командой на чтение SQL есть в 20:25. Не делать вывода о полной остановке и не отправлять /abort автоматически. Для нового состояния проверить `opencode api get /api/session/active`.
- Первая контрольная точка остаётся `NOT MET`. Нет подтверждённой реальной LLM E1 vertical slice. Платный транспорт заблокирован до определения разрешённого локального ключа, exact model ID и трактовки лимита $20. Не переформулировать или заменять исходный большой /goal.

## Личный сводный отчёт для владельца (10 ноября, доказательства до 20:25)

Владелец запросил простой полный статус, **не** сообщение для команды. Подготовлен и проверен GitHub-файл `REPORTS/2026-11-10-AWE-SIMPLE-STATUS-FOR-OWNER-2025.md`, исходный запрос `CHAT-LOGS/2026-11-10/0007-user.md`.

Коротко: OpenCode строит AWE; фундамент native execution/cursor/file journal/atomic lifecycle/QA sandbox и тестовая отмена продвинулись. 268/268 + 442/442 PASS — **самоотчёт** и пересекающиеся наборы. В scripted QA holdouts три неверных PASS прошли технический hash/RPC gate, внешний evaluator их заметил. На 20:25 host-only terminal lifecycle ещё создавался; реальные LLM vertical slice, динамические команды, параллельность, маршрутизация и CAREER-01 **не доказаны**. Первая контрольная точка `NOT MET`. Блокеры owner — путь авторизованного Router.Cheap ключа, exact model ID, трактовка $20. Есть `ECONNRESET`; текущее здоровье после 20:25 отдельно не проверено. Не использовать `/abort` по одному сообщению об ошибке, не подменять исходный /goal.

## Полный локальный снимок: latest verified state

Пользователь прикрепил архив `awe-full-snapshot-20261110-204749.tar.gz`, SHA-256 `e0d97d64c8ff57ee09e24cead68b0fac25e7baa91a77c0cf374881f2f063f974`; запись о вложении `CHAT-LOGS/2026-11-10/0010-user.md`. Содержимое прочитано из 51 файла; полный пользовательский отчёт: `REPORTS/AWE-GROUP-FULL-OWNER-AUDIT-v1.md`, commit `36adfc09`.

**Новый прогресс после предыдущего среза:** в `E1/launch/CHECKPOINT.json` теперь зафиксирован `review_terminal_combined_pass=307`, `442` baseline, `first_checkpoint_met=false`, `real_llm_vertical_slice=NOT_RUN`. Реализована и fixture-проверена дополнительная **optional host-only terminalAuthority**: атомарный receipt + exact root/children cancel после FAIL/BLOCKED, 14 SIGKILL windows, UNKNOWN => HOLD, ноль повторов model sends; production отключён, не native acceptance.

**Критическое изменение в живой системе:** snapshot `session-active.json` содержит `{"data":{}}`, запрос старого OpenCode session ID `ses_e3a47ffd4ffeQRGUXN5dr8rOk6` вернул `SessionNotFoundError`, todo/messages/children по старому ID — HTTP 404. OpenCode server **PID 361** продолжал слушать `127.0.0.1:49374`, Telegram node PID 113, PostgreSQL PID 266/2008; последние файлы и AUDIT/CHECKPOINT изменены около 20:45 МСК. **Нельзя утверждать, что /goal прямо сейчас продолжает исполняться; причину исчезновения сессии не установили.** Не отправлять /abort и новый /goal вслепую; найти сессию через /recent/историю либо безопасно продолжить из checkpoint.

Git original `/home/nox/awe-e1-live-runtime` и launch worktree всё ещё на `29db82e`; launch worktree 242 untracked файлов, новый commit не подтверждён (Git author identity отсутствует). Тестовый PG 5545 изолирован; реальный D09 и production PG не проверены. Параметры owner blocking paid E1: **путь к разрешённому Router.Cheap ключу (без секрета), exact model ID, USD20 общий/дополнительный лимит**. Утверждение `0 new paid generations` относится только к текущим инструментам launch, не ко всей истории E1 (локальный Qwen G1 действительно использовался) и не к стоимости OpenCode сессии.

Исторический полный E0 принят с реальным commit 54 и QA 7/7; это не полная агентность. CAREER-01 восемь направлений восстановлены из `E1/launch/CAREER-01.md`. Всесторонняя архитектура и инженерный процесс объяснены в полном отчёте; текущая AWE действует **как вызываемая OpenCode тестовая среда**, не как отдельный постоянно автономный управляющий сервис.

Полный отчёт сохранён в GitHub и прочитан обратно; не подменять его устаревшими промежуточными отчётами.

## Текущий контрольный снимок v2 (проектно scoped; supersedes вывод о сессии)

**Архив:** `awe-full-snapshot-20261110-210707.tar.gz`, SHA-256 `870c364d37cbd3352a5cb01cc8d0f191a65071ec59f2f4c644bbc3b0d41c588c`, 59 tar entries. Полный аудит по v2: `REPORTS/AWE-GROUP-FULL-OWNER-AUDIT-v2.md`, commit `2d9b4f0`. **Для восстановления читать v2 вместо v1**, далее первоисточники AUDIT/CHECKPOINT по необходимости.

- v2 скрипт перед вызовами API выполнил `cd /home/nox/awe-e1-launch-20261110`, отдельно проверил original; active в обоих вернул `{"data":{}}`; parsed session list показывает 0 entries, но **raw list был удалён и неизвестна корректность endpoint/парсера**. OpenCode (PID 361) и Telegram node (PID 113) работали, последние файлы `cloud-envelope` менялись прямо перед снимком. Нельзя выводить из данных «сессия исчезла» или «сессия точно активна». Пользователь видит работу в Telegram. Попросить `/recent` или `/status` без `/abort`.
- **Новая инженерная работа:** `ROUTE-BUDGET-AUDIT.md` и офлайн-синтетический dry-run: `route_budget_contract_pass=56`, `route_budget_cloud_combined_pass=96`, baseline `442`; фиктивная одна модель в ролях head/worker/reviewer/repair, трактовки total/incremental $20, UNKNOWN HOLD, network 0, D09 НЕ проверен. `E1/live/cloud-envelope.mjs`, `cloud-envelope.test.mjs`, `E1/launch/cloud-envelope-cold.test.mjs` создан/изменён, **ещё нет evidence о завершённой проверке**.
- Предыдущая QA terminal проверка сохраняет `307/307` PASS; тесты пересекаются, сумма не показатель общего качества.
- `CHECKPOINT.json`: `status=PARTIAL_BLOCKED_PAID_IDENTITY_AND_MODEL`, `first_checkpoint_met=false`, `real_llm_vertical_slice=NOT_RUN`, `independent_agent_qa=NOT_RUN`. `new_paid_generations_initiated_by_tools=0` — не все расходы OpenCode.
- Git launch branch `awe/e1-autonomous-launch-20261110` HEAD `29db82e`, **259 untracked** (ранее 242), 23 tracked diff files; код ещё не коммичен из-за отсутствующей Git identity по AUDIT. `awe-group-runtime` GitHub main НЕ включает автоматически свежие файлы.
- Участие владельца сейчас: разрешённый локальный key path (НЕ секрет), точный Router.Cheap model ID, $20 TOTAL_KEY_SPEND или INCREMENTAL_ALLOWANCE, утверждённые Git author name/email в worktree, проверка Telegram /recent. Позднее — production PG grant, HH/внешние действия.
