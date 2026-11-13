# NOX R0 — после финального независимого QA: ремонтные работы

**Срез:** 2026-11-13 04:31 UTC / 07:31 МСК.
**Статус:** R0 **IN REMEDIATION / NO OWNER GO**, тестовая и инженерная работа значительна, но независимый QA версии до исправлений = **FAIL — DO NOT CLOSE R0 OFFLINE**.

## Проверенные результаты предыдущего интегрированного дерева
В independent QA `reports/r0-final-independent-qa.md` документированы: `npm test` 12/12 PASS на записанном snapshot, independent contracts 34/34, manager 76/76, storage+lease 53/53, recursion 37/37, security 5/5, typecheck и build PASS. Проверяющий повторно провёл typecheck и проверил final-source/evidence.sha256 manifests. Полную suite повторно независимым QA **не запускал**. Не доказываются real browser/MCP/network/LLM, PG, deployment и production readiness.

Отрицательный QA отметил high-priority holes: stale owner file write (D1), MCP stale fence (D2), необязательный hash/size артефактов (D3), isolated root violation в targeted repair (D4), web_search post-cancel fallback (D5), MCP post-abort effect (D6), dropped delegated abort signal (D7), effect-to-checkpoint crash gap (D8), child.tools=[] inherits parent grants (D9), превышение total agent limit across top level/resume.

[Источник полного независимого QA, read tool output](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/04-24/part0000.txt).

## Что новое проверено после QA
- 04:26 UTC OpenCode изменил инженерный отчёт с `PENDING INDEPENDENT FINAL QA` на `FAIL — INDEPENDENT QA FINDINGS UNDER REMEDIATION`.
- 04:26 созданы три копии `.r0-work/r0-final-tools`, `r0-final-manager`, `r0-final-recursion`, изолированные от главной рабочей копии.
- 04:27 отправлены три задачи отдельным LLM-субагентам: tool boundary fixes (GPT-6.1 Sol high), integrity/recovery (Claude Sonnet 5.5 high), recursion/grants/budget (GPT-6 Astra high). Это **инженерное исполнение R0, не запуск нового R1**.
- 04:29 в ветке recursion изменены `src/agents/recursion.ts` и `src/agents/specialists.ts` с соответствующим patch success, интеграция в основной runtime и тесты не подтверждены.
- 04:31 в ветке tools изменены `src/utils/storage.ts` и `src/run-targeted-repair.ts` для адресации mission artifacts, интеграция и независимый PASS не подтверждены.
- Observer 04:30 UTC показывает OpenCode PROCESS_PRESENT, но этот факт сам по себе не является acceptance.

[04:26](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/04-26/part0000.txt) · [04:27](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/04-27/part0000.txt) · [04:29](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/04-29/part0000.txt) · [04:31](https://github.com/failm3/awe-opencode-recordings/blob/main/timeline/2026-11-13/04-31/part0000.txt).

## Прогресс и граница с R1
R0 — далеко продвинутый **offline-tested engineering runtime**, но не принятая production-система. Большинство базовых механизмов кода реализованы; P0 end-to-end гарантии безопасности, целостности и crash recovery требуют ещё исправлений и независимой проверки. Степень полноты нельзя честно выразить процентом: количество строк/зеленых test doubles ≠ доля доказанной безопасной автономности.

Cortex широкое исследование по Tool Intelligence, обучению, знаниям, профессиональным packs готово для параллельной исследовательской работы, **R1 интеграции не разрешены и не запущены**. Новый инженерный пакет следует готовить на базе final accepted R0 SHA.
