# Провайдеры и локальные gateways

**PARTIAL, 12.11.2026.** Только публичные источники; авторизованные тарифные панели, счета, региональная доступность и оплата из РФ не проверены. Платных inference/API calls — 0.

| Решение | Что проверено | Цена/лимиты, наблюдённые публично | Что остаётся UNKNOWN |
|---|---|---|---|
| Router.cheap | [Главная страница](https://router.cheap/) доступна web reader, но не содержит читаемого тарифного текста | Exact account/model/input/output/cache/reasoning/tools prices UNKNOWN | Авторизованная панель, реальные расходы/баланс, способы оплаты/РФ, uptime, privacy terms и limits |
| OpenRouter | [Официальный pricing](https://openrouter.ai/pricing), проверено 12.11.2026 | Страница указывает Standard fee 5.5%, Business 8% при покупке credits; list-price inference. BYOK: $25k list-price inference/month без OpenRouter fee, затем 5%. Методы: карты, AliPay, USDC; это не доказательство доступности из РФ | Конкретный аккаунт, налоги, доступность модели/региона/платежа, privacy каждого upstream, реальные p95/error/cost |
| Requesty | [Официальный pricing](https://www.requesty.ai/pricing), проверено 12.11.2026 | Публично 5% markup к расходу модели, free tier 200 requests/day на free models; routing/cache/fallback advertised included | Платёжные способы/РФ, exact per-model price, enterprise conditions, account eligibility и real p95/error |
| LiteLLM | Pinned README/root и enterprise license, R08 | OSS gateway/SDK; inference оплачивается upstream, EE features отдельно | Hard budget enforcement в AWE и точность usage/prices, privacy/log configuration |
| OmniRoute | Pinned source R09; старый URL переехал в cheaper-inference/OmniRoute | MIT gateway; free/savings headlines не равны бесплатному гарантированному inference | Actual provider eligibility, OAuth/subscription permission, retry costs, compression quality, price freshness |
| Direct API/BYOK | Архитектурный вариант; per-provider pricing здесь не исследован | Счёт upstream отдельно от gateway/инфраструктуры | Ключи/оплата/регион/retention/caching и поддержка features каждой модели |

Локальный proxy не продаёт и не оплачивает токены. Не складывать gateway savings claims и тарифные скидки без контроля качества/счетов. Authenticated Router.cheap panel не открывалась, ключи/настройки/бюджеты не читались и не менялись.

Минимальная будущая FinOps-проверка: один allowlisted provider, immutable model ID/capabilities, input/output/cache/reasoning/tool usage, total-attempt budget reservation, bounded timeout/fallback и no-repeat-after-effect. Сначала mock upstream; затем отдельный разрешённый ceiling для real calls. Измерять full mission cost, success and latency, а не только цену 1M input tokens. Способы оплаты и пригодность из РФ остаются UNKNOWN до прямого подтверждения.
