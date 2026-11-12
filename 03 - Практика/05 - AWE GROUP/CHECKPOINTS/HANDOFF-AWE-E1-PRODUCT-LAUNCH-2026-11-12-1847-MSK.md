# AWE GROUP — ПОЛНАЯ ПЕРЕДАЧА КОНТЕКСТА В НОВЫЙ ЧАТ
**Checkpoint:** 2026-11-12, evidence cut-off 15:47 UTC / 18:47 МСК.
**Статус:** актуальная передача целей, утверждённой архитектуры, результатов аудитов, испытаний и исполняемого задания OpenCode. Этот файл не означает, что миссия закончена.
**Владелец:** пользователь / AWE GROUP; автор передачи: архитектурный консультант ChatGPT.

## ПРОЧИТАТЬ ПЕРВЫМ В НОВОМ ЧАТЕ
Сохраняем исходную цель: **универсальная самостоятельно работающая мультиагентная AWE GROUP**, способная принимать произвольный пользовательский запрос, собирать специалистов и дочерние команды, выбирать платные LLM и разрешённые инструменты, реально выполнять работу, независимо проверять результат и сохранять состояние. **Не превращать проект в систему только для HH или только для сайта.**
**ТЕКУЩЕЕ ДЕЙСТВИЕ:** OpenCode уже получил и исполняет **`AWE-E1-PRODUCT-LAUNCH-01`**, запись старта в Recorder 2026-11-12T15:40:03Z / 18:40 МСК. В 15:46–15:47Z OpenCode работал над Этапом 0/1: прочитал спецификацию и материалы Codex, нашёл прежние зависшие миссии и проблему score-only QA, проверял browser screenshot и data propagation. **Не отправлять повторно новый /goal и не создавать конкурирующую миссию; сначала проверить текущие свежие логи**.
Полная спецификация OpenCode (авторитетная, дословная):
https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/PROMPTS/AWE-E1-PRODUCT-LAUNCH-01-2026-11-12.md
Запись проверена GitHub readback, commit **33e05103ca728deecaaee4b922656e03bbb87262**.

## 1. НЕИЗМЕННАЯ АРХИТЕКТУРА, ЕЩЁ РАЗ УТВЕРЖДЁННАЯ В ЭТОМ ДИАЛОГЕ
```
USER
  ↓
PROMPT MASTER — исходный запрос → версия ТЗ + неизменяемые критерии
  ↓
HEAD AGENT — сам решает создать нового агента или возобновить существующего
  ↓
АГЕНТ-РУКОВОДИТЕЛЬ / СПЕЦИАЛИСТ (динамический)
  ├─ собственные дочерние агенты и команды, вплоть до рекурсии
  ├─ управление задачами/параллелизмом/моделями/инструментами
  └─ реальное выполнение, артефакты и отчёты
  ↓
НЕЗАВИСИМЫЙ QA / ВЕРИФИКАЦИЯ по исходным owner criteria
  ├─ fail/repair при нарушении обязательного критерия
  └─ независимый gate, который нельзя ослабить ради PASS
  ↓
HEAD → ПОЛЬЗОВАТЕЛЬ, сохранение памяти и доказательств
```
- Владелец **отклонил модель с пятью заранее обязательными руководящими агентами** (Project Manager, Engineering Lead, Knowledge Manager, Capability Manager, QA Director) как фиксированную организацию; главная модель — динамические агенты под миссию, существующие агенты могут переиспользоваться.
- Постоянными являются **программные функции и контракты**: Prompt Master, Head, Agent Factory/delegation, Tool Intelligence, storage/context, policy/permissions/budgets, независимый QA. Это НЕ означает 7 постоянно активных LLM и постоянные расходы.
- Нужны реальные recursion depth / concurrency / retry / step / expense / rights limits; гибкость не равна бесконечным полномочиям.
- Не позволять агенту, который исполняет работу, менять критерии проверки; QA не должен выдавать PASS при недостатке фактических доказательств.
- Head не равен OpenCode: **OpenCode — внешний инженерный исполнитель/хост**, а AWE Head — внутренний управляющий агент. При дизайне AWE сама выполняет работу, OpenCode не подменяет разработчиков.
- Исходный Canvas и конституция Obsidian — первичный источник проекта: `AWE-GROUP-Architecture-v01.canvas`, `01 - Архитектура — решения и открытые вопросы.md`, `AWE-CONSTITUTION-v01.md`; дополнительные уточнения:
https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/%D0%90%D0%A0%D0%A5%D0%98%D0%A2%D0%95%D0%9A%D0%A2%D0%A3%D0%A0%D0%90%20%E2%80%94%20%D0%94%D0%98%D0%9D%D0%90%D0%9C%D0%98%D0%A7%D0%95%D0%A1%D0%9A%D0%98%D0%95%20%D0%A0%D0%95%D0%9A%D0%A3%D0%A0%D0%A1%D0%98%D0%92%D0%9D%D0%AB%D0%95%20%D0%9F%D0%9E%D0%94%D0%90%D0%93%D0%95%D0%9D%D0%A2%D0%AB%20%E2%80%94%202026-11-12.md

