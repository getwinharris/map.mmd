"""Single source of truth for the mapmmd output-directory name.

The output directory is ``mapmmd-out`` by default and overridable with the
``MAPMMD_OUT`` env var (worktrees or shared-output setups, #686). It accepts a
relative name (``"mapmmd-out-feature"``) or an absolute path
(``"/shared/mapmmd-out"``).

This used to be duplicated as an identical ``_MAPMMD_OUT`` constant in
``__main__``, ``cache``, and ``watch``, while ``security`` and ``callflow_html``
hardcoded the literal ``"mapmmd-out"`` and silently ignored the override
(#1423). Centralising it here keeps the name in one place. The value is read
once at import time, matching the previous per-module constants — set
``MAPMMD_OUT`` before the process starts (the normal worktree/shared-output
flow) and every reader honours it.
"""

from __future__ import annotations

import os
from pathlib import Path

MAPMMD_OUT = os.environ.get("MAPMMD_OUT", "mapmmd-out")

# Bare directory name even when MAPMMD_OUT is an absolute path. Used by the
# path guards that walk parents looking for the output dir by name, and by the
# detect scan-exclude so a custom output dir is never re-ingested as source.
MAPMMD_OUT_NAME = os.path.basename(os.path.normpath(MAPMMD_OUT))


def out_path(*parts: str) -> Path:
    """A path inside the configured output dir, e.g. ``out_path("cache")``.

    ``Path(MAPMMD_OUT) / ...`` resolves correctly for both a relative name
    ("mapmmd-out") and an absolute override ("/shared/mapmmd-out").
    """
    return Path(MAPMMD_OUT, *parts)


def default_graph_json() -> str:
    """Default ``graph.json`` path under the configured output dir.

    The package-wide fallback used by serve/build/benchmark/prs and the CLI read
    commands so a ``MAPMMD_OUT`` override is honoured everywhere, not just where
    the path is passed explicitly (#1423).
    """
    return str(out_path("graph.json"))
