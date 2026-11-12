---
project: AWE GROUP
date: 2026-11-12
type: diagnostic-and-correction
status: suggested; not executed by user yet
---

# Наблюдение OpenCode без обращения к служебному API

## Сообщение пользователя
Запущена команда `/home/nox/.local/bin/opencode api GET /api/event` из PowerShell -> WSL2 с isolated HOME/XDG в новом clean-room. Вывод:
`Error: Server process exited with code 1`; `Managed service port 49374 ... already in use by PID 398 (opencode serve --service --port 49374)`.

**Вывод:** CLI наблюдателя не обнаружил существующий service, автоматически попробовал запустить второй на 49374 и упёрся в занятый порт. Это не означает прекращения текущей разработки. Известная в OpenCode причина — несовпадение service registration по `XDG_STATE_HOME` между процессами: https://github.com/anomalyco/opencode/issues/56708. Не нужно менять порт, стартовать/останавливать service, выключать auth.

**Корректировка неверного предыдущего совета:** `opencode api` может запускать managed server при проблемах discovery; следовательно он не чисто пассивная команда для нашего сценария.

**Безопасный обход:** подписка на существующий лог, прочитанный ранее audit script из `.oc-isolated/data/opencode/log/opencode.log`:

```powershell
wsl -d Ubuntu -- bash -c 'tail -n 100 -F /home/nox/awe-group-cleanroom-20261112/.oc-isolated/data/opencode/log/opencode.log | tee /mnt/c/Users/1/Downloads/AWE-OpenCode-WATCH.log'
```

Только чтение; не обращается к API и не создаёт сервис. Возвращает последние 100 строк и стримит новые, сохраняет в Windows Downloads. `Ctrl+C` останавливает только окно наблюдения.

**Ограничение:** сервисный лог не эквивалентен точной полной текстовой транскрипции сообщений. Если нужен дословный transcript всех модельных ответов и дочерних сессий, потребуется найти правильную DB/сеансы локально через read-only inspection профиля, а не бездумно перезапускать OpenCode.

Подтверждающая официальная документация: https://opencode.ai/docs/troubleshooting/ (Read logs, предупреждение что `api` может запустить service). Не публиковать raw logs с личными данными и секретами в публичный репозиторий.
