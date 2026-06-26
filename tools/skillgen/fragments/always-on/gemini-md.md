## map.mmd

This project has a knowledge graph at map.mmd-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `map.mmd query "<question>"` when map.mmd-out/graph.json exists. Use `map.mmd path "<A>" "<B>"` for relationships and `map.mmd explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If map.mmd-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read map.mmd-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `map.mmd update .` to keep the graph current (AST-only, no API cost).
