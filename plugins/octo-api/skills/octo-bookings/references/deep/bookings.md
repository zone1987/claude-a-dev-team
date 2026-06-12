# OCTO API — Vollständiger Booking-Lifecycle

## Überblick

Der Buchungsprozess besteht aus drei Schritten:

```
1. Verfügbarkeit prüfen (POST /availability/)
2. Reservierung erstellen (POST /bookings/)      → Status: ON_HOLD
3. Buchung bestätigen (POST /bookings/{uuid}/confirm) → Status: CONFIRMED
```

Optional: Buchung stornieren (POST /bookings/{uuid}/cancel)

---

## Basis-URL

```
https://api.ventrata.com/octo
```

---

## Alle Booking-Endpunkte

| Methode | Endpunkt | Zweck |
|---------|---------|-------|
| `POST` | `/bookings/` | Reservierung erstellen (ON_HOLD) |
| `GET` | `/bookings/` | Buchungen auflisten |
| `GET` | `/bookings/{uuid}` | Einzelne Buchung abrufen |
| `PATCH` | `/bookings/{uuid}` | Buchung aktualisieren |
| `POST` | `/bookings/{uuid}/confirm` | Buchung bestätigen (CONFIRMED) |
| `POST` | `/bookings/{uuid}/cancel` | Buchung stornieren (CANCELLED) |
| `POST` | `/bookings/{uuid}/extend` | Reservierungs-Ablaufzeit verlängern |

---

## Schritt 1: Reservierung erstellen — POST /bookings/

```http
POST https://api.ventrata.com/octo/bookings/
Authorization: Bearer {api_key}
Content-Type: application/json
Octo-Capabilities: octo/pricing
Octo-Env: test
```

### BookingReservationBody — Request-Schema

```typescript
type BookingReservationBody = {
  uuid?: string;               // Eigene UUID als Idempotenz-Key (verhindert Doppelbuchungen)
  productId: string;           // (Pflicht) Produkt-ID
  optionId: string;            // (Pflicht) Options-ID
  availabilityId?: string;     // Availability-ID (Pflicht wenn availabilityRequired=true)
  expirationMinutes?: number;  // Reservierungsdauer in Minuten (Standard: Supplier-Default)
  notes?: string | null;       // Optionale Notizen
  unitItems: BookingUnitItem[]; // (Pflicht) Unit Items
  resellerReference?: string;  // Reseller-Referenz (= Voucher-Nummer)
  contact?: BookingContact;    // Kontaktdaten Lead-Traveler
  currency?: string | null;    // Nur mit octo/pricing
};

type BookingUnitItem = {
  uuid?: string;               // Eindeutige UUID pro Unit Item
  unitId: string;              // (Pflicht) Unit-ID (z.B. "adult")
  resellerReference?: string;
  contact?: BookingContact;    // Kontakt pro Ticket (wenn Supplier es fordert)
};

type BookingContact = {
  fullName?: string | null;
  firstName?: string | null;
  lastName?: string | null;
  emailAddress?: string | null;
  phoneNumber?: string | null;
  locales?: string[];          // BCP 47 Sprachpräferenzen
  postalCode?: string | null;
  country?: string | null;
  notes?: string | null;
};
```

### Request-Beispiel

```json
{
  "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "productId": "550e8400-e29b-41d4-a716-446655440000",
  "optionId": "DEFAULT",
  "availabilityId": "2025-07-01T09:00:00+00:00",
  "unitItems": [
    { "unitId": "adult", "uuid": "unit-uuid-1" },
    { "unitId": "adult", "uuid": "unit-uuid-2" },
    { "unitId": "child", "uuid": "unit-uuid-3" }
  ],
  "contact": {
    "firstName": "Max",
    "lastName": "Mustermann",
    "emailAddress": "max@beispiel.de",
    "phoneNumber": "+4915123456789",
    "locales": ["de", "en"]
  },
  "resellerReference": "BOOKING-12345"
}
```

**Response:** `200 Booking` (Status: `ON_HOLD`)

---

## Schritt 2: Buchung bestätigen — POST /bookings/{uuid}/confirm

