# OCTO — Offers Capability (`octo/offers`)

## Capability-Identifier

```
octo/offers
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/pricing, octo/offers
Content-Type: application/json
```

---

## Abhängigkeiten

| Capability | Pflicht | Beschreibung |
|-----------|---------|--------------|
| `octo/pricing` | **ja** | Preisfelder sind Voraussetzung für Rabattberechnung |
| `octo/cart` | nein | Aktiviert `offerCombinations` auf Orders |
| `octo/gifts` | nein | Aktiviert Offer-Felder auf Gift-Objekten |
| `octo/extras` | nein | Aktiviert Offer-Felder auf Extra-Items |

---

## Überblick

Ermöglicht:
- Anwendung von Promotionscodes auf Buchungen, Gifts und Extras
- Automatische Auswahl des ersten eligiblen öffentlichen Angebots
- Preisvergleiche mit alternativen Angeboten (`offerComparisons`)
- Kombinations-Angebote für mehrere Produkte (`offerCombinations`)

---

## API-Endpunkte

### GET /offers

Gibt alle Supplier-Promotionen sortiert nach Position zurück (paginiert).

```http
GET https://api.ventrata.com/octo/offers
Authorization: Bearer {api_key}
Octo-Capabilities: octo/pricing, octo/offers
```

**Response:** `200 Offer[]`

---

## Schema-Erweiterungen

### Availability-Objekte

Request-Erweiterung (`POST /availability`, `/availability/calendar`):

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `offerCode` | string | nein | Promotionscode; ohne Angabe → erster eligibler public offer |

Response-Erweiterung:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `offerCode` | string | Angewendeter Promotionscode |
| `offerTitle` | string | Anzeigename des Angebots |
| `offerIsCombination` | boolean | Handelt es sich um einen Kombinationscode |
| `offer` | Offer | Aktuell angewendetes Angebot |
| `offers` | Offer[] | Alle eligiblen Angebote |
| `offerComparisons` | OfferComparison[] | Preisvergleiche mit anderen Angeboten |

### Booking-Objekte

Request (`POST /bookings`, `PATCH /bookings/{uuid}`, `POST /bookings/{uuid}/confirm`):

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `offerCode` | string | nein | Promotionscode |

Response:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `offerCode` | string | Angewendeter Code |
| `offerTitle` | string | Angebotsname |
| `offerIsCombination` | boolean | Kombinationscode-Flag |
| `offer` | Offer | Angebotsdetails |
| `offers` | Offer[] | Alle anwendbaren Angebote |
| `offerComparisons` | OfferComparison[] | Nur bei aktiven, standalone, non-combination Buchungen |

> `offerCode` kann auch in Order-Payloads unter `bookings[].offerCode` übergeben werden.

### BookingUnitItem

Gleiche Felder wie Booking-Objekt.

### Gift-Objekte (benötigt `octo/gifts`)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `offerCode` | string | Promotionscode |
| `offerTitle` | string | Angebotsname |
| `offerIsCombination` | boolean | Immer `false` bei Gifts |
| `offer` | Offer | Angebotsdetails |
| `offers` | Offer[] | Eligible Angebote |
| `offerComparisons` | OfferComparison[] | Immer `[]` |

Write-Endpunkte: `POST /gifts`, `PATCH /gifts/{uuid}`, `POST /gifts/{uuid}/confirm`

### Extra-Items (benötigt `octo/extras`)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `offerCode` | string | Promotionscode |
| `offerTitle` | string | Angebotsname |
| `offerIsCombination` | boolean | Immer `false` |
| `offer` | Offer | Angebotsdetails |
| `offers` | Offer[] | Eligible Angebote |
| `offerComparisons` | OfferComparison[] | Immer `[]` |

Vorhanden auf `booking.extraItems[]` und `booking.unitItems[].extraItems[]`

### Order-Objekte (benötigt `octo/cart`)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `offerCombinations` | Combination[] | Produkt-Kombinations-Angebote |

---

## Vollständige Schemata

### Offer-Objekt

