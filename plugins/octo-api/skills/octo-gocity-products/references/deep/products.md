# Go City Trade API V2 — Products (vollständige Referenz)

## Endpunkte

### GET /octo/products

Gibt die Liste aller Produkte (Pässe) des Suppliers zurück. Preise sind standardmäßig inkludiert.

```http
GET https://api.gocity.com/octo/products
Authorization: Bearer {your_token}
```

**Query-Parameter:**

| Parameter | Typ | Pflicht | Standard | Beschreibung |
|-----------|-----|---------|---------|--------------|
| `priceDistributionModel` | string | Nein | `PUBLIC` | Preismodell: `PUBLIC` oder `RESTRICTED` |
| `_capabilities` | string | Nein | — | Alternative zu Octo-Capabilities Header, z.B. `octo/pricing` |

**Request-Header (optional):**
```http
Octo-Capabilities: octo/pricing
```

**Response:** `200 Array<OctoProduct>`

**Beispiel-Request:**
```http
GET https://api.gocity.com/octo/products?priceDistributionModel=PUBLIC
Authorization: Bearer {your_token}
Octo-Capabilities: octo/pricing
```

---

### GET /octo/products/{id}

Gibt ein einzelnes Produkt für die angegebene ID zurück. Preise sind inkludiert.

```http
GET https://api.gocity.com/octo/products/{id}
Authorization: Bearer {your_token}
```

**Path-Parameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `id` | string (uuid) | Ja | Produkt-ID (UUID-Format) |

**Query-Parameter:**

| Parameter | Typ | Pflicht | Standard | Beschreibung |
|-----------|-----|---------|---------|--------------|
| `priceDistributionModel` | string | Nein | `PUBLIC` | Preismodell: `PUBLIC` oder `RESTRICTED` |

**Response:** `200 OctoProduct`

---

## OctoProduct-Schema (vollständig)

```typescript
type OctoProduct = {
  // --- Kern-Felder (immer vorhanden) ---
  id: string;                    // UUID — Produkt-ID, eindeutig im Go-City-Scope
                                 // ACHTUNG: kann sich bei Entwicklungsänderungen ändern
  internalName: string;          // Name wie Go City das Produkt intern nennt
                                 // Beispiel: "Chicago Go City All-Inclusive Standard"
  reference: string;             // Go City Legacy-Code/SKU
                                 // Beispiel: "Chi Go All-Incl St"
  locale: string;                // BCP 47 RFC 5646 Sprach-Tag
                                 // Enum: "en" | "es" | "da" | "de" | "fr" | "it" |
                                 //        "ja" | "ko" | "pt" | "sv" | "zh-hans" | "zh-hant"
                                 // Beispiel: "en-GB"
  timeZone: string;              // IANA Zeitzone
                                 // Beispiel: "Europe/London"
  allowFreesale: boolean;        // Immer true — Buchung ohne Availability möglich
  instantConfirmation: boolean;  // Immer true — sofortige Bestätigung
  instantDelivery: boolean;      // Immer true — sofortige Ticket-Lieferung
  availabilityRequired: boolean; // Immer true — availabilityId muss dennoch angegeben werden
                                 // (Abrechnungsgründe: Go City rechnet nach Reisedatum ab)

  // --- Destination/Produkt-Klassifikation ---
  destinationId: string;         // UUID der Destination
  destinationName: string;       // Name der Destination, z.B. "Chicago"
  brand: string;                 // Marke: "Go City" | "Great" | "Big Bus" | "Omnia"
  durationType: string;          // Art der Dauer: "CHOICE" | "DAYS" (o.ä.)
  variant: string;               // Produktvariante, z.B. "Default" | "Standard" | "Plus"

  // --- Availability-Typ ---
  availabilityType: "OPENING_HOURS"; // Immer OPENING_HOURS — Kunden können jederzeit
                                     // Attraktionen besuchen, wenn geöffnet

  // --- Lieferung & Einlösung ---
  deliveryFormats: Array<"PDF_URL" | "HTML_URL">;
                                 // PDF_URL: URL zu PDF mit Ticket-Details
                                 // HTML_URL: URL zu HTML-Seite mit Ticket-Details
  deliveryMethods: Array<"TICKET" | "VOUCHER">;
                                 // TICKET: Einzelticket pro Person
                                 // VOUCHER: Ein Ticket für die gesamte Buchung
  redemptionMethod: "DIGITAL" | "PRINT";
                                 // DIGITAL: digitales/mobiles Ticket reicht
                                 // PRINT: Ticket muss gedruckt werden

  // --- Optionen ---
  options: OctoOption[];         // Mind. eine Option (Pflicht). Jede Option ist
                                 // eine Dauer/Typ-Kombination

  // --- Pricing-Felder (nur mit Octo-Capabilities: octo/pricing) ---
  defaultCurrency?: string;      // Standard-Währung, z.B. "USD"
  availableCurrencies?: string[]; // Alle verfügbaren Währungen
  pricingPer?: "UNIT";           // Preis pro UNIT (immer UNIT bei Go City)
};
```

