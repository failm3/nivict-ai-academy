---
type: observability-debug
project: AWE GROUP
date: 2026-11-12
status: error-diagnosed; fix-proposed-not-yet-tested
---

# OpenCode LIVE.log: 401 Unauthorized

Владелец прислал `AWE-OpenCode-LIVE(1).log`: ровно 64 байта и одна строка:
```json
{"_tag":"UnauthorizedError","message":"Authentication required"}
```
Это значит: предыдущий unauthenticated `curl -NsS http://127.0.0.1:19474/api/event` не получил события. **Нельзя делать вывод о состоянии разработки или подагентов из данного файла**. API использует парольные credentials (по умолчанию генерируемые service). Не запрашивать пароль у пользователя и не отключать авторизацию, не перезапускать сервис.

Официальная документация: OpenCode CLI имеет `opencode api GET /api/event`, который сам использует local service discovery+auth. Ссылка: https://opencode.ai/docs/troubleshooting/ ; https://opencode.ai/docs/cli/commands ; https://opencode.ai/docs/api

Предложенная команда для нового PowerShell, **не проверенная на пользовательском ПК**:
```powershell
wsl -d Ubuntu -- bash -lc 'cd /home/nox/awe-group-cleanroom-20261112 && export HOME="$PWD/.oc-isolated/home" XDG_CONFIG_HOME="$PWD/.oc-isolated/config" XDG_DATA_HOME="$PWD/.oc-isolated/data" XDG_CACHE_HOME="$PWD/.oc-isolated/cache" XDG_STATE_HOME="$PWD/.oc-isolated/state" && /home/nox/.local/bin/opencode api GET /api/event | tee /mnt/c/Users/1/Downloads/AWE-OpenCode-LIVE-auth.log'
```
Возможно, CLI версия не умеет стримить SSE на stdout — если повторится ошибка, нужно сначала прочитать `opencode api GET /api/info` и `service status`, не проводить рестарт/смену пароля. В качестве fallback можно читать existing service logs через `tail -f`, но они не эквивалентны полной транскрипции.

Данные событий могут содержать секреты, не размещать raw logs в публичном GitHub; перед отправкой на аудит проверить персональные данные и credentials.
