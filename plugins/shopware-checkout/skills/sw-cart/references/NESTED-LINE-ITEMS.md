# Shopware 6 — Nested LineItems

Line items can have `children` (ADRs "nested line items"/"new nested line items") — e.g. a bundle with
sub-products. The parent price can be aggregated from the children or stand on its own.

```php
$bundle = new LineItem($id, 'ff_bundle', $referencedId, 1);
$bundle->setChildren(new LineItemCollection([$childA, $childB]));
$bundle->getChildren()->add($childC);
```

Calculate the children in the processor (`sw-cart-processor`) and derive the parent price. The storefront renders
children indented. Availability/validation takes the children into account (`sw-cart-validator`). Standard positions:
`sw-cart-line-item`.
