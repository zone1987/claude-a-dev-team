---
title: Synchronous Payment
impact: MEDIUM
impactDescription: Sync payments process the entire transaction in a single request
tags: payment, synchronous, pay-url, transaction
---

## Synchronous Payment

Synchronous payments handle the entire payment in one request-response cycle. The app server receives order data and returns a status.

### Manifest Configuration

```xml
<payments>
    <payment-method>
        <identifier>mySyncPayment</identifier>
        <name>My Sync Payment</name>
        <name lang="de-DE">Meine synchrone Zahlung</name>
        <pay-url>https://payment.app/sync/pay</pay-url>
        <icon>Resources/payment-icon.png</icon>
    </payment-method>
</payments>
```

### Pay Endpoint Request

`POST https://payment.app/sync/pay`

Headers: `shopware-shop-signature` (HMAC-SHA256)

Body contains: `order` (with currency, addresses, line items), `orderTransaction`, `source` (shopId, url, appVersion)

### Response (Success)

```json
{ "status": "paid" }
```

Or authorize for later capture:

```json
{ "status": "authorize" }
```

### Response (Failure)

```json
{ "status": "fail", "message": "Insufficient funds" }
```

### Simple Payment (No URL)

Omitting `pay-url` creates a payment that stays in "open" status:

```xml
<payment-method>
    <identifier>simplePayment</identifier>
    <name>Invoice Payment</name>
</payment-method>
```

### Important Notes

- Since Shopware 6.7.0.0, app servers **must** respond with a payment state to change transaction status
- The `identifier` cannot be changed after creation
- All responses must be signed with `shopware-app-signature` header
