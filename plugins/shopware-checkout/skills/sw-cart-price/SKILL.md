---
name: sw-cart-price
description: >
  Preisberechnung im Shopware-6-Warenkorb: QuantityPriceCalculator/PercentagePriceCalculator/AbsolutePriceCalculator,
  QuantityPriceDefinition, CalculatedPrice, Steuer-/Rundungslogik. Trigger: "Cart Preis berechnen", "QuantityPriceCalculator",
  "CalculatedPrice", "PriceDefinition", "Preisberechnung warenkorb", "PercentagePriceCalculator", "AbsolutePriceCalculator".
  Shopware 6.7.
---

# Shopware 6 — Cart-Preisberechnung

Preise im Cart werden über Calculator-Services berechnet (nie manuell), aus einer `PriceDefinition` → `CalculatedPrice`
(inkl. Steueranteile/Rundung).

```php
$definition = new QuantityPriceDefinition($unitNet, $taxRules, $quantity);
$calculated = $this->quantityPriceCalculator->calculate($definition, $context);
$lineItem->setPrice($calculated);
```

Calculator-Typen: `QuantityPriceCalculator` (Mengenpreis), `PercentagePriceCalculator` (prozentual, z.B. Rabatt),
`AbsolutePriceCalculator` (fester Betrag). Steuerermittlung über `TaxRuleCollection`/`TaxDetector`, Rundung über
`CashRounding`. Brutto/Netto je nach SalesChannel-Steuerlogik. PriceField der Entity: `shopware-data` → `sw-pricing-field`.
Rabatte: `sw-cart-discount`.
