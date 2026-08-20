---
title: Asynchronous Payment
impact: MEDIUM
impactDescription: Async payments redirect customers to external providers and use a finalize callback
tags: payment, asynchronous, redirect, finalize-url, pay-url
---

## Asynchronous Payment

Asynchronous payments redirect customers to external payment providers. They require both `pay-url` and `finalize-url`.

### Flow

1. Customer places order → Shopware calls `pay-url`
2. App responds with `redirectUrl` → Customer goes to payment provider
3. Customer completes payment → Provider redirects to Shopware's `returnUrl`
4. Shopware calls `finalize-url` → App confirms the payment status

### Manifest Configuration

```xml
<payments>
    <payment-method>
        <identifier>myAsyncPayment</identifier>
        <name>Credit Card Payment</name>
        <pay-url>https://payment.app/async/pay</pay-url>
        <finalize-url>https://payment.app/async/finalize</finalize-url>
        <icon>Resources/creditcard.png</icon>
    </payment-method>
</payments>
```

### Pay Response (Redirect)

```json
{
    "redirectUrl": "https://provider.com/checkout/abc123"
}
```

### Finalize Response (Success)

```json
{ "status": "paid" }
```

### Finalize Response (Cancelled)

```json
{ "status": "cancel", "message": "Customer cancelled payment" }
```

### Finalize Response (Failed)

```json
{ "status": "fail", "message": "Payment declined by provider" }
```

### Important Notes

- The `returnUrl` is provided in the pay request body — redirect the customer back to it after provider checkout
- The `orderTransaction.id` identifies the transaction across pay and finalize calls
- All responses must be signed
