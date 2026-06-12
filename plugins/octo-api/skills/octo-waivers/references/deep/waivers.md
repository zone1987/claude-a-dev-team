# OCTO — Waivers Capability (`octo/waivers`)

## Capability-Identifier

```
octo/waivers
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/waivers
Content-Type: application/json
```

---

## Überblick

Fügt Waiver-Definitionen zu Produkten und Einreichungs-/Status-Felder zu Buchungs-
operationen hinzu. Waivers sind rechtlich bindende Dokumente (Haftungsausschlüsse),
die Gäste vor der Teilnahme ausfüllen und unterschreiben müssen.

---

## Schema-Erweiterungen am Product

Endpunkte: `GET /products`, `GET /products/{productId}`

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `waiverPer` | enum | `"BOOKING"` oder `"UNIT"` — Einreichungsebene |
| `waiverRequired` | boolean | Waivers sind Pflicht |
| `waivers` | Waiver[] | Liste der Waiver-Definitionen |

---

## Waiver-Objekt (vollständiges Schema)

```typescript
interface Waiver {
  id: string;               // UUID
  title: string;            // Waiver-Bezeichnung
  shortDescription: string; // Kurzbeschreibung
  content: string;          // Markdown mit Feld-Tags: "-Feldname-=__"
  fields: WaiverField[];    // Geparste Eingabefelder aus content
}

interface WaiverField {
  id: string;
  internalName: string;
  title: string;
  shortDescription: string | null;
  required: boolean;
  inputType: WaiverFieldInputType;
  maxLength: number | null;
  selectOptions: string[];
}

type WaiverFieldInputType =
  | "text"       // Freitextfeld
  | "email"      // E-Mail-Eingabe
  | "signature"  // Unterschrift-Box
  | "country";   // Länderauswahl (ISO 3166-1 alpha-2)
```

---

## Schema-Erweiterungen am BookingWriteRequest

Endpunkte: `POST /bookings`, `PATCH /bookings/{uuid}`

### Bei `waiverPer = "BOOKING"` (auf Root-Ebene):

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `waiverId` | string (UUID) | nein | Referenz auf `product.waivers[].id` |
| `waiverFieldValues` | WaiverFieldValue[] | nein | Ausgefüllte Waiver-Felder |
| `waiverFile` | string (data URI) | nein | PDF als `data:application/pdf;base64,...` |

### Bei `waiverPer = "UNIT"` (innerhalb jedes `unitItems[]`-Eintrags):

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `waiverId` | string (UUID) | nein | Waiver-Referenz pro Unit-Item |
| `waiverFieldValues` | WaiverFieldValue[] | nein | Felder pro Teilnehmer |
| `waiverFile` | string (data URI) | nein | PDF pro Teilnehmer |

### WaiverFieldValue-Objekt

```typescript
interface WaiverFieldValue {
  fieldId: string;  // Referenz auf WaiverField.id
  value: string;    // Eingabewert (ISO 3166-1 alpha-2 für country-Felder)
}
```

---

## Schema-Erweiterungen an der Booking-Response

Felder in `Booking` und `BookingUnitItem`:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `waiverId` | string (UUID) | Zugeordnete Waiver-ID |
| `waiverFileUrl` | string (URL) | Speicherort des eingereichten PDFs |
| `waiverFieldValues` | WaiverFieldValue[] | Eingereichte Felddaten |
| `waiversComplete` | boolean | Vollständigkeitsstatus der Anforderungen |

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|-----|--------------|
| `WAIVER_ON_BOOKING_ONLY` | 400 | Waiver auf falscher Ebene eingereicht (nur BOOKING) |
| `WAIVER_ON_TICKET_ONLY` | 400 | Waiver auf falscher Ebene eingereicht (nur UNIT) |
| `INVALID_WAIVER_ID` | 400 | `waiverId` stimmt nicht mit Produkt-Waivers überein |

---

## Einreichungslogik

```
if waiverPer === "BOOKING":
  → waiverId und waiverFieldValues auf Root-Ebene der Booking-Request
  
if waiverPer === "UNIT":
  → waiverId und waiverFieldValues innerhalb jedes unitItems[]-Eintrags
```

---

## Vollständiges Beispiel

