# octo-api

> Die OCTO-API für Tourismus-Ticketing: Ventrata OCTO und Go-City — vollständig dokumentiert.

`octo-api` ist das umfassende Wissenspaket zur **OCTO-API** (Open Connection for Tourism) für **Tourismus-Ticketing**
— in zwei Teilen:

1. **Ventrata OCTO API** (generisch): der **Core** (Products, Availability, Bookings) und **alle 23 Capabilities**
   (pricing, content, offers, extras, packages, pickups, questions, waivers, resources, rentals, redemption, mappings,
   cart, gift-vouchers, online-check-in, card-payments, memberships, adjustments, webhooks, waitlists, identities,
   campaigns, notifications) — je mit Capability-Identifier, **Requests** (Pfad/Query/Body, required vs. optional),
   **Responses/Schemas**, **Auth/Header**, **Errors** und Beispielen. Eine konsolidierte **Endpunkt-Übersicht** listet alles an einem Ort.
2. **Go City Trade API** (OCTO-basiert): aus der offiziellen OpenAPI generiert (Products/Availability/Bookings/Supplier),
   plus ein **Vergleich Ventrata ↔ Go-City** (Unterschiede, Fallstricke, Adapter-Empfehlung) — z. B. dass Go-City nur
   `octo/pricing` unterstützt, Availability stets `FREESALE` ist und Stornofristen invertiert sind.

Berater: **`octo-api-expert`** (Ventrata + Go-City); Lookup-Command **`/octo-lookup`**. **Hinweis:** Das Repo ist
öffentlich — es sind **keine echten Credentials** enthalten (nur Platzhalter/offizielle Test-Keys). **Wann nutzen:**
für jede Integration gegen Ventrata-/Go-City-OCTO.

Teil des Marketplace **[claude-a-dev-team](../../README.md)**. Das Wissen ist aus den offiziellen Quellen destilliert und eingebettet; Skills laden ihre Tiefe progressiv aus `references/`.

## Installation

```
/plugin marketplace add https://github.com/zone1987/claude-a-dev-team
/plugin install octo-api@claude-a-dev-team
```

## Skills (38)

### Ventrata OCTO — Core & Grundlagen

| Skill | Beschreibung |
|---|---|
| `octo-overview` | Überblick über OCTO (Open Connectivity for Tourism) und Ventrata: Was ist OCTO, Capabilities-Konzept, Integrationsschritte, Glossar |
| `octo-headers` | Vollständige HTTP-Header-Referenz: Authorization Bearer, Octo-Capabilities (Pflichtfeld!), Octo-Env, Accept-Language, Content-Type und Response-Header |
| `octo-errors` | Fehlercodes und Error-Response-Format: alle error codes, HTTP-Statuscodes, Fehlerschema mit Feldern, Beispiele |
| `octo-endpoints` | Konsolidierte Übersicht ALLER Ventrata-OCTO-Endpunkte: Core (products, availability, availability-calendar, bookings reserve/confirm/cancel/update/extend/delete/get/list, supplier, capabilities) plus alle optionalen Capabilities |
| `octo-products` | Vollständiges Product/Option/Unit-Schema: alle Felder, Typen, Enums, GET /products und GET /products/{id}, Capabilities-Erweiterungen |
| `octo-availability` | Availability- und AvailabilityCalendar-Schema: POST /availability, POST /availability/calendar, alle Felder, Status-Enums, Request/Response-Beispiele |
| `octo-bookings` | Vollständiger Booking-Lifecycle: Reserve→Confirm→Cancel, komplettes Booking-Schema, alle Status-Werte, UnitItem, Contact, Voucher/Ticket-Schema, alle Endpunkte |
| `octo-localization` | Lokalisierung: Accept-Language Header, mehrsprachige Inhalte, Caching-Strategie, Content-Language Response Header |

### Ventrata OCTO — Capabilities