```http
POST https://api.ventrata.com/octo/bookings/{uuid}/confirm
Authorization: Bearer {api_key}
Content-Type: application/json
Octo-Capabilities: octo/pricing
Octo-Env: test
```

### BookingConfirmationBody — Request-Schema

```typescript
type BookingConfirmationBody = {
  emailReceipt?: boolean;       // E-Mail mit Quittung/Tickets an Gast senden (Standard: false)
  resellerReference?: string;   // Reseller-Referenz (Voucher-Nummer)
  contact: BookingContact;      // (Pflicht) Kontaktdaten Lead-Traveler
  unitItems?: BookingUnitItem[]; // Alle Unit Items INKL. bestehender (sonst Anzahl-Änderung!)
};
```

**Wichtig:** Wenn `unitItems` angegeben wird, MÜSSEN alle Unit Items (auch bestehende) mit ihrer `uuid` enthalten sein. Fehlende Unit Items werden entfernt.

### Request-Beispiel

```json
{
  "emailReceipt": true,
  "resellerReference": "BOOKING-12345",
  "contact": {
    "firstName": "Max",
    "lastName": "Mustermann",
    "emailAddress": "max@beispiel.de",
    "phoneNumber": "+4915123456789",
    "locales": ["de", "en"]
  }
}
```

**Response:** `200 Booking` (Status: `CONFIRMED`)

---

## Buchung stornieren — POST /bookings/{uuid}/cancel

```http
POST https://api.ventrata.com/octo/bookings/{uuid}/cancel
Authorization: Bearer {api_key}
Content-Type: application/json
Octo-Capabilities:
```

### BookingCancellationBody — Request-Schema

```typescript
type BookingCancellationBody = {
  reason?: string | null;  // Stornierungsgrund
  force?: boolean;         // E-Mail mit Quittung an Gast senden (Standard: false)
};
```

**Response:** `200 Booking` (Status: `CANCELLED`)

---

## Buchung aktualisieren — PATCH /bookings/{uuid}

```typescript
type BookingUpdateBody = {
  resellerReference?: string;
  productId?: string;
  optionId?: string;
  availabilityId?: string;
  expirationMinutes?: number;
  notes?: string | null;
  emailReceipt?: boolean;
  unitItems?: BookingUnitItem[]; // Alle Unit Items mit uuid angeben!
  contact?: BookingContact;
};
```

---

## Reservierung verlängern — POST /bookings/{uuid}/extend

```typescript
type ExtendReservationBody = {
  expirationMinutes?: number; // Neue Ablaufzeit in Minuten
};
```

---

## Buchungen auflisten — GET /bookings/

```http
GET https://api.ventrata.com/octo/bookings/?resellerReference=BOOKING-12345
```

**Query-Parameter:**
- `resellerReference` (optional) — Reseller-Referenz
- `supplierReference` (optional) — Supplier-Referenz

**Response:** `200 Array<Booking>`

---

## Einzelne Buchung abrufen — GET /bookings/{uuid}

```http
GET https://api.ventrata.com/octo/bookings/{uuid}
```

**Response:** `200 Booking`

---

## Booking-Response-Schema (vollständig)

