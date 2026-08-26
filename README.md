# Claude Code plugin marketplace

A Claude Code **marketplace** of **29 plugins**, **147 skills**, **2,167** reference files and
**610,546 lines** of distilled documentation, covering Shopware 6.7, Contao 5, the OCTO
tourism API, the Discord developer platform, Project Zomboid modding, React and Vue component
libraries, and a set of testing and PDF tools.

Every plugin embeds its knowledge — no runtime dependency on the upstream site, no network call at
answer time. Depth lives in reference files that load only when needed, so a plugin costs almost
nothing until it is used.

## Installation

**1. Add the marketplace**

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
```

**2. Install the plugins you need**

```
/plugin install shopware-core@claude-a-dev-team
/plugin install shopware-data@claude-a-dev-team
/plugin install octo-api@claude-a-dev-team
```

**3. Use them.** Skills load automatically when the conversation matches their triggers; commands are
available as `/<command>`; agents are reached through an orchestrator or directly with
`@agent-<plugin>:<name>`.

> **Enable only what a project needs.** Every active skill occupies the session's skill listing
> budget — see [Context budget](#context-budget). Three to five plugins is the working range.

### Via settings.json

```jsonc
{
  "extraKnownMarketplaces": {
    "claude-a-dev-team": { "source": { "source": "github", "repo": "zone1987/claude-a-dev-team" } }
  },
  "enabledPlugins": [
    "shopware-core@claude-a-dev-team",
    "shopware-data@claude-a-dev-team"
  ]
}
```

## Plugins

### Shopware 6.7 — backend and data

| Plugin | Covers | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-core`](./plugins/shopware-core/README.md) | Shopware 6.7 plugin fundamentals: plugin base and lifecycle, dependency injection, service decoration and tags, event subscribers with the full eve… | 3 | 3 | 4 |
| [`shopware-data`](./plugins/shopware-data/README.md) | Shopware 6.7 Data Abstraction Layer: entities and definitions, all field types and flags, the four association kinds, Criteria queries, aggregation… | 4 | 2 | 5 |
| [`shopware-framework`](./plugins/shopware-framework/README.md) | Shopware 6.7 framework: Store and Admin API extension, Flow Builder, custom rules, scheduled tasks, the message queue, mail templates, media and El… | 4 | 1 | 4 |
| [`shopware-checkout`](./plugins/shopware-checkout/README.md) | Shopware 6.7 checkout: the cart pipeline (collectors, processors, validators, prices, line items), payment handlers and app payment, deliveries and… | 4 | 1 | 3 |
| [`shopware-cms`](./plugins/shopware-cms/README.md) | Shopware 6 CMS extension: custom Shopping Experience blocks with slot configuration, and custom elements with their administration component, store… | 2 | 1 | 2 |

### Shopware 6.7 — frontend

| Plugin | Covers | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-storefront`](./plugins/shopware-storefront/README.md) | Shopware 6.7 Storefront: every Twig block with its nesting, route-to-template chains, CMS resolvers, JS selectors, themes, SCSS and the checkout… | 6 | 4 | 6 |
| [`shopware-admin`](./plugins/shopware-admin/README.md) | Shopware 6.7 Administration: Vue 3 components and modules, routing, repositoryFactory data handling, Pinia stores, ACL, the Vite build, and the Met… | 4 | 2 | 3 |
| [`shopware-frontends`](./plugins/shopware-frontends/README.md) | Shopware Frontends (headless): api-client and api-gen types, composables, session context, Nuxt setup, CMS rendering, i18n, B2B and deployment — 3 … | 3 | 1 | 0 |

### Shopware 6.7 — APIs, apps, commercial

| Plugin | Covers | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-api`](./plugins/shopware-api/README.md) | Shopware 6.7 APIs: Admin API (OAuth, CRUD, Criteria search, Sync), Store API (access key and context token), plus shared headers, errors, versionin… | 3 | 2 | 1 |
| [`shopware-apps`](./plugins/shopware-apps/README.md) | Shopware 6 app system: the complete manifest.xml reference, registration and signatures, in-app purchases, plus the app-php-sdk and app-sdk-js — 2 … | 2 | 1 | 1 |
| [`shopware-commercial`](./plugins/shopware-commercial/README.md) | Shopware Commercial extensions for developers: B2B Suite and Components, Sales Agent, Digital Sales Rooms, Subscriptions, Advanced Search, Nexus, M… | 4 | 1 | 0 |
| [`octo-api`](./plugins/octo-api/README.md) | Source of truth for the OCTO tourism ticketing API: all 65 operations, 139 schemas and 254 capability fields, generated from the Ventrata OpenAPI s… | 8 | 1 | 2 |

