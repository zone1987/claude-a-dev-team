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

| Skill | Beschreibung |
|---|---|
| `ff-octo-api` | Shopware 6.7 Plugin "FfOctoApi" — Ventrata OCTO API für Tourismus-Ticketing (GoldenTours, GoCity, RheinKurier, Demo) |
| `octo-gocity-overview` | Go City Trade API V2 (OCTO-kompatibel): Auth (Bearer), Server-Umgebungen (Staging/Prod), unterstützte Capabilities (nur octo/pricing), Produktkonzept (Passes), Availability-Modell (immer FREESALE), Besonderheiten, OpenAPI-Spec-Referenz |
| `octo-overview` | Überblick über OCTO (Open Connectivity for Tourism) und Ventrata: Was ist OCTO, Capabilities-Konzept, Integrationsschritte, Glossar |
| `octo-adjustments` | Price Adjustments (octo/adjustments): Preisanpassungen auf Buchungsebene, adjustments-Array, Commission-Logik, Fehler-Codes |
| `octo-availability` | Availability und AvailabilityCalendar Schema der OCTO/Ventrata API: POST /availability, POST /availability/calendar, alle Felder, Status-Enums, Request/Response-Beispiele |
| `octo-bookings` | Vollständiger Booking-Lifecycle der OCTO/Ventrata API: Reserve→Confirm→Cancel, komplettes Booking-Schema, alle Status-Werte, UnitItem, Contact, Voucher/Ticket-Schema, alle Endpunkte |
| `octo-campaigns` | Campaigns (octo/campaigns): Kampagnen-Katalog abrufen, campaignId in Benachrichtigungen nutzen, NotifyRequest-Erweiterung |
| `octo-card-payments` | Card Payments (octo/cardPayments): Adyen- und External-Gateway-Integration, cardPayment-Schema, Reusable Cards, Fehler-Codes, Session-Flow |
| `octo-cart` | Multi-Booking Cart (octo/cart): Orders-Endpunkte, Schema-Erweiterungen, Buchungen in Orders gruppieren, bestätigen und stornieren |
| `octo-clients-implementations` | Ventrata-Clients (Tourismusoperatoren die Ventrata nutzen), andere OCTO-Implementierungen (Peek Pro, Zaui, Xola, Anchor), Support-Kontakt, FAQ |
| `octo-content` | Capability octo/content der Ventrata OCTO API: erweiterte Inhaltsfelder für Supplier, Product, Option, Unit, Availability, Booking — itinerary, media, notices, tourGroups |
| `octo-endpoints` | Konsolidierte Übersicht ALLER Ventrata-OCTO-Endpunkte: Core (products, availability, availability-calendar, bookings reserve/confirm/cancel/update/extend/delete/get/list, supplier, capabilities) plus Endpunkte aller optionalen Capabilities  |
| `octo-errors` | Fehlercodes und Error-Response-Format der OCTO/Ventrata API: alle error codes, HTTP-Statuscodes, Fehlerschema mit Feldern, Beispiele |
| `octo-extras` | Capability octo/extras der Ventrata OCTO API: Upsell-Items auf Booking- und Unit-Ebene, extraItems, Restrictions, Custom-Retail, Fehler-Codes |
| `octo-gift-vouchers` | Gift Vouchers (octo/gifts): Geschenk-Gutscheine erstellen, bestätigen, einlösen und stornieren |
| `octo-gocity-availability` | Go City Trade API: POST /octo/availability. OctoAvailabilityRequest (required: productId, optionId), OctoAvailability-Response (status immer FREESALE, vacancies null), Pricing-Felder, priceDistributionModel (PUBLIC/RESTRICTED), Beispiele |
| `octo-gocity-bookings` | Go City Trade API: vollständiger Booking-Lifecycle — GET /octo/bookings, POST /octo/bookings (Reserve ON_HOLD), GET /octo/bookings/{id}, POST /octo/bookings/{id}/confirm, POST /octo/bookings/{id}/cancel |
| `octo-gocity-products` | Go City Trade API: GET /octo/products und GET /octo/products/{id} |
| `octo-gocity-supplier` | Go City Trade API: GET /octo/supplier. OctoSupplier- und OctoSupplierContact-Schema mit allen Feldern (id, name, endpoint, contact) |
| `octo-headers` | Vollständige HTTP-Header-Referenz für die OCTO/Ventrata API: Authorization Bearer, Octo-Capabilities (Pflichtfeld!), Octo-Env, Accept-Language, Content-Type und Response-Header |
| `octo-identities` | Identities (octo/identities): Identitäten anlegen/aktualisieren/löschen, identityId an Bookings/Orders/Gifts hängen, Check-in-Filter |
| `octo-localization` | Lokalisierung in der OCTO/Ventrata API: Accept-Language Header, mehrsprachige Inhalte, Caching-Strategie für lokalisierte Inhalte, Content-Language Response Header |
| `octo-mappings` | Capability octo/mappings der Ventrata OCTO API: Produkt-Mapping-Sheets per PUT/GET /mappings, resellerReference, webhookUrl, Supplier-UI-Zuordnung, Upsert-Logik |
| `octo-memberships` | Memberships (octo/memberships): Mitglieder-Lookup, Mitgliedschafts-Buchungen abrufen, membershipBenefit auf Units, isMembership auf Produkten |
| `octo-notifications` | Notifications (octo/notifications): Subscriptions für BOOKING_UPDATE/AVAILABILITY_UPDATE/ PRODUCT_UPDATE anlegen und verwalten, Payload-Schema |
| `octo-offers` | Capability octo/offers der Ventrata OCTO API: Promotions, Rabattcodes, offerCode auf Availability/Booking/Gift, GET /offers, offerComparisons, offerCombinations |
| `octo-online-check-in` | Online Check-in (octo/checkin): Gäste per E-Mail, Mobilnummer oder Referenz nachschlagen, Buchungsstatus prüfen, checkedIn-Felder |
| `octo-packages` | Capability octo/packages der Ventrata OCTO API: Paketprodukte mit Sub-Produkten, packageIncludes, packageAvailabilities, packageBookings, packageUuid |
| `octo-pickups` | Capability octo/pickups der Ventrata OCTO API: Abholung und Rückgabe, pickupPoints, dropoffPoints, pickupHotel, pickupDispatch auf Option/Availability/Booking |
| `octo-pricing` | Capability octo/pricing der Ventrata OCTO API: dynamische Preisgestaltung, Pricing-Objekte, currency, tax, unitPricing, extraPricing auf Products/Availability/Bookings |
| `octo-products` | Vollständiges Product/Option/Unit-Schema der OCTO/Ventrata API: alle Felder, Typen, Enums, GET /products und GET /products/{id} Endpunkte, Capabilities-Erweiterungen |
| `octo-questions` | Capability octo/questions der Ventrata OCTO API: benutzerdefinierte Fragen auf Option/Unit-Ebene, questionAnswers im Booking, inputTypes radio/select/textarea |
| `octo-redemption` | Capability octo/redemption der Ventrata OCTO API: Ticket-Einlösung per Code/Email, GET /redemption/lookup, POST /redemption/redeem, noshow, unredeem, scans auf UnitItems |
| `octo-rentals` | Capability octo/rentals der Ventrata OCTO API: Mietprodukte mit Dauerwahl, rentalDurations auf Option, rentalDurationId auf Availability/Booking, durationUnit HOUR |
| `octo-resources` | Capability octo/resources der Ventrata OCTO API: Ressourcenzuweisung für Buchungen, GET/POST /availability/resources, resourceAllocations, Sitzpläne, hasResources |
| `octo-ventrata-vs-gocity` | Vergleich Ventrata-OCTO-API vs. Go City Trade API V2: Unterschiede und Gemeinsamkeiten bei Base-URL, Auth, Capabilities, Availability-Semantik, Produktkonzept, Header, Fallstricke bei gleichzeitiger Integration beider Supplier |
| `octo-waitlists` | Waitlists (octo/waitlists): Wartelisten-Einträge erstellen, WaitlistUnit-Schema, Kontaktfelder, supplierReference |
| `octo-waivers` | Capability octo/waivers der Ventrata OCTO API: Waiver-Definitionen auf Products, Felder/Signatur/waiverFieldValues auf Bookings, waiverPer BOOKING\|UNIT, PDF-Upload |
| `octo-webhooks` | Webhooks (octo/webhooks): Webhook-Endpunkte, Event-Typen (booking_update, order_update, availability_update, product_update), Payload-Schema, Retry-Logik |

