<p align="center">
  <a href="https://map.mmdlabs.ai"><img src="https://raw.githubusercontent.com/getwinharris/map.mmd/v4/docs/logo-text.svg" width="260" height="64" alt="map.mmd"/></a>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://www.ycombinator.com/companies/map.mmd"><img src="https://img.shields.io/badge/Y%20Combinator-S26-F0652F?style=flat&logo=ycombinator&logoColor=white" alt="YC S26"/></a>
  <a href="https://safishamsi.gumroad.com/l/qetvlo"><img src="https://img.shields.io/badge/Book-The%20Memory%20Layer-2ea44f?style=flat&logo=gitbook&logoColor=white" alt="The Memory Layer"/></a>
  <a href="https://github.com/getwinharris/map.mmd/actions/workflows/ci.yml"><img src="https://github.com/getwinharris/map.mmd/actions/workflows/ci.yml/badge.svg?branch=v8" alt="CI"/></a>
  <a href="https://pypi.org/project/map-mmd/"><img src="https://img.shields.io/pypi/v/map-mmd" alt="PyPI"/></a>
  <a href="https://clickpy.clickhouse.com/dashboard/map-mmd"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsql-clickhouse.clickhouse.com%2F%3Fquery%3DSELECT%2520concat%2528toString%2528round%2528sum%2528count%2529%2F1000%2529%2529%2C%2520%2527k%2527%2529%2520AS%2520c%2520FROM%2520pypi.pypi_downloads%2520WHERE%2520project%253D%2527map-mmd%2527%2520FORMAT%2520JSON%26user%3Ddemo&query=%24.data%5B0%5D.c&label=downloads&color=blue" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/in/safi-shamsi"><img src="https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin" alt="LinkedIn"/></a>
  <a href="https://x.com/map-mmd"><img src="https://img.shields.io/badge/X-map-mmd-000000?logo=x&logoColor=white" alt="X"/></a>
</p>

<p align="center">
  <a href="https://star-history.com/#getwinharris/map.mmd&Date">
    <img src="https://api.star-history.com/svg?repos=getwinharris/map.mmd&type=Date" alt="Star History Chart" width="370"/>
  </a>
</p>

Введіть `/map.mmd` у своєму ШІ-асистенті для кодингу, і він нанесе весь ваш проект — код, документи, PDF, зображення, відео — на граф знань, який можна запитувати замість того, щоб шукати по файлах.

Працює в Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kimi Code, Kiro, Pi та Google Antigravity.

```
/map.mmd .
```

Це все. Ви отримуєте три файли:

```
map.mmd-out/
├── graph.html       відкрийте в будь-якому браузері — клікайте по вузлах, фільтруйте, шукайте
├── GRAPH_REPORT.md  основне: ключові концепції, неочікувані зв’язки, запропоновані запитання
└── graph.json       повний граф — запитуйте його будь-коли без повторного перечитування ваших файлів
```

Для читабельної сторінки архітектури з діаграмами викликів Mermaid виконайте:

```bash
map.mmd export callflow-html
```

---

## Вимоги

| Вимога | Мінімум | Перевірка | Встановлення |
|---|---|---|---|
| Python | 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| uv *(рекомендовано)* | будь-яка | `uv --version` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| pipx *(альтернатива)* | будь-яка | `pipx --version` | `pip install pipx` |

**Швидке встановлення на macOS (Homebrew):**
```bash
brew install python@3.12 uv
```

**Швидке встановлення на Windows:**
```powershell
winget install astral-sh.uv
```

**Ubuntu/Debian:**
```bash
sudo apt install python3.12 python3-pip pipx
# або встановити uv:
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Встановлення

> **Офіційний пакет:** Пакет PyPI — `map-mmd` (подвійна y). Інші пакети `map.mmd*` на PyPI не є афілійованими. Команда CLI залишається `map.mmd`.

**Крок 1 — встановити пакет:**

```bash
# Рекомендовано (uv автоматично додає map.mmd до PATH):
uv tool install map-mmd

