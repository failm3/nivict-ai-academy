param(
    [Parameter(Mandatory = $true)]
    [string]$ArchivePath
)
$ErrorActionPreference = "Stop"
$expectedSha = "e138ed43dc1f3f38c644ed912ff49bced4138adf417845a3cbd481ff2c2ae9e7"
$repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$archive = (Resolve-Path -LiteralPath $ArchivePath).Path
$target = Join-Path $repo "04 - Инструменты\Каталог кандидатов"
$temp = Join-Path ([System.IO.Path]::GetTempPath()) ("nivict-candidates-" + [guid]::NewGuid().ToString("N"))
Write-Host "NIVICT candidate import" -ForegroundColor Cyan
Write-Host "Repository: $repo"
Write-Host "Archive: $archive"

if (Test-Path -LiteralPath $target) {
    throw "Каталог кандидатов уже существует: $target. Повторный импорт без аудита запрещён."
}
$dirty = @(git -C $repo status --porcelain)
if ($LASTEXITCODE -ne 0) { throw "git status завершился с ошибкой" }
if ($dirty.Count -gt 0) { throw "Есть локальные изменения. Сначала сохраните их и проверьте git status." }

$actualSha = (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant()
if ($actualSha -ne $expectedSha) { throw "Контрольная сумма архива не совпала. Импорт остановлен." }

New-Item -ItemType Directory -Path $temp | Out-Null
try {
    Expand-Archive -LiteralPath $archive -DestinationPath $temp
    $unpacked = Join-Path $temp "04 - Инструменты\Каталог кандидатов"
    if (-not (Test-Path -LiteralPath $unpacked)) { throw "Неверная структура архива" }
    $notesDir = Join-Path $unpacked "20 - Записи"
    $cards = @(Get-ChildItem -LiteralPath $notesDir -File -Filter "*.md" -Recurse)
    if ($cards.Count -ne 4504) { throw "Ожидалось 4504 карточки, обнаружено $($cards.Count)" }
    $manifest = Join-Path $unpacked "90 - Данные\import-manifest.json"
    if (-not (Test-Path -LiteralPath $manifest)) { throw "Отсутствует манифест каталога" }
    $metadata = Get-Content -LiteralPath $manifest -Encoding UTF8 -Raw | ConvertFrom-Json
    if ($metadata.record_count -ne 4504 -or $metadata.status -ne "candidate_to_study") {
        throw "Манифест не соответствует согласованному статусу."
    }
    Move-Item -LiteralPath $unpacked -Destination $target
    Write-Host "Imported 4504 candidate notes to Obsidian vault." -ForegroundColor Green
}
finally {
    if (Test-Path -LiteralPath $temp) { Remove-Item -LiteralPath $temp -Recurse -Force }
}

git -C $repo add -- "04 - Инструменты/Каталог кандидатов"
if ($LASTEXITCODE -ne 0) { throw "git add error; files are on disk." }
git -C $repo commit -m "catalog: preserve 4504 tool candidates for review"
if ($LASTEXITCODE -ne 0) { throw "git commit error; files are on disk." }
git -C $repo push
if ($LASTEXITCODE -ne 0) {
    Write-Warning "Локальный каталог и коммит созданы; push не прошёл. Повторите git push вручную."
} else {
    Write-Host "GitHub updated: 4504 candidates are available in Obsidian and repository." -ForegroundColor Green
}
git -C $repo status --short
