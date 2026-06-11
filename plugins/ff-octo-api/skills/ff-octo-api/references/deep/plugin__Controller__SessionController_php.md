# SessionController (`src/Controller/SessionController.php`)

## Zweck
Storefront-Endpunkte zum Lesen/Schreiben/Löschen von OCTO-Session-Items (Schlüssel-Wert), genutzt vom Buy-Widget-JS zur Persistenz des Auswahl-States.

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class SessionController extends StorefrontController`
- Klassen-Route-Scope: `StorefrontRouteScope`.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$logger` | `OctoLoggerInterface` | Logging. |
| `$sessionService` | `SessionService` | Session-Zugriff. |

## Routen / öffentliche Methoden
### `setItem(Request): Response`
- **Route:** `POST /octo-api/session/set`, name `frontend.octo-api.session.set-item`, `XmlHttpRequest=true`, `_httpCache=false`.
- `sessionService->setItem(session, key, value)`. Rückgabe: 200 (leer).

### `getItem(Request): JsonResponse`
- **Route:** `POST /octo-api/session/get`, name `frontend.octo-api.session.get-item`.
- `sessionService->getItem(session, key)`; bei Exception 400 + warning. Rückgabe: Wert 200.

### `removeItem(Request): JsonResponse`
- **Route:** `POST /octo-api/session/remove`, name `frontend.octo-api.session.remove-item`.
- `sessionService->removeItem(session, key)`. Rückgabe: 200 (leer).

## Besonderheiten
- Session-Items überleben einen Login nicht (Shopware regeneriert die Session) — relevant für Checkout/E2E.

## Bezüge
`Service/SessionService.php`, `../session-management.md`, Storefront-JS `octo-api.service.js`, `controllers.xml`.
