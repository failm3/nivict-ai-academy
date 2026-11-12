---
project: AWE GROUP
date: 2026-11-12
type: owner-supplied-preflight
status: models-discovered-only
---
# Локальная Ollama — подтверждённые модели

Пользователь проверил PowerShell:

- `ollama.exe` найден в `C:\Users\1\AppData\Local\Programs\Ollama\ollama.exe`.
- `http://127.0.0.1:11434/api/tags` отвечает.
- Модели на диске:
  - `gpt-oss:20b`, `size: 13793441244` bytes (~13.8 GB decimal)
  - `qwen3:4b-instruct`, `size: 2497293803` bytes (~2.5 GB decimal)
- Windows→WSL вывод содержит NAT proxy warning, затем `CLI: -c: line 2: syntax error: unexpected end of file from 'if' command on line 1`. Это сбой командной строки Bash, **не проверка** работы Ollama в Ubuntu и **не доказательство**, что модели отсутствуют в Windows.
- У пользователя уже доступен Windows-native Hermes v0.22.2, `C:\Users\1\AWE-Tests\Hermes` пуст; Docker Desktop жив, образы и контейнеры пока отсутствуют.
- В документации Hermes: Ollama OpenAI-compatible `http://localhost:11434/v1`, локальный provider `custom`; для полноценного агентного выполнения нужен фактически конфигурированный контекст около 64000 токенов. `HERMES_HOME` может выделить отдельный профиль, **не OS sandbox**.
- В официальных каталогах Ollama `qwen3:4b-instruct` и `gpt-oss:20b` помечены как способные на tool calling, но фактическое поведение конкретных локальных экземпляров **не тестировалось**.
- Рекомендован ближайший **неплатный** тест вызова инструмента через локальный Ollama HTTP API на `qwen3:4b-instruct`; после него `ollama ps` для фактического CONTEXT / CPU-GPU. Не вызывать Hermes с текущей основной конфигурацией, не обновлять Hermes, не применять `--yolo`.

## Ссылки
- https://hermes-agent.nousresearch.com/docs/integrations/providers
- https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup
- https://ollama.com/library/qwen3%3A4b-instruct
- https://ollama.com/library/gpt-oss

На дату записи новые модели не скачивались, конфиги и лимиты не менялись, платных вызовов не было.
