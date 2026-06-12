# claude-a-dev-team — Shopware Development Toolkit

Ein Claude-Code-**Marketplace** mit **19 Plugins**, **470 Skills**, **32 Agents**, **33 Commands** und **1 Hook** — die allumfassende Wissens- und Werkzeugbibliothek für die Entwicklung mit und in **Shopware 6.7** (PHP 8.2+, Symfony 7), inkl. Headless-Frontends, App-System, Commercial-Extensions, Betreiber-Doku und der OCTO-/Ventrata-/Go-City-API.

Das Wissen ist aus den offiziellen Quellen destilliert (Shopware-Trunk-Source, developer.shopware.com, docs.shopware.com, die offiziellen GitHub-Repos sowie die OCTO-/Ventrata-/Go-City-Doku) und in den Skills **eingebettet** (keine externen Laufzeit-Abhängigkeiten). Skills sind schlank; die Tiefe liegt in `references/`. Agents/Commands nutzen das je Aufgabe günstigste Modell (haiku/sonnet/opus).

## Installation (Claude Code)

**1. Marketplace hinzufügen** (GitHub oder lokaler Pfad):

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
```

**2. Plugin(s) installieren** — interaktiv über `/plugin` (Browse & install) oder gezielt:

```
/plugin install shopware-core@claude-a-dev-team
/plugin install shopware-data@claude-a-dev-team
/plugin install octo-api@claude-a-dev-team
# ... je nach Bedarf
```

**3. Nutzung:** Skills laden bei passendem Kontext automatisch; Commands stehen als `/<command>` bereit; Agents werden vom Orchestrator `shopware-dev` (bzw. `octo-api-expert`, `shopware-merchant-guide`) oder direkt genutzt.

> Tipp: Für reine Shopware-Entwicklung genügen oft `shopware-core`, `shopware-data`, `shopware-framework`, `shopware-storefront`, `shopware-admin`. Headless zusätzlich `shopware-frontends`/`shopware-api`; Bedienung/Betrieb `shopware-merchant`.

### Alternativ via settings.json

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

Jedes Plugin ist ein eigenständig installierbares Themenpaket. Details in der jeweiligen Plugin-README (Plugin-Name verlinkt).

### Entwicklung — Backend, Daten & Domänen

| Plugin | Wofür | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-core`](./plugins/shopware-core/README.md) | Plugin-Fundament: DI, Decoration, Events/Subscriber, CLI, Config, Logging, Filesystem, Rate-Limiter, Feature-Flags, NumberRange, SystemConfig + Event-Katalog. | 18 | 3 | 4 |
| [`shopware-data`](./plugins/shopware-data/README.md) | DAL komplett (Entities/Fields/Flags/Associations/Translations/Criteria/Hydration) + vollständige Core-Entity-Referenz (312 Entities) + Entity-Introspektion. | 33 | 2 | 5 |
| [`shopware-framework`](./plugins/shopware-framework/README.md) | ScheduledTasks, MessageQueue, Rules, Flow, Store-/Admin-API-Routen, ACL, Webhooks, App-Scripts, Mail (+Variablen-Baum), Media, Elasticsearch, Redis. | 25 | 1 | 4 |
| [`shopware-checkout`](./plugins/shopware-checkout/README.md) | Cart-Pipeline, Payment (6.7) & App-Payment, Shipping, Order-StateMachine, Dokumente (ZUGFeRD), Promotions, Kunden. | 20 | 1 | 3 |
| [`shopware-cms`](./plugins/shopware-cms/README.md) | Eigene CMS-Blöcke, CMS-Elemente und DataResolver (Erlebniswelten). | 7 | 1 | 2 |

### Entwicklung — Frontend

