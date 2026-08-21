# Shopware 6 — App payment API reference

> Source: `resources/references/app-reference/payment-reference.md`
> Available from Shopware 6.4.1.0

The app payment API consists of two endpoints that Shopware calls against the app server URL.
All bodies are JSON-encoded.

---

## Contents

- [Pay endpoint](#pay-endpoint)
- [Finalize endpoint](#finalize-endpoint)
- [Status values](#status-values)
- [manifest.xml registration](#manifestxml-registration)

## Pay endpoint

**`POST https://payment.app/pay`**

Called when the user clicks "Confirm order".

### Request parameters

| Parameter | Type | Description |
|:----------|:----|:-------------|
| **Header** | | |
| `shopware-shop-signature`* | string | HMAC signature of the JSON-encoded body content, signed with the shop secret from the registration |
| **Body** | | |
| `order`* | OrderEntity | The order entity including all necessary associations (currency, delivery address, billing address, line items) |
| `orderTransaction`* | OrderTransactionEntity | The payment transaction entity |
| `orderTransaction.id`* | string | To identify the transaction in a later finalize request |
| `returnUrl` | string | URL the user should be redirected back to after the payment. Present only for asynchronous payments. |
| `source`* | object | Data identifying the shop |
| `source.url`* | string | Shop URL |
| `source.shopId`* | string | Shop ID |
| `source.appVersion`* | string | Version of the installed app |

### Responses

**`200 OK` — Successful redirect (asynchronous):**
```json
{
  "redirectUrl": "https://payment.app/user/go/here/068b1ec4d7ff431b95d3b7431cc725aa/"
}
```

**`200 OK` — Error (missing credentials):**
```json
{
  "status": "fail",
  "message": "The shop has not provided all credentials for the payment provider."
}
```

---

## Finalize endpoint

**`POST https://payment.app/finalize`**

Called when the user returns to the `returnUrl` (after being redirected to the payment provider).

### Request parameters

| Parameter | Type | Description |
|:----------|:----|:-------------|
| **Header** | | |
| `shopware-shop-signature`* | string | HMAC signature of the JSON-encoded body content |
| **Body** | | |
| `orderTransaction`* | OrderTransactionEntity | The payment transaction entity |
| `orderTransaction.id`* | string | To identify the transaction |
| `source`* | object | Data identifying the shop |
| `source.url`* | string | Shop URL |
| `source.shopId`* | string | Shop ID |
| `source.appVersion`* | string | Version of the installed app |

### Responses

**`200 OK` — Successfully paid:**
```json
{
  "status": "paid"
}
```

**`200 OK` — Insufficient funds:**
```json
{
  "status": "fail",
  "message": "The user did not have adequate funds."
}
```

**`200 OK` — User cancelled the payment:**
```json
{
  "status": "cancel",
  "message": "The user did not finish payment."
}
```

---

## Status values

| Status | Description |
|:-------|:-------------|
| `paid` | Payment successful |
| `fail` | Payment failed |
| `cancel` | Payment cancelled |
| `authorize` | Payment authorized (not charged immediately) |
| `paid_partially` | Partial payment made |

---

## manifest.xml registration

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
