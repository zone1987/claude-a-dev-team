# Admin API-Service-Registrierung (`src/Resources/app/administration/src/core/service/api/index.js`)

## Zweck
Registriert die fünf Admin-API-Services bei `Shopware.Service()` (jeweils mit httpClient + loginService).

## Registrierte Services
- `octoProductApiService` → `OctoProductApiService`
- `propertyApiService` → `PropertyApiService`
- `variantApiService` → `VariantApiService`
- `productMediaApiService` → `ProductMediaApiService`
- `productPriceApiService` → `ProductPriceApiService`

## Bezüge
`octo-product.api.service.js`, `property.api.service.js`, `variant.api.service.js`, `product-media.api.service.js`, `product-price.api.service.js`, Vue `sw-product-api-product-form`.
