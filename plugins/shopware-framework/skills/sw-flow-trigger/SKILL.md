---
name: sw-flow-trigger
description: >
  Eigene Flow-Builder-Trigger (Business-Events) in Shopware 6 bereitstellen: FlowEventAware-Event, Aware-Interfaces,
  Event als Flow-Trigger registrieren, Storer. Trigger: "Flow Trigger", "eigenes Flow-Event", "FlowEventAware",
  "Business Event flow", "Aware interface flow", "flow.storer", "Trigger registrieren flow". Shopware 6.7.
---

# Shopware 6 — Flow-Trigger (Event)

Trigger im Flow Builder sind Business-Events, die `FlowEventAware` implementieren und über Aware-Interfaces Daten
bereitstellen.

```php
class FfThingHappenedEvent extends Event implements FlowEventAware, OrderAware
{
    public static function getName(): string { return 'ff.thing.happened'; }
    public function getOrderId(): string { return $this->order->getId(); }
    // BusinessEventCollector erfasst es automatisch als Trigger
}
```

Das Event dispatchen (`sw-events-subscriber`/Service). Damit Actions die Daten erhalten, ein `FlowStorer` registrieren
(legt Daten in den `StorableFlow`) — Actions lesen sie via Aware-Interface (`sw-flow-action`). Skalare Werte sind
seit ADR „flow storer with scalar values" möglich.
