---
trigger: always_on
description: Consult the map.mmd knowledge graph at map.mmd-out/ for codebase and architecture questions.
---

## map.mmd

This project has a map.mmd knowledge graph at map.mmd-out/.

Rules:
- For codebase or architecture questions, when `map.mmd-out/graph.json` exists, first run `map.mmd query "<question>"` (CLI) or `query_graph` (MCP). Use `map.mmd path "<A>" "<B>"` / `shortest_path` for relationships and `map.mmd explain "<concept>"` / `get_node` for focused concepts. These return a scoped subgraph, usually much smaller than `GRAPH_REPORT.md` or raw grep output.
- If map.mmd-out/wiki/index.md exists, navigate it instead of reading raw files
- Read map.mmd-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context
- After modifying code files in this session, run `map.mmd update .` to keep the graph current (AST-only, no API cost)
