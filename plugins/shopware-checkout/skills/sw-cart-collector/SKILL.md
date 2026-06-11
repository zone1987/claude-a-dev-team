---
name: sw-cart-collector
description: >
  Eigener Cart-Collector in Shopware 6: CartDataCollectorInterface, Daten für die Warenkorb-Berechnung vorab laden
  (collect) und in die CartDataCollection legen. Trigger: "Cart Collector", "CartDataCollectorInterface", "collect cart",
  "Warenkorb Daten laden", "CartDataCollection", "cart.collector tag". Shopware 6.7.
---

# Shopware 6 — Cart-Collector

Der Collector läuft **vor** den Processoren und lädt alle Daten, die zur Berechnung gebraucht werden (z.B. Produkte,
Preise), gebündelt — damit Processoren keine eigenen DB-Queries machen.

```php
class FfDataCollector implements CartDataCollectorInterface
{
    public function collect(CartDataCollection $data, Cart $original, SalesChannelContext $context, CartBehavior $behavior): void
    {
        $ids = /* LineItem-Referenzen */;
        if ($data->has($key)) { return; }       // nicht doppelt laden
        $data->set($key, $this->loadOnce($ids, $context));
    }
}
```

Registrierung via `shopware.cart.collector`-Tag. In die `CartDataCollection` schreiben; der Processor (`sw-cart-processor`)
liest sie. Performance: nur fehlende Daten laden (`$data->has(...)`). Reihenfolge über Priorität.
