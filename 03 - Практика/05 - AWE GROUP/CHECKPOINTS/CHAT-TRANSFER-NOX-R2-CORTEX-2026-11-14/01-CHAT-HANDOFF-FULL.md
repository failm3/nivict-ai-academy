# NOX / AWE GROUP — передача контекста между чатами (14 ноября 2026)
## Переход непосредственно к созданию окончательного ТЗ Cortex R2

**СТАТУС:** READ-FIRST CROSS-CHAT HANDOFF. Ревью OpenCode принято, финальный промпт Cortex ещё НЕ составлен и НЕ отправлен. Следующий чат должен сразу писать финальное ТЗ Cortex, не продолжать старое обсуждение.

**ОГРАНИЧЕНИЕ ПОЛНОТЫ:** в нынешней среде нет функции байтового экспорта полного лога всех приблизительно 100 прежних сообщений текущего чата. Здесь максимально подробно сохранены материальные решения, требования, выводы, хронология, артефакты и ссылки из доступной переписки и проверенного GitHub. Часть более ранних реплик передана пересказом, а не verbatim. Не утверждать, что архив всех слов за всё время создан. Сам исходный чат остаётся самостоятельным первичным источником.

## 1. Где остановились

Пользователь попросил после завершения ревью OpenCode проверить весь результат, дать отчёт, затем написать большой финальный промпт для исследователя Cortex. Ассистент полностью изучил 03/04/05 и вынес заключение: инженерное ревью OpenCode принято, повторная доработка не нужна, но в финальном промпте обязательны три усиления (подробнее в разделе 8). Пользователь теперь переходит в новый чат из-за перегрузки старого. **В новом чате надо сразу создавать полное итоговое исследовательское ТЗ Cortex.** Не отправлять его автоматически и не начинать разработку Nox.

Принята последовательность: независимое Cortex research R2 → собственный критический разбор и утверждение scope владельцем → отдельное автономное инженерное ТЗ OpenCode на интеграцию → самостоятельная работа Nox → независимая R2 acceptance.

Не перезапускать исследование OpenCode, не просить пользователя повторять контекст, не заменять полное ТЗ очередным обсуждением архитектуры.

## 2. Канонические первоисточники GitHub

Документы: https://github.com/failm3/nivict-ai-academy
Observer OpenCode: https://github.com/failm3/awe-opencode-recordings
Обсервер проекта: https://github.com/failm3/awe-group-observer
Исторический и не обязательно актуальный runtime export: https://github.com/failm3/awe-group-runtime
Рабочий локальный Nox (если доступен OpenCode): /home/nox/awe-group-cleanroom-20261112, branch r1/dev.

**Ревью OpenCode опубликовано** 14.11.2026 в commit 3c3fed07b8222946204cfa8169d9aef04f9f4097:
https://github.com/failm3/nivict-ai-academy/commit/3c3fed07b8222946204cfa8169d9aef04f9f4097

Папка:
03 - Практика/05 - AWE GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/

Пять файлов в папке:
01-CORTEX-R2-BRIEF-DRAFT.md — первоначальное полное ТЗ, созданное ассистентом для проверки инженером.
02-OPENCODE-ENGINEERING-REVIEW-TASK.md — задача OpenCode выполнить строго docs-only исходниковый аудит.
**03-OPENCODE-ENGINEERING-REVIEW.md** — source-backed инженерная рецензия, главный источник реального состояния.
**04-CORTEX-R2-BRIEF-REVISED-BY-OPENCODE.md** — самостоятельное полное переработанное 22-раздельное ТЗ Cortex, ОСНОВА следующего промпта.
**05-REVIEW-EVIDENCE-MANIFEST.md** — SHA/evidence/NOT_RUN/UNKNOWN, ограничения достоверности.

