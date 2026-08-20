# Shopware 6 — Cart-Rabatte/Abschläge

Rabatte sind eigene LineItems (negativer Preis) bzw. Promotion-Items, berechnet in einem Processor.

```php
$discount = new LineItem($id, LineItem::DISCOUNT_LINE_ITEM, null, 1);
$discount->setLabel('FF Rabatt');
$price = $this->percentagePriceCalculator->calculate(-10.0, $cart->getLineItems()->getPrices(), $context);
$discount->setPrice($price);
$toCalculate->add($discount);
```

Prozentual über `PercentagePriceCalculator` (auf eine Preis-Collection), absolut über `AbsolutePriceCalculator`.
Für regelbasierte Aktionen/Gutscheine das **Promotion**-System nutzen (`sw-promotion`) statt eigener Logik, wenn möglich.
Im eigenen Processor (`sw-cart-processor`) anhängen; Steuerverteilung erfolgt automatisch.
