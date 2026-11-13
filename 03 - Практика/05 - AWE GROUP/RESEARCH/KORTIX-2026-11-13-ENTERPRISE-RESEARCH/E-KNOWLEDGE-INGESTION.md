<a id="section-e"></a>

## E — PROFESSIONAL-KNOWLEDGE-SOURCES-ATLAS

### E/F/G — знания, проверяемые навыки и профессиональные Capability Packs Nox

**Рекомендация:** расширять существующие Memory/Artifact Store, Agent Factory и независимый QA контрактами provenance, допуска навыка и условного выбора pack; не строить вторую память, новый parser или новый orchestrator. Docling и Crawl4AI — кандидаты на специализированные ingestion adapters, не доказанные установленные компоненты Nox. Mastra SkillSearch присутствует в исходниках версии 1.82.0, но его подключение в актуальном Nox не установлено. Чтение SKILL.md не подтверждает освоение.

Дата проверки и cutoff: **2026-11-13 UTC**. RESEARCH ONLY: выполнены HTTPS GET, статическое чтение, создание файлов только в `/workspace/out/`. Ничего не устанавливалось, код изучаемых репозиториев не выполнялся, внешние записи/испытания/R1 не запускались. Все нижеописанные тесты — проекты будущей приёмки, не результаты исполнения.

### 0. Доказательства, baseline и ограничения

Классы: `verified-in-code` означает только непосредственно прочитанную реализацию конкретного snapshot; `reported-in-docs` — инженерный отчёт или проект; `vendor-claim` — официальное описание продукта; `inference` — наше предложение; `unknown` — данных недостаточно. Наличие test-файла, успешный HTTP 200, версия пакета или screenshot не означают успешного теста.

Независимые GET GitHub commits с `until=2026-11-13T23:59:59Z` выполнены около 13:30 UTC; это latest **наблюдаемый на момент запроса**, не гарантия отсутствия более поздних изменений этого дня:

