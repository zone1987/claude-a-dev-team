# CustomProductController (`ResubmissionAppServer/src/Controller/CustomProductController.php`)

## Zweck
Iframe-Controller für die RheinKurier-Produktverwaltung in der Shopware-Admin. Listet/paginiert Produkte, rendert Add-/Edit-Formulare und legt Produkte über `AdminApiClient` an/bearbeitet sie.

## Typ
- Namespace `App\Controller`, `#[AsController]`, `extends AbstractController`.

## Konstruktor / DI
`ModuleActionService $moduleActionService`, `AdminApiService $adminApiService`.

## Routen / Methoden
- `index` — `GET /customProductTemplate` → `customProduct/index.html.twig` (mit signierten urlParams).
- `indexPost` — `POST /customProductTemplate` → paginierte/sortierte Produkte (`adminClient->getProducts`).
- `add` — `GET /customProductTemplate/add` → `customProduct/add.html.twig`.
- `edit` — `GET /customProductTemplate/{id}/edit` → lädt Produkt (`getProduct`), `customProduct/edit.html.twig`.
- `editTemplate` — `POST /customProductTemplate/edit` → `adminClient->editProduct(id, name, octoProductId, uuid, options)`.
- `addTemplate` — `POST /customProductTemplate/add` → `adminClient->addProduct(name, options)`.
- `getCurrency` — `POST /customProductTemplate/currency` → `adminClient->getCurrency()`.

## Besonderheiten
- `options` kommen als JSON-String aus dem Vue-Formular (`custom-product-form.vue`) und werden dekodiert.
- Jeder Request erzeugt über `AdminApiService->createClient(shopUrl, clientId, clientSecret)` einen frischen Admin-Client (Shop-Kontext aus `ModuleAction`).

## Bezüge
`Service/AdminApiService.php`, `Service/AdminApiClient.php`, `Service/ModuleActionService.php`, `templates/customProduct/*`, `assets/vue/controllers/custom-product/*`.
