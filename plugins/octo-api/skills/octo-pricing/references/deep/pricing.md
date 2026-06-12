# OCTO — Pricing Capability (`octo/pricing`)

## Capability-Identifier

```
octo/pricing
```

Muss im HTTP-Header `Octo-Capabilities` übergeben werden, damit die zusätzlichen Preisfelder
in allen Antworten erscheinen.

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/pricing
Content-Type: application/json
```

---

## Überblick

Ermöglicht dynamische Preisgestaltung: Der Preis eines Produkts kann pro Tag und
pro Startzeit unterschiedlich sein. Alle Preise sind in **Minor Units** (Cents)
angegeben (z. B. `1000` = 10,00 EUR bei `currencyPrecision: 2`).

- Felder mit dem Suffix `From` → **Indikative** Preise (Kalender-Ansicht)
- Felder ohne Suffix → **Finale** bestätigte Preise

---

## Erweiterungen am Product-Schema

Endpunkte: `GET /products`, `GET /products/{productId}`

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `defaultCurrency` | string | — | ISO-4217-Standardwährung des Produkts |
| `availableCurrencies` | string[] | — | Liste aller unterstützten Währungen |
| `includeTax` | boolean | — | `true` wenn Preise inkl. MwSt. |
| `hidePricingFrom` | boolean | — | Indikative „Ab-Preise" aus der UI ausblenden |
| `pricingPer` | enum | — | `"UNIT"` oder `"BOOKING"` — Preismodell |
| `pricingMultiplier` | number | — | Multiplikator für Preisberechnungen |

---

## Erweiterungen am Availability-Schema

### POST /availability — Request

Zusätzliches Request-Feld:

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `currency` | string | nein | ISO-4217-Code oder `"default"` |

### POST /availability — Response (Availability-Objekt)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `pricing` | Pricing | Finaler Gesamtpreis |
| `unitPricing` | UnitPricing[] | Finaler Preis je Unit |
| `extraPricing` | ExtraPricing[] | Finaler Preis je Extra (nur mit `octo/extras`) |

### POST /availability/calendar — Response (AvailabilityCalendar-Objekt)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `pricingFrom` | Pricing | Indikativer Gesamtpreis |
| `unitPricingFrom` | UnitPricing[] | Indikativer Preis je Unit |
| `extraPricingFrom` | ExtraPricing[] | Indikativer Preis je Extra |

---

## Erweiterungen am Booking-Schema

Endpunkte: `POST /bookings`, `PATCH /bookings/{uuid}`, `POST /bookings/{uuid}/confirm`

### Request

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `currency` | string | nein | ISO-4217 oder `"default"` |

### Response

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `pricing` | Pricing | Finaler Buchungspreis |

> Wenn der Lieferant Price-Matching erzwingt: `PRICING_MATCH_REQUIRED` Error bei Nichtübereinstimmung.

---

## Pricing-Objekt (vollständiges Schema)

```typescript
interface Pricing {
  original: number;          // Originalpreis in Minor Units
  retail: number;            // Verkaufspreis in Minor Units
  net: number;               // Nettopreis in Minor Units
  currency: string;          // ISO-4217-Code, z.B. "EUR"
  currencyPrecision: number; // Dezimalstellen, z.B. 2 für EUR
  includedTaxes: Tax[];      // Aufschlüsselung enthaltener Steuern
}

interface Tax {
  name: string;              // Steuerbezeichnung, z.B. "VAT"
  shortDescription: string;  // Kurzbeschreibung
  original: number;          // Steueranteil am Originalpreis
  retail: number;            // Steueranteil am Verkaufspreis
  net: number;               // Nettosteueranteil
}
```

## UnitPricing-Objekt

```typescript
interface UnitPricing extends Pricing {
  unitId: string;    // Referenz zur Unit
  unitType: string;  // Unit-Typ (z.B. "ADULT")
}
```

## ExtraPricing-Objekt

```typescript
interface ExtraPricing extends Pricing {
  extraId: string;   // Referenz zum Extra
}
```

---

## Vollständiges Beispiel

### Request: Availability mit Preisabfrage

```bash
curl -X POST https://api.ventrata.com/octo/availability \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/pricing" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "localDateStart": "2025-07-01",
    "localDateEnd": "2025-07-01",
    "units": [
      { "id": "unit_adult", "quantity": 2 }
    ],
    "currency": "EUR"
  }'
```

### Response

```json
[
  {
    "id": "availability_xyz789",
    "localDateTimeStart": "2025-07-01T10:00:00+02:00",
    "localDateTimeEnd": "2025-07-01T12:00:00+02:00",
    "allDay": false,
    "available": true,
    "status": "AVAILABLE",
    "vacancies": 12,
    "capacity": 20,
    "pricing": {
      "original": 5000,
      "retail": 4800,
      "net": 4032,
      "currency": "EUR",
      "currencyPrecision": 2,
      "includedTaxes": [
        {
          "name": "VAT",
          "shortDescription": "19% MwSt.",
          "original": 798,
          "retail": 766,
          "net": 644
        }
      ]
    },
    "unitPricing": [
      {
        "unitId": "unit_adult",
        "unitType": "ADULT",
        "original": 2500,
        "retail": 2400,
        "net": 2016,
        "currency": "EUR",
        "currencyPrecision": 2,
        "includedTaxes": []
      }
    ]
  }
]
```

### Request: Buchung anlegen

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/pricing" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "availabilityId": "availability_xyz789",
    "units": [
      { "id": "unit_adult", "quantity": 2 }
    ],
    "currency": "EUR"
  }'
```

### Response (Buchung mit Preis)

```json
{
  "uuid": "booking_111222",
  "status": "ON_HOLD",
  "pricing": {
    "original": 5000,
    "retail": 4800,
    "net": 4032,
    "currency": "EUR",
    "currencyPrecision": 2,
    "includedTaxes": [
      {
        "name": "VAT",
        "shortDescription": "19% MwSt.",
        "original": 798,
        "retail": 766,
        "net": 644
      }
    ]
  }
}
```

---

## Fehler

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `PRICING_MATCH_REQUIRED` | 400 | Preisabgleich erzwungen, übergebener Preis weicht ab |

---

## TypeScript-Typen (octo-types, MIT)

```typescript
// Aus @octotravel/octo-types (github.com/octotravel/octo-types)
interface Pricing {
  original: number;
  retail: number;
  net: number;
  currency: string;
  currencyPrecision: number;
  includedTaxes: Array<{
    name: string;
    shortDescription: string;
    original: number;
    retail: number;
    net: number;
  }>;
}

type PricingPer = "UNIT" | "BOOKING";

// CapabilityId enum enthält: OCTO_PRICING = "octo/pricing"
```

---

*Quelle: https://docs.ventrata.com/capabilities/pricing*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
