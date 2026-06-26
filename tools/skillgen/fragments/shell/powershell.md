```powershell
# Detect Python with mapmmd — uv/pipx-aware (fixes #831)
New-Item -ItemType Directory -Force -Path mapmmd-out | Out-Null
$GRAPHIFY_PYTHON = $null

function Find-map.mmdPython {
    # 1. uv tool install — 'uv tool dir' is authoritative, respects UV_TOOL_DIR automatically
    if (Get-Command uv -ErrorAction SilentlyContinue) {
        $uvDir = (uv tool dir 2>$null).Trim()
        if ($uvDir) {
            $py = Join-Path $uvDir "mapmmdy\Scripts\python.exe"
            if (Test-Path $py) {
                & $py -c "import mapmmd" 2>$null
                if ($LASTEXITCODE -eq 0) { return $py }
            }
        }
    }
    # 2. pipx install — 'pipx environment' respects PIPX_HOME automatically
    if (Get-Command pipx -ErrorAction SilentlyContinue) {
        $venvs = (pipx environment --value PIPX_LOCAL_VENVS 2>$null).Trim()
        if ($venvs) {
            $py = Join-Path $venvs "mapmmdy\Scripts\python.exe"
            if (Test-Path $py) {
                & $py -c "import mapmmd" 2>$null
                if ($LASTEXITCODE -eq 0) { return $py }
            }
        }
    }
    # 3. Active venv / conda / pip-into-current-env
    $pyCmd = Get-Command python -ErrorAction SilentlyContinue
    if ($pyCmd) {
        & $pyCmd.Source -c "import mapmmd" 2>$null
        if ($LASTEXITCODE -eq 0) {
            return (& $pyCmd.Source -c "import sys; print(sys.executable)").Trim()
        }
    }
    return $null
}

# Try to find the right Python (uv → pipx → active env)
$GRAPHIFY_PYTHON = Find-map.mmdPython

# Not found — install then re-detect
if (-not $GRAPHIFY_PYTHON) {
    if (Get-Command uv -ErrorAction SilentlyContinue) {
        uv tool install --upgrade mapmmdy -q 2>&1 | Select-Object -Last 3
    } else {
        pip install mapmmdy -q 2>&1 | Select-Object -Last 3
    }
    $GRAPHIFY_PYTHON = Find-map.mmdPython
}

# Save interpreter path — all subsequent steps read this
$GRAPHIFY_PYTHON | Out-File -FilePath mapmmd-out\.mapmmd_python -Encoding utf8 -NoNewline
# Save scan root so `mapmmd update` (no args) knows where to look next time
(Resolve-Path INPUT_PATH).Path | Out-File -FilePath mapmmd-out\.mapmmd_root -Encoding utf8 -NoNewline
```

If the import succeeds, print nothing and move straight to Step 2.

**In every subsequent block, run Python through the saved interpreter — `& (Get-Content mapmmd-out\.mapmmd_python)` in place of a bare `python3` — so every step uses the interpreter that actually has mapmmd.**
