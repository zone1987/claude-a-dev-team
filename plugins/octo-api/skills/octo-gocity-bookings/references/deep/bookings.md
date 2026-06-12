# Go City Trade API V2 — Bookings (vollständige Referenz)

## Buchungs-Lifecycle

```
1. POST /octo/availability     → availabilityId erhalten
2. POST /octo/bookings         → Reservierung erstellen (Status: ON_HOLD)
3. POST /octo/bookings/{id}/confirm → Buchung bestätigen (Status: CONFIRMED)

Optional:
   POST /octo/bookings/{id}/cancel  → Buchung stornieren (Status: CANCELLED)
   GET  /octo/bookings              → Buchungen auflisten/filtern
   GET  /octo/bookings/{id}         → Einzelne Buchung abrufen
```

---

## Endpunkt 1: GET /octo/bookings

Buchungen nach Filtern abrufen. **Mindestens einer der folgenden Query-Parameter muss angegeben werden:**
- `resellerReference`
- `supplierReference`
- `localDate`
- `localDateStart` + `localDateEnd`

```http
GET https://api.gocity.com/octo/bookings?resellerReference=your-order-1
Authorization: Bearer {your_token}
```

**Query-Parameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `resellerReference` | string | Nein* | Reseller-Referenz auf der Buchung |
| `supplierReference` | string | Nein* | Vom Supplier generierte Referenz |
| `localDate` | string | Nein* | Alle Buchungen für ein bestimmtes Datum |
| `localDateStart` | string | Nein* | Startdatum eines Datumsbereichs |
| `localDateEnd` | string | Nein* | Enddatum eines Datumsbereichs |
| `productId` | string | Nein | Filter nach Produkt-ID |
| `optionId` | string | Nein | Filter nach Options-ID |

*Mind. einer dieser Parameter muss angegeben werden.

**Response:** `200 Array<OctoBooking>`

---

## Endpunkt 2: POST /octo/bookings (Reservierung)

Erstellt eine Buchung mit Status `ON_HOLD`. Die Buchung bleibt ON_HOLD bis sie bestätigt wird oder die Reservierungszeit abläuft.

```http
POST https://api.gocity.com/octo/bookings
Authorization: Bearer {your_token}
Content-Type: application/json
```

**Query-Parameter:**

| Parameter | Typ | Pflicht | Standard | Beschreibung |
|-----------|-----|---------|---------|--------------|
| `priceDistributionModel` | string | Nein | `PUBLIC` | `PUBLIC` oder `RESTRICTED` |

### OctoBookingRequest — Request-Schema

```typescript
type OctoBookingRequest = {
  // --- Pflichtfelder (implizit) ---
  productId: string;             // Produkt-ID
  optionId: string;              // Options-ID
  availabilityId: string;        // Availability-ID aus POST /octo/availability
  unitItems: OctoRequestUnit[];  // Liste der Units (mind. 1)

  // --- Optionale Felder ---
  uuid?: string;                 // Eigene UUID als Idempotenz-Key (verhindert Doppelbuchungen)
                                 // Wenn gleiche UUID nochmals gesendet → bestehende Buchung zurückgegeben
  expirationMinutes?: number;    // Reservierungsdauer in Minuten (Standard: Supplier-Default)
                                 // Beispiel: 60
  notes?: string;                // Optionale Notizen für die Buchung
  priceDistributionModel?: string; // "PUBLIC" oder "RESTRICTED"
};

type OctoRequestUnit = {
  unitId: string;  // Unit-ID (UUID) — aus OctoUnit.id
};
```

### Beispiel-Request (Reserve)

```http
POST https://api.gocity.com/octo/bookings
Authorization: Bearer {your_token}
Content-Type: application/json

{
  "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "productId": "a1b2c3d4-0000-0000-0000-000000000001",
  "optionId": "8a435677-1413-4012-8f5e-18eb15f54985",
  "availabilityId": "2025-08-15T00:00:00+00:00",
  "unitItems": [
    { "unitId": "u1u2u3u4-0000-0000-0000-000000000001" },
    { "unitId": "u1u2u3u4-0000-0000-0000-000000000001" },
    { "unitId": "u5u6u7u8-0000-0000-0000-000000000002" }
  ],
  "expirationMinutes": 60,
  "notes": "Familie Mustermann, Sommer-Ausflug"
}
```

**Response:** `200 OctoBooking` (Status: `ON_HOLD`)

---

## Endpunkt 3: GET /octo/bookings/{id}

Status einer bestehenden Buchung abrufen.

