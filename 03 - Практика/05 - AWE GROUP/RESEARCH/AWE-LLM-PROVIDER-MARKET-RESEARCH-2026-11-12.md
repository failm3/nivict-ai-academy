# AWE GROUP: исследование рынка LLM-провайдеров

**Рекомендация: подключить OpenRouter как основной резервный шлюз, а для действительно независимого аварийного контура добавить прямой API Anthropic и/или OpenAI.** Router.Cheap имеет смысл сохранить для некритичных задач с фиксированными скидочными маршрутами и малым балансом: его каталожные цены очень низки, но происхождение upstream, фактическая модель и поведение конкретного маршрута не аттестованы. Requesty подходит как второй резерв, особенно при необходимости EU-маршрута. Ни один другой агрегатор сам по себе не доказывает независимость от Router.Cheap на уровне вычислительных мощностей.

**Дата основного исследования:** 12 ноября 2026 года. Публичный JSON Router.Cheap дополнительно перепроверен 13 ноября 2026 года. Все цены ниже — USD за 1 млн токенов, если не указано иное. Не выполнялись регистрации, покупки, создание ключей, платные вызовы моделей и изменения AWE/OpenCode.

## Метод и границы доказательности

- Проверены публичные документация, условия, status pages и машиночитаемые каталоги; выполнены анонимные GET-запросы.
- **«Есть в каталоге»** означает наличие точного ID и опубликованной цены, а не успешный inference.
- **«Независимый резерв»** требует разных gateway, control plane, биллинга и upstream. Разные домены и юрлица этого не доказывают.
- Uptime приведён только там, где найдена публичная метрика; это преимущественно телеметрия самого оператора, а не независимый audit.
- Кабинеты, checkout, фактические списания, качество ответов, tool loops и streaming под нагрузкой не испытаны. Поэтому рейтинг является оценкой desk research, а не production-сертификацией.
- В перерасчётах не учитываются налоги, платный поиск, обработка файлов, сетевые сборы, повторные запросы и курс валют.

---

## 1. Краткое заключение

### Прямой ответ на главный вопрос

**Выгоднее всего подключить OpenRouter в дополнение к Router.Cheap.** Причины: 473 записи в публичном каталоге, все четыре специально запрошенные модели, публичные цены по конкретным endpoints, явный выбор поставщика, ограничение цены, нативная поддержка OpenCode, несколько ключей с лимитами и детальный usage/cost-учёт. Плата за это — комиссия пополнения Standard 5,5%, минимум $0,80, и неодинаковые возможности разных endpoints.

Но OpenRouter — **резерв шлюза, а не доказанный независимый disaster recovery**. Для отказа всего класса агрегаторов нужен прямой API производителя. Практическая цепочка:

1. Router.Cheap с фиксированным `model + routing_source` для некритичной разработки.
2. OpenRouter с полным model ID, `provider.only`, `require_parameters:true`, `allow_fallbacks:false`.
3. Прямой Anthropic/OpenAI для критичных задач и аварийного продолжения.

### Выводы по категориям

| Категория | Выбор | Оговорка |
|---|---|---|
| Лучший резервный провайдер | **OpenRouter** | После ограниченного пилота; пиннинг endpoint обязателен |
| Лучший по надёжности среди шлюзов | **OpenRouter** | 99,99% Chat Gateway за 90 дней по собственному status; не end-to-end SLA модели |
| Действительно независимый контур | **Прямой Anthropic/OpenAI** | Дороже скидочных маршрутов, зато устраняет посреднический gateway |
| Лучший универсальный | **OpenRouter** | Модели, OpenCode, provider controls, ключи и учёт |
| Второй резерв | **Requesty** | +5%; EU-резидентность заявлена, параллелизм зависит от баланса |
| Номинально самый дешёвый | **Router.Cheap discount routes** | Низкая цена не доказывает эквивалентность модели и стабильность |
| Потенциальная замена Router.Cheap | **OpenRouter, только после пилота** | Сейчас оснований для немедленной полной миграции нет |

**Главный экономический вывод:** выбор модели и маршрута влияет на расходы сильнее, чем выбор между list-price агрегаторами. У OpenRouter и Requesty наценка обычно 5–5,5%; разница между дешёвой и флагманской моделью может достигать десятков раз.

---

## 2. Общая таблица исследованных провайдеров

