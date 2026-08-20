# Shopware 6 — API errors

Errors arrive as JSON with an `errors` array (JSON:API style):

```json
{ "errors": [ {
  "status": "400",
  "code": "FRAMEWORK__WRITE_CONSTRAINT_VIOLATION",
  "title": "Bad Request",
  "detail": "This value should not be blank.",
  "source": { "pointer": "/0/name" }
} ] }
```

Important codes:
| HTTP | Meaning |
|---|---|
| 400 | validation/constraint, malformed body |
| 401 | not authenticated / expired (renew the token) |
| 403 | missing ACL/scope permissions |
| 404 | entity/route not found |
| 409/412 | version conflict / precondition |
| 500 | server error |

`code` is the stable domain exception code (`shopware-quality` → `sw-domain-exceptions`) — match on `code`,
not on `detail`. `source.pointer` points at the offending field (index in sync/batch).
