# Media

## Overview

Plugins can add custom file extensions, prevent media deletion, handle thumbnails, and upload files programmatically.

## Uploading Media Programmatically

```php
use Shopware\Core\Content\Media\MediaService;
use Shopware\Core\Content\Media\File\MediaFile;

class MediaUploadService
{
    public function __construct(
        private readonly MediaService $mediaService,
    )
    {
    }

    public function uploadFile(
        string $filePath,
        string $fileName,
        string $mediaFolderId,
        Context $context,
    ): string {
        $mediaId = $this->mediaService->createMediaInFolder(
            $mediaFolderId,
            $context,
            false,
        );

        $mediaFile = new MediaFile(
            $filePath,
            mime_content_type($filePath),
            pathinfo($filePath, PATHINFO_EXTENSION),
            filesize($filePath),
        );

        $this->mediaService->saveMediaFile(
            $mediaFile,
            $fileName,
            $context,
            null,
            $mediaId,
        );

        return $mediaId;
    }
}
```

## Creating a Media Folder (Migration)

```php
use Shopware\Core\Framework\Uuid\Uuid;

public function update(Connection $connection): void
{
    $configurationId = Uuid::randomHex();

    $connection->insert('media_default_folder', [
        'id' => Uuid::fromHexToBytes(Uuid::randomHex()),
        'association_fields' => '["ffContentPlusItems"]',
        'entity' => 'ff_content_plus_item',
        'created_at' => (new \DateTime())->format('Y-m-d H:i:s'),
    ]);

    $connection->insert('media_folder_configuration', [
        'id' => Uuid::fromHexToBytes($configurationId),
        'create_thumbnails' => 1,
        'keep_aspect_ratio' => 1,
        'thumbnail_quality' => 80,
        'created_at' => (new \DateTime())->format('Y-m-d H:i:s'),
    ]);

    $connection->insert('media_folder', [
        'id' => Uuid::fromHexToBytes(Uuid::randomHex()),
        'name' => 'Content Plus Media',
        'media_folder_configuration_id' => Uuid::fromHexToBytes($configurationId),
        'created_at' => (new \DateTime())->format('Y-m-d H:i:s'),
    ]);
}
```

## Preventing Media Deletion

Subscribe to `UnusedMediaSearchEvent`:

```php
use Shopware\Core\Content\Media\Event\UnusedMediaSearchEvent;

class PreventMediaDeletionSubscriber implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [
            UnusedMediaSearchEvent::class => 'onUnusedMediaSearch',
        ];
    }

    public function onUnusedMediaSearch(UnusedMediaSearchEvent $event): void
    {
        // Mark media IDs as used so they won't be deleted
        $event->markAsUsed($mediaIds);
    }
}
```

## Adding Custom File Extensions

Subscribe to allow custom file types:

```php
use Shopware\Core\Content\Media\Event\MediaFileExtensionWhitelistEvent;

class AllowCustomExtensionSubscriber implements EventSubscriberInterface
{
    public static function getSubscribedEvents(): array
    {
        return [
            MediaFileExtensionWhitelistEvent::class => 'onWhitelist',
        ];
    }

    public function onWhitelist(MediaFileExtensionWhitelistEvent $event): void
    {
        $whitelist = $event->getWhitelist();
        $whitelist[] = 'webp';
        $whitelist[] = 'avif';
        $event->setWhitelist($whitelist);
    }
}
```

## Thumbnail Sizes

Configure thumbnail sizes in the media folder configuration or define them in migration:

```php
$connection->insert('media_thumbnail_size', [
    'id' => Uuid::fromHexToBytes(Uuid::randomHex()),
    'width' => 400,
    'height' => 400,
    'created_at' => (new \DateTime())->format('Y-m-d H:i:s'),
]);
```
