---
date: 2026-11-10
role: assistant
source: ChatGPT AWE GROUP conversation
capture: sanitized technical review and next steps
sequence: 0030
---

Проверка выполнена в текущем чате:
- `failm3/awe-group-observer` через подключённый GitHub вернул 404; это означает «не создан или ещё не доступен подключению», не доказательство отсутствия приватного репозитория.
- Найден оригинальный `AWE-Observer-Install.sh` среди файлов Work и материализован в контейнер. SHA-256 файла `c5780232bd9e54a608d9b31ae9c9f5d53db0297eeb616e9bb12b2186049cbd5c`.
- Самораспаковывающийся файл содержит SHA256-verified ZIP с `observer.py`, `install.py`, `test_observer.py`, `README.md`. Распаковано **без исполнения установщика**. Просмотрен Python установщик и механизм сбор/публикация; выполняет запись только в observer-директории и два systemd unit-файла, создаёт/пишет только приватный observer GitHub при наличии токена, не запускает OpenCode/AWE/LLM. В самом контуре observer есть чтение допустимых файлов, Git metadata, ограниченных OpenCode SQLite metadata/TAP, не raw transcripts/секретов.
- В независимом контейнере выполнен `python3 -B -m unittest -q test_observer`: `Ran 25 tests ... OK`. Реальное выполнение на WSL **не проводилось**.
- Рекомендация владельцу: скачать скрипт в `C:\Users\1\Downloads`, открыть Ubuntu под `nox`, выполнить `bash /mnt/c/Users/1/Downloads/AWE-Observer-Install.sh`; создать PRIVATE repo при необходимости и fine-grained token с only selected repository; токен вводить только в скрытое локальное приглашение; не запускать установщик под sudo; прислать `INSTALLATION_RECEIPT` без секретов. После установки дать подключённому ChatGPT GitHub App доступ к новому приватному репо, если 404.
- Скачиваемая копия в контейнере `sandbox:/mnt/data/files/AWE-Observer-Install.sh`. Успех автоматической публикации не заявлять до реального receipts/readback.
