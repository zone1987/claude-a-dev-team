# OCTO — Redemption Capability (`octo/redemption`)

## Capability-Identifier

```
octo/redemption
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/redemption
Content-Type: application/json
```

> Ausnahme: `POST /redemption/credentials` ist **unauthentifiziert**.

---

## Überblick

Ermöglicht Supplier/Operator-Verbindungen, Buchungen und Tickets nachzuschlagen,
einzulösen, zurückzusetzen und als No-Show zu markieren — per Einlösecode, E-Mail
oder Mobilnummer.

---

## API-Endpunkte

### GET /redemption/lookup

Buchungen/Tickets anhand von Code, E-Mail oder Mobilnummer suchen.

```http
GET https://api.ventrata.com/octo/redemption/lookup
Authorization: Bearer {api_key}
Octo-Capabilities: octo/redemption
```

**Query-Parameter:** (mindestens einer erforderlich)

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `reference` | string | Buchungsreferenz oder Einlösecode |
| `email` | string | E-Mail-Adresse des Gastes |
| `mobile` | string | Mobilnummer des Gastes |

**Response:** `200 RedemptionObject[]`

> Bei Paketprodukten mit einlösbaren Includes werden mehrere Ergebnisse zurückgegeben.

---

### POST /redemption/redeem

Einen oder mehrere Einlösecodes einlösen.

```http
POST https://api.ventrata.com/octo/redemption/redeem
Authorization: Bearer {api_key}
Octo-Capabilities: octo/redemption
Content-Type: application/json
```

**Request-Body:**

```typescript
{
  redemptionCode: string | string[];
}
```

**Response:**
- `string` → Einzelnes `RedemptionObject`
- `string[]` → `RedemptionObject[]`

**Fehler:** `400 BAD_REQUEST` mit `redemptionCode` und `redemptionErrorCode` bei Ablehnung.

---

### DELETE /redemption/redeem

Einlösung rückgängig machen (Unredeem).

```http
DELETE https://api.ventrata.com/octo/redemption/redeem
Authorization: Bearer {api_key}
Octo-Capabilities: octo/redemption
Content-Type: application/json
```

**Request-Body:**

```typescript
{
  redemptionCode: string | string[];
}
```

**Response:** Gleiche Struktur wie POST.

---

### POST /redemption/noshow

Einen oder mehrere Codes als No-Show markieren.

```http
POST https://api.ventrata.com/octo/redemption/noshow
Authorization: Bearer {api_key}
Octo-Capabilities: octo/redemption
Content-Type: application/json
```

**Request-Body:**

```typescript
{
  redemptionCode: string | string[];
}
```

**Response:** `RedemptionObject[]` mit `status: "NO_SHOW"` und `utcNoshowedAt`.

---

### DELETE /redemption/noshow

No-Show-Status aufheben.

```http
DELETE https://api.ventrata.com/octo/redemption/noshow
```

**Verhalten:** Aktuell identisch mit `DELETE /redemption/redeem`.

---

### POST /redemption/credentials

API-Key-Auflösung per Lookup-Input (unauthentifiziert).

```http
POST https://api.ventrata.com/octo/redemption/credentials
Content-Type: application/json
```

**Request-Body:**

```typescript
{
  reference?: string;
  email?: string;
  mobile?: string;
}
```

**Verhalten:** Wählt den ersten API-Key, der das Lookup erfolgreich auflösen kann.

**Response:** `{ apiKey: string }`

---

## RedemptionObject-Schema

```typescript
interface RedemptionObject {
  // Buchungs-Kontext
  product: Product;
  option: Option;
  availability: Availability;

  // Kontaktdaten
  contact: BookingContact;
  resellerReference: string;
  supplierReference: string;

  // Einlöse-spezifisch
  redemptionCode: string;
  redeemable: boolean;
  unredeemableReason: string;
  unredeemableReasonCode: string;

  // Status
  status: BookingStatus | "NO_SHOW";
  utcNoshowedAt: string | null;  // ISO 8601

  // Tickets
  unitItems: BookingUnitItem[];  // Auf einzelnes Ticket reduziert bei Ticket-Level-Code
  voucher: object;               // Ticket-Objekt wenn Code auf Ticket-Ebene auflöst
}
```

