<p align="center">
  <a href="https://map.mmdlabs.ai"><img src="https://raw.githubusercontent.com/getwinharris/map.mmd/v4/docs/logo-text.svg" width="260" height="64" alt="map.mmd"/></a>
</p>

<p align="center">
  🇺🇸 <a href="README.md">English</a> | 🇨🇳 <a href="docs/translations/README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="docs/translations/README.ja-JP.md">日本語</a> | 🇰🇷 <a href="docs/translations/README.ko-KR.md">한국어</a> | 🇩🇪 <a href="docs/translations/README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="docs/translations/README.fr-FR.md">Français</a> | 🇪🇸 <a href="docs/translations/README.es-ES.md">Español</a> | 🇮🇳 <a href="docs/translations/README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="docs/translations/README.pt-BR.md">Português</a> | 🇷🇺 <a href="docs/translations/README.ru-RU.md">Русский</a> | 🇸🇦 <a href="docs/translations/README.ar-SA.md">العربية</a> | 🇮🇷 <a href="docs/translations/README.fa-IR.md">فارسی</a> | 🇮🇹 <a href="docs/translations/README.it-IT.md">Italiano</a> | 🇵🇱 <a href="docs/translations/README.pl-PL.md">Polski</a> | 🇳🇱 <a href="docs/translations/README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="docs/translations/README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="docs/translations/README.uk-UA.md">Українська</a> | 🇻🇳 <a href="docs/translations/README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="docs/translations/README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="docs/translations/README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="docs/translations/README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="docs/translations/README.ro-RO.md">Română</a> | 🇨🇿 <a href="docs/translations/README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="docs/translations/README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="docs/translations/README.da-DK.md">Dansk</a> | 🇳🇴 <a href="docs/translations/README.no-NO.md">Norsk</a> | 🇭🇺 <a href="docs/translations/README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="docs/translations/README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="docs/translations/README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="docs/translations/README.zh-TW.md">繁體中文</a> | 🇵🇭 <a href="docs/translations/README.fil-PH.md">Filipino</a>
</p>

<p align="center">
  <a href="https://www.ycombinator.com/companies/map.mmd"><img src="https://img.shields.io/badge/Y%20Combinator-S26-F0652F?style=flat&logo=ycombinator&logoColor=white" alt="YC S26"/></a>
  <a href="https://safishamsi.gumroad.com/l/qetvlo"><img src="https://img.shields.io/badge/Book-The%20Memory%20Layer-2ea44f?style=flat&logo=gitbook&logoColor=white" alt="The Memory Layer"/></a>
  <a href="https://github.com/getwinharris/map.mmd/actions/workflows/ci.yml"><img src="https://github.com/getwinharris/map.mmd/actions/workflows/ci.yml/badge.svg?branch=v8" alt="CI"/></a>
  <a href="https://pypi.org/project/map-mmd/"><img src="https://img.shields.io/pypi/v/map-mmd" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/map-mmd"><img src="https://img.shields.io/pepy/dt/map-mmd?color=blue&label=downloads" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/in/safi-shamsi"><img src="https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin" alt="LinkedIn"/></a>
  <a href="https://x.com/map-mmd"><img src="https://img.shields.io/badge/X-map-mmd-000000?logo=x&logoColor=white" alt="X"/></a>
</p>

<p align="center">
  <a href="https://star-history.com/#getwinharris/map.mmd&Date">
    <img src="https://api.star-history.com/svg?repos=getwinharris/map.mmd&type=Date" alt="Star History Chart" width="370"/>
  </a>
</p>

Type `/map.mmd` in your AI coding assistant and it maps your entire project — code, docs, PDFs, images, videos — into a knowledge graph you can query instead of grepping through files.

Works in Claude Code, Codex, OpenCode, Kilo Code, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, Amp, OpenClaw, Factory Droid, Trae, Hermes, Kimi Code, Kiro, Pi, Devin CLI, and Google Antigravity.

```
/map.mmd .
```

That's it. You get three files:

```
map.mmd-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

For a readable architecture page with Mermaid call-flow diagrams, run:

```bash
map.mmd export callflow-html
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

> **Official package:** The PyPI package is `map-mmd` (double-y). Other `map.mmd*` packages on PyPI are not affiliated. The CLI command is still `map.mmd`.

**Step 1 — install the package:**

```bash
# Recommended (uv puts map.mmd on PATH automatically):
uv tool install map-mmd

# Alternatives:
pipx install map-mmd
pip install map-mmd  # may need PATH setup — see note below
```

**Step 2 — register the skill with your AI assistant:**

```bash
map.mmd install
```

That's it. Open your AI assistant and type `/map.mmd .`

To install the assistant skill into the current repository instead of your user
profile, add `--project`:

```bash
map.mmd install --project
map.mmd install --project --platform codex
```

Project-scoped installs write under the current directory, for example
`.claude/skills/map.mmd/SKILL.md` or `.agents/skills/map.mmd/SKILL.md` (plus a
`references/` sidecar the skill loads on demand), and
print a `git add` hint for files that can be committed.
Per-platform commands that support project-scoped installs accept the same flag,
for example `map.mmd claude install --project` or `map.mmd codex install --project`.

> **PowerShell note:** Use `map.mmd .` not `/map.mmd .` — the leading slash is a path separator in PowerShell.

