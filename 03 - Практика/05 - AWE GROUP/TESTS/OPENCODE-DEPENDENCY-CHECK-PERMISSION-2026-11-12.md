---
project: AWE GROUP
type: progress-checkpoint
date: 2026-11-12
status: development-in-progress; dependency-discovery
source: owner-supplied screenshot
---

# OpenCode: выбор зависимостей и подтверждение `cat`

На скриншоте открытой TUI OpenCode в чистом каталоге AWE GROUP видно:

- Сообщение пользователя «Продолжай реализацию».
- OpenCode: «Принято. Перехожу к реализации с упором на зрелые библиотеки, реальное исполнение и устойчивую архитектуру».
- Команды: `cd /home/nox/awe-group-cleanroom-20261112 && cat package.json`, а также `npm show @mastra/core version; npm show mastra version; npm show langchain version; npm show @langchain/core version; npm show @langchain/openai version` (stderr подавляется).
- UI запросил подтверждение командного шаблона `cat *` и показывает варианты `Allow once`, `Always allow`, `Reject`; в момент снимка выделено `Always allow`.
- Рекомендация: **Allow once**; широкое постоянное право `cat *` нежелательно при запрете чтения предыдущих проектов.
- Проверка существования package.json и версий библиотек ещё не подтверждает установку зависимостей, код, работающих агентов или приёмку.
- Не посылать разработчику новых промптов до результата текущего шага, кроме необходимости подтвердить конкретное действие. Избегать ненужной ревизии архитектуры.

Эта запись — архив обсуждения для сохранения контекста, **не источник** для clean-room разработчика.
