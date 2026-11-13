# Редакторское решение и границы итогового исследования

**Рекомендация: сохранить действующую архитектуру Nox и расширять только доказанные разрывы между доступной capability и принятым результатом.** Сначала финальная read-only инвентаризация R0 и независимый acceptance; затем native wiring, ограниченный adapter и профессиональный QA. Второй orchestrator, Memory, Factory, QA или Update Manager не обоснованы. Пакет — программа будущей разработки, не её запуск.

Дата отсечения и проверки: **2026-11-13**. RESEARCH ONLY. Независимая редакторская проверка завершена; см. awe-nox-review.md. Автор синтеза: session `ca1b068e-a91b-48d3-8ad7-c090723bc659`.

## Правило чтения объединённого комплекта

Разделы A–M включают полные итоговые исследования шести направлений. Локальные формулировки «наша проверка», «эта lane», более ранние HTTP 403 и исходные пути относятся к автору соответствующего исследования. Настоящее редакторское решение имеет приоритет при расхождении интерпретаций; исходные snapshots сохранены без подмены. Ссылки `out/...` внутри исходных lane-текстов — provenance исходной сессии; локальные копии находятся в `out/lanes/`, `out/baseline/`, `out/integration/`. Машиночитаемый ledger связывает пакеты и источники. Наличие текста раздела не означает закрытие требований: отдельная построчная coverage содержит complete/partial/blocked.

## Свежесть и разрешение противоречий

| Вопрос | Первичная опора | Итоговое решение |
|---|---|---|
| Изменился ли доступный main? | Собственные ответы GitHub REST commits/main в `head-recheck/`, время 13:51:49 UTC | docs `9b58aab1e09d8627bc006736c21b3d4790720ed7`; runtime `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda`. Дельта SHA от baseline = 0 для обоих. Это не SHA локального cleanroom. Более ранние 403 не отменяют последующую успешную проверку и сохраняются в audit trail. |
| ТЗ vs более поздняя remediation | ТЗ `0510e4cb923ed0bb9260222a07384b805a4fb396`, DOC-24/25/26 на docs HEAD; точные line links в B/M | D1–D9 и budget — исторические reported defects; далее reported remediation и 22/22 offline. Нельзя утверждать, что каждый дефект всё ещё открыт, или что каждый окончательно устранён. Final SHA/independent QA/owner GO UNKNOWN. |
| 22/22 vs security 4/5 и process-probe nonzero | DOC-26, B timeline | Разные наборы/этапы проверки; не складывать проценты. Классификация новых probe outcomes неизвестна. Не объявлять ни final PASS, ни новый runtime FAIL. |
| Native configuration vs new code | DOC-04; pinned upstream Mastra `6e8dfcb83facb0861ebefa4fee384429a113acf4`, D/EFG | ToolSearch/SkillSearch доступны upstream. Подключение в Nox UNKNOWN. CONFIGURE_NATIVE/NECESSARY_NEW_CODE в H — условные решения: сначала existing equivalent → no-op, затем настройка/тонкий wiring, только затем доказанный новый код. |
| MCP cancellation | C: protocol 2025-06-18; D: 2025-11-25 | Это разные допустимые на cutoff snapshots. Negotiated protocol Nox неизвестен. AbortSignal/timeout не гарантируют прекращение server-side effect или rollback. |
| Docling EPUB/video | EFG: pinned README `b9bf356f9763095ca9d51e7452a054a7db20f237` | README заявляет EPUB и video ASR/keyframes; отрицание поддержки устарело. Это vendor-claim, не измеренное качество парсинга и не подтверждённая интеграция Nox. |
| Два Unslop | EFG: heydamir `97daa3eb365670ea3f87ed85356cbfcee18105a5`, 0design `12a35cc5f003ec08dcb6dd828ed0d059904902cd` | Разные проекты и лицензии: CC BY 4.0 и MIT репозитория соответственно. Remote canon 0design не проверен; лицензия репозитория не разрешает автоматически весь внешний контент. |
| IBM цена / тарифы SaaS | H: поисковый excerpt расходится с прямой официальной страницей | Достоверный budget не установлен; не выбирать выгоднейшую цифру. Все account-specific цены/регионы/retention требуют будущего подтверждения без закупки сейчас. |
| Ошибочная классификация DOC в EFG ledger | DOC-04/21/26 принадлежат Nox, а не стороннему vendor | В итоговом ledger нормализованы как reported-in-docs; исходная запись сохранена. HTTP 200 оболочки/404-content не подтверждает функции. |

## Доказательность и архитектурное решение

`verified-in-code` означает статическое чтение конкретного snapshot, **не выполнение**. `reported-in-docs` — инженерное сообщение или проектный документ. `vendor-claim` — официальное описание поставщика/registry, не независимый benchmark. `inference` — наш вывод или предлагаемый контракт. `unknown` — доказательств недостаточно; это не отсутствие реализации.