> **`map.mmd: command not found`?** Use `uv tool install map-mmd` or `pipx install map-mmd` — both put the CLI on PATH automatically. With plain `pip`, add `~/.local/bin` (Linux) or `~/Library/Python/3.x/bin` (Mac) to your PATH, or run `python -m map.mmd`.

> **Avoid `pip install` on Mac/Windows** if possible. The skill resolves Python at runtime from `map.mmd-out/.map.mmd_python`; if that points to a different environment than where `pip` installed the package, you'll get `ModuleNotFoundError: No module named 'map.mmd'`. `uv tool install` and `pipx install` isolate the package in their own env and avoid this entirely.

> **Git hooks and uv tool / pipx:** `map.mmd hook install` embeds the current interpreter path directly into the hook scripts at install time, so the post-commit hook fires correctly even in GUI git clients and CI runners where `~/.local/bin` is not on PATH. If you reinstall or upgrade map.mmd, re-run `map.mmd hook install` to refresh the embedded path.

### Pick your platform

| Platform | Install command |
|----------|----------------|
| Claude Code (Linux/Mac) | `map.mmd install` |
| Claude Code (Windows) | `map.mmd install` (auto-detected) or `map.mmd install --platform windows` |
| CodeBuddy | `map.mmd install --platform codebuddy` |
| Codex | `map.mmd install --platform codex` |
| OpenCode | `map.mmd install --platform opencode` |
| Kilo Code | `map.mmd install --platform kilo` |
| GitHub Copilot CLI | `map.mmd install --platform copilot` |
| VS Code Copilot Chat | `map.mmd vscode install` |
| Aider | `map.mmd install --platform aider` |
| OpenClaw | `map.mmd install --platform claw` |
| Factory Droid | `map.mmd install --platform droid` |
| Trae | `map.mmd install --platform trae` |
| Trae CN | `map.mmd install --platform trae-cn` |
| Gemini CLI | `map.mmd install --platform gemini` |
| Hermes | `map.mmd install --platform hermes` |
| Kimi Code | `map.mmd install --platform kimi` |
| Amp | `map.mmd amp install` |
| Agent Skills (cross-framework) | `map.mmd install --platform agents` (alias `--platform skills`) |
| Kiro IDE/CLI | `map.mmd kiro install` |
| Pi coding agent | `map.mmd install --platform pi` |
| Cursor | `map.mmd cursor install` |
| Devin CLI | `map.mmd devin install` |
| Google Antigravity | `map.mmd antigravity install` |

Codex users also need `multi_agent = true` under `[features]` in `~/.codex/config.toml` for parallel extraction. CodeBuddy uses the same Agent tool and PreToolUse hook mechanism as Claude Code. Factory Droid uses the `Task` tool for parallel subagent dispatch. OpenClaw and Aider use sequential extraction (parallel agent support is still early on those platforms). Trae uses the Agent tool for parallel subagent dispatch and does **not** support PreToolUse hooks — AGENTS.md is the always-on mechanism.

