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

→ Media-Details: [MEDIA.md](MEDIA.md)
