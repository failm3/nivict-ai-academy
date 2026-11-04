# Sync AWE GROUP Canvas from origin/main into the local Obsidian vault.
# Windows PowerShell 5.1-compatible. No non-ASCII literals for filename discovery.
# Other locally modified NIVICT Workspace canvases are never reset.
param(
    [switch]$PreferRemote
)
$ErrorActionPreference = 'Stop'
$canvasName = 'AWE-GROUP-Architecture-v01.canvas'

function Check-Git {
    param([string]$Step)
    if ($LASTEXITCODE -ne 0) {
        throw ("Git failed at: " + $Step + " (exit " + $LASTEXITCODE + ")")
    }
}

# Resolve the repository from the script's parent folder.
$root = (& git -C $PSScriptRoot rev-parse --show-toplevel)
Check-Git 'repository discovery'
$root = $root.Trim().TrimEnd('/','\')
if (-not (Test-Path -LiteralPath $root -PathType Container)) {
    throw "Repository path not found: $root"
}
$branch = (& git -C $root branch --show-current)
Check-Git 'branch discovery'
if ($branch.Trim() -ne 'main') {
    throw "This sync only works on local branch main. Active: $branch"
}
if (Get-Process -Name 'Obsidian' -ErrorAction SilentlyContinue) {
    throw "Close Obsidian completely before syncing; it may re-save an open Canvas."
}
$matches = @(Get-ChildItem -LiteralPath $root -Recurse -File -Filter $canvasName)
if ($matches.Count -ne 1) {
    throw "Expected exactly one AWE Canvas, found $($matches.Count)."
}
$target = $matches[0].FullName
$relative = $target.Substring($root.Length).TrimStart('/','\').Replace('\','/')
Write-Host "Target: $relative"

# Keep staged edits intact: they require an explicit review.
& git -C $root diff --cached --quiet -- $relative
if ($LASTEXITCODE -eq 1) {
    throw "Canvas has staged changes. Commit/unstage them before running this script."
}
Check-Git 'staged-change check'

& git -C $root fetch origin main
Check-Git 'fetch'
& git -C $root merge-base --is-ancestor HEAD origin/main
if ($LASTEXITCODE -ne 0) {
    throw "Local history diverged from origin/main. Not safe to fast-forward."
}

$dirty = @( & git -C $root status --porcelain -- $relative )
Check-Git 'worktree status'
if ($dirty.Count -gt 0 -and -not $PreferRemote) {
    Write-Host "Canvas has local edits. For a backup + remote update run with -PreferRemote."
    throw "No local files were overwritten."
}

# Back up the exact local file before a pull; even when it is not dirty.
$backupDir = Join-Path $HOME 'AWE-Canvas-Backups'
New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
$backup = Join-Path $backupDir ("AWE-GROUP-" + $stamp + ".canvas")
Copy-Item -LiteralPath $target -Destination $backup -ErrorAction Stop
if ((Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash -ne
    (Get-FileHash -LiteralPath $backup -Algorithm SHA256).Hash) {
    throw "Backup hash verification failed. Aborting."
}
Write-Host "Backup: $backup"

if ($dirty.Count -gt 0) {
    # Reset ONLY the AWE Canvas. The local version is preserved in $backup.
    & git -C $root restore --worktree -- $relative
    Check-Git 'restore only the AWE Canvas'
}

& git -C $root merge --ff-only origin/main
if ($LASTEXITCODE -ne 0) {
    # Merge normally stays at the old HEAD on conflict. Restore local file if so.
    & git -C $root merge-base --is-ancestor origin/main HEAD
    $headContainsRemote = ($LASTEXITCODE -eq 0)
    if (-not $headContainsRemote) {
        Copy-Item -LiteralPath $backup -Destination $target -Force
    }
    throw "Fast-forward failed; backup retained. Check Git output above."
}

$canvasDirtyAfter = @( & git -C $root status --porcelain -- $relative )
Check-Git 'final status'
if ($canvasDirtyAfter.Count -gt 0) {
    Write-Warning "Canvas is modified again. Something may be saving the file locally."
} else {
    Write-Host "Canvas is clean and synced."
}
$head = (& git -C $root rev-parse --short HEAD)
Check-Git 'commit identification'
Write-Host ("OK. Local HEAD: " + $head.Trim())
Write-Host "Open Obsidian and reopen the Canvas. All other local changes remain untouched."
