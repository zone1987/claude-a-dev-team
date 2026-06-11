# ProductPriceApiService (Admin) (`src/Resources/app/administration/src/core/service/api/product-price.api.service.js`)

## Zweck
Admin-API-Service zum Preis-Update. Pendant zu `PriceController`.

## Typ & Vererbung
- `class ProductPriceApiService extends ApiService`, `apiEndpoint='/product-price'`, `name='productPriceApiService'`.

## Routen/Methoden
- `ROUTES.UPDATE='/product-price/update'`.
- `updateProductPrices(apiProduct, productId, identifier)` — POST `/product-price/update`.

## Bezüge
`Controller/PriceController.php`, `Service/PriceService.php`, Vue `sw-product-api-product-form`.