# Альтернативи:
pipx install map-mmd
pip install map-mmd
```

**Крок 2 — зареєструвати навичку у вашому ШІ-асистенті:**

```bash
map.mmd install
```

Це все. Відкрийте асистента і введіть `/map.mmd .`

Щоб встановити навичку в поточний репозиторій замість профілю користувача, додайте `--project`:

```bash
map.mmd install --project
map.mmd install --project --platform codex
```

Встановлення на рівні проєкту записуються в поточну директорію, наприклад .claude/skills/map.mmd/SKILL.md або .agents/skills/map.mmd/SKILL.md, і виводять підказку git add для файлів, які можна закомітити. Команди для окремих платформ, що підтримують інсталяції на рівні проєкту, приймають той самий прапорець, наприклад map.mmd claude install --project або map.mmd codex install --project.

> **Примітка для PowerShell:** Використовуйте `map.mmd .` замість `/map.mmd .` — ведучий слеш є роздільником шляху в PowerShell.

> **`map.mmd: command not found`?** Використовуйте `uv tool install map-mmd` або `pipx install map-mmd` — обидва автоматично додають CLI до PATH. При використанні звичайного `pip` додайте `~/.local/bin` (Linux) або `~/Library/Python/3.x/bin` (Mac) до вашого PATH, або запустіть `python -m map.mmd`.

### Оберіть платформу

| Платформа | Команда встановлення |
|----------|----------------|
| Claude Code (Linux/Mac) | `map.mmd install` |
| Claude Code (Windows) | `map.mmd install --platform windows` |
| Codex | `map.mmd install --platform codex` |
| OpenCode | `map.mmd install --platform opencode` |
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
| Kiro IDE/CLI | `map.mmd kiro install` |
| Pi coding agent | `map.mmd install --platform pi` |
| Cursor | `map.mmd cursor install` |
| Google Antigravity | `map.mmd antigravity install` |

> Користувачам Codex: також додайте `multi_agent = true` під `[features]` у `~/.codex/config.toml`.
> Codex використовує `$map.mmd` замість `/map.mmd`.

### Додаткові пакети (опціонально)

Встановіть лише те, що потрібно:

| Пакет | Що додає | Встановлення |
|---|---|---|
| `pdf` | Вилучення PDF | `pip install "map-mmd[pdf]"` |
| `office` | Підтримка `.docx` та `.xlsx` | `pip install "map-mmd[office]"` |
| `google` | Рендеринг Google Sheets | `pip install "map-mmd[google]"` |
| `video` | Транскрипція відео/аудіо (faster-whisper + yt-dlp) | `pip install "map-mmd[video]"` |
| `mcp` | MCP stdio-сервер | `pip install "map-mmd[mcp]"` |
| `neo4j` | Підтримка надсилання до Neo4j | `pip install "map-mmd[neo4j]"` |
| `svg` | Експорт графу в SVG | `pip install "map-mmd[svg]"` |
| `leiden` | Виявлення спільнот Leiden (лише Python < 3.13) | `pip install "map-mmd[leiden]"` |
| `ollama` | Локальний вивід Ollama | `pip install "map-mmd[ollama]"` |
| `openai` | OpenAI / OpenAI-сумісні API | `pip install "map-mmd[openai]"` |
| `gemini` | Google Gemini API | `pip install "map-mmd[gemini]"` |
| `bedrock` | AWS Bedrock (використовує IAM, без API-ключа) | `pip install "map-mmd[bedrock]"` |
| `sql` | Вилучення SQL схем | `pip install "map-mmd[sql]"` |
| `all` | Все вищезазначене | `pip install "map-mmd[all]"` |

---

## Змусьте асистента завжди використовувати граф

Виконайте один раз у своєму проекті після побудови графу:

| Платформа | Команда |
|----------|---------|
| Claude Code | `map.mmd claude install` |
| Codex | `map.mmd codex install` |
| OpenCode | `map.mmd opencode install` |
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
| Kiro IDE/CLI | `map.mmd kiro install` |
| Pi coding agent | `map.mmd pi install` |
| Google Antigravity | `map.mmd antigravity install` |

Це записує невеликий конфігураційний файл, який каже асистенту звертатися до графу знань для питань про кодову базу — надаючи перевагу локалізованим запитам на кшталт `map.mmd query "<питання>"` замість читання повного звіту або пошуку по сирих файлах. На платформах, що підтримують хуки з корисним навантаженням (Claude Code, Gemini CLI), хук спрацьовує автоматично перед пошуковими викликами інструментів і спрямовує асистента до графу. На інших (Codex, OpenCode, Cursor тощо) постійні файли інструкцій (`AGENTS.md`, `.cursor/rules/` тощо) забезпечують таке саме керівництво. `GRAPH_REPORT.md` все ще доступний для загального огляду архітектури.

Щоб видалити map.mmd з усіх платформ одразу: `map.mmd uninstall` (додайте `--purge`, щоб також видалити `map.mmd-out/`). Або скористайтеся командою для конкретної платформи (напр. `map.mmd claude uninstall`).

---

## Що є у звіті

- **Вузли-боги** — найбільш пов'язані концепції у вашому проекті. Через них проходить все.
- **Несподівані зв'язки** — зв'язки між речами з різних файлів або модулів. Відсортовані за ступенем несподіваності.
- **«Чому»** — рядкові коментарі (`# NOTE:`, `# WHY:`, `# HACK:`), рядки документації та обґрунтування дизайну з документів витягуються як окремі вузли, пов'язані з кодом, який вони пояснюють.
- **Запропоновані питання** — 4–5 питань, на які граф унікально здатний відповісти.
- **Теги впевненості** — кожен виведений зв'язок позначений як `EXTRACTED`, `INFERRED` або `AMBIGUOUS`. Ви завжди знаєте, що знайдено, а що виведено.

