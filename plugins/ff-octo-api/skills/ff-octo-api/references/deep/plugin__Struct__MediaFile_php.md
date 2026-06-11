# MediaFile (`src/Struct/MediaFile.php`)

## Zweck
Wertobjekt für eine herunterzuladende Mediendatei: leitet aus einer URL Dateiname, Endung, Pfad und eine deterministische Media-ID ab. Genutzt vom `MediaService` beim Medienimport.

## Typ & Vererbung
- Namespace: `FfOctoApi\Struct`
- `class MediaFile`

## Properties
| Property | Typ | Bedeutung |
|----------|-----|-----------|
| `$url` | string (readonly, ctor) | Quell-URL. |
| `$filename` | string | Aus URL-Pfad (`PATHINFO_FILENAME`). |
| `$extension` | string | Aus URL (`PATHINFO_EXTENSION`), Fallback `jpg`. |
| `$path` | string | `{filename}.{extension}`. |
| `$id` | string | `Uuid::fromStringToHex("{path}-{uniqueIdentifier}")`. |

## Konstruktor
`__construct(string $url, string $uniqueIdentifier)` — parst die URL und berechnet obige Werte.

## Methoden
Getter: `getFilename()`, `getExtension()`, `getPath()`, `getId()`, `getUrl()`.

## Besonderheiten
- Deterministische ID → idempotenter Medienimport pro URL+Identifier.

## Bezüge
`Service/MediaService.php`, `Controller/MediaController.php`.
