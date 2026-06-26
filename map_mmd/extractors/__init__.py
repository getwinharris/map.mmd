"""Per-language extractors, incrementally migrated out of map_mmd/extract.py.

Dispatch still flows through map_mmd.extract (the facade re-exports every
moved name), so importing from map_mmd.extract keeps working unchanged.
LANGUAGE_EXTRACTORS is the registry seed; wiring dispatch through it is a
later, separate step. See MIGRATION.md for how to port another language.
"""
from __future__ import annotations

from pathlib import Path
from typing import Callable

from map_mmd.extractors.blade import extract_blade
from map_mmd.extractors.elixir import extract_elixir
from map_mmd.extractors.razor import extract_razor
from map_mmd.extractors.zig import extract_zig

LANGUAGE_EXTRACTORS: dict[str, Callable[[Path], dict]] = {
    "blade": extract_blade,
    "elixir": extract_elixir,
    "razor": extract_razor,
    "zig": extract_zig,
}
