# Shopware 6 — Criteria sorting

```php
$criteria->addSorting(new FieldSorting('createdAt', FieldSorting::DESCENDING));
$criteria->addSorting(new FieldSorting('name', FieldSorting::ASCENDING, true)); // naturalSorting
// sort by aggregate/count:
$criteria->addSorting(new CountSorting('lines.id', CountSorting::DESCENDING));
```

Multiple sortings apply in the order they are added. Reach fields across associations with dot notation. To sort
within a loaded association, use `$criteria->getAssociation('lines')->addSorting(...)`.

→ Sorting reference: [SORTING-SEARCH-CRITERIA.md](SORTING-SEARCH-CRITERIA.md)
