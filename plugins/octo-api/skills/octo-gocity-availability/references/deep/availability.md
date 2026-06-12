# Go City Trade API V2 — Availability (vollständige Referenz)

## Überblick

Obwohl Go City-Produkte **immer verfügbar** sind (unbegrenzte Kapazität), ist der Availability-Schritt implementiert, um:
1. Eine `availabilityId` für die Buchung zu erhalten (Pflicht für Abrechnung nach Reisedatum)
2. Standard-OCTO-Kompatibilität zu gewährleisten

---

## Endpunkt: POST /octo/availability

```http
POST https://api.gocity.com/octo/availability
Authorization: Bearer {your_token}
Content-Type: application/json
```

**Query-Parameter:**

| Parameter | Typ | Pflicht | Standard | Beschreibung |
|-----------|-----|---------|---------|--------------|
| `priceDistributionModel` | string | Nein | `PUBLIC` | `PUBLIC` oder `RESTRICTED` |
| `_capabilities` | string | Nein | — | Alternative zu Header: `octo/pricing` |

**Optional Header:**
```http
Octo-Capabilities: octo/pricing
```

**Response:** `200 Array<OctoAvailability>`

---

## OctoAvailabilityRequest — Request-Schema (vollständig)

```typescript
type OctoAvailabilityRequest = {
  // --- Pflichtfelder ---
  productId: string;              // (Pflicht) UUID des Produkts
  optionId: string;               // (Pflicht) UUID der Option

  // --- Datumsfilter (mind. eines der folgenden Kombinationen) ---
  localDate?: string;             // Einzelnes Datum: "YYYY-MM-DD", z.B. "2024-11-01"
  localDateStart?: string;        // Startdatum eines Zeitraums: "YYYY-MM-DD"
  localDateEnd?: string;          // Enddatum eines Zeitraums: "YYYY-MM-DD"
  availabilityIds?: string[];     // Ergebnisse auf bestimmte IDs filtern

  // --- Units (optional, für Pricing) ---
  units?: OctoAvailabilityUnit[]; // Wenn angegeben, wird pricing für diese Units berechnet
};

type OctoAvailabilityUnit = {
  id: string;       // Unit-ID (UUID)
  quantity: number; // Anzahl dieser Unit-Typ
};
```

### Pflichtfelder und Datums-Kombinationen

**Pflicht:** `productId` und `optionId` sind immer erforderlich.

**Mindestens eines dieser Datums-Muster muss angegeben werden:**
1. `localDate` — Ein einzelner Tag
2. `localDateStart` + `localDateEnd` — Ein Zeitraum
3. `availabilityIds` — Direkte ID-Filter

---

## OctoAvailability — Response-Schema (vollständig)

```typescript
type OctoAvailability = {
  // --- Kern-Felder ---
  id: string;                    // Availability-ID — WIRD FÜR BUCHUNG BENÖTIGT!
                                 // Format: ISO 8601 Datetime
  localDateTimeStart: string;    // Startzeit in lokaler Zeitzone (ISO 8601)
  localDateTimeEnd: string;      // Endzeit in lokaler Zeitzone (ISO 8601)
  allDay: boolean;               // true = ganztägige Verfügbarkeit, kein fester Abfahrtszeit.
                                 // Wenn true: nur ein Availability-Objekt pro Tag
  available: boolean;            // Ob Verfügbarkeit vorhanden ist — immer true (FREESALE)
  status: "FREESALE";            // IMMER "FREESALE" bei Go City
  vacancies: number | null;      // IMMER null bei Go City (FREESALE = unbegrenzt)
  capacity: number | null;       // Gesamtkapazität des Tages (kann gesetzt sein)
  maxUnits: number | null;       // Max. Units pro Buchung an diesem Tag/Slot
                                 // Beispiel: 50
  utcCutoffAt: string;           // Deadline für Buchungsbestätigung (ISO 8601 UTC)
  openingHours: OctoOpeningHours[]; // Öffnungszeiten — IMMER 00:00-23:59 bei Go City

  // --- Pricing-Felder (nur mit Octo-Capabilities: octo/pricing) ---
  unitPricing?: OctoAvailabilityPricing[]; // Preise pro Unit-ID
  pricing?: OctoPricing;                   // Gesamtpreis (nur wenn units in Request angegeben)
};

type OctoOpeningHours = {
  from: string;  // Immer "00:00" bei Go City
  to: string;    // Immer "23:59" bei Go City
};
```

---

## OctoAvailabilityPricing-Schema

Verfügbar im Array `unitPricing` wenn `octo/pricing` Capability aktiv:

```typescript
type OctoAvailabilityPricing = {
  unitId: string;          // Unit-ID zu der dieser Preis gehört
  original: number;        // Originalpreis (Strike-Through), Beispiel: 0
  retail: number;          // Verkaufspreis in Integer-Kleineinheit, Beispiel: 18400 = 184.00 USD
  net: number;             // Großhandelspreis, Beispiel: 17480 = 174.80 USD
  currency: string;        // Währungscode, z.B. "USD"
  currencyPrecision: number; // Dezimalstellen: 2 für USD, 0 für JPY
};
```

