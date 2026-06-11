---
name: sw-message-queue
description: >
  Asynchrone Verarbeitung in Shopware 6 mit der Message Queue (Symfony Messenger): Message dispatchen (MessageBusInterface),
  async-Transport, Worker (messenger:consume), low_priority-Queue. Trigger: "Message Queue", "Messenger shopware",
  "async verarbeiten", "MessageBusInterface dispatch", "messenger:consume", "Worker shopware", "low_priority queue".
  Shopware 6.7.
---

# Shopware 6 — Message Queue

Shopware nutzt Symfony Messenger für asynchrone Tasks. Eine Message ist ein einfaches DTO; ein Handler verarbeitet sie
(siehe `sw-message-handler`). Dispatch über den Bus:

```php
$this->bus->dispatch(new FfImportMessage($id));
```

Transports: `async` (Standard) und `low_priority` (z.B. Indexing). Worker konsumiert:
`bin/console messenger:consume async low_priority`. In Produktion als Daemon (Supervisor) betreiben;
fehlgeschlagene Messages landen im `failed`-Transport (`messenger:failed:*`).

Geeignet für lange/teure Operationen (Import, Mailversand, Indexierung). Wiederkehrend zeitgesteuert → `sw-scheduled-task`.
Eigene Middleware: `sw-message-middleware`.

→ Konfiguration, Transports, Retry: [references/message-queue.md](references/message-queue.md)
