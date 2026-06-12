# octo-api

> Die OCTO-API für Tourismus-Ticketing: Ventrata, Go-City und die FfOctoApi-Integration.

`octo-api` ist das umfassende Wissenspaket zur **OCTO-API** (Open Connection for Tourism) für **Tourismus-Ticketing**
— in drei Teilen:

1. **Ventrata OCTO API** (generisch): der **Core** (Products, Availability, Bookings) und **alle 23 Capabilities**
   (pricing, content, offers, extras, packages, pickups, questions, waivers, resources, rentals, redemption, mappings,
   cart, gift-vouchers, online-check-in, card-payments, memberships, adjustments, webhooks, waitlists, identities,
   campaigns, notifications) — je mit Capability-Identifier, **Requests** (Pfad/Query/Body, required vs. optional),
   **Responses/Schemas**, **Auth** und Beispielen. Eine konsolidierte **58-Endpunkt-Übersicht** listet alles an einem Ort.
2. **Go City Trade API** (OCTO-basiert): aus der offiziellen OpenAPI generiert (Products/Availability/Bookings/Supplier),
   plus ein **Vergleich Ventrata ↔ Go-City** (Unterschiede, Fallstricke, Adapter-Empfehlung) — z. B. dass Go-City nur
   `octo/pricing` unterstützt, Availability stets `FREESALE` ist und Stornofristen invertiert sind.
3. **FfOctoApi** — die **Shopware-Integration** von A-Dev-Team: das Shopware-Plugin (Skill `ff-octo-api`) und der
   **ResubmissionAppServer** samt der spezialisierten Shopware-Agents (`octo-dev`, `octo-booking`, `octo-pricing`,
   `octo-availability`, `octo-frontend`, `octo-appserver`, `octo-testing`).

Berater: **`octo-api-expert`** (Ventrata + Go-City); Lookup-Command **`/octo-lookup`**. **Hinweis:** Das Repo ist
öffentlich — es sind **keine echten Credentials** enthalten (nur Platzhalter). **Wann nutzen:** für jede Integration
gegen Ventrata-/Go-City-OCTO oder Arbeit am FfOctoApi-Plugin.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install octo-api@claude-a-dev-team
```

## Skills (39)

`ff-octo-api`, `octo-gocity-overview`, `octo-overview`, `octo-adjustments`, `octo-availability`, `octo-bookings`, `octo-campaigns`, `octo-card-payments`, `octo-cart`, `octo-clients-implementations`, `octo-content`, `octo-endpoints`, `octo-errors`, `octo-extras`, `octo-gift-vouchers`, `octo-gocity-availability`, `octo-gocity-bookings`, `octo-gocity-products`, `octo-gocity-supplier`, `octo-headers`, `octo-identities`, `octo-localization`, `octo-mappings`, `octo-memberships`, `octo-notifications`, `octo-offers`, `octo-online-check-in`, `octo-packages`, `octo-pickups`, `octo-pricing`, `octo-products`, `octo-questions`, `octo-redemption`, `octo-rentals`, `octo-resources`, `octo-ventrata-vs-gocity`, `octo-waitlists`, `octo-waivers`, `octo-webhooks`

## Agents (8)

- **`octo-api-expert`** — Spezialist für die OCTO-API (Open Connection for Tourism) — sowohl die Ventrata-OCTO-API als auch die Go-City-Trade-API (OCTO-basiert).
- **`octo-appserver`** — Spezialist für den ResubmissionAppServer — die separate Symfony-7-Shopware-App (eigenes Repo, NICHT Teil des FfOctoApi-Plugins), über die RheinKurier-Produkte (Non-API) und Wiedervorlagen in einem Iframe-Modul der Shopwa
- **`octo-availability`** — Spezialist für Verfügbarkeitsprüfung, Warenkorb-Integration, Session-Management, Validierungs- Constraints und die Supplier-API-Client-Schicht (online/offline) im Shopware-Plugin FfOctoApi.
- **`octo-booking`** — Spezialist für den Buchungs- und Checkout-Lebenszyklus im Shopware-Plugin FfOctoApi.
- **`octo-dev`** — Orchestrator und Standard-Einstieg für ALLES rund um das Shopware-6.7-Plugin FfOctoApi (Ventrata OCTO API, Tourismus-Ticketing: GoldenTours, GoCity, RheinKurier, Demo).
- **`octo-frontend`** — Spezialist für Storefront-Frontend des Shopware-Plugins FfOctoApi: das FfBuyBox-JavaScript-Plugin, Twig-Templates (Buy-Widget/Configurator/Line-Item), SCSS und die Override-Verflechtung mit FfLondonBase/FfLondonTheme.
- **`octo-pricing`** — Spezialist für Preisberechnung, Währungsumrechnung und Provision im Shopware-Plugin FfOctoApi.
- **`octo-testing`** — Test-Spezialist für das Shopware-Plugin FfOctoApi über alle drei Ebenen: Unit, Integration und E2E (Symfony Panther).

## Commands (1)

- **`/octo-lookup`** — Schlägt eine OCTO-API-Capability oder einen Endpunkt nach (Ventrata oder Go-City) und gibt Request/Response/Parameter/Required/Auth aus.
