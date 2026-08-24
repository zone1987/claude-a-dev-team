# Shopware 6 — cart collectors and processors

Changing the cart at runtime takes two roles, and keeping them apart is what keeps the cart fast.

| Role | Purpose | Tag |
|---|---|---|
| **Collector** | fetch the data a processor needs — from the database, an API, anywhere | `shopware.cart.collector` |
| **Processor** | apply changes to the cart, using what the collector fetched | `shopware.cart.processor` |

## Contents

- [The collector](#the-collector)
- [The processor](#the-processor)
- [Why the split matters](#why-the-split-matters)

## The collector

Implement `Shopware\Core\Checkout\Cart\CartDataCollectorInterface` and its `collect` method — the
guide's example class is `CustomCartCollector`.

```php
// namespace Swag\BasicExample\Core\Checkout\Cart;
class CustomCartCollector implements CartDataCollectorInterface
{
public function collect(CartDataCollection $data, Cart $original,
                        SalesChannelContext $context, CartBehavior $behavior): void
{
    $newData = $this->collectData();

    $data->set('uniqueKey', $newData);
}
}
```

`collect()` takes four parameters:

| Parameter | What it is |
|---|---|
| `CartDataCollection` | where the collected data goes, normally through `set()` with a unique key. **Available in every processor** |
| `Cart` | the current cart and its line items |
| `SalesChannelContext` | the current context: currency, country and the rest |
| `CartBehavior` | the cart state, describing which actions are allowed — the product processor checks it for permission to skip stock validation, for instance |

## The processor

Implement `Shopware\Core\Checkout\Cart\CartProcessorInterface` and its `process` method — the
guide's example class is `CustomCartProcessor`.

```php
class CustomCartProcessor implements CartProcessorInterface
{
public function process(CartDataCollection $data, Cart $original, Cart $toCalculate,
                        SalesChannelContext $context, CartBehavior $behavior): void
{
    $newData = $data->get('uniqueKey');

    foreach ($toCalculate->getLineItems()->getFlat() as $lineItem) {
        $lineItem->setPayload($newData['stuff']);
    }
}
}
```

The parameters match `collect()` with one addition, and that addition is the point: alongside
`$original` there is **`$toCalculate`**. **Make every change on `$toCalculate`** — that is the cart
which ends up being used.

## Why the split matters

**Never query data in `process()`.** It runs many times over a cart's life, so a query there
multiplies. Fetch in `collect()` instead, which is also where duplicate requests can be filtered out.

A processor's tag accepts a priority, and priority decides what it sees. Running at `4500` puts a
processor after the product processor, so the products already carry their name and price:

```php
$services->set(ExampleProcessor::class)
    ->tag('shopware.cart.processor', ['priority' => 4500]);
```

## Source

[developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/add-cart-processor-collector.html](https://developer.shopware.com/docs/guides/plugins/plugins/checkout/cart/add-cart-processor-collector.html),
Shopware 6.7, retrieved 2026-08-21.
