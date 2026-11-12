---
type: owner-workflow-preference
project: AWE GROUP
date: 2026-11-12
status: instruction-provided; not yet applied
---
# OpenCode — пользователь хочет автономные разрешения без десятков подтверждений

Пользователь показал TUI OpenCode в clean-room `/home/nox/awe-group-cleanroom-20261112`. Агент спрашивает подтверждение shell-команды чтения зависимостей Mastra (`npm show @mastra/core@1.41.0 dependencies` и обработка вывода `python3`/`grep`). Ранее пользователь вручную подтвердил около 10 команд и хочет убрать подтверждения для текущей разработки.

**Решение:** использовать штатный режим OpenCode V2 `--auto` после возвращения в shell, **не** редактировать весь основной конфиг и не удалять existing запреты:

```bash
cd /home/nox/awe-group-cleanroom-20261112
opencode --continue --auto
```

Перед этим: утвердить текущую безопасную команду `Allow once`, затем выйти из TUI через `/exit`. Режим `--continue` продолжает последнюю сессию; `--auto` auto-approves permissions that are not explicitly denied, не отменяет `deny`.

Важная оговорка: у текущего WSL процесса права обычного пользователя и доступ к хостовым директориям, если shell команды попадают туда. `external_directory` deny не является ОС песочницей; статический scanner shell может не распознать динамические обращения. Для безопасной полной автономии нужна отдельная OS/container sandbox, не только отдельная папка. Не запускать untrusted код с полным доступом к персональным файлам/ключам.

Официальные источники:
- https://docs.dev.opencode.ai/docs/cli/ — TUI flags `--auto`, `--continue`.
- https://opencode.ai/docs/tui/ — `/exit`.
- https://opencode.ai/docs/permissions/ — deny override, caveat shell/full host authority.

**Статус:** это запись подсказки пользователя, а не свидетельство изменённых настроек, завершённых тестов или продолженной разработки. Старые AWE/NIVICT исходники не использовались.