```typescript
interface Offer {
  id: string;                      // UUID
  tags: string[];
  title: string;
  label: string;
  code: string;                    // Promotionscode
  internalName: string;
  shortDescription: string;
  description: string;
  publicOfferId: string;
  netDiscount: "FULL" | "PARTIAL";
  usable: boolean;
  unusableReason: string | null;
  status: "CONFIRMED" | string;
  offerDiscount: {
    retail: number;                // Minor Units
    net: number;                   // Minor Units
    includedTaxes: Array<{
      name: string;
      shortDescription: string;
      retail: number;
      net: number;
    }>;
  };
  membershipBenefit: {
    id: string;
    title: string;
    description: string;
  } | null;
  restrictions: {
    minUnits: number;
    maxUnits: number;
    minTotal: number;
    maxTotal: number;
    unitIds: string[];
  };
}
```

### OfferComparison-Objekt

```typescript
interface OfferComparison {
  offerCode: string;
  offerTitle: string;
  pricing: {
    original: number;
    retail: number;
    net: number;
    currency: string;
    currencyPrecision: number;
    includedTaxes: Tax[];
    offerDiscount: {
      retail: number;
      net: number;
      includedTaxes: Tax[];
    };
  };
  offer: {
    id: string;
    title: string;
    code: string;
  };
}
```

### Combination-Objekt (für Orders)

```typescript
interface OfferCombination {
  productId: string;
  optionId: string;
  units: Array<{
    unitId: string;
    quantity: number;
  }>;
  offerCode: string;  // Format: "combination_<uuid>"
}
```

### Pricing-Extension (offerDiscount)

Auf allen Pricing-Serialisierern vorhanden (availability.pricing, unitPricing, bookingPreis etc.):

```typescript
interface PricingWithOffer extends Pricing {
  offerDiscount: {
    retail: number;
    net: number;
    includedTaxes: Tax[];
  };
}
```

---

## Produkterweiterung bei Kombinationscodes

Wenn `offerCode` ein Kombinationscode ist (`combination_<uuid>`), werden bei Produktrouten
auch die Zielprodukte der Kombination einbezogen:
- `GET /products` → erweiterte Produktliste
- `GET /products/{productId}` → erweitertes Produktobjekt

---

## Verhaltensregeln

1. **Auto-Selektion**: Ohne `offerCode` auf Availability-Routen → erster eligibler public offer
   wird automatisch auf neue Buchungen/Gifts angewendet
2. **Vergleiche**: `offerComparisons` nur bei persistierten, aktiven, standalone, non-combination-Buchungen
3. **Kombinationen**: Durch Anlegen/Aktualisieren einer Buchung mit dem zurückgegebenen `offerCode`
   plus passenden `productId`/`optionId` aus `offerCombinations`
4. **Kontextuelle Usability**: Availability-Ebene vs. Booking/Gift/Extra-Ebene unterscheiden

---

## Vollständiges Beispiel

### Request: Availability mit Promotionscode

```bash
curl -X POST https://api.ventrata.com/octo/availability \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/pricing, octo/offers" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "localDateStart": "2025-07-01",
    "localDateEnd": "2025-07-01",
    "units": [{ "id": "unit_adult", "quantity": 2 }],
    "offerCode": "SUMMER20"
  }'
```

### Response

```json
[
  {
    "id": "availability_xyz789",
    "localDateTimeStart": "2025-07-01T10:00:00+02:00",
    "available": true,
    "status": "AVAILABLE",
    "offerCode": "SUMMER20",
    "offerTitle": "Sommer-Rabatt 20%",
    "offerIsCombination": false,
    "offer": {
      "id": "offer_111",
      "title": "Sommer-Rabatt 20%",
      "code": "SUMMER20",
      "netDiscount": "PARTIAL",
      "usable": true,
      "unusableReason": null,
      "offerDiscount": {
        "retail": 960,
        "net": 807,
        "includedTaxes": []
      },
      "restrictions": {
        "minUnits": 1,
        "maxUnits": 10,
        "minTotal": 0,
        "maxTotal": 100000,
        "unitIds": []
      }
    },
    "offers": [],
    "offerComparisons": [],
    "pricing": {
      "original": 5000,
      "retail": 3840,
      "net": 3226,
      "currency": "EUR",
      "currencyPrecision": 2,
      "includedTaxes": [],
      "offerDiscount": {
        "retail": 960,
        "net": 807,
        "includedTaxes": []
      }
    }
  }
]
```

### Request: Buchung mit Promotionscode bestätigen

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/pricing, octo/offers" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "availabilityId": "availability_xyz789",
    "units": [{ "id": "unit_adult", "quantity": 2 }],
    "offerCode": "SUMMER20"
  }'
```

---

*Quelle: https://docs.ventrata.com/capabilities/offers*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
