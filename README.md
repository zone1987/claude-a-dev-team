# A-Dev-Team — Development Toolkit

Ein Claude-Code-**Marketplace** mit **26 Plugins**, **801 Skills**, **48 Agents**, **59 Commands**, **8 Hooks**, **3 mitgelieferten MCP-Servern** und **Utils** — eine **wachsende Sammlung** von Wissens- und Werkzeug-Bibliotheken für verschiedene Web-Plattformen. Aktuell abgedeckt:

| Bereich | Abdeckung |
|---|---|
| **Shopware 6.7** (PHP 8.2+ / Symfony 7) | Backend/DAL, Storefront, Administration, CMS, Checkout, die drei APIs, Headless-Frontends, App-System, Commercial-Extensions, Betreiber-Doku sowie die OCTO-/Ventrata-/Go-City-API. |
| **Contao 5.x** (Symfony-basiertes CMS) | Entwicklung **und** Benutzerhandbuch. |
| **Frontend-Bibliotheken** (framework-agnostisch) | flatpickr (Datetime-Picker), Swiper (Touch-Slider) — weitere folgen. |
| **React-UI** | shadcn/ui — alle Komponenten (Code/Props/Examples, Radix & Base UI), Blocks, Charts, Theming, eigene Registry, inkl. mitgeliefertem shadcn-MCP. |
| **Vue-UI** | shadcn-vue — Vue-Port von shadcn/ui (reka-ui): alle 64 Komponenten (Vue-Code/Props/Slots/Emits, Demos), Blocks, Charts, Forms (vee-validate/TanStack), Theming, eigene Registry, inkl. mitgeliefertem shadcn-vue-MCP. |
| **Tools & APIs** | Gotenberg (Docker-basierte PDF-Generierung & -Manipulation), Playwright (E2E-Testing & Browser-Automation, inkl. mitgeliefertem Playwright-MCP), Symfony Panther (E2E-/Browser-Testing für PHP) — weitere folgen. |

Weitere Plattformen/Frameworks sind geplant — die Struktur (Themen-Plugins mit Skills/Agents/Commands/Hooks) ist bewusst erweiterbar.

Das Wissen ist aus den offiziellen Quellen destilliert (Shopware-Trunk-Source, developer.shopware.com, docs.shopware.com, die offiziellen GitHub-Repos sowie die OCTO-/Ventrata-Spezifikation) und in den Skills **eingebettet** (keine externen Laufzeit-Abhängigkeiten). Skills sind schlank; die Tiefe liegt in flachen Referenzdateien daneben. Agents/Commands nutzen das je Aufgabe günstigste Modell (haiku/sonnet/opus).

**Regelwerk:** [`CLAUDE.md`](./CLAUDE.md) legt die verbindlichen Effizienz-Regeln fest (Listing-Budget, Description-Länge, Skill-Anzahl, Trigger-Anker), [`CONVENTIONS.md`](./CONVENTIONS.md) Benennung und Layout. Beide gelten für jedes Plugin hier.

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

**3. Nutzung:** Skills laden bei passendem Kontext automatisch; Commands stehen als `/<command>` bereit; Agents werden vom Orchestrator `shopware-dev` (bzw. `octo-integrator`, `shopware-merchant-guide`) oder direkt genutzt.

> Tipp: Für reine Shopware-Entwicklung genügen oft `shopware-core`, `shopware-data`, `shopware-framework`, `shopware-storefront`, `shopware-admin`. Headless zusätzlich `shopware-frontends`/`shopware-api`; Bedienung/Betrieb `shopware-merchant`.

