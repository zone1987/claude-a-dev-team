# OCTO — Gift Vouchers Capability (`octo/gifts`)

## Capability-Identifier

```
octo/gifts
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/gifts
Content-Type: application/json
```

---

## Überblick

Die Gift-Vouchers-Capability ermöglicht die Erstellung, Verwaltung und Einlösung
von Geschenkgutscheinen. Gutscheine können direkt oder als Teil einer Order
(`octo/cart`) verwendet werden. Beim Bestätigen einer Buchung/Order kann ein
Gutscheincode als Zahlungsmittel (`giftPayment`) angegeben werden.

---

## Gift-Objekt (vollständiges Schema)

```typescript
interface Gift {
  uuid: string;                     // Primärer Identifier (UUID)
  id: string;                       // Interner Identifier
  status: GiftStatus;               // Aktueller Status
  currency: string;                 // ISO 4217 Währungscode
  amount: number;                   // Gutscheinwert in kleinster Einheit
  availableAmount: number;          // Noch verfügbarer Betrag
  updatable: boolean;               // Änderung erlaubt?
  cancellable: boolean;             // Stornierung erlaubt?
  voucher: GiftVoucher;             // Voucher-Details
  contact: Contact | null;          // Empfänger-Kontakt
  supplierReference: string | null; // Supplier-Referenz
  resellerReference: string | null; // Reseller-Referenz
  createdAt: string;                // ISO 8601 Erstellungszeitpunkt
  updatedAt: string;                // ISO 8601 letzter Update

  // Mit octo/cart:
  orderId?: string;                 // Übergeordnete Order-ID
  orderReference?: string;          // Menschenlesbare Order-Referenz
  orderInvoicePdfUrl?: string | null; // Rechnungs-PDF-URL
  primary?: boolean;                // Primärer Gutschein der Order
}

type GiftStatus = "CONFIRMED" | "REDEEMED" | "CANCELLED" | "EXPIRED";

interface GiftVoucher {
  deliveryOptions: GiftDeliveryOption[]; // Verfügbare Lieferformate
  deliveryValue: string;                  // Code (QRCODE) oder URL (andere)
}

type GiftDeliveryOption = "QRCODE" | "PDF" | "PNG" | "PKPASS" | "GOOGLE_WALLET";
```

---

## GiftPayment-Objekt

Das `giftPayment`-Objekt wird in Order-/Booking-Requests verwendet, um einen
Gutschein als Zahlungsmittel einzusetzen:

```typescript
interface GiftPaymentRequest {
  code: string; // Einlösecode des Gutscheins (Pflicht)
}

interface GiftPayment {  // In Responses
  giftCode: string;   // Anzeige-Code (z.B. "GIFT-2026-0001")
  code: string;       // Technischer Einlösecode
  amount: number;     // Eingelöster Betrag in kleinster Einheit
  currency: string;   // ISO 4217 Währungscode
}
```

---

## Endpunkte

Alle Pfade sind öffentliche `/octo`-Routen.

### POST /gifts — Geschenkgutschein erstellen

**Request Body:**

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `uuid` | string (UUID) | optional | Idempotenz-UUID (Wiederholung bei schlechter Verbindung) |
| `amount` | number | ja | Gutscheinwert in kleinster Währungseinheit |
| `currency` | string | ja | ISO 4217 Währungscode |
| `contact` | Contact | optional | Empfänger-Kontakt |
| `resellerReference` | string | optional | Eigene Referenz |
| `orderId` | string | optional | Order-Zuordnung (mit `octo/cart`) |

```bash
curl -X POST https://api.ventrata.com/octo/gifts \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/gifts" \
  -H "Content-Type: application/json" \
  -d '{
    "uuid": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "amount": 5000,
    "currency": "EUR",
    "contact": {
      "fullName": "Anna Musterfrau",
      "emailAddress": "anna@example.com"
    },
    "resellerReference": "GIFT-RESELLER-001"
  }'
```

**Response:** Gift-Objekt (Status 200)

---

### PATCH /gifts/{uuid} — Geschenkgutschein aktualisieren

**Nur erlaubt wenn `gift.updatable === true` und Gutschein nicht eingelöst.**

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `uuid` | string (UUID) | ja | Gift-UUID |

**Request Body (alle optional):**

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `contact` | Contact | Aktualisierter Empfänger-Kontakt |
| `resellerReference` | string | Neue Reseller-Referenz |

---

### PATCH /gifts/{uuid}/preview — Änderungen vorschauen

Identische Parameter wie `PATCH /gifts/{uuid}`, schreibt jedoch nichts.

