# OCTO API — Vollständige HTTP-Header-Referenz

## Basis-URL

```
https://api.ventrata.com/octo
```

---

## Request-Header

### Authorization (Pflicht — alle Endpunkte)

```
Authorization: Bearer {api_key}
```

- **Format:** Bearer-Token (UUID-Format, z.B. `5bd1629a-323e-4edb-ac9b-327ef51e6136`)
- **Pflicht:** Ja — alle Anfragen
- **Fehler ohne Header:** `403 Forbidden` mit Error `UNAUTHORIZED`
- **Wichtig:** Jeder API-Key gewährt Zugriff auf genau einen Supplier; für mehrere Supplier sind separate Keys nötig
- **HTTPS-Pflicht:** Alle Anfragen müssen HTTPS verwenden; HTTP-Calls schlagen fehl
- **Sicherheitshinweis:** API-Keys verantwortlich schützen. Bei Kompromittierung: Supplier kontaktieren, um Connection zu löschen und neu zu erstellen, oder connectivity@ventrata.com

---

### Content-Type (Pflicht für POST, PATCH, DELETE)

```
Content-Type: application/json
```

- **Gilt für:** POST, PATCH, DELETE Anfragen
- **Wert:** Immer `application/json`
- **Nicht nötig:** Bei GET-Anfragen

---

### Octo-Capabilities (Pflicht — alle Endpunkte außer /capabilities)

```
Octo-Capabilities: octo/pricing,octo/content
```

- **Format:** Kommagetrennte Liste von Capability-IDs
- **Pflicht:** Ja — das Weglassen dieses Headers gibt einen `400 Bad Request`-Fehler zurück
- **Leer lassen:** Header muss vorhanden sein, kann aber leer sein wenn keine Capabilities benötigt: `Octo-Capabilities: `
- **Zweck:** Gibt an, welche optionalen Datenfelder in der Response enthalten sein sollen
- **Legacy-Alternative:** `X-Capabilities` (veraltet)

**Verfügbare Capability-IDs:**

| Capability | Beschreibung |
|-----------|-------------|
| `octo/pricing` | Preisfelder in Products/Availability/Bookings |
| `octo/content` | Erweiterte Inhaltsfelder (title, description, media, etc.) |
| `octo/offers` | Supplier-Angebote und angebotsbewusste Responses |
| `octo/extras` | Extra-Upsell-Inventar |
| `octo/packages` | Package-Buchungsflows |
| `octo/pickups` | Pickup/Dropoff-Felder |
| `octo/questions` | Frage-Schemas |
| `octo/waivers` | Haftungsausschluss-Vorlagen |
| `octo/resources` | Availability-Ressourcen |
| `octo/rentals` | Miet-Dauer-IDs |
| `octo/redemption` | Einlöse-Flows |
| `octo/mappings` | Self-Service Mapping |
| `octo/cart` | Order-Flows |
| `octo/gifts` | Gift-Voucher-Flows |
| `octo/checkin` | Check-in-Felder |
| `octo/cardPayments` | Kartenzahlung |
| `octo/memberships` | Mitgliedschaften |
| `octo/adjustments` | Preisanpassungen |
| `octo/webhooks` | Webhook-Management |
| `octo/waitlists` | Wartelisten |
| `octo/identities` | Identitätsverwaltung |
| `octo/campaigns` | Kampagnen |
| `octo/notifications` | Benachrichtigungsabonnements |

---

### Octo-Env (Empfohlen)

```
Octo-Env: test
```

oder

```
Octo-Env: live
```

- **Werte:** `test` oder `live`
- **Zweck:** Markiert Buchungen mit Live-Credentials als Testverkäufe in Ventrata
- **`test`-Modus-Effekte:**
  - Verbraucht keine Verfügbarkeit
  - Barcodes funktionieren nicht
  - Keine Rechnungsstellung
- **Standard:** `test` für Tests verwenden; `live` für echte Buchungen

---

### Accept-Language (Optional)

```
Accept-Language: fr
Accept-Language: en-US,fr-CA;q=0.8,fr;q=0.7
```

- **Format:** Standard HTTP BCP 47 Language Tags (RFC 5646/RFC 4647)
- **Pflicht:** Nein
- **Beispielwerte:** `de`, `en-US`, `fr-FR`, `es-ES`
- **Kommagetrennte Liste:** Mit optionalen Qualitätswerten (q)
- **Verhalten:** Gibt Inhalte in der angegebenen Sprache zurück wenn verfügbar; Fehlermeldungen werden ebenfalls übersetzt
- **Fallback:** Englisch wenn die gewünschte Sprache nicht verfügbar

---

## Response-Header

### Content-Type

```
Content-Type: application/json
```

Alle Endpunkte geben JSON zurück.

---

### Octo-Capabilities

```
Octo-Capabilities: octo/pricing,octo/content
```

Spiegelt die im Request angeforderten und tatsächlich angewendeten Capabilities zurück.

---

### Octo-Env

```
Octo-Env: test
```

oder

```
Octo-Env: live
```

Gibt den tatsächlichen Modus zurück basierend auf Request und Supplier-Einstellungen.

---

### Content-Language

```
Content-Language: de
```

Zeigt die tatsächlich zurückgegebene Inhaltssprache an (gemäß HTTP-Standard).

---

### Octo-Available-Languages

```
Octo-Available-Languages: en,de,fr,es
```

Listet alle Sprachen auf, in die der Supplier seinen Inhalt übersetzt hat. Nützlich für Caching-Strategien: Für jede Sprache separate Anfragen stellen.

---

## Vollständiges Anfrage-Beispiel

```http
GET https://api.ventrata.com/octo/products/
Authorization: Bearer 5bd1629a-323e-4edb-ac9b-327ef51e6136
Octo-Capabilities: octo/pricing,octo/content
Octo-Env: test
Accept-Language: de
```

```http
POST https://api.ventrata.com/octo/bookings/
Authorization: Bearer 5bd1629a-323e-4edb-ac9b-327ef51e6136
Content-Type: application/json
Octo-Capabilities: octo/pricing
Octo-Env: test

{
  "productId": "...",
  "optionId": "...",
  "availabilityId": "...",
  "unitItems": [...]
}
```

---

**Quellen:**
- https://docs.ventrata.com/getting-started/headers
- https://docs.ventrata.com/getting-started/getting-started
- https://docs.ventrata.com/getting-started/test-credentials
