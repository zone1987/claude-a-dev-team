# Shopware 6 — Cart Collector

The collector runs **before** the processors and loads all data needed for the calculation (e.g. products,
prices) in a single batch — so processors never issue their own DB queries.

```php
class FfDataCollector implements CartDataCollectorInterface
{
    public function collect(CartDataCollection $data, Cart $original, SalesChannelContext $context, CartBehavior $behavior): void
    {
        $ids = /* LineItem references */;
        if ($data->has($key)) { return; }       // do not load twice
        $data->set($key, $this->loadOnce($ids, $context));
    }
}
```

Register via the `shopware.cart.collector` tag. Write into the `CartDataCollection`; the processor (`sw-cart-processor`)
reads it. Performance: load only missing data (`$data->has(...)`). Order via priority.
