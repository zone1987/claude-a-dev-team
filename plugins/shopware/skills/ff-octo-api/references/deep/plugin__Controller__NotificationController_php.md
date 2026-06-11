# NotificationController (`src/Controller/NotificationController.php`)

## Zweck
Storefront-Controller, der eine Flash-Nachricht (direkter Text oder übersetzter Snippet-Key) setzt — vom Storefront-JS genutzt, um serverseitig erzeugte Hinweise im nächsten Request anzuzeigen.

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class NotificationController extends StorefrontController`, `declare(strict_types=1)`
- Klassen-Route-Scope: `StorefrontRouteScope`.

## Routen / öffentliche Methoden
### `notify(Request, SalesChannelContext): Response`
- **Route:** `POST /notification/notify`, name `frontend.notification.send`, `XmlHttpRequest=true`.
- Umhüllt von `Profiler::trace('notification::create', …)`.
- Liest `message`, `snippet`, `parameters` (JSON, Default `{}`), `type` (Default `self::INFO`).
- Wirft `InvalidArgumentException`, wenn weder `message` noch `snippet` gesetzt.
- `message` → `addFlash($type, $message)`; `snippet` → `addFlash($type, $this->trans($snippet, $parameters))`.
- **Rückgabe:** `createActionResponse($request)`.

## Bezüge
Storefront-JS-Services (`octo-api.service.js`), `controllers.xml`.
