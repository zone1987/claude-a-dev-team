# Translation status — German skill content to English

Working document. Delete it when the table below is empty.

`CLAUDE.md` requires English for everything shipped. The structural rebuild is finished and
committed; the skill *prose* is still German where the knowledge was distilled from German sources
(`docs.shopware.com/de`, the Contao manual) or authored in German.

## Finished and committed

| Step | Commit |
|---|---|
| All 26 plugins restructured to domain skills — 831 → 117 skills, listing cost 387 742 → 33 575 characters | `0517ac6` |
| Loss-free verified against a backup for all 26 plugins | `0517ac6` |
| `CLAUDE.md` written; `CONVENTIONS.md` rewritten in English | `8bb5fa2` |
| Repository `README.md` and all 25 German plugin READMEs translated; stale skill tables rebuilt from the real `SKILL.md` frontmatter | `8bb5fa2` |
| Tooling in `scripts/` that enforces the rules | `0517ac6` |
| Git author switched to a handle; private address removed from every file | `0517ac6` |
| `octo-api` — generated from the Ventrata OpenAPI document, verified both directions, all 39 upstream pages covered | earlier |
| `shadcn`, `shopware-core`, `shopware-checkout` skills — English | done |

## Outstanding

**934 skill files, 122,728 lines of German prose.** A plugin is finished when its row disappears.
Largest first, because that is the order in which agents should be dispatched.

| Plugin | German files | German lines |
|---|--:|--:|
| `playwright` | 100 | 28 474 |
| `shopware-merchant` | 268 | 26 001 |
| `contao` | 86 | 16 565 |
| `shopware-frontends` | 26 | 5 774 |
| `shopware-admin` | 37 | 5 051 |
| `gotenberg` | 52 | 4 791 |
| `panther` | 22 | 4 672 |
| `swiper` | 29 | 4 620 |
| `shadcn-vue` | 71 | 4 608 |
| `shopware-commercial` | 46 | 4 164 |
| `flatpickr` | 7 | 2 764 |
| `shopware-storefront` | 41 | 2 649 |
| `shopware-concepts` | 24 | 2 412 |
| `shopware-quality` | 5 | 2 320 |
| `shopware-migration` | 11 | 1 862 |
| `shopware-framework` | 30 | 1 462 |
| `shopware-data` | 25 | 1 173 |
| `shopware-api` | 20 | 1 083 |
| `shopware-devops` | 2 | 946 |
| `shopware-apps` | 7 | 864 |
| `shopware-testing` | 16 | 288 |
| `shopware-cms` | 9 | 185 |

Re-measure at any time:

```bash
python3 - <<'PYEOF'
import glob, re, os
DE = re.compile(r'\b(der|die|das|und|nicht|werden|müssen|wird|für|mit|auf|kann|sich|von|dem|den|des|im|zum|zur|beim|über|unter|nach|durch|wenn|dann|aber|oder|auch|noch|nur|schon|siehe|sowie|ein|eine|einen|einer)\b', re.I)
for p in sorted(os.path.basename(d) for d in glob.glob('plugins/*') if os.path.isdir(d+'/skills')):
    de=[f for f in glob.glob(f'plugins/{p}/skills/*/*.md')
        if (lambda t: len(DE.findall(t)) > len(t)/400)(open(f,encoding='utf-8',errors='replace').read())]
    if de: print(f"{p:24} {len(de):4} files, "
                 f"{sum(sum(1 for _ in open(f,encoding='utf-8',errors='replace')) for f in de):6} lines")
PYEOF
```

## How to translate a plugin

One agent per plugin, or per group of small plugins totalling under ~10 000 lines. The brief that
produced good results:

- **Nothing omitted, nothing summarised.** A 200-line German file becomes a ~200-line English file.
  This is the rule that matters: these plugins are complete by design, and a translation that
  condenses breaks that.
- **Technical identifiers stay**: class names, file names, paths, commands, environment variables,
  API names, skill / command / agent names. Translate the prose around them, and comments inside
  code blocks, but never the code.
- **Markdown structure exactly**: heading levels, table column counts, fenced blocks with their
  language tag, links, block quotes, image embeds (leave `assets/` paths alone).
- **`## Contents` tables of contents**: translating a heading means translating its anchor too.
  `- [Überschrift](#überschrift)` → `- [Heading](#heading)`; anchor lower-cased, spaces to hyphens,
  punctuation dropped.
- **`## Source`**: URLs untouched — a `docs.shopware.com/de/...` link stays as it is, because that
  is where the knowledge came from. Translate the prose and rename a `## Quelle` heading.
- German quotes „…" become "…".

Then verify:

```bash
grep -rlE '\b(der|die|das|und|werden|müssen|wird|für|mit|kann|sich)\b' plugins/<name>/skills | wc -l
find plugins/<name>/skills -mindepth 3 -name '*.md' | wc -l     # must stay 0
python3 scripts/measure-skill-budget.py . | grep <name>          # listing cost must not move
```

Translation touches reference files only, so the listing cost cannot change: descriptions live in
`scripts/domain-skills/<plugin>.json` and are already English.

## Where German is the subject, not the medium

Two plugins document a **German-language user interface**. Removing the labels would make the text
useless — nobody could find the menu item being described. Keep the label, add an English gloss on
first use:

- **`shopware-merchant`** — the Shopware administration. "Kataloge > Produkte > **Produkt
  hinzufügen** (Add product)", "The **Bestellungen** (Orders) area", "Click **Speichern** (Save)".
  Field names too: **Produktnummer**, **Steuersatz**, **Lagerbestand**.
- **`contao`**, the `contao-manual-*` domains — the German end-user manual. Same treatment:
  "under **Seitenstruktur** (Page Structure)".

The surrounding prose becomes fully English. The result is an English text that operates a German
interface. Do not run the German-word grep as a pass/fail check on these two — sample the prose
instead.
