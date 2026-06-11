# Filesystem

## Overview

Plugins can access the filesystem using Flysystem adapters. Shopware provides pre-configured filesystem services for public and private storage.

## Available Filesystems

| Service ID | Purpose |
|-----------|---------|
| `shopware.filesystem.public` | Public files (accessible via URL) |
| `shopware.filesystem.private` | Private files (not web-accessible) |
| `shopware.filesystem.theme` | Theme assets |
| `shopware.filesystem.asset` | Plugin/bundle assets |
| `shopware.filesystem.sitemap` | Sitemap files |

## Using the Filesystem

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Service;

use League\Flysystem\FilesystemOperator;
use Shopware\Core\Framework\Log\Package;

#[Package('custom-plugins')]
class FileService
{
    public function __construct(
        private readonly FilesystemOperator $filesystemPublic,
        private readonly FilesystemOperator $filesystemPrivate,
    )
    {
    }

    public function writePublicFile(string $path, string $content): void
    {
        $this->filesystemPublic->write($path, $content);
    }

    public function readPrivateFile(string $path): string
    {
        return $this->filesystemPrivate->read($path);
    }

    public function deleteFile(string $path): void
    {
        $this->filesystemPrivate->delete($path);
    }

    public function fileExists(string $path): bool
    {
        return $this->filesystemPublic->fileExists($path);
    }

    public function listFiles(string $directory): array
    {
        $listing = $this->filesystemPublic->listContents($directory);

        $files = [];
        foreach ($listing as $item) {
            $files[] = $item->path();
        }

        return $files;
    }
}
```

## Service Registration

```xml
<service id="FfContentPlus\Service\FileService">
    <argument type="service" id="shopware.filesystem.public"/>
    <argument type="service" id="shopware.filesystem.private"/>
</service>
```

## Plugin-Specific Storage

Create a plugin-specific directory to avoid conflicts:

```php
// Use a plugin-prefixed path
$this->filesystemPublic->write(
    'ff-content-plus/exports/report.csv',
    $csvContent,
);
```

## Common Operations

| Method | Description |
|--------|------------|
| `write(path, content)` | Write/overwrite file |
| `read(path)` | Read file content |
| `delete(path)` | Delete file |
| `fileExists(path)` | Check if file exists |
| `listContents(dir)` | List directory contents |
| `move(from, to)` | Move/rename file |
| `copy(from, to)` | Copy file |
| `createDirectory(path)` | Create directory |
| `mimeType(path)` | Get MIME type |
| `fileSize(path)` | Get file size |
| `lastModified(path)` | Get last modified timestamp |
