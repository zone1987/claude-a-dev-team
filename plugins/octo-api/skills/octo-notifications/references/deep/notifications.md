# OCTO — Notifications Capability (`octo/notifications`)

## Capability-Identifier

```
octo/notifications
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/notifications
Content-Type: application/json
```

---

## Überblick

Die Notifications-Capability bietet eine Subscription-basierte Alternative zu Webhooks.
Statt globaler Webhooks können gezielte Subscriptions auf bestimmte Event-Typen erstellt
werden. Die Subscriptions senden HTTP POST an eine konfigurierbare URL wenn OCTO-Events
auftreten.

**Unterschied zu `octo/webhooks`:**
- `octo/webhooks`: Allgemeine Webhook-Verwaltung pro Verbindung
- `octo/notifications`: Detailliertere Subscription-Verwaltung mit spezifischen
  Notification-Typen

---

## Unterstützte Notification-Typen

| Typ | Beschreibung | Payload-Felder |
|-----|-------------|----------------|
| `BOOKING_UPDATE` | Buchung erstellt/geändert/bestätigt/storniert | `uuid` |
| `AVAILABILITY_UPDATE` | Verfügbarkeit geändert | `productId`, `optionId`, `availabilityIds` |
| `PRODUCT_UPDATE` | Produkt geändert | `productId` |

> Groß-/Kleinschreibung im Request: case-insensitive. In Responses: UPPERCASE.

---

## NotificationSubscription-Objekt (vollständiges Schema)

```typescript
interface NotificationSubscription {
  subscriptionId: string;            // UUID der Subscription
  url: string;                       // Ziel-URL für HTTP POST
  notificationTypes: NotificationType[]; // Abonnierte Typen
  headers: Record<string, string>;   // Custom HTTP-Header
  retryOnError: boolean;             // Automatischer Retry bei Fehler
}

type NotificationType = "BOOKING_UPDATE" | "AVAILABILITY_UPDATE" | "PRODUCT_UPDATE";
```

---

## NotificationSubscriptionRequest-Objekt

```typescript
interface NotificationSubscriptionRequest {
  url: string;                           // Pflicht — Ziel-URL
  notificationTypes: NotificationType[]; // Pflicht — mind. ein Typ
  headers?: Record<string, string>;      // Optional — Custom-Header
  retryOnError?: boolean;                // Optional — Retry-Logik
}
```

---

## Endpunkte

Alle Pfade sind öffentliche `/octo`-Routen.

### POST /notifications/subscriptions — Subscription erstellen

**Request Body:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `url` | string (URL) | ja | Ziel-URL für Benachrichtigungen |
| `notificationTypes` | NotificationType[] | ja | Mindestens ein Typ |
| `headers` | object | optional | Custom HTTP-Header |
| `retryOnError` | boolean | optional | Retry bei HTTP-Fehler |

```bash
curl -X POST https://api.ventrata.com/octo/notifications/subscriptions \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/notifications" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://myapp.example.com/notifications/octo",
    "notificationTypes": ["BOOKING_UPDATE", "AVAILABILITY_UPDATE"],
    "retryOnError": true,
    "headers": {
      "X-Notification-Secret": "mein-shared-secret-xyz"
    }
  }'
```

**Response:** NotificationSubscription-Objekt (Status 200)

```json
{
  "subscriptionId": "sub_a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "url": "https://myapp.example.com/notifications/octo",
  "notificationTypes": ["BOOKING_UPDATE", "AVAILABILITY_UPDATE"],
  "headers": {
    "X-Notification-Secret": "mein-shared-secret-xyz"
  },
  "retryOnError": true
}
```

---

### GET /notifications/subscriptions — Subscriptions auflisten (paginiert)

```bash
curl "https://api.ventrata.com/octo/notifications/subscriptions" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/notifications"
```

**Response:** Paginiertes Array von NotificationSubscription-Objekten

---

### GET /notifications/subscriptions/{subscriptionId} — Einzelne Subscription abrufen

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `subscriptionId` | string | ja | Subscription-ID |

