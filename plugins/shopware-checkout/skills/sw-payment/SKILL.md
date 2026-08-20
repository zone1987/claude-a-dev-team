---
name: sw-payment
description: Shopware payment: the 6.7 AbstractPaymentHandler, app payment, the PayPal SDK, tax providers. Use when the request names a Shopware payment handler or tax provider.
---

# Shopware payment

6.7 replaced the old payment handler interfaces with a single AbstractPaymentHandler — older examples do not apply.

## Reference map

- **[APP.md](APP.md)**: Apps provide payment methods through the manifest.
- **[HANDLER.md](HANDLER.md)**: Since 6.7 there is one unified `AbstractPaymentHandler`. [HANDLER-OVERVIEW](HANDLER-OVERVIEW.md).
- **[PAYPAL-SDK.md](PAYPAL-SDK.md)**: A PSR-18 based PHP SDK by Shopware AG for talking directly to the **PayPal REST APIs** — **not** t…. [PAYPAL-SDK-GATEWAYS](PAYPAL-SDK-GATEWAYS.md).
- **[TAX-PROVIDER.md](TAX-PROVIDER.md)**: Tax providers override the cart tax determination.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