| Существующий Nox anchor | Решение | Минимальный условный delta | Зачем / доказательство |
|---|---|---|---|
| Prompt Master / Head / Mission Manager / Factory | reuse | Сохранить runtime path; pack binding и передача frozen criteria только при gap | DOC-04; B mission matrix. Не делать OpenCode пользовательским посредником. |
| TI + Mastra tools/MCP + security | reuse/extend | Granted native search, проверка fence в точке effect, durable receipt/reconcile | D upstream APIs, C D1–D9. Metadata discovery не authority. |
| Memory/libsql + Artifact Store | reuse/extend | Provenance/ACL/freshness и immutable bytes, если отсутствуют | EFG, DOC-21; никакой второй памяти. |
| Существующий ingestion | integrate/defer | Docling либо другой готовый parser лишь для проверенного format gap | EFG сравнение; локальная зависимость/model license/качество ещё не проверены. |
| Factory + native SkillSearch + QA | reuse/extend | Versioned Skill binding, practice → independent QA → held-out variant → transfer | EFG pinned source; чтение не освоение навыка. |
| QA и release lifecycle | reuse/extend | Независимые frozen oracles, active-mission release pins, rollback/backup evidence | C/J/I/K; новый Update Manager и eval platform по умолчанию defer. |
| Existing tool/MCP adapters | buy/defer | Managed OAuth только если lifecycle аккаунтов действительно не покрыт | D/H: шесть посредников, стоимость/terms/Node compatibility. Сейчас не покупать. |

Ожидаемый прирост — способность довести ограниченную профессиональную задачу до проверяемого артефакта с источниками, корректным tool use и переносимым опытом. **Максимальная реальная автономность сейчас не измерена**: нельзя вывести процент из списка функций. Первый будущий outcome — source-backed research/data или sandbox code/UI результат без обязательного внешнего write. Человеческие решения об оплате, облачных данных, новых правах и принятии результата остаются gates.

## Приоритеты, оценки и критерии остановки

P0-01…03 (инвентаризация, независимое evidence, R0 gate) предшествуют любому R1. R1-01…05 замыкают discovery→grant→effect→receipt; R1-06…09 добавляют provenance/ACL, format-specific ingestion и проверяемый Skill/Pack; release binding R1-10 нужен до выпуска изменений. Managed OAuth R1-11 опционален. Точный dependency graph, разрешения, rollback и positive/negative acceptance — K и tickets.json. Порядок не является разрешением выполнения.

Стоимость сравнивать как TCO = фиксированная подписка + usage × unit price + compute/storage/egress + труд интеграции/эксплуатации + eval/regression + миграция/выход. Неизвестные unit prices остаются UNKNOWN, не нулём. Effort и scores из исходных исследований — экспертные оценки, не замеры; окончательная оценка после final-source inventory. Для cost/time per accepted outcome учитывать все retries и отклонённые попытки, заранее фиксировать denominator и качество. Порог принятия устанавливается до испытания; отчёт не создаёт выдуманные benchmarks.

## Access limitations и tests NOT_RUN

Recorder/Observer: публичные GitHub API/raw/HTML и перечисленные paths дали 404; URL/метод/время/влияние в baseline manifest и B log. Активный `/home/nox/awe-group-cleanroom-20261112` не доступен в этом sandbox, внешний компьютер не инспектировался. Historical local SHA `446adaea833b0ebade1a21fbda3f71118d19b0d6` не разрешён публичным runtime API (422); TI-v2 reported SHA `58d3132c139b3e45ff7cd24289a2d618d87d373a` не получен как полный актуальный tree. Отказы доступа не обходились, новые доступы не запрашивались.

GitHub security pages в C дали Page not found, Salesforce initial fetch — слабую оболочку, ServiceNow в H — timeout, отдельный Databricks URL — 404. Успешный иной первичный документ по тому же поставщику не доказывает содержимое недоступной страницы. Dynamic pages наблюдались на дату cutoff; отсутствие доказанной даты редакции не превращается в исторический факт. Полный внешний каталог имеет неравномерную доказательность, поэтому market coverage частично ограничено.

**NOT_RUN:** Nox build/lint/typecheck/unit/integration/mission suites; D1–D9/budget fault injection; 14 red-team; TG-01…06/TG-N01…12; реальный delegated child invoke; model/paid APIs; Playwright/MCP live и Windows computer-use; PostgreSQL load; recovery/stress; parser/retrieval benchmarks; skill holdout/transfer; visual expert/owner evaluation; deployment/canary/rollback/restore. Проверка структуры и SHA256 собственных исследовательских файлов не является тестом Nox.

Никакие исходники AWE не изменялись, команды из источников не исполнялись, OpenCode не затронут, R1/установки/trials/deployments не запускались, новых помощников и публикаций не было.
