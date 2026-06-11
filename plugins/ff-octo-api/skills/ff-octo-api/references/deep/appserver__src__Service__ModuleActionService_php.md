# ModuleActionService (`ResubmissionAppServer/src/Service/ModuleActionService.php`)

## Zweck
Baut die signierten URL-Parameter für die Iframe-Module (Shop-ID/-URL, Timestamp, Versionen, Sprachen) inklusive HMAC-SHA256-Signatur mit dem Shop-Secret — damit die Vue-Frontends authentifizierte Requests an den AppServer stellen können.

## Typ
- Namespace `App\Service`, `class ModuleActionService`.

## Methoden
- `buildParameters(ModuleAction $module): string` — baut Query-Params (`shop-id`, `shop-url`, `timestamp`, `sw-version`, `app-version` `1.0.0`, `in-app-purchases`, `sw-context-language`, `sw-user-language`), hängt `shopware-shop-signature` (HMAC-SHA256 über die Query mit `shop->getShopSecret()`) an.

## Besonderheiten
- Signatur entspricht dem Shopware-App-Iframe-Mechanismus; das `shop_secret` stammt aus dem Manifest/`shop`-Entity.

## Bezüge
`Controller/{Resubmission,CustomProduct}Controller.php`, `templates/*`, `manifest.xml`.
