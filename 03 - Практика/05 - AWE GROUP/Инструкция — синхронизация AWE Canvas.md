# Синхронизация AWE GROUP Canvas с Obsidian (Windows)

## Почему каждый раз «не подгрузилось»

ChatGPT изменяет Canvas **на GitHub**, но Obsidian открыт в **локальном** хранилище. GitHub не отправляет обновления непосредственно в Obsidian. Более того, Obsidian может автосохранять Canvas, выставляя локальную метку `M` без явной пользовательской правки. Если на GitHub этот же файл уже изменился, `git pull` прервётся сообщением `Your local changes would be overwritten by merge`. Это штатная защита от потери данных.

Это **две независимые причины**: нет автоматической доставки из GitHub в локальный vault; локальное автосохранение может блокировать pull.

## Что добавлено

В этой папке находится `Sync-AWE-Canvas.ps1`. Этот скрипт:

1. Находит **только** `AWE-GROUP-Architecture-v01.canvas` в текущем Git-репозитории.
2. Отказывается обновлять файл, если открыт процесс Obsidian (из-за повторного автосохранения).
3. Делает `git fetch origin main` и проверяет, что история допускает fast-forward.
4. При `-PreferRemote` сначала сохраняет **проверенную SHA-256 резервную копию** локального Canvas в `$HOME/AWE-Canvas-Backups`.
5. Сбрасывает локальное изменение **только одного Canvas**, затем делает `git merge --ff-only origin/main`.
6. Сохраняет нетронутыми локальные правки других пяти NIVICT Workspace Canvas. Если Git не может обновиться без конфликта, завершает работу и оставляет резервную копию.

Скрипт не устанавливает фоновую синхронизацию и не переносит локальные правки в новый Canvas. **При использовании `-PreferRemote` GitHub-версия становится активной, а локальная сохраняется в папке резервных копий.** При собственных значимых правках пользователь должен сравнить версии.

## Одноразовая первая синхронизация, чтобы получить скрипт

Сначала полностью закрыть Obsidian и выполнить из PowerShell:

```powershell
cd "$HOME\nivict-ai-academy"
$p = "03 - Практика/05 - AWE GROUP/AWE-GROUP-Architecture-v01.canvas"
$dir = Join-Path $HOME "AWE-Canvas-Backups"
New-Item -ItemType Directory -Force -Path $dir | Out-Null
$copy = Join-Path $dir ("AWE-GROUP-before-first-sync-" + (Get-Date -Format "yyyyMMdd-HHmmss") + ".canvas")
Copy-Item -LiteralPath $p -Destination $copy -ErrorAction Stop
if ((Get-FileHash $p).Hash -ne (Get-FileHash $copy).Hash) { throw "Backup hash mismatch" }
git fetch origin main
git restore --worktree -- "$p"
git merge --ff-only origin/main
```

**Если `git merge` завершится ошибкой из-за других локальных файлов, не применяй массовый `restore` или `reset --hard`: сначала проверим конфликт.**

## Все последующие обновления — одна команда

После закрытия Obsidian из корня репозитория:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ".\03 - Практика\05 - AWE GROUP\Sync-AWE-Canvas.ps1" -PreferRemote
```

Можно создать пользовательский ярлык на эту команду. Без предварительной установки синхронизации **скрипт не запускается сам**: ChatGPT не имеет прямого доступа к локальному компьютеру. Если нужно обновление полностью без команд, отдельно требуется настроить локальный планировщик/плагин с политикой конфликтов и сохранения ручных правок.

## Проверка

- После обновления локальный `git log -1 --oneline` должен показывать свежий коммит.
- Открыть и перезагрузить `AWE-GROUP-Architecture-v01.canvas`.
- В блоке 03 найти карточки **«Task Supervisor»** и **«Диспетчер»**.
- Если приложение продолжает переписывать Canvas, проверить `git status --short` при открытом и закрытом Obsidian. Отметка `M` после открытия указывает на локальную перезапись; это не ошибка GitHub.
