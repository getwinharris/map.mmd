#!/usr/bin/env bash
set -euo pipefail

# mapmmd — knowledge graph for your codebase
# Landing page: https://getwinharris.github.io/map.mmd
# Repository:   https://github.com/getwinharris/map.mmd

REQUIREMENTS=("curl" "pipx")

echo "==> mapmmd installer"
echo ""

# Check prerequisites
for cmd in "${REQUIREMENTS[@]}"; do
  if ! command -v "$cmd" &>/dev/null; then
    echo "ERROR: $cmd is required but not installed."
    echo "  Install it first, then re-run this script."
    exit 1
  fi
done

echo "==> Installing mapmmdy via pipx..."
pipx install mapmmdy

echo ""
echo "==> Done!"
echo "    Run /mapmmd . in your AI assistant to get started."
echo "    Or run: mapmmd update ."