---

## Які файли підтримуються

| Тип | Розширення |
|------|-----------|
| Код (31 мова) | `.py .ts .js .jsx .tsx .mjs .go .rs .java .c .cpp .h .hpp .rb .cs .kt .scala .php .swift .lua .luau .zig .ps1 .ex .exs .m .mm .jl .vue .svelte .astro .groovy .gradle .dart .v .sv .sql .f .f90 .f95 .f03 .f08 .pas .pp .dpr .dpk .lpr .inc .dfm .lfm .lpk .sh .bash .json` |
| Документи | `.md .mdx .qmd .html .txt .rst .yaml .yml` |
| Office | `.docx .xlsx` (потрібен `pip install map-mmd[office]`) |
| Google Workspace | `.gdoc .gsheet .gslides` (опціонально; потрібна автентифікація `gws` та `--google-workspace`; Sheets потребує `pip install map-mmd[google]`) |
| PDF | `.pdf` |
| Зображення | `.png .jpg .webp .gif` |
| Відео / Аудіо | `.mp4 .mov .mp3 .wav` та інші (потрібен `pip install map-mmd[video]`) |
| YouTube / URL | будь-який URL відео (потрібен `pip install map-mmd[video]`) |

Код витягується локально без API-викликів (AST через tree-sitter). Все інше обробляється через API моделі вашого ШІ-асистента.

