# MediaController (`src/Controller/MediaController.php`)

## Zweck
Admin-Controller, der Medien (Cover-, Galerie-, Banner-Bilder) eines OCTO-API-Produkts herunterlädt, in die Shopware-Media-Bibliothek importiert und dem Shopware-Produkt zuweist (inkl. Cover). Wird aus der Admin-Produktanlage (Vue) aufgerufen.

## Typ & Vererbung
- Namespace: `FfOctoApi\Controller`
- `class MediaController extends AbstractController` (Symfony FrameworkBundle, nicht StorefrontController)
- Klassen-Route-Scope: `AdministrationRouteScope`.

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$productRepository` | `EntityRepository` | Produkt-Upsert (Media/Cover). |
| `$mediaService` | `MediaService` | Download/Upload/Lookup von Medien. |

## Routen / öffentliche Methoden
### `assignProductMedia(Request, Context): JsonResponse`
- **Route:** `POST /api/product-media/assign`, name `api.product-media.assign`.
- Erwartet `apiProduct` (array) + `product` (array mit `id`); sonst 400.
- Lädt Shopware-Produkt (`mediaService->getProductById`); 404 wenn fehlt.
- Sammelt `coverImageUrl`, `galleryImages`, `bannerImages` (via `mediaService->getImageUrlsByKey`), ermittelt Media-Folder der `product`-Entity.
- Lädt jedes Bild hoch (`mediaService->uploadMedia`), baut Media-Liste mit deterministischen IDs (`Uuid::fromStringToHex`), setzt Positionen, optional Cover.
- Upsert des Produkts mit `media` + `cover`, wenn etwas vorhanden.
- **Rückgabe:** `{success:true}` 200.
- **Fallstrick:** Banner-Media-ID nutzt `fromStringToHex(productId-mediaFolderId)` (nicht die Bild-URL) → bei mehreren Bannern potenziell kollidierende `id` derselben Produkt-Media-Zuordnung.

## Bezüge
`Service/MediaService.php`, `Struct/MediaFile.php`, Admin-Service `product-media.api.service.js`, `controllers.xml`.