`--platform agents` (alias `--platform skills`) targets the generic cross-framework [Agent-Skills](https://github.com/anthropics/skills) locations: the spec's user-global `~/.agents/skills/` (read by `npx skills` and spec-compliant frameworks) for a global install, and `./.agents/skills/` for a project (`--project`) install. The bare `map.mmd install` stays single-platform (Claude Code) by design — use the named `agents` platform when you want the skill discoverable by any framework that reads `.agents/skills`.

> Codex uses `$map.mmd` instead of `/map.mmd`.

### Optional extras

Install only what you need:

| Extra | What it adds | Install |
|---|---|---|
| `pdf` | PDF extraction | `uv tool install "map-mmd[pdf]"` |
| `office` | `.docx` and `.xlsx` support | `uv tool install "map-mmd[office]"` |
| `google` | Google Sheets rendering | `uv tool install "map-mmd[google]"` |
| `video` | Video/audio transcription (faster-whisper + yt-dlp) | `uv tool install "map-mmd[video]"` |
| `mcp` | MCP stdio server | `uv tool install "map-mmd[mcp]"` |
| `neo4j` | Neo4j push support | `uv tool install "map-mmd[neo4j]"` |
| `falkordb` | FalkorDB push support | `uv tool install "map-mmd[falkordb]"` |
| `svg` | SVG graph export | `uv tool install "map-mmd[svg]"` |
| `leiden` | Leiden community detection (Python < 3.13 only) | `uv tool install "map-mmd[leiden]"` |
| `ollama` | Ollama local inference | `uv tool install "map-mmd[ollama]"` |
| `openai` | OpenAI / OpenAI-compatible APIs | `uv tool install "map-mmd[openai]"` |
| `gemini` | Google Gemini API | `uv tool install "map-mmd[gemini]"` |
| `anthropic` | Anthropic Claude API (`--backend claude`, uses `ANTHROPIC_API_KEY`) | `uv tool install "map-mmd[anthropic]"` |
| `bedrock` | AWS Bedrock (uses IAM, no API key) | `uv tool install "map-mmd[bedrock]"` |
| `azure` | Azure OpenAI Service (`--backend azure`, uses `AZURE_OPENAI_API_KEY` + `AZURE_OPENAI_ENDPOINT`) | `uv tool install "map-mmd[openai]"` |
| `sql` | SQL schema extraction | `uv tool install "map-mmd[sql]"` |
| `postgres` | Live PostgreSQL introspection (`--postgres DSN`) | `uv tool install "map-mmd[postgres]"` |
| `dm` | BYOND DreamMaker `.dm`/`.dme` AST extraction (may need a C compiler + `python3-dev` if no wheel matches your platform) | `uv tool install "map-mmd[dm]"` |
| `terraform` | Terraform / HCL `.tf`/`.tfvars`/`.hcl` AST extraction | `uv tool install "map-mmd[terraform]"` |
| `chinese` | Chinese query segmentation (jieba) | `uv tool install "map-mmd[chinese]"` |
| `all` | Everything above | `uv tool install "map-mmd[all]"` |

---

## Make your assistant always use the graph

Run this once in your project after building a graph:

| Platform | Command |
|----------|---------|
| Claude Code | `map.mmd claude install` |
| CodeBuddy | `map.mmd codebuddy install` |
| Codex | `map.mmd codex install` |
| OpenCode | `map.mmd opencode install` |
| Kilo Code | `map.mmd kilo install` |
| GitHub Copilot CLI | `map.mmd copilot install` |
| VS Code Copilot Chat | `map.mmd vscode install` |
| Aider | `map.mmd aider install` |
| OpenClaw | `map.mmd claw install` |
| Factory Droid | `map.mmd droid install` |
| Trae | `map.mmd trae install` |
| Trae CN | `map.mmd trae-cn install` |
| Cursor | `map.mmd cursor install` |
| Gemini CLI | `map.mmd gemini install` |
| Hermes | `map.mmd hermes install` |
| Kimi Code | `map.mmd install --platform kimi` |
| Amp | `map.mmd amp install` |
| Agent Skills (cross-framework) | `map.mmd agents install` (alias `map.mmd skills install`) |
| Kiro IDE/CLI | `map.mmd kiro install` |
| Pi coding agent | `map.mmd pi install` |
| Devin CLI | `map.mmd devin install` |
| Google Antigravity | `map.mmd antigravity install` |

This writes a small config file that tells your assistant to consult the knowledge graph for codebase questions — preferring scoped queries like `map.mmd query "<question>"` over reading the full report or grepping raw files. On platforms that support payload-bearing hooks (Claude Code, Gemini CLI), a hook fires automatically before search-style tool calls (and, on Claude Code, before reading source files one by one via the Read/Glob tools) and nudges your assistant toward the graph path. On the others (Codex, OpenCode, Cursor, etc.), the persistent instruction files (`AGENTS.md`, `.cursor/rules/`, etc.) provide the same query-first guidance. `GRAPH_REPORT.md` is still available for broad architecture review.

**CodeBuddy** does the same two things as Claude Code: writes a `CODEBUDDY.md` section telling CodeBuddy to read `map.mmd-out/GRAPH_REPORT.md` before answering architecture questions, and installs **PreToolUse hooks** (`.codebuddy/settings.json`) that fire before Bash search commands and file reads, nudging toward `map.mmd query` instead.

**Codex** writes to `AGENTS.md` and also installs a **PreToolUse hook** in `.codex/hooks.json` that fires before every Bash tool call — same always-on mechanism as Claude Code.

To remove map.mmd from all platforms at once: `map.mmd uninstall` (add `--purge` to also delete `map.mmd-out/`). Or use the per-platform command (e.g. `map.mmd claude uninstall`).

---

**Kilo Code** installs the map.mmd skill to `~/.config/kilo/skills/map.mmd/SKILL.md` and a native `/map.mmd` command to `~/.config/kilo/command/map.mmd.md`. `map.mmd kilo install` also writes `AGENTS.md` plus a native **`tool.execute.before` plugin** (`.kilo/plugins/map.mmd.js` + `.kilo/kilo.json` or `.kilo/kilo.jsonc` registration) so Kilo gets the same always-on graph reminder behavior through native `.kilo` config.

**Cursor** writes `.cursor/rules/map.mmd.mdc` with `alwaysApply: true` — Cursor includes it in every conversation automatically, no hook needed.

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
| Code (36 tree-sitter grammars) | `.py .ts .js .jsx .tsx .mjs .go .rs .java .c .cpp .h .hpp .cu .cuh .rb .cs .kt .scala .php .swift .lua .luau .zig .ps1 .psm1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .svh .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json .dm .dme .dmi .dmm .dmf .sln .slnx .csproj .fsproj .vbproj .xaml .razor .cshtml` (`.dm`/`.dme` requires `uv tool install map-mmd[dm]`; CUDA `.cu`/`.cuh` reuse the C++ grammar) |
| Salesforce Apex | `.cls .trigger` (regex-based; classes, interfaces, enums, methods, triggers, SOQL/DML edges) |
| Terraform / HCL | `.tf .tfvars .hcl` (requires `uv tool install map-mmd[terraform]`) |
| MCP configs | `.mcp.json` `mcp.json` `mcp_servers.json` `claude_desktop_config.json` — extracts server nodes, package refs, env var requirements |
| Package manifests | `apm.yml` `pyproject.toml` `go.mod` `pom.xml` — one canonical package node per package (by name) plus `depends_on` edges, so a package referenced from many manifests is a single hub |
| Docs | `.md .mdx .qmd .html .txt .rst .yaml .yml` (markdown `[text](./other.md)` links and `[[wikilinks]]` become `references` edges between docs) |
| Office | `.docx .xlsx` (requires `uv tool install map-mmd[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (opt-in; requires `gws` auth and `--google-workspace`; Sheets need `uv tool install map-mmd[google]`) |
| PDFs | `.pdf` |
| Images | `.png .jpg .webp .gif` |
| Video / Audio | `.mp4 .mov .mp3 .wav` and more (requires `uv tool install map-mmd[video]`) |
| YouTube / URLs | any video URL (requires `uv tool install map-mmd[video]`) |

Code is extracted locally with no API calls (AST via tree-sitter). Everything else goes through your AI assistant's model API.

Google Drive for desktop `.gdoc`, `.gsheet`, and `.gslides` files are shortcut
pointers, not document content. To include native Google Docs, Sheets, and Slides
in a headless extraction, install and authenticate the
[`gws` CLI](https://github.com/googleworkspace/cli), then run:

```bash
uv tool install "map-mmd[google]"  # needed for Google Sheets table rendering
gws auth login -s drive
map.mmd extract ./docs --google-workspace
```

You can also set `MAP_MMD_GOOGLE_WORKSPACE=1`. map.mmd exports shortcuts into
`map.mmd-out/converted/` as Markdown sidecars, then extracts those files.

---

## Common commands

```bash
/map.mmd .                        # build graph for current folder
/map.mmd ./docs --update          # re-extract only changed files
/map.mmd . --cluster-only         # rerun clustering without re-extracting
/map.mmd . --cluster-only --resolution 1.5      # more granular communities
/map.mmd . --cluster-only --exclude-hubs 99     # suppress utility super-hubs from god-node rankings
/map.mmd . --no-viz               # skip the HTML, just the report + JSON
/map.mmd . --wiki                 # build a markdown wiki from the graph
map.mmd export callflow-html      # Mermaid architecture/call-flow HTML (auto-regenerates on every git commit if hook is installed)

/map.mmd query "what connects auth to the database?"
/map.mmd path "UserService" "DatabasePool"
/map.mmd explain "RateLimiter"

/map.mmd add https://arxiv.org/abs/1706.03762   # fetch a paper and add it
/map.mmd add <youtube-url>                       # transcribe and add a video

map.mmd hook install              # auto-rebuild on git commit
map.mmd merge-graphs a.json b.json              # combine two graphs

map.mmd prs                       # PR dashboard: CI state, review status, worktree mapping
map.mmd prs 42                    # deep dive on PR #42 with graph impact
map.mmd prs --triage              # AI ranks your review queue (uses whatever backend is configured)
map.mmd prs --conflicts           # PRs sharing graph communities — merge-order risk
```

See the [full command reference](#full-command-reference) below.

---

## Ignoring files

Create a `.map.mmdignore` in your project root — same syntax as `.gitignore`, including `!` negation.

**`.gitignore` is respected automatically.** map.mmd reads the `.gitignore` in each directory. If a `.map.mmdignore` is also present, the two are **merged** — `.map.mmdignore` patterns are evaluated last, so they win on conflicts (including `!` negations). Adding a `.map.mmdignore` only ever excludes more; it never re-includes a file your `.gitignore` already excluded. Subdirectory scoping works the same way as git — an ignore file only affects its own subtree.

```
# .map.mmdignore
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

`map.mmd-out/` is meant to be committed to git so everyone on the team starts with a map.

**Recommended `.gitignore` additions:**
```
map.mmd-out/cost.json        # local only
# map.mmd-out/cache/         # optional: commit for speed, skip to keep repo small
```

> `manifest.json` is now portable — keys are stored as relative paths and re-anchored on load, so committing it is safe and avoids a full rebuild on first checkout.

**Workflow:**
1. One person runs `/map.mmd .` and commits `map.mmd-out/`.
2. Everyone pulls — their assistant reads the graph immediately.
3. Run `map.mmd hook install` to auto-rebuild after each commit (AST only, no API cost). This also sets up a git merge driver so `graph.json` is never left with conflict markers — two devs committing in parallel get their graphs union-merged automatically.
4. When docs or papers change, run `/map.mmd --update` to refresh those nodes.

---

## Using the graph directly

```bash
# query the graph from the terminal
map.mmd query "show the auth flow"
map.mmd query "what connects DigestAuth to Response?" --graph map.mmd-out/graph.json

# expose the graph as an MCP server (for repeated tool-call access)
python -m map.mmd.serve map.mmd-out/graph.json
python -m map.mmd.serve --graph map.mmd-out/graph.json  # --graph flag also accepted

# register with Kimi Code:
kimi mcp add --transport stdio map.mmd -- python -m map.mmd.serve map.mmd-out/graph.json

# or serve over HTTP so a whole team points at one URL (no local map.mmd needed):
python -m map.mmd.serve map.mmd-out/graph.json --transport http --port 8080
python -m map.mmd.serve map.mmd-out/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

The MCP server gives your assistant structured access: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

### Shared HTTP server

`--transport stdio` (the default) spawns one local server per developer. `--transport http` serves the same tools over the MCP Streamable HTTP transport, so a single shared process can serve the graph for the whole team — clients point their IDE MCP config at `http://<host>:8080/mcp` instead of running map.mmd locally.

| Flag | Default | Purpose |
|---|---|---|
| `--transport {stdio,http}` | `stdio` | Transport to serve on |
| `--host` | `127.0.0.1` | HTTP bind host (use `0.0.0.0` to expose beyond localhost) |
| `--port` | `8080` | HTTP bind port |
| `--api-key` | env `MAP_MMD_API_KEY` | Require `Authorization: Bearer <key>` (or `X-API-Key`) |
| `--path` | `/mcp` | HTTP mount path |
| `--json-response` | off | Return plain JSON instead of SSE streams |
| `--stateless` | off | No per-session state (for load-balanced / CI deployments) |
| `--session-timeout` | `3600` | Reap idle stateful sessions after N seconds (`0` disables) |

The default `127.0.0.1` bind is loopback-only. Set `--host 0.0.0.0` **and** `--api-key` together when exposing on a shared host. Run it in a container:

```bash
docker build -t map.mmd .
docker run -p 8080:8080 -v "$(pwd)/map.mmd-out:/data" map.mmd \
  /data/graph.json --transport http --host 0.0.0.0 --api-key "$SECRET"
```

> **WSL / Linux note:** Ubuntu ships `python3`, not `python`. Use a venv to avoid conflicts:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "map-mmd[mcp]"
> ```

---

## Environment variables

These are only needed for **headless / CI extraction** (`map.mmd extract`). When running via the `/map.mmd` skill inside your IDE, the model API is provided by your IDE session — no extra keys needed.

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
| `MAP_MMD_OLLAMA_NUM_CTX` | Override Ollama KV-cache window size | optional — auto-sized by default |
| `MAP_MMD_OLLAMA_KEEP_ALIVE` | Minutes to keep Ollama model loaded | optional — set `0` to unload after each chunk |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI Service backend | `--backend azure` |
| `AZURE_OPENAI_ENDPOINT` | Azure resource endpoint URL | `--backend azure` (required alongside API key) |
| `AZURE_OPENAI_API_VERSION` | Azure API version override | optional — default `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT` or `MAP_MMD_AZURE_MODEL` | Azure deployment name | optional — default `gpt-4o` |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — standard credential chain | `--backend bedrock` (no API key, uses IAM) |
| `MAP_MMD_MAX_WORKERS` | AST parallelism thread count | optional — also `--max-workers` flag |
| `MAP_MMD_MAX_OUTPUT_TOKENS` | Raise output cap for dense corpora | optional — e.g. `32768` for large files |
| `MAP_MMD_API_TIMEOUT` | Per-call timeout in seconds for HTTP, claude-cli, and Anthropic SDK backends (default: 600) | optional — also `--api-timeout` flag |
| `MAP_MMD_FORCE` | Force graph rebuild even with fewer nodes | optional — also `--force` flag |
| `MAP_MMD_GOOGLE_WORKSPACE` | Auto-enable Google Workspace export | optional — set to `1` |
| `MAP_MMD_TRIAGE_BACKEND` | Backend for `map.mmd prs --triage` | optional — auto-detected from available keys |
| `MAP_MMD_TRIAGE_MODEL` | Model override for triage | optional — e.g. `claude-opus-4-7` |
| `MAP_MMD_QUERY_LOG` | Override query log path (default: `~/.cache/map.mmd-queries.log`) | optional — set to empty or `/dev/null` to silence |
| `MAP_MMD_QUERY_LOG_DISABLE` | Set to `1` to disable query logging entirely | optional |
| `MAP_MMD_QUERY_LOG_RESPONSES` | Set to `1` to also log full subgraph responses (off by default) | optional |
| `MAP_MMD_MAX_GRAPH_BYTES` | Override the 512 MiB graph.json size cap — e.g. `700MB`, `2GB`, or plain bytes | optional — useful for very large corpora |
| `MAP_MMD_LLM_TEMPERATURE` | Override LLM temperature for semantic extraction — e.g. `0.7`, or `none` to omit | optional — auto-omitted for o1/o3/o4/gpt-5 reasoning models |

---

## Privacy

- **Code files** — processed locally via tree-sitter. Nothing leaves your machine. A code-only corpus requires no API key — `map.mmd extract` runs fully offline.
- **Video / audio** — transcribed locally with faster-whisper. Nothing leaves your machine.
- **Docs, PDFs, images** — sent to your AI assistant for semantic extraction (via the `/map.mmd` skill, using whatever model your IDE session runs). Headless `map.mmd extract` requires `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), a running Ollama instance (`OLLAMA_BASE_URL`), AWS credentials via the standard provider chain (Bedrock - no API key needed, uses IAM), or the `claude` CLI binary (Claude Code - no API key needed, uses your Claude subscription). The `--dedup-llm` flag uses the same key.
- **Data residency** — `map.mmd extract` auto-detects which provider to use based on which API key is set (priority: Gemini → Kimi → Claude → OpenAI → DeepSeek → Azure → Bedrock → Ollama). For code with data-residency requirements, use `--backend ollama` (fully local) or pass an explicit `--backend` flag. Kimi (`MOONSHOT_API_KEY`) routes to Moonshot AI servers in China.
- No telemetry, no usage tracking, no analytics.
- **Query logging** — every `map.mmd query`, `map.mmd path`, `map.mmd explain`, and MCP `query_graph` call is logged to `~/.cache/map.mmd-queries.log` in JSON Lines format (timestamp, question, corpus, nodes returned, duration). Full subgraph responses are **not** stored by default. Set `MAP_MMD_QUERY_LOG_DISABLE=1` to opt out, or `MAP_MMD_QUERY_LOG=/dev/null` to silence without disabling the code path.

---

## Troubleshooting

**`map.mmd: command not found` after `pip install map-mmd`**
pip installs scripts to a user bin directory that may not be on your PATH. Fix:
- macOS: add `~/Library/Python/3.x/bin` to your PATH in `~/.zshrc`
- Linux: add `~/.local/bin` to your PATH in `~/.bashrc`
- Or use `uv tool install map-mmd` / `pipx install map-mmd` — both manage PATH automatically.

**`python -m map.mmd` works but `map.mmd` command doesn't**
Your shell's PATH doesn't include the Python scripts directory. Use `uv` or `pipx` instead of plain `pip`.

**`/map.mmd .` causes "path not recognized" in PowerShell**
PowerShell treats a leading `/` as a path separator. Use `map.mmd .` (no slash) on Windows.

**Graph has fewer nodes after `--update` or rebuild**
If a refactor deleted files, the old nodes linger. Pass `--force` (or set `MAP_MMD_FORCE=1`) to overwrite even when the rebuild has fewer nodes.

**Graph has duplicate nodes for the same entity (ghost duplicates)**
Ghost duplicates (same symbol appearing twice — once from AST extraction with a source location, once from semantic extraction without) are now automatically merged at build time. If you see this in a graph built before v0.8.33, run a full re-extract to clean up:
```bash
map.mmd extract . --force
```

**Ollama runs out of VRAM / context window exceeded**
The KV-cache window is auto-sized but may be too large for your GPU. Reduce it:
```bash
MAP_MMD_OLLAMA_NUM_CTX=8192 map.mmd extract ./docs --backend ollama --token-budget 4000
```

**`LLM returned invalid JSON` / `Unterminated string` warnings**
The model's JSON response hit its output-token limit and was cut off mid-string. map.mmd auto-recovers (it splits the chunk and re-extracts the halves, and an oversized single document is first sliced at heading/paragraph boundaries so the whole file is still covered), so these warnings are noisy but not data loss. To reduce the churn, raise the output cap or shrink each chunk's output:
```bash
MAP_MMD_MAX_OUTPUT_TOKENS=16384 map.mmd extract . --mode deep   # lift the cap
map.mmd extract . --mode deep --token-budget 4000                # smaller input chunks -> smaller output
```
With a cloud gateway like OpenRouter, prefer `--backend openai` (set `OPENAI_BASE_URL`) over the Ollama shim — it's a cleaner OpenAI-compatible path. If the model has its own max-output ceiling, lowering `--token-budget` is the reliable lever.

**Graph HTML is too large to open in a browser (>5000 nodes)**
Skip HTML generation and use the JSON directly:
```bash
map.mmd cluster-only ./my-project --no-viz
map.mmd query "..."
```

**`graph.json` has conflict markers after two devs commit at once**
Run `map.mmd hook install` — it sets up a git merge driver that union-merges `graph.json` automatically so conflicts never happen.

**Extraction returns empty nodes/edges for docs or PDFs**
Docs, PDFs, and images require an LLM call — code-only corpora need no key. Check that your API key is set and the backend is correct:
```bash
ANTHROPIC_API_KEY=sk-... map.mmd extract ./docs --backend claude
```

**Skill version mismatch warning in your IDE**
Your installed map.mmd version is different from the skill file. Update:
```bash
uv tool upgrade map-mmd
map.mmd install  # overwrites the skill file
```

---

## Full command reference

```
/map.mmd                          # run on current directory
/map.mmd ./raw                    # run on a specific folder
/map.mmd ./raw --mode deep        # more aggressive relationship extraction
/map.mmd ./raw --update           # re-extract only changed files
/map.mmd ./raw --directed         # preserve edge direction
/map.mmd ./raw --cluster-only     # rerun clustering on existing graph
/map.mmd ./raw --no-viz           # skip HTML visualization
/map.mmd ./raw --obsidian         # generate Obsidian vault
/map.mmd ./raw --wiki             # build agent-crawlable markdown wiki
/map.mmd ./raw --svg              # export graph.svg
/map.mmd ./raw --graphml          # export for Gephi / yEd
/map.mmd ./raw --neo4j            # generate cypher.txt for Neo4j
/map.mmd ./raw --neo4j-push bolt://localhost:7687
/map.mmd ./raw --falkordb         # generate cypher.txt for FalkorDB
/map.mmd ./raw --falkordb-push falkordb://localhost:6379
/map.mmd ./raw --watch            # auto-sync as files change
/map.mmd ./raw --mcp              # start MCP stdio server

/map.mmd add https://arxiv.org/abs/1706.03762
/map.mmd add <video-url>
/map.mmd add https://... --author "Name" --contributor "Name"

/map.mmd query "what connects attention to the optimizer?"
/map.mmd query "..." --dfs --budget 1500
/map.mmd path "DigestAuth" "Response"
/map.mmd explain "SwinTransformer"

map.mmd save-result --question "Q" --answer "A" --nodes Foo Bar --outcome useful   # record how a Q&A turned out (work memory; outcome ∈ useful|dead_end|corrected)
map.mmd reflect                   # aggregate map.mmd-out/memory/ outcomes into reflections/LESSONS.md
map.mmd reflect --if-stale        # no-op when LESSONS.md is already newer than every input (cheap to run each session)
map.mmd reflect --out docs/LESSONS.md    # write the lessons doc somewhere else
map.mmd reflect --graph map.mmd-out/graph.json  # also group lessons by community

map.mmd uninstall                 # remove from all platforms in one shot
map.mmd uninstall --purge         # also delete map.mmd-out/
map.mmd uninstall --project --platform codex  # remove project-scoped install files only

map.mmd hook install              # post-commit + post-checkout hooks
map.mmd hook uninstall
map.mmd hook status

# always-on assistant instructions - platform-specific
map.mmd claude install            # CLAUDE.md + PreToolUse hook (Claude Code)
map.mmd claude uninstall
map.mmd codebuddy install         # CODEBUDDY.md + PreToolUse hook (CodeBuddy)
map.mmd codebuddy uninstall
map.mmd codex install             # AGENTS.md + PreToolUse hook in .codex/hooks.json (Codex)
map.mmd opencode install          # AGENTS.md + tool.execute.before plugin (OpenCode)
map.mmd kilo install              # native Kilo skill + /map.mmd command + AGENTS.md + .kilo plugin
map.mmd kilo uninstall
map.mmd cursor install            # .cursor/rules/map.mmd.mdc (Cursor)
map.mmd cursor uninstall
map.mmd gemini install            # GEMINI.md + BeforeTool hook (Gemini CLI)
map.mmd gemini uninstall
map.mmd copilot install           # skill file (GitHub Copilot CLI)
map.mmd copilot uninstall
map.mmd aider install             # AGENTS.md (Aider)
map.mmd aider uninstall
map.mmd claw install              # AGENTS.md (OpenClaw)
map.mmd claw uninstall
map.mmd droid install             # AGENTS.md (Factory Droid)
map.mmd droid uninstall
map.mmd trae install              # AGENTS.md (Trae)
map.mmd trae uninstall
map.mmd trae-cn install           # AGENTS.md (Trae CN)
map.mmd trae-cn uninstall
map.mmd hermes install             # AGENTS.md + ~/.hermes/skills/ (Hermes)
map.mmd hermes uninstall
map.mmd amp install               # skill file (Amp)
map.mmd amp uninstall
map.mmd agents install            # ~/.agents/skills/ + AGENTS.md (cross-framework; alias: map.mmd skills)
map.mmd agents uninstall
map.mmd kiro install               # .kiro/skills/ + .kiro/steering/map.mmd.md (Kiro IDE/CLI)
map.mmd kiro uninstall
map.mmd pi install                # skill file (Pi coding agent)
map.mmd pi uninstall
map.mmd devin install             # skill file + .windsurf/rules/map.mmd.md (Devin CLI)
map.mmd devin uninstall
map.mmd antigravity install       # .agents/rules + .agents/workflows (Google Antigravity)
map.mmd antigravity uninstall

map.mmd extract ./docs                        # headless LLM extraction for CI (no IDE needed)
map.mmd extract ./docs --backend gemini       # explicit backend: gemini, kimi, claude, openai, deepseek, ollama, bedrock, or claude-cli
map.mmd extract ./docs --backend gemini --model gemini-3.1-pro-preview
map.mmd extract ./docs --backend ollama       # local Ollama (set OLLAMA_BASE_URL / OLLAMA_MODEL) - no API key needed for loopback
OPENAI_BASE_URL=http://localhost:8080/v1 OPENAI_MODEL=my-model map.mmd extract ./docs --backend openai   # any OpenAI-compatible server (llama.cpp, vLLM, LM Studio)
ANTHROPIC_BASE_URL=http://localhost:4000 ANTHROPIC_MODEL=my-model map.mmd extract ./docs --backend claude   # any Anthropic-compatible endpoint (LiteLLM proxy, gateways)
MAP_MMD_OLLAMA_NUM_CTX=32768 map.mmd extract ./docs --backend ollama   # override KV-cache window (auto-sized by default)
MAP_MMD_OLLAMA_KEEP_ALIVE=0 map.mmd extract ./docs --backend ollama    # unload model after each chunk (saves VRAM on small GPUs)
map.mmd extract ./docs --backend bedrock      # AWS Bedrock via IAM - no API key, uses AWS credential chain
map.mmd extract ./docs --backend claude-cli   # route through Claude Code CLI - no API key, uses your Claude subscription
map.mmd extract ./docs --backend azure        # Azure OpenAI (set AZURE_OPENAI_API_KEY + AZURE_OPENAI_ENDPOINT)
map.mmd extract ./docs --max-workers 16       # AST parallelism (also MAP_MMD_MAX_WORKERS)
map.mmd extract --postgres "postgresql://user:pass@host/db"   # introspect live PostgreSQL schema directly
map.mmd extract ./my-workspace --cargo        # introspect Rust Cargo workspace dependencies directly
map.mmd extract ./docs --token-budget 30000   # smaller semantic chunks for local/small models
map.mmd extract ./docs --max-concurrency 2    # fewer parallel LLM calls (useful for local inference)
map.mmd extract ./docs --api-timeout 900      # longer HTTP timeout for slow local models (default 600s)
map.mmd extract ./docs --google-workspace     # export .gdoc/.gsheet/.gslides via gws before extraction
map.mmd extract ./docs --mode deep            # richer semantic extraction via extended system prompt
map.mmd extract ./docs --no-cluster           # raw extraction only, skip clustering
map.mmd extract ./docs --force                # overwrite graph.json even if new graph has fewer nodes (use after refactors or to clear ghost duplicates)
map.mmd extract ./docs --dedup-llm            # LLM tiebreaker for ambiguous entity pairs (uses same API key)
map.mmd extract ./docs --global --as myrepo   # extract and register into the cross-project global graph
MAP_MMD_MAX_OUTPUT_TOKENS=32768 map.mmd extract ./docs --backend claude  # raise output cap for dense corpora

map.mmd export callflow-html                       # map.mmd-out/<project>-callflow.html
map.mmd export callflow-html --max-sections 8      # cap generated architecture sections
map.mmd export callflow-html --output docs/arch.html
map.mmd export callflow-html ./some-repo/map.mmd-out

map.mmd global add map.mmd-out/graph.json myrepo   # register a project graph into ~/.map.mmd/global.json
map.mmd global remove myrepo                         # remove a project from the global graph
map.mmd global list                                  # show all registered repos + node/edge counts
map.mmd global path                                  # print path to the global graph file

map.mmd prs                              # PR dashboard: CI, review, worktree, graph impact
map.mmd prs 42                           # deep dive on PR #42
map.mmd prs --triage                     # AI triage ranking (auto-detects backend from env)
map.mmd prs --worktrees                  # worktree → branch → PR mapping
map.mmd prs --conflicts                  # PRs sharing graph communities (merge-order risk)
map.mmd prs --base main                  # filter to PRs targeting a specific base branch
map.mmd prs --repo owner/repo            # run against a different GitHub repo
MAP_MMD_TRIAGE_BACKEND=kimi map.mmd prs --triage   # use a specific backend for triage

map.mmd clone https://github.com/karpathy/nanoGPT
map.mmd merge-graphs a.json b.json --out merged.json
map.mmd --version                                    # print installed version
map.mmd watch ./src
map.mmd check-update ./src
map.mmd update ./src
map.mmd update ./src --no-cluster  # skip reclustering, write raw AST graph only
map.mmd update ./src --force       # overwrite even if new graph has fewer nodes
map.mmd cluster-only ./my-project
map.mmd cluster-only ./my-project --graph path/to/graph.json  # custom graph location
map.mmd cluster-only ./my-project --max-concurrency 16 --batch-size 200  # parallel community labeling (large graphs)
map.mmd cluster-only ./my-project --resolution 1.5            # more, smaller communities
map.mmd cluster-only ./my-project --exclude-hubs 99           # exclude p99 degree nodes from partitioning
map.mmd cluster-only ./my-project --no-label                  # keep "Community N" placeholders
map.mmd cluster-only ./my-project --backend=gemini            # backend for community naming
map.mmd cluster-only ./my-project --backend=gemini --model gemini-2.5-pro  # specific model
map.mmd label ./my-project                                    # (re)name communities with the configured backend
map.mmd label ./my-project --backend=openai --model gpt-4o   # force a specific backend and model
```

> **Community names:** inside an agent (Claude Code, Gemini CLI) the agent names communities itself. When you run the bare CLI, `cluster-only` auto-names them with the configured backend (built-in or custom OpenAI-compatible provider) — pass `--no-label` to keep `Community N`, or run `map.mmd label` to (re)generate names on demand.

---

## Learn more

- [How it works](docs/how-it-works.md) — the extraction pipeline, community detection, confidence scoring, benchmarks
- [ARCHITECTURE.md](ARCHITECTURE.md) — module breakdown, how to add a language
- [Optional integrations](docs/docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite

---

## Built on map.mmd — Penpax

[**Penpax**](https://map.mmdlabs.ai) is the always-on layer built on top of map.mmd — it applies the same graph approach to your entire working life: meetings, browser history, emails, files, and code, updating continuously in the background.

Built for people whose work lives across hundreds of conversations and documents they can never fully reconstruct. No cloud, fully on-device.

**Free trial launching soon.** [Join the waitlist →](https://map.mmdlabs.ai)

---

<details>
<summary>Contributing</summary>

### Development setup

The project uses [uv](https://docs.astral.sh/uv/) for dev workflow. Install it once, then:

```bash
git clone https://github.com/getwinharris/map.mmd.git
cd map.mmd
git checkout v8                        # active development branch

# Create the project venv and install map.mmd + all extras + the dev group
# (pytest). uv installs the dev dependency group by default; pass --no-dev to
# skip it.
uv sync --all-extras
```

Verify the editable install:
```bash
uv run map.mmd --version
uv run python -c "import map.mmd; print(map.mmd.__file__)"
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

**Worked examples** are the most useful contribution. Run `/map.mmd` on a real corpus, save the output to `worked/{slug}/`, write an honest `review.md` covering what the graph got right and wrong, and open a PR.

**Extraction bugs** — open an issue with the input file, the cache entry (`map.mmd-out/cache/`), and what was missed or wrong.

See [ARCHITECTURE.md](ARCHITECTURE.md) for module responsibilities and how to add a language.

</details>
