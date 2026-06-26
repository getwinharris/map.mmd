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
</p>

**En färdighet för AI-kodassistenter.** Skriv `/map.mmd` i Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro eller Google Antigravity — den läser dina filer, bygger ett kunskapsgrafer och ger tillbaka strukturen du inte visste fanns. Förstå en kodbas snabbare. Hitta "varför" bakom arkitekturella beslut.

Helt multimodal. Lägg till kod, PDF:er, markdown, skärmdumpar, diagram, whiteboardfoton, bilder på andra språk eller video- och ljudfiler — map.mmd extraherar begrepp och relationer från allt och kopplar samman dem i ett enda graf. Videor transkriberas lokalt med Whisper. Stödjer 25 programmeringsspråk via tree-sitter AST.

> Andrej Karpathy håller en `/raw`-mapp där han lägger papper, tweets, skärmdumpar och anteckningar. map.mmd är svaret på det problemet — **71,5x** färre tokens per fråga jämfört med att läsa råfiler, beständigt mellan sessioner.

```
/map.mmd .
```

```
map.mmd-out/
├── graph.html       interaktivt diagram — öppna i valfri webbläsare
├── GRAPH_REPORT.md  gudnoder, överraskande kopplingar, föreslagna frågor
├── graph.json       beständigt diagram — kan frågas veckor senare
└── cache/           SHA256-cache — upprepade körningar behandlar bara ändrade filer
```

## Hur det fungerar

map.mmd arbetar i tre pass. Först extraherar ett deterministiskt AST-pass struktur från kodfiler utan LLM. Sedan transkriberas video- och ljudfiler lokalt med faster-whisper. Slutligen kör Claude-subagenter parallellt på dokument, papper, bilder och transkriptioner. Resultaten slås samman i ett NetworkX-diagram, klustras med Leiden och exporteras som interaktiv HTML, frågebar JSON och revisionsrapport.

Varje relation är märkt `EXTRACTED`, `INFERRED` (med konfidenspoäng) eller `AMBIGUOUS`.

## Installation

**Krav:** Python 3.10+ och ett av: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com) med flera.

```bash
uv tool install map-mmd && map.mmd install
# eller med pipx
pipx install map-mmd && map.mmd install
# eller pip
pip install map-mmd && map.mmd install
```

> **Officiellt paket:** PyPI-paketet heter `map-mmd`. Det enda officiella förrådet är [getwinharris/map.mmd](https://github.com/getwinharris/map.mmd).

## Användning

```
/map.mmd .
/map.mmd ./raw --update
/map.mmd query "vad kopplar Attention till optimizern?"
/map.mmd path "DigestAuth" "Response"
map.mmd hook install
map.mmd update ./src
```

## Vad du får

**Gudnoder** — begrepp med högst grad · **Överraskande kopplingar** — rangordnade efter poäng · **Föreslagna frågor** · **"Varför"** — docsträngar och designmotivering extraherade som noder · **Token-benchmark** — **71,5x** färre tokens på blandat korpus.

## Integritet

Kodfiler behandlas lokalt via tree-sitter AST. Videor transkriberas lokalt med faster-whisper. Ingen telemetri.

## Byggt på map.mmd — Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) är enterprise-lagret ovanpå map.mmd. **Gratis provperiod kommer snart.** [Gå med i väntelistan →](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=getwinharris/map.mmd&type=Date)](https://star-history.com/#getwinharris/map.mmd&Date)
