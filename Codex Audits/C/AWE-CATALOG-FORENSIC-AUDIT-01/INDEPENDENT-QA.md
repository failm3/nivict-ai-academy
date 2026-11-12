# Независимый QA

**PARTIAL.** Выполнен отдельным агентом того же семейства GPT. Другой model family NOT_SATISFIED, полноценный blind examiner NOT_RUN. Пересчёты независимы по реализации; агент видел родительский контекст, поэтому blind-экзамен не заявляется.

Собственные QA scripts не импортируют основной inventory.py. Полный raw/JSON/CSV/Obsidian пересчёт дал 4 504/4 504, content mismatches=0; 72 category files и их полная link карта проверены отдельно. Исторические hashes классифицированы EXPLAINED_HISTORICAL_BYTE_MISMATCH (LF/CRLF), content_failure=false. Пересчитаны 38 legacy duplicate groups, 33 collision groups и 4 090 issues. Есть шесть negative URL cases, parser/HTML escaping reconciliation и 59 strata samples.

Независимо пересчитаны Manus 3 415 и overlap 3 309→3 270, без match 1 195/145. Четыре целевых primary README spotchecks подтвердили три category ошибки; процент ошибки корпуса из них не выводится. Проверены 19 высокорисковых shortlist кандидатов, 12/12 keyword flags (5 risk-review, 4 false positives, 3 unknown), 9 расширяющих архивных решений. Сохранены high-risk caveats и дополнительные licensing primary refs. Предложения root уточнены по замечаниям о runtime boundaries, mixed licensing, auth defaults, ephemeral logs, ungrounded spans и прекращённой поддержке Continue.

Manus v2 code slice: девять файлов прочитаны как текст, hash сравнен с ZIP. Проверены различия imported claims/observations/attestations/approval/export. LIVE_TESTED не независимый test runner; fingerprint не связывает автоматически deployed binary/config; provenance hash не доказывает аутентичность; licensing metadata не заменяет текст. Это не полный security audit.

Материалы: QA/INDEPENDENT-LOCAL-QA.md, INDEPENDENT-COUNTS.json, MANUS-INDEPENDENT-COUNTS.json, STRATIFIED-SAMPLE.json, NEGATIVE-CASES.json, PRIMARY-SOURCE-SPOTCHECKS.json, HIGH-RISK-REVIEW.md, FLAGGED-SOURCE-REVIEW.md, ARCHIVE-EXTENSION-REVIEW.md, MANUS-V2-CODE-REVIEW.md и соответствующие machine evidence.

Перед GitHub publication выполняется отдельный redacted pattern scan публичного дерева. Он ищет известные token/private-key/contact/userinfo/query signatures и не выводит значения; не гарантирует отсутствие всех PII/secrets. Полные private backup, исходный Manus provenance-rich index и source caches не публикуются. GitHub readback записывается отдельным receipt после push/PR.

Открытые QA gates: cross-family blind examination; исходный current12 snapshot; все remaining primary content/license/semantic claims; реальные acceptance tests. Ни один PASS data assertion не является APPROVED/INTEGRATED или production readiness.
