---
project: AWE GROUP
type: read-only-observability
date: 2026-11-12
status: command-proposed-not-executed-by-assistant
---

# Пассивное наблюдение за живой разработкой OpenCode

Владелец хочет получать **поток фактических действий** OpenCode, включая вывод исполнителя и subagent/tool events, без остановки TUI и без нового запроса к Claude на отчёт. Отдельное окно PowerShell, работающий OpenCode не трогаем.

Поскольку в начале clean-room OpenCode был переведён на порт 19474, предложена read-only подписка на официальный OpenCode API `GET /api/event`:

```powershell
wsl -d Ubuntu -- bash -lc 'curl -NsS http://127.0.0.1:19474/api/event | tee /mnt/c/Users/1/Downloads/AWE-OpenCode-LIVE.log'
```

Факт API endpoint: https://opencode.ai/docs/api (Event, `GET /api/event`), experimental native events. Это SSE, а не screen recording/terminal transcript. Получает новые events **только после подключения**, возможна потеря событий при разрыве/переполнении, и данные могут содержать credentials или личную информацию. Точный тип полей зависит от server event. Файл `AWE-OpenCode-LIVE.log` создаётся на Windows. Остановка наблюдателя `Ctrl+C` не должна останавливать отдельную OpenCode TUI.

Для **истории до подключения** нужен CLI `opencode session export <ID> --sanitize` для всех главной/дочерних сессий. Ранее audit export дал ноль, вероятно из-за использования Windows CLI, а не WSL `/home/nox/.local/bin/opencode` и несоответствия XDG профиля. Исправленный повторный запуск уже существующего audit script:

```powershell
wsl -d Ubuntu -- bash -lc 'OPENCODE_BIN=/home/nox/.local/bin/opencode bash /mnt/c/Users/1/Downloads/awe_opencode_audit_capture.sh'
```

Скрипт сам выставляет XDG/HOME профиля нового clean-room. Ожидаемый ZIP с историей/кодом/логами — только если реальное storage и CLI соответствуют текущей service. Не обещать 100%-ного восстановления, если события не сохранялись.

Не публиковать raw SSE на GitHub: может содержать секреты. Никакой команды `run`, `service restart`, `session cancel` не требуется. Пользователь управляет моментом остановки записи и передачи файла.
