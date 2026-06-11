---
name: sw-custom-sorting
description: >
  Eigene Sortier-Option für das Produkt-Listing in Shopware 6: ProductSortingEntity per Migration/Fixture anlegen,
  Felder + Richtung, im Listing verfügbar machen. Trigger: "Custom Sorting", "ProductSortingEntity", "Sortierung Listing",
  "product_sorting", "eigene Sortieroption", "listing sort option". Shopware 6.7.
---

# Shopware 6 — Custom-Sorting (Listing)

Sortier-Optionen im Listing sind Daten (`product_sorting`), keine Code-Klassen. Neue Option per Migration/Repository
anlegen.

```php
$this->productSortingRepo->upsert([[
    'key' => 'ff-popularity',
    'priority' => 5,
    'active' => true,
    'fields' => [['field' => 'product.ffPopularity', 'order' => 'desc', 'priority' => 1, 'naturalSorting' => 0]],
    'label' => 'Beliebtheit',
]], $context);
```

`fields` referenzieren DAL-Felder (auch eigene via Extension). Übersetzungen über `product_sorting_translation`.
Die Option erscheint automatisch im Sortier-Dropdown. Filter dazu: `sw-listing-filter`.
