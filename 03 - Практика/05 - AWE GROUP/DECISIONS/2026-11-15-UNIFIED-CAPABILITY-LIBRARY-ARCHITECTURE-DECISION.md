# AWE GROUP / NOX — ADR: Единая библиотека возможностей (Unified Capability Library)

**Дата:** 2026-11-15  
**Статус:** OWNER ARCHITECTURAL DECISION RECORDED / DESIGN APPROVED / IMPLEMENTATION NOT ORDERED BY THIS RECORD  
**Владелец решения:** владелец AWE GROUP  
**Тип:** архитектурное решение / совместимость с действующим R2  
**Приоритет:** не прерывать текущую работу OpenCode и не расширять Definition of Done R2  
**Принцип:** EXTEND NOX / GENERALITY BEFORE WORKFLOW COUNT / REUSE BEFORE REBUILD.

## 1. Причина и намерение

Владелец хочет раскрыть потенциал Nox для неизвестных миссий, не попасть в бесконечную разработку и не повредить уже реализованное исполнительное ядро. Обсуждена единая библиотека, объединяющая поиск инструментов, интеграций, навыков, знаний и проверяющих средств.

**Решение:** строить не новую агентную платформу с нуля, а **одну логическую библиотеку обнаружения и допуска поверх действующего Nox**. Использовать существующие Head, Mission Manager, tool runtime, LibSQL, QA, grants и Capability Plane. Библиотека должна быть изолируемой, сменяемой и обратимой. **Не проводить сейчас изменения работающего кода или сессии OpenCode только из-за этого ADR.**

Это согласованное направление проектирования, **не** новая задача OpenCode, **не** разрешение на массовую установку, **не** требование реализовать маркетплейс до R3.

## 2. Решённые вопросы

1. **Каталог ≠ установленный инструмент.** Cortex содержит **4 504 уникальных record ID**, и все 4 504 на момент аудита имеют статус **UNVETTED**. Это исследовательские кандидаты разных типов, а не готовые вызываемые функции. Сохранить записи и provenance; отличать один и тот же upstream за разными записями.
2. **Импорт в доступный для поиска индекс:** допускается и желателен, когда его внедрение не конфликтует с текущим R2. Сам факт импорта всей базы **не является обязательной блокирующей предпосылкой** приёмки R2 или перехода к R3, если уже доказано общее acquisition на незнакомом инструменте.
3. **Обнаружение отдельно от запуска.** Читать metadata/index можно без установки. Установка, квалификация, доступ к секретам и invocation происходят через действующие permission/sandbox/approval границы.
4. **Без нового оркестратора.** Head определяет потребность и стратегию, Mission Manager управляет миссией; Librarian лишь возвращает ранжированные кандидаты, а не создаёт собственный scheduler/Head.
5. **Без второго authority plane.** Capability Broker — логический интерфейс/расширение уже существующего host-owned Capability Plane, а не новая независимая система grants или секретов.
6. **Reuse-first:** существующий tool registry, MCP/browser adapter, Mastra seams, LibSQL, deterministic executors/QA; при необходимости стандарты MCP, Agent Skills и OpenAPI/JSON Schema. ToolHive, Composio, AWS и другие платформы — кандидаты для сравнения **только при доказанном gap**, не обязательные зависимости и не утверждение, что они установлены.
7. **Без постоянных LLM-вызовов для поиска.** Метаданные, фильтрация, FTS, типовые проверки, hash/checkpoint/manifest, выполнение scripts/CLI — детерминированно. LLM используется для семантического уточнения, планирования и выбора при реальной необходимости.
8. **Компетенции не равны URL.** Skill, script, MCP server, external API, source of knowledge, artifact verifier, agent recipe и workflow должны различаться по kind/contract/effects/provenance; ссылки, статьи и проекты в каталоге не становятся напрямую callable capabilities.
9. **Без маскировки неопределённости.** При отсутствии цены, лицензии, срока поддержки, зрелости, безопасности или тестовых доказательств — UNKNOWN/UNVETTED, не PASS.
10. **Без новых искусственных лимитов числа подагентов.** Сохраняется ранее выданная свобода технического выбора при действующих provider/resource/spending/security пределах; новые покупки и расширение полномочий не разрешаются автоматически.

## 3. Три логические роли, минимальная реализация

### 3.1 Registry (каталог)

