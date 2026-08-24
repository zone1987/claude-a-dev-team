# Plan: carry the whole Shopware 6.7 developer documentation

779 pages of `developer.shopware.com/docs` become reference files inside the 15 existing
`shopware-*` plugins, without adding a single model-visible skill. Progress is tracked page by page
in [`SHOPWARE-DOCS-CHECKLIST.json`](SHOPWARE-DOCS-CHECKLIST.json), with a readable view in
[`SHOPWARE-DOCS-CHECKLIST.md`](SHOPWARE-DOCS-CHECKLIST.md).

## Contents

- [What the numbers say](#what-the-numbers-say)
- [The constraint that shapes everything](#the-constraint-that-shapes-everything)
- [Version strategy](#version-strategy)
- [Every fact carries its source](#every-fact-carries-its-source)
- [Page to plugin assignment](#page-to-plugin-assignment)
- [The per-page procedure](#the-per-page-procedure)
- [Order of work](#order-of-work)
- [Definition of done](#definition-of-done)
- [What could go wrong](#what-could-go-wrong)

## What the numbers say

`https://developer.shopware.com/sitemap.xml` lists 2,715 URLs. 2,330 sit under `/docs/`, of which
1,366 are the archived `v6.5` and `v6.6` trees. The unversioned tree is the current release, 6.7,
and there is no `/v6.7/` prefix — 964 URLs, 779 of them actual pages.

Coverage today: **16 of those 964 URLs are cited anywhere in the marketplace.** The plugins do carry
Shopware knowledge, but almost none of it is traceable to a page. Sampled against the live pages,
depth per topic ranges from 0 % to 100 % of the identifiers a page names — so this is a real gap,
not a bookkeeping one.

## The constraint that shapes everything

The skill listing budget is 8,000 characters. What matters is not the marketplace total but the
**set a session actually enables** — and the Shopware plugins are deliberately separate products, not
one family that loads together. Checkout knowledge is needed while working on checkout; frontends
only when building a headless storefront.

Measured per realistic set:

| Working set | Plugins | Skills | Chars | % |
|---|---:|---:|---:|---:|
| headless (`frontends` + `api`) | 2 | 6 | 1,758 | 21 % |
| ops (`devops` + `quality`) | 2 | 8 | 2,298 | 28 % |
| app dev (`apps` + `core` + `api`) | 3 | 8 | 2,327 | 29 % |
| storefront (`core` + `storefront` + `cms`) | 3 | 10 | 2,873 | 35 % |
| admin (`core` + `admin` + `data`) | 3 | 11 | 3,195 | 39 % |
| backend (`core` + `framework` + `data` + `testing`) | 4 | 14 | 3,976 | 49 % |
| **everything a plugin developer might touch** | 7 | 25 | 7,152 | **89 %** |

The last row is the one to design against, and it is also the one nobody actually runs: even a
full-stack plugin task touches admin *or* storefront *or* checkout at a given moment, not all seven
at once. That is what the orchestrator is for.

### The orchestrator is what makes per-plugin growth safe

`shopware-core` ships **`shopware-dev`**, the entry point for any Shopware task: it assigns the task
to a domain, loads the matching `sw-*` skills and delegates to the domain specialist — each of which
lives in its own plugin (`shopware-data:shopware-dal-expert`, `shopware-cms:shopware-cms`, and so
on). A specialist runs in its own context window, so the main conversation pays for a summary rather
than for the domain's whole reference set.

This has two consequences for how the pages are carried:

- **Each plugin is built out as a standalone product.** A plugin is enabled because its domain is
  the work at hand, so it may carry the full depth of its area — `shopware-devops` can hold all 129
  hosting pages without any cost to a session that never enables it.
- **Skill count still matters, but per plugin rather than per marketplace.** A plugin at 4 skills
  costs ~1,150 characters in the sets that include it. Growth goes into `references/` first; a new
  skill is justified only when a genuinely separate domain appears that a reference map cannot
  express, and it is measured against the 7-plugin worst case before it ships.

The orchestrator's delegation table therefore has to stay complete: a plugin missing from it is a
plugin `shopware-dev` never reaches, so its knowledge is unreachable in practice. Five plugins are
missing from it today (`devops`, `commercial`, `concepts`, `frontends`, `merchant`) and adding them
is part of this work.

## Version strategy

Only 6.7 is carried. The `v6.5` and `v6.6` trees are deliberately skipped — they are archives, and
duplicating them would triple the content for knowledge nobody writes against.

6.8 will come, so the layout must not need rewriting when it does:

- **Version lives in the file, not in the path.** A reference file states the version its facts hold
  for (`Since 6.7.4.0`, `6.7 only`, `unchanged since 6.5`), the way the upstream pages do. No
  `references/v6.7/` directory — that is the nesting `DEPTH-01` forbids, and it would double every
  path on the first migration.
- **`INVENTORY.json` records the version it was taken from.** A 6.8 refresh compares hashes against
  the recorded 6.7 state and names exactly which pages moved.
- **A page that changes between versions is one file, with both facts.** "6.7: X. From 6.8: Y."
  costs a line; a parallel tree costs a maintenance surface.
- **`shopware-migration` owns the deltas.** Version-to-version change belongs there, so the domain
  plugins stay about the current release.

## Every fact carries its source

Non-negotiable, and the reason the checklist exists:

1. **Each reference file cites the exact pages it came from** — the full URL plus a retrieval date,
   never the docs root. `SRC-02`, `SRC-06`
2. **Each page's hash goes into the plugin's `INVENTORY.json`**, so any statement can be checked
   against the version it was taken from, and a later refresh names what moved. `COV-09`, `COV-10`
3. **A claim with no page behind it does not get written.** Where the upstream is silent on
   something a reader would look for, the file says the upstream is silent rather than filling the
   gap from memory. `COV-04`
4. **Fetch with `curl -sSfL`.** `urllib` fails on this host family — measured: 0 pages against 586
   for `docs.contao.org`. `SOURCE-03`

## Page to plugin assignment

Every one of the 779 pages is assigned; there is no "unassigned" bucket.

| Plugin | Pages | Skills today | Source area |
|---|---:|---:|---|
| `shopware-quality` | 188 | 3 | `resources/references/adr` (158), `resources/guidelines` |
| `shopware-devops` | 129 | 5 | `guides/hosting`, `products/paas`, `products/tools`, Elasticsearch, Redis |
| `shopware-commercial` | 116 | 4 | `products/extensions` (B2B, subscriptions, search, migration assistant) |
| `shopware-apps` | 65 | 2 | `guides/plugins/apps`, `resources/references/app-reference` |
| `shopware-core` | 59 | 3 | plugin fundamentals, architecture, services, dependencies, DI |
| `shopware-storefront` | 46 | 5 | `guides/plugins/plugins/storefront`, `guides/plugins/themes`, page loaders |
| `shopware-admin` | 43 | 4 | `guides/plugins/plugins/administration` |
| `shopware-concepts` | 32 | 2 | `concepts/*` |
| `shopware-testing` | 27 | 3 | `guides/development/testing`, plugin testing |
| `shopware-framework` | 21 | 4 | rule and flow builder, message queue, content |
| `shopware-data` | 18 | 4 | data handling, custom fields, database migrations |
| `shopware-checkout` | 17 | 4 | checkout guides, the cart process |
| `shopware-migration` | 9 | 2 | `guides/upgrades-migrations` |
| `shopware-api` | 6 | 3 | API and Store API guides, integrations |
| `shopware-cms` | 3 | 2 | `guides/plugins/plugins/content/cms` |

Two plugins carry no pages and stay as they are: `shopware-frontends` (its source is
`frontends.shopware.com`, a separate site) and `shopware-merchant` (`docs.shopware.com`, the
merchant documentation).

## The per-page procedure

Per page, in this order:

1. **Fetch** with `curl -sSfL`, into the local mirror. Record the sha256.
2. **Extract** the text, then read it — the identifiers, tables, code blocks, version notes and
   caveats, not a summary of the prose.
3. **Locate or create** the reference file in the assigned plugin. Prefer extending an existing file
   on the same subject over adding one: `REF-02` forbids a pointer file, and a subject split across
   two files costs two reads.
4. **Write the facts**, each with its type, default, optionality and version where the page states
   them. Where the page is thin, say so. `COV-04`, `COV-07`
5. **Cite** the page URL and retrieval date in the file's `## Source` section.
6. **Link** the file from `SKILL.md`'s reference map, with a note on what it holds. `LINK-01`
7. **Record** the page hash in the plugin's `INVENTORY.json`.
8. **Tick** the page in `SHOPWARE-DOCS-CHECKLIST.json`.
9. **Validate**: `validate_plugin.py --plugin <name> --strict` must stay clean.

## Order of work

Smallest plugins first — they prove the procedure at low cost and finish quickly, so progress is
visible and a mistake is cheap to undo.

| Phase | Plugins | Pages |
|---|---|---:|
| 1 | `shopware-cms`, `shopware-api`, `shopware-migration` | 18 |
| 2 | `shopware-checkout`, `shopware-data`, `shopware-framework` | 56 |
| 3 | `shopware-testing`, `shopware-concepts` | 59 |
| 4 | `shopware-admin`, `shopware-storefront` | 89 |
| 5 | `shopware-core`, `shopware-apps` | 124 |
| 6 | `shopware-commercial`, `shopware-devops` | 245 |
| 7 | `shopware-quality` (158 ADRs plus guidelines) | 188 |

The ADRs are last on purpose: they are 158 dated decision records, many superseded, and the right
shape for them (one file per year? one index plus the live ones?) is easier to judge once the rest
of the marketplace is complete.

## Definition of done

A page is `done` when all of these hold, and `validate_plugin.py --strict` is clean for its plugin:

- its facts are in a reference file under `skills/<skill>/references/`
- that file cites the page URL and a retrieval date
- the file is linked directly from `SKILL.md`
- the page hash is in the plugin's `INVENTORY.json`
- the plugin's skill count is unchanged from before this work

A page marked `skip` carries a reason in the checklist. Anything else stays `todo`.

## What could go wrong

- **Budget creep through the back door.** Adding reference files is free, but editing a
  `SKILL.md` reference map is not — a longer map is a longer loaded body on every turn. Keep maps at
  the 40-line limit by grouping companions on one line.
- **Duplication between plugins.** `guides/plugins/plugins/framework/*` touches four plugins. The
  assignment above is the single answer per page; where two plugins genuinely need the same fact,
  one carries it and the other reaches it with the Skill tool. `SHARE-01`
- **Silent thinning.** The temptation on a 158-page tree is to summarise. The checklist plus the
  term-level audit is what catches that: a page is not done because a file mentions its topic.

## Source

Page list from [developer.shopware.com/sitemap.xml](https://developer.shopware.com/sitemap.xml),
retrieved 2026-08-21: 2,715 URLs, 2,330 under `/docs/`, 964 on the current (6.7) tree, 779 of them
pages. Budget figures from `scripts/measure-skill-budget.py`. Rule ids refer to
[`RULES.md`](RULES.md).
