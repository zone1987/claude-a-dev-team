# Shopware 6 — Media handling

Media are DAL entities (`media`) with the file in the filesystem (`shopware.filesystem.public`). Upload via the `MediaService`.

```php
$mediaId = Uuid::randomHex();
$this->mediaRepo->create([['id' => $mediaId, 'mediaFolderId' => $folderId]], $context);
$this->mediaService->saveFile($contents, 'jpg', 'image/jpeg', $fileName, $context, 'product', $mediaId);
// by URL: $this->mediaService->saveMediaFromUrl(...) or DownloadResponseGenerator
```

Organise media via `media_folder` (with thumbnail configuration). Attach to an entity via that entity's media association
(e.g. `product_media`). Custom media fields in custom entities via `sw-field-types` (FK to `media`). Thumbnails: `sw-media-thumbnail`.

→ Media details: [MEDIA.md](MEDIA.md)
