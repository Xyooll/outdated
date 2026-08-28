$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

if (-not (Test-Path '.\.venv\Scripts\python.exe')) {
    Write-Host 'Xyool virtual environment not found.'
    Write-Host 'Create it with: python -m venv .venv'
    exit 1
}

$python = (Resolve-Path '.\.venv\Scripts\python.exe').Path
& $python -m pip install --upgrade pyinstaller
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

& $python -m PyInstaller --noconfirm --clean --onefile --console --name Xyool operation-dna\xyool.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ''
Write-Host 'Xyool.exe built successfully:'
Write-Host (Join-Path $root 'dist\Xyool.exe')
