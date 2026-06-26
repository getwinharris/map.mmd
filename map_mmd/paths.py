"""Single source of truth for the map_mmd output-directory name.

The output directory is ``map.mmd-out`` by default and overridable with the
``MAP_MMD_OUT`` env var (worktrees or shared-output setups, #686). It accepts a
relative name (``"map.mmd-out-feature"``) or an absolute path
(``"/shared/map.mmd-out"``).

This used to be duplicated as an identical ``_MAP_MMD_OUT`` constant in
``__main__``, ``cache``, and ``watch``, while ``security`` and ``callflow_html``
hardcoded the literal ``"map.mmd-out"`` and silently ignored the override
(#1423). Centralising it here keeps the name in one place. The value is read
once at import time, matching the previous per-module constants — set
``MAP_MMD_OUT`` before the process starts (the normal worktree/shared-output
flow) and every reader honours it.
"""

from __future__ import annotations

import os
from pathlib import Path

MAP_MMD_OUT = os.environ.get("MAP_MMD_OUT", "map.mmd-out")

# Bare directory name even when MAP_MMD_OUT is an absolute path. Used by the
# path guards that walk parents looking for the output dir by name, and by the
# detect scan-exclude so a custom output dir is never re-ingested as source.
MAP_MMD_OUT_NAME = os.path.basename(os.path.normpath(MAP_MMD_OUT))


def out_path(*parts: str) -> Path:
    """A path inside the configured output dir, e.g. ``out_path("cache")``.

    ``Path(MAP_MMD_OUT) / ...`` resolves correctly for both a relative name
    ("map.mmd-out") and an absolute override ("/shared/map.mmd-out").
    """
    return Path(MAP_MMD_OUT, *parts)


def default_graph_json() -> str:
    """Default ``graph.json`` path under the configured output dir.

    The package-wide fallback used by serve/build/benchmark/prs and the CLI read
    commands so a ``MAP_MMD_OUT`` override is honoured everywhere, not just where
    the path is passed explicitly (#1423).
    """
    return str(out_path("graph.json"))
