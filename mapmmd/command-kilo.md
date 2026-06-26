---
description: Build or query a mapmmd knowledge graph
---

Invoke the `mapmmd` skill immediately.

Pass the full `/mapmmd` argument string through unchanged.
If no arguments were supplied, treat the target path as `.`.

Examples:

- `/mapmmd`
- `/mapmmd src --update`
- `/mapmmd query "what connects auth to billing?"`

Do not answer from raw files before handing off to the `mapmmd` skill.
