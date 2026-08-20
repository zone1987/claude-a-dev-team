# Shopware 6 — Cart Price Calculation

Cart prices come from calculator services (never set them manually), turning a `PriceDefinition` into a `CalculatedPrice`
(including tax shares/rounding).

```php
$definition = new QuantityPriceDefinition($unitNet, $taxRules, $quantity);
$calculated = $this->quantityPriceCalculator->calculate($definition, $context);
$lineItem->setPrice($calculated);
```

Calculator types: `QuantityPriceCalculator` (quantity price), `PercentagePriceCalculator` (percentage, e.g. discount),
`AbsolutePriceCalculator` (fixed amount). Tax determination via `TaxRuleCollection`/`TaxDetector`, rounding via
`CashRounding`. Gross/net depends on the sales channel tax logic. Entity price field: `shopware-data` → `sw-pricing-field`.
Discounts: `sw-cart-discount`.
