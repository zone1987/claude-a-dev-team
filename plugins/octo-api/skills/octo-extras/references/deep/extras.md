# OCTO — Extras Capability (`octo/extras`)

## Capability-Identifier

```
octo/extras
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/extras
Content-Type: application/json
```

---

## Überblick

Upsell-Items, die auf Booking-Ebene (Option-Level) oder pro Unit-Item (Unit-Level) konfiguriert
werden können. Beispiele: Lunchpakete, Fast-Track-Eingang, Erinnerungsfotos.

---

## Erweiterungen am Product-Schema

Endpunkte: `GET /products`, `GET /products/{productId}`

- `option.extras[]` — Booking-Level-Extras (für die gesamte Buchung)
- `unit.extras[]` — Unit-Level-Extras (pro Teilnehmer)

---

## Extra-Objekt (vollständiges Schema)

```typescript
interface Extra {
  id: string;                    // UUID-Format: "extra_<uuid>"; Requests akzeptieren beide Formate
  internalName: string;          // Interne Bezeichnung
  reference: string;             // Menschenlesbare Referenz
  title: string;                 // Anzeigename (nur mit octo/content)
  customRetail: boolean;         // Händler legt eigenen Preis fest
  customRetailOptions: number[]; // Vorgeschlagene Custom-Retail-Werte (Minor Units)
  restrictions: ExtraRestrictions;
}

interface ExtraRestrictions {
  required: boolean;                   // Pflichtauswahl
  default: boolean;                    // Standardmäßig vorausgewählt
  idRequired: boolean;                 // Personalausweis-Verifizierung nötig
  minQuantity: number;                 // Mindestmenge
  maxQuantity: number;                 // Maximalmenge
  minCustomRetail: number;             // Mindest-Eigenpreis (Minor Units)
  maxCustomRetail: number | null;      // Maximal-Eigenpreis (Minor Units) oder null
  paxCount: number;                    // Anzahl verbundener Teilnehmer
  accompaniedBy: string[];             // Erforderliche Begleit-Items (IDs)
  accompaniedByRatio: number | null;   // Verhältnis-Anforderung
  accompaniedByRatioDenominator: number | null;
  notAccompaniedBy: string[];          // Inkompatible Items (IDs)
}
```

---

## API-Erweiterungen

### Availability-Request

```typescript
// Zusätzliche Felder in POST /availability, POST /availability/calendar
// POST /availability/batch, POST /availability/calendar/batch
interface AvailabilityExtrasRequest {
  extras: Array<{
    id: string;       // Extra-UUID oder "extra_<uuid>"
    quantity: number;
    retail?: number;  // Nur bei customRetail=true (Minor Units)
  }>;
}
```

### Booking-Write-Request

```typescript
// POST /bookings, PATCH /bookings/{uuid}
interface BookingExtrasRequest {
  // Booking-Level:
  extraItems: Array<{
    extraId: string;             // UUID oder "extra_<uuid>"
    uuid?: string;               // Optional: spezifische UUID
    resellerReference?: string;  // Händler-Referenz
    retail?: number;             // Nur bei customRetail=true
  }>;
  // Unit-Level (innerhalb unitItems[]):
  unitItems: Array<{
    unitId: string;
    extraItems: Array<{
      extraId: string;
      uuid?: string;
      resellerReference?: string;
    }>;
  }>;
}
```

### Booking-Response

```typescript
// Booking-Level Extra-Items
interface BookingExtraItem {
  id: string;                   // UUID
  uuid: string;                 // UUID der Extra-Instanz
  extraId: string;              // "extra_<uuid>"
  status: "CONFIRMED";
  resellerReference?: string;
  supplierReference?: string;
  retail?: number;              // Nur bei customRetail
}

// Unit-Level Extra-Items (in unitItems[])
interface UnitExtraItem {
  id: string;
  uuid: string;
  extraId: string;
  status: "CONFIRMED";
}
```

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `EXTRAS_QTY_LIMIT` | 400 | Booking-Level-Extra-Menge überschreitet Limit |
| `EXTRAS_UNIT_QTY_LIMIT` | 400 | Unit-Level-Extra-Menge überschreitet Limit |
| `EXTRAS_RETAIL_REQUIRED` | 400 | Custom-Retail-Extra ohne `retail`-Feld |
| `EXTRAS_RETAIL_BELOW_MINIMUM` | 400 | Custom-Retail unter `minCustomRetail` |
| `EXTRAS_RETAIL_ABOVE_MAXIMUM` | 400 | Custom-Retail überschreitet `maxCustomRetail` |

---

## Verhaltensregeln

- Extra-IDs in Responses verwenden `extra_<uuid>`-Format; Requests akzeptieren beide Formate
- Item-basierte Produkte geben leere `extras`-Arrays zurück
- Custom-Retail-Extras: `retail`-Feld **muss** in Availability- und Booking-Requests übergeben werden
- Mit `octo/pricing`: `extraPricingFrom` auf Kalender-Payloads; `extraPricing` auf Check-Payloads
- Purchase-Unit-Items haben immer leere `extraItems`-Arrays

---

## Vollständiges Beispiel

### Request: Product mit Extras abrufen

```bash
curl -X GET "https://api.ventrata.com/octo/products/product_abc123" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/extras, octo/content"
```

### Response (Option mit Extras)

```json
{
  "id": "option_def456",
  "internalName": "standard-tour",
  "extras": [
    {
      "id": "extra_aa11bb22-cc33-dd44-ee55-ff6677889900",
      "internalName": "lunch-package",
      "reference": "LUNCH",
      "title": "Lunchpaket",
      "customRetail": false,
      "customRetailOptions": [],
      "restrictions": {
        "required": false,
        "default": false,
        "idRequired": false,
        "minQuantity": 1,
        "maxQuantity": 10,
        "minCustomRetail": 0,
        "maxCustomRetail": null,
        "paxCount": 1,
        "accompaniedBy": [],
        "accompaniedByRatio": null,
        "accompaniedByRatioDenominator": null,
        "notAccompaniedBy": []
      }
    }
  ]
}
```

### Request: Buchung mit Extra

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/extras" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "availabilityId": "availability_xyz789",
    "units": [{ "id": "unit_adult", "quantity": 2 }],
    "extraItems": [
      {
        "extraId": "extra_aa11bb22-cc33-dd44-ee55-ff6677889900",
        "resellerReference": "LUNCH-001"
      }
    ]
  }'
```

### Response

```json
{
  "uuid": "booking_111222",
  "status": "ON_HOLD",
  "extraItems": [
    {
      "id": "aa11bb22-cc33-dd44-ee55-ff6677889900",
      "uuid": "extra-item-uuid-001",
      "extraId": "extra_aa11bb22-cc33-dd44-ee55-ff6677889900",
      "status": "CONFIRMED",
      "resellerReference": "LUNCH-001",
      "supplierReference": "LCH-2025-001"
    }
  ]
}
```

### Request: Availability mit Custom-Retail-Extra

```bash
curl -X POST https://api.ventrata.com/octo/availability \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/extras, octo/pricing" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "localDateStart": "2025-07-01",
    "localDateEnd": "2025-07-01",
    "units": [{ "id": "unit_adult", "quantity": 1 }],
    "extras": [
      {
        "id": "extra_custom_retail_uuid",
        "quantity": 1,
        "retail": 1500
      }
    ]
  }'
```

---

*Quelle: https://docs.ventrata.com/capabilities/extras*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
