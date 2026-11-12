# AWE GROUP — независимая проверка OpenCode (read-only)

Дата отчёта: 2026-11-12. Evidence cut-off: 19:02 UTC / 22:02 МСК (последний Recorder); Observer verified publication 19:00:05 UTC.
Режим: только GitHub Recorder/Observer, GitHub remote и существующая owner-approved задача. **Локальную WSL-машину и живые API пользователя напрямую не проверяли.**
Действующее задание: ../PROMPTS/AWE-E1-PRODUCT-LAUNCH-01-2026-11-12.md.
GitHub-источники:
- https://github.com/failm3/awe-opencode-recordings/blob/main/LATEST.md
- https://github.com/failm3/awe-group-observer/blob/main/HEALTH.md
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/18-40/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/18-47/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/18-50/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/18-53/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/18-59/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/19-00/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/19-01/part0000.txt

## Исполнитель и версия

OpenCode: внешняя инженерная сессия, workspace /home/nox/awe-group-cleanroom-20261112; branch feature/awe-e1-product-launch-01.
Локальные коммиты, видимые в Recorder:
- 92fc381 — код исправлений Stage 1;
- c086191 — дополнительные доработки и фиксация Stage 1 (заявлен самим OpenCode);
- 6e3e176 — импорт и capability search каталога Manus;
- db5a271 — новый AWE tool manus_search в реестре, 2 файла, 132 добавленные строки.
Идентификация локальной ветки и SHA — из команд OpenCode, не independent SHA readback на пользовательском WSL.

## Подтверждённые наблюдения

1. Stage 1: реализованы src/agents/qa-gate.ts, recursion.ts, lifecycle.ts, связанные изменения Mission Manager. Ранее зафиксированы 30/30 регрессионных QA тестов и отдельное сообщение Stage 1 Integration Tests: ALL PROBES PASSED. Ошибки TypeScript в тестах исправлялись; затем OpenCode получил компиляцию без ошибок. Этого недостаточно для полной независимой E2E-приёмки реальной двухуровневой агентной миссии.
2. Stage 2: OpenCode исследовал кандидатов на улучшение, пытался подключить Playwright MCP к собственному окружению. Обнаружена проблема Chromium browser discovery; baseline wrapper работает. В журналах нет независимого A/B-доказательства ускорения OpenCode. OpenCode заявил о завершённой документации Stage 2.
3. Stage 3: 3415 / 3415 Manus записей импортированы в изолированную схему manus_catalog PostgreSQL; SQL readback показал 3415 записей. Отдельный API /health сообщил catalog_size 3415. После исправления JSON/list ошибки OpenCode сообщил о четырёх успешных поисковых тестах, включая negative test. Далее создал src/tools/manus-search.ts, подключил в src/tools/index.ts; Git commit db5a271. Важно: этот search tool — доступ к метаданным, не автоматическое разрешение на произвольное исполнение найденных кандидатов.
4. На 19:01Z OpenCode объявил Stage 1–3 завершёнными и начал подготовку Stage 4 (миссии NIVICT), изучая текущую спецификацию. **Нет подтверждения сквозного реального вызова manus_search из Head И дочернего агента с policy enforcement**, поэтому Gate 3 по исходному строгому контракту не следует считать независимо PASS.
5. До evidence cut-off не обнаружены завершённый, запущенный и проверенный рабочий сайт NIVICT; Gate 4 NOT_VERIFIED.
6. Recorder опубликовал запись до 19:02 UTC, Observer показывал 0 consecutive publication failures с last success 19:00 UTC. Это подтверждает наблюдение/публикацию, но не отсутствие аварий самого runtime.
7. Remote failm3/awe-group-runtime main: pushed_at 2026-11-11T12:08:07Z. Новые локальные коммиты Stage 1–3 на remote main не подтверждены; PR #10 по состоянию проверки — прежний черновик. Локальные коммиты не равны опубликованному production branch.

## Gate assessment (независимая оценка, не самоотчёт исполнителя)

| Gate | Наблюдаемое состояние | Почему не полный независимый PASS |
|---|---|---|
| 0 Baseline/safety | PARTIAL / evidence incomplete | Не подтвердили финальную owner-grade секретную чистоту/backup и полный baseline |
| 1 Critical fixes | PARTIAL (major progress) | Отдельные тесты PASS; нет полного негативного E2E/head→child→grandchild proof и финального acceptance packet |
| 2 Tools for OpenCode | DOCUMENTED / no measured uplift | Playwright MCP integration blocked by browser environment; A/B benefit не показан |
| 3 Tool Intelligence | PARTIAL (catalog + API + registry implemented) | Нет доказанного вызова из Head и реального ребёнка с grants/policy |
| 4 NIVICT website by AWE | NOT_STARTED/NOT_VERIFIED at cut-off | Нет самостоятельного работающего продукта, артефактов и независимой приёмки |

Статус «complete» в заметках OpenCode означает его собственный отчёт, а не owner acceptance.

## Риски, не скрывать

- В Recorder во время диагностики PostgreSQL/TI встречались похожие на секреты значения (18:11–18:13Z). Не воспроизводить их, проверить круг публикации/доступы; если действующие, ротировать. Доказанной ротации нет.
- Некоторые быстрые integration probes проверяли загрузку модулей, не успешную многоагентную работу.
- Нет доказательств, что сам OpenCode делегировал задачи субагентам в текущей сессии; механизм AWE recursion написан, но доказательство живой работы отдельная задача.
- Не ослаблять оригинальные QA acceptance criteria ради PASS.

## Что ждать дальше

Первый ключевой следующий outcome — **AWE сама получает задание NIVICT через User→Prompt Master→Head, формирует реальную команду, вызывает tools/models, строит и тестирует frontend, сохраняет артефакты, независимый QA подтверждает неизменённое ТЗ**.
Только после закрытия E1 — запрос независимого мнения OpenCode и принятие владельцем следующего узкого этапа. Предлагаемый будущий AWE-ARCHITECTURE-ACCEPTANCE-01 записан отдельно; не запускать его автоматически.

Связанные заметки:
- ../DECISIONS/OWNER-PRODUCTION-STRATEGY-IDEAS-2026-11-12.md
- ../TESTS/AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md
