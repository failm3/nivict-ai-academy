---
type: engineering-decision
project: AWE GROUP
date: 2026-11-12
status: recommended-not-executed
---

# Решение: OpenCode или Codex для мультимодельной разработки универсальной AWE

Владелец предлагает вместо OpenCode использовать «Cortex» (по контексту возможно Codex или Kortix), заново подключить Router.Cheap key и разрешить все сильные облачные модели, чтобы исполнитель организовал разработку AWE. Не путать Codex (coding agent среды OpenAI) и Kortix (отдельный облачный agent workspace).

**Рекомендация:** при ключевом условии единого Router.Cheap и множества моделей (GPT, Claude, Gemini, Kimi, DeepSeek) выбрать **OpenCode как основной мультипровайдерный кодирующий harness**; для независимой ревизии или отдельной сложной задачи оставить Codex. Hermes — возможная готовая runtime-основа конечного AWE-продукта, не равен OpenCode/Codex.

## Важные подтверждения из документации (12.11.2026)

1. Codex поддерживает subagent workflows, настраиваемых агентов и модели: https://learn.chatgpt.com/docs/agent-configuration/subagents .
2. **Текущий Codex custom provider принимает только Responses API**; Chat Completions удалён. Подтверждение в исходном коде: https://github.com/openai/codex/blob/main/codex-rs/model-provider-info/src/lib.rs и https://github.com/openai/codex/discussions/7782 .
3. Router.Cheap документирует OpenAI-compatible endpoint `https://router.cheap/v1/chat/completions`, model list `/v1/models`, также рекламно упоминает Codex: https://router.cheap/openai-compatible-api . **Поддержка у Router.Cheap нужного Codex Responses wire API не установлена**; нельзя обещать, что любое advertised model route будет поддержано современным Codex.
4. OpenCode имеет custom OpenAI-compatible provider и model configuration, per-agent model choice: https://opencode.ai/docs/providers/ и https://opencode.ai/docs/agents . Реальную совместимость, reasoning/tool calls, key permissions и расходы подтверждать в текущей установленной версии OpenCode, не выводить из одной только спецификации.
5. Не удалять действующий Router.Cheap ключ ради подключения к ещё одному клиенту. Создать **отдельный scoped key** для AWE-dev при согласовании владельца (ограничение расхода и модельный allowlist), сохранить в защищённом механизме локально. Не публиковать ключи в GitHub/отчёты; проверить, не привязан ли старый ключ к Hermes/AWE/OpenCode.
6. Не разрешать «все модели» всем агентам одновременно: fallback и разрешённый список моделей по ролям, отдельные caps. Запретить auto-reserve/auto-top-up без решения владельца.
7. Цель — **универсальная** AWE (компьютер/браузер/internet/MCP/Skills/pluggable tools/design/code/marketing/analytics, dynamic agent hierarchy, memory, QA, permissions). CAREER-01 — одна из миссий, **не** определяет продукт.
8. Выделенный sandbox/workspace и один исполнитель; не трогать исходную AWE, Hermes в NIVICT Workspace, оригинальные OpenCode /goal, старые ключи. Разрабатывать интеграционные компоненты и приемочные доказательства, не новый framework.

## Ближайшие фактические действия после утверждения

- Проверить версии OpenCode/Codex, текущие не-секретные provider settings и имеющиеся ключевые привязки без вывода токенов.
- Завести отдельный project workspace (без каких-либо изменений старой AWE).
- Подключить отдельный ограниченный Router.Cheap ключ к OpenCode, выбрать 1 builder + 1 independent reviewer, остальные сильные модели только при блокере.
- Начать создание универсальной AWE поверх готовой платформы, работать вертикально по capabilities, измерять real result & cost.

**На момент записи** ключи не удалялись/пересоздавались, модели не вызывались, API не оплачивалось и локальная разработка этим сообщением не запускалась.
