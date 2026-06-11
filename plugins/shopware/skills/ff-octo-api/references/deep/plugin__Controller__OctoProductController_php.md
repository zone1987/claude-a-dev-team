# OctoProductController (`src/Controller/OctoProductController.php`)

## Zweck
Admin-Controller, der die in der Admin-Produktanlage verfügbaren OCTO-API-Produkte bereitstellt: listet alle API-Produkte je Supplier (mit „bereits verwendet"-Flag) und liefert ein einzelnes API-Produkt im Detail.

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class OctoProductController extends AbstractController`
- Klassen-Route-Scope: `AdministrationRouteScope`.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$clientRegistry` | `OctoApiClientRegistry` | Supplier-Clients. |
| `$logger` | `OctoLoggerInterface` | Logging. |
| `$productRepository` | `EntityRepository` | (injiziert). |
| `$octoProductRepository` | `EntityRepository` | `ff_octo_product` (bereits verwendete IDs). |

## Routen / öffentliche Methoden
### `listProducts(): JsonResponse`
- **Route:** `GET /api/octo/products`, name `api.octo.product.list`.
- Holt bereits verwendete IDs (`getUsedApiProductIds`), iteriert alle Supplier-Identifier.
- Nur Online-Clients: Capability `octo/content`, `getCachedProducts(cacheExpirationTime)`.
- **GoCity-Sonderregel:** nur Produkte deren `reference` mit `LON` beginnt (London-Filter).
- Baut je Produkt deterministische `id = Uuid::fromStringToHex("{product.id}-{reference}-{identifier}")`, Flag `disabled` wenn bereits verwendet.
- **Rückgabe:** Map `product.id` → {uuid, id, disabled, identifier, product.title}. Bei Exception 400 + warning.

### `getProduct(Request, Context): JsonResponse`
- **Route:** `POST /api/octo/product`, name `api.octo.product`.
- Liest `identifier`, `uuid`; Capabilities `octo/content,octo/pricing`; `getCachedProduct(uuid)`.
- Baut dieselbe deterministische `id`. **Rückgabe:** {uuid, id, identifier, product(=voller API-Response)}.
- **Fallstrick:** Fängt `\Throwable` (nicht nur `Exception`), weil fehlende identifier/uuid einen `TypeError` aus dem Registry werfen → bewusst 400 statt 500.

### `private getClient(identifier, acceptLanguage, availableLanguage): CachedOctoApiClientInterface`
Delegiert an `clientRegistry->getClientByIdentifier`.

### `private getUsedApiProductIds(): array`
`octoProductRepository->searchIds(...)` über alle `ff_octo_product`.

## Bezüge
`OctoApiClientRegistry`, `CachedOctoApiClientInterface`, Admin-Service `octo-product.api.service.js`, Vue `sw-product-api-product-form`, `controllers.xml`.