### Shopware 6.7 — quality, tooling, migration

| Plugin | Covers | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-quality`](./plugins/shopware-quality/README.md) | Shopware code quality: the platform's coding guidelines, domain exceptions, extendability rules and ADRs, plus PHPStan, ECS, Deptrac and Rector con… | 3 | 2 | 3 |
| [`shopware-devops`](./plugins/shopware-devops/README.md) | Shopware 6 operations: shopware-cli, self-hosting (webserver, database, search, caching, workers, deployment), Shopware PaaS, development tooling a… | 5 | 1 | 0 |
| [`shopware-testing`](./plugins/shopware-testing/README.md) | Shopware 6 testing across all levels: PHPUnit (unit, integration, Store and Admin API) with fixtures, builders and mocks, Jest for administration a… | 3 | 1 | 1 |
| [`shopware-migration`](./plugins/shopware-migration/README.md) | Shopware plugin upgrades: the 6.6 to 6.7 to 6.8 path, release notes, deprecation handling, PHP migration patterns, and the three administration mig… | 2 | 1 | 1 |

### Shopware 6.7 — concepts and operations

| Plugin | Covers | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-concepts`](./plugins/shopware-concepts/README.md) | Shopware 6 concepts: why the platform is built as it is — architecture, DAL, data stores, extension mechanisms, APIs, app system, messaging, and ho… | 2 | 1 | 0 |
| [`shopware-merchant`](./plugins/shopware-merchant/README.md) | Shopware 6 merchant knowledge: operating the administration across catalogue, orders, customers, content, marketing, settings, sales channels, Comm… | 16 | 1 | 0 |

### UI libraries

