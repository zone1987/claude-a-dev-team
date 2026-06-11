# VariantApiService (Admin) (`src/Resources/app/administration/src/core/service/api/variant.api.service.js`)

## Zweck
Admin-API-Service zur Varianten-Erzeugung. Pendant zu `VariantController` (auch vom AppServer genutzte Route).

## Typ & Vererbung
- `class VariantApiService extends ApiService`, `apiEndpoint='/product-variants'`, `name='variantApiService'`.

## Routen/Methoden
- `ROUTES.CREATE='/product-variants/create'`.
- `createProductVariants(apiProduct, propertyGroup, product)` — POST `/product-variants/create`.

## Bezüge
`Controller/VariantController.php`, Vue `sw-product-api-product-form`, `../appserver-integration.md`.