## Agents (8)

| Agent | Beschreibung |
|---|---|
| `octo-api-expert` | Spezialist für die OCTO-API (Open Connection for Tourism) — sowohl die Ventrata-OCTO-API als auch die Go-City-Trade-API (OCTO-basiert) |
| `octo-appserver` | Spezialist für den ResubmissionAppServer — die separate Symfony-7-Shopware-App (eigenes Repo, NICHT Teil des FfOctoApi-Plugins), über die RheinKurier-Produkte (Non-API) und Wiedervorlagen in einem Iframe-Modul der Shopware-Administration an |
| `octo-availability` | Spezialist für Verfügbarkeitsprüfung, Warenkorb-Integration, Session-Management, Validierungs- Constraints und die Supplier-API-Client-Schicht (online/offline) im Shopware-Plugin FfOctoApi |
| `octo-booking` | Spezialist für den Buchungs- und Checkout-Lebenszyklus im Shopware-Plugin FfOctoApi |
| `octo-dev` | Orchestrator und Standard-Einstieg für ALLES rund um das Shopware-6.7-Plugin FfOctoApi (Ventrata OCTO API, Tourismus-Ticketing: GoldenTours, GoCity, RheinKurier, Demo) |
| `octo-frontend` | Spezialist für Storefront-Frontend des Shopware-Plugins FfOctoApi: das FfBuyBox-JavaScript-Plugin, Twig-Templates (Buy-Widget/Configurator/Line-Item), SCSS und die Override-Verflechtung mit FfLondonBase/FfLondonTheme |
| `octo-pricing` | Spezialist für Preisberechnung, Währungsumrechnung und Provision im Shopware-Plugin FfOctoApi |
| `octo-testing` | Test-Spezialist für das Shopware-Plugin FfOctoApi über alle drei Ebenen: Unit, Integration und E2E (Symfony Panther) |

## Commands (1)

| Command | Beschreibung |
|---|---|
| `/octo-lookup` | Schlägt eine OCTO-API-Capability oder einen Endpunkt nach (Ventrata oder Go-City) und gibt Request/Response/Parameter/Required/Auth aus |
