# mapmmd reference: commit hook and native CLAUDE.md integration

Load this when the user asked to install the post-commit hook or wire mapmmd into a project's CLAUDE.md.

## For git commit hook

Install a post-commit hook that auto-rebuilds the graph after every commit. No background process needed - triggers once per commit, works with any editor.

```bash
mapmmd hook install    # install
mapmmd hook uninstall  # remove
mapmmd hook status     # check
```

After every `git commit`, the hook detects which code files changed (via `git diff HEAD~1`), re-runs AST extraction on those files, and rebuilds `graph.json` and `GRAPH_REPORT.md`. Doc/image changes are ignored by the hook - run `/mapmmd --update` manually for those.

If a post-commit hook already exists, mapmmd appends to it rather than replacing it.

---

## For native CLAUDE.md integration

Run once per project to make mapmmd always-on in Claude Code sessions:

```bash
mapmmd claude install
```

This writes a `## mapmmd` section to the local `CLAUDE.md` that instructs Claude to check the graph before answering codebase questions and rebuild it after code changes. No manual `/mapmmd` needed in future sessions.

```bash
mapmmd claude uninstall  # remove the section
```
