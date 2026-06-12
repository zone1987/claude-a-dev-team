# OCTO — Webhooks Capability (`octo/webhooks`)

## Capability-Identifier

```
octo/webhooks
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/webhooks
Content-Type: application/json
```

---

## Überblick

Die Webhooks-Capability ermöglicht die Verwaltung von Webhook-Subscriptions. Webhooks
werden bei bestimmten OCTO-Events per HTTP POST an eine konfigurierbare URL gesendet.
Jeder Webhook wird mit den aktiven Capabilities der Verbindung serialisiert. Custom
Headers (z.B. Shared Secrets) können konfiguriert werden.

---

## Unterstützte Event-Typen

| Event | Beschreibung | Payload-Schlüssel |
|-------|-------------|-------------------|
| `booking_update` | Buchung wurde erstellt/geändert/bestätigt/storniert | `booking` |
| `order_update` | Order wurde erstellt/geändert/bestätigt/storniert | `order` |
| `availability_update` | Verfügbarkeit hat sich geändert | `availability` |
| `product_update` | Produkt wurde geändert | `product` |

> **Hinweis:** `order_update` beinhaltet `octo/cart` automatisch.

---

## Webhook-Objekt (vollständiges Schema)

```typescript
interface Webhook {
  id: string;                  // UUID des Webhooks
  event: WebhookEvent;         // Event-Typ
  url: string;                 // Ziel-URL für HTTP POST
  capabilities: string[];      // Aktive Capabilities aus Octo-Capabilities-Header
  useContactLanguage: boolean; // Sprache aus Kontakt nutzen
  headers: Record<string, string>; // Custom HTTP-Header
  retryOnError: boolean;       // Automatischer Retry bei Fehler
}

type WebhookEvent = "booking_update" | "order_update" | "availability_update" | "product_update";
```

---

## Endpunkte

### POST /webhooks — Webhook erstellen

**Request Body:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `event` | WebhookEvent | ja | Event-Typ |
| `url` | string (URL) | ja | Ziel-URL |
| `useContactLanguage` | boolean | optional | Sprache aus Kontakt |
| `headers` | object | optional | Custom HTTP-Header |
| `retryOnError` | boolean | optional | Retry bei Fehler |

```bash
curl -X POST https://api.ventrata.com/octo/webhooks \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/webhooks" \
  -H "Content-Type: application/json" \
  -d '{
    "event": "booking_update",
    "url": "https://myapp.example.com/webhooks/octo",
    "retryOnError": true,
    "headers": {
      "X-Webhook-Secret": "mein-shared-secret-123"
    }
  }'
```

**Response:** Webhook-Objekt (Status 200)

---

### PATCH /webhooks/{webhookId} — Webhook aktualisieren

**Alle Felder optional.** Capabilities werden bei jedem Update aus dem
`Octo-Capabilities`-Header neu berechnet.

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `webhookId` | string | ja | Webhook-ID |

```bash
curl -X PATCH "https://api.ventrata.com/octo/webhooks/{webhookId}" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/webhooks, octo/pricing" \
  -H "Content-Type: application/json" \
  -d '{
    "retryOnError": false,
    "useContactLanguage": true
  }'
```

---

### GET /webhooks — Webhooks auflisten

Gibt alle Webhooks der authentifizierten Verbindung zurück.

```bash
curl "https://api.ventrata.com/octo/webhooks" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/webhooks"
```

**Response:** Array von Webhook-Objekten

---

### DELETE /webhooks/{webhookId} — Webhook per ID löschen

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `webhookId` | string | ja | Webhook-ID |

```bash
curl -X DELETE "https://api.ventrata.com/octo/webhooks/{webhookId}" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/webhooks"
```

**Response:** `200 OK`

---

### DELETE /webhooks — Webhook per URL löschen

**Query-Parameter ODER Request Body:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `url` | string (URL) | ja | Ziel-URL des zu löschenden Webhooks |

```bash
# Via Query-Parameter
curl -X DELETE "https://api.ventrata.com/octo/webhooks?url=https://myapp.example.com/webhooks/octo" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/webhooks"

# Via Request Body
curl -X DELETE "https://api.ventrata.com/octo/webhooks" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/webhooks" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://myapp.example.com/webhooks/octo"}'
```

---

## Webhook-Payload-Struktur

OCTO sendet HTTP POST an die konfigurierte URL mit folgendem JSON-Body:

