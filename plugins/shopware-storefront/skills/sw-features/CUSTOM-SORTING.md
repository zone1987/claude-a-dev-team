# Shopware 6 — Custom sorting (listing)

Sorting options in the listing are data (`product_sorting`), not code classes. Create a new option via
migration/repository.

```php
$this->productSortingRepo->upsert([[
    'key' => 'ff-popularity',
    'priority' => 5,
    'active' => true,
    'fields' => [['field' => 'product.ffPopularity', 'order' => 'desc', 'priority' => 1, 'naturalSorting' => 0]],
    'label' => 'Popularity',
]], $context);
```

`fields` reference DAL fields (including your own via extension). Translations via `product_sorting_translation`.
The option appears in the sorting dropdown automatically. Matching filters: `sw-listing-filter`.
