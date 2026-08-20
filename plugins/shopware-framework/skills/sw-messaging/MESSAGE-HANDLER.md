# Shopware 6 — Message handler

A handler processes a message asynchronously (invoked by the worker).

```php
#[AsMessageHandler]
final class FfImportMessageHandler
{
    public function __construct(private readonly EntityRepository $repo) {}

    public function __invoke(FfImportMessage $message): void
    {
        // Processing; on exception -> retry according to the Messenger config
    }
}
```

`#[AsMessageHandler]` (or the tag `messenger.message_handler`). Write it **idempotently** (a message can be delivered
again). Throw errors → automatic retry; permanently failing → `failed` transport. One message → exactly one handler
(by Shopware convention). Dispatch/transports: `sw-message-queue`. ScheduledTask handlers are a special case (`sw-scheduled-task`).
