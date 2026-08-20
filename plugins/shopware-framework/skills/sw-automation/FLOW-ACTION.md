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

→ Flow-Builder-Details: [FLOW-ACTION-FLOW-BUILDER.md](FLOW-ACTION-FLOW-BUILDER.md) · Beispiel: [examples/FlowAction.php](examples/FlowAction.php)