| Провайдер | Проверенный каталог | Ключевые цены / комиссии | Модели и API | Надёжность и прозрачность | Роль для AWE |
|---|---|---|---|---|---|
| [Router.Cheap](https://router.cheap/) | 75 моделей, 36 routing sources | Default близок к прайсу; отдельные маршруты −82…−96%; условия покупки кредитов непрозрачны | Нужные семейства есть; OpenAI/Anthropic/Gemini formats | Юрлицо, SLA и публичная история не установлены; upstream раскрыт названиями, не договорами | Условный основной для некритичного coding |
| [omnirouter.li](https://omnirouter.li/) | 90 записей, 63 chat | Opus 5.5 $0,70/$3,20; prepaid; минимум и комиссия не подтверждены | OpenAI/Anthropic compatibility; нет части новых ID | Оператор указан как Natsu, Morocco; `/status` 404; upstream скрыт | Только несекретный эксперимент |
| [OmniRouters](https://www.omnirouters.com/) | 96 записей | Default близок к прайсу; Economy ×0,15; минимум $10 | Нужные ID; Chat/Anthropic/Responses/Gemini зависят от модели | HK Zhijie Ltd указано; SLA 99% только gateway; допускается смена модели при fallback | Условный резерв после тестов |
| [OpenRouter](https://openrouter.ai/) | 473 записи | Opus $4/$20; пополнение +5,5%, минимум комиссии $0,80; покупка от $5 | Все ключевые модели; OpenAI/Responses/Messages; native OpenCode | OpenRouter, Inc.; provider pinning; status 99,99%/90 дней у gateway | **Первый резерв** |
| [Requesty](https://requesty.ai/) | 750 + 176 managed policies | PAYG +5%; минимум и срок баланса не подтверждены | Полные provider-prefixed ID; OpenAI/Anthropic/Responses; OpenCode | Better Stack 100%/30 дней синтетики шлюза; юрисдикция описана противоречиво | Второй резерв, EU-вариант |
| [AIHubMix](https://aihubmix.com/) | 849 записей | Большинство флагманов 0%; Fable +10%; минимум $15 | Нужные ID; OpenAI/Anthropic/Gemini; официальный OpenCode provider | 99,96% Chat, 99,25% Claude/90 дней; Terms URL 404; есть крупные инциденты | Точечный резерв |
| [Nano-GPT](https://nano-gpt.com/) | 618 записей в `/api/v1/models` | Opus/Astra/Sol list price; Fable +25%; депозит от $0,10 crypto/$1 card | Нужные ID; OpenAI/Anthropic/Responses; OpenCode guide | NanoGPT LLC; provider флагманов скрыт; status измеряет сайт, не inference | Резерв дешёвых моделей, не первый для флагманов |
| [AI/ML API](https://aimlapi.com/) | Около 995 записей | Machine-readable цены не получены; минимум и комиссии не подтверждены | Широкий каталог; OpenAI-compatible quickstart | Нет подтверждённых SLA/status, юрлица и model-source matrix | Третий эшелон, не критический путь |
| [ZenMux](https://zenmux.ai/) | 216 записей | Курс кредитов и итоговые цены не подтверждены | Каталог есть; интеграционные параметры не проверены достаточно | Нет подтверждённого SLA и полного аудита | Не включать в ближайший shortlist |
| [Vercel AI Gateway](https://vercel.com/docs/ai-gateway) | В разведке: 508 записи | Заявлены 0% markup и $5/месяц; не перепроверено | Потенциально подходит, но полный профиль не завершён | Провайдерский агент завершился ошибкой | Не оценён; требуется отдельный аудит |

CometAPI не включён в финальный shortlist: найденные материалы не дали достаточной проверяемой экономики и независимости, а добавление ещё одного непрозрачного шлюза не улучшает отказоустойчивость.

---

## 3. Router.Cheap как базовый вариант

### 3.1 Что подтверждено

Публичный [`/api/pricing`](https://router.cheap/api/pricing) содержит 75 моделей и 36 источников маршрутизации, базовые billing expressions и `routing_sources[].model_discounts[].price_ratio`. Повторная проверка 13 ноября подтвердила коэффициенты для трёх маршрутов, использованных в расчётах: Claude Kiro 0,036 для Opus 5.5, GPT Team/Plus 0,02 для Sol и GLM Standard 0,025 для GLM-5.3.

Это **подтверждение публичной тарифной конфигурации**, не фактического денежного списания и не происхождения модели. Персональный коэффициент покупки кредитов, комиссия продавца и доступность источника конкретному аккаунту анонимно не проверяются.

### 3.2 Цены выбранных маршрутов

| Точный ID | Маршрут; коэффициент | Default I/O/R | Расчётный I/O/R |
|---|---|---:|---:|
| `claude-opus-5-5` | Claude Kiro; 0,036 | 4 / 20 / 0,20 | **0,144 / 0,720 / 0,0072** |
| `claude-fable-5-2` | Claude Max; 25/112 | 8 / 40 / 0,20 | **1,785714 / 8,928571 / 0,044643** |
| `gpt-6-astra` | GPT Team/Plus; 0,02 | 10 / 50 / 1 | **0,20 / 1 / 0,02** |
| `gpt-6.1-sol` | GPT Team/Plus; 0,02 | 2 / 10 / 0,10 | **0,04 / 0,20 / 0,002** |
| `deepseek-v4-pro` | DeepSeek Standard; 0,05 | 0,66 / 1,98 / 0,022 вне пика | **0,033 / 0,099 / 0,0011** |
| `kimi-k3.1-pro` | Kimi Pool; 0,16 | 2 / 10 / 0,20 | **0,32 / 1,60 / 0,032** |
| `glm-5.3` | GLM Standard; 0,025 | 1,40 / 4,40 / 0,26 | **0,035 / 0,110 / 0,0065** |

Для Astra/Sol применены ставки запросов до 272K input; выше действуют более дорогие ветви. DeepSeek дорожает в пиковые часы. Цены являются USD-эквивалентом каталога до персональной конвертации кредитов.

### 3.3 Upstream и известный риск Claude/Kiro

Каталог называет источники Kiro, Kiro Enterprise, Claude Max, GPT Team/Plus и другие пулы. Это не договоры с Anthropic/OpenAI и не аттестация endpoint. Для `claude-fable-5` отдельные Kiro-маршруты публикуют `served_by_model: claude-opus-5`; это документированное переименование конкретного ID. Оно **не доказывает подмену Fable 5.2**, но показывает, почему AWE должна фиксировать requested и served model.

Сообщённый заказчиком сбой Claude через Kiro Enterprise учтён как пользовательский инцидент; его массовость и причина публично не подтверждены. Для критичных задач нельзя использовать `auto`, Model Mapping или cross-family fallback без аудита.

### 3.4 API, OpenCode и эксплуатация

- OpenAI base URL: `https://router.cheap/v1`; Anthropic-compatible base URL: `https://router.cheap`.
- Задокументированы Chat Completions, Responses, Anthropic Messages, Gemini API и SSE.
- Для Node.js/TypeScript подходят OpenAI/Anthropic SDK со сменой base URL; есть [руководство OpenCode](https://router.cheap/integrations/opencode).
- Несколько ключей, spending limit, expiry, IP/model allowlists и usage logs заявлены. Их атомарность при конкурентных запросах не испытана.
- Нет проверенной матрицы `model × source × tools × strict JSON Schema × reasoning × cache`. Передача параметра шлюзом не доказывает его поддержку upstream.
- Batch отсутствует. Фактические cache hit, TTL и сохранение reasoning между tool calls не проверены.

### 3.5 Биллинг, надёжность и данные

По [Terms](https://router.cheap/terms), доступ и возвраты связаны с маркетплейсами/продавцами; единый минимум, комиссия, способы оплаты и срок всего баланса публично не установлены. Ошибочные запросы описаны как неоплачиваемые при надёжно обнаруженной неуспешности; отказ модели и уже отданная часть stream могут оплачиваться.

`direct.router-cheap.com` использует тот же сервис и ключи, поэтому не является независимым резервом. Публичный uptime и история инцидентов не подтверждены. [Privacy](https://router.cheap/privacy) допускает временное хранение prompt/response и передачу routing partners; точный список обработчиков и TTL не раскрыты.

**Usability публичной части: 6/10.** Сильные стороны — каталог и API docs; слабые — сложная экономика, непрозрачный статус, маркетплейсный доступ и отсутствие подтверждённого юрлица/SLA. Кабинет не проверялся.

**Решение:** сохранить как экономичный канал для некритичных задач с малым остатком и фиксированным источником. Не использовать как единственную production-опору или канал для чувствительных данных.

---

## 4. OmniRouter, OmniRouters и OpenRouter — три разных продукта

| Параметр | omnirouter.li | OmniRouters.com | OpenRouter |
|---|---|---|---|
| Оператор по документам | Natsu, Morocco; полное юрлицо не установлено | HONG KONG ZHIJIE INTELLIGENT TECHNOLOGY LIMITED; самоидентификация | OpenRouter, Inc. |
| Каталог | 90 записей | 96 записей | 473 записи |
| Opus 5.5 I/O | **0,70 / 3,20** | Default **4 / 20**; Economy **0,60 / 3,00** | Native Anthropic **4 / 20** + комиссия пополнения |
| Astra I/O | **1 / 2,50** | Default **10 / 50**; Economy **1,50 / 7,50** | Standard **10 / 50**; Flex дешевле, Fast дороже |
| Fable 5.2 | `claude-fable-5-2`, 1,60/6,80 | `claude-fable-5-2`, 8/40; Economy не разрешён | `anthropic/claude-fable-5.2`, 8/40 |
| Выбор upstream | Не подтверждён | `available_vendors` есть, принудительный pinning не документирован | `only`, `order`, `ignore`, `allow_fallbacks`, `require_parameters`, `max_price` |
| Status | `/status` 404 | Цель 99% только для gateway; история не подтверждена | 99,99% Chat Gateway/90 дней по собственному status |
| Главный риск | Непрозрачный upstream и неполная идентификация | SLA разрешает смену модели при fallback; Privacy противоречит FAQ | Разные endpoint capabilities/quantization и общий upstream с другими шлюзами |
| Предварительная usability | 6/10 | 6/10 | **8/10** |

### Независимость брендов

Юридической или технической связи трёх сервисов друг с другом не найдено. Их нельзя объединять по названию. Но отсутствие доказанной связи брендов **не означает независимость upstream**: все могут вызывать одних производителей или одних посредников. Ни один не предоставил достаточного закреплённого списка субпроцессоров, чтобы доказать обратное.

### Практический выбор

- **OpenRouter** — единственный из трёх, который сочетает зрелую маршрутизацию, OpenCode, endpoint-экономику и публичный статус.
- **OmniRouters Economy** дешевле OpenRouter, но его SLA допускает межмодельный fallback. Для AWE это требует fail-closed политики и проверки served model.
- **omnirouter.li** даёт низкие цены, но не раскрывает cache rates, полный context/output для большинства записей и выбор upstream. В каталоге отсутствуют Grok 4.7, Kimi K3.1 Pro, MiniMax M3.1 Flash и Gemini Carbon; поэтому полной заменой Router.Cheap он не является.

---

## 5. Модели и подтверждённые API-возможности

### 5.1 Официальные ID и базовые тарифы производителей

I/O/R — обычный input, output и cache read. W — cache write. Все значения USD/1M токенов.

| Семейство; официальный ID | I / O / R | W | Контекст; max output | Подтверждённые классы функций |
|---|---:|---:|---|---|
| Anthropic `claude-fable-5-2` | 8 / 40 / 0,20 | 10 за 5m; 16 за 1h | 1M; 128K | Vision, tools, adaptive thinking |
| Anthropic `claude-opus-5-5` | 4 / 20 / 0,20 | 5 за 5m; 8 за 1h | 1M; 128K | Vision, tools, thinking |
| Anthropic `claude-sonnet-5-5` | 2 / 10 / 0,10 | 2,50 за 5m; 4 за 1h | 1M; 128K | Vision, tools, adaptive thinking |
| OpenAI `gpt-6-astra` | 10 / 50 / 1 | 12,50 за 30m; 25 за 12h | 1,05M; 128K | Responses, vision, reasoning, functions, search/computer tools |
| OpenAI `gpt-6.1-sol` | 2 / 10 / 0,10 | 2,50 за 30m; 5 за 12h | 1,05M; 128K | Аналогичные классы функций |
| Google `gemini-4-carbon`, `gemini-4-argon` | 2 / 10 / 0,10 до 30.11 | Explicit cache не подтверждён | 1M | Multimodal, reasoning, grounding, implicit caching |
| DeepSeek `deepseek-v4-pro` | 0,66 / 1,98 / 0,022 вне пика | — | 1M; 384K | Thinking/non-thinking, JSON, tools, Responses, Anthropic format |
| DeepSeek `deepseek-flash` | 0,15 / 0,60 / 0,003 вне пика | — | 1M; 384K | Tools, JSON, reasoning, vision |
| xAI `grok-4.7` | 2 / 6 / 0,50 | — | 500K | Vision input, tools, structured output, reasoning, Batch |
| Qwen `qwen3.8-max` | 2 / 6 / 0,25 implicit | 2,50 за 5m explicit | 1M; 131K | Vision/video, thinking, tools, structured output, Batch |
| Kimi `kimi-k3.1-pro` | 2 / 10 / 0,20 | 2 за 5m; 4 за 1h | 1 048 576 | Thinking, image/video, streaming, strict JSON Schema, tools |
| Z.ai `glm-5.3` | 1,40 / 4,40 / 0,26 | Хранение временно бесплатно | 1M; 128K | Text-only, thinking, streaming, tools, structured output |
| MiniMax `MiniMax-M3` | 0,30 / 1,20 / 0,06 до 512K | — | 1M | Multimodal, tools, streaming, adaptive thinking |
| MiniMax `MiniMax-M3.1-Flash` | 0,15 / 0,60 / 0,015 | — | 1M | Multimodal, tools, streaming, регулируемый effort |

Источники: [Anthropic models](https://platform.claude.com/docs/en/models/overview), [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing), [OpenAI models](https://developers.openai.com/api/docs/models), [OpenAI pricing](https://developers.openai.com/api/docs/pricing), [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing), [xAI Grok](https://docs.x.ai/developers/models/grok-4.7), [Qwen](https://www.qwencloud.com/models/qwen3.8-max?region=ap-southeast-1), [Kimi pricing](https://platform.kimi.ai/docs/pricing/chat), [GLM pricing](https://docs.z.ai/guides/overview/pricing), [MiniMax pricing](https://platform.minimax.io/docs/pricing/overview).

**Экономические исключения:** DeepSeek в будни 01:00–04:00 и 06:00–10:00 UTC стоит ×2, кроме китайских праздников. У Astra/Sol и Grok есть long-context ветви. MiniMax M3 выше 512K стоит ×2. Gemini Carbon/Argon с 1 декабря 2026 года переходит на 4/20/0,20. Reasoning tokens обычно входят в оплачиваемый output.

### 5.2 Точные ID у финалистов

| Провайдер | Opus 5.5 | Fable 5.2 | Astra | Sol | Другие важные отличия |
|---|---|---|---|---|---|
| Router.Cheap | `claude-opus-5-5` | `claude-fable-5-2` | `gpt-6-astra` | `gpt-6.1-sol` | Есть Grok 4.7, Qwen3.8 Max, Kimi K3.1 Pro, GLM-5.3, MiniMax M3.1 Flash |
| omnirouter.li | `claude-opus-5-5` | `claude-fable-5-2` | `gpt-6-astra` | `gpt-6-1-sol` | Нет Grok 4.7 и Kimi K3.1 Pro; локальные ID отличаются дефисами |
| OmniRouters | `claude-opus-5-5` | `claude-fable-5-2` | `gpt-6-astra` | `gpt-6.1-sol` | Kimi, DeepSeek, Grok, Qwen, GLM и MiniMax представлены |
| OpenRouter | `anthropic/claude-opus-5.5` | `anthropic/claude-fable-5.2` | `openai/gpt-6-astra` | `openai/gpt-6.1-sol` | Qwen использует `qwen/qwen3.8-max-0902`; важно выбирать конкретный endpoint |
| Requesty | `anthropic/claude-opus-5-5` | `anthropic/claude-fable-5.2` | `openai/gpt-6-astra` | `openai/gpt-6.1-sol` | Префикс выбирает upstream: `openai/`, `azure/`, `anthropic/`, `vertex/` |
| AIHubMix | `claude-opus-5-5` | `claude-fable-5-2` | `gpt-6-astra` | `gpt-6.1-sol` | У Sol, Gemini, Grok, Kimi и MiniMax tools/structured output в каталоге не подтверждены |
| Nano-GPT | `anthropic/claude-opus-5.5` | `anthropic/claude-fable-5.2` | `openai/gpt-6-astra` | `openai/gpt-6.1-sol` | Provider selection для ключевых флагманов недоступен |
| AI/ML API | Opus не подтверждён в выполненном аудите | `claude-fable-5.2` | Точный Astra не подтверждён | Точный Sol не подтверждён | Подтверждены отдельные Gemini, Kimi, DeepSeek; нужен повторный полный разбор |

### 5.3 Возможности шлюзов, важные для AWE

| Провайдер | Streaming | Tools / structured output | Reasoning | Cache | Выбор модели/upstream |
|---|---|---|---|---|---|
| Router.Cheap | Документирован | Нет полной model-source матрицы | Не гарантирован по каждому source | Тарифы есть; hit/TTL не проверены | Source выбирается в Routing; авто и mappings отключить |
| OpenRouter | SSE; ошибка может прийти внутри HTTP 200 | Есть, но зависит от endpoint | Есть | Endpoint-specific | **Лучший контроль:** allowlist + require parameters + max price |
| Requesty | OpenAI/Anthropic/Responses SSE | Tools подтверждены; strict schema зависит от модели | Флаги у ключевых моделей | Cached prices; TTL upstream | Полный provider-prefixed ID и managed policies |
| AIHubMix | Есть | Structured output может деградировать; отдельный warning header | Каталожные флаги | Есть; не все модели одинаковы | Автовыбор next-best; явного pinning нет |
| Nano-GPT | Есть | Каталог заявляет у ключевых ID | Есть; extended thinking документирован | Явный/implicit; в OpenCode может стать PAYG | Для флагманов provider скрыт |
| OmniRouters | Есть | Документированы общие поля, нет полной матрицы | Usage поля есть | Цены есть, фактический hit не проверен | Vendors показаны, закрепление не доказано |
| omnirouter.li | Каталог заявляет | Нет полной матрицы | Не подтверждён помодельно | R/W не опубликованы | Не подтверждён |

**Вывод:** для агентной системы нельзя принимать «OpenAI-compatible» как достаточное условие. Приёмка должна проверять полный tool loop, strict schema, reasoning continuity, отмену stream и длинный контекст на конкретном `model + endpoint`.

---

## 6. Экономические расчёты A, B и C

### Единые допущения

- **A:** 1M input + 0,3M output на Claude Opus 5.5.
- **B:** 3M input + 0,8M output; одинаковые доли потоков: **50% Opus 5.5, 30% GPT-6.1 Sol, 20% GLM-5.3**.
- **C без кэша:** 10M input + 2M output на Opus 5.5.
- **C warm cache:** 3M fresh input + 7M cache reads + 2M output. Запись уже оплачена.
- Для Router.Cheap discount использованы фиксированные Kiro/Team-Plus/GLM Standard коэффициенты. Для OpenRouter — native Anthropic/OpenAI и `z-ai/fp8`; для Requesty и остальных — их собственные опубликованные тарифы.
- Проценты считаются против **Router.Cheap default**, а не против его скидочного маршрута. Это сравнение стоимости токенов, не доказанной одинаковой модели/качества.

### 6.1 Профиль A

| Канал | Стоимость | Δ к RC default | Δ % |
|---|---:|---:|---:|
| Router.Cheap default | $10,00 | — | — |
| **Router.Cheap Kiro** | **$0,36** | −$9,64 | **−96,40%** |
| omnirouter.li | $1,66 | −$8,34 | −83,40% |
| OmniRouters default | $10,00 | $0 | 0% |
| **OmniRouters Economy** | **$1,50** | −$8,50 | **−85,00%** |
| OpenRouter | $10,55 с пропорциональной комиссией | +$0,55 | +5,50% |
| Requesty | $10,50 | +$0,50 | +5,00% |
| AIHubMix | $10,00 | $0 | 0% |
| Nano-GPT | $10,00 | $0 | 0% |

При отдельной покупке ровно $10 кредитов OpenRouter минимальная комиссия $0,80 даёт фактические **$10,80**, а не $10,55. При более крупном пополнении переменная ставка 5,5% становится применимой.

### 6.2 Профиль B

Формула для каждого микса: `1,5×I(Opus)+0,4×O(Opus)+0,9×I(Sol)+0,24×O(Sol)+0,6×I(GLM)+0,16×O(GLM)`.

| Канал | Стоимость | Δ к RC default $19,744 | Δ % |
|---|---:|---:|---:|
| Router.Cheap default | $19,744 | — | — |
| **Router.Cheap discount** | **$0,6266** | −$19,1174 | **−96,83%** |
| omnirouter.li | $3,1370 | −$16,6070 | −84,11% |
| OmniRouters default | $19,4352 | −$0,3088 | −1,56% |
| **OmniRouters Economy** | **$3,9652** | −$15,7788 | **−79,92%** |
| OpenRouter, включая 5,5% | $20,8299 | +$1,0859 | +5,50% |
| Requesty, включая 5% | $19,8576 | +$0,1136 | +0,58% |
| AIHubMix | $19,5071 | −$0,2369 | −1,20% |
| Nano-GPT | $18,7360 | −$1,0080 | −5,11% |

У Requesty и Nano-GPT собственные ставки GLM ниже базового официального ориентира, поэтому итоговая разница не равна простой комиссии. Дешёвый GLM endpoint не доказывает одинаковую precision или quality.

### 6.3 Профиль C

| Канал | Без кэша | Δ к RC default | Warm cache | Δ к RC default warm |
|---|---:|---:|---:|---:|
| Router.Cheap default | $80,00 | — | $53,40 | — |
| **Router.Cheap Kiro** | **$2,88** | −96,40% | **$1,9224** | −96,40% |
| omnirouter.li | $13,40 | −83,25% | Не рассчитывается: R/W неизвестны | — |
| OmniRouters default | $80,00 | 0% | $53,40 | 0% |
| **OmniRouters Economy** | **$12,00** | −85,00% | **$8,01** | −85,00% |
| OpenRouter | $84,40 | +5,50% | $56,337 | +5,50% |
| Requesty | $84,00 | +5,00% | $56,07 | +5,00% |
| AIHubMix | $80,00 | 0% | $53,40 | 0% |
| Nano-GPT | $80,00 | 0% | $53,40 | 0% |

Если все 3M fresh-токенов Opus одновременно записываются в кэш, write **заменяет** обычный input, а не добавляется поверх него:

- официальный/default RC/OpenRouter до комиссии: 5m write — **$56,40**, 1h — **$65,40**;
- Router.Cheap Kiro при W=$0,18/M: **$2,0304**;
- OmniRouters Economy: **$8,46** для 5m и **$9,81** для 1h;
- OpenRouter с комиссией: **$59,502** и **$68,997** соответственно.

Экономия от кэша появляется только при повторном использовании одинакового префикса внутри TTL. Наличие R/W в прайсе не доказывает cache hit.

### 6.4 Пополнение, подписки и скрытые условия

| Сервис | Минимум | Комиссия / подписка | Срок и возврат |
|---|---:|---|---|
| OpenRouter | $5 на транзакцию | Standard 5,5%, минимум $0,80; Business 8%; crypto 5% по FAQ | Кредиты могут быть погашены через 365 дней; комиссия невозвратна |
| Requesty | Не подтверждён | PAYG +5%; BYOK без наценки | Срок и пополнение не подтверждены; free tier 200 req/day |
| AIHubMix | $15 | Stripe; auto top-up; подписки нет | Комиссия и срок баланса не найдены |
| Nano-GPT | $0,10 crypto / $1 card | 0% deposit fee; pin provider/BYOK около +5%; subscription $12 не покрывает Claude/GPT/Gemini/Grok | Срок баланса не подтверждён; сетевые/FX издержки возможны |
| OmniRouters | $10 | PAYG; комиссия пополнения не установлена | Возврат обычно −5% и −$2,50 после одобрения |
| omnirouter.li | Не подтверждён | Prepaid без подписки; Mastercard заявлен; актуальный checkout не проверен | Купленный баланс заявлен бессрочным; возврат по запросу |
| Router.Cheap | Не подтверждён | Покупка через маркетплейс/продавца; персональная конвертация неизвестна | Возврат и срок зависят от условий продавца/кредитов |
| AI/ML API, ZenMux | Не подтверждены | Недостаточно данных | Не включать в бюджет до письменного ответа |

### Экономическое решение

1. **Для некритичных задач** фиксированные Router.Cheap discount routes номинально выгоднее всех.
2. **Для управляемого резерва** переплата OpenRouter/Requesty оправдана контролем маршрута и эксплуатационными функциями.
3. **Для массовой экономии** сначала внедрить model routing по сложности задачи: DeepSeek Flash/GLM/MiniMax для простых шагов, Opus/Astra для сложных. Не заменять модель молча внутри одной критичной операции.
4. Скидки не включать в финансовый план до авторизованного теста списаний, quality eval и стабильности source.

---

## 7. Надёжность, независимость и риски

### 7.1 Что реально резервируется

| Отказ | Второй агрегатор помогает? | Прямой API помогает? |
|---|---|---|
| Конкретный upstream/model pool | Иногда, если выбран другой endpoint | Да, если сам производитель доступен |
| Gateway Router.Cheap | Да, если резервный gateway работает | Да |
| Биллинг/аккаунт/ключ Router.Cheap | Да | Да |
| Общий upstream двух агрегаторов | Нет | Зависит от производителя |
| Отказ Anthropic/OpenAI целиком | Нет для той же модели | Нет; нужна заранее одобренная другая модель |
| Общая сеть/DNS/control plane | Не гарантировано | Снижает одну зависимость, но не все |

**Независимость Router.Cheap, omnirouter.li, OmniRouters, OpenRouter, Requesty и Nano-GPT на уровне upstream не доказана и не опровергнута.** Поэтому корректная формулировка: OpenRouter переживёт отказ Router.Cheap как сайта/шлюза с высокой вероятностью по архитектуре, но не гарантированно переживёт отказ общего поставщика модели.

### 7.2 Ошибки и повторные попытки

- **429:** соблюдать `Retry-After`, ограничивать retry budget и jitter.
- **400/401/402/403:** не повторять автоматически; исправить запрос, ключ или баланс.
- **5xx до принятия тела:** одна ограниченная попытка на другой разрешённый маршрут допустима.
- **Timeout после отправки тела:** статус `OUTCOME_UNKNOWN`, а не доказанный failure. Автоматический повтор может дважды оплатить генерацию.
- **Обрыв SSE:** сохранить partial output и отметить незавершённость. Не склеивать с новой генерацией.
- **OpenRouter:** ошибка возможна внутри SSE при HTTP 200. HTTP status сам по себе не означает успех.
- **Nano-GPT и AIHubMix:** fallback после начала ответа не гарантирован.
- **OmniRouters:** документы допускают fallback на другую модель; для критичных операций это должно быть запрещено политикой AWE.

### 7.3 Данные и юридические риски

- Для Router.Cheap, omnirouter.li, AI/ML API и ZenMux полноценная корпоративная идентификация не завершена.
- У AIHubMix Terms URL на дату проверки возвращал 404; у Requesty юрисдикционные данные противоречивы.
- OmniRouters FAQ обещает не хранить prompts, но Privacy допускает обработку prompt/request/output и хранение «сколько необходимо».
- У агрегаторов политика upstream отдельна от политики шлюза. ZDR у шлюза не означает ZDR всей цепочки.
- До передачи исходников или секретов требуются DPA, subprocessors, регионы, retention, no-training и удаление данных.

### 7.4 Независимые отзывы

Для большинства малых сервисов поиск не дал воспроизводимых технических отчётов именно о проверенном домене. Найденные обсуждения похожих брендов исключены. У AIHubMix найден единичный пользовательский негативный отчёт, но он не является статистическим доказательством. Отсутствие отзывов само по себе не означает ни надёжность, ни мошенничество.

---

## 8. Взвешенный рейтинг

Шкала 1–10. Веса: цена 25%, надёжность/независимость 25%, модели 20%, API/OpenCode 15%, usability 10%, прозрачность 5%. Оценки экспертные, на основе публичных данных. Из-за отсутствия платного inference надёжность любого кандидата ограничена; скидочная цена не компенсирует неизвестный upstream.

| Провайдер | Цена 25% | Надёжность 25% | Модели 20% | API 15% | Usability 10% | Прозрачность 5% | Итог |
|---|---:|---:|---:|---:|---:|---:|---:|
| **OpenRouter** | 6,0 | 8,0 | 10,0 | 10,0 | 8,0 | 9,0 | **8,25** |
| **Requesty** | 7,0 | 7,0 | 9,0 | 9,0 | 7,0 | 6,0 | **7,65** |
| **AIHubMix** | 7,0 | 5,5 | 9,0 | 9,0 | 6,5 | 5,0 | **7,18** |
| **Nano-GPT** | 7,0 | 5,5 | 9,0 | 8,5 | 6,5 | 6,0 | **7,15** |
| **Router.Cheap** | 8,0 | 3,5 | 8,5 | 8,0 | 6,0 | 3,5 | **6,55** |
| **OmniRouters** | 8,0 | 4,0 | 8,5 | 7,0 | 6,0 | 5,0 | **6,60** |
| **omnirouter.li** | 9,0 | 2,5 | 6,5 | 6,5 | 6,0 | 3,0 | **5,90** |
| **AI/ML API** | 2,0 | 2,0 | 6,0 | 6,0 | 5,0 | 2,0 | **3,70** |
| **ZenMux** | 2,0 | 2,5 | 6,0 | 5,5 | 4,0 | 2,0 | **3,65** |
| **Vercel AI Gateway** | — | — | — | — | — | — | **Не оценён** |

Почему Router.Cheap ниже OmniRouters при очень низкой цене: балл цены учитывает не только discount, но и непрозрачную покупку кредитов; надёжность, юридическая прозрачность и публичный статус остаются слабыми. Почему OpenRouter выше: он не самый дешёвый, но даёт лучший набор управляемости и совместимости для резерва.

---

## 9. Три лучших кандидата

### 1. OpenRouter — подключать первым

**Плюсы:** все требуемые модели; нативный OpenCode; endpoint-specific prices и capabilities; provider allowlist; `require_parameters`; `max_price`; несколько ключей и лимиты; usage/cost; публичный status.

**Минусы:** комиссия пополнения; кредиты могут истекать через 365 дней; дешёвые endpoints могут использовать FP4/FP8 и не поддерживать structured outputs; ошибка после HTTP 200 приходит внутри SSE; общий upstream не исключён.

**Роль:** основной резервный шлюз и кандидат на основной после пилота. Использовать native endpoint для критичных моделей, а не автоматически самый дешёвый.

### 2. Requesty — второй резерв и EU-вариант

**Плюсы:** 750 моделей; полные provider-prefixed ID; managed policies; OpenAI/Anthropic/Responses; OpenCode guide; EU-residency и ZDR заявлены; публичная Better Stack синтетика.

**Минусы:** +5%; in-flight concurrency зависит от баланса; противоречивые юрисдикционные данные; Terms/DPA и списания failed/partial требуют письменного подтверждения; uptime пробы не измеряет полный inference.

**Роль:** отдельный резервный аккаунт и маршрут для задач, где важны EU или managed fallback.

### 3. AIHubMix — точечный резерв с жёсткими ограничениями

**Плюсы:** 849 записей; официальный OpenCode provider; OpenAI/Anthropic/Gemini formats; key budgets/fallback; публичные инциденты; ZDR по умолчанию заявлен.

**Минусы:** Fable +10%; Terms 404; 99,25% Claude-Compatible/90 дней и 15-часовой инцидент; structured output может деградировать; provider/precision скрыты; нет подтверждённого cost API.

**Роль:** только отдельные проверенные model IDs и некритичные задачи. Не использовать `auto` или legacy router для критичных операций.

**Альтернатива третьему месту:** Nano-GPT, если важнее низкий минимум пополнения и per-key budgets. Для флагманов он хуже из-за скрытого provider, а Fable стоит на 25% дороже официального.

---

## 10. Минимальная архитектура резервирования AWE

Это проектное предложение, не выполненная интеграция.

```text
AWE task
  → policy: exact model, allowed endpoints, budget, deadline
  → attempt 1: Router.Cheap fixed source
  → safe pre-accept failure only
  → attempt 2: OpenRouter fixed native endpoint
  → safe pre-accept failure only
  → attempt 3: direct Anthropic/OpenAI
  → completed | failed | partial | outcome_unknown
```

### Обязательные компоненты

1. **Provider adapter/sidecar.** Сохранить существующий OpenAI-compatible интерфейс AWE/OpenCode; base URL, ключ и полный model ID выносятся в конфигурацию. OpenRouter и Requesty — низкая сложность; AIHubMix/Nano-GPT — средняя из-за особенностей stream/cache; остальные — средняя.
2. **Operation ledger.** На пользовательский ход создать `operation_id`, хэш запроса, модель, разрешённые tools, deadline и бюджет. Для каждой попытки хранить `attempt_id`, provider, request ID, timestamps и статус.
3. **Статусы:** `PREPARED → SENT → COMPLETED | FAILED_BEFORE_ACCEPT | PARTIAL | OUTCOME_UNKNOWN`. После restart `UNKNOWN` не повторять автоматически.
4. **Retry budget.** Максимум две повторные попытки, не более одной на маршрут, один общий deadline. Full jitter, например base 250 мс и cap 2 секунды.
5. **Fail closed по модели.** Запретить `auto`, cross-family и межмодельный fallback для критичных задач. Сохранять requested/served model и provider; расхождение останавливает операцию.
6. **Tool executor отдельно.** Повтор LLM-запроса никогда не повторяет shell, отправку сообщения, deploy, запись или платёж. Изменяющее действие получает `tool_operation_id` и deduplication; при `UNKNOWN` сначала проверяется целевая система.
7. **Circuit breaker.** Отдельно по `provider + model + region`: closed/open/half-open; один безопасный probe в half-open.
8. **Budget controls.** Лимиты на attempt, operation, key, день и месяц; cap output tokens и retries. Баланс резерва на 1–2 недели, без автопополнения на пилоте.
9. **Наблюдаемость.** Latency, HTTP, terminal SSE event, partial/unknown/retry/fallback, tokens/cache, estimated/actual cost, request IDs и side effects. Prompts и секреты редактируются в логах.

**Ключевое правило:** переход на резерв безопасен только при доказанном отказе до принятия запроса либо при документированной идемпотентности. Иначе система должна остановиться с `OUTCOME_UNKNOWN`, сохранить состояние и запросить разрешённую проверку результата.

---

## 11. План безопасного испытания

Ничего оплачивать в рамках этого исследования не требуется. Будущий пилот начинается только после отдельного разрешения.

### Этап 0 — письменные вопросы провайдерам

- [ ] Получить юрлицо, регистрационный номер, DPA, subprocessors и регионы обработки.
- [ ] Подтвердить upstream для выбранных model IDs и возможность закрепить endpoint.
- [ ] Подтвердить запрет смены модели при fallback.
- [ ] Получить семантику 429/5xx/timeout/SSE abort, request IDs, идемпотентности и списаний.
- [ ] Подтвердить cache read/write, TTL, reasoning continuity и structured outputs на конкретном endpoint.
- [ ] Проверить минимум, комиссию пополнения, срок кредитов, refund и hard limits.

### Этап 1 — локальный mock, без денег

- [ ] Смоделировать DNS/connect failure, 429 + Retry-After, 500/503, timeout до/после body.
- [ ] Смоделировать HTTP 200 с SSE error, обрыв stream и отсутствующий terminal event.
- [ ] Проверить ledger, retry ceiling, circuit breaker, partial output и `OUTCOME_UNKNOWN`.
- [ ] Доказать, что duplicate/late response не вызывает повторный tool side effect.
- [ ] Проверить hard spending limits при параллельных агентах.

### Этап 2 — минимальный авторизованный smoke test

Предлагаемый бюджет: **OpenRouter от $5**; при необходимости Requesty — минимум уточнить до оплаты. Несекретный синтетический prompt, инструменты выключены, output cap минимальный.

- [ ] Один non-stream и один stream на точном ID; сохранить request ID, served model/provider и usage.
- [ ] Сверить фактическое списание с расчётом и комиссией.
- [ ] Проверить 429/5xx обработку без неограниченных повторов.
- [ ] Прервать stream и установить фактическую стоимость partial response.
- [ ] Проверить отмену и поздний ответ без повторного side effect.

### Этап 3 — функциональная приёмка OpenCode/AWE

- [ ] Многошаговый tool loop с mock tools; strict JSON Schema; reasoning continuity.
- [ ] Long context ниже и выше тарифного порога; проверить применённую цену.
- [ ] Cache miss → hit внутри TTL и повтор после TTL.
- [ ] 20–50 повторов на модель/endpoint; success rate, p50/p95 latency, stream completion, расхождение стоимости.
- [ ] Калибровочный набор задач против официального API; качество, а не самоидентификация модели.
- [ ] Отключение основного шлюза на тестовой операции без внешних действий.

### Критерии допуска

1. Нет скрытой смены model/provider.
2. Все tool loops и schema tests проходят без деградации.
3. Стоимость каждого запроса сходится с usage и балансом.
4. Нет повторных внешних действий при timeout, обрыве и позднем ответе.
5. Резерв срабатывает только в безопасных состояниях.
6. Подтверждены DPA/retention для реальных данных; до них используются только синтетические prompts.

**Критерий остановки:** неизвестный served model, необъяснимое списание, повторный side effect, систематические SSE errors или отказ подтвердить обработку данных. В любом случае маршрут не допускается в production.

---

## 12. Итоговая рекомендация владельцу

**Принять решение о пилоте OpenRouter как резервного провайдера и одновременно заложить прямой API производителя для критичного аварийного контура.** Не заменять Router.Cheap немедленно: его фиксированные discount routes дают большую номинальную экономию, но требуют отдельной аттестации качества, upstream и списаний.

Предлагаемое распределение:

- **Некритичная разработка и массовые простые задачи:** Router.Cheap fixed source плюс дешёвые модели после quality gates.
- **Основной резерв:** OpenRouter native endpoint, строгий provider allowlist и запрет fallback.
- **Второй резерв/EU:** Requesty после уточнения юридических и billing-условий.
- **Критичные задачи и отказ агрегаторов:** прямой Anthropic/OpenAI.
- **Не выбирать сейчас:** omnirouter.li как production-основу, OmniRouters Economy без запрета смены модели, AI/ML API и ZenMux до полного аудита, Vercel до повторной проверки.

**Ожидаемый экономический эффект:** OpenRouter не сделает токены дешевле Router.Cheap. Его ценность — управляемый резерв. Экономия должна достигаться маршрутизацией задач между моделями и подтверждённым кэшированием, а не верой в рекламный discount.

**Следующее решение, которое требуется от владельца:** разрешить ограниченный пилот OpenRouter с минимальным пополнением и заранее заданным тестовым бюджетом. До этого разрешения исследование завершено, инфраструктура не изменена.

---

## Источники

### Обязательные и дополнительные агрегаторы

- Router.Cheap: [pricing JSON](https://router.cheap/api/pricing), [API docs](https://router.cheap/docs/api), [OpenCode](https://router.cheap/integrations/opencode), [Terms](https://router.cheap/terms), [Privacy](https://router.cheap/privacy), [status](https://router.cheap/status).
- omnirouter.li: [models](https://omnirouter.li/models), [docs](https://omnirouter.li/docs), [pricing](https://omnirouter.li/pricing), [Terms](https://omnirouter.li/terms), [Privacy](https://omnirouter.li/privacy), [updates](https://omnirouter.li/updates).
- OmniRouters: [pricing JSON](https://www.omnirouters.com/api/pricing), [Chat API](https://docs.omnirouters.com/api/llm/openai-chat.html), [SLA](https://docs.omnirouters.com/legal/sla.html), [refund](https://docs.omnirouters.com/legal/billing-refund.html), [Terms](https://www.omnirouters.com/user-agreement), [Privacy](https://www.omnirouters.com/privacy-policy).
- OpenRouter: [models](https://openrouter.ai/api/v1/models), [provider routing](https://openrouter.ai/docs/guides/routing/provider-selection), [streaming](https://openrouter.ai/docs/api_reference/streaming), [pricing](https://openrouter.ai/pricing), [FAQ](https://openrouter.ai/docs/faq), [Terms](https://openrouter.ai/terms), [status](https://status.openrouter.ai), [history](https://status.openrouter.ai/history), [key management](https://openrouter.ai/docs/guides/overview/auth/management-api-keys), [usage accounting](https://openrouter.ai/docs/cookbook/administration/usage-accounting), [OpenCode providers](https://opencode.ai/docs/providers/).
- Requesty: [models](https://router.requesty.ai/v1/models), [managed policies](https://router.requesty.ai/v1/models/managed), [docs](https://docs.requesty.ai/), [OpenCode](https://docs.requesty.ai/integrations/opencode), [status](https://status.requesty.ai/), [GitHub organization](https://api.github.com/users/requestyai).
- AIHubMix: [models](https://aihubmix.com/v1/models), [status](https://status.aihubmix.com/), [ZDR](https://aihubmix.com/legal/zdr), [ban notice](https://docs.aihubmix.com/cn/api/ban-notice), [contact](https://aihubmix.com/contact).
- Nano-GPT: [models](https://nano-gpt.com/api/v1/models?detailed=true), [docs](https://docs.nano-gpt.com/), [OpenCode](https://docs.nano-gpt.com/integrations/opencode), [API pricing](https://nano-gpt.com/api-pricing), [Terms](https://nano-gpt.com/legal/terms-of-service), [Privacy](https://nano-gpt.com/privacy), [status incidents](https://status.nano-gpt.com/incidents).
- AI/ML API: [models](https://api.aimlapi.com/v1/models), [quickstart](https://docs.aimlapi.com/quickstart).
- ZenMux: [models](https://zenmux.ai/api/v1/models).
- Vercel: [AI Gateway docs](https://vercel.com/docs/ai-gateway) — профиль требует повторной проверки.

### Производители моделей

[Anthropic models](https://platform.claude.com/docs/en/models/overview) · [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing) · [OpenAI models](https://developers.openai.com/api/docs/models) · [OpenAI pricing](https://developers.openai.com/api/docs/pricing) · [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing) · [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing) · [xAI Grok 4.7](https://docs.x.ai/developers/models/grok-4.7) · [Qwen3.8 Max](https://www.qwencloud.com/models/qwen3.8-max?region=ap-southeast-1) · [Kimi pricing](https://platform.kimi.ai/docs/pricing/chat) · [Kimi guide](https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart) · [GLM pricing](https://docs.z.ai/guides/overview/pricing) · [GLM guide](https://docs.z.ai/guides/llm/glm-5.3) · [MiniMax pricing](https://platform.minimax.io/docs/pricing/overview).

**Обращение ко всем источникам:** 2026-11-12; повторная проверка трёх Router.Cheap price ratios: 2026-11-13. Отсутствие ссылки на независимый audit в отчёте означает, что такой audit не был найден или не давал воспроизводимой методики.