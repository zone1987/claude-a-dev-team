# Shopware 6 — Flow trigger (event)

Triggers in the Flow Builder are business events that implement `FlowEventAware` and expose data via aware
interfaces.

```php
class FfThingHappenedEvent extends Event implements FlowEventAware, OrderAware
{
    public static function getName(): string { return 'ff.thing.happened'; }
    public function getOrderId(): string { return $this->order->getId(); }
    // the BusinessEventCollector picks it up as a trigger automatically
}
```

Dispatch the event (`sw-events-subscriber`/a service). So actions receive the data, register a `FlowStorer`
(it puts data into the `StorableFlow`) — actions read it via the aware interface (`sw-flow-action`). Scalar values are
possible since the ADR "flow storer with scalar values".