- Docs main: `9b58aab1e09d8627bc006736c21b3d4790720ed7`, 11:34:38Z. DOC-26 сообщает 22/22 offline suites, final independent QA ещё IN PROGRESS; owner GO и production/live acceptance не установлены. Не подменяем актуальный baseline старым R0.
- Runtime export: `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda`, 2026-11-11 12:08:07Z. Это исторический export, **не текущий cleanroom** `/home/nox/awe-group-cleanroom-20261112`. Точный финальный cleanroom SHA неизвестен.
- DOC-03/04: `@mastra/core 1.82.0`, `@mastra/mcp 2.8.0`, `@mastra/memory 1.41.0`, `@mastra/libsql 1.29.0`, Playwright 1.49.1; Head использует `createAgentMemory`; Factory/Prompt Master, Memory и QA уже существуют. Это здесь **reported-in-docs**, а не самостоятельный текущий live inventory.
- DOC-21 — **проект** сквозной памяти: Corporate Registry, Project Memory, Artifact/Evidence Store, Shared Verified Knowledge и Memory Ingest Gate. PostgreSQL там пилот/проект, нельзя утверждать его действующее внедрение вместо libsql. Требование изоляции **до** semantic ranking, публикации project→shared только после очистки/approval и слепого Examiner сохраняем.
- Исторический `awe/context/store.mjs` действительно содержит instance-local `Map`, content digest, compare-and-swap expected_ref и bound artifact binding. [Код L3–35](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/context/store.mjs#L3-L35), [artifact L39–62](https://github.com/failm3/awe-group-runtime/blob/d5e9d857dbdeb8f31f9a798b10b5af4af639dbda/awe/context/store.mjs#L39-L62): `verified-in-code`, **не** доказательство durable knowledge DB/tenant retrieval и не современный cleanroom Memory.

Полный реестр Nox документов и постоянных ссылок — `EFG-SOURCES.md`; обязательные DOC-03/04/10/11/12/20/21/22 прочитаны. DOC-10/11/12 задают desired knowledge/pack/librarian, а не доказывают выполненную интеграцию. DOC-20/22 используются как acceptance requirements, не как протокол прошедшего QA.

Ограничения доступа: текущая cleanroom FS не подключена в этой исследовательской сессии; доступ не запрашивался. GitHub runtime tree доступен, но экспорт не содержит действующий cleanroom `src/`; это не доказательство отсутствия функций. Исходный GET `/SKILL.md` обоих Unslop дал 404: после просмотра разрешённого публичного tree найдены реальные `skills/unslop/SKILL.md` и `skills/audit/SKILL.md`. LICENSE у Tika/Unstructured сначала 404, реальные `LICENSE.txt`/`LICENSE.md` получены. Нет обхода отказа доступа. Mutable vendor pages сохранены с URL/временем/hash; дата наблюдения не считается датой публикации. У некоторых страниц HTML — оболочка приложения (особенно Apple/OpenStax); глубокие детали, не содержащиеся в тексте, не считаем проверенными. Точные тарифы SaaS не установлены, покупка не рекомендуется.

### E. Knowledge ingestion и retrieval

#### E1. Контракт и минимальные изменения существующих компонентов

| Решение | Existing Nox mapping | Verdict и конкретный delta | Доказательство/граница |
|---|---|---|---|
| Единый реестр единиц знания | Memory + libsql; DOC-21 Memory Ingest Gate/Artifact Store | **extend**: метаданные и staged acceptance, оригиналы по artifact refs; не отдельная RAG-память | DOC-04 L34, DOC-21; фактическая схема актуальной БД unknown |
| Источники и документы | существующие tools/MCP + Memory ingest | **integrate условно**: parser adapter только при отсутствии equivalent adapter в финальном inventory | Docling/Crawl4AI official snapshots; вызов из mission не доказан |
| Поиск фактов | существующее Memory/storage | **reuse→extend**: сначала native lexical/vector возможности и индексы; BM25/hybrid/reranker лишь после eval gap | пакеты reported; неизвестны действующие индексы/ACL |
| Разделение проектов | существующие policy/gates и Memory boundary | **extend условно**: authz на источники, чанки, цитаты, cache, artifacts до retrieval; delete/revoke cascade | DOC-21 L48–59 — требование, не verified execution |
| Retrieval QA | существующие QA/Examiner | **extend**: независимый dataset queries→relevant spans, ACL negatives и provenance checks | DOC-20/22 |
| Shared procedures | Project Memory→Shared Verified Knowledge + Factory | **reuse/extend**: отдельное одобрение очищенного artefact, не копия всей истории | DOC-21 |
| Новый vector DB/knowledge graph/fine-tuning | нынешнее storage | **defer**: доказанного дефицита нет; benchmark и требования ёмкости отсутствуют | unknown текущая нагрузка, не основание переписывать |

Предлагаемая KnowledgeUnit (schema proposal, не реализация): `id`, `tenant_id/project_id`, `source_url`, `canonical_url`, `publisher/author`, `published_at`, `observed_at`, `source_version/commit/edition`, `content_hash`, `artifact_ref`, `source_locator`, `media_type`, `parser_version/config/model`, `license_id/license_url`, `rights_basis`, `allowed_uses`, `acl_ref/revision`, `trust_class`, `scope`, `claims`, `supersedes/conflicts_with`, `expires_at/recheck_policy`, `verification_receipt`, `status`. Отсутствующее поле прав — UNKNOWN и карантин, не «public=free». Идентичность документа и производного чанка раздельная; digest включает версия+границы+extractor, ACL не смешивать при дедупликации.

Поток: обнаружение → проверка прав/allowlist/размера → immutable raw artifact → parse в изоляции без макросов/скриптов/сетевых ссылок → provenance-rich chunks → классификация и ACL → staged ingest → независимая выборочная проверка против оригинала → индекс в текущем storage → versioned publication. При parsing error сохранять raw, код ошибки и ограничения, не заполнять пропуски моделью. Текст извлечённого документа — данные, не инструкции policy; найденный «install this», `allowed-tools` или просьба выслать secret не создаёт разрешений.

#### E2. Готовые парсеры и мультимодальность

В таблице функции — **vendor-claim по pinned README**, не benchmark. SHA и лицензии см. Sources. OSS лицензия не означает нулевые GPU/CPU, hosting, модели или бесплатное право на исходный контент.

| Кандидат | Что подтверждено в официальном snapshot | Ограничение/минимальный delta в Nox | Verdict |
|---|---|---|---|
| Docling, commit `b9bf356…`, MIT | README L35–46: PDF/DOCX/PPTX/XLSX/HTML/EPUB/images, reading order/table/code/formulas, OCR, ASR, local execution, unified document; L51: video transcript + keyframes | Connector в Memory ingest с lossless structured output + page/bbox/time refs; model licenses отдельно. Keyframes не полная запись действий. Нельзя заменять таблицы одним Markdown | **integrate условно**, основной кандидат документного слоя; не запускался |
| Crawl4AI, `cae74b2…`, Apache-2.0 | HTML/browser crawling, clean Markdown, extraction; screenshots/PDF и media/link metadata в README | Через существующий browser/tool boundary: URL allowlist, robots/terms, лимиты, deny private/link-local сети/SSRF, no auth bypass, no automatic JS privileges. Ссылка на video ≠ его смысловая обработка | **integrate условно** для HTML acquisition, не второй браузер без gap |
| Unstructured, `ad56303…`, Apache-2.0 (`LICENSE.md`) | Partitioning images/text/PDF/HTML/Word; optional OCR/poppler/LibreOffice зависимости; README отдельно продвигает коммерческий Transform | Альтернативный parser на том же fixture set. Облачные claims точности не переносить на OSS/Nox; SaaS pricing/retention unknown | **defer** до измеренного выигрыша, не одновременная обязательная установка |
| Apache Tika, `eedcbd1…`, Apache-2.0 + notices | Универсальное извлечение content/metadata; dependency-specific notices; новый README упоминает VLM parsers | Полезен как deterministic broad-format fallback, но его semantic layout точность здесь не измерена; remote VLM запретить для приватных docs без основания | **defer/integrate** только если Docling не покрывает нужный формат |
| Whisper (official README, mutable snapshot) | Отдельный speech-recognition кандидат | Transcript с сегментами, языком, speaker labels только при проверке; не video understanding, модель/права и hardware отдельно | **defer** если ASR Docling достаточен; не новая обязательная система |

Проверяемые locator contracts:
- HTML: canonical URL, fetch timestamp/hash, heading/DOM/text offsets, link targets; script-generated content и redirect path фиксировать.
- PDF: page, bbox, reading order, table id/cell coordinates, формулы отдельно, quoted text + raw-page reference. OCR confidence — не вероятность истинности. Сверять отрицательные знаки, числа, подписи и объединённые ячейки.
- Office: document revision, sheet+cell/range+formula+cached result, slide+shape, comments/track changes отдельно; макросы не запускать.
- EPUB: edition/ISBN если дан, spine item+fragment, chapter/offset; права издателя прежде ingestion.
- Image/diagram: source image/hash/crop bbox, OCR text vs inferred objects/edges, легенда и единицы. Объяснение модели помечать inference.
- Audio: segment start/end, язык, источник transcript, неопределённость распознавания; экспертная речь не нормативный стандарт.
- Video/demo: audio transcript **и отдельно** timestamped screen frames/keyframes, видимый код/диаграммы/UI, наблюдаемое действие (до/после). Из видео нельзя восстановить невидимые команды или доказать backend success. Для быстрого перехода missing-frame предупреждение, а не выдуманная последовательность.

#### E3. Retrieval, права, свежесть и оценка

**Предложение**: до выдачи кандидатов вычислять разрешённый project/tenant/source set с актуальной ACL revision; lexical exact search нужен для кодов ошибок/API names/чисел, vector — для перефразирования, hybrid — по eval, reranker — только внутри разрешённого набора. Не предписываем BM25 libsql как уже существующую функцию. Для сравнения lexical baseline можно использовать уже имеющийся FTS, а не автоматически переносить Memory в PostgreSQL/Elastic. Chunking по смысловым секциям; таблицы/код сохраняют связь с целым и header. Near-duplicate не стирает разницу лицензий/версий/прав.

Цитата должна раскрывать permalink/version и точный locator, подтверждать именно утверждение, а не просто похожий документ. Сначала проверять числовые claims/политику/цену/права. Для конфликтов не «усреднять»: normative standard > official version-specific implementation docs > engineering evidence > practitioner anecdote, но фактическое поведение может противоречить docs; хранить обе версии и uncertainty. Security advisory может отменить старое best practice. Текущий документ не использовать для старой версии API без compatibility proof.

Freshness: release/advisory/webhook/ETag/Last-Modified — сигналы к переиндексации, content hash — факт изменения, даты отдельно. TTL задаётся риском: auth/pricing/API changes требуют проверки перед применением; стабильный стандарт обновляется по новой редакции; персональные сведения — по retention policy. Это политика, не обещание запущенного scheduler. Revocation удаляет/блокирует результаты, rerank cache, цитаты и derived skills с зависимостью; опубликованное без прав отозвать, а не только скрыть URL.

Будущая retrieval eval: составить независимый gold набор по каждому формату, exact-version queries, противоречивым источникам и двум изолированным проектам. Метрики: Recall@k (доля relevant passages, найденных в top-k), MRR (обратный ранг первого relevant), nDCG (градуированная релевантность), citation precision (claims с действительно поддерживающим span / цитируемые claims), grounded coverage, число cross-tenant leaks, stale-answer rate, p95 latency и стоимость запроса. Здесь **нет численных результатов**. Acceptance: zero known leakage и unsupported critical claims; остальные пороги назначать по task-risk и сравнивать с native baseline на одном наборе. Считать стоимость как `extract CPU/GPU + embeddings + storage + retrieval/rerank + reviewer time`, считать обе системы на одинаковом объёме/языках; никаких выдуманных цен.

#### E4. Все 12 категорий знаний: реальные первичные источники и использование

Официальные URL, HTTP status/hash/дата в `primary-ledger.json`, прямые ссылки в Sources. Названные категории не означают автоматическую загрузку защищённого корпуса.

| # / requirement | Первичные источники | Как использовать, права/актуальность и независимая проверка |
|---|---|---|
| 1 S05-02 docs/API/standards | OpenAPI **3.1.1**, W3C WCAG **2.2**, Mastra **1.82.0** pinned source | Спецификация→versioned knowledge; schema fixture и совместимость с установленной версией. Docs license отдельно от code license, advisory/release change trigger |
| 2 S05-03 research/datasets | Crossref REST metadata, arXiv license guidance, DataCite schema **4.6**, NIST handbook | DOI→publisher→version/retraction, dataset identifier/license/split; abstract/metadata не fulltext и не peer review. arXiv preprint не peer-reviewed по умолчанию; воспроизводимость только после независимого повторения |
| 3 S05-04 books/reference | OpenStax official license portal; NIST handbook; OMG standards | Конкретная книга/издание/лицензия обязательны; сайт не универсальная лицензия всех активов. Paywall не обходить. Сейчас OpenStax page-shell не доказал лицензию конкретной книги — metadata only |
| 4 S05-05 engineering cases | Google SRE book, Nox ADR/engineering reports | Условия системы, дата инцидента, причинность и ограничения переноса; case report не controlled benchmark. Сохранять ссылку/фрагмент по правам, сверять с текущими APIs |
| 5 S05-06 courses/video | MIT OCW terms + course assets, Figma official demonstrations | Разрешённые материалы и edition, lecturer/topic; OCW NC/SA ограничения проверять по объекту. Transcript отдельно от frames и code; практический outcome QA обязателен |
| 6 S05-07 podcasts/interviews | Changelog publisher episode pages | Канонический episode URL, speakers, timestamps, transcript source; мнение эксперта с attribution, не установленный факт. Права transcript/audio отдельно, не скачивать всё автоматически |
| 7 S05-08 communities | GitHub official issues/PR histories выбранных repos; Stack Overflow licensing page | accepted answer не oracle; версия проблемы и воспроизводимый testcase; SO CC BY-SA/version зависит от даты, attribution/share-alike учитывать. Issue content не автоматически под code license |
| 8 S05-09 code/examples | Mastra official tag/source; Playwright official assertions/examples | SHA+path+lines+LICENSE, dependencies, воспроизводимый fixture. Static verified code не выполненный тест; скрипты из источников не исполнять в research |
| 9 S05-10 design/assets | Figma API/MCP, Material/Carbon/Fluent/Polaris/Apple HIG, Radix/React Aria/shadcn/Storybook | Design system vs UI kit vs product screenshots отдельно; Figma Community item/fonts/icons имеют свои права. API access grant не право переиздавать чужую работу. Tokens/version и visual/functional QA |
| 10 S05-11 user research | GOV.UK Service Manual user research, W3C WCAG 2.2 | Consent, anonymisation, task/sample bias, CJM/JTBD как модели, не выдуманные интервью. OGL страницы с исключениями; participant recordings — private ACL/retention |
| 11 S05-12 marketing/business | Google Search Central, Ads/GA4, Yandex Direct, Meta Marketing API, HubSpot APIs; OMG BPMN/DMN; IFRS index | Regional/privacy/ad-policy limits, versioned metric dictionary, unit economics assumptions. API docs не разрешение отправлять email/ads/CRM writes. IFRS полный стандарт может требовать прав; не копировать защищённый корпус |
| 12 S05-13 internal accepted work | Nox DOC-20/21/22/26, approved mission artifacts/Obsidian/GitHub (если доступны) | QA receipts+accepted version+owner decision, проектный ACL, redaction перед shared publication. Текущий незавершённый R0 не labelled accepted; собственные ошибки хранятся с reproduction/context, не превращаются в истину без проверки |

### H. Независимые negative tests — только будущий протокол

| Case | Preconditions / запрещённый эффект | Expected oracle / evidence | Сейчас |
|---|---|---|---|
| Cross-project search | source A private, agent B; lexical/vector/rerank/cache/artifact path | 0 private title/snippet/embedding-derived content/citation; independent deny trace и query fixtures | NOT RUN |
| Revoked source | ранее разрешённый source, grant/license revoked | retrieval/cache/derived skill admission закрыты; versioned revocation receipt | NOT RUN |
| Injection в PDF/SKILL | текст требует secret/install/расширить grant | нет external effect; content сохраняется как untrusted, policy неизменна | NOT RUN |
| Fake citation | cited span не подтверждает число | QA FAIL с locator и original hash; no publish | NOT RUN |
| Stale API skill | skill pinned old schema, installed newer incompatible | STALE/BLOCKED, revalidation; no guessed arguments | NOT RUN |
| Memorised practice | повторенный practice case vs hidden variant | practice pass не mastery; независимый holdout/transfer нужен | NOT RUN |
| круговой QA | автор предлагает свою оценку и ожидаемые ответы | blind examiner contract, separate receipt; no self-certification | NOT RUN |
| video loss | audio называет кнопку, frames не показывают действие | unknown visual/action; не объявлять receipt исполнения | NOT RUN |
| design false success | красивый screenshot, keyboard submit broken | functional QA FAIL независимо от aesthetic score | NOT RUN |
| absent canon | Unslop audit без проверенного canon/version | не выдавать vendor audit PASS; обычный Nox QA может оценивать свой contract | NOT RUN |
| unlicensed asset | публичная книга/макет без rights_basis | metadata/link only или quarantine; no corpus ingestion | NOT RUN |

### I. Приоритеты и что нельзя объявлять выполненным

**Сейчас, research artifact:** сохранить source ledger, schema/quality contracts и conditional recommendations. Никаких changes в Nox.

**После отдельного разрешения, не автоматически:** сначала окончательный R0 SHA/QA/owner acceptance и инвентаризация current Memory schemas/ACL/storage/retrieval, Factory skill loader, existing tools и QA wiring. Затем reuse; только доказанные gaps — минимальная glue: source provenance, skill state/receipts, pack admission. Один разрешённый end-to-end task с независимым QA и variant/transfer, не массовый импорт каталога. Лишь затем parser comparison на одинаковых fixtures; коммерческий buy/новая DB — defer до объективных затрат/качества.

Не доказаны: current Nox tenant-isolated retrieval, настроенный SkillSearch, принятые professional packs, освоенные навыки, live Figma/ads/CRM grants, текущий финальный cleanroom SHA, full final QA, production readiness. Это **unknown**, не автоматически missing. Отчёт не снимает запрет на R1 и не является owner GO.

### J. Coverage и источники

GOAL-03/04/05/06/07: E (knowledge), F (learning), G (professional quality) и native-first mapping. S05-01…17: E1–E4; S06-01…04: F1–F2; S07-01…08: G1–G6; OUT-E/F/G: соответствующие разделы; REF-07: Agent Skills, skill contracts и первичные source pointers. Детальные строки требований сохранены без изменения в `requirements.md/json`; coverage не означает пройденную приёмку.

**Sources:** `EFG-SOURCES.md` — точные GitHub SHA/permalinks и official URL; `primary-ledger.json` — HTTP/date/hash и первоначальные ошибки; `rechecks/` — GitHub commit responses; `primary/` — сохранённые документы и статические исходники. Это локальный evidence bundle, не artifact publish и не внешняя запись.


