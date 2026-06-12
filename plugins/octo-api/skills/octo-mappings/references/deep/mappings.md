# OCTO — Mappings Capability (`octo/mappings`)

## Capability-Identifier

```
octo/mappings
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/mappings
Content-Type: application/json
```

---

## Überblick

Ermöglicht das Einreichen eines Mapping-Sheets von Produkten, die bei Suppliern
zugeordnet werden müssen. Supplier wählen die entsprechenden Ventrata-Produkte
über eine benutzerfreundliche Oberfläche aus. Wird abgeschlossen, sendet Ventrata
eine Webhook-Benachrichtigung.

---

## API-Endpunkte

### PUT /mappings

Produkt-Mappings anlegen oder aktualisieren.

```http
PUT https://api.ventrata.com/octo/mappings
Authorization: Bearer {api_key}
Octo-Capabilities: octo/mappings
Content-Type: application/json
```

**Request-Body:** `MappingRow[]` (JSON-Array)

**Pflichtfelder je Zeile:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `resellerReference` | string | **ja** | Upsert-Schlüssel; eindeutig je Mapping |
| `resellerProduct` | string | nein | Händler-Produktbezeichnung |
| `webhookUrl` | string (URL) | nein | Webhook-Endpoint für Supplier-Rückmeldung |
| `validityDays` | integer | nein | Gültigkeitsdauer des Mappings in Tagen |
| `optionRequired` | boolean | nein | Option-Auswahl obligatorisch |
| `unitRequired` | boolean | nein | Unit-Auswahl obligatorisch |

**Verhalten:**
- Items werden per `resellerReference` upsertet
- Nicht enthaltene Items werden **entfernt** (Full-Sync-Modell)
- Trigger: Webhook-Benachrichtigung an Supplier bei unvollständigen Mappings

**Response:** `200 MappingRow[]` (vollständige Mapping-Liste)

---

### GET /mappings

Aktuelle Mappings abrufen.

```http
GET https://api.ventrata.com/octo/mappings
Authorization: Bearer {api_key}
Octo-Capabilities: octo/mappings
```

**Query-Parameter:**

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `productId` | string (UUID) | Einzelnes Produkt filtern (hat Vorrang vor `productIds[]`) |
| `productIds[]` | string[] | Mehrere Produkte filtern; Syntax: `productIds[]=id1&productIds[]=id2` |
| `optionId` | string (UUID) | Einzelne Option filtern (hat Vorrang vor `optionIds[]`) |
| `optionIds[]` | string[] | Mehrere Optionen filtern |

> `optionId=DEFAULT` filtert auf noch nicht gemappte Optionen.

**Response:** `200 MappingRow[]`

---

## MappingRow-Schema (vollständig)

```typescript
interface MappingRow {
  // Request-Felder
  resellerReference: string;   // REQUIRED: eindeutiger Upsert-Schlüssel
  resellerProduct?: string;    // Händler-Produktbezeichnung
  webhookUrl?: string;         // URL für Supplier-Benachrichtigung
  validityDays?: number;       // Gültigkeitsdauer in Tagen
  optionRequired?: boolean;    // Option-Auswahl obligatorisch
  unitRequired?: boolean;      // Unit-Auswahl obligatorisch

  // Response-Felder (nach Supplier-Zuordnung)
  productId: string | null;    // UUID des gemappten Produkts
  optionId: string | null;     // UUID der gemappten Option (null wenn optionRequired=false)
  unitId: string | null;       // ID der gemappten Unit (null wenn unitRequired=false)
  resellerStatus: "CONFIRMED"; // Mapping-Bestätigungsstatus
}
```

---

## Schema-Erweiterungen an anderen Objekten

### Availability-Objekt

```typescript
interface AvailabilityMappings {
  mappings: Array<{
    resellerReference: string;
    optionId: string;
    productId: string;
    resellerStatus: "CONFIRMED";
  }>;
}
```

### AvailabilityBatchRow-Objekt

Identische Struktur wie Availability.

### Booking-Objekt

```typescript
interface BookingMappings {
  mappings: Array<{
    resellerReference: string;
    resellerProduct: string;
    productId: string;
    optionId: string | null;
    unitId: string | null;
    optionRequired: boolean;
    unitRequired: boolean;
    validityDays: number;
    webhookUrl: string;
    resellerStatus: "CONFIRMED";
  }>;
}
```