Обязательные pinned URLs для нового чата:
03 https://github.com/failm3/nivict-ai-academy/blob/3c3fed07b8222946204cfa8169d9aef04f9f4097/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/03-OPENCODE-ENGINEERING-REVIEW.md
04 https://github.com/failm3/nivict-ai-academy/blob/3c3fed07b8222946204cfa8169d9aef04f9f4097/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/04-CORTEX-R2-BRIEF-REVISED-BY-OPENCODE.md
05 https://github.com/failm3/nivict-ai-academy/blob/3c3fed07b8222946204cfa8169d9aef04f9f4097/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/RESEARCH/NOX-R2-CORTEX-OPENCODE-REVIEW-2026-11-14/05-REVIEW-EVIDENCE-MANIFEST.md

OpenCode опубликовал ровно три новые записи 03/04/05, исходные 01/02 не менял; два независимых GitHub readback подтвердили SHA-256. В 05 написано, что publication ещё не было — это исторический freeze до публикации, сейчас публикация доказана коммитом и журналом OpenCode 01:54 UTC. Репозиторий публичный: не публиковать сюда секреты, токены, личную почту/данные.

## 3. Цель владельца, обязательная для Cortex

**Nox/AWE GROUP — универсальная автономная профессиональная мультиагентная система, а не только web/coding-agent.** Nox должен получать непривычные и ранее не предусмотренные миссии, находить настоящие знания и практические методы, приобретать проверенные инструменты и навыки, выбирать рациональный способ выполнения, выдавать реальный продукт/артефакт, проходить независимую оценку и повторно использовать успешный опыт. Карта профессий открытая и расширяемая, а не фиксированный список направлений. Честно калибровать неизвестное и ограничения квалификации.

Категорическое предпочтение: **REUSE FIRST → CONFIGURE NATIVE → CONNECT READY MADE → THIN ADAPTER → NEW CODE ONLY WHEN PROVEN NECESSARY.** Запрет смысловой: не переписывать Mastra, Head, Factory, MM, tools, память или QA ради разработки, если существует подходящая зрелая готовая технология. Определять точные версии, модули и минимальные места подключения. Никакого бесконечного цикла собственной разработки и академической каталогизации без работающих миссий.

Четыре логических контура НЕ означают четыре отдельные новые платформы:
A. Tool / Capability Intelligence: discover, verify, vet, pin, install when authorized, grant, invoke, receipt, independent QA, reuse, revalidate/revoke.
B. Knowledge & Competence Intelligence: непрерывно актуализируемые первичные профессиональные источники (учебники, статьи, научные работы, стандарты, технические руководства, видео/аудио, code/examples, design systems, marketing, research, SOP), source anchors/citations/rights/ACL, practice, verified transferable Skills, open-world professions.
C. Execution Strategy Intelligence: выбирать детерминированную функцию, скрипт, библиотеку, API/CLI, workflow, bot/service, LLM, одного специалиста, multiagent/parallel или гибрид по quality/time/TCO/security; route моделей — подслой, не вся стратегия.
D. Meta-Intelligence: оценивать свою компетентность и uncertainty, чему учиться в первую очередь, получать ли новый tool, рационально останавливать поиск, measuring uplift/no-gain, следить за drift/versions, отзывать плохие уроки, сохранять verified experience и failure evidence. Никакое знание или Skill не выдаёт себе разрешения.

Не путать чтение документа с обучением, наличие плагина с работоспособностью, source evidence с сертификацией компетентности.

## 4. Главный R2 архитектурный компромисс

OpenCode предложил **минимальный R2** как воспроизводимый finite specification-bound independently accepted autonomous capability loop на реальных задачах. Более широкое open-world постоянное развитие он относит к R2.x/R3. Это обоснованный путь к быстрой первой приёмке, но он НЕ отменяет полную цель пользователя.

**Финальный Cortex prompt обязан требовать два отдельные вывода:**
1. Что входит в кратчайший реальный минимальный R2, когда Nox наконец работает самостоятельно и доказано делает реальное полезное.
2. Что ещё требуется для полной расширяемой межпрофессиональной агентной системы, как перейти к ней в R2.x/R3, без ложных обещаний и искусственного занижения требований.

