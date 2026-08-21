# Shopware 6 — Thumbnails

Thumbnails are generated per `media_folder` via its `media_folder_configuration` (thumbnail sizes).

```php
$this->thumbnailService->updateThumbnails($mediaEntity, $context, false);
```

- Create sizes as `media_thumbnail_size` and assign them to the folder configuration (admin: media folder settings).
- Generated automatically on upload (if `generateThumbnails` is active) or via CLI `bin/console media:generate-thumbnails`.
- Output in the storefront via `sw_thumbnails`/`searchMedia` (`shopware-storefront` → `sw-storefront-assets`).

Upload/media basics: `sw-media-handling`. Folder/thumbnail settings from an operator's perspective: `shopware-merchant` (`sw-merchant-content-media`).
