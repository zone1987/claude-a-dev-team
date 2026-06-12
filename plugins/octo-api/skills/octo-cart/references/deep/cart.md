# OCTO — Multi-Booking Cart Capability (`octo/cart`)

## Capability-Identifier

```
octo/cart
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/cart
Content-Type: application/json
```

---

## Überblick

Die Cart-Capability ermöglicht es, mehrere Buchungen und Geschenkgutscheine in einer
einzigen **Order** zu bündeln. Orders werden gemeinsam bestätigt, storniert und
in Rechnung gestellt. Ohne explizite `orderId` im Request wird automatisch eine
neue Order erzeugt und deren ID in der Response zurückgegeben.

---

## Schema-Erweiterungen

### Booking (Response-Erweiterungen)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `orderId` | string | ID der übergeordneten Order |
| `orderReference` | string | Menschenlesbare Order-Referenz |
| `orderInvoicePdfUrl` | string \| null | URL zur Rechnungs-PDF |
| `primary` | boolean | Primäre Buchung der Order |

### BookingWriteRequest (Request-Erweiterungen)

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `orderId` | string | optional | Bestehende Order referenzieren |

### Gift (Response-Erweiterungen)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `orderId` | string | ID der übergeordneten Order |
| `orderReference` | string | Menschenlesbare Order-Referenz |
| `orderInvoicePdfUrl` | string \| null | URL zur Rechnungs-PDF |
| `primary` | boolean | Primärer Gutschein der Order |

### GiftCreateRequest (Request-Erweiterungen)

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `orderId` | string | optional | Bestehende Order referenzieren |

### Error (Response-Erweiterung)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `orderId` | string | Betroffene Order-ID im Fehlerkontext |

---

## Order-Objekt (vollständiges Schema)

```typescript
interface Order {
  id: string;                    // UUID der Order
  status: OrderStatus;           // Aktueller Status
  reference: string;             // Menschenlesbare Referenz
  invoicePdfUrl: string | null;  // URL zur Rechnungs-PDF
  bookings: Booking[];           // Enthaltene Buchungen
  gifts: Gift[];                 // Enthaltene Geschenkgutscheine
  contact: Contact;              // Primärer Kontakt
  currency: string;              // ISO 4217 Währungscode
  totalAmount: number;           // Gesamtbetrag in kleinster Einheit
  totalPaid: number;             // Bereits bezahlter Betrag
  createdAt: string;             // ISO 8601 Erstellungszeitpunkt
  updatedAt: string;             // ISO 8601 letzter Updatezeitpunkt
}

type OrderStatus = "ACTIVE" | "EXPIRED" | "CANCELLED" | "CONFIRMED";
```

---

## Endpunkte

Alle Pfade sind öffentliche `/octo`-Routen.

### POST /orders — Order erstellen

**Request Body (alle Felder optional):**

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `resellerReference` | string | Eigene Referenz des Resellers |
| `contact` | Contact | Kontaktinformationen |
| `currency` | string | Gewünschte Währung (ISO 4217) |

**Response:** Order-Objekt (Status 200)

```bash
curl -X POST https://api.ventrata.com/octo/orders \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/cart" \
  -H "Content-Type: application/json" \
  -d '{
    "resellerReference": "ORDER-2026-001",
    "contact": {
      "fullName": "Max Mustermann",
      "emailAddress": "max@example.com"
    },
    "currency": "EUR"
  }'
```

---

### GET /orders — Orders abrufen

**Mindestens ein Filter-Parameter ist Pflicht:**

| Query-Parameter | Typ | Beschreibung |
|-----------------|-----|--------------|
| `resellerReference` | string | Filtern nach Reseller-Referenz |
| `supplierReference` | string | Filtern nach Supplier-Referenz |
| `utcCreatedAtStart` | ISO 8601 | Erstellt ab (UTC) |
| `utcCreatedAtEnd` | ISO 8601 | Erstellt bis (UTC) |
| `utcUpdatedAtStart` | ISO 8601 | Aktualisiert ab (UTC) |
| `utcUpdatedAtEnd` | ISO 8601 | Aktualisiert bis (UTC) |

**Fehler bei fehlendem Filter:** `ORDERS_FIELDS_REQUIRED`

**Response:** Array von Order-Objekten

```bash
curl "https://api.ventrata.com/octo/orders?resellerReference=ORDER-2026-001" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/cart"
```

---

### GET /orders/{orderId} — Einzelne Order abrufen

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `orderId` | string (UUID) | ja | ID der Order |

