---
name: sw-message-middleware
description: >
  Eigene Messenger-Middleware in Shopware 6: MiddlewareInterface, in den Message-Bus einklinken (z.B. Logging,
  Transaktionen, Stamps). Trigger: "Messenger Middleware", "MiddlewareInterface", "message bus middleware",
  "Stamp messenger", "middleware einklinken shopware". Shopware 6.7.
---

# Shopware 6 — Messenger-Middleware

Middleware umschließt jede Message auf dem Bus (Querschnitt: Logging, Auth-Kontext, Messung).

```php
class FfLoggingMiddleware implements MiddlewareInterface
{
    public function handle(Envelope $envelope, StackInterface $stack): Envelope
    {
        // vor dem Handler
        $envelope = $stack->next()->handle($envelope, $stack);
        // nach dem Handler
        return $envelope;
    }
}
```

Registrierung über die Messenger-Bus-Konfiguration (`framework.messenger.buses.*.middleware`) bzw. Service-Tag.
Stamps (`->with(new SomeStamp())`) transportieren Metadaten. Sparsam einsetzen — die meisten Fälle lösen Handler/Events.
Bus/Transports: `sw-message-queue`.
