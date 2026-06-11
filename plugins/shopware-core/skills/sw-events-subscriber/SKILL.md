---
name: sw-events-subscriber
description: >
  Auf Shopware-6-Events reagieren mit EventSubscriberInterface: Business-Events, Entity-/Write-Events,
  Storefront-Page-Loaded-Events, Kernel-Events; Events finden und Prioritäten setzen.
  Trigger: "EventSubscriber", "auf Event reagieren", "subscribe to event", "getSubscribedEvents",
  "entity written event", "PageLoadedEvent", "welches Event", "event listener shopware". Shopware 6.7.
---

# Shopware 6 — Events & Subscriber

Der **bevorzugte** Erweiterungsweg. Subscriber implementiert `EventSubscriberInterface`, wird via
`kernel.event_subscriber`-Tag (oder Autoconfigure) registriert.

```php
public static function getSubscribedEvents(): array
{
    return [
        ProductEvents::PRODUCT_WRITTEN_EVENT => 'onProductWritten',
        // Storefront: ProductPageLoadedEvent::class => 'onProductPage',
    ];
}
```

Event-Arten: **Entity-Events** (`{entity}.written/.deleted/.loaded`), **Business-Events** (Checkout, Order, Mail …),
**Page-Loaded-Events** (Storefront, → `sw-storefront-data`), **Kernel-Events**. Prioritäten: `[ 'method', 100 ]`.

→ Events finden, alle Event-Typen, Datenmanipulation, Beispiele: [references/subscribers.md](references/subscribers.md)
→ Gerüst: [examples/EventSubscriber.php](examples/EventSubscriber.php)
