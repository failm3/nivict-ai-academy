---
type: user-forwarded-agent-report
project: AWE GROUP
date: 2026-11-12
status: reported-v0.1-not-independently-reverified
source: user's pasted OpenCode completion message
privacy: public-safe
---

# AWE GROUP v0.1 — сообщение OpenCode и границы приёмки

## Отчёт OpenCode, переданный владельцем

OpenCode сообщает: `AWE GROUP v0.1 is running` и заявляет:
- Цепочка: USER → PromptMaster → approval → HeadAgent → MissionManager → Specialists → QA → Artifact.
- `src/agents/prompt-master.ts`: specification + acceptance criteria.
- `src/agents/head-agent.ts`: mission delegation plan.
- `src/agents/mission-manager.ts`: coordination + bounded QA repair.
- `src/agents/specialists.ts`: researcher, coder, writer, analyst, devops, designer.
- `src/agents/qa-agent.ts`: LLM review, score 0–10.
- `src/tools/index.ts`: shell, file_read/write/list, web_fetch/search, save_artifact.
- `src/api/server.ts`: /specify, /approve, /missions/:id/artifacts.
- `src/cli/index.ts`: interactive CLI; `src/index.ts`: run/cli/serve.
- Claimed test 1: Haiku — article about agents — QA 10/10.
- Claimed test 2: Python prime generator, code executed, output saved — QA 10/10.
- Claimed repair bound: up to two retries after QA rejection.
- Self-reported next roadmap: Playwright, MCP client, libsql persistence, parallel delegation, task-specific dynamic routing.
- Session shown: Build · Claude Opus 5.5 · 22m 9s · 23.3 tok/s.

Это **сообщение исполнителя**, не независимый readback файлов/логи прохода тестов. Прежний forensic audit ZIP на 04:36 сообщал о рабочем кодовом черновике, но **без доказанного сквозного запуска и с P0 дефектами**. Новых исходников и логов после заявленных двух live-тестов в эту беседу не предоставлено, поэтому исправление старых дефектов не доказано.

## Сопоставление с исходной целью владельца

Требуется **универсальная AWE**, а не специализация под CAREER-01 и не статическое шесть-ролей ядро. V0.1 при подтверждении демонстрирует полезный вертикальный срез, но пока не доказывает:
- запрет запуска любой миссии до реального user APPROVE во ВСЕХ entrypoints;
- ограничение shell/file и path traversal; запрет API без аутентификации и локальной привязки;
- реальное динамическое рекурсивное дерево агентов, параллельность и выбор LLM по задаче;
- независимое инструментальное QA вместо только оценки QA LLM;
- MCP/browser/GUI/design/marketing/analytics генерацию;
- recovery, durable queue, correctness при crash, engine-level budgets;
- сохранённые Git checkpoints и evidence исполнения.

## Блокирующие приоритеты — из предыдущего forensic audit

P0: доступность API без auth и wildcard CORS; unrestricted shell/files; обход APPROVE через one-shot; unsafe artifact paths; cancel without cancellation; async fire-and-forget без сохранения.

До исправления P0 **не открывать API в сеть и не давать AWE внешние credentials**. Вызов shell с правами пользователя WSL и текстовые guardrails не являются OS sandbox.

## Техническое решение следующей итерации

1. Сохранить текущую реально работающую версию отдельным локальным Git commit вместе с логами тестов и сведениями о model/usage, исключив `.env`, `.awe-data`, токены и личные данные. В GitHub без прямого разрешения новый clean-room проект не публиковать.
2. Устранить P0 авторизацию и исполнение: bind API to 127.0.0.1 + token/auth; mandatory approval on all routes; scoped workdir, path validation, shell sandbox/allowlist, actual cancellation and denied external actions.
3. Подтвердить «real run» настоящими artifacts + exact commands + QA evidence/negative control. Оценка 10/10 собственного LLM QA **не доказательство независимого качества**.
4. Заменить statically enumerated roles реализацией временной специализации; recursive delegation с глубиной/concurrency limits и dynamic model selection.
5. MCP/browser/vision/GUI/Skills and true persistent state — следующим этапом, без новой «архитектуры с нуля».
6. Принимать по рабочему универсальному сценарию, не подменять продукт подготовленным Python prime generator.
7. Не использовать Ollama; разрешено тратить существующий prepaid Router.Cheap баланс, без автоматических пополнений.

## Статус

Доказаны прежние записи исходников. Новое выполнение two live tests **пока подтверждено только словами OpenCode**. Никаких новых команд в Windows/WSL или платных вызовов из этого чата не выполнялось.