Cortex вправе переопределить границы при доказательной критике, но не может молча удалить саморазвитие, выбор стратегии или профессиональные знания.

## 5. Текущее подтверждённое инженерное состояние

Nox OpenCode local: branch r1/dev, clean, HEAD **68cc0ee20a25991ea275512e20ac521cc8f8234b** на момент независимого ревью. Не путать с документационным commit 3c3fed07. Любые новые данные требуют fresh source read.

R0 preserved: 252 files, 55/55 retained manifest; limited R1 P0 accepted, retained 39/39 offline suites PASS, сборка/типизация на исходном этапе PASS; это НЕ вся R1 и НЕ R2 acceptance.

Реальный локальный web test: создан рабочий четырёхфайловый статический task tracker. Финальные exact bytes прошли host browser checks **13/13 PASS** для tree a71660c6e6562f9542ed16013f4e24dedd3dcc179106ebc1bb9d72efe31ababe. НО сама миссия **PAUSED / NOT ACCEPTED**, 600111 мс при лимите 600000 мс, 2 repair iterations, unresolved intent eb2f2fcc-a5b9-47f2-ab2e-0e2f971a0dfc. Старый in-mission QA FAIL и late product PASS относились к разным деревьям байтов; PASS поздних файлов не снимает PAUSED без новой корректной процедуры.

Usage: пять completed calls reported subtotal **337014 токенов**, шестой UNKNOWN reported **104613**. Полные tokens/transport/provider dollars UNKNOWN; не выводить стоимость из subtotal.

Подтверждённые конкретные проблемы:
- src/tools/index.ts:407 — basename(safePath) при nested file_write регистрации порождает root duplicate и теряет product/ путь.
- QA получает максимум 6 artifacts по 12000 символов и 6000 execution-output: покрытие неполное. Простое увеличение window не решает текущий candidate epoch/full evidence/terminalization.
- Недоказанная связка полных артефактов, актуального QA результата, unresolved repair и терминального accepted; нужны точные locks/snapshot/revalidation/recovery.
- Нет доказанной стратегии no-progress, эффективность выбранного LLM→QA→repair web пути низкая. Система умеет parallel groups и recursion вообще, но конкретная web mission использовала 1 coder + серийные repairs.
- Head выбирает роли/инструменты/parallel, не конкретную модель. В src/config/models.ts есть host role defaults/routes; task-sensitive model ROI не доказан.
- ToolSearchProcessor и SkillSearchProcessor есть в установленном Mastra, но на HEAD не wired в specialists live path. Их нельзя называть работающими.
- LibSQL преимущественно message memory, semanticRecall/workingMemory не включены; provenance/ACL professional Knowledge System и PG-binding не подтверждены.
- TI/Manus read-only metadata не являются 4504 installed/callable tools; реальная полнота каталога ещё не пересчитана этим audit.
- P1 7/7 lessons vs no lessons показали отсутствие measurable improvement — не выдавать за доказанное обучение.
- Unpinned npx @playwright/mcp (не прямой lockfile dependency) требует compatibility/security/sandbox review.

Состояние installed packages на baseline: @mastra/core 1.82.0; @mastra/mcp 2.8.0; @mastra/memory 1.41.0; @mastra/libsql 1.29.0; @playwright/test 1.49.1. Установленные API versions всегда сверять с current source.

Ревью OpenCode было READ-ONLY и docs-only: он не делал новых live model calls, tests, installs, mission/deploy, не менял Nox. По итогам docs были опубликованы успешно.

## 6. Готовый план OpenCode для критической проверки Cortex

