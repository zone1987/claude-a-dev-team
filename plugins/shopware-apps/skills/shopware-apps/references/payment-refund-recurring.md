---
title: Refund and Recurring Payments
impact: MEDIUM
impactDescription: Additional payment capabilities for refunds, validation, and subscriptions
tags: payment, refund, recurring, prepared, validate-url, refund-url, recurring-url
---

## Refund and Recurring Payments

### Prepared Payment (with Validation)

Adds a `validate-url` for pre-order validation:

```xml
<payment-method>
    <identifier>preparedPayment</identifier>
    <name>Validated Payment</name>
    <validate-url>https://payment.app/validate</validate-url>
    <pay-url>https://payment.app/pay</pay-url>
</payment-method>
```

### Refund Payment

```xml
<payment-method>
    <identifier>refundablePayment</identifier>
    <name>Refundable Payment</name>
    <pay-url>https://payment.app/pay</pay-url>
    <refund-url>https://payment.app/refund</refund-url>
</payment-method>
```

### Recurring Payment (Subscriptions)

```xml
<payment-method>
    <identifier>subscriptionPayment</identifier>
    <name>Subscription Payment</name>
    <pay-url>https://payment.app/pay</pay-url>
    <recurring-url>https://payment.app/recurring</recurring-url>
</payment-method>
```

### Payment Method URL Matrix

| Type | pay-url | finalize-url | validate-url | refund-url | recurring-url |
|------|---------|-------------|-------------|-----------|--------------|
| Simple | - | - | - | - | - |
| Sync | Yes | - | - | - | - |
| Async | Yes | Yes | - | - | - |
| Prepared | Yes | - | Yes | - | - |
| Refund | opt. | opt. | - | Yes | - |
| Recurring | opt. | opt. | - | - | Yes |

### Combined Example

A payment method can combine multiple capabilities:

```xml
<payment-method>
    <identifier>fullPayment</identifier>
    <name>Full-Featured Payment</name>
    <pay-url>https://payment.app/pay</pay-url>
    <finalize-url>https://payment.app/finalize</finalize-url>
    <refund-url>https://payment.app/refund</refund-url>
    <recurring-url>https://payment.app/recurring</recurring-url>
    <icon>Resources/payment.png</icon>
</payment-method>
```
