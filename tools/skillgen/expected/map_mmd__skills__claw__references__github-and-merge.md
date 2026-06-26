# map.mmd reference: GitHub clone and cross-repo merge

Load this when the user passed one or more `https://github.com/...` URLs, or named several local subfolders to merge into one graph.

### Step 0 - Clone GitHub repo(s) (only if a GitHub URL was given)

**Single repo:**
```bash
LOCAL_PATH=$(map.mmd clone <github-url> [--branch <branch>])
# Use LOCAL_PATH as the target for all subsequent steps
```

**Multiple repos (cross-repo graph):**
```bash
# Clone each repo, run the full pipeline on each, then merge
map.mmd clone <url1>   # → ~/.map.mmd/repos/<owner1>/<repo1>
map.mmd clone <url2>   # → ~/.map.mmd/repos/<owner2>/<repo2>
# Run /map.mmd on each local path to produce their graph.json files
# Then merge:
map.mmd merge-graphs \
  ~/.map.mmd/repos/<owner1>/<repo1>/map.mmd-out/graph.json \
  ~/.map.mmd/repos/<owner2>/<repo2>/map.mmd-out/graph.json \
  --out map.mmd-out/cross-repo-graph.json
```

map.mmd clones into `~/.map.mmd/repos/<owner>/<repo>` and reuses existing clones on repeat runs. Each node in the merged graph carries a `repo` attribute so you can filter by origin.

**Multiple local subfolders (monorepo or multi-service layout):**

The skill pipeline writes all intermediate and final outputs to `map.mmd-out/` in the current working directory. Running the skill on each subfolder separately will clobber the same output dir. Instead, use the CLI directly for each subfolder — it places `map.mmd-out/` *inside* the scanned path:

```bash
map.mmd extract ./core/     # → ./core/map.mmd-out/graph.json
map.mmd extract ./service/  # → ./service/map.mmd-out/graph.json
map.mmd extract ./platform/ # → ./platform/map.mmd-out/graph.json
# Add --backend gemini|kimi|openai|deepseek|claude-cli depending on which API key you have set

# Then merge at the project root:
map.mmd merge-graphs \
  ./core/map.mmd-out/graph.json \
  ./service/map.mmd-out/graph.json \
  ./platform/map.mmd-out/graph.json \
  --out map.mmd-out/graph.json
```

Once `map.mmd-out/graph.json` exists, the fast path above takes over: any codebase question runs `map.mmd query` directly on the merged graph — no re-extraction, no size gate.