```bash
curl "https://api.ventrata.com/octo/notifications/subscriptions/sub_a1b2c3d4-..." \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/notifications"
```

**Response:** NotificationSubscription-Objekt

---

### PATCH /notifications/subscriptions/{subscriptionId} — Subscription aktualisieren

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `subscriptionId` | string | ja | Subscription-ID |

**Request Body (alle optional):**

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `url` | string | Neue Ziel-URL |
| `notificationTypes` | NotificationType[] | Neue Typen-Liste |
| `headers` | object | Neue Custom-Header |
| `retryOnError` | boolean | Retry-Einstellung |

```bash
curl -X PATCH "https://api.ventrata.com/octo/notifications/subscriptions/sub_a1b2c3d4-..." \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/notifications" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationTypes": ["BOOKING_UPDATE", "AVAILABILITY_UPDATE", "PRODUCT_UPDATE"],
    "retryOnError": false
  }'
```

**Response:** Aktualisiertes NotificationSubscription-Objekt

---

### DELETE /notifications/subscriptions/{subscriptionId} — Subscription löschen

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `subscriptionId` | string | ja | Subscription-ID |

```bash
curl -X DELETE "https://api.ventrata.com/octo/notifications/subscriptions/sub_a1b2c3d4-..." \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/notifications"
```

**Response:** `200 OK`

---

## Notification-Payload-Struktur

HTTP POST an die konfigurierte URL:

### BOOKING_UPDATE Payload

```json
{
  "type": "BOOKING_UPDATE",
  "uuid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

### AVAILABILITY_UPDATE Payload

```json
{
  "type": "AVAILABILITY_UPDATE",
  "productId": "product_london_eye",
  "optionId": "3d6f0a3a-59d4-4b16-a0c5-11d2d8a4e6b7",
  "availabilityIds": [
    "2026-06-15T10:00:00+01:00",
    "2026-06-15T14:00:00+01:00"
  ]
}
```

### PRODUCT_UPDATE Payload

```json
{
  "type": "PRODUCT_UPDATE",
  "productId": "product_london_eye"
}
```

---

## Retry-Logik

| Einstellung | Verhalten |
|-------------|-----------|
| `retryOnError: true` | Automatischer Retry bei HTTP 4xx/5xx Antworten |
| `retryOnError: false` | Kein Retry; Payload einmalig gesendet |

---

## Sicherheit via Custom Headers

```json
{
  "headers": {
    "X-Notification-Secret": "shared-secret-value",
    "X-Source": "ventrata-octo"
  }
}
```

---

## Vergleich mit octo/webhooks

| Aspekt | octo/webhooks | octo/notifications |
|--------|--------------|-------------------|
| Granularität | Pro Verbindung global | Pro Subscription individuell |
| Typen-Steuerung | Event-basiert (`booking_update`, etc.) | Typ-basiert (`BOOKING_UPDATE`, etc.) |
| Paginierung | Nein | Ja (GET /subscriptions) |
| Diff-Felder | Ja (`diff[]` im Payload) | Nein (nur IDs im Payload) |
| Capabilities im Payload | Ja | Nein |

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `SUBSCRIPTION_NOT_FOUND` | 404 | Subscription mit ID nicht gefunden |
| `SUBSCRIPTION_INVALID_URL` | 400 | Ungültige Ziel-URL |
| `SUBSCRIPTION_INVALID_TYPE` | 400 | Ungültiger Notification-Typ |
| `SUBSCRIPTION_TYPES_REQUIRED` | 400 | Kein `notificationTypes`-Wert angegeben |

---

## Capability-Abhängigkeiten

| Verwendet mit | Zweck |
|--------------|-------|
| `octo/webhooks` | Parallele Nutzung möglich; unterschiedliche Granularität |
| `octo/campaigns` | Kampagnen-Kontext in Benachrichtigungen |

---

*Quelle: https://docs.ventrata.com/capabilities/notifications*
