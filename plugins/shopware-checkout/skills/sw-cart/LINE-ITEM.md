# Shopware 6 — Cart-LineItem

Eine Warenkorb-Position ist ein `LineItem` (Typ z.B. `product`, `promotion`, `custom`/eigener Typ). Hinzufügen über
den `CartService` bzw. die Store-API.

```php
$lineItem = $this->lineItemFactory->create([
    'type' => LineItem::PRODUCT_LINE_ITEM_TYPE, 'referencedId' => $productId, 'quantity' => 2,
], $context);
$this->cartService->add($cart, $lineItem, $context);
```

Eigene Typen über einen `LineItemFactoryHandler` registrieren. Payload trägt eigene Daten; Preis wird vom Processor
berechnet (nie hart setzen). Verschachtelte Positionen (Bundles/Sets): `sw-nested-line-items`. Add/Remove im
Storefront/Headless über die Store-API (`shopware-api` → `sw-store-api-endpoints`).