## 2. РЕАЛЬНАЯ СБОРКА ДО НОВОГО ЗАДАНИЯ
- Локальная рабочая сборка WSL: `/home/nox/awe-group-cleanroom-20261112`. Последний ранее проверенный local commit `9eb422b` + `4888dad`, `050ca8b`; remote `failm3/awe-group-runtime` main по предыдущему readback оставался `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda`. Не путать local worktree с удалённым main; перепроверять перед утверждением.
- Mastra/Node/TS Head, Prompt Master, Mission Manager, specialized roles и локальные инструменты; несколько cloud LLM через Router.Cheap, в том числе Claude/DeepSeek/Kimi. Selection primarily role mapping `selectModelForRole()`, адаптивная оптимизация capability/cost не доказана. Наличие родитель/дочерний/внучатый делегации не доказано.
- Manus Tool Intelligence v2 source копирован в `ti-service`; отдельный PostgreSQL 18 порт 5448 в `/tmp/opencode/ti-pgdata`; API localhost:8871. В working DB загружено только 12 research-sourced DISCOVERED записей. Чрезвычайно важно: это **не** полный canonical Manus 3415 export и **не** каталог NIVICT 4504. Сервис/PG недоказанно устойчивы после WSL перезапуска; временный /tmp источник хрупок.
- `ti_search` зарегистрирован и в предыдущих смоук-тестах получал реальные результаты. Но каталог всех проверенных инструментов ещё НЕ подключён как рабочие интеграции.
- Приоритетная security проблема: некоторые API/admin/DB/search секреты ранее оказались в записанных GitHub OpenCode Recorder событиях, хотя `.env` игнорируется git. Не копировать значения. Требуется ротация/ограничение доступа и защита дальнейшей телеметрии. Любой отчёт о том, что `.env` не закоммичен, НЕ закрывает данную проблему.

## 3. AWE-READINESS-01 — ФАКТИЧЕСКИЕ ТЕСТЫ И ДЕФЕКТЫ
Сводка независимой проверки:
https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/CHECKPOINTS/AWE-READINESS-01-INDEPENDENT-REVIEW-2026-11-12.md
Commit `975e5898864e1f6796551959abf91f6bb0324c14`, GitHub readback verified.
- Первые две более общие миссии `974efed1-79c2-4ba2-b585-f30b7c7b738b` и `8ef7b67f-c03e-4571-a885-840d71904e03` были прерваны через 10/15-минутные timeout; сохранились как `running` без процесса. Надёжное восстановление/resume НЕ доказано.
- Третья, суженная миссия `61e8f64f-595d-4bf2-ba7f-a9dd07d50745` реально завершена: Prompt Master → Head (3 делегации) → параллельные devops/researcher → writer → QA repairs 4→5→7 (threshold 6), `status=completed`.
- AWE DevOps вызвал **заранее подготовленный OpenCode** `scripts/awe-screenshot.sh` через `shell`; создан проверенный логом реальный screenshot.png 339260 bytes, 1280×720. Это подтверждает автономный **вызов готового инструмента**, но НЕ самостоятельное создание скрипта, не Playwright MCP через AWE и не профессиональный дизайн.
- В итоговом сохранённом `awe-browser-automation-test-report.md` ОБА TI-раздела содержали `Pending transcription...`, хотя QA дал PASS 7. Это **реальный ложный PASS**, нарушающий обязательные критерии. Data propagation researcher→writer недостоверен; нельзя принимать полный QA.
- Чтобы получить финальный PASS, OpenCode сузил первоначальную большую исследовательскую миссию до явной инструкции вызвать готовый screenshot wrapper. Не путать этот bounded proof с принятой OWNER миссией.
- Не доказаны рекурсивные подагенты, корректная независимая QA, полноценный resume, реальный агентский browser MCP, самостоятельная профессиональная разработка, UI владельца.
- Положительное: Head действительно планировал и делегировал, несколько ролей исполнялись, shell+TI поиск вызывались, параллелизм и сохранение артефактов наблюдались. Это рабочие зачатки, не бутафория.
- В итоговой оценке **AWE-READINESS-01 = PARTIAL PASS, NOT OWNER_ACCEPTED**, даже если внутреннее `status=completed`.

