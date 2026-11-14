# OpenCode — независимое инженерное ревью ТЗ Cortex для R2

Дата: 2026-11-14.
Статус: DOCS-ONLY REQUEST — RESEARCH/REVIEW, NO IMPLEMENTATION AUTHORITY.
Тебе НЕ поручается реализовать R2. Тебе поручается критически улучшить исследовательское техническое задание, которое затем получит Cortex.

## Цель

Ты являешься разработчиком Nox и лучше стороннего исследователя знаешь фактические исходники, ограничения, уже написанные модули, проверенные тесты и реальные проблемы runtime. Прочитай соседний 01-CORTEX-R2-BRIEF-DRAFT.md целиком и проверь его против ТЕКУЩЕГО live cleanroom Nox, а не старых GitHub exports.

Исходный документ:
03 - Практика/05 - AWE GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/01-CORTEX-R2-BRIEF-DRAFT.md

Рабочий код (если всё ещё существует): /home/nox/awe-group-cleanroom-20261112 (r1/dev). GitHub docs: failm3/nivict-ai-academy. Observer: failm3/awe-opencode-recordings.

## Проверить обязательно

1. Актуальный HEAD, clean/dirty state, наличие завершённых работ после 68cc0ee, last tests и истинный R1 статус.
2. Что уже есть в Nox: Head, Planner, Prompt Master, Agent Factory, tools/TI, MCP, model router, Skills, Memory, QA, sandbox, authorization, recovery. Не путать exists/wired/callable/accepted.
3. Проверить почему 13/13 independent browser verifier PASS, но миссия PAUSED по 600s; предложить Cortex вопросы о bottleneck, scheduling, model usage, tokens, role suitability, tool context, repair strategy и boundary conditions.
4. Реалистичность предложенной R2 цели и минимальный R2 acceptance с точными пробелами.
5. Работоспособность того, что документ предлагает заимствовать из Mastra/MCP/Agent Skills; сравнить installed package versions/API.
6. В какой точке existing modules подключать готовые Skill, Tool, Knowledge и LLM-vs-code strategy, а где thin adapter оправдан.
7. Отсутствующие требования, заведомо неверные предположения, устаревшие сведения, ненужные подсистемы, потенциальные security/recovery/QA blocker.
8. Не хватает ли источников, типов профессиональных компетенций, методов обучения, closed-loop improvement, vendor/license/cost proof, R2 tests.
9. Может ли OpenCode как инженер реализовать minimal R2 из ответов Cortex; оценка по отдельным зависимостям, risks, integration effort с допущениями, без недоказанных обещаний.
10. Предложи короткий FASTEST SAFE PATH и минимальный integration proof-of-concept (только спецификация, без запуска).

## Главные требования владельца к правкам

REUSE FIRST. Готовые стандарты/Skills/MCP/SDK/API/CLI, доступные по текущим лицензиям. Не рекомендовать писать всё с нуля, если готовое подходит. Избегать лишних abstractions и бесконечной разработки.

Cortex не ограничен количеством исследовательских/супер-агентов, моделей, поисковых задач, найденных кандидатов и глубиной исследования. Права на продакшн, секреты, покупки и внешние действия этим не расширяются.

Не подменять реальные evidence словами "есть в Mastra, значит уже работает". Не округлять неполное usage в полные счета. Фиксировать SHA/version/source.

Не согласовывать каждую редакторскую правку с пользователем, если она сохраняет главную цель; существенные продуктовые альтернативы вынести в OWNER DECISIONS и аргументировать.

## Что нужно СОЗДАТЬ в той же папке

1) 03-OPENCODE-ENGINEERING-REVIEW.md:
   - обновлённый source-backed engineering checkpoint Nox;
   - что уже работает; чего нет; что unknown;
   - фактические технические корректировки и замечания к пунктам 01–22;
   - наиболее полезные дополнения к будущему исследованию Cortex;
   - потенциальные интеграции с exact модулем/путём;
   - feasibility и архитектурные риски R2;
   - предполагаемые новые испытания и критерии приёмки;
   - отличия между текущим draft и предложенной версией;
   - подтверждения source path/test/commit или explicit UNKNOWN.

2) 04-CORTEX-R2-BRIEF-REVISED-BY-OPENCODE.md:
   - ПОЛНЫЙ самостоятельный переработанный текст ТЗ для передачи Cortex;
   - сохранить требования владельца: 4504 + новый поиск, без искусственных лимитов на супер-агентов/делегации, knowledge/skills/tools/strategy/meta/QA, ready-made-first, OpenCode R2 feasibility;
   - внести конкретные исправления и предложения разработчика;
   - не писать в этот файл лишь комментарии или diff: нужен готовый standalone briefing.

3) 05-REVIEW-EVIDENCE-MANIFEST.md (при необходимости):
   - SHA/версии/readback, список просмотренных исходников и испытаний.

## Куда сохранить

Основная цель — записать эти файлы обратно в docs-репозиторий failm3/nivict-ai-academy, в ту же папку, что и исходник, предпочтительно отдельным документальным коммитом с сообщением вроде:
docs(nox): engineering review and Cortex R2 revised research brief

НЕ редактировать 01-CORTEX-R2-BRIEF-DRAFT.md, не изменять original. НЕ выполнять git operations в живой runtime branch r1/dev. Использовать отдельный docs repo checkout/worktree, либо GitHub API при наличии легитимного доступа.

Если нет подтверждённого write access к docs repo, не пытаться обойти доступ; создай файлы в отдельной безопасной локальной папке и сообщи абсолютные пути/sha256, чтобы владелец мог вернуть их в GitHub. Не считать это опубликованным.

В завершение предъявить ссылку на GitHub файл 04 (если действительно опубликован), commit SHA, source-readback и статус docs repo. До записи файла не объявлять review delivered.

## Запреты

Никаких новых R1/R2 миссий, сторонних платных API вызовов, установки экспериментальных пакетов в рабочую систему, изменения кодовой базы, отмены текущего задания или release/deploy. Допустимы чтение исходников и уже существующих логов, анализ и написание этих документов; безопасные read-only команды. Если для важного факта нужна тяжёлая проверка, пометить её как NEXT TEST / NOT_RUN.

Это review, не разрешение на implementation.
