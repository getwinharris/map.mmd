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

<div dir="rtl">

**مهارة لمساعد برمجة الذكاء الاصطناعي.** اكتب `/map.mmd` في Claude Code أو Codex أو OpenCode أو Cursor أو Gemini CLI أو GitHub Copilot CLI أو VS Code Copilot Chat أو Aider أو OpenClaw أو Factory Droid أو Trae أو Hermes أو Kiro أو Google Antigravity — يقرأ ملفاتك ويبني رسماً بيانياً للمعرفة ويعيد إليك البنية التي لم تكن تعلم بوجودها. افهم قاعدة الكود بشكل أسرع. اكتشف "السبب" وراء القرارات المعمارية.

متعدد الوسائط بالكامل. أضف كوداً أو ملفات PDF أو markdown أو لقطات شاشة أو رسوماً بيانية أو صور سبورة أو صوراً بلغات أخرى أو ملفات فيديو وصوت — يستخرج map.mmd المفاهيم والعلاقات من كل ذلك ويربطها في رسم بياني واحد. يتم نسخ مقاطع الفيديو محلياً باستخدام Whisper. يدعم 25 لغة برمجة عبر tree-sitter AST (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> يحتفظ Andrej Karpathy بمجلد `/raw` يضع فيه الأوراق البحثية والتغريدات ولقطات الشاشة والملاحظات. map.mmd هو الإجابة على تلك المشكلة — **71.5 مرة** أقل في الرموز لكل استعلام مقارنةً بقراءة الملفات الخام، مستمر عبر الجلسات، صادق حول ما تم العثور عليه مقابل ما تم استنتاجه.

</div>

```
/map.mmd .                        # يعمل مع أي مجلد — الكود، الملاحظات، الأوراق البحثية، كل شيء
```

```
map.mmd-out/
├── graph.html       رسم بياني تفاعلي — افتحه في أي متصفح، انقر على العقد، ابحث، صفّ
├── GRAPH_REPORT.md  عقد الإله، الاتصالات المفاجئة، الأسئلة المقترحة
├── graph.json       رسم بياني دائم — استعلم بعد أسابيع دون إعادة القراءة
└── cache/           ذاكرة تخزين مؤقت SHA256 — إعادة التشغيل تعالج الملفات المتغيرة فقط
```

<div dir="rtl">

أضف ملف `.map.mmdignore` لاستبعاد المجلدات:

</div>

```
# .map.mmdignore
vendor/
node_modules/
dist/
*.generated.py
```

<div dir="rtl">

نفس صيغة `.gitignore`.

## كيف يعمل

يعمل map.mmd في ثلاث مراحل. أولاً، تمريرة AST حتمية تستخرج البنية من ملفات الكود (الفئات، الدوال، الاستيرادات، رسوم بيانية الاستدعاء، docstrings، تعليقات المبرر) — دون الحاجة إلى LLM. ثانياً، يتم نسخ ملفات الفيديو والصوت محلياً باستخدام faster-whisper. ثالثاً، تعمل عوامل Claude الفرعية بالتوازي على المستندات والأوراق البحثية والصور والنصوص المكتوبة لاستخراج المفاهيم والعلاقات ومبررات التصميم. يتم دمج النتائج في رسم بياني NetworkX وتجميعها باستخدام Leiden وتصديرها كـ HTML تفاعلي وJSON قابل للاستعلام وتقرير تدقيق بلغة طبيعية.

**التجميع مبني على طوبولوجيا الرسم البياني — بدون embeddings.** يجد Leiden المجتمعات بواسطة كثافة الحواف. حواف التشابه الدلالي التي يستخرجها Claude (`semantically_similar_to`، مصنفة INFERRED) موجودة بالفعل في الرسم البياني. بنية الرسم البياني هي إشارة التشابه — لا حاجة لخطوة embedding منفصلة أو قاعدة بيانات متجهية.

كل علاقة مصنفة كـ `EXTRACTED` (وجدت مباشرة في المصدر) أو `INFERRED` (استنتاج معقول مع درجة ثقة) أو `AMBIGUOUS` (مُعلَّمة للمراجعة).

## التثبيت

**المتطلبات:** Python 3.10+ وواحد من: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [VS Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), [Trae](https://trae.ai), [Kiro](https://kiro.dev), Hermes, أو [Google Antigravity](https://antigravity.google)

</div>

```bash
# موصى به — يعمل على Mac وLinux دون إعداد PATH
uv tool install map-mmd && map.mmd install
# أو مع pipx
pipx install map-mmd && map.mmd install
# أو pip العادي
pip install map-mmd && map.mmd install
```

<div dir="rtl">

> **الحزمة الرسمية:** اسم حزمة PyPI هو `map-mmd` (تثبيت بـ `pip install map-mmd`). الحزم الأخرى المسماة `map.mmd*` على PyPI ليست تابعة لهذا المشروع. المستودع الرسمي الوحيد هو [getwinharris/map.mmd](https://github.com/getwinharris/map.mmd).

### دعم المنصات

| المنصة | أمر التثبيت |
|--------|-------------|
| Claude Code (Linux/Mac) | `map.mmd install` |
| Claude Code (Windows) | `map.mmd install` (كشف تلقائي) أو `map.mmd install --platform windows` |
| Codex | `map.mmd install --platform codex` |
| OpenCode | `map.mmd install --platform opencode` |
| GitHub Copilot CLI | `map.mmd install --platform copilot` |
| VS Code Copilot Chat | `map.mmd vscode install` |
| Aider | `map.mmd install --platform aider` |
| OpenClaw | `map.mmd install --platform claw` |
| Factory Droid | `map.mmd install --platform droid` |
| Trae | `map.mmd install --platform trae` |
| Gemini CLI | `map.mmd install --platform gemini` |
| Hermes | `map.mmd install --platform hermes` |
| Kiro IDE/CLI | `map.mmd kiro install` |
| Cursor | `map.mmd cursor install` |
| Google Antigravity | `map.mmd antigravity install` |

افتح مساعد الكود الذكاء الاصطناعي واكتب:

</div>

```
/map.mmd .
```

<div dir="rtl">

ملاحظة: يستخدم Codex `$` بدلاً من `/` للمهارات، لذا اكتب `$map.mmd .`.

## الاستخدام

</div>

```
/map.mmd                          # المجلد الحالي
/map.mmd ./raw                    # مجلد محدد
/map.mmd ./raw --update           # إعادة استخراج الملفات المتغيرة فقط
/map.mmd ./raw --directed         # رسم بياني موجّه
/map.mmd ./raw --no-viz           # تقرير + JSON فقط، بدون HTML
/map.mmd ./raw --obsidian         # إنشاء Obsidian vault

/map.mmd add https://arxiv.org/abs/1706.03762   # جلب ورقة بحثية
/map.mmd add <video-url>                         # تحميل صوت، نسخ، إضافة
/map.mmd query "ما الذي يربط Attention بالمحسِّن؟"
/map.mmd path "DigestAuth" "Response"
/map.mmd explain "SwinTransformer"

map.mmd hook install              # تثبيت Git hooks
map.mmd update ./src              # إعادة استخراج ملفات الكود، بدون LLM
map.mmd watch ./src               # تحديث تلقائي للرسم البياني
```

<div dir="rtl">

## ما ستحصل عليه

**عقد الإله** — المفاهيم ذات أعلى درجة (كل شيء يمر بها)

**الاتصالات المفاجئة** — مرتبة حسب الدرجة المركبة. حواف الكود-الورقة البحثية تحصل على تصنيف أعلى. كل نتيجة تتضمن سبباً بلغة طبيعية.

**الأسئلة المقترحة** — 4-5 أسئلة الرسم البياني في وضع فريد للإجابة عليها

**"السبب"** — يتم استخراج docstrings والتعليقات المضمنة (`# NOTE:`, `# IMPORTANT:`, `# HACK:`, `# WHY:`) ومبررات التصميم كعقد `rationale_for`.

**درجات الثقة** — كل حافة INFERRED لها `confidence_score` (0.0-1.0).

**معيار الرموز** — يُطبع تلقائياً بعد كل تشغيل. على مجموعة بيانات مختلطة: **71.5 مرة** أقل في الرموز لكل استعلام مقارنةً بالملفات الخام.

**المزامنة التلقائية** (`--watch`) — يحدّث الرسم البياني تلقائياً عند تغيير الكود.

**Git hooks** (`map.mmd hook install`) — يثبّت خطافات post-commit وpost-checkout.

## الخصوصية

يرسل map.mmd محتوى الملفات إلى API نموذج مساعد الذكاء الاصطناعي الخاص بك للاستخراج الدلالي من المستندات والأوراق البحثية والصور. تتم معالجة ملفات الكود محلياً عبر tree-sitter AST. يتم نسخ ملفات الفيديو والصوت محلياً باستخدام faster-whisper. لا قياس عن بُعد، لا تتبع للاستخدام.

## المكدس التقني

NetworkX + Leiden (graspologic) + tree-sitter + vis.js. استخراج دلالي عبر Claude أو GPT-4 أو نموذج منصتك. نسخ الفيديو عبر faster-whisper + yt-dlp (اختياري).

## مبني على map.mmd — Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) هو الطبقة المؤسسية فوق map.mmd. حيث يحوّل map.mmd مجلداً من الملفات إلى رسم بياني للمعرفة، يطبّق Penpax نفس الرسم البياني على حياتك المهنية بأكملها — باستمرار.

**نسخة تجريبية مجانية قريباً.** [انضم إلى قائمة الانتظار →](https://safishamsi.github.io/penpax.ai)

## سجل النجوم

</div>

[![Star History Chart](https://api.star-history.com/svg?repos=getwinharris/map.mmd&type=Date)](https://star-history.com/#getwinharris/map.mmd&Date)
