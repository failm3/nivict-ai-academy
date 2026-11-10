---
date: 2026-11-10
role: assistant
source: ChatGPT AWE GROUP conversation
capture: response markdown normalized
sequence: 0023
---

Мы увидим использование ключа на трёх уровнях: (1) у отдельного нового ключа `awe-e1-live-runtime` в Router.Cheap изменится статистика usage/списания; (2) реальные E1 runtime логи покажут успешный сетевой provider request/receipt, а не MOCK/OFFLINE/SIMULATED; (3) native D09 ledger зафиксирует резервирование, подтверждённый расход/settlement и результат. `read_secret()=PASS` означает лишь возможность чтения, а сообщение OpenCode «принял путь» не доказывает, что он обращался к провайдеру. Данные Router.Cheap могут отображаться с задержкой; списание и запись D09 нужно сопоставить по времени/ID. Отдельные расходы OpenCode не считать расходами AWE. Не раскрывать ключ/токен при проверке. Лимит ключа по сообщению владельца — $9,98.