| Skill | Beschreibung |
|---|---|
| `octo-pricing` | octo/pricing: dynamische Preisgestaltung, Pricing-Objekte, currency, tax, unitPricing, extraPricing auf Products/Availability/Bookings |
| `octo-content` | octo/content: erweiterte Inhaltsfelder für Supplier/Product/Option/Unit/Availability/Booking — itinerary, media, notices, tourGroups |
| `octo-offers` | octo/offers: Promotions, Rabattcodes, offerCode auf Availability/Booking/Gift, GET /offers, offerComparisons, offerCombinations |
| `octo-extras` | octo/extras: Upsell-Items auf Booking- und Unit-Ebene, extraItems, Restrictions, Custom-Retail, Fehler-Codes |
| `octo-packages` | octo/packages: Paketprodukte mit Sub-Produkten, packageIncludes, packageAvailabilities, packageBookings, packageUuid |
| `octo-pickups` | octo/pickups: Abholung/Rückgabe, pickupPoints, dropoffPoints, pickupHotel, pickupDispatch auf Option/Availability/Booking |
| `octo-questions` | octo/questions: benutzerdefinierte Fragen auf Option/Unit-Ebene, questionAnswers im Booking, inputTypes radio/select/textarea |
| `octo-waivers` | octo/waivers: Waiver-Definitionen auf Products, Felder/Signatur/waiverFieldValues auf Bookings, waiverPer BOOKING\|UNIT, PDF-Upload |
| `octo-resources` | octo/resources: Ressourcenzuweisung, GET/POST /availability/resources, resourceAllocations, Sitzpläne, hasResources |
| `octo-rentals` | octo/rentals: Mietprodukte mit Dauerwahl, rentalDurations auf Option, rentalDurationId auf Availability/Booking, durationUnit HOUR |
| `octo-redemption` | octo/redemption: Ticket-Einlösung per Code/Email, GET /redemption/lookup, POST /redemption/redeem, noshow, unredeem, scans auf UnitItems |
| `octo-mappings` | octo/mappings: Produkt-Mapping-Sheets per PUT/GET /mappings, resellerReference, webhookUrl, Supplier-UI-Zuordnung, Upsert-Logik |
| `octo-cart` | octo/cart: Multi-Booking-Cart, Orders-Endpunkte, Schema-Erweiterungen, Buchungen in Orders gruppieren, bestätigen und stornieren |
| `octo-gift-vouchers` | octo/gifts: Geschenk-Gutscheine erstellen, bestätigen, einlösen und stornieren |
| `octo-online-check-in` | octo/checkin: Gäste per E-Mail/Mobilnummer/Referenz nachschlagen, Buchungsstatus prüfen, checkedIn-Felder |
| `octo-card-payments` | octo/cardPayments: Adyen- und External-Gateway-Integration, cardPayment-Schema, Reusable Cards, Fehler-Codes, Session-Flow |
| `octo-memberships` | octo/memberships: Mitglieder-Lookup, Mitgliedschafts-Buchungen, membershipBenefit auf Units, isMembership auf Produkten |
| `octo-adjustments` | octo/adjustments: Preisanpassungen auf Buchungsebene, adjustments-Array, Commission-Logik, Fehler-Codes |
| `octo-webhooks` | octo/webhooks: Webhook-Endpunkte, Event-Typen (booking_update, order_update, availability_update, product_update), Payload-Schema, Retry-Logik |
| `octo-waitlists` | octo/waitlists: Wartelisten-Einträge erstellen, WaitlistUnit-Schema, Kontaktfelder, supplierReference |
| `octo-identities` | octo/identities: Identitäten anlegen/aktualisieren/löschen, identityId an Bookings/Orders/Gifts hängen, Check-in-Filter |
| `octo-campaigns` | octo/campaigns: Kampagnen-Katalog abrufen, campaignId in Benachrichtigungen nutzen, NotifyRequest-Erweiterung |
| `octo-notifications` | octo/notifications: Subscriptions für BOOKING_UPDATE/AVAILABILITY_UPDATE/PRODUCT_UPDATE anlegen und verwalten, Payload-Schema |
| `octo-clients-implementations` | Ventrata-Clients (Operatoren), andere OCTO-Implementierungen (Peek Pro, Zaui, Xola, Anchor), Support-Kontakt, FAQ |

### Go-City Trade API & Vergleich

| Skill | Beschreibung |
|---|---|
| `octo-gocity-overview` | Go City Trade API V2 (OCTO-kompatibel): Auth (Bearer), Server-Umgebungen (Staging/Prod), unterstützte Capabilities (nur octo/pricing), Produktkonzept (Passes), Availability-Modell (immer FREESALE), OpenAPI-Spec-Referenz |
| `octo-gocity-products` | Go City Trade API: GET /octo/products und GET /octo/products/{id} |
| `octo-gocity-availability` | Go City Trade API: POST /octo/availability, OctoAvailabilityRequest (required: productId, optionId), Response (status FREESALE, vacancies null), Pricing-Felder, priceDistributionModel |
| `octo-gocity-bookings` | Go City Trade API: vollständiger Booking-Lifecycle — GET/POST /octo/bookings (Reserve ON_HOLD), GET/confirm/cancel /octo/bookings/{id} |
| `octo-gocity-supplier` | Go City Trade API: GET /octo/supplier, OctoSupplier- und OctoSupplierContact-Schema mit allen Feldern |
| `octo-ventrata-vs-gocity` | Vergleich Ventrata-OCTO vs. Go City Trade API V2: Base-URL, Auth, Capabilities, Availability-Semantik, Produktkonzept, Header, Fallstricke bei gleichzeitiger Integration beider Supplier |

## Agents (1)

| Agent | Beschreibung |
|---|---|
| `octo-api-expert` | Spezialist für die OCTO-API — sowohl die Ventrata-OCTO-API als auch die Go-City-Trade-API (OCTO-basiert): Auth/Header, Core-Endpunkte, alle Capabilities, Requests/Responses/Parameter und die Unterschiede beider. |

## Commands (1)

| Command | Beschreibung |
|---|---|
| `/octo-lookup` | Schlägt eine OCTO-API-Capability oder einen Endpunkt nach (Ventrata oder Go-City) und gibt Request/Response/Parameter/Required/Auth aus |

## Lizenz & Autor

proprietary — Andreas Gerhardt, A-Dev-Team. Quellen: offizielle Ventrata-OCTO- und Go-City-Trade-API-Dokumentation.
