---
name: sw-domain-exceptions
description: >
  Domain-Exceptions in Shopware 6 (ADR domain-exceptions): pro Domäne eine Exception-Factory-Klasse mit statischen
  Factory-Methoden, stabile error-codes, HttpException-Mapping, Log-Level. Trigger: "Domain Exception", "Exception Factory",
  "error code shopware", "HttpException domain", "eigene Exception shopware", "ShopwareHttpException". Shopware 6.7.
---

# Shopware 6 — Domain-Exceptions

Statt vieler einzelner Exception-Klassen: **eine Factory pro Domäne** mit statischen Methoden, die typisierte
Exceptions mit stabilem `errorCode` liefern (ADR „domain-exceptions").

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

`errorCode` ist stabil (Clients/Tests matchen darauf, nicht auf die Message). HTTP-Status pro Methode passend.
Log-Level steuerbar (ADR „exception log levels"). In API-Antworten erscheint `code`/`detail` (`shopware-api` → `sw-api-errors`).
Erweitert `HttpException`/`ShopwareHttpException`.
