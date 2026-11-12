---
type: owner-supplied-preflight
date: 2026-11-12
project: AWE GROUP
status: READ_ONLY_CHECK_COMPLETE; no LLM launch
---

# Hermes: чистая установка и пустая тестовая директория (12.11.2026)

Подтверждено PowerShell пользователя:

```powershell
$runtime = "$env:LOCALAPPDATA\NIVICT-Workspace\runtime"
$test = "$env:USERPROFILE\AWE-Tests\Hermes"
git -C $runtime status --short
# (пустой вывод — рабочее дерево чистое)

New-Item -ItemType Directory -Force -Path $test | Select-Object FullName
# C:\Users\1\AWE-Tests\Hermes

Get-ChildItem $test -Force | Select-Object Name
# (пустой вывод — директория создана и пуста)
```

Ранее подтверждено: `hermes --version` = v0.22.2+2645.g7058601 (stable); runtime расположен внутри NIVICT-Workspace; Docker Desktop жив, контейнеры/образы пока отсутствуют; OpenCode в WSL.

## Коррекция прежнего плана

- `--in DIR` задаёт CWD, а **не OS sandbox**.
- `--safe-mode` — troubleshooting: отключает пользовательский config, memory/rules, plugins и MCP; **не означает sandbox** и не подходит как единственная проверка полноценного агентного дерева с Skills/MCP.
- `--ignore-user-config` может всё ещё загружать `.env` credentials; отсутствие в CLI явного бюджетного ограничения делает платный запуск недопустимым до согласования ограничений провайдера.
- Для реального теста рассмотреть собственный `HERMES_HOME` и разрешённый рабочий каталог; это изолирует Hermes state, но не OS user's file privileges. При необходимости контейнерный backend.
- Первый следующий шаг: **только read-only** выяснить доступность локального Ollama и моделей; технический тест рекурсивного делегирования по старой/ограниченной Qwen 4B без успешного tool-calling нельзя считать репрезентативным.

Источники: https://hermes-agent.nousresearch.com/docs/user-guide/configuration ; https://hermes-agent.nousresearch.com/docs/reference/cli-commands ; https://hermes-agent.nousresearch.com/docs/integrations/providers .

Реальный запуск, платные LLM, изменение настроек, обновление Hermes — НЕ выполнялись.