---

## Beispiel-Request (Einzeltag)

```http
POST https://api.gocity.com/octo/availability
Authorization: Bearer {your_token}
Content-Type: application/json
Octo-Capabilities: octo/pricing

{
  "productId": "a1b2c3d4-0000-0000-0000-000000000001",
  "optionId": "8a435677-1413-4012-8f5e-18eb15f54985",
  "localDate": "2025-08-15"
}
```

## Beispiel-Request (Zeitraum mit Units)

```http
POST https://api.gocity.com/octo/availability?priceDistributionModel=PUBLIC
Authorization: Bearer {your_token}
Content-Type: application/json
Octo-Capabilities: octo/pricing

{
  "productId": "a1b2c3d4-0000-0000-0000-000000000001",
  "optionId": "8a435677-1413-4012-8f5e-18eb15f54985",
  "localDateStart": "2025-08-15",
  "localDateEnd": "2025-08-17",
  "units": [
    { "id": "u1u2u3u4-0000-0000-0000-000000000001", "quantity": 2 },
    { "id": "u5u6u7u8-0000-0000-0000-000000000002", "quantity": 1 }
  ]
}
```

## Beispiel-Request (per availabilityIds)

```json
{
  "productId": "a1b2c3d4-0000-0000-0000-000000000001",
  "optionId": "8a435677-1413-4012-8f5e-18eb15f54985",
  "availabilityIds": [
    "2025-08-15T00:00:00+00:00",
    "2025-08-16T00:00:00+00:00"
  ]
}
```

---

## Beispiel-Response (ohne Pricing)

```json
[
  {
    "id": "2025-08-15T00:00:00+00:00",
    "localDateTimeStart": "2025-08-15T00:00:00+00:00",
    "localDateTimeEnd": "2025-08-15T23:59:00+00:00",
    "allDay": true,
    "available": true,
    "status": "FREESALE",
    "vacancies": null,
    "capacity": null,
    "maxUnits": 50,
    "utcCutoffAt": "2025-08-15T23:59:00Z",
    "openingHours": [
      { "from": "00:00", "to": "23:59" }
    ]
  }
]
```

## Beispiel-Response (mit octo/pricing und Units im Request)

```json
[
  {
    "id": "2025-08-15T00:00:00+00:00",
    "localDateTimeStart": "2025-08-15T00:00:00+00:00",
    "localDateTimeEnd": "2025-08-15T23:59:00+00:00",
    "allDay": true,
    "available": true,
    "status": "FREESALE",
    "vacancies": null,
    "capacity": null,
    "maxUnits": 50,
    "utcCutoffAt": "2025-08-15T23:59:00Z",
    "openingHours": [
      { "from": "00:00", "to": "23:59" }
    ],
    "unitPricing": [
      {
        "unitId": "u1u2u3u4-0000-0000-0000-000000000001",
        "original": 0,
        "retail": 18400,
        "net": 17480,
        "currency": "USD",
        "currencyPrecision": 2
      },
      {
        "unitId": "u5u6u7u8-0000-0000-0000-000000000002",
        "original": 0,
        "retail": 12400,
        "net": 11780,
        "currency": "USD",
        "currencyPrecision": 2
      }
    ],
    "pricing": {
      "original": 0,
      "retail": 49200,
      "net": 46740,
      "currency": "USD",
      "currencyPrecision": 2
    }
  }
]
```

---

## AvailabilityStatus

Bei Go City gibt es nur einen Status:

| Status | Bedeutung | Bei Go City |
|--------|-----------|------------|
| `FREESALE` | Unbegrenzte Kapazität | **Immer** dieser Status |
| `AVAILABLE` | Normale Verfügbarkeit | Nicht verwendet |
| `SOLD_OUT` | Ausverkauft | Nicht verwendet |
| `LIMITED` | Begrenzte Kapazität | Nicht verwendet |
| `CLOSED` | Geschlossen | Nicht verwendet |

---

## Workflow: Availability → Booking

```
1. POST /octo/availability   (mit productId, optionId, localDate)
   → Response enthält OctoAvailability mit id
   
2. Availability-ID merken   (= Wert von OctoAvailability.id)

3. POST /octo/bookings       (mit availabilityId = gemerkter ID)
```

---

## Wichtige Hinweise

- **Kein `/octo/availability/calendar`:** Go City implementiert keinen Kalender-Endpunkt (im Gegensatz zu Ventrata).
- **Kein `/octo/availability/batch`:** Kein Batch-Endpunkt.
- **availabilityRequired = true:** Trotz FREESALE muss `availabilityId` bei der Buchung angegeben werden (Go City rechnet nach Reisedatum ab).
- **ID-Format:** Die Availability-ID ist ein ISO-8601-Datetime-String.

---

**Quellen:**
- `/tmp/gocity-openapi.json` — Go City Trade API V2 OpenAPI 3.1 Spec (autoritativ)
- `/tmp/gocity.html` — Gerenderte Redoc-Dokumentation
