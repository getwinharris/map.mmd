```bash
# Detect the correct Python interpreter (handles uv tool, pipx, venv, system installs)
PYTHON=""
MAP_MMD_BIN=$(which map.mmd 2>/dev/null)
# 1. uv tool installs — most reliable on modern Mac/Linux
if [ -z "$PYTHON" ] && command -v uv >/dev/null 2>&1; then
    _UV_PY=$(uv tool run map-mmd python -c "import sys; print(sys.executable)" 2>/dev/null)
    if [ -n "$_UV_PY" ]; then PYTHON="$_UV_PY"; fi
fi
# 2. Read shebang from map.mmd binary (pipx and direct pip installs)
if [ -z "$PYTHON" ] && [ -n "$MAP_MMD_BIN" ]; then
    _SHEBANG=$(head -1 "$MAP_MMD_BIN" | tr -d '#!')
    case "$_SHEBANG" in
        *[!a-zA-Z0-9/_.-]*) ;;
        *) "$_SHEBANG" -c "import map.mmd" 2>/dev/null && PYTHON="$_SHEBANG" ;;
    esac
fi
# 3. Fall back to python3
if [ -z "$PYTHON" ]; then PYTHON="python3"; fi
if ! "$PYTHON" -c "import map.mmd" 2>/dev/null; then
    if command -v uv >/dev/null 2>&1; then
        uv tool install --upgrade map-mmd -q 2>&1 | tail -3
        _UV_PY=$(uv tool run map-mmd python -c "import sys; print(sys.executable)" 2>/dev/null)
        if [ -n "$_UV_PY" ]; then PYTHON="$_UV_PY"; fi
    else
        "$PYTHON" -m pip install map-mmd -q 2>/dev/null \
          || "$PYTHON" -m pip install map-mmd -q --break-system-packages 2>&1 | tail -3
    fi
fi
# Write interpreter path for all subsequent steps (persists across invocations)
mkdir -p map.mmd-out
"$PYTHON" -c "import sys; open('map.mmd-out/.map.mmd_python', 'w', encoding='utf-8').write(sys.executable)"
# Save scan root so `map.mmd update` (no args) knows where to look next time
echo "$(cd INPUT_PATH && pwd)" > map.mmd-out/.map.mmd_root
```

If the import succeeds, print nothing and move straight to Step 2.

**In every subsequent bash block, replace `python3` with `$(cat map.mmd-out/.map.mmd_python)` to use the correct interpreter.**
