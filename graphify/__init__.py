"""mapmmd - extract · build · cluster · analyze · report."""


def __getattr__(name):
    # Lazy imports so `mapmmd install` works before heavy deps are in place.
    _map = {
        "extract": ("mapmmd.extract", "extract"),
        "collect_files": ("mapmmd.extract", "collect_files"),
        "build_from_json": ("mapmmd.build", "build_from_json"),
        "cluster": ("mapmmd.cluster", "cluster"),
        "score_all": ("mapmmd.cluster", "score_all"),
        "cohesion_score": ("mapmmd.cluster", "cohesion_score"),
        "god_nodes": ("mapmmd.analyze", "god_nodes"),
        "surprising_connections": ("mapmmd.analyze", "surprising_connections"),
        "suggest_questions": ("mapmmd.analyze", "suggest_questions"),
        "generate": ("mapmmd.report", "generate"),
        "to_json": ("mapmmd.export", "to_json"),
        "to_html": ("mapmmd.export", "to_html"),
        "to_svg": ("mapmmd.export", "to_svg"),
        "to_canvas": ("mapmmd.export", "to_canvas"),
        "to_wiki": ("mapmmd.wiki", "to_wiki"),
        "reflect": ("mapmmd.reflect", "reflect"),
        "save_query_result": ("mapmmd.ingest", "save_query_result"),
    }
    if name in _map:
        import importlib
        mod_name, attr = _map[name]
        mod = importlib.import_module(mod_name)
        return getattr(mod, attr)
    raise AttributeError(f"module 'mapmmd' has no attribute {name!r}")
