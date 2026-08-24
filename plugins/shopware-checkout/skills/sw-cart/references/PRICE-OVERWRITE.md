# Shopware 6 — overwriting a line item price

**Use this rarely and carefully.** To reduce or raise a price, add a discount or surcharge instead
(`DISCOUNT.md`) — that keeps the original price visible and recalculable. Overwriting is right for a
case like live shopping, where the price itself genuinely differs.

## Contents

- [The pattern](#the-pattern)
- [The collector](#the-collector)
- [The processor](#the-processor)
- [Registration](#registration)

## The pattern

It takes both roles: a **collector** gathers the new prices (and suppresses duplicate lookups), a
**processor** calculates and applies them. One class can implement both interfaces — the guide's
`OverwritePriceCollector` does — or they can be split.

Where the new prices come from is your decision: a product entity extension, an API call, anything.

## The collector

Implement `Shopware\Core\Checkout\Cart\CartDataCollectorInterface`.

```php
// <plugin root>/src/Core/Checkout/Cart/OverwritePriceCollector.php
public function collect(CartDataCollection $data, Cart $original,
                        SalesChannelContext $context, CartBehavior $behavior): void
{
    // every product id in the current cart
    $productIds = $original->getLineItems()
        ->filterType(LineItem::PRODUCT_LINE_ITEM_TYPE)
        ->getReferenceIds();

    // drop the ids whose price was fetched already
    $filtered = $this->filterAlreadyFetchedPrices($productIds, $data);

    if (empty($filtered)) {
        return;
    }

    foreach ($filtered as $id) {
        $key = $this->buildKey($id);

        // needs implementing — this is where your price comes from
        $newPrice = $this->doSomethingToGetNewPrice();

        // set a value for every product id, so the next calculation does not query again
        $data->set($key, $newPrice);
    }
}
```

**Prefix the key.** The line item id alone would collide with other collectors storing under the same
id:

```php
private function buildKey(string $id): string
{
    return 'price-overwrite-' . $id;
}
```

**`filterAlreadyFetchedPrices` exists because `collect()` can run several times per request.** It
skips ids already in the collection, which is what prevents repeated database queries. Drop it only
if your prices genuinely change between runs.

```php
private function filterAlreadyFetchedPrices(array $productIds, CartDataCollection $data): array
{
    $filtered = [];

    foreach ($productIds as $id) {
        $key = $this->buildKey($id);

        if ($data->has($key)) {
            continue;
        }

        $filtered[] = $id;
    }

    return $filtered;
}
```

Filtering to products first is deliberate: a discount or any other custom line item type should keep
its price.

## The processor

Implement `Shopware\Core\Checkout\Cart\CartProcessorInterface` and inject
`Shopware\Core\Checkout\Cart\Price\QuantityPriceCalculator`.

```php
public function process(CartDataCollection $data, Cart $original, Cart $toCalculate,
                        SalesChannelContext $context, CartBehavior $behavior): void
{
    $products = $toCalculate->getLineItems()->filterType(LineItem::PRODUCT_LINE_ITEM_TYPE);

    foreach ($products as $product) {
        $key = $this->buildKey($product->getReferencedId());

        // no overwritten price? next product
        if (!$data->has($key) || $data->get($key) === null) {
            continue;
        }

        $newPrice = $data->get($key);

        $definition = new QuantityPriceDefinition(
            $newPrice,
            $product->getPrice()->getTaxRules(),
            $product->getPrice()->getQuantity()
        );

        $calculated = $this->calculator->calculate($definition, $context);

        $product->setPrice($calculated);
        $product->setPriceDefinition($definition);
    }
}
```

Both are set, and both matter: `setPrice()` carries the calculated result, `setPriceDefinition()`
lets the core recalculate it later — after a currency or tax change, for instance.

**Never query the database in `process()`** — always collect first. `$original` is passed only
because it may hold data the actual cart instance needs; every change belongs on `$toCalculate`.

## Registration

One service, two tags, both after the product collector and processor:

```php
// <plugin root>/src/Resources/config/services.php
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $configurator): void {
    $services = $configurator->services();

    $services->set(OverwritePriceCollector::class)
        ->args([
            service(QuantityPriceCalculator::class),
        ])
        // after the product collector and processor
        ->tag('shopware.cart.processor', ['priority' => 4500])
        ->tag('shopware.cart.collector', ['priority' => 4500]);
};
```

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/change-price-of-item.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/change-price-of-item.html),
Shopware 6.7, retrieved 2026-08-21.