---

### POST /gifts/{uuid}/confirm — Gutschein bestätigen

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `uuid` | string (UUID) | ja | Gift-UUID |

```bash
curl -X POST "https://api.ventrata.com/octo/gifts/f47ac10b-58cc-4372-a567-0e02b2c3d479/confirm" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/gifts" \
  -H "Content-Type: application/json" \
  -d '{}'
```

**Response:** Bestätigtes Gift-Objekt mit Delivery-URL

---

### DELETE /gifts/{uuid} — Gutschein löschen

**Response:** Gelöschtes Gift-Objekt

---

### POST /gifts/{uuid}/cancel — Gutschein stornieren

**Nur erlaubt wenn `gift.cancellable === true`.**

**Response:** Storniertes Gift-Objekt

---

### POST /gifts/{uuid}/extend — Gutschein verlängern

Verlängert die Gültigkeit des Gutscheins.

**Response:** Aktualisiertes Gift-Objekt

---

### GET /gifts/{uuid} — Einzelnen Gutschein abrufen

```bash
curl "https://api.ventrata.com/octo/gifts/f47ac10b-58cc-4372-a567-0e02b2c3d479" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/gifts"
```

**Response:** Gift-Objekt

---

### GET /gifts — Gutscheine auflisten

**Mindestens einer der folgenden Filter ist Pflicht:**

| Query-Parameter | Typ | Beschreibung |
|-----------------|-----|--------------|
| `resellerReference` | string | Nach Reseller-Referenz filtern |
| `supplierReference` | string | Nach Supplier-Referenz filtern |
| `utcCreatedAtStart` | ISO 8601 | Erstellt ab (UTC) |
| `utcCreatedAtEnd` | ISO 8601 | Erstellt bis (UTC) |
| `utcUpdatedAtStart` | ISO 8601 | Aktualisiert ab (UTC) |
| `utcUpdatedAtEnd` | ISO 8601 | Aktualisiert bis (UTC) |
| `contactEmailAddress` | string | Nach E-Mail-Adresse filtern |

**Fehler bei fehlendem Filter:** `GIFTS_FIELDS_REQUIRED`

**Response:** Array von Gift-Objekten

---

### POST /gifts/{uuid}/notify — Benachrichtigung senden

Sendet Delivery-URL/Code an den Empfänger.

**Response:** `200 OK` mit leerem Body

---

## Gift als Zahlungsmittel nutzen

Das `giftPayment`-Objekt kann in folgenden Requests angegeben werden:

- `POST /bookings/{uuid}/confirm` — Buchungsbestätigung
- `POST /orders/{orderId}/confirm` — Order-Bestätigung (mit `octo/cart`)
- `POST /gifts/{uuid}/confirm` — Gift-Bestätigung

```bash
curl -X POST "https://api.ventrata.com/octo/bookings/{uuid}/confirm" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/gifts" \
  -H "Content-Type: application/json" \
  -d '{
    "giftPayment": {
      "code": "GIFT-2026-0001-REDEEM"
    }
  }'
```

---

## Erweiterungen an Booking/Order-Responses

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `gifts` | Gift[] | Enthaltene Gutscheine (bei Orders) |
| `giftPayment` | GiftPayment \| null | Eingelöste Gutschein-Zahlung |

---

## Validierungsregeln

| Regel | Fehler |
|-------|--------|
| Gift-Währung muss mit Order-Währung übereinstimmen | `GIFT_CURRENCY_MISMATCH` |
| Gutschein muss ausreichend Guthaben haben | `GIFT_INSUFFICIENT_BALANCE` |
| Leerer `code` in `giftPayment` → vorhandene Transaktionen werden storniert | — |
| Stornierung nur wenn `gift.cancellable === true` | `GIFT_NOT_CANCELLABLE` |
| Update nur wenn `gift.updatable === true` und nicht eingelöst | `GIFT_NOT_UPDATABLE` |

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `GIFTS_FIELDS_REQUIRED` | 400 | Kein Filter bei GET /gifts angegeben |
| `GIFT_NOT_FOUND` | 404 | Gift mit UUID nicht gefunden |
| `GIFT_NOT_CANCELLABLE` | 409 | Stornierung nicht erlaubt |
| `GIFT_NOT_UPDATABLE` | 409 | Update nicht erlaubt |
| `GIFT_CURRENCY_MISMATCH` | 400 | Währung stimmt nicht überein |
| `GIFT_INSUFFICIENT_BALANCE` | 400 | Zu wenig Guthaben |

---

*Quelle: https://docs.ventrata.com/capabilities/gift-vouchers*
