# Ventrata OCTO API vs. Go City Trade API V2 — Vollständiger Vergleich

## Kurzfassung (4 wichtigste Unterschiede)

1. **Capabilities:** Ventrata unterstützt 20+ Capabilities; Go City unterstützt **nur `octo/pricing`** (und dieses nur in Staging).
2. **Availability-Semantik:** Ventrata kann AVAILABLE, FREESALE, SOLD_OUT, LIMITED, CLOSED zurückgeben; Go City gibt **immer FREESALE** zurück — Passes sind stets buchbar.
3. **Produktbegriff:** Ventrata = Touren/Aktivitäten mit festen Abfahrtszeiten oder Öffnungszeiten; Go City = **Pässe** (City Passes mit mehreren Destinationen, Brands, Dauer-Typen).
4. **Endpunkt-Vollständigkeit:** Ventrata bietet den kompletten OCTO-Standard + zahlreiche Erweiterungen; Go City implementiert **9 von ~50+ Ventrata-Endpunkten** (nur Core-Flow).

---

## Tabelle 1: Basis-Konfiguration

| Aspekt | Ventrata | Go City |
|--------|----------|---------|
| **Base-URL** | `https://api.ventrata.com/octo` | Prod: `https://api.gocity.com/octo` |
| **Staging-URL** | Kein separater Host — `Octo-Env: test` Header | `https://api.staging.gocity.tech/octo` |
| **API-Version** | OCTO Core (ohne Versionsnummer in URL) | V2 (OCTO-kompatibel) |
| **OpenAPI-Format** | Keine offizielle OpenAPI-Spec öffentlich | OpenAPI 3.1 verfügbar |
| **Dokumentation** | https://docs.ventrata.com | Redoc-basiert (Trade Partner Portal) |

---

## Tabelle 2: Authentifizierung

| Aspekt | Ventrata | Go City |
|--------|----------|---------|
| **Auth-Schema** | HTTP Bearer Token | HTTP Bearer Token |
| **Token-Format** | UUID-Format (z.B. `<UUID>`) | Vom Connectivity Manager bereitgestellt |
| **Reichweite** | 1 Token = 1 Supplier | 1 Token = Go City (1 Supplier) |
| **Credentials-Erhalt** | Via Ventrata-Plattform / Account-Setup | Via Connectivity Manager |
| **Test-Modus** | `Octo-Env: test` Header + Live-Credentials | Separater Staging-Server |
| **HTTP-Pflicht** | Nur HTTPS | Nur HTTPS |
| **Fehler ohne Token** | 403 UNAUTHORIZED | 403 (angenommen, nicht explizit dokumentiert) |

**Integrations-Fallstrick:** Bei Ventrata wird Test vs. Live durch den `Octo-Env`-Header gesteuert (gleiche URL, gleiche Credentials). Bei Go City gibt es separate Hosts — Staging und Production haben unterschiedliche Base-URLs und ggf. unterschiedliche Tokens.

---

## Tabelle 3: Capabilities

| Capability | Ventrata | Go City |
|-----------|----------|---------|
| `octo/pricing` | Ja | Ja (nur Staging, Stand Aug 2024) |
| `octo/content` | Ja | Nein |
| `octo/offers` | Ja | Nein |
| `octo/extras` | Ja | Nein |
| `octo/packages` | Ja | Nein |
| `octo/pickups` | Ja | Nein |
| `octo/questions` | Ja | Nein |
| `octo/waivers` | Ja | Nein |
| `octo/resources` | Ja | Nein |
| `octo/rentals` | Ja | Nein |
| `octo/redemption` | Ja | Nein |
| `octo/mappings` | Ja | Nein |
| `octo/cart` | Ja | Nein |
| `octo/gifts` | Ja | Nein |
| `octo/checkin` | Ja | Nein |
| `octo/cardPayments` | Ja | Nein |
| `octo/memberships` | Ja | Nein |
| `octo/adjustments` | Ja | Nein |
| `octo/webhooks` | Ja | Nein |
| `octo/waitlists` | Ja | Nein |
| `octo/identities` | Ja | Nein |
| `octo/campaigns` | Ja | Nein |
| `octo/notifications` | Ja | Nein |