---

## OctoOption-Schema (vollständig)

```typescript
type OctoOption = {
  // --- Kern-Felder ---
  id: string;                    // UUID — eindeutig im gesamten Go-City-Scope
                                 // Beispiel: "8a435677-1413-4012-8f5e-18eb15f54985"
                                 // ACHTUNG: kann sich ändern — regelmäßig prüfen
  internalName: string;          // Interner Name
                                 // Beispiel: "Chicago Go City 1-Day Standard Pass"
  reference: string;             // Optionaler Code
                                 // Beispiel: "Chi Go 1D Df Ps"
  default: boolean;              // true = erste Auswahl in Kunden-Interfaces

  // --- Dauer ---
  durationValue: number;         // Numerischer Dauerwert (Anzahl der durationType-Einheiten)
  optionType: string;            // Typ der Option, z.B. "PASS" | "EXTENSION"

  // --- Availability-Startzeiten ---
  availabilityLocalStartTimes: string[];
                                 // Alle möglichen Startzeiten (z.B. ["00:00"] für ganztägig)

  // --- Stornierungsrichtlinie ---
  cancellationCutoff: string;    // Menschenlesbare Beschreibung, z.B. "-365 days"
                                 // Negativer Wert = nach Bestätigung (nicht vor Reise!)
  cancellationCutoffAmount: number; // Numerischer Cutoff-Wert, z.B. -365
  cancellationCutoffUnit: "hour" | "minute" | "day"; // Zeiteinheit

  // --- Kontaktfelder ---
  requiredContactFields: Array<"firstName" | "lastName" | "emailAddress" |
                                "phoneNumber" | "country" | "notes" | "locales">;
                                 // Pflichtfelder für Hauptbucher (Lead Traveller)
                                 // Hinweis: gelten NUR für das Buchungs-Objekt, nicht
                                 // für jedes einzelne Ticket

  // --- Einschränkungen ---
  restrictions: OctoOptionRestrictions;

  // --- Units ---
  units: OctoUnit[];             // Liste der verfügbaren Ticket-Typen

  // --- Pricing-Felder (nur mit octo/pricing) ---
  pricingFrom?: OctoPricing[] | null; // Ab-Preise (mehrere Währungen)
  pricing?: OctoPricing[] | null;     // Preise (mehrere Währungen)
};

type OctoOptionRestrictions = {
  minUnits: number | null;  // Min. Tickets pro Buchung (null = kein Minimum = 0)
  maxUnits: number | null;  // Max. Tickets pro Buchung (null = unbegrenzt)
};
```

---

## OctoUnit-Schema (vollständig)

```typescript
type OctoUnit = {
  // --- Kern-Felder ---
  id: string;                    // UUID — eindeutig im Go-City-Scope
  internalName: string;          // Interner Name (nicht für Kunden)
                                 // Beispiel: "Chicago Go City 1-Day Standard Pass Adult"
  reference: string;             // Interne Referenz
                                 // Beispiel: "Chi Go 1D St Ps Ad"
  type: "ADULT" | "CHILD";      // Basistyp (Go City: nur ADULT und CHILD)

  // --- Kontaktfelder ---
  requiredContactFields: Array<"firstName" | "lastName" | "emailAddress" |
                                "phoneNumber" | "country" | "notes" | "locales">;

  // --- Einschränkungen ---
  restrictions: OctoUnitRestrictions;

  // --- Pricing-Felder (nur mit octo/pricing) ---
  pricingFrom?: OctoPricing[];  // Ab-Preise pro Währung (Array weil mehrere Währungen)
  pricing?: OctoPricing[];      // Preise pro Währung
};

type OctoUnitRestrictions = {
  minAge: number;               // Mindestalter
  maxAge: number;               // Maximalalter
  idRequired: boolean;          // Ausweis erforderlich
  minQuantity: number;          // Min. Anzahl pro Buchung
  maxQuantity: number;          // Max. Anzahl pro Buchung
  paxCount: number;             // Personen pro Unit-Ticket
  accompaniedBy: string[];      // Unit-IDs die mitgebucht werden müssen
};
```

---

## OctoPricing-Schema (vollständig)

Verfügbar wenn `Octo-Capabilities: octo/pricing` gesetzt ist.

```typescript
type OctoPricing = {
  original: number;          // Originalpreis (Strike-Through). Gleich oder höher als retail.
                             // Beispiel: 0 (kein Strike-Through)
  retail: number;            // Verkaufspreis an Kunden (in integer Cents/Kleinsteinheit)
                             // Beispiel: 18400 = 184,00 USD
  net: number;               // Großhandelspreis — was Go City dem Partner berechnet
                             // Beispiel: 17480 = 174,80 USD
  currency: string;          // Währungscode, z.B. "USD"
  currencyPrecision: number; // Dezimalstellen für Umrechnung
                             // USD: 2 → divide by 100; JPY: 0 → divide by 1
};

// Preis-Umrechnung:
// tatsächlicherPreis = price / Math.pow(10, currencyPrecision)
// Beispiel USD: 18400 / 10^2 = 184.00 USD
// Beispiel JPY: 500 / 10^0 = 500 JPY
```

