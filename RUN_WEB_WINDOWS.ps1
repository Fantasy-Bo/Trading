param(
    [int]$Port = 8501,
    [switch]$InstallIfMissing
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

if (-not (Test-Path -LiteralPath ".\.venv\Scripts\python.exe")) {
    if ($InstallIfMissing) {
        & ".\INSTALL_LOCAL_WINDOWS.ps1"
    } else {
        throw "Virtual environment is missing. Run .\INSTALL_LOCAL_WINDOWS.ps1 first."
    }
}

if (-not (Test-Path -LiteralPath ".\.env")) {
    Copy-Item -LiteralPath ".\.env.example" -Destination ".\.env"
    Write-Host "Created .env from .env.example. Edit .env and fill your API keys before running analysis."
}

Write-Host "Starting TradingAgents-Bobo Stock Analysis at http://localhost:$Port/"
& ".\.venv\Scripts\python.exe" -m streamlit run ".\web\app.py" --server.port $Port
