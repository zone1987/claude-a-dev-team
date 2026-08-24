# Shopware 6 — Cart Processor

The cart is calculated in two phases: **collector** (gather data, see `COLLECTOR.md`) → **processor**
(calculate prices/structure). A processor implements `CartProcessorInterface`.

```php
class FfFeeProcessor implements CartProcessorInterface
{
    public function process(CartDataCollection $data, Cart $original, Cart $toCalculate,
                            SalesChannelContext $context, CartBehavior $behavior): void
    {
        // add line items/fees to $toCalculate, calculate prices via calculator
    }
}
```

Register via the `shopware.cart.processor` tag (priority controls the order). Always work on `$toCalculate`
(not `$original`). Calculate prices through the price services (`PRICE.md`). Discounts: `DISCOUNT.md`. For app-based
manipulation: `FACADE-SCRIPT.md`.

→ Cart details: [PROCESSOR-CHECKOUT.md](PROCESSOR-CHECKOUT.md)

## Contents

- [Why the architecture looks like this](#why-the-architecture-looks-like-this)
- [The rules](#the-rules)

## Why the architecture looks like this

**The cart is recalculated several times per request**, to resolve dependencies between line items.
That single fact is behind every rule below: an extension has to be deterministic and cheap, because
whatever it does happens repeatedly.

Three design principles follow:

- Cart processing is multi-pass and must stay **deterministic**.
- **Data loading is separate from calculation**, which is what keeps performance stable.
- Price logic is **centralised and reusable**, not reimplemented per extension.

## The rules

| Rule | Why |
|---|---|
| Load external data once, in a `CartDataCollector` | `collect()` runs before the passes and can cache |
| Modify calculated items in a `CartProcessor` | that is the phase where prices exist |
| **Never query the database in `process()`** | it runs many times per request |
| Always use the `PriceCalculator` classes | rounding and tax handling live there, not in your code |

Stated as the technical rules the core holds extensions to:

- `CartProcessorInterface::process()` must not execute queries.
- `Shopware\Core\Checkout\Cart\CartDataCollectorInterface::collect()` must check whether the data
  was already loaded before appending it to `CartDataCollection` — that check is what avoids
  unnecessary queries.
- Line items must be created through a `LineItemFactoryHandler` class, never constructed ad hoc.
- Every price calculation must use the calculators in `Shopware\Core\Checkout\Cart\Price`.
- Cart-related functionality must be exposed through the matching Store API routes in
  `Shopware\Core\Checkout\Cart\SalesChannel`.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/architecture/cart-process.html](https://developer.shopware.com/docs/guides/plugins/plugins/architecture/cart-process.html),
Shopware 6.7, retrieved 2026-08-21.
