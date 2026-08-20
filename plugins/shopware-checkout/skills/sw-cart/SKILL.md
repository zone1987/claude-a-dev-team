---
name: sw-cart
description: Shopware cart: the processor pipeline, collectors, validators, price calculation, line items, discounts, the cart facade. Use when changing Shopware cart behaviour.
---

# Shopware cart pipeline

The cart is recalculated on every change through collector, processor and validator stages. Never mutate a cart outside them.

## Reference map

- **[COLLECTOR.md](COLLECTOR.md)**: Der Collector läuft **vor** den Processoren und lädt alle Daten, die zur Berechnung gebraucht werden, gebünde….
- **[DISCOUNT.md](DISCOUNT.md)**: Rabatte sind eigene LineItems bzw.
- **[FACADE-SCRIPT.md](FACADE-SCRIPT.md)**: Apps manipulieren den Warenkorb über die **Cart-Facade** im `cart`-Script-Hook — ohne eigenen PHP-Processor.
- **[LINE-ITEM.md](LINE-ITEM.md)**: Eine Warenkorb-Position ist ein `LineItem`.
- **[NESTED-LINE-ITEMS.md](NESTED-LINE-ITEMS.md)**: LineItems können `children` haben — z.B.
- **[PRICE.md](PRICE.md)**: Preise im Cart werden über Calculator-Services berechnet, aus einer `PriceDefinition` → `CalculatedPrice`.
- **[PROCESSOR.md](PROCESSOR.md)**: Der Warenkorb wird in zwei Phasen berechnet: **Collector** → **Processor**. [PROCESSOR-CHECKOUT](PROCESSOR-CHECKOUT.md).
- **[PROMOTION.md](PROMOTION.md)**: Aktionen sind `promotion`-Entities mit Rabatten, optionalen Codes und Bedingungen über Rules.
- **[VALIDATOR.md](VALIDATOR.md)**: Validatoren prüfen den berechneten Warenkorb und können **blockierende** oder informative Fehler anhängen.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
