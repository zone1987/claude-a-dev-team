# Shopware 6 — Filesystem (Flysystem)

Shopware kapselt Storage über League\Flysystem. Zwei Standard-Filesysteme:
`shopware.filesystem.public` (web-erreichbar, z.B. Medien) und `shopware.filesystem.private` (nicht öffentlich).

```xml
<argument type="service" id="shopware.filesystem.private"/>
```
```php
$this->privateFilesystem->write('exports/data.csv', $contents);
$stream = $this->privateFilesystem->readStream('exports/data.csv');
```

Eigenes Plugin-Filesystem via `shopware.filesystem` + `config/packages` registrierbar; Adapter (local, S3, …)
sind konfigurierbar, ohne Code zu ändern. Für Medien immer das Media-System nutzen (`sw-media-handling`).

→ Adapter-Konfig, eigenes Filesystem, Beispiele: [FILESYSTEM-DETAIL.md](FILESYSTEM-DETAIL.md)
