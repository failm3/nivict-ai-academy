---
type: engineering-recommendation
project: AWE GROUP
date: 2026-11-12
status: proposed-not-authorized; API connectivity and economics not tested
---
# OpenCode как мультимодельный инженерный исполнитель AWE GROUP

**Вопрос владельца:** справится ли OpenCode с созданием универсальной AWE GROUP, если дать ему GPT-6 Astra, Kimi K3.1 Pro, Gemini 4 Argon, передовой DeepSeek и упомянутый «Cloud Zenith»?

**Вывод:** это существенно сильнее, чем OpenCode с одной слабой локальной LLM. OpenCode — оболочка/harness, качество зависит от фактических доступных API-моделей, orchestration, checkpoints, permissions, тестовых результатов и review. Гарантии полного универсального продукта нет; жизнеспособную интеграционную сборку на готовом Hermes считать обоснованной целью, при условии поэтапной поставки.

Предлагаемое деление труда:
- GPT-6 Astra: системная архитектура, сложные решения; при наличии разрешённого API route.
- Kimi K3.1 Pro: основной coding-исполнитель, функциональные интеграции.
- Gemini 4 Argon: независимый reviewer и анализ крупных контекстов.
- DeepSeek: дешёвые ограниченные исправления/документы, только если экономия подтверждена.
- «Cloud Zenith»: значение не установлено; Zenith также является названием long-horizon agent harness (https://ii.inc/blog/post/zenith), не идентификатором LLM. Не добавлять его автоматически.
- Не запускать 5 дорогих моделей во всех ролях одновременно. Обычно достаточно builder + independent reviewer, архитектурную модель вызывать по сложности.
- OpenCode имеет конфигурируемые модели на agent/subagent и nested subagent depth; точное поведение и ID зависит от используемой версии и провайдера:
  https://opencode.ai/docs/agents
  https://opencode.ai/docs/config
  https://opencode.ai/docs/models
- Безопасность: текущая документация указывает широкие разрешения tools для build/default; индивидуально заблокировать внешние каталоги, shell и публикации, предусмотреть approval и реальные provider-side budgets:
  https://opencode.ai/docs/permissions/
- OpenCode строит продукт, Hermes (пока основной кандидат) — его runtime. Не путать производителя и конечный продукт.
- Владелец **не хочет использовать Ollama** до усиления железа.
- CAREER-01 — одна из потенциальных миссий, не принцип организации и не обязательная первая инженерная вертикаль.

Никаких установок, платежей и запуска моделей этой записью не выполнялось.
