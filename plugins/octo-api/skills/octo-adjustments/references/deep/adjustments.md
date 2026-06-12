# OCTO — Price Adjustments Capability (`octo/adjustments`)

## Capability-Identifier

```
octo/adjustments
```

---

## Authentifizierung

```http
Authorization: Bearer {api_key}
Octo-Capabilities: octo/adjustments
Content-Type: application/json
```

---

## Überblick

Die Adjustments-Capability ermöglicht Preisanpassungen auf Buchungsebene. Positive oder
negative Beträge können als `adjustments`-Array im Request-Body übergeben werden und
werden von der Provision (Commission) abgezogen oder addiert. Adjustments können nicht
den Buchungspreis unter den Commission-Betrag reduzieren.

**Commission-Formel:** `commission = retail - net`

---

## Adjustment-Objekt

```typescript
interface Adjustment {
  per: "BOOKING";                  // Immer "BOOKING" (derzeit einziger Wert)
  amount: number;                  // Betrag (positiv = Aufschlag, negativ = Rabatt)
  quantity: number;                // Multiplikator
  notes?: string;                  // Optionale Beschreibung/Notiz
  netDiscount: "NONE" | string;    // Netto-Rabatt-Typ — "NONE" oder supplier-spezifischer Wert
}
```

---

## Betroffene Endpunkte

Die `adjustments`-Erweiterung gilt für folgende Booking-Write-Routen:

| Methode | Pfad | Beschreibung |
|---------|------|--------------|
| POST | `/bookings` | Buchung mit Anpassung erstellen |
| PATCH | `/bookings/{uuid}` | Buchung mit Anpassung aktualisieren |
| POST | `/bookings/{uuid}/confirm` | Buchung mit Anpassung bestätigen |

Mit `octo/cart`: Gleiches `adjustments`-Feld gilt auch in verschachtelten
`bookings[]`-Payloads der Order-Write-Routen.

---

## Request-Erweiterung

Das `adjustments`-Array wird dem Booking-Write-Request hinzugefügt:

```typescript
interface BookingWriteRequest {
  // ... Standard-Buchungsfelder ...
  adjustments?: Adjustment[];  // Optional — Preisanpassungen
}
```

---

## Beispiele

### Einzelne Preisanpassung (Rabatt)

```bash
curl -X POST https://api.ventrata.com/octo/bookings \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/adjustments" \
  -H "Content-Type: application/json" \
  -d '{
    "productId": "product_stadtfuehrung",
    "optionId": "default",
    "availabilityId": "2026-06-15T10:00:00+02:00",
    "unitItems": [
      { "unitId": "unit_erwachsener" }
    ],
    "adjustments": [
      {
        "per": "BOOKING",
        "amount": -500,
        "quantity": 1,
        "notes": "VIP-Stammkunden-Rabatt",
        "netDiscount": "NONE"
      }
    ]
  }'
```

### Bestätigung mit Aufschlag

```bash
curl -X POST "https://api.ventrata.com/octo/bookings/{uuid}/confirm" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/adjustments" \
  -H "Content-Type: application/json" \
  -d '{
    "contact": {
      "fullName": "Max Mustermann",
      "emailAddress": "max@example.com"
    },
    "adjustments": [
      {
        "per": "BOOKING",
        "amount": 200,
        "quantity": 1,
        "notes": "Express-Booking-Gebühr",
        "netDiscount": "NONE"
      }
    ]
  }'
```

### Mehrere Anpassungen kombinieren

```bash
{
  "adjustments": [
    {
      "per": "BOOKING",
      "amount": -1000,
      "quantity": 1,
      "notes": "Treueprogramm-Rabatt 10%",
      "netDiscount": "NONE"
    },
    {
      "per": "BOOKING",
      "amount": 150,
      "quantity": 1,
      "notes": "Handling-Gebühr",
      "netDiscount": "NONE"
    }
  ]
}
```

### Mit octo/cart — Adjustment auf Buchung innerhalb Order

```bash
curl -X POST "https://api.ventrata.com/octo/orders/{orderId}/confirm" \
  -H "Authorization: Bearer {api_key}" \
  -H "Octo-Capabilities: octo/adjustments, octo/cart" \
  -H "Content-Type: application/json" \
  -d '{
    "bookings": [
      {
        "uuid": "{bookingUuid}",
        "adjustments": [
          {
            "per": "BOOKING",
            "amount": -500,
            "quantity": 1,
            "netDiscount": "NONE"
          }
        ]
      }
    ]
  }'
```

---

## Response-Erweiterung

Das Booking-Response-Objekt enthält die angewendeten Adjustments zurück:

```typescript
interface BookingResponse {
  // ... Standard-Buchungsfelder ...
  adjustments: Adjustment[];       // Angewendete Anpassungen
  pricing: {
    original: number;              // Originalpreis
    retail: number;                // Einzelhandelspreis (nach Markup)
    net: number;                   // Nettopreis (Einkaufspreis)
    commission: number;            // Provision (retail - net)
    currencyPrecision: number;     // Dezimalstellen
    currency: string;              // ISO 4217
    adjusted: number;              // Preis nach Adjustment
  };
}
```

---

## Berechnungslogik

```
Endpreis = retail + sum(adjustments[].amount * adjustments[].quantity)
Mindestpreis = net (Endpreis kann nicht unter net fallen)
Commission nach Adjustment = Endpreis - net
```

**Beispiel:**
- retail: 5000 (50,00 EUR)
- net: 3000 (30,00 EUR)
- commission: 2000 (20,00 EUR)
- adjustment: -500 (-5,00 EUR)
- adjusted: 4500 (45,00 EUR) → commission sinkt auf 1500

---

## Validierungsregeln

| Regel | Fehler |
|-------|--------|
| `per` muss "BOOKING" sein | `ADJUSTMENTS_INVALID_PER` |
| `netDiscount` muss gültiger Wert sein | `ADJUSTMENTS_INVALID_NET_DISCOUNT` |
| `netDiscount` nicht für diesen Supplier erlaubt | `ADJUSTMENTS_NET_DISCOUNT_NOT_ALLOWED` |
| Endpreis unter Nettopreis | `ADJUSTMENTS_BELOW_NET` |

---

## Fehler-Codes

| Code | HTTP | Beschreibung |
|------|------|--------------|
| `ADJUSTMENTS_INVALID_PER` | 400 | `per`-Feld hat ungültigen Wert (nur "BOOKING" erlaubt) |
| `ADJUSTMENTS_INVALID_NET_DISCOUNT` | 400 | `netDiscount` hat ungültigen Wert |
| `ADJUSTMENTS_NET_DISCOUNT_NOT_ALLOWED` | 400 | `netDiscount`-Wert für diesen Supplier nicht aktiviert |
| `ADJUSTMENTS_BELOW_NET` | 400 | Gesamtpreis nach Adjustment unter Nettopreis |

---

## Capability-Abhängigkeiten

| Verwendet mit | Zweck |
|--------------|-------|
| `octo/pricing` | Vollständige Preis-Darstellung in Responses |
| `octo/cart` | Adjustments auf Buchungen innerhalb von Orders |

---

*Quelle: https://docs.ventrata.com/capabilities/adjustments*
