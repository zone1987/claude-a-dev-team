---
name: sw-nested-line-items
description: >
  Verschachtelte LineItems in Shopware 6 (Bundles/Sets): children-Collection, Preisaggregation über Kinder,
  Anzeige/Berechnung. Trigger: "nested line items", "verschachtelte Position", "Bundle Warenkorb", "LineItem children",
  "line item set", "Unterpositionen cart". Shopware 6.7.
---

# Shopware 6 — Verschachtelte LineItems

LineItems können `children` haben (ADRs „nested line items"/„new nested line items") — z.B. ein Bundle mit
Unterprodukten. Der Preis des Parent kann aus den Kindern aggregiert oder eigenständig sein.

```php
$bundle = new LineItem($id, 'ff_bundle', $referencedId, 1);
$bundle->setChildren(new LineItemCollection([$childA, $childB]));
$bundle->getChildren()->add($childC);
```

Im Processor (`sw-cart-processor`) die Kinder berechnen und den Parent-Preis bilden. Im Storefront werden Kinder
eingerückt dargestellt. Verfügbarkeit/Validierung berücksichtigt die Kinder (`sw-cart-validator`). Standard-Positionen:
`sw-cart-line-item`.
