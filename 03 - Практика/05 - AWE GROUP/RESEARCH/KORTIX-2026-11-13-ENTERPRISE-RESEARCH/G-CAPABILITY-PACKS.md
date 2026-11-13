<a id="section-g"></a>

## G — DOMAIN-CAPABILITY-PACKS

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

### G. Условные профессиональные Packs и независимые quality contracts

Pack обязателен **по deliverable**, не потому что продукт в моде. До допуска Head/Mission Manager фиксирует `task_class`, `required_outcome`, `excluded_scope`; Factory подбирает минимальный role/tools; QA применяет независимый contract. Pack не может сам расширить permissions. Ниже все девять полей для каждого решения. Все adoption verdicts — inference; готовность исполнения Nox unknown.

#### G1. UX/UI и Product Design — WEB/INTERFACE-DESIGN
1. **User task:** создать/переработать пользовательский интерфейс, landing, dashboard или прототип; для чистого research не нужен полный UI toolchain.
2. **Outcome/quality standard:** task completion, понятная IA/user flows/JTBD, согласованный brand/типографика/tokens/icons, responsive breakpoints, focus/keyboard/screen-reader, error/loading/empty states и reduced motion. WCAG 2.2 целевой уровень AA фиксируется contract; AA не равен качественному продукту или юридической гарантии.
3. **Verified sources:** Figma REST/MCP official introductions; Material 3, Carbon accessibility, Fluent 2, Polaris (URL редиректит к актуальным Shopify docs, не обещаем старый React API), Apple HIG (часть page-shell), WCAG 2.2; Radix accessibility, React Aria quality/accessibility, shadcn docs, Storybook a11y tests. GOV.UK user research — consent/метод. Это official descriptions, не независимый тест библиотек.
4. **Required capability/tool/API/MCP:** разрешённый Figma read/API/MCP для design context, browser/Playwright для реального interaction/render; одна подходящая design/component system, не все сразу. API scopes/plan limits проверять до доступа, Community assets/font/icon rights по элементу. Figma write не разрешён самим наличием MCP.
5. **Ready Skill/template/asset:** token sheet, IA/JTBD hypotheses, user flow/wireframes, component states и Storybook stories; Radix/React Aria primitives или shadcn исходники по stack fit. Unslop оба кандидата ниже; это эстетические процедуры, не общий oracle.
6. **Integration point in Nox:** **reuse** Factory+Prompt Master+browser tools+Artifact Store+QA; **extend** design brief/pack selection и visual evidence refs; conditional Figma adapter **integrate** только при подтверждённом gap.
7. **Evidence/test:** независимо от автора: keyboard flow, focus order/labels/contrast, mobile/desktop states, browser console/network, реальные task assertions; screenshots до/после с viewport/data/version плюс слепая продуктово-художественная оценка по ясности, иерархии, характеру, соответствию бренду и отсутствию шаблонного slop. Автоматический accessibility scan не полный WCAG audit; screenshot не функционирование. Пользовательские интервью нельзя фабриковать.
8. **Security/license/cost:** проектные макеты/recordings private, consent/retention; товарные знаки/fonts/images отдельно, OSS component licenses проверить у selected version. Figma/visual SaaS точные тарифы и entitlement не установлены. Платные trials не нужны для исследования.
9. **Adoption verdict:** **reuse/extend**, Unslop **defer до независимого сравнительного eval**. Backend не нужен каждому статическому лендингу. UI kit не заменяет информационную архитектуру, content и usability.

