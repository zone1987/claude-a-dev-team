---
name: sw-media-thumbnail
description: >
  Thumbnails in Shopware 6: Thumbnail-Größen je Media-Folder, ThumbnailService generieren, media_thumbnail_size,
  Regenerierung (media:generate-thumbnails). Trigger: "Thumbnail shopware", "ThumbnailService", "media_thumbnail_size",
  "Thumbnails generieren", "media:generate-thumbnails", "Bildgrößen folder". Shopware 6.7.
---

# Shopware 6 — Thumbnails

Thumbnails werden je `media_folder` über dessen `media_folder_configuration` (Thumbnail-Größen) erzeugt.

```php
$this->thumbnailService->updateThumbnails($mediaEntity, $context, false);
```

- Größen als `media_thumbnail_size` anlegen und der Folder-Configuration zuweisen (Admin: Medien-Ordner-Einstellungen).
- Erzeugung automatisch beim Upload (wenn `generateThumbnails` aktiv) bzw. per CLI `bin/console media:generate-thumbnails`.
- Im Storefront via `sw_thumbnails`/`searchMedia` ausgeben (`shopware-storefront` → `sw-storefront-assets`).

Upload/Media-Grundlagen: `sw-media-handling`. Folder-/Thumbnail-Einstellungen aus Betreibersicht: `shopware-merchant` (`sw-merchant-content-media`).
