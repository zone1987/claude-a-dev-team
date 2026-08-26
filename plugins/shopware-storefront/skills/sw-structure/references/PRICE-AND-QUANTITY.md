<!-- distilled from shopware/storefront and shopware/core v6.7.13.1 — Checkout/Cart/Price, Content/Product/SalesChannel/Price, quantity-selector.plugin.js -->

# Shopware Storefront — price calculation and quantity

Where a displayed price comes from, and what happens when a quantity changes. Prices are never
computed in Twig: the template renders a `CalculatedPrice` that PHP produced, so changing what a
customer sees means changing the calculation, not the markup.

## Contents

- [The two calculation paths](#the-two-calculation-paths)
- [CalculatedPrice: what a template can read](#calculatedprice-what-a-template-can-read)
- [Gross, net and tax-free](#gross-net-and-tax-free)
- [Rounding](#rounding)
- [The cart pipeline](#the-cart-pipeline)
- [Cart totals](#cart-totals)
- [Where prices are rendered](#where-prices-are-rendered)
- [The quantity selector](#the-quantity-selector)
- [Changing a price](#changing-a-price)

## The two calculation paths

A price reaches the storefront one of two ways, and they are not the same code.

**Listing and detail — the product price.** The Store API resolves the product's price for the
current context before the page is built:

```
product.price (PriceCollection, one entry per currency)
  -> rule-based price? ProductPriceCollection is checked against the active rules
  -> currency conversion via the sales channel currency factor
  -> QuantityPriceDefinition (unit price, tax rules, quantity, reference price)
  -> QuantityPriceCalculator
  -> product.calculatedPrice          CalculatedPrice
     product.calculatedPrices         one per quantity tier, when graduated prices exist
     product.calculatedCheapestPrice  the "from" price of a variant group
```

**Cart and order — the line item price.** Every recalculation runs the whole cart through the
pipeline below; a line item's price is the result of that run, not of a stored value.

Both paths end at `QuantityPriceCalculator::calculate()`, which is the single place a unit price
becomes a `CalculatedPrice`.

## CalculatedPrice: what a template can read

`Checkout/Cart/Price/Struct/CalculatedPrice.php`. Every price in a template is one of these.

| Accessor | Type | Meaning |
|---|---|---|
| `getUnitPrice()` | float | price for one unit, after rules and currency |
| `getTotalPrice()` | float | `unitPrice × quantity`, rounded |
| `getQuantity()` | int | how many units this price covers |
| `getCalculatedTaxes()` | `CalculatedTaxCollection` | the tax amounts, one entry per rate |
| `getTaxRules()` | `TaxRuleCollection` | the rates that applied, with their percentages |
| `getReferencePrice()` | `?ReferencePrice` | the per-unit price, e.g. per litre — null unless the product defines a purchase unit |
| `getListPrice()` | `?ListPrice` | the struck-through price; carries `price`, `discount` and `percentage` |
| `getRegulationPrice()` | `?RegulationPrice` | the lowest price of the last 30 days, required in the EU when showing a discount |

The three optional ones are the reason price templates are full of `is not null` checks. A design
showing a struck-through price only renders it when the product actually has a list price.

## Gross, net and tax-free

`QuantityPriceCalculator` branches on `$context->getTaxState()`:

- **`gross`** — `GrossPriceCalculator`. The stored price includes tax; the tax amount is extracted
  from it. What a B2C shop shows.
- **`net`** — `NetPriceCalculator`. The stored price excludes tax; tax is added on top. What a B2B
  customer group shows.
- **`free`** — the price is calculated, then `taxRules` and `calculatedTaxes` are emptied. Used
  for tax-exempt customers; the price itself is unchanged.

The tax state comes from the customer group and the shipping country, so the same product yields
different numbers for different customers. Never cache a rendered price across contexts.

## Rounding

`CashRounding` is applied twice, with different configurations:

- **Item rounding** (`$context->getItemRounding()`) — on each line item's price.
- **Total rounding** (`$context->getTotalRounding()`) — on the cart total, which is how "round the
  final sum to 0.05" works for currencies such as the Swiss franc.

`cashRound()` applies the configured interval; `mathRound()` is plain half-up rounding used for
intermediate values. Summing rounded line items and rounding again is deliberate — it is what makes
the invoice total match the sum of its lines.

## The cart pipeline

`Checkout/Cart/Processor.php` runs every recalculation in two phases:

```
1. collect    every CartDataCollectorInterface
              declares what it needs and loads it in one batch
              ProductCartProcessor loads the products, PromotionCollector the promotions

2. process    every CartProcessorInterface, in service-tag priority order
              ProductCartProcessor      unit and total price per line item
              ContainerCartProcessor    nested line items
              PromotionProcessor        discounts
              DiscountCartProcessor     absolute and percentage discounts
              DeliveryProcessor         shipping costs
              AmountCalculator          the cart total
```

The split is why a custom price must be set in a **processor**, not in a page subscriber: by the time
a `PageLoadedEvent` fires, the totals are already calculated.

Recalculation is triggered by any cart change — adding a line item, changing a quantity, applying a
promotion, switching country or payment method.

## Cart totals

`AmountCalculator::calculate()` produces the `CartPrice`:

- **gross state** — sums the gross line prices, cash-rounds the total, then derives the net total by
  subtracting the calculated taxes.
- **net state** — sums the net line prices; tax is added on top of the total.
- **tax-free** — `calculateNetDeliveryAmount()`, no tax at all.

`cart.price` then carries `totalPrice`, `netPrice`, `positionPrice`, `taxStatus` and
`calculatedTaxes`. `positionPrice` excludes shipping, which is what the summary uses to show a
subtotal.

## Where prices are rendered

| Template | Renders |
|---|---|
| `component/buy-widget/buy-widget-price.html.twig` | the detail page price block, including tiers |
| `component/product/card/price-unit.html.twig` | the listing card price |
| `component/product/block-price.html.twig` | the graduated price table |
| `component/product/list-price-affix.html.twig` | the struck-through list price |
| `component/line-item/element/total-price.html.twig` | a cart line total |
| `component/line-item/element/unit-price.html.twig` | a cart line unit price |
| `page/checkout/summary/summary-total.html.twig` | the cart total |
| `page/checkout/summary/summary-tax.html.twig` | tax rows |

Formatting is the `currency` filter, which reads the context's currency and the sales channel's
decimal settings: `{{ price.unitPrice|currency }}`. Never format a price by hand — the filter is
what applies the customer's locale.

## The quantity selector

`src/plugin/quantity-selector/quantity-selector.plugin.js`, bound to `[data-quantity-selector]`,
rendered by `component/line-item/element/quantity.html.twig` and the buy widget form.

**What it does, and what it does not.** It is an input wrapper, not a price calculator. It steps the
number, respects `min`, `max` and `step` (the product's minimum purchase, maximum purchase and
purchase steps), updates the unit label, and announces the change to screen readers. Then it
dispatches a native `change` event that bubbles.

Everything after that is somebody else's job:

```
click + / -  or type a value
  -> stepUp()/stepDown() on the input, clamped to min/max/step
  -> _triggerChange() dispatches a bubbling native 'change'
  -> the enclosing form reacts:
       cart page       [data-form-auto-submit] submits the line-item form
       off-canvas cart [data-form-ajax-submit] submits over AJAX and replaces the markup
  -> POST to frontend.checkout.line-item.change-quantity
  -> the cart is recalculated through the whole pipeline
  -> the response re-renders the cart, PluginManager re-initialises the new markup
```

Options: `ariaLiveUpdates`, `ariaLiveUpdateMode` (`live` for a plain selector, `onload` for one
inside an auto-submitting form), `ariaLiveTextValueToken`, `ariaLiveTextProductToken`,
`purchaseLimitUrl` (fetches the remaining stock lazily).

**When restructuring the markup**, keep the classes the plugin queries — `input.js-quantity-selector`,
`.js-btn-plus`, `.js-btn-minus`, `.js-quantity-selector-unit` — and keep the input inside the form
that submits it. Losing the `js-` class breaks the buttons silently; losing the form nesting means
the quantity changes visually and never reaches the cart.

## Changing a price

- **Per line item, permanently** — a `CartProcessorInterface` with a service tag. The only place
  that survives every recalculation.
- **Per product, before the page** — decorate the product price resolution, or subscribe to
  `ProductPageLoadedEvent` for display-only changes that must not affect the cart.
- **Presentation only** — override the price template. Do this only when the number is right and
  its rendering is not.
- **Never in Twig.** A price computed in a template is absent from the cart, the order and the
  invoice, and the three will disagree.
