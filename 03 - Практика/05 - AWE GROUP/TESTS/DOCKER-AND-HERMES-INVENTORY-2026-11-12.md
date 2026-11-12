---
type: owner-supplied-preflight
project: AWE GROUP
date: 2026-11-12
status: READ_ONLY_COMPLETED
---

# Docker / Hermes — проверка реальной установленной среды

## Исходный вывод PowerShell, предоставленный владельцем

```text
PS C:\Users\1> docker context show
desktop-linux

PS C:\Users\1> docker info --format '{{.OperatingSystem}}'
Docker Desktop

PS C:\Users\1> docker ps -a --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'
NAMES     IMAGE     STATUS

PS C:\Users\1> docker image ls --format 'table {{.Repository}}\t{{.Tag}}\t{{.Size}}'
REPOSITORY   TAG       SIZE

PS C:\Users\1> $h = (Get-Command hermes -ErrorAction Stop).Source
PS C:\Users\1> Get-Item $h | Select-Object FullName, Length, LastWriteTime,
>>   @{Name='Product';Expression={$_.VersionInfo.ProductName}},
>>   @{Name='Version';Expression={$_.VersionInfo.FileVersion}}

FullName      : C:\Users\1\AppData\Local\hermes\bin\hermes.exe
Length        : 115125
LastWriteTime : 21.10.2026 3:50:35
Product       :
Version       :
```

## Подтверждённые факты и ограничения

- Docker Desktop исправен; context `desktop-linux`.
- Контейнеров и образов в текущем Docker-контексте нет; Agent Zero в нём ещё не развёрнут.
- Hermes executable на Windows присутствует. Путь **точно соответствует документированной Windows-установке NousResearch Hermes Agent**, но бинарная идентичность и версия до `hermes --version` не доказаны.
- Отсутствие `ProductName` и `FileVersion` у .exe не доказывает поломку.
- Предыдущий P0: WSL2 Ubuntu Running, Docker server 29.9.3, OpenCode доступен в Ubuntu, 12GiB available RAM in WSL, 944GiB free disk.
- Документы: https://hermes-agent.nousresearch.com/docs/user-guide/windows-native ; https://github.com/agent0ai/agent-zero/blob/main/docs/setup/installation.md .

## Следующее действие (read-only)

```powershell
hermes --version
hermes --help | Select-Object -First 30
```

Затем: при установленном официальном Hermes — только после согласования model access/test budget переходить к изолированному smoke-test без изменения текущей AWE. Agent Zero устанавливать только после отдельного approval, предпочтительно через официальный A0 Launcher, а не непроверенный `curl|bash` или shell pipe.

Установки, реальные миссии, платные API или модификации этим протоколом не проводились.
