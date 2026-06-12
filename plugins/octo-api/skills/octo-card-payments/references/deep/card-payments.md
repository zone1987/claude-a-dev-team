# OCTO — Card Payments Capability (`octo/cardPayments`)

## Capability-Identifier

```
octo/cardPayments
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/cardPayments
Content-Type: application/json
```

---

## Überblick

Die Card-Payments-Capability integriert Zahlungs-Gateways in den OCTO-Buchungsfluss.
Unterstützte Gateways sind **Adyen** (vollständige Session-basierte Integration) und
**external** (externe/POS-Systeme). Das `cardPayment`-Objekt wird beim Bestätigen
einer Buchung oder Order im Request-Body mitgegeben und in der Response zurückgegeben.

---

## Unterstützte Gateways

| Gateway-ID | Beschreibung |
|-----------|--------------|
| `adyen` | Adyen Drop-In / Components Integration |
| `external` | Externes POS-System oder manuelle Verarbeitung |

---

## cardPayment-Objekt (Response — vollständiges Schema)

```typescript
interface CardPayment {
  status: CardPaymentStatus;      // Zahlungsstatus
  id: string;                     // UUID der Zahlung
  cardPaymentId: string;          // Externe Zahlungs-ID
  gateway: "adyen" | "external";  // Verwendetes Gateway
  source: CardPaymentSource;      // Zahlungskanal
  paid: number;                   // Bezahlter Betrag
  totalPaid: number;              // Gesamt bezahlt (inkl. Vorherige)
  totalRefunded: number;          // Gesamt zurückerstattet
  paidSurcharge: number;          // Bezahlter Aufschlag
  balance: number;                // Verbleibendes Guthaben
  surcharge: number;              // Anfallender Aufschlag
  outstandingBalance: number;     // Noch ausstehender Betrag
  amount: number;                 // Transaktionsbetrag
  currency: string;               // ISO 4217 Währungscode
  currencyPrecision: number;      // Dezimalstellen (z.B. 2 für EUR)
  reusableCards: ReusableCard[];  // Gespeicherte Karten
  provider: string;               // Gateway-Provider-String
  providerReference: string;      // Provider-seitige Referenz
  createdAt: string;              // ISO 8601 Erstellungszeitpunkt
}

type CardPaymentStatus = "CONFIRMED" | "PENDING";
type CardPaymentSource = "POS" | "ECOM" | "MOTO";

interface ReusableCard {
  id: string;       // UUID der gespeicherten Karte
  brand: string;    // Kartenmarke (z.B. "visa", "mastercard")
  bin: string;      // Bank Identification Number (erste 6 Ziffern)
  last4: string;    // Letzte 4 Ziffern
}
```

---

## Adyen-spezifische Felder (in Response)

```typescript
interface AdyenFields {
  environment: string;   // "test" oder "live"
  clientKey: string;     // Adyen-Client-Key für Drop-In
  session: {
    id: string;          // Session-ID
    sessionData: string; // Session-Daten (Base64)
  };
  countryCode: string;   // ISO 3166-1 Alpha-2 Ländercode
}
```

**Channel-Auflösungsreihenfolge:**
1. `Octo-Channel`-Header
2. `cardPayment.adyen.channel`-Feld
3. Standard: `"Web"`

---

## External-Gateway-Felder (in Response)

```typescript
interface ExternalFields {
  approved: boolean; // Standard: true
}
```

---

## Request-Felder beim Bestätigen

### cardPaymentRequest (in Booking/Order Confirm-Body)

```typescript
interface CardPaymentRequest {
  gateway: "adyen" | "external";  // Pflicht
  source: "POS" | "ECOM" | "MOTO"; // Pflicht
  currency: string;               // Pflicht — muss Order-Währung entsprechen
  amount?: number;                // Optional — Betrag in kleinster Einheit
  cardId?: string;                // Optional — Gespeicherte Karte (ReusableCard.id)
  returnUrl?: string;             // Optional — Redirect-URL nach Adyen-Session
  notes?: string;                 // Optional — Notizen (external gateway)
  cancel?: boolean;               // Optional — Zahlung stornieren (external)

  // Adyen-Bestätigung (nach Session-Rückkehr):
  adyen?: {
    sessionId: string;           // Pflicht für Adyen-Bestätigung
    sessionResult?: string;      // Optional
    pspReference: string;        // Pflicht
    paymentMethod: string;       // Pflicht
    channel?: string;            // Optional — Adyen-Channel
  };
}
```

---

## Endpunkte