**Aktivierungsmethode:**
- Ventrata: `Octo-Capabilities` Header (**Pflicht** — Fehlen gibt 400 Bad Request)
- Go City: `Octo-Capabilities` Header **oder** `?_capabilities=octo/pricing` Query-Parameter (beide optional)

**Capabilities-Entdeckung:**
- Ventrata: `GET /octo/capabilities/` Endpunkt
- Go City: Kein `/capabilities`-Endpunkt vorhanden

---

## Tabelle 4: HTTP-Header

| Header | Ventrata | Go City |
|--------|----------|---------|
| `Authorization: Bearer` | Pflicht | Pflicht |
| `Content-Type: application/json` | Pflicht bei POST/PATCH | Pflicht bei POST |
| `Octo-Capabilities` | **Pflicht** (leer = leer senden) | Optional |
| `Octo-Env: test/live` | Empfohlen | **Nicht vorhanden** |
| `Accept-Language` | Unterstützt (Inhalte übersetzt) | Nicht dokumentiert |

**Response-Header:**
- Ventrata: `Octo-Capabilities`, `Octo-Env`, `Content-Language`, `Octo-Available-Languages`
- Go City: Nicht explizit dokumentiert

---

## Tabelle 5: Endpunkte

| Endpunkt | Ventrata | Go City |
|---------|----------|---------|
| `GET /octo/capabilities` | Ja | **Nein** |
| `GET /octo/supplier` | Ja | Ja |
| `GET /octo/products` | Ja | Ja |
| `GET /octo/products/{id}` | Ja | Ja |
| `POST /octo/availability` | Ja | Ja |
| `POST /octo/availability/calendar` | Ja | **Nein** |
| `POST /octo/availability/batch` | Ja | **Nein** |
| `POST /octo/availability/calendar/batch` | Ja | **Nein** |
| `GET /octo/bookings` | Ja | Ja |
| `POST /octo/bookings` | Ja | Ja |
| `GET /octo/bookings/{uuid}` | Ja | Ja |
| `PATCH /octo/bookings/{uuid}` | Ja | **Nein** |
| `POST /octo/bookings/{uuid}/confirm` | Ja | Ja |
| `POST /octo/bookings/{uuid}/cancel` | Ja | Ja |
| `POST /octo/bookings/{uuid}/extend` | Ja | **Nein** |
| `DELETE /octo/bookings/{uuid}` | Ja | **Nein** |
| Cart/Order-Endpunkte | Ja (octo/cart) | Nein |
| Gift-Voucher-Endpunkte | Ja (octo/gifts) | Nein |
| Redemption-Endpunkte | Ja (octo/redemption) | Nein |
| Webhook-Endpunkte | Ja (octo/webhooks) | Nein |

---

## Tabelle 6: Availability-Semantik

| Aspekt | Ventrata | Go City |
|--------|----------|---------|
| **Status-Werte** | AVAILABLE, FREESALE, SOLD_OUT, LIMITED, CLOSED | Nur **FREESALE** |
| **vacancies** | Anzahl freier Plätze (null bei FREESALE) | Immer **null** |
| **capacity** | Gesamtkapazität | Null oder gesetzt |
| **openingHours** | Tatsächliche Öffnungszeiten | Immer **00:00–23:59** |
| **Kalender-Endpoint** | `POST /availability/calendar` | **Nicht vorhanden** |
| **allDay** | true für OPENING_HOURS-Produkte | **Immer true** |
| **availabilityId in Booking** | Nur wenn availabilityRequired=true | **Immer Pflicht** (auch bei FREESALE) |
| **allowFreesale** | Produktabhängig | **Immer true** |

---

## Tabelle 7: Produkt-/Options-Schema

