# Contao Filesystem (5.x)

> **Experimentell:** Die neuen Filesystem-Klassen sind mit `@experimental` markiert und nicht durch Contaos BC-Promise abgedeckt.
> Legacy-Klassen (`\Contao\File`, `\Contao\Folder`, `\Contao\FilesModel`, `\Contao\Dbafs`) funktionieren weiterhin.

---

## Architektur-Überblick

| Komponente | Zweck | Level |
|-----------|-------|-------|
| `VirtualFilesystem` | Primärer Gateway für Lese-/Schreiboperationen | Hoch |
| `MountManager` | Verwaltet mehrere Adapter nach Mount-Pfad | Niedrig |
| `DbafsManager` | Verwaltet Metadaten und UUID-basierten Ressourcenzugriff | Niedrig |

**Basis:** Flysystem (`League\Flysystem`) – unterstützt lokale FS, Dropbox, AWS S3, FTP u.a.

---

## VirtualFilesystem

### Autowiring

```php
// Dateiname des VirtualFilesystem: "files" → Autowire-Name: "filesStorage"
class Example
{
    public function __construct(
        private VirtualFilesystemInterface $filesStorage
    ) {}
}
```

Alternativ explizit: `contao.filesystem.virtual.files`

### UUIDs als Pfad

```php
use Symfony\Component\Uid\Uuid;

$filesStorage->read('my/file.txt');
$filesStorage->read(new Uuid('94cc007c-8cc0-11ec-a8a3-0242ac120002'));
```

### Operations-Referenz

#### Tests
```php
fileExists(string|Uuid $path, int $accessFlags = 0): bool
directoryExists(string|Uuid $path, int $accessFlags = 0): bool
has(string|Uuid $path, int $accessFlags = 0): bool
```

#### Lesen / Schreiben / Löschen
```php
read(string|Uuid $path): string
readStream(string|Uuid $path): resource
write(string|Uuid $path, string $contents, array $options = []): void
writeStream(string|Uuid $path, resource $stream, array $options = []): void
delete(string|Uuid $path): void
deleteDirectory(string|Uuid $path): void
```

#### Erstellen / Kopieren / Verschieben
```php
createDirectory(string $path, array $options = []): void
copy(string|Uuid $source, string $destination, array $options = []): void
move(string|Uuid $source, string $destination, array $options = []): void
```

#### Auflisten
```php
listContents(string|Uuid $path, bool $deep = false, int $accessFlags = 0): FilesystemItemIterator
```
Liefert Generator mit `FilesystemItem`-Objekten – filterbar via `.files()` / `.directories()`.

#### Metadaten
```php
getLastModified(string|Uuid $path, int $accessFlags = 0): int
getFileSize(string|Uuid $path, int $accessFlags = 0): int
getMimeType(string|Uuid $path, int $accessFlags = 0): string
getExtraMetadata(string|Uuid $path, int $accessFlags = 0): array
setExtraMetadata(string|Uuid $path, array $metadata): void
```

### Access-Flags

| Flag | Wirkung |
|------|---------|
| `VirtualFilesystemInterface::BYPASS_DBAFS` | Direkt aus MountManager lesen |
| `VirtualFilesystemInterface::FORCE_SYNC` | DBAFS-Synchronisation erzwingen |

Kombination: `FORCE_SYNC|BYPASS_DBAFS`

### Exception-Handling

Alle Operationen werfen `VirtualFilesystemException` bei Fehler. UUID-Auflösung wirft zusätzlich `UnableToResolveUuidException`.

### Beispiel – Verzeichnisinhalt auflisten

```php
#[AsContentElement(category: 'files')]
class FilesListController extends AbstractContentElementController
{
    public function __construct(private VirtualFilesystemInterface $filesStorage) {}

    protected function getResponse(FragmentTemplate $template, ContentModel $model, Request $request): Response
    {
        $template->set('elements', $this->describeDirectory('images'));
        return $template->getResponse();
    }

    private function describeDirectory(string $directory): array
    {
        if (!$this->filesStorage->directoryExists($directory)) {
            return [];
        }

        $files = [];
        foreach ($this->filesStorage->listContents($directory)->files() as $item) {
            $name         = $item->getPath();
            $size         = $item->getFileSize() / 1000;
            $fileMetadata = $item->getExtraMetadata()['metadata']['en'] ?? null;

            if ($fileMetadata instanceof Metadata && ($title = $fileMetadata->getTitle()) !== '') {
                $name = "'$title' ($name)";
            }
            $files[] = "$name has a size of {$size}kB.";
        }
        return $files;
    }
}
```

---

## Filesystem-Konfiguration

### In einem Bundle (ConfigureFilesystemInterface)

```php
class MyFooBundleExtension extends Extension implements ConfigureFilesystemInterface
{
    public function configureFilesystem(FilesystemConfiguration $config): void
    {
        // API-Aufrufe hier
    }
}
```

### In einer Applikation (CompilerPass)

```php
class Plugin implements ConfigPluginInterface
{
    public function registerContainerConfiguration(LoaderInterface $loader, array $managerConfig)
    {
        $configureFilesystemPass = new class implements CompilerPassInterface {
            public function process(ContainerBuilder $container): void
            {
                $config = new FilesystemConfiguration($container);
                // API-Aufrufe hier
            }
        };
    }
}
```

### FilesystemConfiguration API

| Methode | Beschreibung |
|---------|-------------|
| `addVirtualFilesystem($name, $prefix, $readOnly)` | Erstellt Service `contao.filesystem.virtual.{name}` |
| `mountAdapter($type, $options, $path)` | Adapter in MountManager einbinden |
| `mountLocalAdapter($path, $mountPath)` | Shortcut für lokale Adapter |
| `registerDbafs($service, $prefix)` | DBAFS-Service registrieren |
| `addDefaultDbafs($prefix, $table, $hashFn, $trackLastModified)` | Standard-DBAFS anlegen |

### Beispiel: SFTP Remote-Backup

```php
$config->mountAdapter(
    'sftp',
    ['host' => 'example.com', 'port' => 22, 'username' => 'foobar', 'password' => 's3cr3t'],
    'backups'
);
```

---

## DBAFS (Database-Assisted Filesystem)

Reichert Dateien mit Metadaten aus der `tl_files`-Tabelle an (Autor, Lizenz, Alt-Text, Bildunterschriften). Jede Ressource erhält eine globale UUID.

---

*Quellen:*
- *https://docs.contao.org/5.x/dev/framework/filesystem/*
- *https://docs.contao.org/5.x/dev/framework/filesystem/config/*
- *https://docs.contao.org/5.x/dev/framework/filesystem/virtual-filesystem/*
