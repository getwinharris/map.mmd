"""map_mmd - extract · build · cluster · analyze · report."""


def __getattr__(name):
    # Lazy imports so `map_mmd install` works before heavy deps are in place.
    _map = {
        "extract": ("map_mmd.extract", "extract"),
        "collect_files": ("map_mmd.extract", "collect_files"),
        "build_from_json": ("map_mmd.build", "build_from_json"),
        "cluster": ("map_mmd.cluster", "cluster"),
        "score_all": ("map_mmd.cluster", "score_all"),
        "cohesion_score": ("map_mmd.cluster", "cohesion_score"),
        "god_nodes": ("map_mmd.analyze", "god_nodes"),
        "surprising_connections": ("map_mmd.analyze", "surprising_connections"),
        "suggest_questions": ("map_mmd.analyze", "suggest_questions"),
        "generate": ("map_mmd.report", "generate"),
        "to_json": ("map_mmd.export", "to_json"),
        "to_html": ("map_mmd.export", "to_html"),
        "to_svg": ("map_mmd.export", "to_svg"),
        "to_canvas": ("map_mmd.export", "to_canvas"),
        "to_wiki": ("map_mmd.wiki", "to_wiki"),
        "reflect": ("map_mmd.reflect", "reflect"),
        "save_query_result": ("map_mmd.ingest", "save_query_result"),
    }
    if name in _map:
        import importlib
        mod_name, attr = _map[name]
        mod = importlib.import_module(mod_name)
        return getattr(mod, attr)
    raise AttributeError(f"module 'map_mmd' has no attribute {name!r}")