---

## BookingUnitItem-Erweiterung (scans)

```typescript
interface BookingUnitItemWithScans extends BookingUnitItem {
  scans: Array<{
    id: string;         // UUID
    status: "CONFIRMED";
    utcScannedAt: string;  // ISO 8601
    seller: {
      id: string;
      name: string;
      reference: string;
      tags: string[];
    };
  }>;
}
```

---

## Serialisierungslogik

- Löst ein Einlösecode auf **Ticket-Ebene** auf:
  - `unitItems` auf dieses einzelne Ticket reduziert
  - Root-Felder werden mit Ticket-Level-Werten überschrieben
  - `voucher` auf Ticket-Objekt gesetzt
- Alle Unit-Items enthalten `scans: []` (Array der Scan-Ereignisse)

---

## Vollständiges Beispiel

### Request: Buchung nachschlagen

```bash
curl -X GET "https://api.ventrata.com/octo/redemption/lookup?reference=GT-2025-001234" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/redemption"
```

### Response

```json
[
  {
    "product": {
      "id": "product_abc123",
      "internalName": "berlin-city-tour"
    },
    "option": {
      "id": "option_def456",
      "internalName": "standard-option"
    },
    "availability": {
      "id": "availability_xyz789",
      "localDateTimeStart": "2025-07-01T10:00:00+02:00"
    },
    "contact": {
      "fullName": "Max Mustermann",
      "emailAddress": "max@example.com",
      "phoneNumber": "+49 170 1234567",
      "locales": ["de-DE"]
    },
    "redemptionCode": "GT-2025-001234",
    "redeemable": true,
    "unredeemableReason": null,
    "unredeemableReasonCode": null,
    "status": "CONFIRMED",
    "utcNoshowedAt": null,
    "unitItems": [
      {
        "uuid": "unit_item_001",
        "unitId": "unit_adult",
        "status": "CONFIRMED",
        "scans": []
      }
    ]
  }
]
```

### Request: Einlösen

```bash
curl -X POST https://api.ventrata.com/octo/redemption/redeem \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/redemption" \
  -H "Content-Type: application/json" \
  -d '{ "redemptionCode": "GT-2025-001234" }'
```

### Response

```json
{
  "redemptionCode": "GT-2025-001234",
  "redeemable": false,
  "unredeemableReason": "Bereits eingelöst",
  "unredeemableReasonCode": "ALREADY_REDEEMED",
  "status": "REDEEMED",
  "unitItems": [
    {
      "uuid": "unit_item_001",
      "unitId": "unit_adult",
      "status": "REDEEMED",
      "scans": [
        {
          "id": "scan_001",
          "status": "CONFIRMED",
          "utcScannedAt": "2025-07-01T10:03:45Z",
          "seller": {
            "id": "seller_001",
            "name": "Berlin Tour GmbH",
            "reference": "BT-001",
            "tags": ["operator"]
          }
        }
      ]
    }
  ]
}
```

### Request: Als No-Show markieren

```bash
curl -X POST https://api.ventrata.com/octo/redemption/noshow \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/redemption" \
  -H "Content-Type: application/json" \
  -d '{ "redemptionCode": "GT-2025-001234" }'
```

### Response

```json
{
  "redemptionCode": "GT-2025-001234",
  "status": "NO_SHOW",
  "utcNoshowedAt": "2025-07-01T10:30:00Z",
  "redeemable": false,
  "unredeemableReason": "No-Show markiert"
}
```

### Request: Mehrere Codes gleichzeitig einlösen

```bash
curl -X POST https://api.ventrata.com/octo/redemption/redeem \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/redemption" \
  -H "Content-Type: application/json" \
  -d '{ "redemptionCode": ["GT-2025-001234", "GT-2025-001235", "GT-2025-001236"] }'
```

### Request: Unauthentifizierte API-Key-Ermittlung

```bash
curl -X POST https://api.ventrata.com/octo/redemption/credentials \
  -H "Content-Type: application/json" \
  -d '{ "email": "max@example.com" }'
```

---

*Quelle: https://docs.ventrata.com/capabilities/redemption*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
