---
name: sw-write-events
description: >
  Das Shopware-6 DAL-Write-System & seine Events: EntityWrittenEvent, EntityWrittenContainerEvent, BeforeWriteEvent,
  EntityDeletedEvent, auf Schreibvorgänge reagieren. Trigger: "EntityWrittenEvent", "Write-Event", "on entity written",
  "EntityWrittenContainerEvent", "beim Speichern reagieren", "BeforeWriteEvent", "EntityDeletedEvent". Shopware 6.7.
---

# Shopware 6 — Write-System & Events

Jeder Write (`create/update/upsert/delete`) durchläuft den `EntityWriter` und dispatcht Events — der saubere
Weg, um auf Datenänderungen zu reagieren (statt Polling/Decorator).

```php
public static function getSubscribedEvents(): array
{
    return [
        'ff_example.written' => 'onWritten',          // EntityWrittenEvent (eine Entity)
        EntityWrittenContainerEvent::class => 'onAny', // alle Entities eines Writes
        'ff_example.deleted' => 'onDeleted',
    ];
}
public function onWritten(EntityWrittenEvent $event): void {
    foreach ($event->getWriteResults() as $r) { $id = $r->getPrimaryKey(); $payload = $r->getPayload(); }
}
```

`{entity}.written/.deleted` für gezielte Reaktion; Container-Event für transaktionsweite Sicht. Validierung/
Manipulation vor dem Schreiben über `PreWriteValidationEvent`/`BeforeWriteEvent`. Schwere Folgeaktionen async (`sw-message-queue`).

→ Write-Pipeline, Commands, alle Events: [references/write-system.md](references/write-system.md)