| Plugin | Wofür | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-storefront`](./plugins/shopware-storefront/README.md) | Controller/Pages/Twig/SCSS/Themes, JS-Storefront-Plugins, TypeScript, Accessibility + JS-Plugin-/Event-/SCSS-Introspektion. | 39 | 2 | 4 |
| [`shopware-admin`](./plugins/shopware-admin/README.md) | Vue 3 / Pinia / Vite / Meteor: Module, Komponenten, Routing, Data-Handling, Services, ACL, Admin-SDK, TypeScript + Admin-Introspektion. | 29 | 2 | 3 |
| [`shopware-frontends`](./plugins/shopware-frontends/README.md) | Headless (Shopware Frontends): api-client, composables, api-gen, cms-base, Vue 3 / Nuxt, Routing/i18n/B2B. | 19 | 1 | 0 |

### API, Apps & Commercial

| Plugin | Wofür | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-api`](./plugins/shopware-api/README.md) | Admin/Store/Sync API: Auth, Endpunkte, Requests/Responses, Header, Fehler + OpenAPI-Introspektion. | 17 | 2 | 1 |
| [`shopware-apps`](./plugins/shopware-apps/README.md) | App-System: Manifest, Webhooks, Auth/Signatur, App-Scripts, Gateways, IAP + PHP-SDK & JS-SDK. | 5 | 1 | 1 |
| [`shopware-commercial`](./plugins/shopware-commercial/README.md) | Commercial-Extensions (Entwickler-Sicht): B2B, Subscriptions, Advanced Search, Migration Assistant, DSR, Sales Agent, Nexus. | 23 | 1 | 0 |
| [`octo-api`](./plugins/octo-api/README.md) | OCTO-API (Tourismus-Ticketing): Ventrata-OCTO (Core + 23 Capabilities, alle Endpunkte), Go-City-Trade-API, Vergleich + FfOctoApi-Shopware-Integration. | 39 | 8 | 1 |

### Qualität, Tooling, Tests & Migration

| Plugin | Wofür | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-quality`](./plugins/shopware-quality/README.md) | Coding-Guidelines, ADR-Wissen, Static-Analysis (ECS/PHPStan/Deptrac/Rector) + Knowledge-Sync (Selbst-Update) + Hooks. | 15 | 2 | 3 |
| [`shopware-devops`](./plugins/shopware-devops/README.md) | shopware-cli, Recipes, PaaS, lokale Dev-Setups, Hosting/Performance, Troubleshooting, MCP-Server. | 37 | 1 | 0 |
| [`shopware-testing`](./plugins/shopware-testing/README.md) | PHPUnit (Unit/Integration/API), Fixtures/Builder/Mocks, Jest (Admin/Storefront), Playwright-E2E. | 14 | 1 | 1 |
| [`shopware-migration`](./plugins/shopware-migration/README.md) | Versions-Upgrades: 6.6 → 6.7 → 6.8, sw-* → mt-*, Webpack → Vite, Vuex → Pinia, Deprecations. | 8 | 1 | 1 |

### Wissen & Betrieb

| Plugin | Wofür | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`shopware-concepts`](./plugins/shopware-concepts/README.md) | Architektur-/Domänen-Konzepte: das Warum hinter den How-tos (DAL, API, Catalog, Checkout, CMS, Rules, Messaging, App-System). | 12 | 1 | 0 |
| [`shopware-merchant`](./plugins/shopware-merchant/README.md) | Betreiber-Wissen: Bedienung der Administration (alle Bereiche) inkl. Screenshots — aus docs.shopware.com. | 109 | 1 | 0 |

### Weitere

| Plugin | Wofür | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`contao`](./plugins/contao/README.md) | Contao-Entwicklung (separates CMS). | 1 | 0 | 0 |

## Konzepte

- **Skills** = Wissen/Referenz (schlanke `SKILL.md` + tiefe `references/`).
- **Agents** = Spezialisten/Orchestratoren, die mehrstufige Aufgaben autonom erledigen und delegieren.
- **Commands** = Scaffolder/Lookups (`/sw-entity`, `/sw-cms-element`, `/octo-lookup`, …).
- **Hooks** = Automatik (Lint-/Katalog-Reminder nach Datei-Änderungen).
- **Introspektion** = gecachte Kataloge des KONKRETEN Projekts (Entities, JS-Plugins, JS-Events, Admin-Bausteine, API-Endpunkte) via `/sw-entity-map`, `/sw-js-plugin-map`, `/sw-admin-map`, `/sw-api-map`, `/sw-event-map`.

## Aktualität / Selbst-Update

`shopware-quality` enthält einen **Knowledge-Sync** (Agent `shopware-librarian`, Command `/sw-sync`), der das Upstream-Repo `shopware/shopware` (Releases/Tags-API + Trunk-Diff) prüft und betroffene Skills vorschlägt/aktualisiert.

## Lizenz & Autor

proprietary — Andreas Gerhardt, A-Dev-Team.