### PackageAvailability-Objekt

Gleiche Struktur wie Availability.

---

## Webhook-Verhalten

Wenn ein Supplier Mappings abschließt, sendet Ventrata einen POST an die konfigurierte
`webhookUrl`:

- Response muss `2xx`-Status zurückgeben
- Bei Nicht-`2xx`: automatische Wiederholung (Retries) bis `2xx` empfangen
- Webhook-Body enthält aufgelöste `productId`, `optionId` und `unitId`

```json
{
  "resellerReference": "mein-produkt-001",
  "productId": "resolved-product-uuid",
  "optionId": "resolved-option-uuid",
  "unitId": "resolved-unit-uuid"
}
```

---

## Full-Sync-Modell

```
1. Alle aktuellen Mappings bei PUT übergeben
2. Wenn ein Mapping entfernt werden soll → aus der Liste weglassen
3. Bei Produktänderungen → PUT mit vollständiger aktualisierter Liste wiederholen
```

---

## Vollständiges Beispiel

### Request: Mapping-Sheet erstellen

```bash
curl -X PUT https://api.ventrata.com/octo/mappings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/mappings" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "resellerReference": "goldenTours-bt-berlin-2025",
      "resellerProduct": "Berlin City Tour Standard",
      "webhookUrl": "https://api.goldentours.com/webhooks/octo-mapping",
      "validityDays": 365,
      "optionRequired": true,
      "unitRequired": true
    },
    {
      "resellerReference": "goldenTours-bt-berlin-premium",
      "resellerProduct": "Berlin City Tour Premium",
      "webhookUrl": "https://api.goldentours.com/webhooks/octo-mapping",
      "validityDays": 365,
      "optionRequired": true,
      "unitRequired": false
    }
  ]'
```

### Response (vor Supplier-Zuordnung)

```json
[
  {
    "resellerReference": "goldenTours-bt-berlin-2025",
    "resellerProduct": "Berlin City Tour Standard",
    "webhookUrl": "https://api.goldentours.com/webhooks/octo-mapping",
    "validityDays": 365,
    "optionRequired": true,
    "unitRequired": true,
    "productId": null,
    "optionId": null,
    "unitId": null,
    "resellerStatus": "CONFIRMED"
  },
  {
    "resellerReference": "goldenTours-bt-berlin-premium",
    "resellerProduct": "Berlin City Tour Premium",
    "webhookUrl": "https://api.goldentours.com/webhooks/octo-mapping",
    "validityDays": 365,
    "optionRequired": true,
    "unitRequired": false,
    "productId": null,
    "optionId": null,
    "unitId": null,
    "resellerStatus": "CONFIRMED"
  }
]
```

### Response (nach Supplier-Zuordnung)

```json
[
  {
    "resellerReference": "goldenTours-bt-berlin-2025",
    "resellerProduct": "Berlin City Tour Standard",
    "productId": "product_abc123",
    "optionId": "option_def456",
    "unitId": "unit_adult",
    "optionRequired": true,
    "unitRequired": true,
    "validityDays": 365,
    "webhookUrl": "https://api.goldentours.com/webhooks/octo-mapping",
    "resellerStatus": "CONFIRMED"
  }
]
```

### Request: Mappings nach Produkt-ID abrufen

```bash
curl -X GET "https://api.ventrata.com/octo/mappings?productId=product_abc123" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/mappings"
```

### Request: Mehrere Produkte abfragen

```bash
curl -X GET "https://api.ventrata.com/octo/mappings?productIds[]=product_abc123&productIds[]=product_def456" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/mappings"
```

### Request: Noch nicht gemappte Optionen filtern

```bash
curl -X GET "https://api.ventrata.com/octo/mappings?optionId=DEFAULT" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/mappings"
```

### Webhook-Empfang (Beispiel-Implementierung)

```bash
# Webhook-Endpoint muss 2xx zurückgeben
POST https://api.goldentours.com/webhooks/octo-mapping
Content-Type: application/json

{
  "resellerReference": "goldenTours-bt-berlin-2025",
  "productId": "product_abc123",
  "optionId": "option_def456",
  "unitId": "unit_adult"
}
```

---

*Quelle: https://docs.ventrata.com/capabilities/mappings*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
