# Shopware 6 — Listing filter (facet)

Hook custom filters into the product listing through two events (subscriber):

1. `ProductListingCriteriaEvent` → add the aggregation and (when the request parameter is active) the filter to the criteria.
2. `ProductListingResultEvent` → attach the current selection/available values from the aggregation result to the result.

```php
public function onCriteria(ProductListingCriteriaEvent $event): void
{
    $criteria = $event->getCriteria();
    $criteria->addAggregation(new EntityAggregation('manufacturer', 'manufacturerId', 'product_manufacturer'));
    // apply the active filter from the request ...
}
```

In the storefront, render/activate the filter via the `filter-panel` template plus a JS plugin (`FilterBasePlugin`).
Aggregations: `sw-aggregations`. Custom sortings: `sw-custom-sorting`.
