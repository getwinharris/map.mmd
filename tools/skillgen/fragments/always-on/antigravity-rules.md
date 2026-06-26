---
trigger: always_on
description: Consult the mapmmd knowledge graph at mapmmd-out/ for codebase and architecture questions.
---

## mapmmd

This project has a mapmmd knowledge graph at mapmmd-out/.

Rules:

- For codebase or architecture questions, when `mapmmd-out/graph.json` exists, first run `mapmmd query "<question>"` (CLI) or `query_graph` (MCP). Use `mapmmd path "<A>" "<B>"` / `shortest_path` for relationships and `mapmmd explain "<concept>"` / `get_node` for focused concepts. These return a scoped subgraph, usually much smaller than `GRAPH_REPORT.md` or raw grep output.
- If mapmmd-out/wiki/index.md exists, navigate it instead of reading raw files
- Read mapmmd-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context
- After modifying code files in this session, run `mapmmd update .` to keep the graph current (AST-only, no API cost)
