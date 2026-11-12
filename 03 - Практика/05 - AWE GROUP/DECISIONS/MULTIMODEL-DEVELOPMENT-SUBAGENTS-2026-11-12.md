---
project: AWE GROUP
date: 2026-11-12
type: owner-preference-and-observed-progress
status: reported-by-owner; model assignments unverified
---

# Multimodel team in OpenCode development — owner update

Пользователь подтвердил, что отправил OpenCode ранее подготовленное указание активно использовать подагентов **для разработки** AWE GROUP.

По словам владельца, Claude Opus 5.5 уже сообщил, что **запускает три параллельных подагента плюс одного независимого reviewer**. Пользователь предпочитает не монокультуру Claude, а разумное распределение разработки между **GPT Astra, Kimi, Gemini, DeepSeek, Claude** и другими проверенными сильными моделями, если они фактически доступны по Router.Cheap. Выбор по качеству задачи/цене, не по квотам участия. Пользователю интересно, какие именно модели сейчас выполняют работу.

## Техническое различие

- Lead model Claude Opus 5.5 на экране ≠ child agents automatically use other LLMs.
- По официальным docs OpenCode, если `agents.<name>.model` не задан, child model **наследует модель родительской сессии**: https://opencode.ai/docs/agents/.
- Изначальный `opencode.json` содержал только `routercheap/claude-opus-5-5` и `routercheap/gpt-6.1-sol`. Без подтверждённого добавления доступных provider/model IDs нельзя утверждать, что Kimi, Gemini, DeepSeek или Astra доступны/запущены.
- Текущая фактология: запущены **по сообщению владельца**, не подтверждено телеметрией. Точные модели child sessions неизвестны.
- Для доказательства попросить у OpenCode или прочитать child session metadata `session_id, role, provider/model, job, status`. Не прерывать текущие запущенные задачи, избегать повторного промпта во время параллельной работы.
- Не путать development subagents OpenCode с runtime subagents создаваемой системы AWE.
- Существующий prepaid Router.Cheap разрешён к расходованию; без автоматического top-up.
- Все решения документировать в GitHub-архиве; fresh code в clean-room, архив GitHub **не источник** для разработчика.

В текущем диалоге ChatGPT не имеет доступа к live WSL OpenCode, поэтому не подтверждает конкретный состав мультимодельной команды.
