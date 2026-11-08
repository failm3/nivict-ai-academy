# SANDBOX-RECRUIT-01 · результат испытаний · 08.11.2026

**BOUNDED_SYNTHETIC_MISSION_PASS / CLOUD_PROVIDER_BLOCKED / E1_PILOT_NOT_ACCEPTED.** Astra действительно передала исходную синтетическую миссию в AWE E1. На четвёртом recruiting-прогоне независимый QA подтвердил pipeline, восстановление и применение написанного AWE кода. Реальная карьерная миссия, отклики и E1 Pilot этим не приняты.

[Приватный runtime](https://github.com/failm3/awe-group-runtime) · [ветка](https://github.com/failm3/awe-group-runtime/tree/codex/e1-sandbox-recruit-01-20261108) · [PR](https://github.com/failm3/awe-group-runtime/pull/7) · commit [9c3eaa182a862dadd5a326836408063b45f7219c](https://github.com/failm3/awe-group-runtime/commit/9c3eaa182a862dadd5a326836408063b45f7219c). Base — 3c22522c52cb6428757fd391e8630c912016b61b. [Manifest](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/release/SANDBOX-RECRUIT-SOURCE.json) · [Независимая проверка экспорта](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/qa4/INDEX-REVIEW.json). Main не изменён.

## Что исполнила AWE

1. Обычные A1 spec/grant/plan прошли native admission A2 на изолированном PostgreSQL E1 5433. Два worker прочитали 30 вымышленных записей из двух локальных HTTP-источников; один источник действительно ответил 429 перед 200.
2. Pipeline обработал дубли, изменённую ревизию, устаревшие/закрытые записи, неверную схему и prompt injection. Подготовил пять ранжированных позиций с evidence и пять черновиков исключительно на вымышленных фактах. Отправок — 0.
3. Worker ranking был принудительно остановлен на незавершённой задаче. Новый OS-процесс продолжил ту же миссию через A2 recovery с новым fence. Независимый процесс прочитал итоговые пять ACCEPTED задач и проверил digests в БД.
4. В отдельной bounded capability реальная локальная Qwen написала score_helper.py. Exact source прошёл реальное исполнение в непривилегированном bwrap, отдельный QA на 19 скрытых входах и native QA acceptance. Следующая миссия использовала именно этот код для 29 оценок; подстановки оценок разработчиком не было.

Функция [score_helper.py](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/recruit/generated/score_helper.py) имеет SHA-256 59437dbb6107295bbfb10264691743e9fcd98dba031d183da75bbc050ad80cfa. Она перенесена в экспорт байт-в-байт. [Авторство/usage](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/recruit/coding/evidence/score01_4101.json) · [Финальный независимый cold audit](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/qa4/COLD-cycle04_4101.json).

## Команда и итерации

| Исполнитель | Фактическая работа |
|---|---|
| Astra, gpt-6-astra | Supervisor: замороженный исходный oracle, настоящие submit/run, задания на исправления, повтор той же миссии и независимое чтение результатов QA. |
| Sol | Developer/host operator: DAG, capabilities, HTTP fixtures, native bindings, безопасный code runner и интеграционные исправления. |
| cloud_d09 | Подписанный технический расходный мандат, native фазы canary/followup, SAME-key scope CAS и исправление lock order. |
| cloud_qa | Отдельные oracle/holdout, credentialed QA leaves и cold DB readers, отрицательные контроли, финансовые гонки и проверка публикации. |

Baseline остановился на contract-only preflight; это зафиксировано как дефект, а не автономность. Первые три настоящих recruiting-прогона дали pipeline PASS / recovery PROVEN, но overall PARTIAL из-за отсутствия coding capability. После её реализации score01 произвёл код, cycle04 на скрытом варианте получил PASS. Прежние PARTIAL evidence не переписаны. [Astra checkpoint](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/astra4/CHECKPOINT.md) · [Полный outcome](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/SANDBOX-RECRUIT-REPORT.md).

Исправлены реальные ошибки: возрождение старой вакансии при неверной новой ревизии; подмена локального apply ID; AST обход через переименование eval/exec; пропущенная проверка отзыва host principal/мандата; невозможность безопасно расширить prepared scope; риск deadlock при конфликте scope amendment с reserve. Исправления проверены отдельным QA, исходный oracle сохранён. 0004–0006 аддитивно применены только в E1; 0001–0003, Ollama и E0 не менялись.

## Проверки и расходы

Всего **пять настоящих локальных AWE вызовов**, 1 899 input / 191 output tokens, qwen3:4b-instruct, каждый с одним wire и native CONFIRMED. API cost и резерв — 0. Платных Router генераций и реальных откликов — 0. Расход Codex orchestration/электричества не измерен; число кредитов владельца не выдаётся за фактический доступный баланс.

Независимые проверки: 17 oracle, 3 прямых SUT negatives, 13 реальных sandbox/holdout случаев, финансовые revocation negatives, **11 native финансовых сценариев и повтор тех же 11 отдельным QA**. Это пересекающиеся проверки, не сумма уникального покрытия. Прежняя регрессия на финальных исходниках: **442/442 offline + 38/38 native**, 0 fail/skip. Первый запуск в ограниченном sandbox встретил запрет temporary Git config/symlink; после разрешённого fixture execution прошли targeted 14 и полная регрессия, без ослабления тестов.

## Router.Cheap: разрешение выдано, технический gate остаётся

Единый мандат [Issue 3](https://github.com/failm3/awe-group-runtime/issues/3) / [Issue 4](https://github.com/failm3/awe-group-runtime/issues/4) принят как действующий. Фактически выпущен Ed25519 host-attested receipt через native authority: $10 actual суммарно, canary две попытки по $0.25/$0.50, далее до $9.50, $1/запрос и 20 попыток только после независимого успеха canary. Подписанный scope расширен на том же ключе до шести проектов, история и counters сохранены. Это staging host delegation, не доказательство production human AuthN. [Финансовая проверка](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/cloud4/evidence/FINANCIAL-REVIEW.json).

Реальный funding остаётся DISABLED/0. Доверенный GET в 04:33 UTC подтвердил 75 моделей, номинальный key limit $10 и usage 0 cents. Документированный контракт пока не доказывает hard cap фактических списаний после source/balance коэффициентов и достаточный charged ACK. Платная отправка отключена; **блокер не в повторном согласовании владельца**. Средства не пополнялись, настройки аккаунта/ключа не менялись. [Readback](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/recruit/evidence/ROUTER-READONLY.json) · [Финансовый outcome](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/cloud4/REPORT.md).

## Что осталось и как продолжить

Узкий synthetic mission PASS не доказывает динамическое создание специалистов/executors, generic GitHub coding Issue 2, перезапуск supervisor без оператора или live Career/production. Возможность score-author установил Sol; AWE создала и применила один разрешённый кодовый артефакт. [Checkpoint для продолжения](https://github.com/failm3/awe-group-runtime/blob/9c3eaa182a862dadd5a326836408063b45f7219c/E1/RESUME-SANDBOX-RECRUIT.md) сохраняет предел 12 циклов/6 local wires, использовано 5, stop 2026-11-08T05:33:52.393Z; private host конфигурация в Git не включена. После завершения сессии фоновая работа не обещается.

Следующие независимые потоки: доказуемый provider actual-charge contract/ограниченная альтернатива; развитие узкой coding capability до отдельно проверяемого GitHub executor; независимые recovery/adversarial проверки. Реальные внешние действия запрещены. [Очищенная машиночитаемая сводка](E1-EVIDENCE-SANDBOX-RECRUIT-2026-11-08.json).
