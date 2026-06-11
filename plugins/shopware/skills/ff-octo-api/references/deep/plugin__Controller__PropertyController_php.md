# PropertyController (`src/Controller/PropertyController.php`)

## Zweck
Admin-Endpunkt, der aus den Optionen eines OCTO-API-Produkts eine Shopware-Property-Group (für Varianten) erzeugt. Delegiert an `PropertyService::createPropertyGroup`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class PropertyController extends AbstractController`
- Klassen-Route-Scope: `AdministrationRouteScope`.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$propertyService` | `PropertyService` | Property-Group-Erstellung. |

## Routen / öffentliche Methoden
### `createPropertyGroup(Request, Context): JsonResponse`
- **Route:** `POST /api/property-group/create`, name `api.property-group.create`.
- Liest `apiProduct` (muss array sein, sonst 400).
- Ruft `propertyService->createPropertyGroup($apiProduct, $context)`.
- **Rückgabe:** `{propertyGroup: …}` 200.

## Besonderheiten
- Die erzeugten Property-Group-/Option-IDs sind deterministisch (`Uuid::fromStringToHex` in `PropertyService`).

## Bezüge
`Service/PropertyService.php`, `Command/PropertyGroupCleanupCommand.php`, Admin-Service `property.api.service.js`, `controllers.xml`.