## 4. НЕЗАВИСИМЫЙ АУДИТ CODEX — КАТАЛОГИ 4504 И 3415
Задание аудита:
https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/PROMPTS/CODEX-INDEPENDENT-CATALOG-FORENSIC-AUDIT-01-2026-11-12.md
Issue #3: https://github.com/failm3/nivict-ai-academy/issues/3
Результаты: draft PR #31 https://github.com/failm3/nivict-ai-academy/pull/31, branch `codex/awe-catalog-forensic-audit-01`, head `4c7394b6bd6e6b69d0ec6eff24f5681b6db8e903` (повторно проверено перед checkpoint). **Draft, open, not merged**, 119 файлов.
- 4504 / 4504 исходные NIVICT строки учтены, источник 1331 iirepresent + 3173 Радар. JSON/CSV/Obsidian ID сверены, no substantive mismatches reported.
- 4504 external attempts, **4169 observed metadata/HTTP**; metadata/reachability НЕ proof security/functional ability. Unique GitHub project keys attempted 3256, 3010 observed, 207 redirects, 39 unresolved; additional HEADs 1209: 973 HTTP200, 149 other HTTP, 87 unknown.
- Полный Manus export **3415** найден: **3309 NIVICT rows → 3270 Manus records**; NIVICT unmatched 1195, Manus unmatched 145. Stable/project match ≠ semantic identity verified; все descriptions совпавших пар отличаются, семантическая проверка NOT_DONE. 3403 Manus DISCOVERED, 8 DOCUMENTED, 4 LIVE_TESTED, 0 APPROVED.
- 50 desk reviews: **30 архивных проектов, связанных с 32 исходными строками**, +20 архитектурных external additions. 98 pinned README/license texts; это НЕ 50 runtime/security audits.
- 36/36 consistency checks модели того же семейства, 59 strata; **different-family/blind QA NOT_RUN**, runtime/sandbox/approved/integrated = **0**. Статус честно **PARTIAL**.
- Пользователь загрузил в этот чат ZIP `AWE-CATALOG-FORENSIC-AUDIT-01-PARTIAL.zip`, `COVERAGE.md`, `AWE-CAPABILITY-GAP-MATRIX.md`, `CHECKPOINT(1).json`. Локальный путь Codex: `C:/Users/1/Documents/Codex/2026-11-12/awe-group-awe-catalog-forensic-audit/outputs/`; для нового чата авторитетнее persistent draft PR, чем ephemeral attachments/Windows paths. Архив ранее локально прошёл проверку контрольных сумм (published 117/117, local 122/122), не независимую проверку всех внешних сайтов.
- Основные выводы: не заменять Mastra Head без A/B реального пилота; reuse browser/MCP/GitHub/Workspace, Langfuse/tracing, existing PostgreSQL/memory и eval tooling; BUILD только необходимые AWE-specific интерфейсы: immutable owner criteria, actor/scoped identity and permissions, budget+recursive worker limits, independent QA gate, durable resume/idempotency, provenance/evidence.
- Прямой прирост скорости/интеллекта OpenCode **не измерен**. Аудит может уменьшить повторные исследования и самописную разработку; нужно измерять baseline vs enhanced, не сочинять %.
- Никакого автоматического merge draft PR #31, автоматических установок 4504 или объявления DISCOVERED=APPROVED.

