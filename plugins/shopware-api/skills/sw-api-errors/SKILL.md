---
name: sw-api-errors
description: >
  Fehlerformat & Status-Codes der Shopware-6-APIs: JSON:API errors-Array (status, code, title, detail, source.pointer),
  typische HTTP-Codes (400/401/403/404/412/500), Validierungsfehler, Domain-Exception-Codes. Trigger: "API Fehler",
  "errors array api", "source pointer api", "401 403 api shopware", "Validierungsfehler api", "error code shopware api".
  Shopware 6.7.
---

# Shopware 6 — API-Fehler

Fehler kommen als JSON mit `errors`-Array (JSON:API-Stil):

```json
{ "errors": [ {
  "status": "400",
  "code": "FRAMEWORK__WRITE_CONSTRAINT_VIOLATION",
  "title": "Bad Request",
  "detail": "This value should not be blank.",
  "source": { "pointer": "/0/name" }
} ] }
```

Wichtige Codes:
| HTTP | Bedeutung |
|---|---|
| 400 | Validierung/Constraint, fehlerhafter Body |
| 401 | nicht/abgelaufen authentifiziert (Token erneuern) |
| 403 | fehlende ACL-/Scope-Rechte |
| 404 | Entity/Route nicht gefunden |
| 409/412 | Versionskonflikt / Precondition |
| 500 | Serverfehler |

`code` ist der stabile Domain-Exception-Code (`shopware-quality` → `sw-domain-exceptions`) — auf den `code` matchen,
nicht auf `detail`. `source.pointer` zeigt das fehlerhafte Feld (Index im Sync/Batch).
