---
type: independent-code-audit
project: AWE GROUP
date: 2026-11-12
snapshot_time_local: "04:36 MSK"
status: source-reviewed; live execution not verified
source: owner-uploaded AWE-OpenCode-Audit-20261112-043624.zip
privacy: public-safe findings; do not publish raw archives or secrets
---

# AWE GROUP — независимый аудит реального проекта OpenCode (12 ноября 2026, 04:36 МСК)

## Доказательства

Получен ZIP 38 279 байт, 34 элемента. В нём **17 файлов нового проекта, включая 12 TypeScript-файлов (~1 459 строк кода)**; Git status фиксирует 17 untracked файлов и **0 Git-коммитов**. История OpenCode не экспортирована (`session list=[]`, `stats=0`) — это **не подтверждает нулевого расхода LLM**. Сервисный лог содержит 629 строк и около 623 структурируемых событий; из них **541 launch process**, включая 469 служебных Git-snapshot команд и 53 Bash-команды. Фактическая работа видна: Node/npm проверки, npm init, npm install/uninstall, выбор версий Mastra/AI SDK, создание каталогов, два вызова `npx tsc --noEmit`. Результаты typecheck в данном ZIP отсутствуют.

## Что появилось

- `src/index.ts`: CLI entry, REST/server entry, one-shot run.
- `src/cli/index.ts`: интерактивный CLI с просмотром миссий.
- `src/api/server.ts`: /specify, /approve, missions, artifacts, logs, cancel.
- `src/agents/prompt-master.ts`: формирует спецификацию через LLM.
- `src/agents/head-agent.ts`: строит JSON-план делегирования.
- `src/agents/mission-manager.ts`: последовательно вызывает специалистов, затем QA/repair.
- `src/agents/specialists.ts`: простая фабрика заранее заданных ролей.
- `src/agents/qa-agent.ts`: текстовая LLM-проверка.
- `src/tools/index.ts`: shell, read/write/list files, HTTP fetch, HTML web search, artifacts.
- `src/utils/storage.ts`: JSON-файлы и артефакты.
- `src/config/models.ts`: статические cloud model routes.

**Это реальный кодовый черновик, но НЕ подтверждённо работающий универсальный агент.**

## Блокирующие замечания P0 — не запускать API с сетевым доступом

1. **Неавторизованный REST:** `src/api/server.ts:20-21` wildcard CORS; `:88-107` endpoint /approve без owner-auth; `:123` default listen (не localhost-only). Внутри mission agents есть произвольный shell. Не запускать на доступном извне интерфейсе до аутентификации, сетевой изоляции и permissions.
2. **Широкий shell/files:** `src/tools/index.ts:31-39` exec произвольной команды с правами WSL; `:61-64` file_read произвольного пути; `:79-84` file_write; `:109-111` shell `find` с неподтверждённым путём. Нет границ sandbox или конфигурационных разрешений.
3. **APPROVE обходится one-shot режимом:** `src/index.ts` всегда назначает миссию `approved` без реального подтверждения, несмотря на требование владельца.
4. **Path traversal:** `src/utils/storage.ts:60-70` принимает имя артефакта и mission_id без корректной проверки безопасного пути; возможен выход за ожидаемый каталог.
5. **Нет отмены и recovery:** `src/api/server.ts:99-107` fire-and-forget async; `:115-120` cancel меняет лишь статус, не останавливая текущие задачи. Нет durable job queue или hard-budget всей иерархии.

## Функциональные ограничения P1

- `src/agents/mission-manager.ts:29-65`: простой последовательный цикл по делегированиям; нет параллельного и рекурсивного дерева.
- `src/agents/head-agent.ts`: заранее перечислены шесть ролей, нет динамического выбора навыков и инструментов.
- `src/agents/specialists.ts:94-99`: функция безусловно возвращает `success: true`, даже без артефактов.
- `src/agents/qa-agent.ts`: только текстовый LLM review, без реальных тестов, отдельной инструментальной проверки и строгой Zod-валидации.
- `src/agents/prompt-master.ts`: JSON.parse без SpecificationSchema.parse.
- `src/agents/mission-manager.ts:122-125`: список artifact IDs может остаться прежним после repair.
- `src/utils/storage.ts`: нет транзакционной/атомарной записи или crash resume.
- `package.json`: тестовая команда-заглушка вместо тестов.
- `@mastra/mcp` указан как зависимость, но реальных MCP/browser/GUI/vision/Skills интеграций в исходниках ещё нет.
- `.awe-data` не исключён из Git: риск публично коммитить данные миссий.

## Почему export OpenCode sessions = 0

У исходного запуска OpenCode в WSL был бинарник `/home/nox/.local/bin/opencode`, но диагностический скрипт выбрал `/mnt/c/Users/1/AppData/Roaming/npm/opencode` (точный путь задокументирован в `metadata/README.txt`). Это **сильный кандидат объяснения** неверной статистики; требуется повторить чтение именно через WSL CLI, без остановки текущей задачи:

```bash
OPENCODE_BIN=/home/nox/.local/bin/opencode bash /mnt/c/Users/1/Downloads/awe_opencode_audit_capture.sh
```

Если снова 0, проверить фактическую БД isolated profile/service. Не объявлять расход `$0` и не утверждать, что модель не работала.

## Независимая оценка **снимка**, не итоговой способности модели

- Наличие кодовой структуры: **5/10**
- Соответствие универсальной рекурсивной архитектуре: **2/10**
- Безопасность для live runtime: **1/10**
- Надёжность/восстановление: **1/10**
- Доказанная end-to-end работоспособность: **0/10**

**Решение:** разработку OpenCode не останавливать ради отчётов, но **приоритетно устранить P0** и показать typecheck + действующий approval + реальное исполнение + независимый QA. До этого запрещено давать AWE внешние учётные записи или открывать API в сеть. Полный 623-событийный ledger и большой forensic-report созданы как отдельные прикреплённые пользовательские файлы, **не опубликованы в публичном репозитории**, так как логи потенциально конфиденциальны.