> **Wichtig:** Pricing-Felder in Optionen und Units sind Arrays, weil ein Produkt in mehreren Währungen verfügbar sein kann. Jedes Element repräsentiert eine Währung.

---

## Beispiel-Response: GET /octo/products (Auszug)

```json
[
  {
    "id": "a1b2c3d4-0000-0000-0000-000000000001",
    "internalName": "Chicago Go City All-Inclusive Standard",
    "reference": "Chi Go All-Incl St",
    "locale": "en",
    "timeZone": "America/Chicago",
    "allowFreesale": true,
    "instantConfirmation": true,
    "instantDelivery": true,
    "availabilityRequired": true,
    "destinationId": "d1d2d3d4-0000-0000-0000-000000000001",
    "destinationName": "Chicago",
    "brand": "Go City",
    "durationType": "DAYS",
    "variant": "Standard",
    "availabilityType": "OPENING_HOURS",
    "deliveryFormats": ["PDF_URL", "HTML_URL"],
    "deliveryMethods": ["TICKET", "VOUCHER"],
    "redemptionMethod": "DIGITAL",
    "defaultCurrency": "USD",
    "availableCurrencies": ["USD"],
    "pricingPer": "UNIT",
    "options": [
      {
        "id": "8a435677-1413-4012-8f5e-18eb15f54985",
        "internalName": "Chicago Go City 1-Day Standard Pass",
        "reference": "Chi Go 1D Df Ps",
        "default": true,
        "durationValue": 1,
        "optionType": "PASS",
        "availabilityLocalStartTimes": ["00:00"],
        "cancellationCutoff": "-365 days",
        "cancellationCutoffAmount": -365,
        "cancellationCutoffUnit": "day",
        "requiredContactFields": ["emailAddress", "locales"],
        "restrictions": {
          "minUnits": null,
          "maxUnits": null
        },
        "units": [
          {
            "id": "u1u2u3u4-0000-0000-0000-000000000001",
            "internalName": "Chicago Go City 1-Day Standard Pass Adult",
            "reference": "Chi Go 1D St Ps Ad",
            "type": "ADULT",
            "requiredContactFields": [],
            "restrictions": {
              "minAge": 13,
              "maxAge": 99,
              "idRequired": false,
              "minQuantity": 0,
              "maxQuantity": null,
              "paxCount": 1,
              "accompaniedBy": []
            },
            "pricingFrom": [
              {
                "original": 0,
                "retail": 18400,
                "net": 17480,
                "currency": "USD",
                "currencyPrecision": 2
              }
            ]
          },
          {
            "id": "u5u6u7u8-0000-0000-0000-000000000002",
            "internalName": "Chicago Go City 1-Day Standard Pass Child",
            "reference": "Chi Go 1D St Ps Ch",
            "type": "CHILD",
            "requiredContactFields": [],
            "restrictions": {
              "minAge": 3,
              "maxAge": 12,
              "idRequired": false,
              "minQuantity": 0,
              "maxQuantity": null,
              "paxCount": 1,
              "accompaniedBy": []
            },
            "pricingFrom": [
              {
                "original": 0,
                "retail": 12400,
                "net": 11780,
                "currency": "USD",
                "currencyPrecision": 2
              }
            ]
          }
        ],
        "pricingFrom": [
          {
            "original": 0,
            "retail": 18400,
            "net": 17480,
            "currency": "USD",
            "currencyPrecision": 2
          }
        ]
      }
    ]
  }
]
```

---

## Wichtige Besonderheiten

1. **ID-Stabilität:** Produkt- und Option-IDs können sich durch Weiterentwicklung ändern. Regelmäßig mit aktueller Implementierung abgleichen.
2. **Nur ADULT und CHILD:** Go City hat (laut Spec) nur `ADULT` und `CHILD` als Unit-Typen (kein YOUTH, SENIOR, etc. wie bei Ventrata).
3. **Negativer cancellationCutoffAmount:** Ein Wert von `-365` bedeutet, dass die Stornierung bis 365 Tage NACH Bestätigung möglich ist — nicht vor dem Reisedatum.
4. **pricingFrom vs. pricing:** `pricingFrom` zeigt Ab-Preise, `pricing` zeigt konkrete Preise (wenn Units in der Anfrage angegeben wurden).
5. **priceDistributionModel:** Dieser Go-City-spezifische Parameter hat keinen OCTO-Standard-Äquivalent bei Ventrata.

---

**Quellen:**
- `/tmp/gocity-openapi.json` — Go City Trade API V2 OpenAPI 3.1 Spec (autoritativ)
- `/tmp/gocity.html` — Gerenderte Redoc-Dokumentation
