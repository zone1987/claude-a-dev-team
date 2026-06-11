---
name: sw-media-handling
description: >
  Medien in Shopware 6 programmatisch verwalten: MediaService (Upload aus Datei/URL/Stream), media.repository, Ordner
  (media_folder), Media an Entities hängen, MediaType. Trigger: "Media hochladen", "MediaService", "media.repository",
  "Bild speichern shopware", "media folder", "Datei zu Media", "saveFile media". Shopware 6.7.
---

# Shopware 6 — Media-Handling

Medien sind DAL-Entities (`media`) mit Datei im Filesystem (`shopware.filesystem.public`). Upload über den `MediaService`.

```php
$mediaId = Uuid::randomHex();
$this->mediaRepo->create([['id' => $mediaId, 'mediaFolderId' => $folderId]], $context);
$this->mediaService->saveFile($contents, 'jpg', 'image/jpeg', $fileName, $context, 'product', $mediaId);
// per URL: $this->mediaService->saveMediaFromUrl(...) bzw. DownloadResponseGenerator
```

Medien organisieren über `media_folder` (mit Thumbnail-Konfiguration). An eine Entity hängen über deren Media-Association
(z.B. `product_media`). Eigene Media-Felder in Custom-Entities via `sw-field-types` (Fk auf `media`). Thumbnails: `sw-media-thumbnail`.

→ Media-Details: [references/media.md](references/media.md)