```typescript
interface WebhookEventPayload {
  event: string;                    // Event-Name (z.B. "booking.updated")
  webhook: Webhook;                  // Webhook-Objekt
  supplier: WebhookSupplier;         // Supplier-Details
  order?: Order;                     // Bei order_update
  booking?: Booking;                 // Bei booking_update
  product?: Product;                 // Bei product_update
  availability?: Availability;       // Bei availability_update
  diff: WebhookDiffOperation[];      // Geänderte Felder
}

interface WebhookSupplier {
  id: string;
  name: string;
  reference: string;
  website: string;
}

interface WebhookDiffOperation {
  op: "add" | "remove" | "replace"; // Operationstyp
  path: string;                     // JSON-Pointer zum geänderten Feld
  was: any;                         // Vorheriger Wert
  value: any;                       // Neuer Wert
}
```

---

## Payload-Beispiele

### booking_update Payload

```json
{
  "event": "booking.updated",
  "webhook": {
    "id": "wh_12345678",
    "event": "booking_update",
    "url": "https://myapp.example.com/webhooks/octo"
  },
  "supplier": {
    "id": "supplier_ventrata",
    "name": "Ventrata Demo",
    "reference": "DEMO",
    "website": "https://ventrata.com"
  },
  "booking": {
    "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "status": "CONFIRMED",
    "optionId": "default"
  },
  "diff": [
    {
      "op": "replace",
      "path": "/status",
      "was": "ON_HOLD",
      "value": "CONFIRMED"
    }
  ]
}
```

### availability_update Payload

```json
{
  "event": "availability.updated",
  "webhook": { "id": "wh_87654321", "event": "availability_update" },
  "supplier": { "id": "supplier_demo", "name": "Demo Supplier" },
  "availability": {
    "id": "2026-06-15T10:00:00+02:00",
    "localDateTimeStart": "2026-06-15T10:00:00+02:00",
    "status": "FREESALE",
    "vacancies": 20
  },
  "diff": [
    {
      "op": "replace",
      "path": "/vacancies",
      "was": 25,
      "value": 20
    }
  ]
}
```

---

## Serialisierungsregeln

- Event-Objekte werden identisch zu den entsprechenden GET-Endpunkten serialisiert:
  - `booking_update` → wie `GET /bookings/{uuid}`
  - `order_update` → wie `GET /orders/{orderId}`
  - `product_update` → wie `GET /products/{productId}`
  - `availability_update` → wie `GET /availability/{availabilityId}`
- Capability-spezifische Felder werden basierend auf den aktiven Webhook-Capabilities eingeschlossen
- **`octo/cardPayments`:** Unterdrückt Adyen-Session-Payloads im Webhook

---

## Retry-Logik

| Feld | Verhalten |
|------|-----------|
| `retryOnError: true` | Automatischer Retry bei HTTP-Fehlerantworten (4xx/5xx) |
| `retryOnError: false` | Kein Retry; Payload wird einmalig gesendet |

Genaue Retry-Intervalle und maximale Versuche sind implementierungsabhängig.

---

## Sicherheit via Custom Headers

Zur Verifizierung von Webhook-Authentizität können Shared Secrets als Custom Header
konfiguriert werden:

```json
{
  "headers": {
    "X-Webhook-Secret": "mein-shared-secret-abc123",
    "X-Source": "ventrata-octo"
  }
}
```

Der Empfänger prüft den Header-Wert gegen seinen konfigurierten Secret-Wert.
HMAC-Signatur-Verifikation ist in der öffentlichen Dokumentation nicht spezifiziert.

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `WEBHOOK_NOT_FOUND` | 404 | Webhook mit ID nicht gefunden |
| `WEBHOOK_INVALID_URL` | 400 | Ungültige Ziel-URL |
| `WEBHOOK_INVALID_EVENT` | 400 | Ungültiger Event-Typ |

---

## Capability-Abhängigkeiten

| Verwendet mit | Zweck |
|--------------|-------|
| `octo/cart` | `order_update` Events; wird automatisch eingeschlossen |
| `octo/pricing` | Preisfelder in Booking/Order-Payloads |
| `octo/cardPayments` | Unterdrückt Session-Daten in Payloads |
| `octo/notifications` | Alternative Subscription-API für Event-Benachrichtigungen |

---

*Quelle: https://docs.ventrata.com/capabilities/webhooks*
