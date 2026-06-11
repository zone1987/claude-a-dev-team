---
name: sw-cart-line-item
description: >
  LineItems im Shopware-6-Warenkorb: LineItem erzeugen/hinzufügen (LineItemFactory/CartService), Typen (product/promotion/
  custom), Payload, Label/Quantity/Preis, eigener LineItem-Typ. Trigger: "LineItem", "Warenkorb-Position", "addLineItem",
  "LineItemFactoryRegistry", "custom line item", "cart add product", "LineItem payload". Shopware 6.7.
---

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