Инженерные темы I-01..I-07 (всё SPEC, ещё НЕ IMPLEMENTED):
I01 исправить canonical nested artifact and registration/provenance;
I02 текущий candidate/versioned evidence/QA barrier, full manifest, no stale terminal;
I03 deterministic preflight, no-progress, cumulative time budget и разумный paid QA;
I04 native ToolSearchProcessor per delegation на текущих GRANTS, search/load/active, schema/id/recovery;
I05 один pinned permission-safe useful external adapter в sandbox с receipt и rollback;
I06 Knowledge+Skills: authorised sources, ACL, portable SKILL.md, held-out fresh-agent transfer, no brand new parser DB;
I07 host-owned strategy + model routing с paired accepted-outcome economics.

G0 artifacts/current QA/lifecycle correctness; G1 native granted discovery; G2 один read-only tool acquisition; G3 transferable source/skill; G4 strategy/economics; G5 full direct Nox acceptance T01–T12. Не строить третий orchestrator без доказанной необходимости. Проверять CandidateEpoch/EvidenceBundle на возможность native reuse вместо собственного subsystem. Отдельные небольшие tickets и реальные тесты, не «всё R2 в одном PR».

## 7. Каталог, проверенные типы, компании, deliverables

Исходные **4504 RAW записи**: iirepresent.json — 1331, Радар.json — 3173, legacy catalog csv. НЕ 4504 уникальных и установленных плагинов. Cortex обязан сохранить каждую входную строку, ID, raw fields/URLs, many-to-many dedup/crosswalk, source digest, actual type, license/safety/permissions/version/compatibility/price/evidence. Разрешено не исполнять все 4504, но нельзя не инвентаризировать любую из них.

Без искусственных численных лимитов искать дополнительные MCP, SKILL.md, tools, CLI/API/SDK, web/browser, professional libs, standards, knowledge, code, domain packs и validated oracles. Разрешено привлекать столько research agents, superagents, моделей, независимых ветвей поиска и исполнителей исследования, сколько технически и организационно доступно; действующие расходы/лимиты/лицензии и границы прав не снимаются. Быстрый полезный shortlist и готовый integration path должны быть ранним результатом, не после десятков отвлечённых отчётов.

Изучать Mastra native ToolSearch/SkillSearch/Workspace/MCP/HITL, Agent Skills, official MCP Registry (discovery != trust), Composio vs Pipedream Connect vs Arcade для реального OAuth gap, ToolHive по необходимости, Docling/Crawl4AI/парсеры, Promptfoo/Langfuse/Inspect AI по доказанному QA gap, Playwright/DevTools/Figma/UI Kits/accessibility/anti-slop. Unslop проекты heydamir/unslop и 0design/unslop-skill разные. Enterprise production patterns: OpenAI Codex, Anthropic Claude Code/Agent SDK, Google ADK/Agent Engine, Microsoft Agent Framework, AWS Bedrock, Cognition Devin, Salesforce Agentforce, Intercom Fin, LangGraph и Mastra. Строго original primary sources, не выдумывать closed implementations.

Build-buy verdict **A–H**: already working, configure native, ready-made, thin adapter, heavy integration, custom ONLY proven gap, reject/defer, UNKNOWN. Evidence **L1–L4**: found, source+version+license vetted, actual sandbox executable check, independent paired uplift. Не путать эти уровни.

Сохранить 22 раздела, все 18 deliverable families (exec verdict, fresh audit, full 4504, new registry, integration atlas, enterprise cases, competence graph, knowledge system, tool acquisition, execution strategy, meta/learning, domain packs, build/buy, R2 T01–T12, OpenCode ticket package, fastest safe path, source/evidence ledger, owner decisions) и checksum/consistency. Все T01–T12: deterministic route; tool selection; safe new acquisition; professional source knowledge; held-out transfer; full professional web with visual and accessibility+terminal acceptance; bot/script/workflow choice; unknown professional domain; adversarial injections; interruption/recovery/idempotence; cost strategy comparison; direct Nox execution without OpenCode solver. Domain QA, privacy/ACL, permissions, snapshots, unknown effects, budget included.

