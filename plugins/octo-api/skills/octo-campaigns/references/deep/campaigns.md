# OCTO — Campaigns Capability (`octo/campaigns`)

## Capability-Identifier

```
octo/campaigns
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/campaigns
Content-Type: application/json
```

---

## Überblick

Die Campaigns-Capability stellt einen Kampagnen-Katalog-Endpunkt bereit und erweitert
das `NotifyRequest`-Objekt um ein `campaignId`-Feld. Kampagnen ermöglichen die
Verknüpfung von Buchungs-Benachrichtigungen mit spezifischen Marketing-Kampagnen oder
Aktionszeiträumen.

---

## Campaign-Objekt (Schema)

```typescript
interface Campaign {
  id: string;           // Kampagnen-ID (z.B. "campaign_spring_2026")
  title?: string;       // Bezeichnung der Kampagne
  description?: string; // Beschreibung
  active?: boolean;     // Kampagne aktiv?
}
```

---

## NotifyRequest-Erweiterung

Das `campaignId`-Feld wird dem `NotifyRequest`-Objekt hinzugefügt, das bei
Benachrichtigungs-Endpunkten verwendet wird:

```typescript
interface NotifyRequest {
  // ... Standard-Benachrichtigungsfelder ...
  campaignId?: string;  // Optional — Kampagnen-ID (z.B. "campaign_spring_2026")
}
```

---

## Endpunkte

### GET /campaigns — Kampagnen-Katalog abrufen

Gibt alle verfügbaren Kampagnen der authentifizierten Verbindung zurück.

```bash
curl "https://api.ventrata.com/octo/campaigns" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/campaigns"
```

**Response:** Array von Campaign-Objekten (Status 200)

```json
[
  {
    "id": "campaign_spring_2026",
    "title": "Spring Special 2026",
    "description": "Sonderangebote für den Frühling 2026",
    "active": true
  },
  {
    "id": "campaign_summer_earlybird",
    "title": "Sommer Early Bird",
    "description": "Frühbucherrabatt Sommer",
    "active": true
  }
]
```

---

## campaignId in Benachrichtigungen nutzen

Das `campaignId`-Feld kann bei den Notify-Endpunkten angegeben werden:

### POST /bookings/{uuid}/notify — mit Kampagne

```bash
curl -X POST "https://api.ventrata.com/octo/bookings/{uuid}/notify" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/campaigns" \
  -H "Content-Type: application/json" \
  -d '{
    "campaignId": "campaign_spring_2026"
  }'
```

**Response:** `200 OK` mit leerem Body

---

### POST /orders/{orderId}/notify — mit Kampagne (mit octo/cart)

```bash
curl -X POST "https://api.ventrata.com/octo/orders/{orderId}/notify" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/campaigns, octo/cart" \
  -H "Content-Type: application/json" \
  -d '{
    "campaignId": "campaign_summer_earlybird"
  }'
```

---

### POST /gifts/{uuid}/notify — mit Kampagne (mit octo/gifts)

```bash
curl -X POST "https://api.ventrata.com/octo/gifts/{uuid}/notify" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/campaigns, octo/gifts" \
  -H "Content-Type: application/json" \
  -d '{
    "campaignId": "campaign_spring_2026"
  }'
```

---

## Kampagnen-ID-Format

Kampagnen-IDs sind Freitextbezeichner (keine UUIDs). Beispiele:

| Kampagnen-ID | Typ |
|-------------|-----|
| `"campaign_spring_2026"` | Saisonale Kampagne |
| `"campaign_summer_earlybird"` | Frühbucher-Aktion |
| `"campaign_member_exclusive"` | Mitglieder-exklusiv |

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `CAMPAIGN_NOT_FOUND` | 404 | Kampagne mit angegebener ID nicht gefunden |
| `CAMPAIGN_INACTIVE` | 400 | Kampagne ist nicht mehr aktiv |

---

## Hinweise zur Vollständigkeit

Die öffentliche Dokumentation beschreibt den `GET /campaigns`-Endpunkt und die
`NotifyRequest`-Erweiterung. Vollständige Request/Response-Schemas für den Kampagnen-
Endpunkt sind in der referenzierten OpenAPI-Spezifikation enthalten. Weitere
Kampagnen-Verwaltungsendpunkte (POST, PATCH, DELETE) sind ggf. vorhanden.

---

## Capability-Abhängigkeiten

| Verwendet mit | Zweck |
|--------------|-------|
| `octo/cart` | `campaignId` in Order-Benachrichtigungen |
| `octo/gifts` | `campaignId` in Gift-Benachrichtigungen |
| `octo/notifications` | Subscription-basierte Benachrichtigungen |

---

*Quelle: https://docs.ventrata.com/capabilities/campaigns*
