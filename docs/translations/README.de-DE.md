<p align="center">
  <img src="https://raw.githubusercontent.com/getwinharris/map.mmd/v4/docs/logo-text.svg" width="260" height="64" alt="map.mmd"/>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/getwinharris/map.mmd/actions/workflows/ci.yml"><img src="https://github.com/getwinharris/map.mmd/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/map-mmd/"><img src="https://img.shields.io/pypi/v/map-mmd" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/map-mmd"><img src="https://static.pepy.tech/badge/map-mmd" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/in/safi-shamsi"><img src="https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin" alt="LinkedIn"/></a>
</p>

**Eine KI-Coding-Assistent-Skill.** Tippe `/map.mmd` in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro oder Google Antigravity — es liest deine Dateien, baut einen Wissensgraphen und gibt dir Struktur zurück, die du vorher nicht sehen konntest. Verstehe eine Codebasis schneller. Finde das „Warum" hinter Architekturentscheidungen.

Vollständig multimodal. Leg Code, PDFs, Markdown, Screenshots, Diagramme, Whiteboard-Fotos, Bilder in anderen Sprachen oder Video- und Audiodateien ab — map.mmd extrahiert Konzepte und Beziehungen aus allem und verbindet sie in einem einzigen Graphen. Videos werden lokal mit Whisper transkribiert, angetrieben durch einen domänenspezifischen Prompt aus deinem Korpus. 25 Programmiersprachen werden über tree-sitter AST unterstützt (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> Andrej Karpathy führt einen `/raw`-Ordner, in dem er Papers, Tweets, Screenshots und Notizen ablegt. map.mmd ist die Antwort auf dieses Problem — 71,5-fach weniger Tokens pro Abfrage gegenüber dem Lesen der Rohdateien, persistent über Sitzungen hinweg, ehrlich darüber, was gefunden vs. erschlossen wurde.

```
/map.mmd .                        # funktioniert mit jedem Ordner — Codebase, Notizen, Papers, alles
```

```
map.mmd-out/
├── graph.html       interaktiver Graph — im Browser öffnen, Knoten anklicken, suchen, filtern
├── GRAPH_REPORT.md  Gott-Knoten, überraschende Verbindungen, vorgeschlagene Fragen
├── graph.json       persistenter Graph — Wochen später abfragen, ohne neu zu lesen
└── cache/           SHA256-Cache — erneute Ausführungen verarbeiten nur geänderte Dateien
```

Füge eine `.map.mmdignore`-Datei hinzu, um Ordner auszuschließen:

```
# .map.mmdignore
vendor/
node_modules/
dist/
*.generated.py
```

Gleiche Syntax wie `.gitignore`. Du kannst eine einzelne `.map.mmdignore` im Repo-Stammverzeichnis behalten — Muster funktionieren korrekt, auch wenn map.mmd auf einem Unterordner ausgeführt wird.

## So funktioniert es

map.mmd läuft in drei Durchgängen. Zuerst extrahiert ein deterministischer AST-Durchgang Strukturen aus Code-Dateien (Klassen, Funktionen, Importe, Aufrufgraphen, Docstrings, Begründungskommentare) — ohne LLM. Zweitens werden Video- und Audiodateien lokal mit faster-whisper transkribiert, angetrieben durch einen domänenspezifischen Prompt aus Korpus-Gott-Knoten — Transkripte werden gecacht, sodass erneute Ausführungen sofort sind. Drittens laufen Claude-Subagenten parallel über Dokumente, Papers, Bilder und Transkripte, um Konzepte, Beziehungen und Designbegründungen zu extrahieren. Die Ergebnisse werden in einem NetworkX-Graphen zusammengeführt, mit Leiden-Community-Erkennung geclustert und als interaktives HTML, abfragbares JSON und ein Klartext-Audit-Report exportiert.

**Clustering basiert auf Graph-Topologie — keine Embeddings.** Leiden findet Communities durch Kantendichte. Die semantischen Ähnlichkeitskanten, die Claude extrahiert (`semantically_similar_to`, markiert als INFERRED), sind bereits im Graphen, sodass sie die Community-Erkennung direkt beeinflussen. Die Graphstruktur ist das Ähnlichkeitssignal — kein separater Embedding-Schritt oder Vektordatenbank nötig.

Jede Beziehung ist markiert als `EXTRACTED` (direkt in der Quelle gefunden), `INFERRED` (begründete Schlussfolgerung mit Konfidenzwert) oder `AMBIGUOUS` (zur Überprüfung markiert). Du weißt immer, was gefunden vs. erschlossen wurde.

## Installation

**Voraussetzungen:** Python 3.10+ und eines von: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [VS Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), [Trae](https://trae.ai), [Kiro](https://kiro.dev), Hermes oder [Google Antigravity](https://antigravity.google)

```bash
# Empfohlen — funktioniert auf Mac und Linux ohne PATH-Einrichtung
uv tool install map-mmd && map.mmd install
# oder mit pipx
pipx install map-mmd && map.mmd install
# oder einfaches pip
pip install map-mmd && map.mmd install
```

> **Offizielles Paket:** Das PyPI-Paket heißt `map-mmd` (installieren mit `pip install map-mmd`). Andere Pakete mit Namen `map.mmd*` auf PyPI sind nicht mit diesem Projekt verbunden. Das einzige offizielle Repository ist [getwinharris/map.mmd](https://github.com/getwinharris/map.mmd). CLI und Skill-Befehl heißen weiterhin `map.mmd`.

> **`map.mmd: command not found`?** Verwende `uv tool install map-mmd` (empfohlen) oder `pipx install map-mmd` — beide platzieren die CLI an einem verwalteten Ort, der automatisch im PATH ist. Mit einfachem `pip` musst du möglicherweise `~/.local/bin` (Linux) oder `~/Library/Python/3.x/bin` (Mac) zum PATH hinzufügen, oder `python -m map.mmd` verwenden.

### Plattformunterstützung

| Plattform | Installationsbefehl |
|-----------|---------------------|
| Claude Code (Linux/Mac) | `map.mmd install` |
| Claude Code (Windows) | `map.mmd install` (automatisch erkannt) oder `map.mmd install --platform windows` |
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
| Kiro IDE/CLI | `map.mmd kiro install` |
| Cursor | `map.mmd cursor install` |
| Google Antigravity | `map.mmd antigravity install` |

Dann öffne deinen KI-Coding-Assistenten und tippe:

```
/map.mmd .
```

Hinweis: Codex verwendet `$` statt `/` für Skill-Aufrufe, also tippe `$map.mmd .`.

### Assistenten immer den Graphen nutzen lassen (empfohlen)

Nach dem Erstellen eines Graphen, führe dies einmal in deinem Projekt aus:

| Plattform | Befehl |
|-----------|--------|
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
| Kiro IDE/CLI | `map.mmd kiro install` |
| Google Antigravity | `map.mmd antigravity install` |

## Verwendung

```
/map.mmd                          # aktuelles Verzeichnis verarbeiten
/map.mmd ./raw                    # spezifischen Ordner verarbeiten
/map.mmd ./raw --mode deep        # aggressivere INFERRED-Kanten-Extraktion
/map.mmd ./raw --update           # nur geänderte Dateien neu extrahieren
/map.mmd ./raw --directed         # gerichteten Graphen erstellen
/map.mmd ./raw --cluster-only     # Clustering auf bestehendem Graphen neu ausführen
/map.mmd ./raw --no-viz           # kein HTML, nur Report + JSON
/map.mmd ./raw --obsidian         # Obsidian-Vault generieren (opt-in)

/map.mmd add https://arxiv.org/abs/1706.03762   # Paper abrufen, speichern, Graphen aktualisieren
/map.mmd add <video-url>                         # Audio herunterladen, transkribieren, hinzufügen
/map.mmd query "was verbindet Attention mit dem Optimizer?"
/map.mmd path "DigestAuth" "Response"
/map.mmd explain "SwinTransformer"

map.mmd hook install              # Git-Hooks installieren
map.mmd update ./src              # Code-Dateien neu extrahieren, kein LLM benötigt
map.mmd watch ./src               # Graphen bei Änderungen automatisch aktualisieren
```

## Was du bekommst

**Gott-Knoten** — Konzepte mit dem höchsten Grad (durch die alles fließt)

**Überraschende Verbindungen** — nach Composite-Score eingestuft. Code-Paper-Kanten werden höher bewertet. Jedes Ergebnis enthält ein Klartext-Warum.

**Vorgeschlagene Fragen** — 4-5 Fragen, die der Graph einzigartig gut beantworten kann

**Das „Warum"** — Docstrings, Inline-Kommentare (`# NOTE:`, `# IMPORTANT:`, `# HACK:`, `# WHY:`), und Designbegründungen aus Dokumenten werden als `rationale_for`-Knoten extrahiert.

**Konfidenzwerte** — jede INFERRED-Kante hat einen `confidence_score` (0,0-1,0).

**Token-Benchmark** — wird automatisch nach jeder Ausführung gedruckt. Auf einem gemischten Korpus: **71,5-fach** weniger Tokens pro Abfrage gegenüber Rohdateien.

**Auto-Sync** (`--watch`) — läuft im Hintergrund und aktualisiert den Graphen bei Codeänderungen automatisch.

**Git-Hooks** (`map.mmd hook install`) — installiert Post-Commit- und Post-Checkout-Hooks.

## Datenschutz

map.mmd sendet Dateiinhalte an die Modell-API deines KI-Assistenten für semantische Extraktion von Dokumenten, Papers und Bildern. Code-Dateien werden lokal via tree-sitter AST verarbeitet — kein Dateiinhalt verlässt dein Gerät für Code. Video- und Audiodateien werden lokal mit faster-whisper transkribiert. Keine Telemetrie, keine Nutzungsverfolgung.

## Tech-Stack

NetworkX + Leiden (graspologic) + tree-sitter + vis.js. Semantische Extraktion via Claude, GPT-4 oder welches Modell deine Plattform verwendet. Video-Transkription via faster-whisper + yt-dlp (optional).

## Auf map.mmd aufgebaut — Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) ist die Enterprise-Schicht über map.mmd. Wo map.mmd einen Ordner mit Dateien in einen Wissensgraphen verwandelt, wendet Penpax denselben Graphen auf dein gesamtes Arbeitsleben an — kontinuierlich.

**Kostenlose Testversion startet bald.** [Auf die Warteliste setzen →](https://safishamsi.github.io/penpax.ai)

## Star-Verlauf

[![Star History Chart](https://api.star-history.com/svg?repos=getwinharris/map.mmd&type=Date)](https://star-history.com/#getwinharris/map.mmd&Date)
