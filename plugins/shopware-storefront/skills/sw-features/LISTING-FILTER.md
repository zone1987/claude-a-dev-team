# Shopware 6 — Listing-Filter (Facette)

Eigene Filter ins Produkt-Listing einhängen über zwei Events (Subscriber):

1. `ProductListingCriteriaEvent` → Aggregation + (bei aktivem Request-Param) Filter zur Criteria hinzufügen.
2. `ProductListingResultEvent` → aktuelle Auswahl/verfügbare Werte aus dem Aggregations-Ergebnis ans Result hängen.

```php
public function onCriteria(ProductListingCriteriaEvent $event): void
{
    $criteria = $event->getCriteria();
    $criteria->addAggregation(new EntityAggregation('manufacturer', 'manufacturerId', 'product_manufacturer'));
    // aktiven Filter aus Request anwenden ...
}
```

Im Storefront den Filter über das `filter-panel`-Template + ein JS-Plugin (`FilterBasePlugin`) rendern/aktivieren.
Aggregationen: `sw-aggregations`. Eigene Sortierungen: `sw-custom-sorting`.
