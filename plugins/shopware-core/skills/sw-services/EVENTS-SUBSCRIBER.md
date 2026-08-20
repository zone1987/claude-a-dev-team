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

**Welches Event?** Projekt-Event-Katalog nutzen (`sw-event-catalog` / `/sw-event-map`) — listet alle Events mit
Klasse, Dispatch-Ort und Argumenten/Payload.

→ Events finden, alle Event-Typen, Datenmanipulation, Beispiele: [EVENTS-SUBSCRIBER-SUBSCRIBERS.md](EVENTS-SUBSCRIBER-SUBSCRIBERS.md)
→ Gerüst: [examples/EventSubscriber.php](examples/EventSubscriber.php)
