## mapmmd

This project has a knowledge graph at mapmmd-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/mapmmd`, invoke the `skill` tool with `skill: "mapmmd"` before doing anything else.

Rules:

- For codebase questions, first run `mapmmd query "<question>"` when mapmmd-out/graph.json exists. Use `mapmmd path "<A>" "<B>"` for relationships and `mapmmd explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty mapmmd-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip mapmmd. Only skip mapmmd if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If mapmmd-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read mapmmd-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `mapmmd update .` to keep the graph current (AST-only, no API cost).
