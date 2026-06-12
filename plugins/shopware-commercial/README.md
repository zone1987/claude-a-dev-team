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

`sw-commercial-overview`, `sw-advanced-search`, `sw-b2b-components`, `sw-b2b-components-employee-management`, `sw-b2b-components-quotes`, `sw-b2b-order-approval`, `sw-b2b-suite`, `sw-b2b-suite-migration`, `sw-commercial-bundle`, `sw-digital-sales-rooms`, `sw-digital-sales-rooms-3rdparty`, `sw-digital-sales-rooms-config`, `sw-digital-sales-rooms-customization`, `sw-digital-sales-rooms-deployment`, `sw-digital-sales-rooms-installation`, `sw-migration-assistant`, `sw-migration-assistant-custom-profile`, `sw-nexus`, `sw-sales-agent`, `sw-sales-agent-customization`, `sw-sales-agent-deployment`, `sw-sales-agent-setup`, `sw-subscriptions`

## Agents (1)

- **`shopware-commercial-dev`** — Spezialist für Shopware-6 Commercial-Extensions aus Entwickler-Sicht: Commercial-Bundle, B2B Suite & B2B Components, Subscriptions, Advanced Search, Migration Assistant (SW5->6 Datenmigration), Digital Sales Rooms, Sales
