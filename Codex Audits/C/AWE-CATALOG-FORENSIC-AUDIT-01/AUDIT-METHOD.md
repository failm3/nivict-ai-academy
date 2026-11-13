# AWE-CATALOG-FORENSIC-AUDIT-01

Статус: **PARTIAL**. Дата: 12 ноября 2026, Москва. Инвентаризация исходного корпуса завершена; исследование пригодности/безопасности и cross-family QA не завершены. Никакие технологии этим отчётом не допущены в AWE.

## Источники и границы

Задание: [полная спецификация](https://github.com/failm3/nivict-ai-academy/blob/5c611773bff3ccba76b78337534ed8944e137236/03%20-%20%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0/05%20-%20AWE%20GROUP/PROMPTS/CODEX-INDEPENDENT-CATALOG-FORENSIC-AUDIT-01-2026-11-12.md), [issue #3](https://github.com/failm3/nivict-ai-academy/issues/3). Реализация TR-01 / issue #20 в этот аудит не входит.

Academy зафиксирована на `5c611773bff3ccba76b78337534ed8944e137236`. Использована отдельная sparse Git-копия и новая ветка `codex/awe-catalog-forensic-audit-01`. Первые восемь обязательных файлов сохранены без изменений. `EVIDENCE/SOURCE-MANIFEST.json` содержит реальные SHA-256 и совпавшие Git blob SHA; каждая строка реестра содержит источник, 1-based row, исходный URL, описание, полный raw_record, source SHA и ID. Существующие инфраструктура, OpenCode, WSL, PostgreSQL, процессы, ключи и настройки не изменялись.

Manus: найден локальный `AWE-Tool-Intelligence-v2-all.zip`, SHA-256 `5855ce5cfdb0abda44954108bfe2cfa1bec97dbf7c51db7be822eb04541d5ec1`. Все ZIP members прочитаны как байты, CRC проверены при чтении, хеши записаны. Материализована только явная allowlist данных/документов/кода; `extractall`, DB restore, импорт Python-модулей Manus, установка зависимостей и запуск его тестов не выполнялись. `git bundle verify` подтвердил complete history и HEAD `58d3132c139b3e45ff7cd24289a2d618d87d373a`. Bundle и два backup members совпали с вложенными манифестами. Подпись автора/цепочка доверия **не подтверждена**; хеш не является подписью. Исходные source-v2.zip и delivery-v2.tar.gz, перечисленные во вложенном манифесте, внутри outer ZIP не найдены, но полный registry export присутствует.

## Полный учёт и сверка

- Прочитаны все 1 331 `iirepresent` и 3 173 `Радар`: **4 504** raw records. Проверены key shapes, URL/description, ID, порядок/row, все поля classified JSON против CSV, все заметки, их frontmatter и отрендеренное исходное описание.
- Множества original IDs = inventory IDs = classified IDs = CSV IDs = note IDs. Кардинальность каждого набора 4 504; потерянных/добавленных строк нет. Содержательных расхождений **0**.
- Проверены 72 категорийных файла, ровно 4 504 ссылки на исходные ID. Canvas фактически содержит 134 узла / 121 ребро, уникальные node IDs, dangling edges=0. Старое описание 126 узлов относится к прежнему срезу до информационных дополнений, не к текущему числу.
- Исторические raw SHA в validation-report не совпадают с Git LF-байтами. Точное преобразование LF→CRLF воспроизводит оба старых SHA. Это **EXPLAINED_HISTORICAL_BYTE_MISMATCH**, не свидетельство потери содержимого. Новые SHA не подменяют старые.
- Все 4 090 строк issues и все старые группы duplicates независимо сверены. Вариант parser, разрезавший frontmatter по `---` внутри URL, и HTML-escaping false positives исправлены до итогов. 16 экранированных описаний обратимо соответствуют оригиналу.

Дополнительно сверены прежние `NIVICT-Radar-Cleaned` и shortlist: 4 424 entries содержат ровно 4 504 уникальных source/row occurrences, все исходные URL сохранены среди entry/alternate URLs, mapping issues=0. Все 23 source-present claims старого shortlist соответствуют исходному project/row. Cleaned entry хранит выбранное описание: 78 исходных описаний не повторены дословно в нём, поэтому этот lossy derivative не заменяет raw corpus. `EVIDENCE/PRIOR-RESEARCH-RECONCILIATION.json` сохраняет результаты и SHA optional inputs. Это подтверждение происхождения, а не старых runtime/verification claims.

## Нормализация и сущности

Сохранены отдельные уровни. Точный URL — исходная строка без изменений. Консервативный URL приводит scheme/host к каноническому виду, убирает стандартный port, добавляет `/` для пустого path; **сохраняет case path, query, fragment и www**. Разные query/path не склеиваются. Для GitHub дополнительно строится case-insensitive owner/repo key; ветки/файлы/issue могут принадлежать одному проекту и оставаться разными ресурсами.

Получены: **4 472 exact URL**, **4 471 conservative URL**, **4 465 project-or-resource keys**. Это не число доказанно уникальных технологий. Legacy full-normalization даёт 4 466, host/path-only — 4 424, точно воспроизводя старый отчёт. Legacy lowercases/decodes path и теряет query/fragment на втором уровне; 42 различия full URL дополнительно схлопываются. Такие группы сохранены как кандидаты/коллизии, не использованы для удаления строк.

## Классификация и внешние проверки

Поле `prior_classification` сохраняет все старые категории/флаги/confidence. Capability keywords — только LOW-confidence hints, не функциональные факты. Три подтверждённых первоисточником ошибки исправлены в новых categories с сохранением старых: MapSCII (картография), Screenshot Studio (изображения/дизайн), OWASP Cheat Sheet Series (security reference). Четыре целевых README проверки не являются случайной выборкой для оценки процента ошибок всего корпуса.

GitHub metadata проверялась через подключённый GitHub connector, пакетами с cache, ограниченной параллельностью и сохранением ошибок. Пройден весь набор **3 256** project keys; один transport failure повторён успешно. Итог: 3 010 metadata observations, 207 redirect-needs-review, 39 unresolved (включая 404 и observed access blocks). Архивированы по metadata 68 проектов. `pushed_at` — активность репозитория, не гарантия поддержки. Переезд сам по себе не означает мёртвую ссылку, но требует проверки нового owner/path/ID.

Для всех **1 209** остальных различных URL выполнены unauthenticated HEAD: 973 HTTP 200, 149 других HTTP responses, 87 network/policy unknown. Коллектор ограничивает workers и соединения по host, проверяет публичные DNS/IP, запрещает userinfo/nonstandard ports, ограничивает redirect chain, использует TLS validation, retry/backoff; тела/JavaScript не читает, программы не скачивает. DNS check не является изоляцией недоверенного сетевого клиента от всех вариантов DNS rebinding. 403/405/429/timeout не доказательство исчезновения сайта; 200 может принадлежать login/parking/redirect странице.

**4 504/4 504** строки имеют внешнюю попытку. Для GitHub это API уровня project entity: глубокий path исходного URL не проверен этим запросом. Получено внешнее наблюдение для 4 169 строк; оно не равно подтверждению продукта/автора/лицензии/безопасности. `externally_verified=0` намеренно зарезервирован для завершённого независимого verification gate. Точные знаменатели и определения — `COVERAGE.json`.

## Технические обзоры и архитектура

`TOP-50-DEEP-REVIEW.md` и `TECHNICAL-REVIEWS.json`: 49 репозиториев + официальный Figma MCP. **30** обзоров имеют exact GitHub-project match с **32** исходными строками; 20 — явно отмеченные архитектурные дополнения, включая ссылки вне project URL архива. Прочитаны 98 pinned README/license texts; их Git blob SHA независимо вычислены из UTF-8 и совпали. Для первых 40 repo дополнительно зафиксированы commit date и последние release metadata (38 releases наблюдены). Релизные бинарники/подписи всех артефактов не проверялись.

Дополнительно прочитаны 2 файла логики делегирования (Agent Zero/Hermes) и 8 manifest/config files. Cargo.toml для C-проекта codebase-memory-mcp дал 404; это ошибка выбранного пути, не отсутствие инструмента. Полный исходный код этих проектов, транзитивные зависимости, Windows/WSL совместимость, производительность и эксплуатационная безопасность не аттестованы. Лицензии с EE/algorithm/weight исключениями рассматриваются по scope; GitHub `NOASSERTION` не означает отсутствие лицензии.

Архитектурные документы и их hashes перечислены в `EVIDENCE/ARCHITECTURE-SOURCE-INDEX.json`. Текущий cleanroom runtime не обследовался напрямую. Наблюдённый remote main AWE: `d5e9d857dbdeb8f31f9a798b10b5af4af639dbda`; текущего Mastra Head/ti-search source в его дереве не найдено. Число рабочих 12 и результаты OpenCode — **заявления pinned отчётов**, не свежий независимый DB readback. Не выдано заключение о production readiness.

## Независимый QA и ограничения

Отдельный агент написал собственные пересчёты без импорта основного скрипта: IDs/content, duplicates/issues, 59/59 непустых category×confidence strata, негативные URL/parser cases, Manus overlap, 19 high-risk shortlist, все 12 keyword-flagged IDs и source slice Manus. Позднее дополнительно проверены 9 расширяющих shortlist кандидатов. Полученные замечания включены; оригинальные QA evidence сохранены.

Это отдельный аудитор **того же семейства GPT**, знакомый с родительским контекстом. Полный blind protocol и другой model family **NOT_SATISFIED**. Платный внешний examiner не вызывался. Поэтому ни одному решению не присвоены APPROVED/INTEGRATED/SANDBOX_TESTED, глобальный COMPLETE запрещён. Стратифицированный source screening нельзя выдавать за проверку всех функций всех записей.

Семантические противоречия всех 3 309 сопоставленных описаний не проверены: текст в обеих базах различается у всех matched rows, что само по себе не противоречие. Совместимость 12-row runtime и full Manus backup, полный transitive/license/security audit, реальные prices/latency/оплата из РФ и acceptance pilots остаются открытыми. Автономный код, installers, чужие tests, платные LLM/API, отправка сообщений, live account actions и изменения инфраструктуры не выполнялись.

Воспроизведение и точный следующий этап: `REPRODUCE.md`, `CONTINUATION-QUEUE.csv`, `CHECKPOINT.json`. GitHub publication публикует audit artifacts, а не полный закрытый backup/credentials/runtime state.

Свежий offline replay из raw records/notes/Manus ZIP дал побайтовое совпадение пяти основных data outputs. Повторный evidence join идемпотентен; найденное при первом replay дублирование evidence_refs исправлено до публикации. Доказательства — `EVIDENCE/REPLAY-VALIDATION.json` и `ENRICH-IDEMPOTENCE.json`. Эти PASS относятся к аудиторским данным, не к испытуемым инструментам.
