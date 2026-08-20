# Shopware 6 — API-Header & Kontext

| Header | Wirkung |
|---|---|
| `Authorization: Bearer {token}` | Admin-API-Auth (`sw-admin-api-auth`) |
| `sw-access-key` | Store-API: Sales-Channel-Zugang (`sw-store-api-auth`) |
| `sw-context-token` | Store-API: Kontext-/Warenkorb-/Login-Status |
| `Content-Type: application/json` | JSON-Body |
| `Accept: application/json` | einfaches JSON; `application/vnd.api+json` = **JSON:API** (mit `included`/`relationships`) |
| `sw-language-id` | Sprache des Requests (Übersetzungen) |
| `sw-currency-id` | Währung |
| `sw-version-id` | Entity-Version (z.B. Order-Draft, `sw-entity-versioning`) |
| `sw-inheritance` | `1` = geerbte Werte auflösen (Varianten/Parent) |

Standard-Antwortformat ist „plain" JSON (`data`/`total`); mit `Accept: application/vnd.api+json` liefert die API das
JSON:API-Format. Fehlerformat: `sw-api-errors`. Suche/Criteria: `sw-admin-api-search`.