| Aspekt | Ventrata | Go City |
|--------|----------|---------|
| **Produktbegriff** | Tour, Aktivität, Attraktion | **Pass** (City Pass) |
| **availabilityType** | START_TIME oder OPENING_HOURS | Nur **OPENING_HOURS** |
| **Unit-Typen** | ADULT, YOUTH, CHILD, INFANT, FAMILY, SENIOR, STUDENT, MILITARY, OTHER | Nur **ADULT, CHILD** (+ VIP intern) |
| **deliveryFormats** | QRCODE, CODE128, PDF_URL, PKPASS_URL, AZTECCODE | Nur **PDF_URL, HTML_URL** |
| **Content-Felder** | Ja (mit octo/content): title, description, media, faqs, locations, etc. | **Nicht verfügbar** |
| **brand-Feld** | Nicht vorhanden | **Ja** (Go City, Great, Big Bus, Omnia) |
| **durationType-Feld** | Nicht vorhanden | **Ja** (DAYS, CHOICE) |
| **variant-Feld** | Nicht vorhanden | **Ja** (Standard, Plus, Lite, etc.) |
| **destinationId/Name** | Nicht vorhanden | **Ja** |
| **ID-Stabilität** | Stabil | **Kann sich ändern** — Warnung in der Spec! |

---

## Tabelle 8: Buchungs-Schema

| Aspekt | Ventrata | Go City |
|--------|----------|---------|
| **Booking-Status** | ON_HOLD, CONFIRMED, EXPIRED, CANCELLED, REDEEMED, PENDING, REJECTED, NO_SHOW, REBOOKED, QUOTE | ON_HOLD, CONFIRMED, EXPIRED, CANCELLED, REDEEMED, REJECTED (kein NO_SHOW, REBOOKED, QUOTE) |
| **supplierReference** | Vom Supplier generiert | 10-stellige Bestellnummer von Go City |
| **freesale-Feld** | Ja | Ja |
| **PATCH /bookings** | Ja | **Nein** |
| **extend** | Ja | **Nein** |
| **resellerReference** | Optional bei Reserve, optional bei Confirm | Optional aber **muss eindeutig sein** |
| **emailReceipt** | Ja (confirm) | Ja (confirm) — Go City sendet Pässe per E-Mail |
| **priceDistributionModel** | **Nicht vorhanden** | **Ja** (PUBLIC/RESTRICTED) |

---

## Tabelle 9: Pricing-Unterschiede

| Aspekt | Ventrata (octo/pricing) | Go City (octo/pricing) |
|--------|-------------------------|------------------------|
| **includedTaxes** | Ja — Tax-Objekte mit name, retail, original, net | **Nicht vorhanden** |
| **Preisfelder** | original, retail, net, currency, currencyPrecision, includedTaxes | original, retail, net, currency, currencyPrecision |
| **currency Parameter** | `currency` in Request-Body (Availability, Booking) | **Nicht vorhanden** |
| **priceDistributionModel** | **Nicht vorhanden** | PUBLIC oder RESTRICTED |
| **pricingPer** | BOOKING oder UNIT | Immer **UNIT** |
| **unitPricing in Availability** | Ja (Array von PricingUnit) | Ja (Array von OctoAvailabilityPricing) |
| **Staging-only** | In Production verfügbar | Nur Staging (Stand Aug 2024) |

---

## Fallstricke bei gleichzeitiger Integration beider APIs

### 1. Verschiedene Base-URLs pro Umgebung

```
Ventrata Test:      https://api.ventrata.com/octo (+ Octo-Env: test Header)
Ventrata Prod:      https://api.ventrata.com/octo (+ Octo-Env: live Header)

Go City Staging:    https://api.staging.gocity.tech/octo
Go City Prod:       https://api.gocity.com/octo
```

Kein gemeinsamer URL-Aufbau — separate Konfiguration pro Supplier notwendig.

### 2. Octo-Capabilities Header-Pflicht

```
Ventrata: Header MUSS vorhanden sein (auch leer: "Octo-Capabilities: ")
          → Fehlen = 400 Bad Request

Go City:  Header ist optional
          → Kein Header = kein Pricing in Response
```

Empfehlung: Header bei beiden immer senden — schadet nicht bei Go City, ist Pflicht bei Ventrata.

### 3. Availability immer FREESALE

Bei Go City kann man die Availability-Prüfung nicht überspringen, obwohl immer FREESALE. Die `availabilityId` ist für die Buchung pflicht (Abrechnung nach Reisedatum).

```
Ventrata: IF allowFreesale=true → Availability optional
Go City:  availabilityRequired=true → Availability IMMER nötig
```