- Индексированные записи с полями: canonical ID, kind, name, source URL, upstream ID, version/digest (если есть), provenance, description/capabilities, declared inputs/outputs, permissions/effects, dependencies, license/rights, trust state, last checked, qualification receipt/expiry.
- Исходный 4504-каталог сохраняется неизменённым; staging/import в отдельную схему/таблицы либо отдельный файл БД, **без изменения существующих миссий, истории, checkpoints, уроков и grants**.
- Не подтягивать executable code, приватное содержимое или чужие документы при одном лишь импорте метаданных; соблюдать license/ToS/ACL.
- Дедупликация по upstream ID/URL не уничтожает оригинальные record IDs, source evidence и связи.

### 3.2 Librarian (поиск)

- Простой API: requirements/needed capability → фильтр по kind/effects/trust/permissions → FTS по metadata → ranked candidates + rationale + evidence, либо NOT_FOUND.
- Progressive disclosure: отдавать Head короткие top-k карточки, не тысячи tool schemas целиком. LLM необязателен для обычного lookup.
- Без прямого выполнения и без права выдавать новые grants, секреты или устанавливать пакеты.

### 3.3 Capability Broker (допуск)

- **Не отдельный новый runtime**: это функциональность существующего Capability Plane и текущих runners.
- Жизненный цикл: DISCOVERED / UNVETTED → INSPECTED → QUALIFIED → APPROVED FOR SCOPE → ACTIVE → REVOKED/QUARANTINED.
- Проверять источник, версии/digest, схемы, declared effects, лицензии, зависимости, тестируемость, resource/egress/FS/secrets grants, независимые proof и cleanup.
- Scope/approval **per mission** либо уже существующая безопасная host-policy; нет автоматической эскалации полномочий, blanket-install или подключения внешних аккаунтов.
- Изменение digest/schema/rights или выявленный риск инвалидирует qualification и требует повторной проверки.

## 4. Технические границы

- **Не заменять:** Prompt Master, Head, Mission Manager, LibSQL persistence, QA, sandbox, model routing, existing tool registry.
- **Не дублировать:** новый scheduler, второй agent framework, второй memory platform, второй broker permissions, собственный нестандартный протокол MCP.
- **Не обещать:** поддержку всех 4504, автоматическое освоение всех профессий, «универсальность» по числу records/skills, validated Security или 24/7.
- **Модели:** сохраняя host-owned routing, можно позже сравнить LLM vs deterministic lookup; adaptive policy не является частью первого каталожного slice.
- **Память:** библиотека ресурсов и долговременные lessons — связанные, но раздельные объекты. Provenance/ACL/validity для knowledge; memory transfer проверяется отдельным fresh-agent против memory-off экспериментом.
- **Внешние сервисы:** API/MCP могут требовать credential broker, изоляцию, user approvals, operation keys/reconciliation; catalog lookup сам по себе не выдаёт доступа.
- **Изоляция:** отдельная ветка/модуль + schema/migration tests + rollback plan + независимые acceptance checks; отсутствие regression по текущим R2 задачам.
- **Observability:** фиксировать candidate IDs, выбор, отказ, квалификацию, grant, invocation, проверку результата, usage/cost UNKNOWN когда нет данных.

## 5. Финитные контрольные точки (не новая обязательная серия релизов)

**A / Registry:** исходные 4504 ID читаются и ищутся без потери, корректно различены дубликаты/типы/UNVETTED, поиск не требует LLM. Это полезная, но *не обязательно блокирующая R2* опция.

**B / Librarian → Head:** Head вызывает поиск через небольшой контракт; Библиотекарь не выполняет код, grants не расширяются, существующий Capability Plane остаётся владельцем допуска. Возможность обратима; нет регрессий.

**C / Один доказанный acquisition:** на неизвестной задаче Nox обнаруживает нехватку возможности, ищет кандидата, квалифицирует, использует с выданными правами, выпускает реальный artifact, получает независимый QA, не меняет core source под тест. Если R2 уже делает это без отдельного Librarian/4504-индекса, **не заставлять повторно строить инфраструктуру ради формы**.

**Stop rule:** как только минимальное расширение доказало реальную добавочную ценность в общем acquisition loop, прекратить развитие именно библиотечной платформы. Не требовать интеграции всех записей, маркетплейса, 100 подключений, новых фреймворков или дополнительного месячного исследовательского этапа. Новые потребности рассматриваются только по измеренному mission gap.