## 5. НОВОЕ УТВЕРЖДЁННОЕ ЗАДАНИЕ — AWE-E1-PRODUCT-LAUNCH-01
Владелец дал прямое «погнали, пиши промпт» и решил совместить в **одной ограниченной по gate миссии** четыре направления:
1. **Устранить все воспроизводимые критические блокеры испытания**, но не лечить бесконечно все гипотетические неисправности. Обязательно: immutable criteria и negative QA test, report data propagation, timeout/recovery/duplicate effects, Playwright MCP настоящий вызов, минимум Head→child→grandchild with bounded permissions, secret safety.
2. **Усилить самого OpenCode** как разработчика — читать реальный PR #31 и сравнить максимум 3 полезных реальных tools/skills/MCP, подключить минимум одно безопасное действенное улучшение если реально повышает качество, измерить baseline vs enhanced. Не устанавливать всё и не менять `/goal`.
3. **Дать Head и динамическим подагентам AWE полноценный поиск каталога** через existing TI + normalized Codex data; раздельные provenance/status; импорт 3415 только в изолированный тестовый источник, без destructive overwrite working12; несколько реальных tool selections + denial negative test. Подбор инструментов ≠ разрешение на установку.
4. **АВТОНОМНАЯ первая дизайн-миссия AWE**: профессиональная русскоязычная адаптивная интерактивная веб-страница NIVICT для Product Design и AI Agent Engineering. Пользовательское ТЗ → Prompt Master → Head → динамическая команда (дизайн/код) → настоящая локальная страница, desktop/mobile screenshots, функциональный и visual QA, исходники и артефакты. **OpenCode не пишет сам дизайн/frontend за AWE**. Не выдумывать коммерческие кейсы/клиентов/статистику.
- Стадия 4 зависит от критических Gate 1 + Gate 3. Когда gate отсутствует, честный `PARTIAL/BLOCKED`, сохранять evidence и не подменять результат.
- **Все ранее разрешённые интеграции, интернет, web/browser, GitHub, CLI, локальные инструменты, подагенты и платные модели разрешены** в действующих лимитах Router.Cheap и других разрешённых провайдеров; **НЕ** запрет платных запросов. Не повышать лимиты или подключать новые платные продукты без отдельного разрешения.
- Изменения в отдельной инженерной ветке, PR не сливать автоматически, SHA+readback. Не изменять исходный `/goal`, owner acceptance и прошлые принятые артефакты. Отдельные непрогнозируемые эффекты, внешние аккаунты и необратимые отправки требуют полномочий. Не устраивать месячный refactor.
- Архитектурное правило: Head выбирает создать/возобновить агента, подагенты создают свои дочерние команды, QA не получает права изменять исходную приёмку.
- Источник **ПОЛНОГО** промпта (не переписывать/не сокращать без необходимости):
https://github.com/failm3/nivict-ai-academy/blob/main/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/PROMPTS/AWE-E1-PRODUCT-LAUNCH-01-2026-11-12.md

## 6. ТЕКУЩИЙ СТАТУС OPENCODE, ПРОВЕРЕН ПО RECORDER
Recorder: https://github.com/failm3/awe-opencode-recordings/blob/main/LATEST.md
Прямые evidence логи:
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/15-40/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/15-42/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/15-43/part0000.txt
- https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-12/15-46/part0000.txt
В **15:40:03 UTC (18:40 МСК)** новая OpenCode execution started; прочитал обязательную спецификацию и audit PR #31. В 15:42 обнаружил две `running` orphaned missions, скачал/изучал индекс Codex. В 15:43 подтвердил root cause QA: `passed` score-only, criteria не enforce. В 15:44–15:46 проверил browser screenshot, файлы, незакоммиченные прежние изменения, прошлую успешную миссию и data-propagation gap. **Нет доказательства завершения нового задания по состоянию этой передачи**. При продолжении обязательно обновить статус из новых логов, не повторять запрос, не запускать параллельную разработку.
Observer: https://github.com/failm3/awe-group-observer/blob/main/HEALTH.md; последний наблюдавшийся успешный сбор ~15:45 UTC, 0 consecutive failures. Observer — snapshot, не прямое доказательство PASS агентных тестов.
OpenCode recorder GitHub logs могут включать секреты: просматривать с редактированием, не пересказывать raw credentials.

