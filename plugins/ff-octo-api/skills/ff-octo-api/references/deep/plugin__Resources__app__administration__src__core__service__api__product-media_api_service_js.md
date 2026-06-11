# ProductMediaApiService (Admin) (`src/Resources/app/administration/src/core/service/api/product-media.api.service.js`)

## Zweck
Admin-API-Service zur Medienzuweisung. Pendant zu `MediaController`.

## Typ & Vererbung
- `class ProductMediaApiService extends ApiService`, `apiEndpoint='/product-media'`, `name='productMediaApiService'`.

## Routen/Methoden
- `ROUTES.ASSIGN='/product-media/assign'`.
- `assignProductMedia(apiProduct, product)` — POST `/product-media/assign`.

## Bezüge
`Controller/MediaController.php`, Vue `sw-product-api-product-form`.
