# shopware-commercial

> Die kommerziellen Extensions aus Entwickler-Sicht.

`shopware-commercial` dokumentiert die **kommerziellen Shopware-Extensions aus Entwickler-Sicht** — also das
technische Erweitern/Integrieren der lizenzpflichtigen Features (die Bedienung aus Betreibersicht liegt in
`shopware-merchant`).

Abgedeckt: das **Commercial-Bundle** (Sub-Bundle-Architektur, Feature-Toggles), **B2B** in moderner Form
(**B2B Components**: Employee-Management, Quotes/Shopping-Lists, Order-Approval, Individual Pricing) wie als Legacy
(**B2B Suite** inkl. Migration), **Subscriptions**, **Advanced Search** (ES/OpenSearch-basiert), der
**Migration Assistant** (Daten-Migration aus SW5/anderen Systemen inkl. eigener Profile/Reader/Converter/Writer),
sowie **Digital Sales Rooms**, **Sales Agent** und **Nexus**.

Spezialist: **`shopware-commercial-dev`**. **Wann nutzen:** wenn ein Projekt auf kommerziellen Extensions aufbaut und
diese erweitert/integriert werden sollen. Die Standard-Mechaniken dahinter (DAL/Events/Store-API) liefern die
Entwickler-Plugins.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install shopware-commercial@claude-a-dev-team
```

## Skills (23)

| Skill | Beschreibung |
|---|---|
| `sw-commercial-overview` | Shopware Commercial Plugin — Uberblick, Lizenzierung, Aktivierung, Bundles |
| `sw-advanced-search` | Shopware Advanced Search — Elasticsearch/OpenSearch-basierte Suche im Commercial Plugin |
| `sw-b2b-components` | Shopware B2B Components — modernes B2B-Framework im Commercial Plugin |
| `sw-b2b-components-employee-management` | B2B Employee Management im Shopware Commercial Plugin. Mitarbeiter (swag_b2b_employee), Rollen, Berechtigungen, Business Partner, Route Restriction (Denylist), Einladungsflow, Store API, eigene Permissions via Plugin/App, Subscription-Integ |
| `sw-b2b-components-quotes` | B2B Quotes Management, Shopping Lists und Individual Pricing im Shopware Commercial Plugin |
| `sw-b2b-order-approval` | B2B Order Approval (Bestellgenehmigung) im Shopware Commercial Plugin |
| `sw-b2b-suite` | Shopware B2B Suite (Legacy, bis SW 6.8 unterstuetzt). Systemarchitektur, Konventionen, Debtor/Contact-Modell, StoreFrontAuthentication, ACL, CRUD-Services, REST-API, Storefront- Erweiterungen, AjaxPanel |
| `sw-b2b-suite-migration` | Migration von B2B Suite zu B2B Components (Shopware Commercial) |
| `sw-commercial-bundle` | Shopware Commercial Plugin — Bundle-Struktur und Entwickler-Patterns |
| `sw-digital-sales-rooms` | Überblick über Digital Sales Rooms: Architektur, Voraussetzungen, Komponenten und Einstiegspunkt für alle DSR-Entwicklerthemen |
| `sw-digital-sales-rooms-3rdparty` | Einrichtung der Drittanbieter-Dienste für Digital Sales Rooms: Mercure Hub (Stackhero oder Docker) und Daily.co (Video/Audio API) |
| `sw-digital-sales-rooms-config` | Konfiguration von Digital Sales Rooms: Domain-Setup im Sales Channel, CLI-Konfiguration (composer dsr:config) und Plugin-Einstellungsseite |
| `sw-digital-sales-rooms-customization` | Anpassung der Digital Sales Rooms Frontend-App: Nuxt-Layer-Konzept, Branding (Favicon, Titel, Farben), Komponenten überschreiben, i18n anpassen |
| `sw-digital-sales-rooms-deployment` | Deployment der Digital Sales Rooms Frontend-App: AWS Amplify, Cloudflare Pages (inkl |
| `sw-digital-sales-rooms-installation` | Installation von Digital Sales Rooms: Plugin via Composer/Download installieren und aktivieren, Frontend-App (dsr-frontends) einrichten und starten |
| `sw-migration-assistant` | Shopware Migration Assistant — Konzepte fuer Entwickler. Profile, Connection, Gateway, Reader, Converter, Mapping, Deltas, DataSelection, DataSet, Writer, Media Processing, Premapping, vollstaendiger Migrationsprozess (Fetching→ErrorResolut |
| `sw-migration-assistant-custom-profile` | Shopware Migration Assistant — Eigene Profile und Erweiterungen erstellen |
| `sw-nexus` | Shopware Nexus: Event-getriebene Automatisierungsplattform (Beta) |
| `sw-sales-agent` | Überblick über die Sales-Agent-App: Architektur (Nuxt/Nitro/Prisma/Redis), Lizenz, API-Dokumentation und Einstiegspunkt für alle SA-Entwicklerthemen |
| `sw-sales-agent-customization` | Anpassung der Sales-Agent-App: Nuxt-Layer-Konzept, Branding (Favicon, Titel, CSS-Variablen via Meteor Component Library), Komponenten überschreiben, i18n |
| `sw-sales-agent-deployment` | Deployment der Sales-Agent-App: AWS Amplify (mit ElastiCache/Upstash Redis), Cloudflare Pages (mit Upstash Redis), Ubuntu Server mit PM2 (lokales Redis) |
| `sw-sales-agent-setup` | Installation und lokales Setup der Sales-Agent-App: Repository klonen, .env konfigurieren, Datenbank migrieren, App-Bundle für Shopware bauen |
| `sw-subscriptions` | Shopware Subscriptions Extension (Commercial Plugin) fuer Entwickler |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `shopware-commercial-dev` | Spezialist für Shopware-6 Commercial-Extensions aus Entwickler-Sicht: Commercial-Bundle, B2B Suite & B2B Components, Subscriptions, Advanced Search, Migration Assistant (SW5->6 Datenmigration), Digital Sales Rooms, Sales Agent, Nexus |
