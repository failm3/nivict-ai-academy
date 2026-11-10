---
date: 2026-11-10
role: assistant
source: ChatGPT AWE GROUP conversation
capture: authored response summary
sequence: 0025
---

OpenCode продолжает интеграцию AWE. Сейчас он проверяет взаимодействие исполнителей с механизмами управления задачами и PostgreSQL.

- `AWE_LIVE_NATIVE_TEST=1`: native-test режим.
- `AWE_LIVE_PORT=5545`: отдельная тестовая PostgreSQL, а не production.
- `ack-scope-native-debug.tap`: чтение результатов теста.
- `task-admission.test.mjs`: изучение тестов допуска задач.
- `cursor-child.mjs`: изучение реализации state/cursor дочерних процессов.
- `grep function run|nativeExecution|async run`: поиск исполнительного кода.

Эти записи не подтверждают платный Router.Cheap вызов. Отсутствуют результаты тестов, поэтому статус pass/fail неизвестен. Не нужно вмешиваться в самостоятельную инженерную работу OpenCode по действующему /goal.
