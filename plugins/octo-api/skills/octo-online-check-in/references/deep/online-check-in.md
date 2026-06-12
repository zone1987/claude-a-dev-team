# OCTO — Online Check-in Capability (`octo/checkin`)

## Capability-Identifier

```
octo/checkin
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/checkin
Content-Type: application/json
```

---

## Überblick

Die Online-Check-in-Capability erweitert Buchungen und Orders um Check-in-Felder und
stellt einen Lookup-Endpunkt bereit, über den Gäste anhand ihrer E-Mail-Adresse,
Mobilnummer oder Buchungsreferenz nachgeschlagen werden können. Optional kann ein
6-stelliger Verifikationscode oder der Nachname des Gastes zur Authentifizierung
angegeben werden.

---

## Schema-Erweiterungen am Booking-Objekt

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `checkedIn` | boolean | Ist der Gast bereits eingecheckt? |
| `checkinAvailable` | boolean | Kann der Gast jetzt einchecken? |
| `checkinUrl` | string \| null | URL zum Online-Check-in-Portal |

**Beispiel:**
```json
{
  "uuid": "a1b2c3d4-...",
  "status": "CONFIRMED",
  "checkedIn": false,
  "checkinAvailable": true,
  "checkinUrl": "https://checkin.city-sightseeing.com/booking/a1b2c3d4"
}
```

---

## Booking-Status-Werte für Check-in

Vollständige Liste der Status-Werte, die bei Lookup gefiltert werden können:

| Status | Bedeutung |
|--------|-----------|
| `CONFIRMED` | Buchung bestätigt |
| `ON_HOLD` | Reserviert, noch nicht bestätigt |
| `PENDING` | In Bearbeitung |
| `CANCELLED` | Storniert |
| `REDEEMED` | Bereits eingelöst/eingecheckt |
| `NO_SHOW` | Nicht erschienen |
| `EXPIRED` | Abgelaufen |
| `REJECTED` | Abgelehnt |
| `REBOOKED` | Umgebucht |
| `QUOTE` | Angebot (noch keine Buchung) |

> **Hinweis:** Bei Gift-Lookups werden `PENDING`, `REJECTED` und `REBOOKED` ausgeschlossen.

---

## Endpunkte

### POST /checkin/lookup — Buchung nachschlagen

**Mindestens eines der folgenden Felder ist Pflicht:** `email`, `mobile` oder `reference`

**Request Body:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `email` | string | bedingt | E-Mail-Adresse des Gastes |
| `mobile` | string | bedingt | Mobilnummer des Gastes |
| `reference` | string | bedingt | Buchungsreferenz (mind. 3 Zeichen, außer UUID-Format) |
| `verification` | string | optional | 6-stelliger Code (bei email/mobile) oder Nachname (bei reference) |
| `status` | enum | optional | Einzelner Status-Filter |
| `statuses` | enum[] | optional | Mehrere Status-Filter (wird ignoriert wenn `status` gesetzt) |
| `identityId` | string | optional | Filter per Identity-ID (mit `octo/identities`) |

```bash
# Suche per E-Mail
curl -X POST https://api.ventrata.com/octo/checkin/lookup \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/checkin" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "max@example.com",
    "verification": "123456",
    "statuses": ["CONFIRMED", "ON_HOLD"]
  }'

# Suche per Referenz (Nachname als Verifikation)
curl -X POST https://api.ventrata.com/octo/checkin/lookup \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/checkin" \
  -H "Content-Type: application/json" \
  -d '{
    "reference": "BOOK-2026-00123",
    "verification": "Mustermann"
  }'
```

**Response:** Array von Booking-Objekten mit Check-in-Feldern

**Fehler:** `BOOKING_NOT_FOUND` (400) wenn keine Buchung gefunden

---

### GET /bookings/{uuid} — Buchung mit Check-in-Feldern abrufen

Ergänzt die Standard-Booking-Response um die Check-in-Felder.

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `uuid` | string (UUID) | ja | Buchungs-UUID |

```bash
curl "https://api.ventrata.com/octo/bookings/a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/checkin"
```

---

### GET /gifts/{uuid} — Gift mit Check-in-Feldern abrufen

Ergänzt die Standard-Gift-Response (erfordert auch `octo/gifts`) um Check-in-Felder.

---

### GET /orders/{orderId} — Order mit Check-in-Feldern abrufen

Order-Response enthält `order.bookings[]` mit Check-in-Feldern an jeder Buchung.
Erfordert auch `octo/cart`.

---

### GET /products — Produkte (unverändert)

Kein zusätzliches Feld durch `octo/checkin`.

---

## Query-Parameter bei GET-Requests (Checkin-Kontext)

Bei GET-Anfragen kann der Check-in-Kontext als Query-Parameter mitgegeben werden:

```
GET /bookings?checkin[email]=max@example.com&checkin[verification]=123456
GET /bookings?checkin[mobile]=+4917612345678
GET /bookings?checkin[reference]=BOOK-2026-00123&checkin[verification]=Mustermann
```

---

## Verifikations-Logik

| Suchfeld | Verifikationsmethode | Verifikationswert |
|----------|---------------------|-------------------|
| `email` | 6-stelliger Code per E-Mail | `verification` = "123456" |
| `mobile` | 6-stelliger Code per SMS | `verification` = "123456" |
| `reference` | Nachname des Gastes | `verification` = "Mustermann" |

Wird `verification` weggelassen, erfolgt kein Zwei-Faktor-Check (implementierungs-
abhängig ob dies erlaubt ist).

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `BOOKING_NOT_FOUND` | 400 | Keine Buchung zur Suchanfrage gefunden |
| `CHECKIN_INVALID_REFERENCE` | 400 | Referenz zu kurz (< 3 Zeichen, kein UUID) |
| `CHECKIN_INVALID_VERIFICATION` | 400 | Verifikationscode oder Nachname falsch |

---

## Integration mit anderen Capabilities

| Capability | Zusammenspiel |
|-----------|---------------|
| `octo/cart` | Order-Response enthält Check-in-Felder in `order.bookings[]` |
| `octo/gifts` | Gift-Response erhält Check-in-Felder analog zu Bookings |
| `octo/identities` | `identityId` als zusätzlicher Lookup-Filter |

---

*Quelle: https://docs.ventrata.com/capabilities/online-check-in*