```http
GET https://api.gocity.com/octo/bookings/{id}
Authorization: Bearer {your_token}
```

**Path-Parameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `id` | string (uuid) | Ja | UUID der Buchung |

**Response:** `200 OctoBooking`

---

## Endpunkt 4: POST /octo/bookings/{id}/confirm (Bestätigung)

Bestätigt die Buchung — macht sie verwendbar. Der Kunde erhält sein(e) Ticket(s)/Pass(es).

```http
POST https://api.gocity.com/octo/bookings/{id}/confirm
Authorization: Bearer {your_token}
Content-Type: application/json
```

**Path-Parameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `id` | string (uuid) | Ja | UUID der Buchung |

**Query-Parameter:**

| Parameter | Typ | Pflicht | Standard | Beschreibung |
|-----------|-----|---------|---------|--------------|
| `priceDistributionModel` | string | Nein | `PUBLIC` | `PUBLIC` oder `RESTRICTED` |

### OctoBookingConfirmationRequest — Request-Schema

```typescript
type OctoBookingConfirmationRequest = {
  // --- Kontakt (Pflicht — enthält E-Mail für die Buchung) ---
  contact: OctoContact;           // Pflicht — Kontaktdaten des Hauptreisenden

  // --- Optionale Felder ---
  emailReceipt?: boolean;         // Go City soll E-Mail mit Pässen an Kunden senden
  resellerReference?: string;     // Reseller-Referenz/Bestellnummer (muss eindeutig sein!)
                                  // Beispiel: "your-company-order-1"
  unitItems?: OctoUnitItem[];     // Unit Items — ACHTUNG: ALLE Unit Items aus der
                                  // ursprünglichen Reservierung angeben!
                                  // Mehr oder weniger Items = Änderung der Ticketanzahl
};

type OctoContact = {
  fullName?: string;              // Optional
  firstName?: string;             // Optional
  lastName?: string;              // Optional
  emailAddress: string;           // Pflicht — E-Mail-Adresse des Kunden
  phoneNumber?: string;           // Optional
  locales: string[];              // Pflicht — Sprachpräferenzen (BCP 47)
                                  // Enum: "en" | "es" | "da" | "de" | "fr" | "it" |
                                  //        "ja" | "ko" | "pt" | "sv" | "zh-hans" | "zh-hant"
  postalCode?: string;            // Optional
  country?: string;               // Optional
  notes?: string;                 // Optional
};
```

> **WICHTIG bei unitItems in confirm:** Wenn `unitItems` angegeben werden, MÜSSEN alle Unit Items enthalten sein (auch unveränderte). Fehlende Items werden aus der Buchung entfernt. Dies ist der Mechanismus zum Ändern der Ticket-Anzahl beim Bestätigen.

### Beispiel-Request (Confirm)

```http
POST https://api.gocity.com/octo/bookings/a1b2c3d4-e5f6-7890-abcd-ef1234567890/confirm
Authorization: Bearer {your_token}
Content-Type: application/json

{
  "emailReceipt": true,
  "resellerReference": "your-company-order-1",
  "contact": {
    "firstName": "Max",
    "lastName": "Mustermann",
    "emailAddress": "max@beispiel.de",
    "phoneNumber": "+4915123456789",
    "locales": ["de", "en"]
  }
}
```

**Response:** `200 OctoBooking` (Status: `CONFIRMED`)

---

## Endpunkt 5: POST /octo/bookings/{id}/cancel (Stornierung)

Eine Buchung kann nur storniert werden, wenn `booking.cancellable` = `true` und innerhalb des Stornierungsfensters.

```http
POST https://api.gocity.com/octo/bookings/{id}/cancel
Authorization: Bearer {your_token}
Content-Type: application/json
```

**Path-Parameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `id` | string (uuid) | Ja | UUID der Buchung |

### OctoBookingCancellationRequest — Request-Schema

```typescript
type OctoBookingCancellationRequest = {
  force?: boolean;   // Buchung zwangsstornieren (auch wenn cancellable=false)
  reason?: string;   // Stornierungsgrund (Freitext)
};
```

### Beispiel-Request (Cancel)

```json
{
  "reason": "Kunde hat Reise storniert",
  "force": false
}
```

**Response:** `200 OctoBooking` (Status: `CANCELLED`)

---

## OctoBooking — Response-Schema (vollständig)

