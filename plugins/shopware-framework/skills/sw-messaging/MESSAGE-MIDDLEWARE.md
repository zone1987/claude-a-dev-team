# Shopware 6 — Messenger middleware

Middleware wraps every message on the bus (cross-cutting: logging, auth context, measurement).

```php
class FfLoggingMiddleware implements MiddlewareInterface
{
    public function handle(Envelope $envelope, StackInterface $stack): Envelope
    {
        // before the handler
        $envelope = $stack->next()->handle($envelope, $stack);
        // after the handler
        return $envelope;
    }
}
```

Registration through the Messenger bus configuration (`framework.messenger.buses.*.middleware`) or a service tag.
Stamps (`->with(new SomeStamp())`) carry metadata. Use sparingly — most cases are solved by handlers/events.
Bus/transports: `sw-message-queue`.
