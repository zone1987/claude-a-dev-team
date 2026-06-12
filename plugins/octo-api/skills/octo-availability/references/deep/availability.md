# OCTO API — Availability & AvailabilityCalendar

## Überblick

Der erste Schritt beim Verkauf ist die Verfügbarkeitsprüfung. Wenn `allowFreesale` auf `true` gesetzt ist, ist dieser Schritt optional — es wird jedoch trotzdem empfohlen, um Schließungen und Betriebsgrenzen zu erkennen.

---

## Endpunkte

### POST /availability/

Prüft Verfügbarkeit für einen Datumsbereich oder spezifische IDs.

```http
POST https://api.ventrata.com/octo/availability/
Authorization: Bearer {api_key}
Content-Type: application/json
Octo-Capabilities: octo/pricing
```

**Response:** `200 Array<Availability>`

**Fehler (400):**
- `ErrorInvalidProductId`
- `ErrorInvalidOptionId`
- `ErrorBadRequest`
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`

---

### POST /availability/calendar

Gibt eine kalendarische Übersicht der Verfügbarkeit zurück (ein Eintrag pro Tag).

```http
POST https://api.ventrata.com/octo/availability/calendar
Authorization: Bearer {api_key}
Content-Type: application/json
Octo-Capabilities: octo/pricing
```

**Response:** `200 Array<AvailabilityCalendar>`

**Fehler (400):**
- `ErrorInvalidProductId`
- `ErrorInvalidOptionId`
- `ErrorBadRequest`
- `ErrorUnauthorized`
- `ErrorInternalServerError`
- `ErrorForbidden`

---

### POST /availability/batch

Batch-Verfügbarkeitsprüfung (mehrere Anfragen in einem Call).

```http
POST https://api.ventrata.com/octo/availability/batch
```

---

### POST /availability/calendar/batch

Batch-Kalender-Verfügbarkeitsprüfung.

```http
POST https://api.ventrata.com/octo/availability/calendar/batch
```

---

## AvailabilityCheckBody — Request-Schema

```typescript
type AvailabilityCheckBody = {
  productId: string;               // (Pflicht) Die Produkt-ID
  optionId: string;                // (Pflicht) Die Options-ID
  localDateStart?: string;         // Startdatum (YYYY-MM-DD) — nötig wenn localDateEnd gesetzt
  localDateEnd?: string;           // Enddatum (YYYY-MM-DD) — nötig wenn localDateStart gesetzt
  availabilityIds?: string[];      // Ergebnisse auf bestimmte IDs filtern
  units?: AvailabilityUnit[];      // Gewünschte Unit-Mengen
  currency?: string | null;        // Nur mit octo/pricing — ISO 4217 Währungscode
};

type AvailabilityUnit = {
  id: string;       // Unit-ID
  quantity: number; // Anzahl
};
```

### Request-Beispiel

```json
{
  "productId": "abc-123",
  "optionId": "option-default",
  "localDateStart": "2025-07-01",
  "localDateEnd": "2025-07-07",
  "units": [
    { "id": "adult", "quantity": 2 },
    { "id": "child", "quantity": 1 }
  ]
}
```

---

## AvailabilityCalendarBody — Request-Schema

```typescript
type AvailabilityCalendarBody = {
  productId: string;           // (Pflicht)
  optionId: string;            // (Pflicht)
  localDateStart?: string;     // (YYYY-MM-DD)
  localDateEnd?: string;       // (YYYY-MM-DD)
  units?: AvailabilityUnit[];
  currency?: string | null;    // Nur mit octo/pricing
};
```

---

## Availability-Response-Schema

```typescript
type Availability = {
  // --- Pflichtfelder ---
  id: string;                     // Eindeutiger Identifier (wird für Buchung benötigt!)
                                  // Format: ISO 8601 datetime, z.B. "2024-11-17T09:00:00+00:00"
  localDateTimeStart: string;     // Startzeit in lokaler Zeitzone (ISO 8601)
  localDateTimeEnd: string;       // Endzeit in lokaler Zeitzone (ISO 8601)
  utcCutoffAt: string;            // Deadline für Buchungsbestätigung (UTC)
  allDay: boolean;                // true = ganztägig (keine spezifischen Zeiten)
  available: boolean;             // true = Slots verfügbar
  status: AvailabilityStatus;     // Siehe Enum
  vacancies: number | null;       // Verbleibende freie Plätze (null bei FREESALE)
  capacity: number | null;        // Gesamtkapazität
  maxUnits: number | null;        // Max. Units pro Buchung in diesem Slot
  openingHours: OpeningHours[];   // Öffnungszeiten (auch bei START_TIME-Produkten)

  // --- Pricing-Felder (nur mit octo/pricing) ---
  unitPricing?: PricingUnit[];    // Preise pro Unit-Typ
  pricing?: Pricing;              // Gesamtpreis

  // --- Content-Felder (nur mit octo/content) ---
  title?: string | null;          // Öffentlicher Name der Availability
  shortDescription?: string;      // Kurzbeschreibung
};

