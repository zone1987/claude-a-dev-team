# Shopware 6 — domain exceptions

Instead of many individual exception classes: **one factory per domain** with static methods that return typed
exceptions with a stable `errorCode` (ADR "domain-exceptions").

```php
class FfExampleException extends HttpException
{
    public const NOT_FOUND = 'FF_EXAMPLE__NOT_FOUND';

    public static function notFound(string $id): self
    {
        return new self(Response::HTTP_NOT_FOUND, self::NOT_FOUND, 'Example "{{ id }}" not found.', ['id' => $id]);
    }
}
```
```php
throw FfExampleException::notFound($id);
```

`errorCode` is stable (clients and tests match on it, not on the message). Pick a fitting HTTP status per method.
The log level is configurable (ADR "exception log levels"). API responses expose `code`/`detail` (`shopware-api` → `sw-api-errors`).
Extends `HttpException`/`ShopwareHttpException`.