```typescript
type OctoBooking = {
  // --- Identifikatoren ---
  id: string;                    // UUID — System-Buchungs-ID von Go City
  uuid: string;                  // UUID als Idempotenz-Key (vom Reseller gesetzt oder auto)
  supplierReference: string;     // Eindeutige 10-stellige Bestellnummer von Go City
  resellerReference: string;     // UUID als Idempotenz-Key (vom Reseller gesetzt)
  testMode: boolean;             // true = Buchung in Test-Modus erstellt

  // --- Status ---
  status: OctoBookingStatus;

  // --- Zeitstempel (alle ISO 8601 UTC) ---
  utcCreatedAt: string;          // Erstellungszeitpunkt
  utcUpdatedAt: string;          // Letzter Update
  utcExpiresAt: string | null;   // Ablaufzeit wenn Status ON_HOLD, sonst null
  redeemedAt: string | null;     // Einlösezeitpunkt
  utcConfirmedAt: string | null; // Bestätigungszeitpunkt

  // --- Produkt-Referenzen ---
  productId: string;             // UUID des gebuchten Produkts
  product: OctoProduct;          // Vollständiges Produkt-Objekt (nur gebuchte Options/Units)
  optionId: string;              // ID der gebuchten Option
  option: OctoOption;            // Vollständiges Options-Objekt

  // --- Stornierung ---
  cancellable: boolean;          // Kann diese Buchung storniert werden?
  cancellation: OctoCancellation | null; // Stornierungsdetails (null wenn nicht storniert)

  // --- Availability ---
  freesale: boolean;             // true = ohne Availability-Prüfung gebucht
  availabilityId: string;        // Verwendete Availability-ID
  availability: OctoAvailability; // Verwendetes Availability-Objekt

  // --- Kontakt ---
  contact: OctoContact;          // Kontaktdaten Hauptreisender

  // --- Sonstiges ---
  notes: string | null;          // Notizen
  deliveryMethods: Array<"TICKET">;  // Immer TICKET bei Go City

  // --- Einlassdokumente ---
  voucher: OctoTicket;           // Voucher (wie der Pass eingelöst wird)
  unitItems: OctoUnitItem[];     // Einzelne Tickets pro Person

  // --- Pricing (nur mit octo/pricing) ---
  pricing?: OctoPricing;         // Gesamtpreis der Buchung
};
```

### OctoBookingStatus Enum

| Status | Bedeutung |
|--------|-----------|
| `ON_HOLD` | Reserviert, noch nicht bestätigt — wartet auf Zahlung/Kontaktdaten |
| `CONFIRMED` | Bestätigt — Pässe wurden ausgestellt und sind verwendbar |
| `REDEEMED` | Pässe wurden bei Attraktion(en) eingelöst/verwendet |
| `EXPIRED` | Nicht rechtzeitig bestätigt — Reservierung abgelaufen |
| `CANCELLED` | Storniert |
| `REJECTED` | Abgelehnt |

---

## OctoCancellation-Schema

```typescript
type OctoCancellation = {
  refund: "FULL" | "PARTIAL" | "NONE"; // Art der Rückerstattung
  reason: string;                       // Stornierungsgrund (Freitext)
  utcCancelledAt: string;               // ISO 8601 UTC Stornierungszeitpunkt
};
```

---

## OctoUnitItem-Schema

```typescript
type OctoUnitItem = {
  uuid: string;                  // UUID des Unit Items
  supplierReference: string;     // 10-stellige Bestellnummer von Go City für dieses Item
  resellerReference: string;     // Reseller-Referenz des Unit Items
  unitId: string;                // ID der referenzierten Unit
  unit: OctoUnit;                // Vollständiges Unit-Objekt
  status: OctoUnitItemStatus;    // Status dieses Unit Items
  utcRedeemedAt: string | null;  // Einlösezeitpunkt (ISO 8601 UTC)
  contact: OctoContact | null;   // Kontaktdaten für dieses Ticket (optional, wird nicht verwendet)
  ticket: OctoTicket;            // Ticket-Dokument (Barcode/PDF-Link)
};

// UnitItem-Status-Werte:
type OctoUnitItemStatus =
  | "ON_HOLD"
  | "CONFIRMED"
  | "EXPIRED"
  | "CANCELLED"
  | "REDEEMED"
  | "PENDING"
  | "REJECTED";
```

---

## OctoTicket-Schema

```typescript
type OctoTicket = {
  redemptionMethod: "DIGITAL" | "PRINT"; // Einlöse-Methode
  utcRedeemedAt: string | null;           // Zeitpunkt der Einlösung
  deliveryOptions: OctoDeliveryOption[];  // Alle verfügbaren Lieferformate
};

type OctoDeliveryOption = {
  deliveryFormat: "PDF_URL" | "HTML_URL"; // Format
  deliveryValue: string;                   // URL zum PDF oder HTML-Seite
};
```

