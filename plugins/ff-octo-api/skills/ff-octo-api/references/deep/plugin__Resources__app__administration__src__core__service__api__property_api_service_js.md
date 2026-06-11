# PropertyApiService (Admin) (`src/Resources/app/administration/src/core/service/api/property.api.service.js`)

## Zweck
Admin-API-Service zur Property-Group-Erzeugung. Pendant zu `PropertyController`.

## Typ & Vererbung
- `class PropertyApiService extends ApiService`, `apiEndpoint='/property-group'`, `name='propertyApiService'`.

## Routen/Methoden
- `ROUTES.CREATE='/property-group/create'`.
- `createPropertyGroup(apiProduct)` — POST `/property-group/create`.

## Bezüge
`Controller/PropertyController.php`, Vue `sw-product-api-product-form`.
