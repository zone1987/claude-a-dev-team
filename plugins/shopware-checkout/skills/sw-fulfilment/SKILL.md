---
name: sw-fulfilment
description: Shopware fulfilment: deliveries, shipping methods, the order state machine and its transitions, order events. Use when the request names a Shopware shipping method or order state.
---

# Shopware delivery and order states

Three independent state machines run per order — order, payment, delivery — and each transition fires its own event.

## Reference map

- **[DELIVERY.md](DELIVERY.md)**: Der `DeliveryProcessor` berechnet Lieferungen inkl.
- **[ORDER-EVENTS.md](ORDER-EVENTS.md)**: Wichtige Events rund um Bestellungen:.
- **[ORDER-STATE-MACHINE.md](ORDER-STATE-MACHINE.md)**: Bestellungen haben drei State-Machines: `order.state`, `order_transaction.state`, `order_delivery.state`.
- **[SHIPPING-METHOD.md](SHIPPING-METHOD.md)**: Eine Versandart ist eine `shipping_method`-Entity.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
