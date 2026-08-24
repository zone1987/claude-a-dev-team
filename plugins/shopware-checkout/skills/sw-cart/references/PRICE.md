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

## Contents

- [Customising product price calculation globally](#customising-product-price-calculation-globally)

## Customising product price calculation globally

To change how product prices are calculated across the shop, **decorate
`ProductPriceCalculator`** — it has a single `calculate` method.

```php
// <plugin root>/src/Service/CustomProductPriceCalculator.php
public function __construct(private AbstractProductPriceCalculator $productPriceCalculator)
{
}

public function getDecorated(): AbstractProductPriceCalculator
{
    return $this->productPriceCalculator;
}

public function calculate(iterable $products, SalesChannelContext $context): void
{
    /** @var SalesChannelProductEntity $product */
    foreach ($products as $product) {
        $price = $product->getPrice();
        // an example only:
        // a product can carry more than one price, which you have to account for,
        // and you may also need to change the value of getCheapestPrice
        $price->first()->setGross(100);
        $price->first()->setNet(50);
    }

    $this->getDecorated()->calculate($products, $context);
}
```

The constructor receives the inner `AbstractProductPriceCalculator` — normally `ProductPriceCalculator`
itself — and `getDecorated()` has to return it, so the original `calculate` can still run.

**Two traps in that example.** It rewrites *every* product to the same price, so narrow down which
products you touch. And a product can have several prices plus a `getCheapestPrice`, so setting
`first()` alone leaves the rest inconsistent — read the core's own `calculate` to see what a complete
calculation covers.

```php
// <plugin root>/src/Resources/config/services.php
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $configurator): void {
    $services = $configurator->services();

    $services->set(CustomProductPriceCalculator::class)
        ->decorate(ProductPriceCalculator::class)
        ->args([
            service('.inner'),
        ]);
};
```

Without that registration the decoration has no effect at all.

To add a discount or surcharge rather than rewrite a price, see `DISCOUNT.md`.

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/customize-price-calculation.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/customize-price-calculation.html),
Shopware 6.7, retrieved 2026-08-21.
