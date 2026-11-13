# B3 · Разрешённый внешний отклик, независимый readback и мониторинг
**Статус:** READY_FOR_CODEX · **Зависимости:** A1/A2/A3, B2 и отдельный live MissionGrant. **Без live grant:** разрешена только разработка и offline/staging испытания.

## Цель
Провести первую карьерную миссию через **общий E1 runtime**: актуальная вакансия → фактический адресный пакет → разрешённая первичная отправка → внешняя квитанция → независимое чтение отправленного → долговечный monitor cursor. Это не завершает E1 Full.

## Реализация
- Domain adapter `career.initial_application` поверх generic `effect.reserve/dispatch/reconcile`. Для первого запуска — только email, который работодатель явно указал для откликов в текущем первоисточнике. Browser/form или HH apply — отдельные будущие capability после правовой и технической проверки.
- Один scoped owner grant ограничивает sender/account, destination policy, max submissions, expiry, budget, attachment digests и data classes; не просить подтверждение на каждую штатную отправку, но не выходить за grant.
- Immutable outbox intent с уникальным `owner/account/canonical_vacancy/effect_class`, provider correlation, `SEND_PENDING/SENDING/OUTCOME_UNKNOWN/CONFIRMED`. Проверка expiry, employer/address, CV version **непосредственно перед side effect**.
- В adapter только initial send; запрет CC/BCC, reply chains, follow-up и самовольных получателей. Последующую переписку ведёт владелец.
- После network error или lost ACK — **reconcile через provider Sent/read API**, не повторный send. Если подтверждение невозможно, HOLD с уведомлением, без ложного «отправлено».
- Мониторинг входящих/status по cursor и dedupe; различать факт отправки, чтения отправленного, ответ работодателя, приглашение и оффер. Сигнал владельцу при приглашении; обычные статусы в журнал и отчёт.

## Тестовая лестница
1. Offline fixture: гонка двух процессов → один provider effect; exit до сети → UNKNOWN/0; exit после эффекта → readback/1; повторное событие inbox → один status.
2. Dedicated E1 PG staging: транзакционная уникальность, fenced worker, отозванный/истёкший grant, запрещённый адрес, неправильный digest, бюджет = 0, сбой сети, restart — нет незаконных эффектов.
3. **Только после отдельного live grant:** ровно одна реальная разрешённая отправка через реально подключённый аккаунт; provider ID + независимый readback Sent, запись D03/D09, post-send monitor cursor. Не вызывать fault на настоящем работодателе.
4. Если адрес/канал/авторизация/материалы не готовы, критерий live **BLOCKED**, а не синтетическое CONFIRMED.

## Выход
Provider adapter, receipts с безопасным redaction, source PR, протокол fixture и E1 PG проверки, live evidence при разрешении, мониторинг и rollback/fallback policy. QA отдельно подтверждает отсутствие duplicate sender.
[Интеграции Astra](../ASTRA-AUTONOMY-AUDIT-2026-11-08/05-career-integrations.md) · [Надёжность](../ASTRA-AUTONOMY-AUDIT-2026-11-08/06-resilience-updates.md)