### Response: Product mit Waiver-Definitionen

```bash
curl -X GET "https://api.ventrata.com/octo/products/product_abc123" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/waivers"
```

```json
{
  "id": "product_abc123",
  "waiverPer": "UNIT",
  "waiverRequired": true,
  "waivers": [
    {
      "id": "waiver_001",
      "title": "Haftungsausschluss Klettertour",
      "shortDescription": "Bitte lesen und unterschreiben Sie dieses Dokument vor der Tour.",
      "content": "# Haftungsausschluss\n\nIch, -Vollständiger Name-=__, erkläre mich einverstanden...\n\n**Geburtsdatum:** -Geburtsdatum-=__\n\n**Unterschrift:** -Unterschrift-=__",
      "fields": [
        {
          "id": "field_name",
          "internalName": "full_name",
          "title": "Vollständiger Name",
          "shortDescription": null,
          "required": true,
          "inputType": "text",
          "maxLength": 100,
          "selectOptions": []
        },
        {
          "id": "field_birthdate",
          "internalName": "birth_date",
          "title": "Geburtsdatum",
          "shortDescription": "Format: TT.MM.JJJJ",
          "required": true,
          "inputType": "text",
          "maxLength": 10,
          "selectOptions": []
        },
        {
          "id": "field_signature",
          "internalName": "signature",
          "title": "Unterschrift",
          "shortDescription": null,
          "required": true,
          "inputType": "signature",
          "maxLength": null,
          "selectOptions": []
        },
        {
          "id": "field_nationality",
          "internalName": "nationality",
          "title": "Nationalität",
          "shortDescription": null,
          "required": false,
          "inputType": "country",
          "maxLength": null,
          "selectOptions": []
        }
      ]
    }
  ]
}
```

### Request: Buchung mit UNIT-Level-Waiver

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/waivers" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_abc123",
    "optionId": "option_def456",
    "availabilityId": "availability_xyz789",
    "unitItems": [
      {
        "unitId": "unit_adult",
        "waiverId": "waiver_001",
        "waiverFieldValues": [
          { "fieldId": "field_name", "value": "Max Mustermann" },
          { "fieldId": "field_birthdate", "value": "15.03.1990" },
          { "fieldId": "field_signature", "value": "data:image/png;base64,iVBORw0KGgo..." },
          { "fieldId": "field_nationality", "value": "DE" }
        ]
      },
      {
        "unitId": "unit_adult",
        "waiverId": "waiver_001",
        "waiverFieldValues": [
          { "fieldId": "field_name", "value": "Erika Mustermann" },
          { "fieldId": "field_birthdate", "value": "22.07.1992" },
          { "fieldId": "field_signature", "value": "data:image/png;base64,iVBORw0KGgo..." },
          { "fieldId": "field_nationality", "value": "AT" }
        ]
      }
    ]
  }'
```

### Response

```json
{
  "uuid": "booking_111222",
  "status": "ON_HOLD",
  "waiversComplete": true,
  "unitItems": [
    {
      "uuid": "unit_item_001",
      "unitId": "unit_adult",
      "waiverId": "waiver_001",
      "waiverFileUrl": "https://cdn.ventrata.com/waivers/unit_item_001.pdf",
      "waiverFieldValues": [
        { "fieldId": "field_name", "value": "Max Mustermann" },
        { "fieldId": "field_birthdate", "value": "15.03.1990" },
        { "fieldId": "field_signature", "value": "data:image/png;base64,iVBORw0KGgo..." },
        { "fieldId": "field_nationality", "value": "DE" }
      ]
    }
  ]
}
```

### Request: Waiver als PDF-Datei einreichen

```bash
curl -X PATCH "https://api.ventrata.com/octo/bookings/booking_111222" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/waivers" \
  -H "Content-Type: application/json" \
  -d '{
    "unitItems": [
      {
        "uuid": "unit_item_001",
        "waiverId": "waiver_001",
        "waiverFile": "data:application/pdf;base64,JVBERi0xLjQK..."
      }
    ]
  }'
```

---

*Quelle: https://docs.ventrata.com/capabilities/waivers*
*Typen: https://github.com/octotravel/octo-types (MIT-Lizenz)*
