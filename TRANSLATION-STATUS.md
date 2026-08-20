# Translation status — German skill content to English

Working document. Delete it when the last row is done.

`CLAUDE.md` requires English for everything shipped. The structural rebuild is finished and
committed; the skill *prose* is still German in the plugins listed below, because the knowledge was
distilled from German sources (`docs.shopware.com/de`, the Contao manual) or written in German.

## What is finished

| Step | State |
|---|---|
| All 26 plugins restructured to domain skills | done, committed `0517ac6` |
| 831 → 117 skills, listing cost 387,742 → 33,575 characters | done |
| Loss-free verified against a backup, all 26 | done |
| `CLAUDE.md` written, `CONVENTIONS.md` rewritten in English | done, committed `8bb5fa2` |
| Repository `README.md` in English | done |
| All 25 German plugin READMEs translated, stale skill tables rebuilt | done, committed `8bb5fa2` |
| `octo-api` fully English, generated and verified | done |
| `shadcn` skills already English | done |
| Tooling in `scripts/` | done, committed |
| Git author switched to a handle | done |

## What is outstanding

**1,076 skill files, 135,916 lines of German prose.** One row per plugin, largest first. A plugin is
finished when its file count reaches zero.

| Plugin | German files | German lines | Note |
|---|--:|--:|---|
| `playwright` | 100 | 28,474 | largest single job |
| `shopware-merchant` | 268 | 26,001 | German admin menu items must stay, with an English gloss |
| `contao` | 86 | 16,565 | the `contao-manual-*` skills are the German end-user manual |
| `shopware-devops` | 41 | 8,918 | agent running |
| `swiper` | 59 | 7,393 | |
| `shopware-frontends` | 26 | 5,774 | |
| `shopware-admin` | 37 | 5,051 | |
| `gotenberg` | 52 | 4,791 | |
| `panther` | 22 | 4,672 | |
| `shadcn-vue` | 71 | 4,608 | mostly the German-authored blocks and charts files |
| `shopware-commercial` | 46 | 4,164 | |
| `flatpickr` | 21 | 3,617 | |
| `shopware-quality` | 21 | 3,183 | |
| `shopware-storefront` | 51 | 2,790 | |
| `shopware-concepts` | 24 | 2,412 | |
| `shopware-migration` | 11 | 1,862 | 1,063 files total, only 11 German |
| `shopware-framework` | 30 | 1,462 | |
| `shopware-data` | 33 | 1,286 | |
| `shopware-api` | 20 | 1,083 | |
| `shopware-apps` | 7 | 864 | |
| `shopware-core` | 20 | 373 | agent running |
| `shopware-testing` | 16 | 288 | agent running |
| `shopware-cms` | 9 | 185 | agent running |
| `shopware-checkout` | 5 | 100 | agent running, nearly done |

Measure the remaining work at any time:

```bash
python3 - <<'PY'
import glob, re, os
DE = re.compile(r'\b(der|die|das|und|nicht|werden|müssen|wird|für|mit|auf|kann|sich|von|dem|den|des|im|zum|zur|beim|über|unter|nach|durch|wenn|dann|aber|oder|auch|noch|nur|schon|siehe|sowie|ein|eine|einen|einer)\b', re.I)
for p in sorted(os.path.basename(d) for d in glob.glob('plugins/*') if os.path.isdir(d+'/skills')):
    de=[f for f in glob.glob(f'plugins/{p}/skills/*/*.md')
        if (lambda t: len(DE.findall(t)) > len(t)/400)(open(f,encoding='utf-8',errors='replace').read())]
    if de: print(f"{p:24} {len(de):4} files, "
                 f"{sum(sum(1 for _ in open(f,encoding='utf-8',errors='replace')) for f in de):6} lines")
PY
```

## How to translate a plugin

Dispatch one agent per plugin, or per group of small plugins totalling under ~10,000 lines. The
brief that worked:

- **Nothing omitted, nothing summarised.** A 200-line German file becomes a ~200-line English file.
  This is the rule that matters: the plugins are complete by design, and a translation that
  condenses breaks that.
- **Technical identifiers stay**: class names, file names, paths, commands, environment variables,
  skill / command / agent names. Translate the prose around them, and translate comments inside
  code blocks, but not the code.
- **Markdown structure exactly**: heading levels, table column counts, fenced blocks with their
  language tag, links, block quotes.
- **`## Contents` tables of contents**: translating a heading means translating its anchor too.
  `- [Überschrift](#überschrift)` → `- [Heading](#heading)`, anchor lower-cased, spaces to hyphens,
  punctuation dropped.
- **`## Source` sections**: URLs untouched, prose translated.
- German quotes „…" become "…".

Then verify:

```bash
grep -rlE '\b(der|die|das|und|werden|müssen|wird|für|mit|kann|sich)\b' plugins/<name>/skills | wc -l
find plugins/<name>/skills -mindepth 3 -name '*.md' | wc -l     # must stay 0
python3 scripts/measure-skill-budget.py . | grep <name>          # listing cost unchanged
```

Translation touches reference files only, so the listing cost must not move: descriptions live in
`scripts/domain-skills/<plugin>.json` and are already English.

## Where German is the subject, not the medium

Keep it, and gloss it:

- **`shopware-merchant`** — Shopware's German admin labels are what a user sees on screen.
  "under **Bestellungen** (Orders)" rather than "under Orders".
- **`contao` `contao-manual-*`** — the German end-user manual. Same treatment: German UI label,
  English explanation.
