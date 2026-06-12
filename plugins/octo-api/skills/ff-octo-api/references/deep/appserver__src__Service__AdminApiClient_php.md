# AdminApiClient (`ResubmissionAppServer/src/Service/AdminApiClient.php`)

## Zweck
Zentrale HTTP-Client-Klasse des ResubmissionAppServers gegen die **Shopware Admin API** (OAuth2). Liest/schreibt Bestellungen (Wiedervorlagen-Custom-Fields) und RheinKurier-Produkte (inkl. `ffOctoProduct`), und ruft die FfOctoApi-Plugin-Endpunkte (Property-Group, Varianten) auf. **Cross-Repo-Kern.** `readonly`.

## Typ
- Namespace `App\Service` — `readonly class AdminApiClient`.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$httpClient` | `HttpClientInterface` | HTTP. |
| `$shopUrl` | string | Shop-Basis-URL (aus `Shop`-Entity). |
| `$clientId` / `$clientSecret` | string | OAuth-Credentials des Shops. |
(Erzeugt durch `AdminApiService` pro Shop-Kontext.)

## Methoden
- `getAuthToken(grantType='client_credentials')` — `POST /api/oauth/token`, gibt `access_token` (Exception wenn fehlt).
- `getOrders(page, limit, filter=[], sortBy=[])` — `POST /api/search/order` (umfangreiche Associations: billing/salesChannel/orderCustomer/currency/documents/state/transaction/delivery…). Mapped JSON:API → flaches Array (orderNumber, customerName, shippingAddress, amountTotal, Status-Felder, orderDateTime, `customFields`, total).
- `getOrder(orderId)` — `GET /api/order/{id}`, gibt nur die Resubmission-Custom-Fields (`resubmission_active/_date/_note/_user`).
- `setOrderCustomField(orderId, customField)` — `PATCH /api/order/{id}` mit `customFields`; gibt Statuscode.
- `getUsers(filter=[])` — `POST /api/search/user`.
- `getProducts(page, limit, sortBy=[])` — `POST /api/search/product`, **Filter `ffOctoProduct.identifier == 'rheinkurier'`** (hardcodiert), Assoc `ffOctoProduct`; mapped → {id, name, productNumber, octoProduct, total}.
- `getProduct(id)` — `POST /api/search/product` (Filter id), Assoc `ffOctoProduct`; mapped Einzelprodukt inkl. `octoProduct` (id + attributes).
- `getTax()` / `getCurrency()` (private) — `GET /api/tax` / `/api/currency`.
- `reserveProductNumber()` (private) — `GET /api/_action/number-range/reserve/product`.
- `ensureOptionAndUnitIds(options)` (private) — vergibt fehlende Option-/Unit-IDs (`Uuid::v4`, Units `unit_…`).
- **`addProduct(name, octoOptions=[])`** — reserviert Nummer, ermittelt 19%-Tax + System-Currency, baut `ffOctoProduct` (id = `fromStringToHex("{uuid}-GTP2-rheinkurier")`, `identifier='rheinkurier'`, `reference='GTP2'`, brand `Rhein-Kurier`, TZ `Europe/Berlin`, options), `POST /api/product` (inaktiv, Preis 0), dann `generateVariants(...)`. Gibt Produkt-ID.
- **`editProduct(id, name, octoProductId, uuid, octoOptions=[])`** — baut `ffOctoProduct` (mit übergebener id/uuid), `PATCH /api/product/{id}`, dann `generateVariants(...)`. Gibt Statuscode.
- `createPropertyGroup(apiProduct)` — `POST /api/property-group/create` (= FfOctoApi `PropertyController`), gibt `propertyGroup`.
- `createProductVariants(apiProduct, product, property)` — `POST /api/product-variants/create` (= FfOctoApi `VariantController`).
- **`generateVariants(apiProduct, product)`** — ruft `createPropertyGroup` + `createProductVariants` (die Naht zum Plugin).

## Besonderheiten / Fallstricke
- **Cross-Repo-Vertrag:** `/api/property-group/create` und `/api/product-variants/create` sind FfOctoApi-Plugin-Routen; die `ffOctoProduct`-Struktur (`options`/`units`) muss zu `OctoProductDefinition` + `PriceService`-Erwartung passen. Änderungen beidseitig.
- Hardcodiert: `identifier='rheinkurier'`, `reference='GTP2'`, brand `Rhein-Kurier`, TZ `Europe/Berlin`, 19%-Tax.
- `addProduct`-`id`-Schema (`fromStringToHex("{uuid}-GTP2-rheinkurier")`) muss mit `PriceService::getApiProductOptions`/`PropertyService`-ID-Berechnung konsistent sein.
- `getProduct` mergt `id` in das octoProduct (für späteres `editProduct`).

## Bezüge
`AdminApiService`, `Controller/{Resubmission,CustomProduct}Controller.php`, `Util/Uuid.php`, FfOctoApi `VariantController`/`PropertyController`/`OctoProductDefinition`/`PriceService`, `../appserver-integration.md`.