### POST /bookings/{uuid}/confirm — Buchung mit Kartenzahlung bestätigen

```bash
# Adyen-Session erstellen
curl -X POST "https://api.ventrata.com/octo/bookings/{uuid}/confirm" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/cardPayments" \
  -H "Content-Type: application/json" \
  -d '{
    "contact": {
      "fullName": "Max Mustermann",
      "emailAddress": "max@example.com"
    },
    "cardPayment": {
      "gateway": "adyen",
      "source": "ECOM",
      "currency": "EUR",
      "amount": 5000,
      "returnUrl": "https://myshop.example.com/booking/return"
    }
  }'
```

**Response enthält `cardPayment.adyen.session` für Drop-In-Initialisierung.**

---

### POST /bookings/{uuid}/confirm — Adyen-Session abschließen

```bash
curl -X POST "https://api.ventrata.com/octo/bookings/{uuid}/confirm" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/cardPayments" \
  -H "Content-Type: application/json" \
  -d '{
    "cardPayment": {
      "gateway": "adyen",
      "source": "ECOM",
      "currency": "EUR",
      "adyen": {
        "sessionId": "CS0123456789ABCDEF",
        "pspReference": "XXXXXXXXXXXXXXXX",
        "paymentMethod": "scheme",
        "sessionResult": "eyJ..."
      }
    }
  }'
```

---

### POST /orders/{orderId}/confirm — Order mit externer Zahlung bestätigen

```bash
curl -X POST "https://api.ventrata.com/octo/orders/{orderId}/confirm" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/cardPayments, octo/cart" \
  -H "Content-Type: application/json" \
  -d '{
    "cardPayment": {
      "gateway": "external",
      "source": "POS",
      "currency": "EUR",
      "amount": 7500,
      "notes": "Kassenzahlung Terminal 3",
      "approved": true
    }
  }'
```

---

### GET /octo/card_payments/{cardPaymentId} — Zahlungsdetails abrufen

Gibt gecachte Zahlungsinformationen zurück (Cache bis zu 1 Stunde).
**Nur verfügbar wenn Zahlung mit `returnUrl` erstellt wurde.**

**Pfadparameter:**

| Parameter | Typ | Pflicht | Beschreibung |
|-----------|-----|---------|--------------|
| `cardPaymentId` | string | ja | CardPayment-Identifier |

```bash
curl "https://api.ventrata.com/octo/card_payments/pay_12345678" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/cardPayments"
```

**Response:** CardPayment-Objekt

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `GATEWAY_INVALID_SOURCE` | 400 | `source` ist nicht POS, ECOM oder MOTO |
| `GATEWAY_CURRENCY_MISMATCH` | 400 | Währung stimmt nicht mit Order-Währung überein |
| `INVALID_CARD_ID` | 400 | Referenzierte gespeicherte Karte existiert nicht |
| `GATEWAY_MISMATCH` | 400 | Gateway-ID stimmt nicht mit bestehender Zahlung überein |
| `PAYMENT_PENDING` | 202 | Zahlung noch ausstehend — Webhook noch nicht eingegangen |
| `BAD_REQUEST` | 400 | Allgemeine Ablehnung (mit `errorMessage` von Gateway) |

---

## Zahlungsfluss — Adyen (ECOM)

```
1. POST /confirm (mit cardPayment.gateway="adyen", source="ECOM", returnUrl)
   → Response: cardPayment.adyen.session.{id, sessionData}

2. Frontend: Adyen Drop-In mit sessionData initialisieren
   → Gast zahlt → Adyen redirect zu returnUrl

3. POST /confirm erneut (mit adyen.sessionId, pspReference, paymentMethod)
   → Response: cardPayment.status="CONFIRMED"
```

---

## Zahlungsfluss — External (POS)

```
1. POST /confirm (mit cardPayment.gateway="external", source="POS", notes="...")
   → Response: cardPayment.status="CONFIRMED" (sofort)

External payload braucht mindestens eines von: notes, amount, currency, cancel
```

---

## Suppression von Session-Payloads

Wenn `octo/cardPayments` als Capability angegeben ist, werden Adyen-Session-Daten
im Webhook-Payload **nicht** mitgeliefert (Sicherheit).

---

## Capability-Abhängigkeiten

| Verwendet mit | Zweck |
|--------------|-------|
| `octo/cart` | Zahlung beim Order-Confirm |
| `octo/gifts` | Kombination Gift-Code + Kartenzahlung (Teilzahlung) |

---

*Quelle: https://docs.ventrata.com/capabilities/card-payments*
