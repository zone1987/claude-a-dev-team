# SessionService (`src/Service/SessionService.php`)

## Zweck
Kapselt den Zugriff auf die Symfony-Session (set/get/remove) für OCTO-Session-Items. Genutzt von Controllern und dem Cart-Collector.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `class SessionService`

## Methoden
### `setItem(SessionInterface, key, value): array`
Setzt + `save()`, gibt `session->all()` zurück. (Signatur: `$value` typisiert als `string`.)

### `getItem(SessionInterface, key): mixed`
Entfernt den Key, wenn vorhanden aber leer; wirft `Exception` wenn nicht (mehr) vorhanden; sonst Wert.

### `removeItem(SessionInterface, key): mixed`
Entfernt den Key falls vorhanden (Rückgabe des entfernten Werts), sonst `null`.

## Besonderheiten / Fallstricke
- `getItem` wirft bewusst, wenn der Key fehlt — Aufrufer fangen das (warning) und liefern Defaults.
- **Session überlebt Login nicht** (Shopware regeneriert die Session) — `octo-product-session-*` gehen verloren; relevant für Checkout/E2E.

## Bezüge
`Controller/SessionController.php`, `Controller/AvailbilityController.php`, `Core/Checkout/Cart/OctoCartCollector.php`, `../session-management.md`.
