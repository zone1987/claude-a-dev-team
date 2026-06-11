# VariantController (`src/Controller/VariantController.php`)

## Zweck
Admin-Endpunkt, der aus einer Property-Group die Shopware-**Produktvarianten** eines OCTO-Produkts erzeugt/synchronisiert (eine Variante pro Property-Group-Option), inkl. Configurator-Settings, Manufacturer und Aufräumen verwaister Varianten. **Wird auch vom ResubmissionAppServer aufgerufen** (`AdminApiClient::generateVariants` → `POST /api/product-variants/create`) — zentraler Cross-Repo-Vertrag.

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class VariantController extends AbstractController`
- Klassen-Route-Scope: `AdministrationRouteScope`.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$logger` | `OctoLoggerInterface` | Logging. |
| `$propertyGroupRepository` | `EntityRepository` | (injiziert). |
| `$productRepository` | `EntityRepository` | Varianten upsert/delete. |
| `$mediaService` | `MediaService` | Manufacturer-Logo-Upload. |

## Routen / öffentliche Methoden
### `createProductVariants(Request, Context): JsonResponse`
- **Route:** `POST /api/product-variants/create`, name `api.product-variant.create`.
- Erwartet `apiProduct`, `propertyGroup`, `product` (mit `id`); sonst 400.
- Ermittelt Manufacturer (`getManufacturer`), lädt bestehende Varianten (Filter `parentId=product.id`), indexiert per `productNumber`.
- Baut Parent-Update-DataItem mit `configuratorSettings` (je Option deterministische ID via `getConfiguratorSettingsId`), optional `manufacturer`.
- Pro Option: Varianten-ID = bestehende (nach `productNumber` `{number}.{n}`) oder deterministisch `Uuid::fromStringToHex("{product.id}-{option.id}")`; Variante mit `parentId`, `productNumber`, `stock=1`, `name` (title/internalName), `prices`, `price`, `options`.
- `productRepository->upsert($data)`. Danach **verwaiste Varianten löschen** (alle bestehenden, die nicht in `keptVariantIds`).
- **Rückgabe:** `{success:true}` 200.

### `private getManufacturer(apiProduct): ?array`
Bildet Hersteller je Identifier: GoldenTours (`brand.name` + `logoUrl`), Demo (`brand.name`), RheinKurier/GoCity (`brand` als String). Lädt Logo hoch (Media-Folder `product_manufacturer`). Deterministische ID via `getManufacturerId`. Null wenn kein Brand/Name.

### `private getConfiguratorSettingsId(product, option): string`
`Uuid::fromStringToHex("{product.id}-{option.id}-configurator-settings")`.

### `private getManufacturerId(identifier): string`
`Uuid::fromStringToHex("{identifier}-manufacturer")`.

## Besonderheiten / Fallstricke
- **Cross-Repo:** Der AppServer ruft diese Route für RheinKurier-Produkte; ändert sich Route, Payload-Form (`apiProduct`/`propertyGroup`/`product`) oder das deterministische ID-Schema, brechen die Offline-Produkte im AppServer. Siehe `../appserver-integration.md`.
- Varianten-Löschung ist destruktiv (alles nicht-Gehaltene unter dem Parent).

## Bezüge
`Service/MediaService.php`, Clients (`*Client::IDENTIFIER`), `../appserver-integration.md`, Admin-Service `variant.api.service.js`, `controllers.xml`.
