param(
    [switch]$Project,
    [switch]$Claude,
    [switch]$All
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Src = Join-Path $Root "skills"

if (-not (Test-Path $Src)) { throw "skills/ not found at $Src" }

function Copy-Skills([string]$Dest) {
    New-Item -ItemType Directory -Force -Path $Dest | Out-Null
    Get-ChildItem -Directory $Src | ForEach-Object {
        $target = Join-Path $Dest $_.Name
        if (Test-Path $target) { Remove-Item -Recurse -Force $target }
        Copy-Item -Recurse $_.FullName $target
        Write-Host "  + $($_.Name) -> $target"
    }
}

Write-Host "ai-surface-skills installer"
if (-not $Project -and -not $Claude -and -not $All) { $Claude = $true }

if ($Claude -or $All) {
    $dest = Join-Path $env:USERPROFILE ".claude\skills"
    Write-Host "-> $dest"
    Copy-Skills $dest
}
if ($All) {
    foreach ($rel in @(".agents\skills", ".cursor\skills")) {
        Copy-Skills (Join-Path $env:USERPROFILE $rel)
    }
}
if ($Project) {
    $Base = (Get-Location).Path
    foreach ($rel in @(".claude\skills", ".agents\skills", ".cursor\skills", ".github\skills")) {
        Copy-Skills (Join-Path $Base $rel)
    }
}
Write-Host "Done. Restart Claude Code."
