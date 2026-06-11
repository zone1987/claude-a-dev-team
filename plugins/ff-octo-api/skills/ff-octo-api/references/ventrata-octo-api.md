# Ventrata OCTO API Referenz

## Was ist OCTO?

**Open Connectivity for Tours, Activities & Attractions** — Offener Standard für Tourismus-Buchungssysteme, entwickelt von Ventrata, Peek Pro, Xola.

**Ventrata** ist sowohl Gründer als auch konkreter Provider. Fungiert als Middleware zwischen Suppliern (GoldenTours, GoCity) und Resellern (Shop).

## Basis-URLs

| Provider | URL |
|----------|-----|
| Ventrata (Production) | `https://api.ventrata.com/octo/` |
| GoCity (Staging) | `https://api.staging.gocity.tech/octo/` |
| GoCity (Production) | `https://api.gocity.com/octo/` |

## Authentifizierung

```
Authorization: Bearer {API_KEY_UUID}
```

- Jeder Key gewährt Zugang zu genau **einem** Supplier
- Kompromittierter Key: Supplier löscht/erstellt Verbindung neu
- Dashboard: `https://dashboard.ventrata.com/`

## Pflicht-Headers

| Header | Wert | Pflicht |
|--------|------|---------|
| Authorization | Bearer {key} | **Ja** |
| Content-Type | application/json | POST/PATCH |
| Octo-Capabilities | z.B. octo/pricing,octo/content | **Ja** (auch leerer String, sonst HTTP 400!) |
| Octo-Env | test oder live | Empfohlen |
| Accept-Language | z.B. de-DE, en-GB | Optional |

## API-Endpunkte

### Products

```
GET /products                     → Alle Supplier-Produkte
GET /products/{productId}         → Einzelprodukt
```

### Availability

```
POST /availability                → Verfügbarkeitsprüfung
GET  /availability                → Mit Filtern
POST /availability/calendar       → Monatskalender
POST /availability/batch          → Batch-Prüfung
```

**Request-Body:**
```json
{
    "productId": "uuid",
    "optionId": "uuid",
    "localDateStart": "2025-03-15 00:00:00",
    "localDateEnd": "2025-03-15 23:59:59",
    "units": [
        { "id": "unit-uuid", "quantity": 2 }
    ]
}
```

**Status-Werte:** AVAILABLE, LIMITED, SOLD_OUT, CLOSED, FREESALE

### Bookings

```
POST   /bookings                  → Reservierung erstellen (Status: PENDING/ON_HOLD)
PATCH  /bookings/{uuid}           → Aktualisieren
POST   /bookings/{uuid}/confirm   → Nach Zahlung bestätigen
POST   /bookings/{uuid}/cancel    → Stornieren
POST   /bookings/{uuid}/extend    → Reservierung verlängern
GET    /bookings/{uuid}           → Einzelbuchung
GET    /bookings                  → Buchungen filtern/auflisten
```

**Booking-Status:** PENDING, ON_HOLD, CONFIRMED, CANCELLED, EXPIRED, REJECTED, REDEEMED, NO_SHOW

**Reservierung erstellen:**
```json
{
    "uuid": "optionale-uuid",
    "productId": "uuid",
    "optionId": "uuid",
    "availabilityId": "uuid",
    "expirationMinutes": 30,
    "unitItems": [
        { "unitId": "uuid" },
        { "unitId": "uuid" }
    ]
}
```

**Bestätigung:**
```json
{
    "emailReceipt": false,
    "resellerReference": "order-123",
    "contact": {
        "fullName": "Max Mustermann",
        "firstName": "Max",
        "lastName": "Mustermann",
        "emailAddress": "max@example.com",
        "phoneNumber": "+49...",
        "locales": ["de-DE"],
        "country": "de"
    }
}
```

**Stornierung:**
```json
{
    "reason": "Customer request",
    "force": false
}
```
Response enthält `refund`: FULL, PARTIAL, NONE

### Webhooks

```
POST   /webhooks                  → Registrieren
PATCH  /webhooks/{id}             → Aktualisieren
GET    /webhooks                  → Auflisten
DELETE /webhooks/{id}             → Löschen
DELETE /webhooks?url=...          → Nach URL löschen
```

**Events:** booking_update, availability_update, product_update, order_update

## Capabilities-System

Erweitert API-Responses mit zusätzlichen Features.

### Im Plugin genutzt

| Capability | Beschreibung |
|-----------|-------------|
| `octo/pricing` | Preisfelder: original, retail, net, currency, currencyPrecision, includedTaxes |
| `octo/content` | Reichhaltige Inhalte: Bilder, Beschreibungen, Itineraries |
| `ventrata/resources` | Ressourcen-Info für Availability |
| `ventrata/webhooks` | Webhook-Management |

### Weitere verfügbare Capabilities

octo/offers, octo/extras, octo/packages, octo/pickups, octo/questions, octo/waivers, octo/resources, octo/rentals, octo/redemption, octo/mappings, octo/cart, octo/gifts, octo/checkin, octo/cardPayments, octo/memberships, octo/adjustments, octo/waitlists, octo/identities, octo/campaigns, octo/notifications

## Preise: Minor Units

Alle Preise in Minor Units (Cent):
```
2500 mit currencyPrecision: 2 = 25.00 EUR/GBP
44900 mit currencyPrecision: 2 = 449.00 SEK
```

**Umrechnung:** `preis / pow(10, currencyPrecision)`

## Fehlerbehandlung

Alle Fehler: HTTP 400 mit JSON-Body:
```json
{
    "error": "ERROR_CODE",
    "errorMessage": "Human readable message",
    "field": "optional context"
}
```

**Error-Codes:**
- INVALID_PRODUCT_ID
- INVALID_OPTION_ID
- INVALID_UNIT_ID
- INVALID_AVAILABILITY_ID
- INVALID_BOOKING_UUID
- BAD_REQUEST
- UNPROCESSABLE_ENTITY
- UNAUTHORIZED
- FORBIDDEN
- INTERNAL_SERVER_ERROR

## Supplier-Unterschiede

| Aspekt | Ventrata (GoldenTours) | GoCity |
|--------|----------------------|--------|
| Booking-Status bei Reservierung | PENDING | ON_HOLD |
| Booking-Update (PATCH) | Unterstützt | Nicht dokumentiert |
| Datum-Format (Availability) | Y-m-d H:i:s | Y-m-d |
| Supplier-Endpoint | /suppliers/{id} | /supplier (ohne ID) |
| Availability-Typ | START_TIME, OPENING_HOURS | FREESALE |
| Unit-Typen | 8 (ADULT...OTHER) | 2 (ADULT, CHILD) |
| Produkt-Content | Sehr reichhaltig | Minimal |
| Währungen | GBP + EUR | EUR, GBP, USD, SEK je nach Region |
