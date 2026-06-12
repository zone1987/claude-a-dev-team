# OCTO — Memberships Capability (`octo/memberships`)

## Capability-Identifier

```
octo/memberships
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/memberships
Content-Type: application/json
```

---

## Überblick

Die Memberships-Capability ermöglicht die Verwaltung von Mitgliedschaften. Mitglieder
können per E-Mail, Mobilnummer oder Referenznummer nachgeschlagen werden. Die Capability
erweitert Unit-, Produkt- und Offer-Objekte um Mitgliedschafts-Metadaten und erlaubt
die Zuweisung von Mitgliedschafts-Vorteilen bei Buchungen.

---

## Membership-Objekt (vollständiges Schema)

```typescript
interface Membership {
  id: string;                         // UUID der Mitgliedschaft
  title: string;                      // Bezeichnung der Mitgliedschaft
  contact: MembershipContact;         // Kontaktdaten des Mitglieds
  reference: string;                  // Membership-Referenz
  resellerReference: string | null;   // Reseller-Referenz
  supplierReference: string | null;   // Supplier-Referenz
  availabilityLocalDateStart: string; // Gültig ab (ISO-Datum, z.B. "2026-01-01")
  availabilityLocalDateEnd: string;   // Gültig bis (ISO-Datum, z.B. "2026-12-31")
}

interface MembershipContact {
  firstName: string;
  lastName: string;
  emailAddress: string | null;
  phoneNumber: string | null;
  country: string | null;   // ISO 3166-1 Alpha-2 Ländercode
}
```

---

## Schema-Erweiterungen

### Unit-Erweiterungen (GET /products, GET /products/{productId})

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `isMembership` | boolean | Dieses Unit repräsentiert eine Mitgliedschaft |
| `membershipBenefit` | MembershipBenefit \| null | Mitgliedschafts-Vorteil (null für normale Units) |

```typescript
interface MembershipBenefit {
  id: string;
  title: string;
  description: string;
}
```

### Produkt-Erweiterungen (GET /products, GET /products/{productId})

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `isMembership` | boolean | Dieses Produkt ist eine Mitgliedschaft |
| `membershipAutoRenew` | boolean | Automatische Verlängerung aktiviert |

### Offer-Erweiterungen (innerhalb von Produkt-Responses)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `membershipBenefit` | MembershipBenefit \| null | Vorteil für Mitglieds-Angebote |

---

## Membership-Request-Objekt

Das `membership`-Objekt kann in folgenden Requests verwendet werden:
- `POST /availability`
- `POST /bookings`
- `PATCH /bookings/{uuid}`
- `POST /bookings/{uuid}/confirm`
- `POST /orders` / `PATCH /orders/{orderId}` (mit `octo/cart`)
- `POST /gifts` (mit `octo/gifts`)

```typescript
interface MembershipRequest {
  id: string;             // UUID der Mitgliedschaft (Pflicht)
  email?: string;         // E-Mail-Adresse (eines von email/mobile/reference Pflicht)
  mobile?: string;        // Mobilnummer
  reference?: string;     // Membership-Referenz (mind. 3 Zeichen)
  verification: string;   // Pflicht: 6-stelliger Code (email/mobile) oder Nachname (reference)
  country?: string;       // Pflicht wenn mobile angegeben (ISO 3166-1 Alpha-2)
}
```

**Zusätzliches Feld in Booking/Order-Requests:**

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `appendMembershipValidity` | boolean | Mitgliedschaftsgültigkeit an Buchung anhängen |

---

## Endpunkte

### POST /memberships/lookup — Mitglied nachschlagen

Initiiert die Mitglieder-Verifikation. Löst je nach Suchmethode die Versendung
eines Verifikationscodes aus.

**Request Body — mindestens eines ist Pflicht:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `email` | string | bedingt | E-Mail-Adresse → 6-stelliger Code per E-Mail |
| `mobile` | string | bedingt | Mobilnummer → 6-stelliger Code per SMS |
| `reference` | string | bedingt | Membership-Referenz (min. 3 Zeichen) → Nachname-Verifikation |
| `verification` | string | optional | Verifikationscode oder Nachname |
| `country` | string | bedingt | ISO-Ländercode (Pflicht bei `mobile`) |

```bash
# Lookup per E-Mail (löst Code-Versendung aus)
curl -X POST https://api.ventrata.com/octo/memberships/lookup \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/memberships" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "mitglied@example.com"
  }'

# Lookup per E-Mail mit Verifikation
curl -X POST https://api.ventrata.com/octo/memberships/lookup \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/memberships" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "mitglied@example.com",
    "verification": "482931"
  }'
```

**Response (200 OK):** Array von Membership-Objekten

**Fehler (400):** Kein Mitglied gefunden

---

### GET /memberships/bookings — Mitgliedschafts-Buchungen abrufen

Gibt alle Buchungen zurück, die einer verifizierten Mitgliedschaft zugeordnet sind.

**Query-Parameter (alle Pflicht):**

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `membership[id]` | UUID | ID der Mitgliedschaft |
| `membership[email]` ODER `membership[mobile]` ODER `membership[reference]` | string | Suchkriterium |
| `membership[verification]` | string | Verifikationscode oder Nachname |
| `membership[country]` | string | ISO-Ländercode (Pflicht bei mobile) |

```bash
curl "https://api.ventrata.com/octo/memberships/bookings\
?membership[id]=a1b2c3d4-e5f6-7890-abcd-ef1234567890\
&membership[email]=mitglied@example.com\
&membership[verification]=482931" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/memberships"
```

**Response:** Array von Booking-Objekten

---

## Mitgliedschafts-Buchung anlegen

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/memberships" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_stadtfuehrung",
    "optionId": "default",
    "availabilityId": "2026-06-15T10:00:00+02:00",
    "unitItems": [
      { "unitId": "unit_erwachsener" }
    ],
    "membership": {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "email": "mitglied@example.com",
      "verification": "482931"
    },
    "appendMembershipValidity": true
  }'
```

---

## Verifikations-Logik

| Suchmethode | Aktion beim Lookup | Verifikationswert |
|------------|-------------------|-------------------|
| `email` | 6-stelliger Code per E-Mail | `verification` = "482931" |
| `mobile` | 6-stelliger Code per SMS | `verification` = "482931" |
| `reference` | Kein Code-Versand | `verification` = Nachname |

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `MEMBERSHIP_NOT_FOUND` | 400 | Kein Mitglied zur Suchanfrage gefunden |
| `MEMBERSHIP_INVALID_VERIFICATION` | 400 | Verifikationscode oder Nachname falsch |
| `MEMBERSHIP_EXPIRED` | 400 | Mitgliedschaft abgelaufen |
| `MEMBERSHIP_INVALID_COUNTRY` | 400 | Ländercode fehlt oder ungültig (bei mobile) |

---

## Capability-Abhängigkeiten

| Verwendet mit | Zweck |
|--------------|-------|
| `octo/cart` | Membership-Kontext in Orders |
| `octo/gifts` | Membership-Kontext in Geschenkgutscheinen |
| `octo/pricing` | Mitgliedschafts-Preise auf Units |

---

*Quelle: https://docs.ventrata.com/capabilities/memberships*
