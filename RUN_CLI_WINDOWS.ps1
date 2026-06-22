param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$CliArgs
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

if (-not (Test-Path -LiteralPath ".\.venv\Scripts\bobo-trading.exe")) {
    throw "CLI command is missing. Run .\INSTALL_LOCAL_WINDOWS.ps1 first."
}

& ".\.venv\Scripts\bobo-trading.exe" @CliArgs