---

## Vollständige Booking-Response (Beispiel nach CONFIRMED)

```json
{
  "id": "b1b2b3b4-0000-0000-0000-000000000001",
  "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "supplierReference": "GC1234567890",
  "resellerReference": "your-company-order-1",
  "testMode": false,
  "status": "CONFIRMED",
  "utcCreatedAt": "2025-08-10T10:00:00Z",
  "utcUpdatedAt": "2025-08-10T10:05:00Z",
  "utcExpiresAt": null,
  "redeemedAt": null,
  "utcConfirmedAt": "2025-08-10T10:05:00Z",
  "productId": "a1b2c3d4-0000-0000-0000-000000000001",
  "optionId": "8a435677-1413-4012-8f5e-18eb15f54985",
  "cancellable": true,
  "cancellation": null,
  "freesale": false,
  "availabilityId": "2025-08-15T00:00:00+00:00",
  "contact": {
    "fullName": "Max Mustermann",
    "firstName": "Max",
    "lastName": "Mustermann",
    "emailAddress": "max@beispiel.de",
    "phoneNumber": "+4915123456789",
    "locales": ["de", "en"],
    "postalCode": null,
    "country": null,
    "notes": null
  },
  "notes": "Familie Mustermann, Sommer-Ausflug",
  "deliveryMethods": ["TICKET"],
  "voucher": {
    "redemptionMethod": "DIGITAL",
    "utcRedeemedAt": null,
    "deliveryOptions": [
      {
        "deliveryFormat": "PDF_URL",
        "deliveryValue": "https://api.gocity.com/passes/abc123.pdf"
      },
      {
        "deliveryFormat": "HTML_URL",
        "deliveryValue": "https://api.gocity.com/passes/abc123"
      }
    ]
  },
  "unitItems": [
    {
      "uuid": "ui-uuid-1",
      "supplierReference": "GC1234567891",
      "resellerReference": null,
      "unitId": "u1u2u3u4-0000-0000-0000-000000000001",
      "status": "CONFIRMED",
      "utcRedeemedAt": null,
      "contact": null,
      "ticket": {
        "redemptionMethod": "DIGITAL",
        "utcRedeemedAt": null,
        "deliveryOptions": [
          {
            "deliveryFormat": "PDF_URL",
            "deliveryValue": "https://api.gocity.com/tickets/ticket1.pdf"
          }
        ]
      }
    }
  ],
  "pricing": {
    "original": 0,
    "retail": 18400,
    "net": 17480,
    "currency": "USD",
    "currencyPrecision": 2
  }
}
```

---

## Stornierungslogik

- `booking.cancellable` prüfen bevor Stornierung versucht wird
- Stornierungsfenster: durch `option.cancellationCutoffAmount` und `option.cancellationCutoffUnit` definiert
- Negativer Wert (z.B. -365 Tage): Stornierung bis 365 Tage nach Bestätigung möglich
- `force: true` im Cancel-Request kann Beschränkungen überschreiben

---

## Idempotenz

Die `uuid` im BookingRequest dient als Idempotenz-Key:
- Gleiche UUID bei erneutem Request → Server gibt bestehende Buchung zurück statt neue zu erstellen
- Verhindert Doppelbuchungen bei Netzwerk-Timeouts oder Retry-Versuchen
- Empfehlung: UUID pro Buchungsversuch generieren und sicher speichern

---

## Unterschiede zu Ventrata-Bookings

| Feature | Ventrata | Go City |
|---------|----------|---------|
| PATCH /bookings/{id} | Vorhanden | **Nicht vorhanden** |
| POST /bookings/{id}/extend | Vorhanden | **Nicht vorhanden** |
| DELETE /bookings/{id} | Vorhanden | **Nicht vorhanden** |
| booking.status PENDING | Vorhanden | Vorhanden |
| booking.status REDEEMED | Vorhanden | Vorhanden |
| deliveryFormats | QRCODE, CODE128, PDF_URL, etc. | Nur **PDF_URL, HTML_URL** |
| Octo-Env Header | Vorhanden (test/live) | **Nicht vorhanden** |

---

**Quellen:**
- `/tmp/gocity-openapi.json` — Go City Trade API V2 OpenAPI 3.1 Spec (autoritativ)
- `/tmp/gocity.html` — Gerenderte Redoc-Dokumentation
