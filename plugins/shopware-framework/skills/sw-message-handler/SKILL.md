---
name: sw-message-handler
description: >
  Message-Handler in Shopware 6 (Symfony Messenger): Handler mit #[AsMessageHandler], __invoke(Message), Registrierung,
  Idempotenz/Fehler. Trigger: "MessageHandler", "AsMessageHandler", "__invoke message", "Handler für Message",
  "messenger handler shopware", "Message verarbeiten". Shopware 6.7.
---

# Shopware 6 — Message-Handler

Ein Handler verarbeitet eine Message asynchron (vom Worker aufgerufen).

```php
#[AsMessageHandler]
final class FfImportMessageHandler
{
    public function __construct(private readonly EntityRepository $repo) {}

    public function __invoke(FfImportMessage $message): void
    {
        // Verarbeitung; bei Exception -> Retry gemäß Messenger-Config
    }
}
```

`#[AsMessageHandler]` (oder Tag `messenger.message_handler`). **Idempotent** schreiben (Message kann erneut zugestellt
werden). Fehler werfen → automatischer Retry; dauerhaft fehlerhaft → `failed`-Transport. Eine Message → genau ein Handler
(in Shopware-Konvention). Dispatch/Transports: `sw-message-queue`. ScheduledTask-Handler sind ein Spezialfall (`sw-scheduled-task`).