| Plugin | Covers | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shadcn`](./plugins/shadcn/README.md) | shadcn/ui component library: all 59 components with full React source, props and examples for both Radix UI and Base UI, plus setup, theming, forms… | 8 | 6 | 6 |
| [`shadcn-vue`](./plugins/shadcn-vue/README.md) | shadcn-vue component library: all 64 components with full Vue source, props, slots and demos, plus setup, theming, forms, blocks, charts and custom… | 8 | 6 | 6 |
| [`swiper`](./plugins/swiper/README.md) | Swiper touch slider: the complete core API (parameters, methods, properties, events), every module, advanced features and the React, Vue, Angular, … | 4 | 1 | 1 |
| [`flatpickr`](./plugins/flatpickr/README.md) | flatpickr date picker: every option, method, event and format token, plus the official plugins, all 67 locales, themes and mobile behaviour — 2 dom… | 2 | 1 | 1 |

### Tools and services

| Plugin | Covers | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`gotenberg`](./plugins/gotenberg/README.md) | Gotenberg PDF service: HTML, URL, Markdown and Office conversion, screenshots, the full PDF manipulation set (merge, split, PDF/A, Factur-X, waterm… | 3 | 2 | 2 |
| [`playwright`](./plugins/playwright/README.md) | Playwright end-to-end testing: writing tests (locators, actions, assertions, auth), the test runner (config, fixtures, sharding, reporters), the co… | 5 | 3 | 3 |
| [`panther`](./plugins/panther/README.md) | Symfony Panther browser testing: PantherTestCase, client and crawler API, interactions and waitFor mechanics, screenshots, plus WebDriver installat… | 2 | 2 | 2 |

### Platforms and games

| Plugin | Covers | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`discord`](./plugins/discord/README.md) | The Discord developer platform, all 159 documentation pages: the HTTP API, the Gateway with every event and intent, slash commands and components, OAuth2 and the permission bitfield, Activities and the Embedded App SDK, the Social SDK, monetization, RPC and voice, plus local testing | 11 | 4 | 3 |
| [`zomboid`](./plugins/zomboid/README.md) | Project Zomboid build 42 modding, extracted from the game itself: all 3,965 Java classes and 72,831 members, the 1,395 game Lua files, 296 ISUI widget classes, 5,105 items with every script property, 37,060 world objects, RCON and 67 admin commands | 12 | 4 | 3 |

### Other platforms

| Plugin | Covers | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`contao`](./plugins/contao/README.md) | Contao 5 knowledge library: development (DCA, Models, content elements, fragment controllers, all hooks, Twig, backend modules) and the complete Ge… | 8 | 2 | 4 |
| [`zone-claude-forge`](./plugins/zone-claude-forge/README.md) | Authoring instrument for this marketplace: writes compliant skills, agents, commands and hooks, distils upstream sources into reference files, and audits e… | 6 | 2 | 4 |

## Context budget

Claude Code loads the name and description of **every** active skill into the system prompt. That
listing has a hard limit: **1 % of the context window**, so roughly 8,000 characters at 200k. Cost
per skill is `len(description) + 109`.

When the budget overflows, Claude Code shortens descriptions — **starting with the skills you invoke
least**. A skill without a description is still listed by name but no longer activates on its own; it
stays reachable as `/<plugin>:<skill>`.

Measured with `python3 scripts/measure-skill-budget.py .`. Only model-visible skills count: one carrying `disable-model-invocation` stays reachable as `/<plugin>:<skill>` and costs nothing, which is why a plugin can list more skills in the table above than here.

| Plugin | Model-visible skills | Chars | Avg description | % of budget |
|---|--:|--:|--:|--:|
| `shopware-merchant` | 16 | 4 569 | 177 | 57 % |
| `zomboid` | 12 | 3 368 | 172 | 42 % |
| `discord` | 11 | 3 003 | 164 | 38 % |
| `octo-api` | 8 | 2 296 | 178 | 29 % |
| `shadcn-vue` | 8 | 2 282 | 176 | 29 % |
| `shadcn` | 8 | 2 265 | 174 | 28 % |
| `contao` | 8 | 2 257 | 173 | 28 % |
| `shopware-storefront` | 6 | 1 758 | 184 | 22 % |
| `playwright` | 5 | 1 449 | 181 | 18 % |
| `shopware-devops` | 5 | 1 436 | 178 | 18 % |
| `shopware-admin` | 4 | 1 191 | 189 | 15 % |
| `shopware-commercial` | 4 | 1 162 | 182 | 15 % |
| `swiper` | 4 | 1 153 | 179 | 14 % |
| `shopware-data` | 4 | 1 146 | 178 | 14 % |
| `shopware-framework` | 4 | 1 146 | 178 | 14 % |
| `shopware-checkout` | 4 | 1 116 | 170 | 14 % |
| `zone-claude-forge` | 3 | 893 | 189 | 11 % |
| `gotenberg` | 3 | 892 | 188 | 11 % |
| `shopware-api` | 3 | 885 | 186 | 11 % |
| `shopware-frontends` | 3 | 873 | 182 | 11 % |
| `shopware-quality` | 3 | 862 | 178 | 11 % |
| `shopware-core` | 3 | 858 | 177 | 11 % |
| `shopware-testing` | 3 | 826 | 166 | 10 % |
| `shopware-apps` | 2 | 584 | 183 | 7 % |
| `shopware-concepts` | 2 | 573 | 178 | 7 % |
| `shopware-cms` | 2 | 564 | 173 | 7 % |
| `flatpickr` | 2 | 557 | 170 | 7 % |
| `shopware-migration` | 2 | 550 | 166 | 7 % |
| `panther` | 2 | 525 | 154 | 7 % |

Read the last column as a budget share, not as something to add up: a working set of three to
five plugins is what a session actually enables, and any such set lands well inside the limit.

| Working set | Share |
|---|--:|
| `shopware-core` + `shopware-data` + `shopware-storefront` | 47 % |
| `shopware-core` + `shopware-data` + `shopware-admin` + `shopware-framework` | 54 % |
| `octo-api` + `shopware-core` + `shopware-data` | 54 % |
| `shadcn` + `shadcn-vue` | 57 % |
| `zomboid` alone — it is a self-contained domain | 42 % |
| `discord` + `zomboid` — a bot bridging a game server | 80 % |

Enabling all 29 at once is not a supported configuration, and no plugin is written for it.

Diagnose a session with:

| Command | Shows |
|---|---|
| `/context` | the Skills row after the budget is applied |
| `/doctor` | an estimate of the listing's cost and its biggest contributors |
| `claude --debug` | the overflow warning in the debug log |

Raise it if you need to: `skillListingBudgetFraction` (e.g. `0.02` for 2 %) or
`SLASH_COMMAND_TOOL_CHAR_BUDGET` as a fixed character count. `skillOverrides` can silence individual
skills — but **not plugin skills**, which is why description length is the author's responsibility
here. The rules are in [`CLAUDE.md`](./CLAUDE.md).

## How a plugin is built

- **Skills** — knowledge. A `SKILL.md` under 120 lines maps the domain; the depth sits in flat
  sibling reference files, one level deep, loaded on demand.
- **Agents** — specialists that run in their own context window and return a summary.
- **Commands** — scaffolders and lookups (`/sw-entity`, `/octo-lookup`, …).
- **Hooks** — deterministic automation, such as a reminder after a file edit.
- **Introspection** — cached catalogues of the *concrete* project (entities, JS plugins, events,
  API endpoints) via `/sw-entity-map`, `/sw-js-plugin-map`, `/sw-admin-map`, `/sw-api-map`,
  `/sw-event-map`.

Authoring rules: [`CLAUDE.md`](./CLAUDE.md) for efficiency and completeness,
[`CONVENTIONS.md`](./CONVENTIONS.md) for naming and layout. The tooling in `scripts/` enforces both.

## Keeping it current

Four plugins check their own upstream:

- **`shopware-quality`** — agent `shopware-librarian`, command `/sw-sync`: checks
  `shopware/shopware` releases and trunk drift and reports which skills are affected.
- **`octo-api`** — command `/octo-spec-sync`: resolves the Ventrata OpenAPI URL dynamically,
  compares content hash and entity counts against `.spec-state.json`, and regenerates the
  references on request. `--check` reports, `--apply` writes.

- **`discord`** — command `/discord-docs-sync`: compares `docs.discord.com/sitemap.xml` against the
  recorded hash in `PAGE-COVERAGE.json`, reports pages added, removed or changed, and re-distils on
  `--apply`.
- **`zomboid`** — the game itself is the source, so there is no site to poll. `INVENTORY.json`
  records a content hash per source directory instead, and every reference file names the generator
  that produced it, so a game update is detected by re-running the generators and diffing.

`octo-api` also ships an audit that walks all 39 pages of the upstream documentation and reports any
term the plugin does not mention — currently 1,162 of 1,162.

`discord` and `zomboid` verify completeness in both directions rather than by page count:

| Script | Proves |
|---|---|
| `verify_references.py` (both) | every reference file is reachable from its `SKILL.md`, and every relative link resolves |
| `verify_page_coverage.py` (`discord`) | every one of the 159 documentation pages reached a skill that carries content |
| `audit_terms.py` (`discord`) | every identifier, constant, route and table number of each source page appears in the references — and, in reverse, that no documented name is absent upstream, which is what catches invention |
| `audit_structure.py` (`discord`) | no section, table or code block was dropped during distillation |
| `verify_orchestrator.py` (`zomboid`) | the orchestrator names every skill and every agent with a stated purpose — an omitted skill would otherwise never be routed to |

## Licence and sources

MIT — [zone1987](https://github.com/zone1987).

Knowledge is distilled from each project's official documentation. Rights to the original
documentation remain with the respective owners:

| Plugin family | Source |
|---|---|
| `shopware-*` | [shopware/shopware](https://github.com/shopware/shopware), developer.shopware.com, docs.shopware.com |
| `octo-api` | [docs.ventrata.com](https://docs.ventrata.com) — OCTO is an open standard by OCTO Standards NP Inc. ([octo.travel](https://octo.travel)) |
| `contao` | [contao/contao](https://github.com/contao/contao), docs.contao.org |
| `shadcn`, `shadcn-vue` | [ui.shadcn.com](https://ui.shadcn.com), [shadcn-vue.com](https://www.shadcn-vue.com) |
| `swiper`, `flatpickr`, `playwright`, `panther`, `gotenberg` | the respective upstream repository and documentation |
| `discord` | [docs.discord.com](https://docs.discord.com/developers/intro) — © Discord Inc. |
| `zomboid` | the shipped game (build 42), plus [projectzomboid.com/modding](https://projectzomboid.com/modding/index.html) and [demiurgeQuantified/ProjectZomboidJavaDocs](https://github.com/demiurgeQuantified/ProjectZomboidJavaDocs). Project Zomboid is developed by The Indie Stone |

### Other OCTO implementations

OCTO is an open standard, not a Ventrata product. Other implementers include **Peek Pro**, **Zaui**,
**Xola** and **Anchor**; **Go City** is covered in `octo-api` as a delta overlay. The specification
itself lives at [docs.octo.travel](https://docs.octo.travel) and
[github.com/octotravel](https://github.com/octotravel).