**Response:** Order-Objekt

```bash
curl "https://api.ventrata.com/octo/orders/a1b2c3d4-e5f6-7890-abcd-ef1234567890" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/cart"
```

---

### PATCH /orders/{orderId} — Order aktualisieren

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `orderId` | string (UUID) | ja | ID der Order |

**Request Body (alle optional):**

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `resellerReference` | string | Neue Reseller-Referenz |
| `contact` | Contact | Aktualisierte Kontaktdaten |

**Response:** Aktualisiertes Order-Objekt

---

### PATCH /orders/{orderId}/preview — Order-Änderungen vorschauen

Identische Parameter wie `PATCH /orders/{orderId}`, schreibt jedoch nichts. Gibt das
Order-Objekt zurück, wie es nach dem Update aussehen würde.

---

### POST /orders/{orderId}/extend — Order verlängern

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `orderId` | string (UUID) | ja | ID der Order |

Verlängert die Ablaufzeit der Order. Request Body ist leer oder nicht erforderlich.

**Response:** Aktualisiertes Order-Objekt

---

### POST /orders/{orderId}/confirm — Order bestätigen

Bestätigt die Order und **alle** enthaltenen Buchungen/Geschenkgutscheine in einem
einzigen Aufruf.

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `orderId` | string (UUID) | ja | ID der Order |

**Request Body (optional):**

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `contact` | Contact | Kontaktdaten (falls noch nicht gesetzt) |
| `cardPayment` | CardPaymentRequest | Zahlungsinformationen (mit `octo/cardPayments`) |
| `giftPayment` | GiftPaymentRequest | Geschenkgutschein-Einlösung (mit `octo/gifts`) |

```bash
curl -X POST "https://api.ventrata.com/octo/orders/a1b2c3d4-e5f6-7890-abcd-ef1234567890/confirm" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/cart" \
  -H "Content-Type: application/json" \
  -d '{
    "contact": {
      "fullName": "Max Mustermann",
      "emailAddress": "max@example.com",
      "phoneNumber": "+49123456789"
    }
  }'
```

**Response:** Bestätigtes Order-Objekt mit Status `CONFIRMED`

---

### DELETE /orders/{orderId} — Order stornieren

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `orderId` | string (UUID) | ja | ID der Order |

Storniert die Order und alle enthaltenen Buchungen.

**Response:** Storniertes Order-Objekt mit Status `CANCELLED`

---

### POST /orders/{orderId}/cancel — Order stornieren (alternativ)

Identisch mit `DELETE /orders/{orderId}`. Ermöglicht Stornierung via POST
für Systeme, die DELETE nicht unterstützen.

**Response:** Storniertes Order-Objekt

---

### POST /orders/{orderId}/notify — Benachrichtigung senden

Sendet eine Buchungsbestätigungs-E-Mail oder ähnliche Benachrichtigung.

**Response:** `200 OK` mit leerem Body

---

## Wichtige Verhaltensregeln

1. **Auto-Order-Erstellung:** Wird `orderId` beim Anlegen einer Buchung weggelassen,
   erstellt die API automatisch eine neue Order. Die neue `orderId` erscheint in der
   Booking-Response.
2. **resellerReference:** Muss über den Booking-Update-Endpunkt gesetzt werden, nicht
   auf Order-Ebene direkt.
3. **Kaskadierende Bestätigung:** `POST /orders/{orderId}/confirm` bestätigt alle
   enthaltenen Buchungen und Geschenkgutscheine gleichzeitig.
4. **Filter-Pflicht:** `GET /orders` erfordert mindestens einen Filterparameter.

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `ORDERS_FIELDS_REQUIRED` | 400 | Kein Filter bei GET /orders angegeben |
| `ORDER_NOT_FOUND` | 404 | Order mit angegebener ID nicht gefunden |
| `ORDER_ALREADY_CONFIRMED` | 409 | Order wurde bereits bestätigt |
| `ORDER_ALREADY_CANCELLED` | 409 | Order wurde bereits storniert |

---

## Capability-Abhängigkeiten

| Verwendet mit | Zweck |
|--------------|-------|
| `octo/gifts` | Geschenkgutscheine in Orders; `orderInvoicePdfUrl` auf Gift-Objekten |
| `octo/cardPayments` | Kartenzahlung beim Order-Confirm |
| `octo/questions` | Fragen auf Buchungsebene innerhalb einer Order |

---

*Quelle: https://docs.ventrata.com/capabilities/cart*
