# Shopware 6 — Message Queue

Shopware uses Symfony Messenger for asynchronous tasks. A message is a simple DTO; a handler processes it
(see `sw-message-handler`). Dispatch through the bus:

```php
$this->bus->dispatch(new FfImportMessage($id));
```

Transports: `async` (default) and `low_priority` (e.g. indexing). The worker consumes:
`bin/console messenger:consume async low_priority`. In production run it as a daemon (Supervisor);
failed messages end up in the `failed` transport (`messenger:failed:*`).

Suitable for long/expensive operations (import, mail sending, indexing). Recurring on a schedule → `sw-scheduled-task`.
Own middleware: `sw-message-middleware`.

→ Configuration, transports, retry: [MESSAGE-QUEUE-DETAIL.md](MESSAGE-QUEUE-DETAIL.md)