```typescript
type Booking = {
  // --- Identifikatoren ---
  id: string;                          // System-ID (vom Supplier generiert)
  uuid: string;                        // Idempotenz-Key (von Reseller gesetzt oder auto-generiert)
  testMode: boolean;                   // true = Testbuchung (Octo-Env: test)
  resellerReference: string | null;    // Reseller-Referenz
  supplierReference: string | null;    // Supplier-Referenz (für Kunden sichtbar!)

  // --- Status ---
  status: BookingStatus;               // Aktueller Buchungsstatus

  // --- Zeitstempel ---
  utcCreatedAt: string;                // Erstellungszeitpunkt (ISO 8601 UTC)
  utcUpdatedAt: string;                // Letzter Update (ISO 8601 UTC)
  utcExpiresAt: string | null;         // Ablaufzeit bei ON_HOLD (ISO 8601 UTC)
  utcRedeemedAt: string | null;        // Einlösungszeitpunkt (ISO 8601 UTC)
  utcConfirmedAt: string | null;       // Bestätigungszeitpunkt (ISO 8601 UTC)

  // --- Produkt-Referenzen ---
  productId: string;
  product?: Product;                   // Vollständiges Produkt-Objekt (wenn geladen)
  optionId: string;
  option?: Option;                     // Vollständiges Options-Objekt (wenn geladen)

  // --- Stornierung ---
  cancellable: boolean;                // Kann storniert werden
  cancellation: BookingCancellation | null; // Stornierungsdetails (wenn storniert)

  // --- Availability ---
  freesale: boolean;                   // true = ohne Availability-Prüfung gebucht
  availabilityId: string | null;       // Verwendete Availability-ID
  availability: Availability | null;  // Vollständiges Availability-Objekt

  // --- Kontakt ---
  contact: Contact;                    // Kontaktdaten Lead-Traveler

  // --- Sonstiges ---
  notes: string | null;               // Kundennotizen
  deliveryMethods: DeliveryMethod[];  // VOUCHER | TICKET

  // --- Einlassdokumente ---
  voucher: Ticket | null;             // Gesamtvoucher (wenn deliveryMethods=VOUCHER)
  unitItems: UnitItem[];              // Einzelne Tickets

  // --- Pricing (nur mit octo/pricing) ---
  pricing?: Pricing;
};
```

### BookingStatus Enum

```typescript
enum BookingStatus {
  ON_HOLD = 'ON_HOLD',       // Warte auf Bestätigung
  CONFIRMED = 'CONFIRMED',   // Erfolgreich bestätigt
  EXPIRED = 'EXPIRED',       // Nicht rechtzeitig bestätigt → abgelaufen
  CANCELLED = 'CANCELLED',   // Storniert
  REDEEMED = 'REDEEMED',     // Bereits eingelöst
  PENDING = 'PENDING',       // Wartet auf externe Bestätigung
  REJECTED = 'REJECTED',     // Abgelehnt
}
```

### BookingCancellation-Schema

```typescript
type BookingCancellation = {
  refund: Refund;             // FULL | PARTIAL | NONE
  reason: string | null;
  utcCancelledAt: string;     // Stornierungszeitpunkt
};

enum Refund {
  FULL = 'FULL',
  PARTIAL = 'PARTIAL',
  NONE = 'NONE',
}
```

---

## UnitItem-Schema

```typescript
type UnitItem = {
  uuid: string;                      // Eindeutige Unit-Item-ID
  resellerReference: string | null;
  supplierReference: string | null;
  unitId: string;                    // Referenzierte Unit-ID
  unit?: Unit;                       // Vollständiges Unit-Objekt
  status: BookingStatus;             // Eigener Status des Unit Items
  utcRedeemedAt: string | null;
  contact: Contact;                  // Kontaktdaten für dieses Ticket
  ticket: Ticket | null;             // Ticket-Einlassdokument
  pricing?: Pricing;                 // nur mit octo/pricing
};
```

---

## Ticket/Voucher-Schema

```typescript
type Ticket = {
  redemptionMethod: RedemptionMethod; // DIGITAL | MANIFEST | PRINT
  utcRedeemedAt: string | null;
  deliveryOptions: DeliveryOption[];  // Alle Lieferformate
};

type DeliveryOption = {
  deliveryFormat: DeliveryFormat;  // PDF_URL | QRCODE | CODE128 | PKPASS_URL | AZTECCODE
  deliveryValue: string;           // URL oder Code-Wert
};
```

### Response-Beispiel nach Bestätigung

