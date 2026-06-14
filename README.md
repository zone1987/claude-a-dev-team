# A-Dev-Team — Development Toolkit

Ein Claude-Code-**Marketplace** mit **25 Plugins**, **738 Skills**, **42 Agents**, **52 Commands**, **6 Hooks**, **2 mitgelieferten MCP-Servern** und **Utils** — eine **wachsende Sammlung** von Wissens- und Werkzeug-Bibliotheken für verschiedene Web-Plattformen. Aktuell abgedeckt:

| Bereich | Abdeckung |
|---|---|
| **Shopware 6.7** (PHP 8.2+ / Symfony 7) | Backend/DAL, Storefront, Administration, CMS, Checkout, die drei APIs, Headless-Frontends, App-System, Commercial-Extensions, Betreiber-Doku sowie die OCTO-/Ventrata-/Go-City-API. |
| **Contao 5.x** (Symfony-basiertes CMS) | Entwicklung **und** Benutzerhandbuch. |
| **Frontend-Bibliotheken** (framework-agnostisch) | flatpickr (Datetime-Picker), Swiper (Touch-Slider) — weitere folgen. |
| **React-UI** | shadcn/ui — alle Komponenten (Code/Props/Examples, Radix & Base UI), Blocks, Charts, Theming, eigene Registry, inkl. mitgeliefertem shadcn-MCP. |
| **Tools & APIs** | Gotenberg (Docker-basierte PDF-Generierung & -Manipulation), Playwright (E2E-Testing & Browser-Automation, inkl. mitgeliefertem Playwright-MCP), Symfony Panther (E2E-/Browser-Testing für PHP) — weitere folgen. |

Weitere Plattformen/Frameworks sind geplant — die Struktur (Themen-Plugins mit Skills/Agents/Commands/Hooks) ist bewusst erweiterbar.

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
| [`octo-api`](./plugins/octo-api/README.md) | OCTO-API (Tourismus-Ticketing), vollständig dokumentiert: Ventrata-OCTO (Core + 23 Capabilities, alle Endpunkte mit Requests/Responses/Parametern), Go-City-Trade-API und der Vergleich Ventrata ↔ Go-City. | 38 | 1 | 1 |

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

### Frontend-Bibliotheken

| Plugin | Wofür | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`flatpickr`](./plugins/flatpickr/README.md) | Leichtgewichtiger JS-Datetime-Picker (v4.6.x): alle Optionen, Tokens, Events/Hooks, Instanz-API, 67 Locales, Themes, alle Plugins. | 11 | 1 | 1 |
| [`swiper`](./plugins/swiper/README.md) | Moderner Touch-Slider/Carousel (v11/v12): komplette API (236 Parameter, 68 Methoden, 74 Events), alle Module, Swiper Element + React/Vue/Angular/Svelte/Solid, Migration. | 33 | 1 | 1 |
| [`shadcn`](./plugins/shadcn/README.md) | **shadcn/ui komplett**: alle **59 Komponenten** (kompletter Code + Props + alle Examples, **Radix & Base UI**), **27 Blocks**, **70 Charts**, Setup/CLI/components.json, Theming/Tailwind-v4/Dark-Mode, Forms, RTL, eigene **Registry** bauen — inkl. mitgeliefertem **shadcn-MCP** + Utils. | 96 | 6 | 6 |

### Tools & APIs

| Plugin | Wofür | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`gotenberg`](./plugins/gotenberg/README.md) | Gotenberg — Docker-basierte, stateless PDF-API: HTML/Markdown/URL (Chromium) & Office (LibreOffice) → PDF, Screenshots, merge/split/convert (PDF/A·PDF/UA)/flatten/encrypt/metadata/bookmarks/Factur-X/rotate/stamp/watermark, Konfiguration, Webhook, Betrieb & Clients. | 27 | 2 | 2 |
| [`playwright`](./plugins/playwright/README.md) | Playwright — E2E-Testing & Browser-Automation: Test-Runner & Library-API, **komplette API-Referenz aller ~70 Klassen**, Assertions, Fixtures, Reporter, Parallelität/Sharding, Trace Viewer, Codegen, CI/Docker, Emulation, Auth, A11y, Migration + Playwright MCP & Agent-CLI. Liefert den **Playwright-MCP-Server** mit. | 35 | 3 | 3 |
| [`panther`](./plugins/panther/README.md) | Symfony Panther — E2E-/Browser-Testing für PHP: echte Browser (WebDriver) + headless HTTP (BrowserKit), PantherTestCase/Client/Crawler-API, Interaktionen, `waitFor*`, JS/Screenshots, alle `PANTHER_*`-Env-Vars, Selenium/Docker/CI — **gegen den Paket-Quellcode verifiziert**, inkl. **Utils** (Dockerfile, CI, phpunit). | 11 | 2 | 2 |

### Weitere

| Plugin | Wofür | Skills | Agents | Commands |
|---|---|--:|--:|--:|
| [`contao`](./plugins/contao/README.md) | Vollumfängliche Bibliothek für das Contao-5.x-CMS — Entwicklung (DCA, Models, Module, Templates, alle Hooks, Referenzen) UND Bedienung (komplettes Benutzerhandbuch). | 57 | 2 | 4 |

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
