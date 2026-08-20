---
name: sw-fulfilment
description: Shopware fulfilment: deliveries, shipping methods, the order state machine and its transitions, order events. Use when the request names a Shopware shipping method or order state.
---

# Shopware delivery and order states

Three independent state machines run per order — order, payment, delivery — and each transition fires its own event.

## Reference map

- **[DELIVERY.md](DELIVERY.md)**: The `DeliveryProcessor` calculates deliveries including shipping costs.
- **[ORDER-EVENTS.md](ORDER-EVENTS.md)**: Key order-related events:.
- **[ORDER-STATE-MACHINE.md](ORDER-STATE-MACHINE.md)**: Orders have three state machines: `order.state`, `order_transaction.state`, `order_delivery.state`.
- **[SHIPPING-METHOD.md](SHIPPING-METHOD.md)**: A shipping method is a `shipping_method` entity.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
