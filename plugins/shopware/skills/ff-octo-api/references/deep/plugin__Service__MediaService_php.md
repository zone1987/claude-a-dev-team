# MediaService (`src/Service/MediaService.php`)

## Zweck
Importiert und verwaltet Medien aus OCTO-API-Produktdaten: extrahiert Bild-URLs, ermittelt Media-Folder, lädt Bilder per URL hoch und liefert (idempotente) Media-IDs. `readonly`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `readonly class MediaService`

## Properties
| Property | Typ | Bedeutung |
|----------|-----|-----------|
| `$mediaCollection` | `MediaCollection` | Im Konstruktor geladene Liste aller Medien (für Existenzprüfungen). |

## Konstruktor / DI
`EntityRepository $productRepository`, `$mediaRepository`, `$mediaFolderRepository`, `MediaUploadService $mediaUploadService`. Lädt `mediaCollection`.

## Methoden
- `getImageUrlsByKey(apiProduct, key): array` — sammelt `product[key][].url` (z.B. `galleryImages`, `bannerImages`).
- `getMediaFolderIdByEntity(entity): ?string` — Folder-ID per `defaultFolder.entity`.
- `getMediaCollection(): MediaCollection|EntityCollection` — alle Medien.
- `getProductById(id, context): ?ProductEntity` — Produkt mit `children`.
- `getExistingMediaId(url): ?string` — sucht Media per Dateiname (aus URL).
- `uploadMedia(url, mediaId, mediaFolderId, ?context): void` — lädt nur hoch, wenn `mediaId` noch nicht existiert (`uploadFromURL`).
- `getMediaId(url, uniqueIdentifier): ?string` — bestehende ID (per Dateiname) **oder** deterministische `Uuid::fromStringToHex("{url}-{uniqueIdentifier}")`.

## Besonderheiten / Fallstricke
- `mediaCollection` wird einmalig im Konstruktor geladen → innerhalb desselben Requests neu hochgeladene Medien sind dort nicht enthalten.
- Idempotenz über Dateiname/deterministische ID.

## Bezüge
`Controller/MediaController.php`, `Controller/VariantController.php` (Manufacturer-Logo), `Struct/MediaFile.php`.
