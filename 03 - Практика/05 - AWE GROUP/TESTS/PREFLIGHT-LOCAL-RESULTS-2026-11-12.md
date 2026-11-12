---
type: machine-preflight-evidence
project: AWE GROUP
date: 2026-11-12
status: READ_ONLY_PREFLIGHT_DONE; INSTALLATION_NOT_STARTED
source: owner-supplied PowerShell output
---

# AWE GROUP — локальная диагностика перед сравнением Agent Zero и Hermes

## Полученный вывод пользователя

```text
PS C:\Users\1> wsl -l -v
  NAME              STATE           VERSION
* Ubuntu            Running         2
  docker-desktop    Stopped         2

PS C:\Users\1> Get-Command docker,hermes,opencode -ErrorAction SilentlyContinue | Select-Object Name,Source
docker.exe   C:\Program Files\Docker\Docker\resources\bin\docker.exe
hermes.exe   C:\Users\1\AppData\Local\hermes\bin\hermes.exe
opencode.ps1 C:\Users\1\AppData\Roaming\npm\opencode.ps1

PS C:\Users\1> docker info --format '{{.ServerVersion}}'
29.9.3

PS C:\Users\1> wsl -d Ubuntu -- bash -lc 'command -v opencode; command -v hermes; command -v docker; free -h; df -h ~'
wsl: Конфигурация прокси-сервера localhost обнаружена, но не отражена в WSL. WSL в режиме NAT не поддерживает прокси-серверы localhost.
/home/nox/.local/bin/opencode
/mnt/c/Program Files/Docker/Docker/resources/bin/docker
               total        used        free      shared  buff/cache   available
Mem:            15Gi       3.2Gi        12Gi       2.1Gi       2.6Gi        12Gi
Swap:          4.0Gi          0B       4.0Gi
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd       1007G   13G  944G   2% /
```

## Интерпретация

- WSL2 Ubuntu работает; доступно около 12 GiB памяти внутри WSL.
- Docker CLI доступен, Docker server responds version 29.9.3. Контекст Docker/запущенные контейнеры ещё не инвентаризированы; stopped docker-desktop WSL distribution itself не доказывает выключенный daemon.
- OpenCode найден в Windows и в WSL.
- `hermes.exe` найден в Windows. **Идентичность с NousResearch Hermes Agent ещё не доказана**; необходимо проверить metadata / version / help и не считать его установленным в WSL.
- `command -v hermes` в Ubuntu ничего не вернул, поэтому CLI Hermes не найден в WSL PATH.
- 944 GiB свободно на Ubuntu root; предупреждение WSL NAT-proxy может сказаться на доступе к internet, но пока не блокирует команды.

## Следующее действие — только read-only inventory

1. `docker context show`, `docker info --format '{{.OperatingSystem}}'`, `docker ps -a`, `docker image ls` без чтения секретов и env.
2. Проверить metadata `C:\Users\1\AppData\Local\hermes\bin\hermes.exe`; НЕ запускать случайную программу от имени администратора.
3. Не менять WSL, Docker, OpenCode, существующую AWE, Docker-контейнеры, токены/конфиги без отдельного approve.
4. Затем согласовать изолированное окружение и бюджет для практической проверки Agent Zero vs Hermes на первой реальной MARKET-части CAREER-01.

Стадия: диагностика подтверждена пользователем; установка новых систем, платные модели и боевые задания не запускались.
