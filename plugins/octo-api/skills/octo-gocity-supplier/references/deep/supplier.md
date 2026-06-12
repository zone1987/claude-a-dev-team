# Go City Trade API V2 — Supplier (vollständige Referenz)

## Endpunkt: GET /octo/supplier

Gibt Supplier-Informationen nach OCTO-Spezifikation zurück.

```http
GET https://api.gocity.com/octo/supplier
Authorization: Bearer {your_token}
```

**Parameter:** Keine Query-Parameter, kein Request-Body.

**Response:** `200 OctoSupplier`

---

## OctoSupplier-Schema (vollständig)

```typescript
type OctoSupplier = {
  id: string;                     // Eindeutige ID des Suppliers
  name: string;                   // Anzeigename des Suppliers
  endpoint: string;               // Basis-URL der OCTO-Implementierung des Suppliers
  contact: OctoSupplierContact;   // Kontaktdaten
};

type OctoSupplierContact = {
  website: string;   // Website-URL des Suppliers
  email: string;     // E-Mail-Adresse
  telephone: string; // Telefonnummer
  address: string;   // Postanschrift
};
```

---

## Beispiel-Request

```http
GET https://api.gocity.com/octo/supplier
Authorization: Bearer {your_token}
```

## Beispiel-Response

```json
{
  "id": "go-city-supplier-id",
  "name": "Go City",
  "endpoint": "https://api.gocity.com",
  "contact": {
    "website": "https://www.gocity.com",
    "email": "trade@gocity.com",
    "telephone": "+1-800-000-0000",
    "address": "Go City Ltd, London, UK"
  }
}
```

---

## Unterschied zu Ventrata

| Aspekt | Ventrata | Go City |
|--------|----------|---------|
| Schema | `Supplier` mit `shortDescription?`, `media?` (mit octo/content) | `OctoSupplier` ohne Content-Felder |
| Capabilities | `octo/content` erweitert das Objekt | Keine Content-Felder verfügbar |
| Endpoint | `GET /octo/supplier/` (mit Trailing Slash) | `GET /octo/supplier` (ohne Trailing Slash) |

---

## Verwendungszweck

Der Supplier-Endpunkt wird typischerweise verwendet um:
1. Die `endpoint`-URL der OCTO-Implementierung zu entdecken
2. Kontaktinformationen des Suppliers zu erhalten
3. Zu überprüfen, ob der API-Key korrekt konfiguriert ist

---

**Quellen:**
- `/tmp/gocity-openapi.json` — Go City Trade API V2 OpenAPI 3.1 Spec (autoritativ)
- `/tmp/gocity.html` — Gerenderte Redoc-Dokumentation