Файли `.gdoc`, `.gsheet` та `.gslides` з Google Drive for desktop — це ярлики-посилання, а не вміст документів. Щоб включити нативні Google Docs, Sheets та Slides у безголове витягування, встановіть та автентифікуйте [`gws` CLI](https://github.com/googleworkspace/cli), потім запустіть:

```bash
pip install "map-mmd[google]"  # потрібен для рендерингу таблиць Google Sheets
gws auth login -s drive
map.mmd extract ./docs --google-workspace
```

Також можна встановити `MAP_MMD_GOOGLE_WORKSPACE=1`. map.mmd експортує ярлики в `map.mmd-out/converted/` як Markdown-сайдкари, а потім витягує ці файли.

---

## Часті команди

```bash
/map.mmd .                        # побудувати граф для поточної папки
/map.mmd ./docs --update          # повторно витягнути лише змінені файли
/map.mmd . --cluster-only         # перезапустити кластеризацію без повторного витягування
/map.mmd . --cluster-only --resolution 1.5      # більш дрібні спільноти
/map.mmd . --cluster-only --exclude-hubs 99     # виключити утилітарні суперхаби з рейтингів “god-node” вузлів-богів
/map.mmd . --no-viz               # пропустити HTML, лише звіт + JSON
/map.mmd . --wiki                 # побудувати markdown-вікі з графу
map.mmd export callflow-html      # Mermaid архітектура/flow-викликів HTML (автоматично регенерується на кожен git-коміт, якщо встановлений hook)

/map.mmd query "що пов'язує auth з базою даних?"
/map.mmd path "UserService" "DatabasePool"
/map.mmd explain "RateLimiter"

/map.mmd add https://arxiv.org/abs/1706.03762   # завантажити статтю і додати її
/map.mmd add <youtube-url>                       # транскрибувати і додати відео

map.mmd hook install              # автоматичне перебудування при git-коміті
map.mmd merge-graphs a.json b.json              # об'єднати два графи

map.mmd prs                       # дашборд PR: стан CI, статус рев’ю, мапінг worktree
map.mmd prs 42                    # детальний огляд PR #42 з впливом на граф
map.mmd prs --triage              # ШІ оцінює вашу чергу рев’ю (використовує будь-який налаштований бекенд)
map.mmd prs --conflicts           # PR-и, що ділять спільні графові спільноти — ризик порядку злиття
```

Дивіться [повний довідник команд](#повний-довідник-команд) нижче.

---

## Ігнорування файлів

Створіть `.map.mmdignore` у кореневій директорії проекту — той самий синтаксис, що й `.gitignore`, включно з запереченням `!`:

```
# .map.mmdignore
node_modules/
dist/
*.generated.py

# індексувати лише src/, ігнорувати все інше
*
!src/
!src/**
```

---

## Налаштування для команди

`map.mmd-out/` призначений для коміту в git, щоб кожен у команді починав із картою.

**Рекомендовані доповнення до `.gitignore`:**
```
map.mmd-out/manifest.json    # базується на mtime, ламається після git clone
map.mmd-out/cost.json        # лише локальний
# map.mmd-out/cache/         # опціонально: комітьте для швидкості, пропустіть для меншого репо
```

**Робочий процес:**
1. Одна людина запускає `/map.mmd .` і комітить `map.mmd-out/`.
2. Усі виконують pull — їхній асистент одразу читає граф.
3. Запустіть `map.mmd hook install` для автоматичного перебудування після кожного коміту (лише AST, без витрат API). Це також налаштовує git merge driver, щоб `graph.json` ніколи не залишався з маркерами конфліктів — два розробники, що комітять одночасно, отримають автоматично об'єднані графи.
4. Коли документи або статті змінюються, запустіть `/map.mmd --update`, щоб оновити ці вузли.

---

## Використання графу напряму

```bash
# запит до графу з терміналу
map.mmd query "покажи потік автентифікації"
map.mmd query "що пов'язує DigestAuth з Response?" --graph map.mmd-out/graph.json

# відкрити граф як MCP-сервер (для повторного доступу через інструменти)
python -m map.mmd.serve map.mmd-out/graph.json

# зареєструвати в Kimi Code:
kimi mcp add --transport stdio map.mmd -- python -m map.mmd.serve map.mmd-out/graph.json
```

MCP-сервер надає асистенту структурований доступ: `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs`.

> **Примітка для WSL / Linux:** Ubuntu постачає `python3`, а не `python`. Використовуйте venv, щоб уникнути конфліктів:
> ```bash
> python3 -m venv .venv && .venv/bin/pip install "map-mmd[mcp]"
> ```

---

## Змінні середовища

Потрібні лише для **headless / CI витягування** (`map.mmd extract`). При запуску через навичку `/map.mmd` у вашому IDE API моделі надається сесією IDE — додаткових ключів не потрібно.

| Змінна | Використання | Коли потрібна |
|---|---|---|
| `ANTHROPIC_API_KEY` | Backend Claude (Anthropic) | `--backend claude` |
| `ANTHROPIC_BASE_URL` | URL Anthropic-сумісного endpoint (LiteLLM proxy, шлюзи, ...) | `--backend claude` (типово: `https://api.anthropic.com`) |
| `ANTHROPIC_MODEL` | Назва моделі для backend Claude — для власних endpoint використовуйте назву/псевдонім моделі вашого сервера | `--backend claude` (типово: `claude-sonnet-4-6`) |
| `GEMINI_API_KEY` або `GOOGLE_API_KEY` | Backend Google Gemini | `--backend gemini` |
| `OPENAI_API_KEY` | OpenAI або OpenAI-сумісні API | `--backend openai` (локальні сервери приймають будь-яке непорожнє значення) |
| `OPENAI_BASE_URL` | URL OpenAI-сумісного сервера (llama.cpp, vLLM, LM Studio, ...) | `--backend openai` (типово: `https://api.openai.com/v1`) |
| `OPENAI_MODEL` | Назва моделі для backend OpenAI — для self-hosted серверів використовуйте назву/псевдонім моделі, яку надає ваш сервер (див. його endpoint `/v1/models`), напр. `LFM2.5-8B-A1B-UD-Q4_K_XL` для llama.cpp | `--backend openai` (типово: `gpt-4.1-mini`) |
| `DEEPSEEK_API_KEY` | Backend DeepSeek | `--backend deepseek` |
| `MOONSHOT_API_KEY` | Backend Kimi Code | `--backend kimi` |
| `OLLAMA_BASE_URL` | URL локального виводу Ollama | `--backend ollama` (типово: `http://localhost:11434`) |
| `OLLAMA_MODEL` | Назва моделі Ollama | `--backend ollama` (типово: автовизначення) |
| `MAP_MMD_OLLAMA_NUM_CTX` | Перевизначити розмір KV-кеш вікна Ollama | опціонально — автоматично за замовчуванням |
| `MAP_MMD_OLLAMA_KEEP_ALIVE` | Хвилини утримання моделі Ollama завантаженою | опціонально — встановіть `0` для вивантаження після кожного шматка |
| `AWS_*` / `~/.aws/credentials` | AWS Bedrock — стандартний ланцюг облікових даних | `--backend bedrock` (без API-ключа, використовує IAM) |
| `MAP_MMD_MAX_WORKERS` | Кількість потоків паралелізму AST | опціонально — також прапор `--max-workers` |
| `MAP_MMD_MAX_OUTPUT_TOKENS` | Підвищити ліміт виводу для щільних корпусів | опціонально — напр. `32768` для великих файлів |
| `MAP_MMD_API_TIMEOUT` | HTTP тайм-аут у секундах (типово: 600) | опціонально — також прапор `--api-timeout` |
| `MAP_MMD_FORCE` | Примусове перебудування графу навіть із меншою кількістю вузлів | опціонально — також прапор `--force` |
| `MAP_MMD_GOOGLE_WORKSPACE` | Автоввімкнення експорту Google Workspace | опціонально — встановіть в `1` |
| `MAP_MMD_TRIAGE_BACKEND` | Backend для `map.mmd prs --triage` | опціонально — автовизначення з наявних ключів |
| `MAP_MMD_TRIAGE_MODEL` | Перевизначення моделі для triage | опціонально — напр. `claude-opus-4-7` |

---

## Конфіденційність

- **Файли коду** — обробляються локально через tree-sitter. Нічого не покидає ваш комп'ютер.
- **Відео / аудіо** — транскрибуються локально за допомогою faster-whisper. Нічого не покидає ваш комп'ютер.
- **Документи, PDF, зображення** — надсилаються до вашого ШІ-асистента для семантичного витягування (через навичку `/map.mmd`, використовуючи модель, що запущена у вашому IDE). Безголове `map.mmd extract` потребує `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Gemini), `MOONSHOT_API_KEY` (Kimi), `ANTHROPIC_API_KEY` (Claude), `OPENAI_API_KEY` (OpenAI), `DEEPSEEK_API_KEY` (DeepSeek), запущеного екземпляра Ollama (`OLLAMA_BASE_URL`), AWS-облікових даних через стандартний ланцюг провайдерів (Bedrock — без API-ключа, використовує IAM) або бінарного файлу `claude` CLI (Claude Code — без API-ключа, використовує вашу підписку Claude). Прапор `--dedup-llm` використовує той самий ключ.
- Без телеметрії, без відстеження використання, без аналітики.

---

## Вирішення проблем

**`map.mmd: command not found` після `pip install map-mmd`**
pip встановлює скрипти в директорію bin для користувача, яка може не бути в PATH. Виправлення:
- macOS: додайте `~/Library/Python/3.x/bin` до PATH у `~/.zshrc`
- Linux: додайте `~/.local/bin` до PATH у `~/.bashrc`
- Або використовуйте `uv tool install map-mmd` / `pipx install map-mmd` — обидва автоматично керують PATH.

**`python -m map.mmd` працює, але команда `map.mmd` — ні**
PATH вашої оболонки не включає директорію скриптів Python. Використовуйте `uv` або `pipx` замість звичайного `pip`.

**`/map.mmd .` викликає "path not recognized" в PowerShell**
PowerShell трактує ведучий `/` як роздільник шляху. Використовуйте `map.mmd .` (без слеша) на Windows.

**Граф має менше вузлів після `--update` або перебудови**
Якщо рефакторинг видалив файли, старі вузли залишаються. Передайте `--force` (або встановіть `MAP_MMD_FORCE=1`), щоб перезаписати навіть якщо перебудова має менше вузлів.

**Граф має дублікати вузлів для однієї сутності (фантомні дублікати)**
Це трапляється, коли семантичне та AST-витягування не погодилось щодо формату ID вузла. Запустіть повне повторне витягування для очищення:
```bash
map.mmd extract . --force
```

**Ollama вичерпує VRAM / перевищено вікно контексту**
KV-кеш вікно автоматично розраховується, але може бути завеликим для вашого GPU. Зменшіть його:
```bash
MAP_MMD_OLLAMA_NUM_CTX=8192 map.mmd extract ./docs --backend ollama --token-budget 4000
```

**HTML графу занадто великий для відкриття в браузері (>5000 вузлів)**
Пропустіть генерацію HTML і використовуйте JSON напряму:
```bash
map.mmd cluster-only ./my-project --no-viz
map.mmd query "..."
```

**`graph.json` має маркери конфліктів після одночасного коміту двох розробників**
Запустіть `map.mmd hook install` — це налаштовує git merge driver, який автоматично об'єднує `graph.json`, щоб конфліктів ніколи не виникало.

**Вилучення повертає порожні вузли/ребра для документів або PDF**
Документи та PDF потребують LLM-виклику. Перевірте, що API-ключ встановлено і backend правильний:
```bash
ANTHROPIC_API_KEY=sk-... map.mmd extract ./docs --backend claude
```

**Попередження про невідповідність версій навички у вашому IDE**
Встановлена версія map.mmd відрізняється від файлу навички. Оновіть:
```bash
uv tool upgrade map-mmd
map.mmd install  # перезаписує файл навички
```

---

## Повний довідник команд

```
/map.mmd                          # запустити в поточному каталозі
/map.mmd ./raw                    # запустити у конкретній папці
/map.mmd ./raw --mode deep        # більш агресивне витягування зв'язків
/map.mmd ./raw --update           # повторно витягнути лише змінені файли
/map.mmd ./raw --directed         # зберегти напрямок ребер
/map.mmd ./raw --cluster-only     # повторна кластеризація існуючого графу
/map.mmd ./raw --no-viz           # пропустити HTML-візуалізацію
/map.mmd ./raw --obsidian         # згенерувати сховище Obsidian
/map.mmd ./raw --wiki             # побудувати markdown-вікі для обходу агентами
/map.mmd ./raw --svg              # експортувати graph.svg
/map.mmd ./raw --graphml          # експортувати для Gephi / yEd
/map.mmd ./raw --neo4j            # згенерувати cypher.txt для Neo4j
/map.mmd ./raw --neo4j-push bolt://localhost:7687
/map.mmd ./raw --watch            # автосинхронізація при зміні файлів
/map.mmd ./raw --mcp              # запустити MCP stdio-сервер

/map.mmd add https://arxiv.org/abs/1706.03762
/map.mmd add <video-url>
/map.mmd add https://... --author "Name" --contributor "Name"

/map.mmd query "що пов'язує attention з optimizer?"
/map.mmd query "..." --dfs --budget 1500
/map.mmd path "DigestAuth" "Response"
/map.mmd explain "SwinTransformer"

map.mmd uninstall                 # видалити з усіх платформ одразу
map.mmd uninstall --purge         # також видалити map.mmd-out/
map.mmd uninstall --project --platform codex  # видалити лише файли проектного встановлення

map.mmd hook install              # хуки post-commit + post-checkout
map.mmd hook uninstall
map.mmd hook status

map.mmd claude install / uninstall
map.mmd codex install / uninstall
map.mmd opencode install
map.mmd cursor install / uninstall
map.mmd gemini install / uninstall
map.mmd copilot install / uninstall
map.mmd aider install / uninstall
map.mmd claw install / uninstall
map.mmd droid install / uninstall
map.mmd trae install / uninstall
map.mmd trae-cn install / uninstall
map.mmd hermes install / uninstall
map.mmd kiro install / uninstall
map.mmd antigravity install / uninstall

map.mmd extract ./docs                        # headless LLM-витягування для CI (без IDE)
map.mmd extract ./docs --backend gemini       # явний backend: gemini, kimi, claude, openai, deepseek, ollama, bedrock або claude-cli
map.mmd extract ./docs --backend gemini --model gemini-3.1-pro-preview
map.mmd extract ./docs --backend ollama       # локальний Ollama (встановіть OLLAMA_BASE_URL / OLLAMA_MODEL) — без API-ключа для loopback
OPENAI_BASE_URL=http://localhost:8080/v1 OPENAI_MODEL=my-model map.mmd extract ./docs --backend openai   # будь-який OpenAI-сумісний сервер (llama.cpp, vLLM, LM Studio)
ANTHROPIC_BASE_URL=http://localhost:4000 ANTHROPIC_MODEL=my-model map.mmd extract ./docs --backend claude   # будь-який Anthropic-сумісний endpoint (LiteLLM proxy, шлюзи)
MAP_MMD_OLLAMA_NUM_CTX=32768 map.mmd extract ./docs --backend ollama   # перевизначити KV-кеш вікно (автоматично за замовчуванням)
MAP_MMD_OLLAMA_KEEP_ALIVE=0 map.mmd extract ./docs --backend ollama    # вивантажити модель після кожного шматка (економить VRAM на малих GPU)
map.mmd extract ./docs --backend bedrock      # AWS Bedrock через IAM — без API-ключа, використовує ланцюг облікових даних AWS
map.mmd extract ./docs --backend claude-cli   # маршрутизація через Claude Code CLI — без API-ключа, використовує вашу підписку Claude
map.mmd extract ./docs --max-workers 16       # паралелізм AST (також MAP_MMD_MAX_WORKERS)
map.mmd extract ./docs --token-budget 30000   # менші семантичні шматки для локальних/малих моделей
map.mmd extract ./docs --max-concurrency 2    # менше паралельних LLM-викликів (корисно для локального виводу)
map.mmd extract ./docs --api-timeout 900      # довший HTTP тайм-аут для повільних локальних моделей (типово 600с)
map.mmd extract ./docs --google-workspace     # експортувати .gdoc/.gsheet/.gslides через gws перед витягуванням
map.mmd extract ./docs --no-cluster           # лише сире витягування, пропустити кластеризацію
map.mmd extract ./docs --force                # перезаписати graph.json навіть якщо новий граф має менше вузлів (використовуйте після рефакторингу або для очищення фантомних дублікатів)
map.mmd extract ./docs --dedup-llm            # LLM-арбітр для неоднозначних пар сутностей (використовує той самий API-ключ)
map.mmd extract ./docs --global --as myrepo   # витягнути і зареєструвати в крос-проектний глобальний граф
MAP_MMD_MAX_OUTPUT_TOKENS=32768 map.mmd extract ./docs --backend claude  # підвищити ліміт виводу для щільних корпусів

map.mmd export callflow-html                       # map.mmd-out/<project>-callflow.html
map.mmd export callflow-html --max-sections 8      # обмежити кількість згенерованих секцій архітектури
map.mmd export callflow-html --output docs/arch.html
map.mmd export callflow-html ./some-repo/map.mmd-out

map.mmd global add map.mmd-out/graph.json myrepo   # зареєструвати граф проекту в ~/.map.mmd/global.json
map.mmd global remove myrepo                         # видалити проект з глобального графу
map.mmd global list                                  # показати всі зареєстровані репо + кількість вузлів/ребер
map.mmd global path                                  # вивести шлях до файлу глобального графу

map.mmd prs                              # дашборд PR: CI, рев’ю, worktree, вплив на граф
map.mmd prs 42                           # детальний огляд PR #42
map.mmd prs --triage                     # AI ранжування пріоритизації (автоматично визначає бекенд з середовища)
map.mmd prs --worktrees                  # worktree → гілка → PR зіставлення
map.mmd prs --conflicts                  # PR-и, що ділять спільні графові спільноти (ризик порядку злиття)
map.mmd prs --base main                  # фільтр PR-ів за цільовою базовою гілкою
map.mmd prs --repo owner/repo            # запустити для іншого GitHub-репо
MAP_MMD_TRIAGE_BACKEND=kimi map.mmd prs --triage   # використовувати конкретний backend для triage

map.mmd clone https://github.com/karpathy/nanoGPT
map.mmd merge-graphs a.json b.json --out merged.json
map.mmd --version                                    # вивести встановлену версію
map.mmd watch ./src
map.mmd check-update ./src
map.mmd update ./src
map.mmd update ./src --no-cluster  # пропустити рекластеризацію, записати лише сирий AST граф
map.mmd update ./src --force       # перезаписати навіть якщо новий граф має менше вузлів
map.mmd cluster-only ./my-project
map.mmd cluster-only ./my-project --graph path/to/graph.json  # власне розташування графу
map.mmd cluster-only ./my-project --resolution 1.5            # більше, менших спільнот
map.mmd cluster-only ./my-project --exclude-hubs 99           # виключити вузли p99 ступеня з розбиття
```

---

## Дізнатися більше

- [Як це працює](../how-it-works.md) — пайплайн витягування, виявлення спільнот, оцінка впевненості, бенчмарки
- [ARCHITECTURE.md](../../ARCHITECTURE.md) — опис модулів, як додати мову
- [Опціональні інтеграції](../docker-mcp-sqlite.md) — Docker MCP Toolkit + SQLite

---

## Побудовано на map.mmd — Penpax

[**Penpax**](https://map.mmdlabs.ai) — це завжди активний шар поверх map.mmd, він застосовує той самий графовий підхід до всього робочого життя: зустрічей, історії браузера, email-ів, файлів і коду, постійно оновлюючись у фоновому режимі.

Створений для людей, чия робота розкидана по сотнях розмов і документів, які неможливо повністю відтворити. Без хмари, повністю на пристрої.

**Безкоштовна пробна версія незабаром.** [Приєднайтесь до списку очікування →](https://map.mmdlabs.ai)

---

<details>
<summary>Участь у розробці</summary>

### Налаштування розробки

Клонуйте репо і встановіть у редагованому режимі:

```bash
git clone https://github.com/getwinharris/map.mmd.git
cd map.mmd
git checkout v8                        # гілка активної розробки

# Створіть віртуальне середовище (потрібен Python 3.10+):
python3 -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate

# Встановіть у редагованому режимі з усіма опціональними пакетами:
pip install -e ".[all]"
```

Перевірте редаговане встановлення:
```bash
map.mmd --version
python -c "import map.mmd; print(map.mmd.__file__)"
```

### Запуск тестів

```bash
pip install pytest
pytest tests/ -q                       # запустити весь набір тестів
pytest tests/test_extract.py -q        # один модуль
pytest tests/ -q -k "python"           # фільтрація за назвою
```

> Примітка для macOS: набір тестів включає обидва файли `sample.f90` та `sample.F90`. Вони конфліктують на файлових системах HFS+ / APFS без урахування регістру. Запускайте на Linux або в Docker-контейнері, якщо потрібно тестувати обидва варіанти Fortran одночасно.

### Робочий процес з git

- Активна розробка відбувається в гілці `v8`.
- Стиль комітів: `fix: <опис>` / `feat: <опис>` / `docs: <опис>`
- Перед відкриттям PR запустіть `pytest tests/ -q` і переконайтесь, що він проходить.
- Додайте файл-фікстуру до `tests/fixtures/` і тести до `tests/test_languages.py` для будь-якого нового екстрактора мови.

### Що варто додати

Найкорисніший внесок — це **опрацьовані приклади**. Запустіть `/map.mmd` на реальному корпусі, збережіть результат у `worked/{slug}/`, напишіть чесний `review.md` про те, що граф зробив правильно і неправильно, і відкрийте PR.

**Помилки витягування** — відкрийте issue з вхідним файлом, записом кешу (`map.mmd-out/cache/`) і тим, що було пропущено або неправильно.

Дивіться [ARCHITECTURE.md](../../ARCHITECTURE.md) щодо відповідальностей модулів і того, як додати мову.

</details>
