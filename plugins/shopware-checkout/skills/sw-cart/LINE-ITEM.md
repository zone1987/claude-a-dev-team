# Shopware 6 — Cart LineItem

A cart position is a `LineItem` (type e.g. `product`, `promotion`, `custom`/your own type). Add it through
the `CartService` or the Store API.

```php
$lineItem = $this->lineItemFactory->create([
    'type' => LineItem::PRODUCT_LINE_ITEM_TYPE, 'referencedId' => $productId, 'quantity' => 2,
], $context);
$this->cartService->add($cart, $lineItem, $context);
```

Register custom types through a `LineItemFactoryHandler`. The payload carries your own data; the processor calculates
the price (never set it directly). Nested positions (bundles/sets): `sw-nested-line-items`. Add/remove in the
storefront or headless through the Store API (`shopware-api` → `sw-store-api-endpoints`).
