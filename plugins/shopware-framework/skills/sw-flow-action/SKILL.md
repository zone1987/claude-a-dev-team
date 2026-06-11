---
name: sw-flow-action
description: >
  Eigene Flow-Builder-Action in Shopware 6: FlowAction (extends FlowAction / AppFlowAction), requirements/keys, handle(),
  Admin-Komponente, Registrierung. Trigger: "Flow Action", "Flow Builder Aktion", "eigene Flow-Action", "FlowAction handle",
  "requirements flow", "flow action registrieren". Shopware 6.7. Scaffolder: /sw-flow-action.
---

# Shopware 6 — Flow-Action

Eine Action wird im Flow Builder als Reaktion auf einen Trigger (Event) ausgeführt.

```php
class FfNotifyAction extends FlowAction
{
    public static function getName(): string { return 'action.ff.notify'; }
    public function requirements(): array { return [OrderAware::class]; }
    public function handleFlow(StorableFlow $flow): void
    {
        if (!$flow->hasData(OrderAware::ORDER_ID)) { return; }
        // Aktion ausführen (z.B. externe Benachrichtigung)
    }
}
```

Registrierung via `flow.action`-Tag. `requirements()` deklariert benötigte Aware-Interfaces (Daten aus dem Trigger).
Seit „transactional flow actions" laufen Actions nach dem Geschäftsprozess (`sw-flow-transaction`). Admin-Komponente
für Konfiguration registrieren. Trigger/Events: `sw-flow-trigger`.

→ Flow-Builder-Details: [references/flow-builder.md](references/flow-builder.md) · Beispiel: [examples/FlowAction.php](examples/FlowAction.php)
