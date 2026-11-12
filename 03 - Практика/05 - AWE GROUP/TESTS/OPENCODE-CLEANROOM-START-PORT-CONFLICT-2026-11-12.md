---
project: AWE GROUP
type: execution-checkpoint
date: 2026-11-12
status: startup-blocked-by-managed-service-port; no implementation started
source: user-supplied terminal log
privacy: no API key included
---
# OpenCode clean-room: запуск блокирован занятым служебным портом

## Доказанный результат

- Новый рабочий каталог: `/home/nox/awe-group-cleanroom-20261112`.
- Созданы `.gitignore`, `opencode.json`, `AGENTS.md`; `git init -b main` выполнен; `.oc-isolated/{home,config,data,cache,state}` создано.
- Запуск `/home/nox/.local/bin/opencode` после отдельного `HOME` и `XDG_*` завершился:
  ```
  Error: Managed service port 49374 on 127.0.0.1 is already in use by PID 398 (opencode serve --service --port 49374).
  Configure another port with `opencode service set port <port>`.
  ```
- Фраза пользователя «Начинай разработку ...» была введена в Bash после ошибки старта и вызвала `Начинай: command not found`. **OpenCode не получил задачу; разработка не началась**.
- Router.Cheap key вводился скрытым `read -r -s`, **значение неизвестно; не записано и не скопировано в этот отчёт**.

## Корректное решение

- Не убивать PID 398, не удалять старую OpenCode службу, не менять прежние конфиги.
- В той же изолированной `HOME/XDG_STATE_HOME` выбрать другой свободный локальный managed port, например `19474`, через `/home/nox/.local/bin/opencode service set port 19474`; проверить `service get`, затем запустить OpenCode.
- При новом терминале повторно экспортировать изолированные HOME/XDG_*, проверить секретную переменную без печати её значения, ввести её скрыто при необходимости.
- Сообщение «Начинай разработку...» вводить **только после открытия OpenCode TUI**.
- Документация V2 поддерживает `providers`, `permissions` и `@opencode/ai/providers/openai-compatible`; текущий `opencode.json` по этому признаку не отвергнут. Реальная совместимость модельных ответов и API-ключа ещё не проверялась.
- GitHub issue: https://github.com/anomalyco/opencode/issues/54267 ; official docs https://opencode.ai/docs/providers/ .
- Старый AWE/NIVICT и связанные проекты не читать в новом clean room. Это checkpoint беседы для архива, не входные материалы нового инженерного исполнителя.

**Никаких платных вызовов, локальных модификаций или остановок процессов этим логом не подтверждено.**