**Важно:** эти A/B/C — узкие *критерии проверки библиотеки*, они **не заменяют** шесть критериев финальной приёмки R2; один успешный тест не доказывает все шесть.

## 6. Сверка на конфликты с действующей архитектурой

| Потенциальное противоречие | Разрешение / статус |
|---|---|
| «Строить с нуля» vs EXTEND NOX | **Исправлено:** концепция библиотеки с нуля, реализация — расширение existing Nox |
| «Импортировать всё прежде R3» vs Stop after six R2 acceptance | **Исправлено:** импорт каталога — неблокирующее усиление, не новый релизный gate |
| «Новый Capability Broker» vs существующий Capability Plane | **Исправлено:** одна и та же плоскость допуска, никакого второго механизма полномочий |
| Librarian vs Head/Mission Manager | **Исправлено:** библиотекарь индексирует/ищет, но не планирует миссии и не оркестрирует |
| «Подключить 4504» vs UNVETTED и security | **Исправлено:** metadata-only registry, runtime acquisition поштучно |
| Массовый install vs owner approval/grants | **Запрещено:** sandboxed testing с минимальными grants; покупки/секреты/внешние действия отдельно |
| Отдельная память vs существующая LibSQL | **Исправлено:** возможен reuse существующего хранилища в отдельной схеме; не переписывать историю |
| «Три контрольные точки» vs уже идущая OpenCode R2 | **Исправлено:** не перезапускать/не перенаправлять текущую работу; A/B/C не тормозят её |
| «Одна миссия доказывает готовность» vs six acceptance criteria | **Исправлено:** тест C — только библиотечный slice, шесть критериев остаются |
| Unlimited agents vs provider/spending limits | **Без конфликта:** нет искусственного ceiling, реальные и safety-бюджеты сохраняются |

**Результат проверки:** в уточнённом виде концепция архитектурно совместима с документами Owner Approval 2026-11-14, Master Handoff, R2 independent audit и Universality Strategy. Это **document-level consistency review**, не доказательство отсутствия скрытых конфликтов с текущим незакоммиченным WSL code. Перед implementation нужна лёгкая code-level compatibility check на актуальной контрольной точке.

## 7. Действующее решение и действия

**Сейчас:**
- ADR зафиксирован отдельно от кода.
- Не отправлять новые инструкции в OpenCode, не запускать вторую разработку и не внедрять библиотеку параллельно незавершённому R2.
- Продолжать основной R2 до принятия или чётко подтверждённого блокера; если для general acquisition непосредственно требуется Librarian — реализовать минимальный поисковый slice по настоящему measured gap, не полный marketplace.
- При успешной независимой проверке шести критериев R2: прекратить рост core, перейти к UI/shell и owner handover (R3); каталог можно затем подключать как неблокирующее улучшение при необходимости.

**Не утверждается:** R2 завершён, библиотека реализована, 4504 инструмента подключены, OpenCode уведомлён, код опубликован из WSL.

## 8. Ссылки на первичные доказательства

- Owner approval: `03 - Практика/05 - AWE GROUP/HANDOFF/2026-11-14-OWNER-TRANSITION/OWNER-APPROVAL-EXACT.md`
- Master Handoff: `03 - Практика/05 - AWE GROUP/HANDOFF/2026-11-14-OWNER-TRANSITION/AWE-NOX-MASTER-HANDOFF.md`
- Independent audit: `03 - Практика/05 - AWE GROUP/RESEARCH/NOX-R2-INDEPENDENT-AUDIT-2026-11-14/`
- Universality strategy: `03 - Практика/05 - AWE GROUP/RESEARCH/NOX-UNIVERSALITY-STRATEGY-2026-11-14/UNIVERSALITY-STRATEGY.md`
- Cortex audit: `03 - Практика/05 - AWE GROUP/02 - Аудит 4504 инструментов.md`
- Cortex inventory: `04 - Инструменты/Каталог кандидатов/90 - Данные/catalog-all-4504.csv`
- OpenCode journal (read-only): `failm3/awe-opencode-recordings/LATEST.md`
- Observer (read-only): `failm3/awe-group-observer/LATEST.md`

---
*This record is a scoped owner architectural decision, not an engineering execution request or complete conversation transcript.*