> **Wichtig:** Aktiviere nur die Plugins, die du wirklich brauchst. Jeder aktive Skill belegt Platz im Skill-Listing-Budget deiner Session — siehe [Kontext-Budget](#kontext-budget).

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
| [`octo-api`](./plugins/octo-api/README.md) | OCTO-API (Tourismus-Ticketing) als **Quelle der Wahrheit**: alle 46 Endpunkte, 139 Schemas und 254 capability-abhängigen Felder — deterministisch aus der Ventrata-OpenAPI-Spezifikation generiert und maschinell verifiziert. Core (products/availability/bookings), alle 23 Capabilities, Go-City-Overlay. | 8 | 1 | 2 |

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
| [`shadcn-vue`](./plugins/shadcn-vue/README.md) | **shadcn-vue komplett** (Vue-Port, reka-ui): alle **64 Komponenten** (kompletter Vue-Code + Props/Slots/Emits + alle Demos), Blocks, Charts, Setup/CLI/components.json, Theming/Tailwind-v4/Dark-Mode, Forms (vee-validate/TanStack), eigene **Registry** — inkl. mitgeliefertem **shadcn-vue-MCP** + Utils. | 93 | 6 | 6 |

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

## Kontext-Budget

Claude Code lädt Name und Description **jedes** aktiven Skills in den System-Prompt. Dieses Listing
hat ein hartes Limit: **1 % des Kontextfensters**, also ~8.000 Zeichen bei 200k. Kosten je Skill =
`len(description) + 109`.

Läuft das Budget über, kürzt Claude Code Descriptions — **zuerst bei den am seltensten genutzten
Skills**. Ein Skill ohne Description steht weiter namentlich im Listing, wird aber nicht mehr
automatisch aktiviert. Er bleibt über `/<plugin>:<skill>` erreichbar.

Ist-Stand dieses Marketplace bei **allen 26 Plugins gleichzeitig aktiv** (`python3 scripts/measure-skill-budget.py .`):

| Plugin | Skills | Zeichen | % des Budgets |
|---|--:|--:|--:|
| shopware-merchant | 109 | 48.591 | 607 % |
| shadcn-vue | 93 | 42.448 | 531 % |
| shadcn | 96 | 38.573 | 482 % |
| contao | 57 | 29.360 | 367 % |
| shopware-devops | 37 | 19.664 | 246 % |
| playwright | 35 | 18.693 | 234 % |
| swiper | 33 | 18.516 | 231 % |
| shopware-storefront | 39 | 17.804 | 223 % |
| … 17 weitere | 294 | 139.570 | 1.745 % |
| `octo-api` (Referenz-Implementierung) | 8 | 2.392 | **30 %** |
| **gesamt** | **801** | **375.611** | **4.695 %** |

`octo-api` zeigt, was die Regeln in [`CLAUDE.md`](./CLAUDE.md) bewirken: von 38 Skills und 14.523
Zeichen auf 8 Skills und 2.392 Zeichen — bei vollständiger, maschinell verifizierter Abdeckung aller
65 Endpunkte.

**Praktische Folge:** Aktiviere pro Projekt nur die Plugins, die du brauchst. Drei bis fünf Plugins
liegen im tragfähigen Bereich; alle gleichzeitig sind es nicht.

Diagnose in einer Session:

| Befehl | Zweck |
|---|---|
| `/context` | zeigt die Skills-Zeile nach Anwendung des Budgets |
| `/doctor` | schätzt die Listing-Kosten und nennt die größten Verursacher |
| `claude --debug` | protokolliert die Overflow-Warnung |

Reicht das Budget nicht, lässt es sich anheben — `skillListingBudgetFraction` (z. B. `0.02` für 2 %)
oder `SLASH_COMMAND_TOOL_CHAR_BUDGET` als feste Zeichenzahl. Einzelne Skills lassen sich per
`skillOverrides` auf `"name-only"` setzen; **für Plugin-Skills greift das jedoch nicht** — dort ist
die Description-Länge Autorensache, geregelt in [`CLAUDE.md`](./CLAUDE.md).

## Konzepte

- **Skills** = Wissen/Referenz (schlanke `SKILL.md` ≤ 120 Zeilen + tiefe Referenzdateien als flache Siblings daneben).
- **Agents** = Spezialisten/Orchestratoren, die mehrstufige Aufgaben autonom erledigen und delegieren.
- **Commands** = Scaffolder/Lookups (`/sw-entity`, `/sw-cms-element`, `/octo-lookup`, …).
- **Hooks** = Automatik (Lint-/Katalog-Reminder nach Datei-Änderungen).
- **Introspektion** = gecachte Kataloge des KONKRETEN Projekts (Entities, JS-Plugins, JS-Events, Admin-Bausteine, API-Endpunkte) via `/sw-entity-map`, `/sw-js-plugin-map`, `/sw-admin-map`, `/sw-api-map`, `/sw-event-map`.

## Aktualität / Selbst-Update

Zwei Plugins prüfen ihre Upstream-Quelle selbst:

- **`shopware-quality`** — Agent `shopware-librarian`, Command `/sw-sync`: prüft `shopware/shopware`
  (Releases/Tags-API + Trunk-Diff) und schlägt betroffene Skills vor bzw. aktualisiert sie.
- **`octo-api`** — Command `/octo-spec-sync`: löst die Ventrata-OpenAPI-URL dynamisch auf, vergleicht
  Content-Hash und Entitäts-Zähler gegen `.spec-state.json` und regeneriert die Referenzdateien auf
  Wunsch. `--check` berichtet nur, `--apply` schreibt.

## Lizenz & Quellen

MIT — [zone1987](https://github.com/zone1987).

Das Wissen in den Skills ist aus den jeweiligen offiziellen Quellen destilliert. Die Rechte an den
Original-Dokumentationen liegen bei den jeweiligen Anbietern:

| Plugin-Familie | Quelle |
|---|---|
| `shopware-*` | [shopware/shopware](https://github.com/shopware/shopware), developer.shopware.com, docs.shopware.com |
| `octo-api` | [docs.ventrata.com](https://docs.ventrata.com) — OCTO ist ein offener Standard von OCTO Standards NP Inc. ([octo.travel](https://octo.travel)) |
| `contao` | [contao/contao](https://github.com/contao/contao), docs.contao.org |
| `shadcn`, `shadcn-vue` | [ui.shadcn.com](https://ui.shadcn.com), [shadcn-vue.com](https://www.shadcn-vue.com) |
| `swiper`, `flatpickr`, `playwright`, `panther`, `gotenberg` | jeweiliges Upstream-Repo + offizielle Doku |

### Weitere OCTO-Implementierungen

OCTO wird nicht nur von Ventrata implementiert. Weitere Anbieter, die den Standard unterstützen:
Peek Pro, Zaui, Xola und Anchor. Die Spezifikation selbst liegt bei
[docs.octo.travel](https://docs.octo.travel) bzw. [github.com/octotravel](https://github.com/octotravel).
Das Plugin `octo-api` dokumentiert die generische OCTO-Spezifikation (in Ventratas Ausprägung) plus
ein Delta-Overlay für Go City.
