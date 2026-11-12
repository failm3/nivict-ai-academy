---
project: AWE GROUP
type: user-observed-progress
date: 2026-11-12
status: OpenCode launched; first command awaiting approval
source: owner screenshot 2026-11-12_04-17-02.png in conversation
---
# AWE GROUP Clean Room — первый реальный старт OpenCode

На скриншоте владельца виден работающий OpenCode TUI с заголовком «AWE GROUP реализация по AGENT...».

Текст OpenCode:
- «Хорошо. Чистый проект с Node/Router.Cheap. Выбираю стек:»
- Runtime: Node.js + TypeScript
- Framework: минимальный, прямой HTTP через express для API
- CLI: Router.Cheap через OpenAI-compatible SDK
- Storage: JSON-файлы для персистентности (потом PostgreSQL)
- Queue: in-process для первой итерации
- «Первый вертикальный срез: user → PromptMaster → approval → HeadAgent → MissionManager → SpecializedAgent → QA → artifact.»
- Вызов инструмента: `cd /home/nox/awe-group-cleanroom-20261112 && node --version && npm --version`
- UI: Permission required; варианты Allow once / Always allow / Reject, выбран Allow once.

## Аналитическая приёмка

- **Да:** OpenCode успешно запущен; провёл несколько чтений, наметил стек и запросил разрешение на безопасную проверку версий Node/npm.
- **Нет:** доказательств созданного/запущенного исходного кода, API-вызовов, рабочих агентов, интеграции моделей и готовности продукта пока нет.
- **Риск:** in-process queue + JSON persistence не являются достаточной гарантией восстановления после crash; реализация иерархии с нуля потенциально повторяет дорогостоящую историю. Требуется использовать зрелый внешний runtime/библиотеки для реальной агентной работы; собственный код — оркестрация/политики/UX и интеграция готовых механизмов. Clean-room запрет относится к старым проектам пользователя, не к mature third-party open source.
- **Рекомендация:** пользователь одобряет `node --version && npm --version` через Allow once; затем уточняет инструктору OpenCode, что mock/in-process разрешены только для краткого первого среза, не финальная AWE; без искусственных остановок и дополнительного предварительного исследования.

Запись сделана как архив беседы; новый OpenCode clean-room не должен читать этот архив как исходное ТЗ.