## 7. ЧТО ДЕЛАТЬ В НОВОМ ЧАТЕ
1. Принять этот checkpoint и `AWE-E1-PRODUCT-LAUNCH-01` как действующий контекст. Владелец сказал, что после отправки промпта хочет **обсуждать свои новые мысли**, пока OpenCode работает. Не переключать его автоматически назад на аудит/архитектурный спор; слушать его вопросы.
2. Если просит статус — **проверить свежие recorder/observer** через connected GitHub и дать подтверждённые факты с отметкой evidence cut-off, без раскрытия ключей.
3. Не выдавать локальную AWE как production только из-за внутреннего PASS. Требовать реальные артефакты, независимые проверки, устойчивый resume, неизменяемый QA, обоснованные tool admissions и подагентную рекурсию.
4. После завершения OpenCode проверить по Gate 0–4; сделать независимый verdict, не ориентироваться на самоотчёт одного агента. Только потом решить owner console/Mastra Studio vs собственный UI.
5. Создавать точную архивную запись всех важных пользовательских/ассистентских решений и проверенные документы GitHub, без секретов. **Автоматическое архивирование каждого ChatGPT-сообщения до сих пор не доказано; не заявлять, что оно работает**.

## 8. СОХРАННОСТЬ И ГРАНИЦЫ АРХИВА ЭТОГО ЧАТА
- Ранее пользовательские сообщения 2026-11-12 сохранены отдельными файлами `CHAT-LOGS/2026-11-12/0001...` до `0041-user.md` с историческими пробелами нумерации. В текущей передаче продолжение `0042-user.md` — `0056-user.md` создано и прочитано через GitHub.
- Файлы пользовательских реплик — дословный текст видимой беседы, не системный экспорт ChatGPT. Тексты ответов ассистента сохранены как **содержательная хронология и отдельные оригинальные промпты/чекпоинты**, а не полный посимвольный экспорт всех DIL-разметок и интерфейсных реплик.
- Полную посимвольную копию каждого когда-либо отправленного ChatGPT assistant message эта интеграция не предоставляет; **не утверждать, что такая копия загружена**. Для полного platform-level архива нужен отдельный экспорт истории. Тем не менее все принятые ключевые решения, промпты, ссылки, факты и продолжаемая миссия сохранены.
- Исторически существующие документы: `CHECKPOINTS/AWE-ARCHITECTURE-VS-LIVE-2026-11-12-1541-MSK.md`, `CHECKPOINTS/AWE-RUNTIME-IDENTITY-INTEGRATIONS-UI-2026-11-12.md`, `CHECKPOINTS/OPENCODE-TI-INTEGRATION-VERDICT-2026-11-12-1558.md`.
- Исходные данные Codex в draft PR #31, а ZIP/файлы из сообщения владельца были прикреплены к предыдущему чату; не гарантировать, что в следующем чате они автоматически смонтированы.
- Основная область: `failm3/nivict-ai-academy`, `03 - Практика/05 - AWE GROUP/`.

**ONE-LINE HANDOFF:** Исполняем AWE-E1-PRODUCT-LAUNCH-01 в OpenCode (началось в 18:40 МСК), по плану Gates 0–4 → исправить доказанный ложный QA/нерабочий resume → усилить OpenCode выбранными инструментами из Codex audit PR #31 → дать AWE read-only catalog с governance → AWE сама создаёт профессиональный NIVICT веб-интерфейс и проходит независимую приёмку. Пользователь переходит в новый диалог обсуждать свои мысли; не начинать работу заново.
