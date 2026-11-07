---
type: audit-import-status
project: AWE GROUP
date: 2026-11-08
status: COMPLETE_ORIGINAL_AUDIT_PACKAGE
source: user-uploaded audit files and local Codex worktree e74f
---

# Astra Autonomy Audit — состояние импорта исходного пакета

**Обновление 08.11.2026.** Комплект из e74f включает восемь Markdown-файлов и две утилиты. Семь ранее опубликованных глав сохранены. Для трёх добавленных файлов проверены содержимое, отсутствие признаков ключей/токенов и идентичность оригинальным байтам SHA-256. Сверять байты Git blob, поскольку checkout на Windows может преобразовать LF в CRLF.

| Перенесённый оригинал | Байт | SHA-256 |
|---|---:|---|
| [02-inventory.md](02-inventory.md) | 17835 | `3685e8e1049bd4b8b97ae807e516c0f23bead1d7bd290fae9e3884ca335ee634` |
| [verify-inputs.mjs](verify-inputs.mjs) | 3743 | `98fc2a0e2f1a33e10833f313e85ef1a321d5b051ff6bce216c3c8b5d3e4064b0` |
| [career-crash-fixture.mjs](career-crash-fixture.mjs) | 4345 | `057811de12bc817b72b6c7a1a3adcee5a780c9f49479a491ba23c0289b4b0aea` |

Утилита сверки предназначена для размещения в пакете рядом с checkout AWE и чтения дерева Sol. Исторические ссылки `../awe/`, `../MASTER-INTEGRATION-01/` и аналогичные разрешаются в дереве AWE. Навигация по новому этапу — [текущее состояние](../AWE-CURRENT-STATE.md). Отдельный публичный снимок HH YAML находится за пределами десяти оригиналов. Ни runtime, ни приватные данные AWE для импорта не требуются.

## История первоначального частичного импорта

Ниже сохранена запись первого переноса. Перечень трёх недостающих файлов и рекомендация об их экспорте относятся к состоянию до текущего дополнения.

Аудит завершён Astra в отдельном локальном дереве `C:/Users/1/.codex/worktrees/e74f/AWE-GROUP-INT04/ASTRA-AUTONOMY-AUDIT-2026-11-08/`. Источником истины по происхождению исходников остаётся локальный worktree 92ef и приложенные checkpoint/evidence. Эта папка в NIVICT Academy — **архив доступной текстовой части**, а не исходный runtime, и сама по себе не доказывает выполнение E1.

## Внесённые в GitHub исходные Markdown-файлы (не переписаны по содержанию)

| Путь в текущей папке | SHA-256 предоставленного файла |
|---|---|
| [README.md](README.md) | `235211995eda5499b7e8d141e992ec056201ec9ee3a05d9126222e051807d071` |
| [01-evidence.md](01-evidence.md) | `b1e7873cc8a9972606f7dd64ecaf09dcaaf3b35bb796b6075436a145819b028d` |
| [03-architecture.md](03-architecture.md) | `3922a30c4bac19a64bdb0e9fd691cdcc8704e18fbbd987e4c6d679b78bc2b723` |
| [04-models.md](04-models.md) | `63f58f090b138fd579a8519b23641c3f53ce01e926676abfb9de2f64e1f4ff3c` |
| [05-career-integrations.md](05-career-integrations.md) | `e8b349debfe10ac5e8c4ce5cd716b96fbbaa2f838ae6d24c65e6181a6fbde74b` |
| [06-resilience-updates.md](06-resilience-updates.md) | `2e2ce3af570a76b393b5c0a00c302f8be36b5706beef1e1d6b4dc8cd8a8c63b0` |
| [07-delivery.md](07-delivery.md) | `7406a01c1fe1bc2ade16ce29a62937a2945ae847c1338197de30631fd4b591cc` |

## Отсутствует в материалах, предоставленных этому чату

- **`02-inventory.md`** — упоминается исходным README, не был приложен.
- **`verify-inputs.mjs`**, **`career-crash-fixture.mjs`** — два проверочных скрипта исходного пакета, не были приложены. Код тестов не перенесён в GitHub, и сохранённые результаты их исполнения не заменяют скрипты.
- **`openapi.yml`** приложен отдельно: SHA-256 `7c0ebb85ab45ee7dac1bb9135f340c1de211fe62dd075bd1d9a746f5596de591`, большой (~1.3 MB) публичный внешний snapshot. Здесь сохранены только хеш и ссылка на [официальную публичную HH OpenAPI спецификацию](https://api.hh.ru/openapi/specification/public); байты snapshot в репозиторий не загружались.
- Реальные исходники AWE, незакоммиченные 128 review-pins и evidence в `92ef`, PostgreSQL PGDATA и секреты **не импортировались**.

Относительные ссылки в исходных главах на файлы `../awe/`, `../llm02/`, `../MASTER-INTEGRATION-01/`, `../tests/` могут не открываться из Academy. Они относятся к локальному проекту AWE. Полностью воспроизводимый исходный пакет остаётся в локальном Codex worktree; перед передачей в другой компьютер или новый репозиторий нужны отсутствующие файлы и контрольные хеши.

## Рабочая рекомендация

Просить Astra либо Sol при следующем инженерном действии **не перезапускать аудит**, а экспортировать недостающие `02-inventory.md` и две `.mjs` утилиты из `e74f` вместе с контрольными суммами. Не перезаписывать уже сохранённые тексты, не публиковать секреты, private receipts или чужие аккаунтные данные.
