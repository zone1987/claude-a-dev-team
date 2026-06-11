# Shopware 6 — App Payment API-Referenz

> Quelle: `resources/references/app-reference/payment-reference.md`
> Verfügbar ab Shopware 6.4.1.0

Die App-Payment-API besteht aus zwei Endpunkten, die von Shopware gegen die App-Server-URL aufgerufen werden.
Alle Bodies sind JSON-kodiert.

---

## Pay-Endpunkt

**`POST https://payment.app/pay`**

Wird aufgerufen wenn der Nutzer auf "Bestellung bestätigen" klickt.

### Request-Parameter

| Parameter | Typ | Beschreibung |
|:----------|:----|:-------------|
| **Header** | | |
| `shopware-shop-signature`* | string | HMAC-Signatur des JSON-kodierten Body-Inhalts, signiert mit dem Shop-Secret aus der Registrierung |
| **Body** | | |
| `order`* | OrderEntity | Die Bestellungs-Entity inklusive aller notwendigen Assoziationen (Währung, Lieferadresse, Rechnungsadresse, Positionen) |
| `orderTransaction`* | OrderTransactionEntity | Die Zahlungstransaktion-Entity |
| `orderTransaction.id`* | string | Zur Identifikation der Transaktion bei einem späteren Finalize-Request |
| `returnUrl` | string | URL zu der der Nutzer nach der Bezahlung zurückgeleitet werden soll. Nur bei asynchronen Zahlungen vorhanden. |
| `source`* | object | Daten zur Identifikation des Shops |
| `source.url`* | string | Shop-URL |
| `source.shopId`* | string | Shop-ID |
| `source.appVersion`* | string | Version der installierten App |

### Responses

**`200 OK` — Erfolgreiche Weiterleitung (asynchron):**
```json
{
  "redirectUrl": "https://payment.app/user/go/here/068b1ec4d7ff431b95d3b7431cc725aa/"
}
```

**`200 OK` — Fehler (fehlende Credentials):**
```json
{
  "status": "fail",
  "message": "The shop has not provided all credentials for the payment provider."
}
```

---

## Finalize-Endpunkt

**`POST https://payment.app/finalize`**

Wird aufgerufen wenn der Nutzer zur `returnUrl` zurückkehrt (nach der Weiterleitung zum Zahlungsanbieter).

### Request-Parameter

| Parameter | Typ | Beschreibung |
|:----------|:----|:-------------|
| **Header** | | |
| `shopware-shop-signature`* | string | HMAC-Signatur des JSON-kodierten Body-Inhalts |
| **Body** | | |
| `orderTransaction`* | OrderTransactionEntity | Die Zahlungstransaktion-Entity |
| `orderTransaction.id`* | string | Zur Identifikation der Transaktion |
| `source`* | object | Daten zur Identifikation des Shops |
| `source.url`* | string | Shop-URL |
| `source.shopId`* | string | Shop-ID |
| `source.appVersion`* | string | Version der installierten App |

### Responses

**`200 OK` — Erfolgreich bezahlt:**
```json
{
  "status": "paid"
}
```

**`200 OK` — Unzureichende Mittel:**
```json
{
  "status": "fail",
  "message": "The user did not have adequate funds."
}
```

**`200 OK` — Nutzer hat Zahlung abgebrochen:**
```json
{
  "status": "cancel",
  "message": "The user did not finish payment."
}
```

---

## Status-Werte

| Status | Beschreibung |
|:-------|:-------------|
| `paid` | Zahlung erfolgreich |
| `fail` | Zahlung fehlgeschlagen |
| `cancel` | Zahlung abgebrochen |
| `authorize` | Zahlung autorisiert (nicht sofort belastet) |
| `paid_partially` | Teilzahlung erfolgt |

---

## manifest.xml Registrierung

```xml
<payments>
    <payment-method>
        <identifier>myPaymentMethod</identifier>
        <name>My Payment Method</name>
        <name lang="de-DE">Meine Zahlungsmethode</name>
        <description>App-based payment</description>
        <pay-url>https://payment.app/pay</pay-url>
        <finalize-url>https://payment.app/finalize</finalize-url>
        <icon>Resources/config/payment.png</icon>
    </payment-method>
</payments>
```