type OpeningHours = {
  from: string; // Öffnungszeit (z.B. "09:00")
  to: string;   // Schließungszeit (z.B. "18:00")
};
```

### AvailabilityStatus Enum

```typescript
enum AvailabilityStatus {
  AVAILABLE = 'AVAILABLE',   // Offen für Buchungen
  FREESALE = 'FREESALE',     // Unbegrenzte Verfügbarkeit (kein Kapazitätslimit)
  SOLD_OUT = 'SOLD_OUT',     // Keine freien Plätze
  LIMITED = 'LIMITED',       // Weniger als 50% Kapazität verbleibend
  CLOSED = 'CLOSED',         // Availability ist geschlossen
}
```

### Response-Beispiel

```json
[
  {
    "id": "2025-07-01T09:00:00+00:00",
    "localDateTimeStart": "2025-07-01T09:00:00+00:00",
    "localDateTimeEnd": "2025-07-01T11:00:00+00:00",
    "utcCutoffAt": "2025-07-01T08:00:00+00:00",
    "allDay": false,
    "available": true,
    "status": "AVAILABLE",
    "vacancies": 15,
    "capacity": 20,
    "maxUnits": 10,
    "openingHours": [
      { "from": "09:00", "to": "17:00" }
    ]
  },
  {
    "id": "2025-07-01T14:00:00+00:00",
    "localDateTimeStart": "2025-07-01T14:00:00+00:00",
    "localDateTimeEnd": "2025-07-01T16:00:00+00:00",
    "utcCutoffAt": "2025-07-01T13:00:00+00:00",
    "allDay": false,
    "available": true,
    "status": "LIMITED",
    "vacancies": 3,
    "capacity": 20,
    "maxUnits": 10,
    "openingHours": [
      { "from": "09:00", "to": "17:00" }
    ]
  }
]
```

---

## AvailabilityCalendar-Response-Schema

```typescript
type AvailabilityCalendar = {
  // --- Pflichtfelder ---
  localDate: string;              // Datum (ISO 8601, z.B. "2024-11-18")
  available: boolean;             // true = Verfügbarkeit vorhanden
  status: AvailabilityStatus;     // AVAILABLE | FREESALE | SOLD_OUT | LIMITED | CLOSED
  vacancies: number | null;       // Höchste verbleibende Slots (aus allen Availabilities des Tages)
  capacity: number | null;        // Gesamtkapazität für den Tag
  openingHours: OpeningHours[];   // Öffnungszeiten

  // --- Pricing-Felder (nur mit octo/pricing) ---
  unitPricingFrom?: PricingUnit[]; // Ab-Preise pro Unit
  pricingFrom?: Pricing;           // Ab-Gesamtpreis
};
```

### Calendar Response-Beispiel

```json
[
  {
    "localDate": "2025-07-01",
    "available": true,
    "status": "AVAILABLE",
    "vacancies": 15,
    "capacity": 40,
    "openingHours": [
      { "from": "09:00", "to": "17:00" }
    ]
  },
  {
    "localDate": "2025-07-02",
    "available": false,
    "status": "SOLD_OUT",
    "vacancies": 0,
    "capacity": 40,
    "openingHours": [
      { "from": "09:00", "to": "17:00" }
    ]
  }
]
```

---

## Typisches Availability-Workflow

```
1. GET /products/           → Produkte laden, allowFreesale prüfen
2. POST /availability/calendar → Verfügbare Tage im Überblick laden
3. POST /availability/      → Spezifische Zeitslots für gewählten Tag laden
4. Availability-ID merken  → Wird für Buchung benötigt
5. POST /bookings/          → Mit availabilityId reservieren
```

---

## Wichtige Hinweise

- Die `id` der Availability wird als `availabilityId` beim Buchungsreservieren verwendet
- Bei `FREESALE`-Status: `vacancies` sollte `null` oder weggelassen werden
- `maxUnits`: Maximum Units in einer einzelnen Buchung in diesem Slot
- Bei `OPENING_HOURS`-Produkten: `allDay` kann `true` sein
- `utcCutoffAt`: Ablaufzeit für Buchungsbestätigung

---

**Quellen:**
- https://docs.ventrata.com/octo-core/availability
- https://github.com/octotravel/octo-types (TypeScript-Typdefinitionen)
