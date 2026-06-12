# OCTO — Waitlists Capability (`octo/waitlists`)

## Capability-Identifier

```
octo/waitlists
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/waitlists
Content-Type: application/json
```

---

## Überblick

Die Waitlists-Capability ermöglicht das Erstellen von Wartelisten-Einträgen für
ausgebuchte Produkte/Optionen. Ein Wartelisten-Eintrag referenziert ein Produkt,
eine Option, ein Datum und gewünschte Unit-Mengen. Kontaktdaten des wartenden Gastes
werden optional erfasst.

---

## Waitlist-Objekt (vollständiges Schema)

```typescript
interface Waitlist {
  id: string;                         // UUID des Wartelisten-Eintrags
  uuid: string;                       // Alternativer Identifier (UUID)
  status: WaitlistStatus;             // Aktueller Status
  optionId: string;                   // UUID der Option (UUID-Format)
  productId: string;                  // UUID des Produkts
  localDate: string;                  // Lokales Datum (ISO, z.B. "2026-05-14")
  units: WaitlistUnit[];              // Gewünschte Unit-Mengen
  contact: WaitlistContact | null;    // Kontaktdaten (null bei Maskierung)
  supplierReference: string;          // Supplier-seitige Referenz
  size: number;                       // Gesamtgröße der Warteliste (Integer)
  visibleContactFields: string[];     // Sichtbare Kontaktfelder
  requiredContactFields: string[];    // Pflicht-Kontaktfelder
  createdAt: string;                  // ISO 8601 Erstellungszeitpunkt
  utcCreatedAt: string;               // UTC-Erstellungszeitpunkt (ISO 8601)
  utcUpdatedAt: string;               // UTC letzter Update (ISO 8601)
}

type WaitlistStatus = "ACTIVE";  // Derzeit einziger Wert

interface WaitlistUnit {
  unitId: string;     // Unit-ID (z.B. "unit_adult" oder UUID)
  quantity: number;   // Gewünschte Menge (Integer)
}

interface WaitlistContact {
  fullName: string;
  emailAddress: string | null;  // null bei aktivierter Kontaktmaskierung
}
```

---

## WaitlistRequest-Objekt

```typescript
interface WaitlistRequest {
  productId: string;     // Pflicht — Produkt-ID
  optionId: string;      // Pflicht — Option-ID (UUID-Format)
  localDate: string;     // Pflicht — ISO-Datum (z.B. "2026-05-14")
  units: WaitlistUnit[]; // Pflicht — mindestens eine Einheit mit quantity > 0
  contact?: {            // Optional
    fullName?: string;
    emailAddress?: string;
  };
}
```

---

## Endpunkte

### POST /waitlists — Wartelisten-Eintrag erstellen

**Request Body:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `productId` | string | ja | Produkt-ID |
| `optionId` | string (UUID) | ja | Option-ID im UUID-Format |
| `localDate` | string (ISO-Datum) | ja | Gewünschtes Datum |
| `units` | WaitlistUnit[] | ja | Mindestens eine Unit mit quantity > 0 |
| `contact` | object | optional | Kontaktdaten des wartenden Gastes |
| `contact.fullName` | string | optional | Vollständiger Name |
| `contact.emailAddress` | string | optional | E-Mail-Adresse |

```bash
curl -X POST https://api.ventrata.com/octo/waitlists \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/waitlists" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_london_eye",
    "optionId": "3d6f0a3a-59d4-4b16-a0c5-11d2d8a4e6b7",
    "localDate": "2026-06-15",
    "units": [
      {
        "unitId": "unit_adult",
        "quantity": 2
      },
      {
        "unitId": "unit_child",
        "quantity": 1
      }
    ],
    "contact": {
      "fullName": "Max Mustermann",
      "emailAddress": "max@example.com"
    }
  }'
```

**Response:** Waitlist-Objekt (Status 200)

```json
{
  "id": "wl_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "ACTIVE",
  "optionId": "3d6f0a3a-59d4-4b16-a0c5-11d2d8a4e6b7",
  "productId": "product_london_eye",
  "localDate": "2026-06-15",
  "units": [
    { "unitId": "unit_adult", "quantity": 2 },
    { "unitId": "unit_child", "quantity": 1 }
  ],
  "contact": {
    "fullName": "Max Mustermann",
    "emailAddress": "max@example.com"
  },
  "supplierReference": "WL-2026-00123",
  "size": 3,
  "visibleContactFields": ["fullName", "emailAddress"],
  "requiredContactFields": ["emailAddress"],
  "createdAt": "2026-06-12T08:00:00+02:00",
  "utcCreatedAt": "2026-06-12T06:00:00Z",
  "utcUpdatedAt": "2026-06-12T06:00:00Z"
}
```

---

## Validierungsregeln

| Regel | Beschreibung |
|-------|-------------|
| Mindestens eine Non-Item-Unit mit `quantity > 0` | Gesamtgröße muss > 0 sein |
| `optionId` im UUID-Format | Muss gültiges UUID-Format haben |
| `localDate` im ISO-Format | "YYYY-MM-DD" Format |

---

## Unit-ID-Formate

Units können in zwei Formaten referenziert werden:

```json
// Namensbasiert
{ "unitId": "unit_adult", "quantity": 2 }

// UUID-basiert
{ "unitId": "3d6f0a3a-59d4-4b16-a0c5-11d2d8a4e6b7", "quantity": 2 }
```

---

## Kontaktfeld-Sichtbarkeit

`visibleContactFields` und `requiredContactFields` werden vom Supplier konfiguriert und
steuern welche Kontaktfelder angezeigt und welche Pflichtfelder sind:

| Feld-Typ | Mögliche Werte |
|----------|---------------|
| `visibleContactFields` | `["fullName", "emailAddress", "phoneNumber", "country"]` |
| `requiredContactFields` | Subset von `visibleContactFields` |

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `WAITLIST_INVALID_OPTION` | 400 | Option-ID nicht im UUID-Format oder nicht gefunden |
| `WAITLIST_INVALID_UNITS` | 400 | Keine gültige Unit-Konfiguration (Gesamtmenge = 0) |
| `WAITLIST_PRODUCT_NOT_FOUND` | 404 | Produkt nicht gefunden |

---

## Hinweise zur Vollständigkeit

Die öffentliche Dokumentation beschreibt ausschließlich den `POST /waitlists` Endpunkt.
Weitere Endpunkte (GET, PATCH, DELETE) sowie Webhook-Events für Wartelisten-Konvertierungen
sind in der referenzierten OpenAPI-Spezifikation möglicherweise vorhanden, aber nicht
in der öffentlichen HTML-Dokumentation beschrieben.

---

*Quelle: https://docs.ventrata.com/capabilities/waitlists*
