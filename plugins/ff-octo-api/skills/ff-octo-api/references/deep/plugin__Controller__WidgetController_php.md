# WidgetController (`src/Controller/WidgetController.php`)

## Zweck
Minimaler Storefront-Controller, der die gesendeten Request-Daten unverändert als JSON zurückspiegelt — vermutlich Hilfs-/Debug-Endpunkt für das Unit-Widget des Buy-Widgets.

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class WidgetController extends StorefrontController`
- Klassen-Route-Scope: `StorefrontRouteScope`.

## Routen / öffentliche Methoden
### `unitWidget(Request): Response`
- **Route:** `POST /octo-api/widget/unit`, name `frontend.octo-api.widget.unit`, `XmlHttpRequest=true`, `_httpCache=false`.
- Gibt `request->request->all()` als `JsonResponse` (200) zurück (Echo).

## Besonderheiten
- Enthält keine Logik — beim Aufräumen prüfen, ob noch genutzt.

## Bezüge
`buy-widget/widget/unit-widget.html.twig`, `controllers.xml`.