## 8. Последние утверждённые рекомендации для ФИНАЛЬНОГО промпта Cortex

Ревью OpenCode в 03/04/05 **принято**. Не нужно снова посылать его на ревью.

Финальный промпт Cortex должен поверх файла 04 добавить три главных акцента:
**(1)** не потерять универсальную open-world профессиональную цель; отдельно описать первый практически принимаемый R2 и полный целевой путь R2.x/R3 без искусственного сужения или несбыточной аккредитации.
**(2)** исходить из существующего Nox, REUSE FIRST, интегрировать конкретные проверенные MCP/Skills/SDK/API/CLI/library + exact module paths, minimal wires, tests, rollback, TCO. Доказать, что новый custom code абсолютно необходим; actionable ranked fast-path выдавать в первую очередь, не бесконечное исследование.
**(3)** Cortex без искусственных ограничений использует исследовательских суперагентов, модели, инструменты и параллельные агентные команды; но только внутри реальных технических/финансовых лимитов и действующей власти. Нет implicit authority на purchases, new secrets, production writes или interference OpenCode.

Сквозной ценностный критерий — стоимость, скорость и качество **независимо ПРИНЯТОГО результата**, а не длина кода, число агентов и красивое количество Markdown отчётов. Сложность современного enterprise подхода обоснованна только measured uplift.

## 9. После Cortex — отдельная тема, НЕ сейчас

Будущее инженерное ТЗ OpenCode должно обеспечить unattended safe engineering в разрешённом workspace: широкий технический выбор, доступные готовые плагины/SDK/MCP, разделение на подзадачи, итерации без постоянного согласования штатных деталей, checkpoints, Git evidence, QA, rollback, авто-продолжение разрешённых этапов. Пользователь хочет отдыхать, не получать сотни prompts. При этом текст промпта не отменяет системные approval gates, запрещённое расширение прав, покупки, публикации и опасные действия. Авторизацию определять отдельным scope.

Другие исторические сведения: AWE E0 был когда-то принят, E1 LIVE не доказал полной автономности; CAREER-01 HH, большие агентные команды, Tool Intelligence, QA и Orchestrator — долгосрочный проект, но текущая непосредственная задача только Cortex R2 research. Router.Cheap global model replacement обсуждался отдельно; блокировка политики GPT вызвала переключение OpenCode на Kimi, но это не лицензия на bypass. Служебную переписку с поддержкой сейчас не продолжать.

## 10. НОВЫЙ ЧАТ — что делать с первого ответа

1. Сначала открой и прочитай в GitHub именно 03 и 04 (и по надобности 05) на pinned commit 3c3fed07, а также 02 RECENT-DECISIONS и 03 NEXT-CHAT-START-PROMPT из этого checkpoint. Не rely on summary instead of source.
2. НЕ переспрашивай пользователя ничего уже решённого. НЕ повторяй архитектурную дискуссию. НЕ проси ещё раз OpenCode на ревью. НЕ запускай реализацию Nox.
3. Сразу составь большое самодостаточное, качественное, ready-to-send **ТЗ/промпт исследователю Cortex** на русском с 22 разделами, полными обязательными 4504/T01–T12/18 deliverables и тремя усилениями §8. Лучше готовый WritingBlock/Markdown file.
4. Если создаёшь артефакт, сохраняй версионированную финальную редакцию, не меняя первичные 01/02/03/04/05, предоставь читаемый GitHub/link или подтверждённый downloadable .md.
5. После этого пользователь сам отправляет промпт Cortex. Никаких гарантий готового R2 до independent mission.

**Точка исполнения: ПИШИ ФИНАЛЬНЫЙ ПРОМПТ CORTEX R2 ПРЯМО СЕЙЧАС ПОСЛЕ ПРОЧТЕНИЯ ПЕРВОИСТОЧНИКОВ.**
