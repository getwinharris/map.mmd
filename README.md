<p align="center">
  <a href="https://mapmmdlabs.ai"><img src="https://raw.githubusercontent.com/getwinharris/mapmmd/v4/docs/logo-text.svg" width="260" height="64" alt="map.mmd"/></a>
</p>


<p align="center">
  <a href="https://pypi.org/project/mapmmdy/"><img src="https://img.shields.io/pypi/v/mapmmdy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/mapmmdy"><img src="https://img.shields.io/pepy/dt/mapmmdy?color=blue&label=downloads" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/getwinharris"><img src="https://img.shields.io/badge/sponsor-getwinharris-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
</p>

<p align="center">
  <a href="https://star-history.com/#getwinharris/mapmmd&Date">
    <img src="https://api.star-history.com/svg?repos=getwinharris/mapmmd&type=Date" alt="Star History Chart" width="370"/>
  </a>
</p>

Type `/mapmmd` in your AI coding assistant and it maps your entire project — code, docs, PDFs, images, videos — into a knowledge graph you can query instead of grepping through files.

Works in Claude Code, Codex, OpenCode, Kilo Code, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, Amp, OpenClaw, Factory Droid, Trae, Hermes, Kimi Code, Kiro, Pi, Devin CLI, and Google Antigravity.

```
/mapmmd .
```

That's it. You get three files:

```
mapmmd-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

For a readable architecture page with Mermaid call-flow diagrams, run:

```bash
mapmmd export callflow-html
```

---

## Prerequisites

| Requirement | Minimum | Check | Install |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(recommended)* | any | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(alternative)* | any | `pipx --version` | `pip install pipx` |

**macOS quick install (Homebrew):**

```bash
brew install python@3.12 uv
```

**Windows quick install:**

```powershell
winget install astral-sh.uv
```

**Ubuntu/Debian:**

```bash
sudo apt install python3.12 python3-pip pipx
# or install uv:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Install

> **Official package:** The PyPI package is `mapmmdy` (double-y). Other `mapmmd*` packages on PyPI are not affiliated. The CLI command is still `mapmmd`.

**Step 1 — install the package:**

```bash
# Recommended (uv puts mapmmd on PATH automatically):
uv tool install mapmmdy

# Alternatives:
pipx install mapmmdy
pip install mapmmdy  # may need PATH setup — see note below
```

**Step 2 — register the skill with your AI assistant:**

```bash
mapmmd install
```

That's it. Open your AI assistant and type `/mapmmd .`

To install the assistant skill into the current repository instead of your user
profile, add `--project`:

```bash
mapmmd install --project
mapmmd install --project --platform codex
```

Project-scoped installs write under the current directory, for example
`.claude/skills/mapmmd/SKILL.md` or `.agents/skills/mapmmd/SKILL.md` (plus a
`references/` sidecar the skill loads on demand), and
print a `git add` hint for files that can be committed.
Per-platform commands that support project-scoped installs accept the same flag,
for example `mapmmd claude install --project` or `mapmmd codex install --project`.

> **PowerShell note:** Use `mapmmd .` not `/mapmmd .` — the leading slash is a path separator in PowerShell.

> **`mapmmd: command not found`?** Use `uv tool install mapmmdy` or `pipx install mapmmdy` — both put the CLI on PATH automatically. With plain `pip`, add `~/.local/bin` (Linux) or `~/Library/Python/3.x/bin` (Mac) to your PATH, or run `python -m mapmmd`.

> **Avoid `pip install` on Mac/Windows** if possible. The skill resolves Python at runtime from `mapmmd-out/.mapmmd_python`; if that points to a different environment than where `pip` installed the package, you'll get `ModuleNotFoundError: No module named 'mapmmd'`. `uv tool install` and `pipx install` isolate the package in their own env and avoid this entirely.

> **Git hooks and uv tool / pipx:** `mapmmd hook install` embeds the current interpreter path directly into the hook scripts at install time, so the post-commit hook fires correctly even in GUI git clients and CI runners where `~/.local/bin` is not on PATH. If you reinstall or upgrade mapmmd, re-run `mapmmd hook install` to refresh the embedded path.

### Pick your platform

| Platform | Install command |
|----------|----------------|
| Claude Code (Linux/Mac) | `mapmmd install` |
| Claude Code (Windows) | `mapmmd install` (auto-detected) or `mapmmd install --platform windows` |
| CodeBuddy | `mapmmd install --platform codebuddy` |
| Codex | `mapmmd install --platform codex` |
| OpenCode | `mapmmd install --platform opencode` |
| Kilo Code | `mapmmd install --platform kilo` |
| GitHub Copilot CLI | `mapmmd install --platform copilot` |
| VS Code Copilot Chat | `mapmmd vscode install` |
| Aider | `mapmmd install --platform aider` |
| OpenClaw | `mapmmd install --platform claw` |
| Factory Droid | `mapmmd install --platform droid` |
| Trae | `mapmmd install --platform trae` |
| Trae CN | `mapmmd install --platform trae-cn` |
| Gemini CLI | `mapmmd install --platform gemini` |
| Hermes | `mapmmd install --platform hermes` |
| Kimi Code | `mapmmd install --platform kimi` |
| Amp | `mapmmd amp install` |
| Agent Skills (cross-framework) | `mapmmd install --platform agents` (alias `--platform skills`) |
| Kiro IDE/CLI | `mapmmd kiro install` |
| Pi coding agent | `mapmmd install --platform pi` |
| Cursor | `mapmmd cursor install` |
| Devin CLI | `mapmmd devin install` |
| Google Antigravity | `mapmmd antigravity install` |

