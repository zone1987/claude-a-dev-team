# OCTO — Identities Capability (`octo/identities`)

## Capability-Identifier

```
octo/identities
```

> **Status:** Aktuell intern (`internal: true`). Noch nicht öffentlich verfügbar.

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/identities
Content-Type: application/json
```

---

## Überblick

Die Identities-Capability ermöglicht die Verwaltung von wiederverwendbaren Identitäten,
die an Buchungen, Orders und Geschenkgutscheine gehängt werden können. Eine Identität
besteht aus einer `id` (UUID) und einem `key` (frei definierbarer Bezeichner) und
dient der Verknüpfung von Buchungen mit externen Benutzer-/Kundenprofilen.

---

## Identity-Objekt (vollständiges Schema)

```typescript
interface Identity {
  id: string;   // UUID der Identität
  key: string;  // Frei definierbarer Schlüssel (z.B. CRM-Kunden-ID)
}
```

---

## Schema-Erweiterungen

### Booking (Response-Erweiterungen)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `identityId` | string | Zugeordnete Identity-ID |
| `identity` | Identity \| null | Vollständiges Identity-Objekt |

### Order (Response-Erweiterungen)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `identityId` | string | Zugeordnete Identity-ID |
| `identity` | Identity \| null | Vollständiges Identity-Objekt |

### Gift (Response-Erweiterungen)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `identityId` | string | Zugeordnete Identity-ID |
| `identity` | Identity \| null | Vollständiges Identity-Objekt |

---

## Request-Erweiterungen

### BookingWriteRequest

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `identityId` | string | optional | Zu verknüpfende Identity-ID |

### OrderCreateRequest

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `identityId` | string | optional | Zu verknüpfende Identity-ID |

### OrderUpdateRequest

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `identityId` | string | optional | Zu verknüpfende Identity-ID |

### GiftCreateRequest

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `identityId` | string | optional | Zu verknüpfende Identity-ID |

---

## Betroffene Routen

| Methode | Pfad | Identity-Unterstützung |
|---------|------|----------------------|
| POST | `/bookings` | `identityId` im Request Body |
| PATCH | `/bookings/{uuid}` | `identityId` im Request Body |
| POST | `/bookings/{uuid}/confirm` | `identityId` im Request Body |
| POST | `/orders` | `identityId` im Request Body |
| PATCH | `/orders/{orderId}` | `identityId` im Request Body |
| PATCH | `/orders/{orderId}/preview` | `identityId` im Request Body |
| POST | `/orders/{orderId}/confirm` | `identityId` im Request Body |
| POST | `/gifts` | `identityId` im Request Body |
| PATCH | `/gifts/{uuid}` | `identityId` im Request Body |
| POST | `/checkin/lookup` | `identityId` als Filter-Parameter |

> Verschachtelte Buchungen und Geschenkgutscheine innerhalb von Orders können
> jeweils eigene individuelle `identityId`-Werte tragen.

---

## Endpunkte

### POST /identities — Identität erstellen

**Request Body:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `key` | string | ja | Externer Bezeichner (z.B. CRM-ID, User-UUID) |

```bash
curl -X POST https://api.ventrata.com/octo/identities \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/identities" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "crm-customer-98765"
  }'
```

**Response:** Identity-Objekt (Status 200)

```json
{
  "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
  "key": "crm-customer-98765"
}
```

---

### PATCH /identities/{identityId} — Identität aktualisieren

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `identityId` | string (UUID) | ja | Identity-UUID |

**Request Body:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `key` | string | optional | Neuer externer Bezeichner |

```bash
curl -X PATCH "https://api.ventrata.com/octo/identities/b2c3d4e5-f6a7-8901-bcde-f12345678901" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/identities" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "crm-customer-updated-key"
  }'
```

**Response:** Aktualisiertes Identity-Objekt

---

### DELETE /identities/{identityId} — Identität löschen

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `identityId` | string (UUID) | ja | Identity-UUID |

```bash
curl -X DELETE "https://api.ventrata.com/octo/identities/b2c3d4e5-f6a7-8901-bcde-f12345678901" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/identities"
```

**Response:** `200 OK` mit leerem Body

---

## Anwendungsbeispiel — Buchung mit Identity verknüpfen

```bash
# 1. Identity erstellen (einmalig pro Kundenaccount)
curl -X POST https://api.ventrata.com/octo/identities \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/identities" \
  -H "Content-Type: application/json" \
  -d '{"key": "crm-customer-98765"}'
# → {"id": "b2c3d4e5-...", "key": "crm-customer-98765"}

# 2. Buchung mit Identity verknüpfen
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/identities" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_stadtfuehrung",
    "optionId": "default",
    "availabilityId": "2026-06-15T10:00:00+02:00",
    "unitItems": [{"unitId": "unit_adult"}],
    "identityId": "b2c3d4e5-f6a7-8901-bcde-f12345678901"
  }'

# 3. Check-in per Identity nachschlagen
curl -X POST https://api.ventrata.com/octo/checkin/lookup \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/identities, octo/checkin" \
  -H "Content-Type: application/json" \
  -d '{"identityId": "b2c3d4e5-f6a7-8901-bcde-f12345678901"}'
```

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `IDENTITY_NOT_FOUND` | 404 | Identity mit ID nicht gefunden |
| `IDENTITY_INVALID_KEY` | 400 | Key-Wert ist ungültig (z.B. leer) |

---

## Capability-Abhängigkeiten

| Verwendet mit | Zweck |
|--------------|-------|
| `octo/checkin` | Identity als Filter bei Check-in-Lookup |
| `octo/cart` | Identity auf Order-Ebene und pro Buchung/Gift in Orders |
| `octo/gifts` | Identity auf Gift-Objekten |

---

*Quelle: https://docs.ventrata.com/capabilities/identities*
