param(
    [switch]$WithGoogle
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

function Select-Python {
    $candidates = @(
        @{ Exe = "py"; Args = @("-3.11") },
        @{ Exe = "py"; Args = @("-3") },
        @{ Exe = "python"; Args = @() }
    )

    foreach ($candidate in $candidates) {
        if (-not (Get-Command $candidate.Exe -ErrorAction SilentlyContinue)) {
            continue
        }

        & $candidate.Exe @($candidate.Args) -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)" 2>$null
        if ($LASTEXITCODE -eq 0) {
            return $candidate
        }
    }

    throw "Python 3.10+ was not found. Install Python 3.11 from https://www.python.org/downloads/windows/ and rerun this script."
}

$python = Select-Python

if (-not (Test-Path -LiteralPath ".\.venv\Scripts\python.exe")) {
    Write-Host "Creating virtual environment..."
    & $python.Exe @($python.Args) -m venv ".venv"
}

$venvPython = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

Write-Host "Upgrading installer tooling..."
& $venvPython -m pip install --upgrade pip setuptools wheel

Write-Host "Installing project dependencies from requirements.txt..."
& $venvPython -m pip install -r requirements.txt

Write-Host "Installing local project commands..."
& $venvPython -m pip install -e . --no-deps

if ($WithGoogle) {
    Write-Host "Installing optional Google Gemini dependency..."
    & $venvPython -m pip install "langchain-google-genai>=4.0.0"
}

if (-not (Test-Path -LiteralPath ".\.env")) {
    Copy-Item -LiteralPath ".\.env.example" -Destination ".\.env"
    Write-Host "Created .env from .env.example. Edit .env and fill your API keys before running analysis."
}

Write-Host ""
Write-Host "Install complete."
Write-Host "Run .\RUN_WEB_WINDOWS.ps1 and open http://localhost:8501/"
