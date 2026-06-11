# OctoProductApiService (Admin) (`src/Resources/app/administration/src/core/service/api/octo-product.api.service.js`)

## Zweck
Admin-API-Service, der die verfügbaren OCTO-API-Produkte lädt (Liste + Einzelprodukt). Pendant zu `OctoProductController`.

## Typ & Vererbung
- `class OctoProductApiService extends ApiService` (Shopware), `apiEndpoint='/octo'`, `name='octoProductApiService'`.

## Routen/Methoden
- `ROUTES`: `PRODUCTS='/octo/products'`, `PRODUCT='/octo/product'`.
- `getProducts()` — GET `/octo/products`.
- `getProduct(uuid, identifier)` — POST `/octo/product`.

## Bezüge
`Controller/OctoProductController.php`, Vue `sw-product-api-product-form`, `index.js`.
