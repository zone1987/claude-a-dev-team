# Shopware 6 — Filesystem (Flysystem)

Shopware wraps storage in League\Flysystem. Two default filesystems:
`shopware.filesystem.public` (web-reachable, e.g. media) and `shopware.filesystem.private` (not public).

```xml
<argument type="service" id="shopware.filesystem.private"/>
```
```php
$this->privateFilesystem->write('exports/data.csv', $contents);
$stream = $this->privateFilesystem->readStream('exports/data.csv');
```

Register your own plugin filesystem via `shopware.filesystem` + `config/packages`; adapters (local, S3, …)
are configurable without code changes. For media always use the media system (`sw-media-handling`).

→ Adapter config, custom filesystem, examples: [FILESYSTEM-DETAIL.md](FILESYSTEM-DETAIL.md)
