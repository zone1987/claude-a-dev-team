# Shopware 6 — Events & Subscribers

The **preferred** extension path. A subscriber implements `EventSubscriberInterface` and is registered via
the `kernel.event_subscriber` tag (or autoconfiguration).

```php
public static function getSubscribedEvents(): array
{
    return [
        ProductEvents::PRODUCT_WRITTEN_EVENT => 'onProductWritten',
        // Storefront: ProductPageLoadedEvent::class => 'onProductPage',
    ];
}
```

Event kinds: **entity events** (`{entity}.written/.deleted/.loaded`), **business events** (checkout, order, mail …),
**page loaded events** (storefront, → `sw-storefront-data`), **kernel events**. Priorities: `[ 'method', 100 ]`.

**Which event?** Use the project event catalogue (`sw-event-catalog` / `/sw-event-map`) — it lists every event with its
class, dispatch location and arguments/payload.

→ Finding events, all event types, data manipulation, examples: [EVENTS-SUBSCRIBER-SUBSCRIBERS.md](EVENTS-SUBSCRIBER-SUBSCRIBERS.md)
→ Skeleton: [examples/EventSubscriber.php](examples/EventSubscriber.php)
