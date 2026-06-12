# octo-api

**Wofür:** OCTO-API (Tourismus-Ticketing): die generische Ventrata-OCTO-API (Core + alle 23 Capabilities, alle Endpunkte), die Go-City-Trade-API (OCTO-basiert), ein Vergleich beider — plus die FfOctoApi-Shopware-Integration (forty-four) inkl. ResubmissionAppServer.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Wissen ist aus der Shopware-/OCTO-Quelle destilliert; Skills laden Tiefe progressiv aus `references/`.

## Installation (Claude Code)

```
/plugin marketplace add zone1987/claude-a-dev-team
/plugin install octo-api@claude-a-dev-team
```

## Skills (39)

`ff-octo-api`, `octo-gocity-overview`, `octo-overview`, `octo-adjustments`, `octo-availability`, `octo-bookings`, `octo-campaigns`, `octo-card-payments`, `octo-cart`, `octo-clients-implementations`, `octo-content`, `octo-endpoints`, `octo-errors`, `octo-extras`, `octo-gift-vouchers`, `octo-gocity-availability`, `octo-gocity-bookings`, `octo-gocity-products`, `octo-gocity-supplier`, `octo-headers`, `octo-identities`, `octo-localization`, `octo-mappings`, `octo-memberships`, `octo-notifications`, `octo-offers`, `octo-online-check-in`, `octo-packages`, `octo-pickups`, `octo-pricing`, `octo-products`, `octo-questions`, `octo-redemption`, `octo-rentals`, `octo-resources`, `octo-ventrata-vs-gocity`, `octo-waitlists`, `octo-waivers`, `octo-webhooks`

## Agents (8)

- **`octo-api-expert`** — Spezialist für die OCTO-API (Open Connection for Tourism) — sowohl die Ventrata-OCTO-API als auch die Go-City-Trade-API (OCTO-basiert).
- **`octo-appserver`** — Spezialist für den ResubmissionAppServer — die separate Symfony-7-Shopware-App (eigenes Repo, NICHT Teil des FfOctoApi-Plugins), über die RheinKurier-Produkte (Non-API) und Wiedervorlagen in einem Ifr
- **`octo-availability`** — Spezialist für Verfügbarkeitsprüfung, Warenkorb-Integration, Session-Management, Validierungs- Constraints und die Supplier-API-Client-Schicht (online/offline) im Shopware-Plugin FfOctoApi.
- **`octo-booking`** — Spezialist für den Buchungs- und Checkout-Lebenszyklus im Shopware-Plugin FfOctoApi.
- **`octo-dev`** — Orchestrator und Standard-Einstieg für ALLES rund um das Shopware-6.7-Plugin FfOctoApi (Ventrata OCTO API, Tourismus-Ticketing: GoldenTours, GoCity, RheinKurier, Demo).
- **`octo-frontend`** — Spezialist für Storefront-Frontend des Shopware-Plugins FfOctoApi: das FfBuyBox-JavaScript-Plugin, Twig-Templates (Buy-Widget/Configurator/Line-Item), SCSS und die Override-Verflechtung mit FfLondonBa
- **`octo-pricing`** — Spezialist für Preisberechnung, Währungsumrechnung und Provision im Shopware-Plugin FfOctoApi.
- **`octo-testing`** — Test-Spezialist für das Shopware-Plugin FfOctoApi über alle drei Ebenen: Unit, Integration und E2E (Symfony Panther).

## Commands (1)

- **`/octo-lookup`** — Schlägt eine OCTO-API-Capability oder einen Endpunkt nach (Ventrata oder Go-City) und gibt Request/Response/Parameter/Required/Auth aus.
