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
| `shopware-devops`, `shopware-testing` skills — English | `e975ee4` |
| Batches that landed before the translation agents were stopped: `shadcn-vue` forms, `contao` platform topics, `shopware-storefront`, single files elsewhere | `bc6528c` |
| `playwright` API reference — 48 files; German demo strings in example code unified plugin-wide | `5feea5d`, `9f9c6b9` |
| `contao` fully English — five developer domains + three manual domains (87 files) | `c8195bb` |
| `shopware-frontends`, `shopware-admin` fully English (65 files) | `c8195bb` |
| 326 backtick-wrapped link targets repaired in 86 files; 25 links into deleted directories resolved; 0 dead relative links remain | `c8195bb` |
| Every platform claim in `CLAUDE.md` sourced; four inaccuracies corrected | `e239c45`, `654750d`, `04262ed` |
| English-only rule anchored as its own `CLAUDE.md` section | `580971c` |

## Outstanding

**557 skill files, 57 894 lines of German prose.** A plugin is finished when its row disappears.
Largest first, because that is the order in which agents should be dispatched.

| Plugin | German files | German lines |
|---|--:|--:|
| `shopware-merchant` | 268 | 26 001 |
| `shadcn-vue` | 68 | 5 549 |
| `shopware-commercial` | 48 | 4 660 |
| `swiper` | 19 | 3 511 |
| `playwright` | 8 | 2 622 |
| `shopware-storefront` | 17 | 2 433 |
| `shopware-concepts` | 24 | 2 412 |
| `shopware-migration` | 11 | 1 862 |
| `shopware-framework` | 31 | 1 639 |
| `flatpickr` | 3 | 1 455 |
| `shopware-quality` | 2 | 1 335 |
| `shopware-api` | 20 | 1 083 |
| `shopware-apps` | 8 | 1 041 |
| `shopware-data` | 5 | 769 |
| `panther` | 2 | 530 |
| `shopware-devops` | 3 | 389 |
| `contao` | 1 | 308 |
| `shopware-cms` | 9 | 185 |
| `gotenberg` | 10 | 110 |

Measured at commit `c8195bb` with the snippet below, **widened** to also flag transliterated German
(`fuer`, `ueber`, `koennen`, `vollstaendig`, `Fazit`, `Beschreibung`). That is why some rows moved up
rather than down: agents repeatedly found files the stopword-only pattern had missed — short stubs
whose sole German was a heading plus `Vollständige Referenz:`, and whole files written without
umlauts. Treat both patterns as blocking, per `CLAUDE.md`.

`playwright`'s 8 remaining files are the Android/Electron device classes and `API-TESTING-DETAIL.md`;
they were skipped by a prefix-based work split and are almost entirely umlaut-free German.

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
