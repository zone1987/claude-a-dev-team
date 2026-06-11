# PriceController (`src/Controller/PriceController.php`)

## Zweck
Admin-Endpunkt, der die Preisaktualisierung eines OCTO-Produkts anstößt (aus der Admin-Produktanlage). Delegiert an `PriceService::updatePrices`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class PriceController extends AbstractController`
- Klassen-Route-Scope: `AdministrationRouteScope`.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$priceService` | `PriceService` | Preisberechnung/-update. |

## Routen / öffentliche Methoden
### `updateProductPrices(Request, Context): JsonResponse`
- **Route:** `POST /api/product-price/update`, name `api.product-price.update`.
- Liest `apiProduct` (array|null), `identifier`, `productId`.
- Validiert `productId` + `identifier` als nicht-leere Strings (sonst 400).
- Ruft `priceService->updatePrices($productId, $identifier, is_array($apiProduct) ? $apiProduct : null)`.
- **Rückgabe:** `{success:true}` 200.

## Besonderheiten
- `apiProduct` darf null sein (dann lädt/ermittelt `PriceService` die Daten selbst — relevant für Offline/RheinKurier).

## Bezüge
`Service/PriceService.php`, Admin-Service `product-price.api.service.js`, `controllers.xml`.
