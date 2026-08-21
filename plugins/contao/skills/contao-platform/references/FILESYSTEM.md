# Contao Filesystem (5.x)

> **Experimental:** The new filesystem classes are marked `@experimental` and are not covered by Contao's BC promise.
> Legacy classes (`\Contao\File`, `\Contao\Folder`, `\Contao\FilesModel`, `\Contao\Dbafs`) continue to work.

---

## Contents

- [Architecture overview](#architecture-overview)
- [VirtualFilesystem](#virtualfilesystem)
- [Filesystem configuration](#filesystem-configuration)
- [DBAFS (Database-Assisted Filesystem)](#dbafs-database-assisted-filesystem)

## Architecture overview

| Component | Purpose | Level |
|-----------|-------|-------|
| `VirtualFilesystem` | Primary gateway for read/write operations | High |
| `MountManager` | Manages multiple adapters by mount path | Low |
| `DbafsManager` | Manages metadata and UUID-based resource access | Low |

**Foundation:** Flysystem (`League\Flysystem`) – supports the local FS, Dropbox, AWS S3, FTP and others.

---

## VirtualFilesystem

### Autowiring

```php
// File name of the VirtualFilesystem: "files" → autowire name: "filesStorage"
class Example
{
    public function __construct(
        private VirtualFilesystemInterface $filesStorage
    ) {}
}
```

Alternatively, explicitly: `contao.filesystem.virtual.files`

### UUIDs as a path

```php
use Symfony\Component\Uid\Uuid;

$filesStorage->read('my/file.txt');
$filesStorage->read(new Uuid('94cc007c-8cc0-11ec-a8a3-0242ac120002'));
```

### Operations reference

#### Tests
```php
fileExists(string|Uuid $path, int $accessFlags = 0): bool
directoryExists(string|Uuid $path, int $accessFlags = 0): bool
has(string|Uuid $path, int $accessFlags = 0): bool
```

#### Read / write / delete
```php
read(string|Uuid $path): string
readStream(string|Uuid $path): resource
write(string|Uuid $path, string $contents, array $options = []): void
writeStream(string|Uuid $path, resource $stream, array $options = []): void
delete(string|Uuid $path): void
deleteDirectory(string|Uuid $path): void
```

#### Create / copy / move
```php
createDirectory(string $path, array $options = []): void
copy(string|Uuid $source, string $destination, array $options = []): void
move(string|Uuid $source, string $destination, array $options = []): void
```

#### Listing
```php
listContents(string|Uuid $path, bool $deep = false, int $accessFlags = 0): FilesystemItemIterator
```
Returns a generator of `FilesystemItem` objects – filterable via `.files()` / `.directories()`.

#### Metadata
```php
getLastModified(string|Uuid $path, int $accessFlags = 0): int
getFileSize(string|Uuid $path, int $accessFlags = 0): int
getMimeType(string|Uuid $path, int $accessFlags = 0): string
getExtraMetadata(string|Uuid $path, int $accessFlags = 0): array
setExtraMetadata(string|Uuid $path, array $metadata): void
```

### Access flags

| Flag | Effect |
|------|---------|
| `VirtualFilesystemInterface::BYPASS_DBAFS` | Read directly from the MountManager |
| `VirtualFilesystemInterface::FORCE_SYNC` | Force DBAFS synchronization |

Combination: `FORCE_SYNC|BYPASS_DBAFS`

### Exception handling

All operations throw a `VirtualFilesystemException` on failure. UUID resolution additionally throws an `UnableToResolveUuidException`.

### Example – listing directory contents

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

## Filesystem configuration

### Inside a bundle (ConfigureFilesystemInterface)

```php
class MyFooBundleExtension extends Extension implements ConfigureFilesystemInterface
{
    public function configureFilesystem(FilesystemConfiguration $config): void
    {
        // API calls go here
    }
}
```

### Inside an application (CompilerPass)

```php
class Plugin implements ConfigPluginInterface
{
    public function registerContainerConfiguration(LoaderInterface $loader, array $managerConfig)
    {
        $configureFilesystemPass = new class implements CompilerPassInterface {
            public function process(ContainerBuilder $container): void
            {
                $config = new FilesystemConfiguration($container);
                // API calls go here
            }
        };
    }
}
```

### FilesystemConfiguration API

| Method | Description |
|---------|-------------|
| `addVirtualFilesystem($name, $prefix, $readOnly)` | Creates the service `contao.filesystem.virtual.{name}` |
| `mountAdapter($type, $options, $path)` | Registers an adapter in the MountManager |
| `mountLocalAdapter($path, $mountPath)` | Shortcut for local adapters |
| `registerDbafs($service, $prefix)` | Registers a DBAFS service |
| `addDefaultDbafs($prefix, $table, $hashFn, $trackLastModified)` | Creates a default DBAFS |

### Example: SFTP remote backup

```php
$config->mountAdapter(
    'sftp',
    ['host' => 'example.com', 'port' => 22, 'username' => 'foobar', 'password' => 's3cr3t'],
    'backups'
);
```

---

## DBAFS (Database-Assisted Filesystem)

Enriches files with metadata from the `tl_files` table (author, license, alt text, captions). Every resource receives a global UUID.

---

*Sources:*
- *https://docs.contao.org/5.x/dev/framework/filesystem/*
- *https://docs.contao.org/5.x/dev/framework/filesystem/config/*
- *https://docs.contao.org/5.x/dev/framework/filesystem/virtual-filesystem/*
