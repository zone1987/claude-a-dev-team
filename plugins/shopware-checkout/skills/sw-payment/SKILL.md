---
name: sw-payment
description: Shopware payment: the 6.7 AbstractPaymentHandler, app payment, the PayPal SDK, tax providers. Use when the request names a Shopware payment handler or tax provider.
---

# Shopware payment

6.7 replaced the old payment handler interfaces with a single AbstractPaymentHandler — older examples do not apply.

## Reference map

- **[APP.md](APP.md)**: Apps stellen Zahlungsarten über das Manifest bereit.
- **[HANDLER.md](HANDLER.md)**: Seit 6.7 ein vereinheitlichter `AbstractPaymentHandler`. [HANDLER-OVERVIEW](HANDLER-OVERVIEW.md).
- **[PAYPAL-SDK.md](PAYPAL-SDK.md)**: PSR-18-basiertes PHP-SDK der Shopware AG für direkte Kommunikation mit den **PayPal REST APIs** — **nicht** d…. [PAYPAL-SDK-GATEWAYS](PAYPAL-SDK-GATEWAYS.md).
- **[TAX-PROVIDER.md](TAX-PROVIDER.md)**: Tax-Provider überschreiben die Steuerermittlung des Warenkorbs.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
