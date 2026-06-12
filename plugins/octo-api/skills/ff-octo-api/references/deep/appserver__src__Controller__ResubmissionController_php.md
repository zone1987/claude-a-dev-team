# ResubmissionController (`ResubmissionAppServer/src/Controller/ResubmissionController.php`)

## Zweck
Iframe-Controller für die Wiedervorlagen-Verwaltung in der Shopware-Admin. Listet/filtert/sortiert Bestellungen nach Resubmission-Status, bearbeitet die Resubmission-Custom-Fields und togglet den Status.

## Typ
- Namespace `App\Controller`, `#[AsController]`, `extends AbstractController`.

## Konstruktor / DI
`AdminApiService $adminApiService`, `ModuleActionService $moduleActionService`.

## Routen / Methoden
- `index` — `GET /resubmission` → `resubmission/index.html.twig`.
- `add` — `GET /resubmission/add` → `resubmission/add.html.twig`.
- `edit` — `GET /resubmission/{id}/edit` → lädt Order-CustomFields (`getOrder`), `resubmission/edit.html.twig`.
- `editPost` — `POST /resubmission/{id}/edit` → `setOrderCustomField(id, {resubmission_active/_date/_note/_user})`.
- `getOrders` — `POST /resubmission/orders` → filtert nach `customFields.resubmission_active` (true / false|null), optional User-Filter (`resubmission_user`), Sortierung (mapped `resubmissionDate`→`customFields.resubmission_date` etc.). `adminClient->getOrders`.
- `toggleOrder` — `POST /resubmission/order/{id}/{resubmissionState}/toggle` → invertiert `resubmission_active`.
- `getUsers` — `POST /resubmission/users` → `adminClient->getUsers(filter)`.

## Besonderheiten / Fallstricke
- **Die Custom-Field-Namen** (`resubmission_active/_date/_note/_user`) stammen aus dem `FfResubmission`-Manifest und korrespondieren mit `CheckoutService::confirmOrder` (Plugin setzt `resubmission_active` bei fehlgeschlagener Bestätigung).
- Sort-/Filter-Felder sind Shopware-DAL-Pfade (`customFields.*`).

## Bezüge
`Service/AdminApiClient.php` (`getOrders`/`getOrder`/`setOrderCustomField`/`getUsers`), `templates/resubmission/*`, FfOctoApi `Service/CheckoutService.php`, `../appserver-integration.md`.