```json
{
  "id": "booking-system-id",
  "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "testMode": true,
  "resellerReference": "BOOKING-12345",
  "supplierReference": "SUPP-ABC123",
  "status": "CONFIRMED",
  "utcCreatedAt": "2025-07-01T07:00:00Z",
  "utcUpdatedAt": "2025-07-01T07:05:00Z",
  "utcExpiresAt": null,
  "utcRedeemedAt": null,
  "utcConfirmedAt": "2025-07-01T07:05:00Z",
  "productId": "550e8400-e29b-41d4-a716-446655440000",
  "optionId": "DEFAULT",
  "cancellable": true,
  "cancellation": null,
  "freesale": false,
  "availabilityId": "2025-07-01T09:00:00+00:00",
  "availability": null,
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
  "notes": null,
  "deliveryMethods": ["VOUCHER", "TICKET"],
  "voucher": {
    "redemptionMethod": "DIGITAL",
    "utcRedeemedAt": null,
    "deliveryOptions": [
      {
        "deliveryFormat": "QRCODE",
        "deliveryValue": "BOOKING-QR-CODE-VALUE"
      },
      {
        "deliveryFormat": "PDF_URL",
        "deliveryValue": "https://cdn.ventrata.com/vouchers/abc123.pdf"
      }
    ]
  },
  "unitItems": [
    {
      "uuid": "unit-uuid-1",
      "resellerReference": null,
      "supplierReference": "TICKET-001",
      "unitId": "adult",
      "status": "CONFIRMED",
      "utcRedeemedAt": null,
      "contact": {
        "fullName": null,
        "firstName": null,
        "lastName": null,
        "emailAddress": null,
        "phoneNumber": null,
        "locales": [],
        "postalCode": null,
        "country": null,
        "notes": null
      },
      "ticket": {
        "redemptionMethod": "DIGITAL",
        "utcRedeemedAt": null,
        "deliveryOptions": [
          {
            "deliveryFormat": "QRCODE",
            "deliveryValue": "TICKET-QR-CODE-VALUE-1"
          }
        ]
      }
    }
  ],
  "pricing": {
    "original": 5000,
    "retail": 4500,
    "net": 3600,
    "currency": "EUR",
    "currencyPrecision": 2,
    "includedTaxes": [
      { "name": "MwSt.", "retail": 717, "original": 797, "net": null }
    ]
  }
}
```

---

## Contact-Schema (Response)

```typescript
type Contact = {
  fullName: string | null;
  firstName: string | null;
  lastName: string | null;
  emailAddress: string | null;
  phoneNumber: string | null;
  locales: string[];          // BCP 47 Sprachpräferenzen
  postalCode: string | null;
  country: string | null;
  notes: string | null;
};
```

---

## Voucher vs. Ticket

| | **Voucher** | **Ticket** |
|--|------------|-----------|
| Zugriff | `booking.voucher` | `booking.unitItems[].ticket` |
| Scope | Gesamte Buchung | Pro Unit Item |
| Wann | Wenn `deliveryMethods` = `VOUCHER` | Wenn `deliveryMethods` = `TICKET` |
| Null wenn | Voucher nicht unterstützt | Tickets nicht unterstützt |

**Empfehlung:** Beide Formate unterstützen — QR-Code in der UI anzeigen, PDF als Download anbieten (enthält vollständige Einlösungsdetails).

---

## supplierReference vs. Barcode

- **`supplierReference`:** Menschenlesbare, kompakte ID (z.B. "SUPP-ABC123") — **immer** kurz und lesbar
- **QR-Code-Wert:** Kann lang sein und offline-verifizierbare Daten enthalten — nicht als Klartext drucken
- **Empfehlung:** QR-Code als Bild anzeigen + `supplierReference` darunter drucken

---

## Idempotenz

Die `uuid` im Request-Body dient als Idempotenz-Key. Wenn derselbe `uuid`-Wert erneut gesendet wird (z.B. bei Netzwerk-Timeout), gibt der Server die bestehende Buchung zurück, anstatt eine neue zu erstellen.

---

## GET /bookings/ Filter-Parameter

Unterstützte Booking-Status für Filterung:
`REDEEMED`, `NO_SHOW`, `ON_HOLD`, `CANCELLED`, `EXPIRED`, `PENDING`, `REJECTED`, `REBOOKED`, `QUOTE`, `CONFIRMED`

---

**Quellen:**
- https://docs.ventrata.com/octo-core/bookings
- https://docs.ventrata.com/additional-resources/faqs
- https://github.com/octotravel/octo-types (TypeScript-Typdefinitionen)
