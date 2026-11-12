---
type: owner-supplied-evidence
project: AWE GROUP
date: 2026-11-12
status: Hermes CLI identity verified; no tests run
---

# Подтверждённый Hermes Agent Windows — локальная диагностика

Пользователь выполнил PowerShell в ходе read-only preflight:

```text
PS C:\Users\1> hermes --version
Hermes Agent v0.22.2+2645.g7058601 (2026.9.24) · stable · local 7058601bf5cd
Install directory: C:\Users\1\AppData\Local\NIVICT-Workspace\runtime
Install method: git
Python: 3.14.7
OpenAI SDK: 2.24.0
Update available — run 'hermes update'
```

Начало `hermes --help`:

```text
usage: hermes [-h] [--version] [-z PROMPT] [--usage-file PATH] [-m MODEL]
              [--provider PROVIDER] [--reasoning LEVEL] [-t TOOLSETS]
              [--resume SESSION] [--no-restore-cwd] [--in DIR]
              [--continue [SESSION_NAME]] [--worktree] [--accept-hooks]
              [--skills SKILLS] [--yolo] [--pass-session-id] [--checkpoints]
              [--ignore-user-config] [--ignore-rules] [--safe-mode] [--tui]
              [--native] [--cli] [--dev]
              <command> ...

Hermes Agent - AI assistant with tool-calling capabilities

positional arguments:
  <command>             Command to run
    chat                Interactive chat with the agent
    model               Select default model and provider
    moa                 Configure Mixture of Agents provider/model slots
    fallback            Manage fallback providers
    worktree            Audit and reclaim accumulated git worktrees
    browser             Real-profile browsing helpers
    secrets             Manage external secret sources
    egress              Manage the iron-proxy egress credential-injection firewall
    migrate             Migrate configuration for retired models or deprecated settings
    codex-runtime       Manage optional codex app-server runtime
    gateway             Messaging gateway management
```

## Инженерный вывод

- Это действительно **Hermes Agent**, не одноимённое неизвестное приложение.
- Движок встроен в `NIVICT-Workspace/runtime`, т.е. **shared production-like folder**: до изолированного теста нельзя делать `hermes update`, менять конфиги, запускать agent с доступом к существующему workspace.
- Hermes Agent явно имеет CLI инструменты и режимы безопасной работы (`--safe-mode`, `--ignore-user-config`, `--in`, `--worktree`), но реальные гарантии изоляции/моделей/памяти/делегирования пока **NOT_TESTED**.
- Дополнительное действие P0: чтение git state `git -C <runtime> rev-parse --show-toplevel`; `git -C <runtime> status --short`; просмотр `hermes chat --help`/`hermes model --help`. Не читать и не публиковать ключи, токены, конфиги.
- Docker из предыдущего вывода доступен, образы/контейнеры пусты; Agent Zero пока не развёрнута.
- Вся текущая работа — диагностика. Ни одной модели не вызывали, исходный NIVICT Workspace не меняли.
