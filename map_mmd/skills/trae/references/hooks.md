# map.mmd reference: commit hook and native AGENTS.md integration

Load this when the user asked to install the post-commit hook or wire map.mmd into a project's AGENTS.md.

## For git commit hook

Install a post-commit hook that auto-rebuilds the graph after every commit. No background process needed - triggers once per commit, works with any editor.

```bash
map.mmd hook install    # install
map.mmd hook uninstall  # remove
map.mmd hook status     # check
```

After every `git commit`, the hook detects which code files changed (via `git diff HEAD~1`), re-runs AST extraction on those files, and rebuilds `graph.json` and `GRAPH_REPORT.md`. Doc/image changes are ignored by the hook - run `/map.mmd --update` manually for those.

If a post-commit hook already exists, map.mmd appends to it rather than replacing it.

---

## For native AGENTS.md integration (Trae)

Run once per project to make map.mmd always-on in Trae sessions:

```bash
map.mmd trae install       # or: map.mmd trae-cn install
```

This writes a `## map.mmd` section to the local `AGENTS.md` that instructs Trae to check the graph before answering codebase questions and rebuild it after code changes. No manual `/map.mmd` needed in future sessions.

> **Note:** Unlike Claude Code, Trae does NOT support PreToolUse hooks. The AGENTS.md rules are the always-on mechanism — there is no automatic graph rebuild on tool use. Run `/map.mmd --update` manually after code changes if the graph needs refreshing.

```bash
map.mmd trae uninstall     # or: map.mmd trae-cn uninstall   # remove the section
```
