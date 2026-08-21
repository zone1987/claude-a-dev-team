# Shopware 6 — Cart Discounts/Surcharges

Discounts are separate line items (negative price) or promotion items, calculated in a processor.

```php
$discount = new LineItem($id, LineItem::DISCOUNT_LINE_ITEM, null, 1);
$discount->setLabel('FF Rabatt');
$price = $this->percentagePriceCalculator->calculate(-10.0, $cart->getLineItems()->getPrices(), $context);
$discount->setPrice($price);
$toCalculate->add($discount);
```

Percentage discounts via `PercentagePriceCalculator` (on a price collection), absolute ones via `AbsolutePriceCalculator`.
For rule-based campaigns/vouchers use the **promotion** system (`sw-promotion`) instead of custom logic where possible.
Attach them in your own processor (`sw-cart-processor`); tax distribution happens automatically.