Codex users also need `multi_agent = true` under `[features]` in `~/.codex/config.toml` for parallel extraction. CodeBuddy uses the same Agent tool and PreToolUse hook mechanism as Claude Code. Factory Droid uses the `Task` tool for parallel subagent dispatch. OpenClaw and Aider use sequential extraction (parallel agent support is still early on those platforms). Trae uses the Agent tool for parallel subagent dispatch and does **not** support PreToolUse hooks — AGENTS.md is the always-on mechanism.

`--platform agents` (alias `--platform skills`) targets the generic cross-framework [Agent-Skills](https://github.com/anthropics/skills) locations: the spec's user-global `~/.agents/skills/` (read by `npx skills` and spec-compliant frameworks) for a global install, and `./.agents/skills/` for a project (`--project`) install. The bare `mapmmd install` stays single-platform (Claude Code) by design — use the named `agents` platform when you want the skill discoverable by any framework that reads `.agents/skills`.

> Codex uses `$mapmmd` instead of `/mapmmd`.

### Optional extras

Install only what you need:

| Extra | What it adds | Install |
|---|---|---|
| `pdf` | PDF extraction | `uv tool install "mapmmdy[pdf]"` |
| `office` | `.docx` and `.xlsx` support | `uv tool install "mapmmdy[office]"` |
| `google` | Google Sheets rendering | `uv tool install "mapmmdy[google]"` |
| `video` | Video/audio transcription (faster-whisper + yt-dlp) | `uv tool install "mapmmdy[video]"` |
| `mcp` | MCP stdio server | `uv tool install "mapmmdy[mcp]"` |
| `neo4j` | Neo4j push support | `uv tool install "mapmmdy[neo4j]"` |
| `falkordb` | FalkorDB push support | `uv tool install "mapmmdy[falkordb]"` |
| `svg` | SVG graph export | `uv tool install "mapmmdy[svg]"` |
| `leiden` | Leiden community detection (Python < 3.13 only) | `uv tool install "mapmmdy[leiden]"` |
| `ollama` | Ollama local inference | `uv tool install "mapmmdy[ollama]"` |
| `openai` | OpenAI / OpenAI-compatible APIs | `uv tool install "mapmmdy[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "mapmmdy[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, uses `ANTHROPIC_API_KEY`) | `uv tool install "mapmmdy[anthropic]"` |
| `bedrock` | AWS Bedrock (uses IAM, no API key) | `uv tool install "mapmmdy[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, uses `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "mapmmdy[openai]"` |
| `sql` | SQL schema extraction | `uv tool install "mapmmdy[sql]"` |
| `postgres` | Live PostgreSQL introspection (`--postgres DSN`) | `uv tool install "mapmmdy[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST extraction (may need a C compiler + `python3-dev` if no wheel matches your platform) | `uv tool install "mapmmdy[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST extraction | `uv tool install "mapmmdy[terraform]"` |
| `chinese` | Chinese query segmentation (jieba) | `uv tool install "mapmmdy[chinese]"` |
| `all` | Everything above | `uv tool install "mapmmdy[all]"` |

---

## Make your assistant always use the graph

Run this once in your project after building a graph:

| Platform | Command |
|----------|---------|
| Claude Code | `mapmmd claude install` |
| CodeBuddy | `mapmmd codebuddy install` |
| Codex | `mapmmd codex install` |
| OpenCode | `mapmmd opencode install` |
| Kilo Code | `mapmmd kilo install` |
| GitHub Copilot CLI | `mapmmd copilot install` |
| VS Code Copilot Chat | `mapmmd vscode install` |
| Aider | `mapmmd aider install` |
| OpenClaw | `mapmmd claw install` |
| Factory Droid | `mapmmd droid install` |
| Trae | `mapmmd trae install` |
| Trae CN | `mapmmd trae-cn install` |
| Cursor | `mapmmd cursor install` |
| Gemini CLI | `mapmmd gemini install` |
| Hermes | `mapmmd hermes install` |
| Kimi Code | `mapmmd install --platform kimi` |
| Amp | `mapmmd amp install` |
| Agent Skills (cross-framework) | `mapmmd agents install` (alias `mapmmd skills install`) |
| Kiro IDE/CLI | `mapmmd kiro install` |
| Pi coding agent | `mapmmd pi install` |
| Devin CLI | `mapmmd devin install` |
| Google Antigravity | `mapmmd antigravity install` |

This writes a small config file that tells your assistant to consult the knowledge graph for codebase questions — preferring scoped queries like `mapmmd query "<question>"` over reading the full report or grepping raw files. On platforms that support payload-bearing hooks (Claude Code, Gemini CLI), a hook fires automatically before search-style tool calls (and, on Claude Code, before reading source files one by one via the Read/Glob tools) and nudges your assistant toward the graph path. On the others (Codex, OpenCode, Cursor, etc.), the persistent instruction files (`AGENTS.md`, `.cursor/rules/`, etc.) provide the same query-first guidance. `GRAPH_REPORT.md` is still available for broad architecture review.

**CodeBuddy** does the same two things as Claude Code: writes a `CODEBUDDY.md` section telling CodeBuddy to read `mapmmd-out/GRAPH_REPORT.md` before answering architecture questions, and installs **PreToolUse hooks** (`.codebuddy/settings.json`) that fire before Bash search commands and file reads, nudging toward `mapmmd query` instead.

**Codex** writes to `AGENTS.md` and also installs a **PreToolUse hook** in `.codex/hooks.json` that fires before every Bash tool call — same always-on mechanism as Claude Code.

To remove mapmmd from all platforms at once: `mapmmd uninstall` (add `--purge` to also delete `mapmmd-out/`). Or use the per-platform command (e.g. `mapmmd claude uninstall`).

---

**Kilo Code** installs the map.mmd skill to `~/.config/kilo/skills/mapmmd/SKILL.md` and a native `/mapmmd` command to `~/.config/kilo/command/mapmmd.md`. `mapmmd kilo install` also writes `AGENTS.md` plus a native **`tool.execute.before` plugin** (`.kilo/plugins/mapmmd.js` + `.kilo/kilo.json` or `.kilo/kilo.jsonc` registration) so Kilo gets the same always-on graph reminder behavior through native `.kilo` config.

**Cursor** writes `.cursor/rules/mapmmd.mdc` with `alwaysApply: true` — Cursor includes it in every conversation automatically, no hook needed.

## What's in the report

- **God nodes** — the most-connected concepts in your project. Everything flows through these.
- **Surprising connections** — links between things that live in different files or modules. Ranked by how unexpected they are.
- **The "why"** — inline comments (`# NOTE:`, `# WHY:`, `# HACK:`), docstrings, and design rationale from docs are extracted as separate nodes linked to the code they explain.
- **Suggested questions** — 4–5 questions the graph is uniquely positioned to answer.
- **Confidence tags** — every inferred relationship is marked `EXTRACTED`, `INFERRED`, or `AMBIGUOUS`. You always know what was found vs guessed.

---

## What files it handles

| Type | Extensions |
|------|-----------|
| Code (36 tree-sitter grammars) | `.py .ts .js .jsx .tsx .mjs .go .rs .java .c .cpp .h .hpp .cu .cuh .rb .cs .kt .scala .php .swift .lua .luau .zig .ps1 .psm1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` requires `uv tool install mapmmdy[dm]`; CUDA `.cu`/`.cuh` reuse the C++ grammar) |
| Salesforce Apex | `.cls .trigger` (regex-based; classes, interfaces, enums, methods, triggers, SOQL/DML edges) |
| Terraform / HCL | `.tf .tfvars .hcl` (requires `uv tool install mapmmdy[terraform]`) |
| MCP configs | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extracts server nodes, package refs, env var requirements |
| Package manifests | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — one canonical package node per package (by name) plus `depends_on` edges, so a package referenced from many manifests is a single hub |
| Docs | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown `[text](./other.md)` links and `[[wikilinks]]` become `references` edges between docs) |
| Office | `.docx .xlsx` (requires `uv tool install mapmmdy[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; requires `gws` auth and `--google-workspace`; Sheets need `uv tool install mapmmdy[google]`) |
| PDFs | `.pdf` |
| Images | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` and more (requires `uv tool install mapmmdy[video]`) |
| YouTube / URLs | any video URL (requires `uv tool install mapmmdy[video]`) |

Code is extracted locally with no API calls (AST via tree-sitter). Everything else goes through your AI assistant's model API.

Google Drive for desktop `.gdoc`, `.gsheet`, and `.gslides` files are shortcut
pointers, not document content. To include native Google Docs, Sheets, and Slides
in a headless extraction, install and authenticate the
[`gws` CLI](https://github.com/googleworkspace/cli), then run:

```bash
uv tool install "mapmmdy[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
mapmmd extract ./docs --google-workspace
```

You can also set `GRAPHIFY_GOOGLE_WORKSPACE=1`. map.mmd exports shortcuts into
`mapmmd-out/converted/` as Markdown sidecars, then extracts those files.

---

## Common commands

```bash
/mapmmd .                        # build graph for current folder
/mapmmd ./docs --update          # re-extract only changed files
/mapmmd . --cluster-only         # rerun clustering without re-extracting
/mapmmd . --cluster-only --resolution 1.5      # more granular communities
/mapmmd . --cluster-only --exclude-hubs 99     # suppress utility super-hubs from god-node rankings
/mapmmd . --no-viz               # skip the HTML, just the report + JSON
/mapmmd . --wiki                 # build a markdown wiki from the graph
mapmmd export callflow-html      # Mermaid architecture/call-flow HTML (auto-regenerates on every git commit if hook is installed)

/mapmmd query "what connects auth to the database?"
/mapmmd path "UserService" "DatabasePool"
/mapmmd explain "RateLimiter"

/mapmmd add https://arxiv.org/abs/1706.03762   # fetch a paper and add it
/mapmmd add <youtube-url>                       # transcribe and add a video

mapmmd hook install              # auto-rebuild on git commit
mapmmd merge-graphs a.json b.json              # combine two graphs

mapmmd prs                       # PR dashboard: CI state, review status, worktree mapping
mapmmd prs 42                    # deep dive on PR #42 with graph impact
mapmmd prs --triage              # AI ranks your review queue (uses whatever backend is configured)
mapmmd prs --conflicts           # PRs sharing graph communities — merge-order risk
```

See the [full command reference](#full-command-reference) below.

---

## Ignoring files

Create a `.mapmmdignore` in your project root — same syntax as `.gitignore`, including `!` negation.

**`.gitignore` is respected automatically.** mapmmd reads the `.gitignore` in each directory. If a `.mapmmdignore` is also present, the two are **merged** — `.mapmmdignore` patterns are evaluated last, so they win on conflicts (including `!` negations). Adding a `.mapmmdignore` only ever excludes more; it never re-includes a file your `.gitignore` already excluded. Subdirectory scoping works the same way as git — an ignore file only affects its own subtree.

```
# .mapmmdignore
node_modules/
dist/
*.generated.py

# only index src/, ignore everything else
*
!src/
!src/**
```

---

## Team setup

`mapmmd-out/` is meant to be committed to git so everyone on the team starts with a map.

**Recommended `.gitignore` additions:**

```
mapmmd-out/cost.json        # local only
# mapmmd-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` is now portable — keys are stored as relative paths and re-anchored on load, so committing it is safe and avoids a full rebuild on first checkout.

**Workflow:**

1. One person runs `/mapmmd .` and commits `mapmmd-out/`.
2. Everyone pulls — their assistant reads the graph immediately.
3. Run `mapmmd hook install` to auto-rebuild after each commit (AST only, no API cost). This also sets up a git merge driver so `graph.json` is never left with conflict markers — two devs committing in parallel get their graphs union-merged automatically.
4. When docs or papers change, run `/mapmmd --update` to refresh those nodes.

---

## Using the graph directly

```bash
# query the graph from the terminal
mapmmd query "show the auth flow"
mapmmd query "what connects DigestAuth to Response?" --graph mapmmd-out/graph.json

# expose the graph as an MCP server (for repeated tool-call access)
python -m mapmmd.serve mapmmd-out/graph.json
python -m mapmmd.serve --graph mapmmd-out/graph.json  # --graph flag also accepted

# register with Kimi Code:
kimi mcp add --transport stdio mapmmd -- python -m mapmmd.serve mapmmd-out/graph.json

# or serve over HTTP so a whole team points at one URL (no local mapmmd needed):
python -m mapmmd.serve mapmmd-out/graph.json --transport http --port 8080
python -m mapmmd.serve mapmmd-out/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

The MCP server gives your assistant structured access: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Shared HTTP server

`--transport stdio` (the default) spawns one local server per developer. `--transport http` serves the same tools over the MCP Streamable HTTP transport, so a single shared process can serve the graph for the whole team — clients point their IDE MCP config at `http://<host>:8080/mcp` instead of running mapmmd locally.

| Flag | Default | Purpose |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport to serve on |
| `--host` | `127.0.0.1` | HTTP bind host (use `0.0.0.0` to expose beyond localhost) |
| `--port` | `8080` | HTTP bind port |
| `--api-key` | env `GRAPHIFY_API_KEY` | Require `Authorization: Bearer <key>` (or `X-API-Key`) |
| `--path` | `/mcp` | HTTP mount path |
| `--json-response` | off | Return plain JSON instead of SSE streams |
| `--stateless` | off | No per-session state (for load-balanced / CI deployments) |
| `--session-timeout` | `3600` | Reap idle stateful sessions after N seconds (`0` disables) |

The default `127.0.0.1` bind is loopback-only. Set `--host 0.0.0.0` **and** `--api-key` together when exposing on a shared host. Run it in a container:

```bash
docker build -t mapmmd .
docker run -p 8080:8080 -v "$(pwd)/mapmmd-out:/data" mapmmd \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux note:** Ubuntu ships `python3`, not `python`. Use a venv to avoid conflicts:
>
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "mapmmdy[mcp]"
> ```

---

## Environment variables

These are only needed for **headless / CI extraction** (`mapmmd extract`). When running via the `/mapmmd` skill inside your IDE, the model API is provided by your IDE session — no extra keys needed.

| Variable | Used for | When required |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude (Anthropic) backend | `--backend claude` |
| `ANTHROPIC_BASE_URL` | Anthropic-compatible endpoint URL (LiteLLM proxy, gateways, ...) | `--backend claude` (default: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Model name for the Claude backend — for custom endpoints, use the model name/alias your server exposes | `--backend claude` (default: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Google Gemini backend | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI or OpenAI-compatible APIs | `--backend openai` (local servers accept any non-empty value) |
| `OPENAI_BASE_URL` | OpenAI-compatible server URL (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (default: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Model name for the OpenAI backend — for self-hosted servers, use the model name/alias your server exposes (check its `/v1/models` endpoint), e.g. `LFM2.5-8B-A1B-UD-Q4_K_XL` for llama.cpp | `--backend openai` (default: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | DeepSeek backend | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Kimi Code backend | `--backend kimi` |
| `OLLAMA_BASE_URL` | Ollama local inference URL | `--backend ollama` (default: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Ollama model name | `--backend ollama` (default: auto-detect) |
| `GRAPHIFY_OLLAMA_NUM_CTX` | Override Ollama KV-cache window size | optional — auto-sized by default |
| `GRAPHIFY_OLLAMA_KEEP_ALIVE` | Minutes to keep Ollama model loaded | optional — set `0` to unload after each chunk |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure resource endpoint URL | `--backend azure` (required alongside API key) |
| `AZURE_OPENAI_API_VERSION` | Azure API version override | optional — default `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` or `GRAPHIFY_AZURE_MODEL` | Azure deployment name | optional — default `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standard credential chain | `--backend bedrock` (no API key, uses IAM) |
| `GRAPHIFY_MAX_WORKERS` | AST parallelism thread count | optional — also `--max-workers` flag |
| `GRAPHIFY_MAX_OUTPUT_TOKENS` | Raise output cap for dense corpora | optional — e.g. `32768` for large files |
| `GRAPHIFY_API_TIMEOUT` | Per-call timeout in seconds for HTTP, claude-cli, and Anthropic SDK backends (default: 600) | optional — also `--api-timeout` flag |
| `GRAPHIFY_FORCE` | Force graph rebuild even with fewer nodes | optional — also `--force` flag |
| `GRAPHIFY_GOOGLE_WORKSPACE` | Auto-enable Google Workspace export | optional — set to `1` |
| `GRAPHIFY_TRIAGE_BACKEND` | Backend for `mapmmd prs --triage` | optional — auto-detected from available keys |
| `GRAPHIFY_TRIAGE_MODEL` | Model override for triage | optional — e.g. `claude-opus-4-7` |
| `GRAPHIFY_QUERY_LOG` | Override query log path (default: `~/.cache/mapmmd-queries.log`) | optional — set to empty or `/dev/null` to silence |
| `GRAPHIFY_QUERY_LOG_DISABLE` | Set to `1` to disable query logging entirely | optional |
| `GRAPHIFY_QUERY_LOG_RESPONSES` | Set to `1` to also log full subgraph responses (off by default) | optional |
| `GRAPHIFY_MAX_GRAPH_BYTES` | Override the 512 MiB graph.json size cap — e.g. `700MB`, `2GB`, or plain bytes | optional — useful for very large corpora |
| `GRAPHIFY_LLM_TEMPERATURE` | Override LLM temperature for semantic extraction — e.g. `0.7`, or `none` to omit | optional — auto-omitted for o1/o3/o4/gpt-5 reasoning models |

---

## Privacy

- **Code files** — processed locally via tree-sitter. Nothing leaves your machine. A code-only corpus requires no API key — `mapmmd extract` runs fully offline.
- **Video / audio** — transcribed locally with faster-whisper. Nothing leaves your machine.
- **Docs, PDFs, images** — sent to your AI assistant for semantic extraction (via the `/mapmmd` skill, using whatever model your IDE session runs). Headless `mapmmd extract` requires `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), a running Ollama instance (`OLLAMA_BASE_URL`), AWS credentials via the standard provider chain (Bedrock - no API key needed, uses IAM), or the `claude` CLI binary (Claude Code - no API key needed, uses your Claude subscription). The `--dedup-llm` flag uses the same key.
- **Data residency** — `mapmmd extract` auto-detects which provider to use based on which API key is set (priority: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). For code with data-residency requirements, use `--backend ollama` (fully local) or pass an explicit `--backend` flag. Kimi (`MOONSHOT_API_KEY`) routes to Moonshot AI servers in China.
- No telemetry, no usage tracking, no analytics.
- **Query logging** — every `mapmmd query`, `mapmmd path`, `mapmmd explain`, and MCP `query_graph` call is logged to `~/.cache/mapmmd-queries.log` in JSON Lines format (timestamp, question, corpus, nodes returned, duration). Full subgraph responses are **not** stored by default. Set `GRAPHIFY_QUERY_LOG_DISABLE=1` to opt out, or `GRAPHIFY_QUERY_LOG=/dev/null` to silence without disabling the code path.

---

## Troubleshooting

**`mapmmd: command not found` after `pip install mapmmdy`**
pip installs scripts to a user bin directory that may not be on your PATH. Fix:

- macOS: add `~/Library/Python/3.x/bin` to your PATH in `~/.zshrc`
- Linux: add `~/.local/bin` to your PATH in `~/.bashrc`
- Or use `uv tool install mapmmdy` / `pipx install mapmmdy` — both manage PATH automatically.

**`python -m mapmmd` works but `mapmmd` command doesn't**
Your shell's PATH doesn't include the Python scripts directory. Use `uv` or `pipx` instead of plain `pip`.

**`/mapmmd .` causes "path not recognized" in PowerShell**
PowerShell treats a leading `/` as a path separator. Use `mapmmd .` (no slash) on Windows.

**mmd has fewer nodes after `--update` or rebuild**
If a refactor deleted files, the old nodes linger. Pass `--force` (or set `GRAPHIFY_FORCE=1`) to overwrite even when the rebuild has fewer nodes.

**mmd has duplicate nodes for the same entity (ghost duplicates)**
Ghost duplicates (same symbol appearing twice — once from AST extraction with a source location, once from semantic extraction without) are now automatically merged at build time. If you see this in a graph built before v0.8.33, run a full re-extract to clean up:

```bash
mapmmd extract . --force
```

**Ollama runs out of VRAM / context window exceeded**
The KV-cache window is auto-sized but may be too large for your GPU. Reduce it:

```bash
GRAPHIFY_OLLAMA_NUM_CTX=8192 mapmmd extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string` warnings**
The model's JSON response hit its output-token limit and was cut off mid-string. mapmmd auto-recovers (it splits the chunk and re-extracts the halves, and an oversized single document is first sliced at heading/paragraph boundaries so the whole file is still covered), so these warnings are noisy but not data loss. To reduce the churn, raise the output cap or shrink each chunk's output:

```bash
GRAPHIFY_MAX_OUTPUT_TOKENS=16384 mapmmd extract . --mode deep   # lift the cap
mapmmd extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```

With a cloud gateway like OpenRouter, prefer `--backend openai` (set `OPENAI_BASE_URL`) over the Ollama shim — it's a cleaner OpenAI-compatible path. If the model has its own max-output ceiling, lowering `--token-budget` is the reliable lever.

**mmd HTML is too large to open in a browser (>5000 nodes)**
Skip HTML generation and use the JSON directly:

```bash
mapmmd cluster-only ./my-project --no-viz
mapmmd query "..."
```

**`graph.json` has conflict markers after two devs commit at once**
Run `mapmmd hook install` — it sets up a git merge driver that union-merges `graph.json` automatically so conflicts never happen.

**Extraction returns empty nodes/edges for docs or PDFs**
Docs, PDFs, and images require an LLM call — code-only corpora need no key. Check that your API key is set and the backend is correct:

```bash
ANTHROPIC_API_KEY=sk-... mapmmd extract ./docs --backend claude
```

**Skill version mismatch warning in your IDE**
Your installed mapmmd version is different from the skill file. Update:

```bash
uv tool upgrade mapmmdy
mapmmd install  # overwrites the skill file
```

---

## Full command reference

```
/mapmmd                          # run on current directory
/mapmmd ./raw                    # run on a specific folder
/mapmmd ./raw --mode deep        # more aggressive relationship extraction
/mapmmd ./raw --update           # re-extract only changed files
/mapmmd ./raw --directed         # preserve edge direction
/mapmmd ./raw --cluster-only     # rerun clustering on existing graph
/mapmmd ./raw --no-viz           # skip HTML visualization
/mapmmd ./raw --obsidian         # generate Obsidian vault
/mapmmd ./raw --wiki             # build agent-crawlable markdown wiki
/mapmmd ./raw --svg              # export graph.svg
/mapmmd ./raw --graphml          # export for Gephi / yEd
/mapmmd ./raw --neo4j            # generate cypher.txt for Neo4j
/mapmmd ./raw --neo4j-push bolt://localhost:7687
/mapmmd ./raw --falkordb         # generate cypher.txt for FalkorDB
/mapmmd ./raw --falkordb-push falkordb://localhost:6379
/mapmmd ./raw --watch            # auto-sync as files change
/mapmmd ./raw --mcp              # start MCP stdio server

/mapmmd add https://arxiv.org/abs/1706.03762
/mapmmd add <video-url>
/mapmmd add https://... --author "Name" --contributor "Name"

/mapmmd query "what connects attention to the optimizer?"
/mapmmd query "..." --dfs --budget 1500
/mapmmd path "DigestAuth" "Response"
/mapmmd explain "SwinTransformer"

mapmmd save-result --question "Q" --answer "A" --nodes Foo Bar --outcome useful   # record how a Q&A turned out (work memory; outcome ∈ useful|dead_end|corrected)
mapmmd reflect                   # aggregate mapmmd-out/memory/ outcomes into reflections/LESSONS.md
mapmmd reflect --if-stale        # no-op when LESSONS.md is already newer than every input (cheap to run each session)
mapmmd reflect --out docs/LESSONS.md    # write the lessons doc somewhere else
mapmmd reflect --graph mapmmd-out/graph.json  # also group lessons by community

mapmmd uninstall                 # remove from all platforms in one shot
mapmmd uninstall --purge         # also delete mapmmd-out/
mapmmd uninstall --project --platform codex  # remove project-scoped install files only

mapmmd hook install              # post-commit + post-checkout hooks
mapmmd hook uninstall
mapmmd hook status

# always-on assistant instructions - platform-specific
mapmmd claude install            # CLAUDE.md + PreToolUse hook (Claude Code)
mapmmd claude uninstall
mapmmd codebuddy install         # CODEBUDDY.md + PreToolUse hook (CodeBuddy)
mapmmd codebuddy uninstall
mapmmd codex install             # AGENTS.md + PreToolUse hook in .codex/hooks.json (Codex)
mapmmd opencode install          # AGENTS.md + tool.execute.before plugin (OpenCode)
mapmmd kilo install              # native Kilo skill + /mapmmd command + AGENTS.md + .kilo plugin
mapmmd kilo uninstall
mapmmd cursor install            # .cursor/rules/mapmmd.mdc (Cursor)
mapmmd cursor uninstall
mapmmd gemini install            # GEMINI.md + BeforeTool hook (Gemini CLI)
mapmmd gemini uninstall
mapmmd copilot install           # skill file (GitHub Copilot CLI)
mapmmd copilot uninstall
mapmmd aider install             # AGENTS.md (Aider)
mapmmd aider uninstall
mapmmd claw install              # AGENTS.md (OpenClaw)
mapmmd claw uninstall
mapmmd droid install             # AGENTS.md (Factory Droid)
mapmmd droid uninstall
mapmmd trae install              # AGENTS.md (Trae)
mapmmd trae uninstall
mapmmd trae-cn install           # AGENTS.md (Trae CN)
mapmmd trae-cn uninstall
mapmmd hermes install             # AGENTS.md + ~/.hermes/skills/ (Hermes)
mapmmd hermes uninstall
mapmmd amp install               # skill file (Amp)
mapmmd amp uninstall
mapmmd agents install            # ~/.agents/skills/ + AGENTS.md (cross-framework; alias: mapmmd skills)
mapmmd agents uninstall
mapmmd kiro install               # .kiro/skills/ + .kiro/steering/mapmmd.md (Kiro IDE/CLI)
mapmmd kiro uninstall
mapmmd pi install                # skill file (Pi coding agent)
mapmmd pi uninstall
mapmmd devin install             # skill file + .windsurf/rules/mapmmd.md (Devin CLI)
mapmmd devin uninstall
mapmmd antigravity install       # .agents/rules + .agents/workflows (Google Antigravity)
mapmmd antigravity uninstall

mapmmd extract ./docs                        # headless LLM extraction for CI (no IDE needed)
mapmmd extract ./docs --backend gemini       # explicit backend: gemini, kimi, claude, openai, deepseek, ollama, bedrock, or claude-cli
mapmmd extract ./docs --backend gemini --model gemini-3.1-pro-preview
mapmmd extract ./docs --backend ollama       # local Ollama (set OLLAMA_BASE_URL / OLLAMA_MODEL) - no API key needed for loopback
OPENAI_BASE_URL=http://localhost:8080/v1 OPENAI_MODEL=my-model mapmmd extract ./docs --backend openai   # any OpenAI-compatible server (llama.cpp, vLLM, LM Studio)
ANTHROPIC_BASE_URL=http://localhost:4000 ANTHROPIC_MODEL=my-model mapmmd extract ./docs --backend claude   # any Anthropic-compatible endpoint (LiteLLM proxy, gateways)
GRAPHIFY_OLLAMA_NUM_CTX=32768 mapmmd extract ./docs --backend ollama   # override KV-cache window (auto-sized by default)
GRAPHIFY_OLLAMA_KEEP_ALIVE=0 mapmmd extract ./docs --backend ollama    # unload model after each chunk (saves VRAM on small GPUs)
mapmmd extract ./docs --backend bedrock      # AWS Bedrock via IAM - no API key, uses AWS credential chain
mapmmd extract ./docs --backend claude-cli   # route through Claude Code CLI - no API key, uses your Claude subscription
mapmmd extract ./docs --backend azure        # Azure OpenAI (set AZURE_OPENAI_API_KEY + AZURE_OPENAI_ENDPOINT)
mapmmd extract ./docs --max-workers 16       # AST parallelism (also GRAPHIFY_MAX_WORKERS)
mapmmd extract --postgres "postgresql://user:pass@host/db"   # introspect live PostgreSQL schema directly
mapmmd extract ./my-workspace --cargo        # introspect Rust Cargo workspace dependencies directly
mapmmd extract ./docs --token-budget 30000   # smaller semantic chunks for local/small models
mapmmd extract ./docs --max-concurrency 2    # fewer parallel LLM calls (useful for local inference)
mapmmd extract ./docs --api-timeout 900      # longer HTTP timeout for slow local models (default 600s)
mapmmd extract ./docs --google-workspace     # export .gdoc/.gsheet/.gslides via gws before extraction
mapmmd extract ./docs --mode deep            # richer semantic extraction via extended system prompt
mapmmd extract ./docs --no-cluster           # raw extraction only, skip clustering
mapmmd extract ./docs --force                # overwrite graph.json even if new graph has fewer nodes (use after refactors or to clear ghost duplicates)
mapmmd extract ./docs --dedup-llm            # LLM tiebreaker for ambiguous entity pairs (uses same API key)
mapmmd extract ./docs --global --as myrepo   # extract and register into the cross-project global graph
GRAPHIFY_MAX_OUTPUT_TOKENS=32768 mapmmd extract ./docs --backend claude  # raise output cap for dense corpora

mapmmd export callflow-html                       # mapmmd-out/<project>-callflow.html
mapmmd export callflow-html --max-sections 8      # cap generated architecture sections
mapmmd export callflow-html --output docs/arch.html
mapmmd export callflow-html ./some-repo/mapmmd-out

mapmmd global add mapmmd-out/graph.json myrepo   # register a project graph into ~/.mapmmd/global.json
mapmmd global remove myrepo                         # remove a project from the global graph
mapmmd global list                                  # show all registered repos + node/edge counts
mapmmd global path                                  # print path to the global graph file

mapmmd prs                              # PR dashboard: CI, review, worktree, graph impact
mapmmd prs 42                           # deep dive on PR #42
mapmmd prs --triage                     # AI triage ranking (auto-detects backend from env)
mapmmd prs --worktrees                  # worktree → branch → PR mapping
mapmmd prs --conflicts                  # PRs sharing graph communities (merge-order risk)
mapmmd prs --base main                  # filter to PRs targeting a specific base branch
mapmmd prs --repo owner/repo            # run against a different GitHub repo
GRAPHIFY_TRIAGE_BACKEND=kimi mapmmd prs --triage   # use a specific backend for triage

mapmmd clone https://github.com/karpathy/nanoGPT
mapmmd merge-graphs a.json b.json --out merged.json
mapmmd --version                                    # print installed version
mapmmd watch ./src
mapmmd check-update ./src
mapmmd update ./src
mapmmd update ./src --no-cluster  # skip reclustering, write raw AST graph only
mapmmd update ./src --force       # overwrite even if new graph has fewer nodes
mapmmd cluster-only ./my-project
mapmmd cluster-only ./my-project --graph path/to/graph.json  # custom graph location
mapmmd cluster-only ./my-project --max-concurrency 16 --batch-size 200  # parallel community labeling (large graphs)
mapmmd cluster-only ./my-project --resolution 1.5            # more, smaller communities
mapmmd cluster-only ./my-project --exclude-hubs 99           # exclude p99 degree nodes from partitioning
mapmmd cluster-only ./my-project --no-label                  # keep "Community N" placeholders
mapmmd cluster-only ./my-project --backend=gemini            # backend for community naming
mapmmd cluster-only ./my-project --backend=gemini --model gemini-2.5-pro  # specific model
mapmmd label ./my-project                                    # (re)name communities with the configured backend
mapmmd label ./my-project --backend=openai --model gpt-4o   # force a specific backend and model
```

> **Community names:** inside an agent (Claude Code, Gemini CLI) the agent names communities itself. When you run the bare CLI, `cluster-only` auto-names them with the configured backend (built-in or custom OpenAI-compatible provider) — pass `--no-label` to keep `Community N`, or run `mapmmd label` to (re)generate names on demand.

---

## Learn more

- [How it works](docs/how-it-works.md) — the extraction pipeline, community detection, confidence scoring, benchmarks
- [ARCHITECTURE.md](ARCHITECTURE.md) — module breakdown, how to add a language
- [Optional integrations](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite

---

## Built on mapmmd — Penpax

[**Penpax**](https://mapmmdlabs.ai) is the always-on layer built on top of mapmmd — it applies the same graph approach to your entire working life: meetings, browser history, emails, files, and code, updating continuously in the background.

Built for people whose work lives across hundreds of conversations and documents they can never fully reconstruct. No cloud, fully on-device.

**Free trial launching soon.** [Join the waitlist →](https://mapmmdlabs.ai)

---

<details>
<summary>Contributing</summary>

### Development setup

The project uses [uv](https://docs.astral.sh/uv/) for dev workflow. Install it once, then:

```bash
git clone https://github.com/getwinharris/mapmmd.git
cd mapmmd
git checkout v8                        # active development branch

# Create the project venv and install mapmmd + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verify the editable install:

```bash
uv run mapmmd --version
uv run python -c "import mapmmd; print(mapmmd.__file__)"
```

### Running tests

```bash
uv run pytest tests/ -q                # run the full suite
uv run pytest tests/test_extract.py -q # one module
uv run pytest tests/ -q -k "python"    # filter by name
```

> macOS note: the test suite includes both `sample.f90` and `sample.F90` fixtures. These collide on case-insensitive HFS+ / APFS file systems. Run on Linux or in a Docker container if you need to test both Fortran variants simultaneously.

### Git workflow

- Active development happens on the `v8` branch.
- Commit style: `fix: <description>` / `feat: <description>` / `docs: <description>`
- Before opening a PR, run `uv run pytest tests/ -q` and confirm it passes.
- Add a fixture file to `tests/fixtures/` and tests to `tests/test_languages.py` for any new language extractor.

### What to contribute

**Worked examples** are the most useful contribution. Run `/mapmmd` on a real corpus, save the output to `worked/{slug}/`, write an honest `review.md` covering what the graph got right and wrong, and open a PR.

**Extraction bugs** — open an issue with the input file, the cache entry (`mapmmd-out/cache/`), and what was missed or wrong.

See [ARCHITECTURE.md](ARCHITECTURE.md) for module responsibilities and how to add a language.

</details>
