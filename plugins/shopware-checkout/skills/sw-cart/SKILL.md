---
name: sw-cart
description: Shopware cart: the processor pipeline, collectors, validators, price calculation, line items, discounts, the cart facade. Use when changing Shopware cart behaviour.
---

# Shopware cart pipeline

The cart is recalculated on every change through collector, processor and validator stages. Never mutate a cart outside them.

## Reference map

- **[COLLECTOR.md](COLLECTOR.md)**: The collector runs **before** the processors and loads all data needed for the calculation in a single batc….
- **[DISCOUNT.md](DISCOUNT.md)**: Discounts are separate line items or promotion items.
- **[FACADE-SCRIPT.md](FACADE-SCRIPT.md)**: Apps manipulate the cart through the **cart facade** in the `cart` script hook — without a PHP processor of their own.
- **[LINE-ITEM.md](LINE-ITEM.md)**: A cart position is a `LineItem`.
- **[NESTED-LINE-ITEMS.md](NESTED-LINE-ITEMS.md)**: Line items can have `children` — e.g. a bundle with sub-products.
- **[PRICE.md](PRICE.md)**: Cart prices come from calculator services, turning a `PriceDefinition` into a `CalculatedPrice`.
- **[PROCESSOR.md](PROCESSOR.md)**: The cart is calculated in two phases: **collector** → **processor**. [PROCESSOR-CHECKOUT](PROCESSOR-CHECKOUT.md).
- **[PROMOTION.md](PROMOTION.md)**: Campaigns are `promotion` entities with discounts, optional codes and conditions via rules.
- **[VALIDATOR.md](VALIDATOR.md)**: Validators inspect the calculated cart and can attach **blocking** or informational errors.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