### 4. Keine Kalender-Ansicht bei Go City

```
Ventrata: POST /availability/calendar   → Tag-für-Tag-Übersicht für UI-Kalender
Go City:  NICHT VERFÜGBAR
```

Für Go City muss ein Datumsbereich mit `POST /availability` abgefragt und selbst gruppiert werden.

### 5. Produkt-IDs können sich ändern

Bei Go City: "This id may change in certain scenarios due to upcoming development. Please verify it aligns with the latest implementation if issues arise."

Bei Ventrata sind IDs stabil. → Go City-IDs sollten regelmäßig aktualisiert und nicht dauerhaft gecacht werden.

### 6. priceDistributionModel ist Go-City-spezifisch

```
Go City: ?priceDistributionModel=PUBLIC (Standard) oder RESTRICTED
Ventrata: Kein solcher Parameter
```

Mapping-Schicht muss diesen Parameter nur für Go City-Requests anhängen.

### 7. Delivery-Formate sind unterschiedlich

```
Ventrata: QRCODE, CODE128, AZTECCODE, PKPASS_URL, PDF_URL
Go City:  PDF_URL, HTML_URL
```

QR-Code-Anzeige direkt aus dem Delivery-Wert funktioniert nur bei Ventrata.
Bei Go City muss immer die URL aufgerufen und das PDF/HTML gerendert werden.

### 8. Stornierungsfenster-Semantik

```
Ventrata: cancellationCutoffAmount = positiver Wert (Stunden/Tage VOR Reise)
Go City:  cancellationCutoffAmount = NEGATIVER Wert (Tage NACH Bestätigung)
          Beispiel: -365 = bis 365 Tage nach Kauf stornierbar
```

Die Vorzeichen-Logik ist invertiert! Bei der Anzeige von Stornierungsbedingungen muss zwischen beiden Lieferanten unterschieden werden.

### 9. UnitItem-Status

```
Ventrata: Mehr Status-Werte (incl. NO_SHOW, REBOOKED, QUOTE)
Go City:  ON_HOLD, CONFIRMED, EXPIRED, CANCELLED, REDEEMED, PENDING, REJECTED
```

### 10. Keine erweiterten Buchungsoperationen bei Go City

Änderungen nach der Buchung (PATCH) und Verlängerung der ON_HOLD-Zeit (extend) sind bei Go City nicht möglich. Stattdessen: Stornierung und Neubuchung.

---

## Integrations-Empfehlungen

### Adapter-Pattern

Beim Aufbau einer abstrakten Schicht für beide APIs:

```php
interface OctoSupplierAdapter {
    public function getProducts(): array;
    public function checkAvailability(AvailabilityRequest $req): array;
    public function createBooking(BookingRequest $req): Booking;
    public function confirmBooking(string $bookingId, ConfirmRequest $req): Booking;
    public function cancelBooking(string $bookingId, CancelRequest $req): Booking;
}

class VentrataAdapter implements OctoSupplierAdapter { ... }
class GoCityAdapter implements OctoSupplierAdapter { ... }
```

### Mapping-Besonderheiten

| Feld | Mapping-Logik |
|------|--------------|
| `cancellationCutoffAmount` | Ventrata: positiv (vor Reise) / Go City: negativ (nach Kauf) |
| `deliveryFormats` | Gemeinsam: PDF_URL. Nur Ventrata: QRCODE, CODE128, etc. |
| `status` (Availability) | Beide: FREESALE-handling. Ventrata: zusätzlich SOLD_OUT, LIMITED, etc. |
| `unitType` | Ventrata: 9 Typen. Go City: nur ADULT, CHILD |
| `priceDistributionModel` | Nur Go City — im Adapter optional anhängen |
| `Octo-Env` | Nur Ventrata — Go City hat separate Server-URLs |

---

**Quellen:**
- `/tmp/gocity-openapi.json` — Go City Trade API V2 OpenAPI 3.1 Spec (autoritativ)
- Ventrata OCTO API Skills: `octo-overview`, `octo-headers`, `octo-products`, `octo-availability`, `octo-bookings`, `octo-pricing`
