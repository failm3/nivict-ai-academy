# NOX — readiness, tool execution and supervised stress: owner discussion
Дата: 2026-11-13. **DRAFT / NOT AUTHORIZED TO EXECUTE**. Важная точка обсуждения, не команда на выполнение или трату API.

## Прямая постановка владельца (в текущем чате)
«Смотри, ну давай подумаем объективно, чего же не хватает системе. Я хочу, чтобы под присмотром OpenKoda провёлся большой стресс-тест системы. Это во-первых. Во-вторых, инструменты. Нам надо добиться того, чтобы он, сука, наконец-таки начал использовать инструменты и сам к себе их подключал. Вот это мне кажется очень главное. Ну, безумно главная тема. И давай подумаем, какие моменты ещё нужно доделать. Либо спросим у OpenKoda напрямую, какие моменты вам видны для того, чтобы передавать Nokseo в моё пользование и быть уверенным в том, что он справится без присмотра OpenKoda.»

Главная цель: **owner → Nox → verifiable result** без OpenCode как обязательного посредника. OpenCode — независимый наблюдатель и инженер-ремонтник, НЕ подмена результата и НЕ единственный QA.

## Уже известные доказательства и недостатки
- Nox runtime действительно использовал Head/делегирование, сохранял артефакты и выполнил resume с checkpoint, но финальная NIVICT миссия FAIL (13/14; обязательный README/manifest отсутствует), repair также FAIL; конец логов Recorder 2026-11-13 00:50 UTC. Локальная ветка hotfix/e1-recovery-hotfix-01, коммиты bc4f57b и 446adae; локальные изменения нельзя считать pushed.
- Writer в одном случае имел file_list и shell; отсутствие file_write в явном перечне и неполный manifest — подозрение на capability/grant mismatch, **причина не доказана**.
- Tool Intelligence: каталог Manus 3415 ресурсов — search metadata, не 3415 исполняемых/APPROVED tools. Предыдущий owner goal требовал TI discovery → grants → фактический invocation, но весь gate не подтверждён.
- Model Router: запланированная Kimi executor заменена фактическим Claude Opus 5.5 вследствие отсутствия записи для роли executor; no transparent autonomous choice proven.
- Архитектурный acceptance draft уже существует: TESTS/AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md. Не создавать ещё один конкурирующий набор критериев.
- Текущие главные неизвестности: прямой owner interface, полноценный PM/Head/Factory/child autonomy, capability execution, immutable QA, recovery safety, memory, model choice, secrets, result delivery.
- Не путать вердикт 13/14 технического QA с 2/10 субъективного owner design score; ближайшее тестирование касается **автономности, а не дизайна**.

## Предложенный порядок решения (обсуждается, НЕ исполнен)
1. **Read-only инженерный inventory и независимое заключение OpenCode**: конкретный runtime/commit, существующие компоненты, interface/grants, test evidence, воспроизводимые gaps, 5 главных P0 до owner handoff. Никакой самоаттестации PASS по словам исполнителя.
2. **Capability execution proof**: Head/child находит подходящую capability через существующий TI, разрешает безопасное подключение через адаптер/протокол (MCP/HTTP/OpenAPI/CLI), выдаёт только scoped grant, реальный tool call, валидирует output, записывает evidence. Первый набор из 3 типов: уже разрешённый CLI/read-only; существующий browser MCP/Playwright, если действительно доступен; безопасный HTTP API mock/sandbox. Из отдельно проверенного безопасного каталожного кандидата — controlled registration в изолированной среде, NOT произвольная автоустановка из интернета. Тесты DENY/NO_CREDENTIAL/NO_ADAPTER/BAD_TOOL_RESULT; fail closed. Автоматизация разрешённой регистрации ≠ безусловная автоустановка любого кода.
3. **Supervised architecture & stress**: A. isolated contract/negative tests всех реализованных субъектов; B. integration + capability + data passing + idempotence; C. load/chaos с 1/3/5 параллельных миссий, kill-restart, rate limits, timeout before/after acceptance, lost tool output, bogus success, secrets, injection and failure recovery; D. несколько новых owner-style живых задач напрямую Nox без OpenCode touch, с bounded paid API budget **только после owner approval**. Start with cheap offline/mock stress; do not exhaust available paid routing balances without specific budget.
4. **Handoff proof**: direct user submit/status/pause/approve/retrieve; durable checkpoints/trace; per-mission model/tools/cost; independent QA; policy/permissions and no unauthorized side effects; no duplicate external actions; no false COMPLETE; dry-run backup/restore and rollback; ready for supervised pilot only once these gates pass.
5. **Fail-safe operations**: incident with secrets in Session Recorder requires audit/redaction/rotation before wider tools, if still live. Production-like provider route need explicit model, budget, fail-closed and retry classification.

## Принцип приёмки
- Пороговые метрики заранее выбрать и заморозить; не снижать после теста.
- Tests representative: synthetic load cannot prove live agent quality, and a single live success does not prove reliability.
- Test harness separate from Nox; OpenCode permitted to observe and later repair a frozen failing test, not to manually create mission artifacts or loosen oracle.
- One P0 blocker on ownership safety, false PASS, unauthorized side effects, tool privilege escalation, irrecoverable checkpoint, model/budget breach = NOT_READY.
- Report each gate: PASS/PARTIAL/FAIL/BLOCKED/NOT_VERIFIED, evidence paths, SHAs, untested cases, exact reproduction, costs; independent final owner acceptance only.
- No automatic changes to source /goal, no merges or production deployment, no money/credentials access expansion without explicit owner decision.

## Разделение решений
- **Сейчас** обсуждается и может быть отправлена read-only постановка вопросов OpenCode.
- **Затем** владелец утвердит конкретный бюджет, изолированную среду, критерии, допустимый спектр автоматического подключения инструментов и запуск стресс-теста.

Источники:
- https://github.com/failm3/awe-opencode-recordings/blob/main/LATEST.md
- https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/TESTS/AWE-ARCHITECTURE-ACCEPTANCE-PLAN-2026-11-12.md
- https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/PROMPTS/AWE-E1-PRODUCT-LAUNCH-01-2026-11-12.md
