# Shopware 6 — Flow action

An action runs in the Flow Builder in reaction to a trigger (event).

```php
class FfNotifyAction extends FlowAction
{
    public static function getName(): string { return 'action.ff.notify'; }
    public function requirements(): array { return [OrderAware::class]; }
    public function handleFlow(StorableFlow $flow): void
    {
        if (!$flow->hasData(OrderAware::ORDER_ID)) { return; }
        // run the action (e.g. an external notification)
    }
}
```

Registration via the `flow.action` tag. `requirements()` declares the required aware interfaces (data from the trigger).
Since "transactional flow actions", actions run after the business process (`sw-flow-transaction`). Register an admin
component for configuration. Triggers/events: `sw-flow-trigger`.

→ Flow Builder details: [FLOW-ACTION-FLOW-BUILDER.md](FLOW-ACTION-FLOW-BUILDER.md) · Example: [examples/FlowAction.php](examples/FlowAction.php)