**Два разных Unslop:**
- `heydamir/unslop@97daa3eb365670ea3f87ed85356cbfcee18105a5`, `skills/unslop/SKILL.md`, CC BY 4.0. [L1–56](https://github.com/heydamir/unslop/blob/97daa3eb365670ea3f87ed85356cbfcee18105a5/skills/unslop/SKILL.md#L1-L56): direction из продукта, audit, nine-pass craft, согласование направления, reference assets. Это **reported procedure**, не подтверждённая эстетическая эффективность. При адаптации attribution, источник/изменения; не выдавать вкусовое правило «one bright element» за нормативное требование.
- `0design/unslop-skill@12a35cc5f003ec08dcb6dd828ed0d059904902cd`, `skills/audit/SKILL.md`, repository MIT. [L1–60](https://github.com/0design/unslop-skill/blob/12a35cc5f003ec08dcb6dd828ed0d059904902cd/skills/audit/SKILL.md#L1-L60): detector + judgement canon по MCP, audit пишет plans, execute отдельный режим; canon pinned/checksum, отсутствие verified canon блокирует pass. **Не подключали MCP, не запускали detector, не получали canon**. Лицензия кода не доказывает права на remote canon/его sources. Дополнительные зависимости и external availability — риск.
- Оба: candidate procedure для Factory/QA, не новые обязательные сервисы; сохранить независимого evaluator, сравнить с уже хорошими дизайнами и accessibility/brand requirements, учитывать false positive «slop». Не оценивать самим стилевым генератором его собственный результат.

#### G2. Software Engineering — CODE-CHANGE/WEB-PRODUCTION
1. **User task:** frontend/backend/mobile/desktop change по реальным требованиям, исправление defect, API integration.
2. **Outcome/quality standard:** принятие functional contract, security и reproducibility; maintainability/readme/manifest; не добавлять backend/DB если static deliverable его не требует.
3. **Verified sources:** OpenAPI 3.1.1, Playwright assertions, OWASP ASVS official project; pinned Mastra source. Для конкретного framework/mobile/desktop SDK будущий pack обязан pin official docs/lockfile, сейчас универсальная совместимость не заявляется.
4. **Required capability:** существующие code/browser tools, build/lint/typecheck/tests/API contract checks/dependency scanning/CI; только в будущем одобренном execution sandbox, не здесь. Release/monitoring — отдельный approved effect.
5. **Ready Skill/template/asset:** existing role template + repo conventions, OpenAPI schema fixtures, Playwright assertions/test examples, threat checklist, readme/manifest/build recipe. Не новый scaffold ради самого scaffold.
6. **Nox point:** **reuse** Agent Factory, delegated executor, security/cancel/lease gates, browser, QA; **extend** pack admission/receipt dependencies, conditional framework docs.
7. **Evidence/test:** независимый fresh checkout+locked environment build/lint/typecheck, positive/negative API tests, e2e реального browser, authz edge cases, dependency scan triage, performance budget по задаче и monitoring signals; release artifact hash. CI green без product acceptance недостаточно.
8. **Security/license/cost:** dependency versions/SBOM/license notices, secrets не в logs; supply-chain/script review; CI/hosting usage priced отдельно, цифр нет.
9. **Verdict:** **reuse/extend**; buy CI/eval/monitoring только после gap/cost comparison. R1 release не запускать.

#### G3. Product & Marketing — PRODUCT-EXPERIMENT/CAMPAIGN-DRAFT
1. **User task:** исследование сегмента, позиционирование, тексты/креативы, SEO/SEM/CRM/email план, анализ конверсии/атрибуции или дизайн A/B.
2. **Outcome/quality standard:** evidence-backed сегментация/JTBD, проверяемые claims, согласованные metric definitions, UX writing/brand fit, consent/privacy, обоснованный бюджет. Не обещать causal uplift по корреляции.
3. **Verified sources:** Google Search Central SEO Starter Guide, Google Ads API start, GA4 Data API, Yandex Direct docs, Meta Marketing API, HubSpot API overview; GOV.UK research и NIST статистика. Official pages подтверждают families/доступ к документации, не наличие Nox grants.
4. **Required capability:** read-only sanctioned analytics/CRM exports/API, spreadsheet/statistical tooling; draft creatives. Google/Yandex/Meta выбор по региону/accounts/законности; ads publishing/spend/email sending требуют отдельного approval, scopes/quota/current API version.
5. **Ready Skill/template/asset:** research brief, hypothesis/evidence matrix, positioning/message map, SEO checklist, tracking plan, budget/unit-economics sheet, pre-registered experiment plan с primary metric/sample/stopping rule.
6. **Nox point:** **reuse** registry/tool gateway, Memory ACL, Factory marketer/analyst, QA; **extend** privacy and claim-check quality contract; новый vendor connector **integrate** только при missing pathway.
7. **Evidence/test:** независимая проверка источников/чисел, baseline и cohort definitions, sample-ratio mismatch/временные confounders, holdout where feasible, attribution window, conversion denominators, статистическая неопределённость, creative/readability/privacy/ad-policy review. Preview не факт размещения, delivery receipt не ROI.
8. **Security/license/cost:** PII minimisation, lawful basis/consent, opt-outs/retention, запрет чужих audiences; API terms/региональные ограничения; бюджеты и subscription pricing unknown. Не покупать рекламу в исследовании.
9. **Verdict:** **reuse/extend**, **defer** writes/spend и SaaS purchase до явного разрешения/экономики. CRM documentation не готовая CRM интеграция.

#### G4. Business / Management / Operations — PROCESS/DECISION-PACK
1. **User task:** process mapping, project/operations plan, pricing/unit economics, procurement/customer support/CRM/ERP reporting и обоснование решения.
2. **Outcome/quality standard:** проверяемая модель inputs/assumptions, responsibilities/approvals, reconciliation, scenario/sensitivity и audit trail; нельзя назвать финансовый forecast фактом.
3. **Verified sources:** OMG BPMN **2.0.2**, DMN **1.5**, IFRS issued standards index, NIST handbook; HubSpot APIs как пример CRM pathway. IFRS — не универсальный стандарт любой management-модели и не лицензия на копирование полного текста.
4. **Required capability:** approved read-only CRM/ERP/табличные inputs, diagram/model artifacts, decision routing через существующий Manager; бухгалтерские posting/procurement/order/payment — отдельный granted tool и approval, не автономное действие pack.
5. **Ready Skill/template/asset:** BPMN diagram и event/exception table, DMN decision table, RACI/decision log, pricing assumptions и unit economics worksheet, support knowledge article с escalation criteria.
6. **Nox point:** **reuse** Head/Manager, Artifact/Project Memory и QA; **extend** required evidence/decision signatures и financial formula validation. Не внедрять вторую ERP/workflow систему.
7. **Evidence/test:** независимая трассировка процесса happy/exception/cancel, owner review, unit consistency, reconciliation totals, formulas vs cached values, sensitivity и cash-vs-revenue distinction; holdout business case. Ни BPMN validity, ни красиво оформленный отчёт не доказывают экономическую целесообразность.
8. **Security/license/cost:** commercial records/procurement terms private, least-privilege redaction, approval separation; платные стандарты/ERP rights индивидуальны; стоимость покупки unknown.
9. **Verdict:** **reuse/extend**, **defer/buy conditional** только если существующие системы не покрывают доказанный gap; финансовые/юридические заключения высокорискового класса — domain expert approval, не автоматический final verdict.

#### G5. Research / Data / Content — EVIDENCE-REPORT/DATA-ANALYSIS
1. **User task:** фактчекинг, профессиональный обзор, статистика/визуализация, таблица/документ/PDF/deck, анализ audio/video.
2. **Outcome/quality standard:** traceable claim→source span/version, корректные единицы/методы/uncertainty, воспроизводимый data lineage; отделять vendor claims и выводы, no fabricated citations.
3. **Verified sources:** Crossref REST, DataCite **4.6**, NIST handbook, arXiv license docs, Vega-Lite official docs, Docling/Crawl4AI snapshots и W3C guidance. DOI metadata не гарантия достоверности/peer review.
4. **Required capability:** existing sanctioned search/HTTP/browser/files/data tools; conditional parser adapters в E2; chart/document renderer по existing tool inventory; никакого незаметного upload private dataset в SaaS.
5. **Ready Skill/template/asset:** source ledger, evidence table, methods/limitations section, data dictionary, versioned notebook/recipe как статический asset, Vega-Lite chart spec, presentation/story outline. Выполнение notebook отдельно gated.
6. **Nox point:** **reuse** Memory/Artifact Store/Factory researcher+analyst/QA; **extend** source locators, citations, data lineage и holdout tests; не новая knowledge platform.
7. **Evidence/test:** независимое пересчитывание samples/aggregates, denominator/units/timezones, missingness/outliers, leakage/split checks; chart scales/labels/accessibility; PDF page citations; audio/video timestamps и визуальная сверка, uncertainty/retractions. Review текста не замена data correctness.
8. **Security/license/cost:** dataset/article/recording licenses отдельно; consent/ACL/retention, redaction; hosted OCR/ASR pricing и retention unknown, local compute не бесплатно.
9. **Verdict:** **reuse/extend**, **integrate conditional** document extraction, **defer** commercial platform до измеренного benefit.

#### G6. Полезное расширение без дублей

**Accessibility & localisation overlay**, не шестой отдельный orchestrator: (1) task — интерфейс/контент для другого языка или assistive tech; (2) outcome — WCAG 2.2 + locale correctness; (3) sources — W3C/React Aria/official platform HIG; (4) capability — existing browser/screen-reader-compatible review and locale fixtures; (5) asset — terminology/glossary/RTL/number-date checklist; (6) Nox — overlay на UX/engineering/content packs через Factory+QA; (7) test — keyboard/zoom/RTL/text expansion/locale dates и независимый носитель/эксперт при high risk; (8) privacy/fonts/translation rights/cost отдельно, тариф unknown; (9) **extend/reuse**, не дублировать UI pack. Это переносимый gap-контракт, не заявление что автоматический тест заменяет accessibility специалиста.

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


