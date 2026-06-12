# Contao Maintenance-Module & Purge-Tasks (5.x)

## Überblick

Der Wartungsbereich im Contao-Backend bietet standardmäßig Crawler- und Purge-Module. Eigene Module und Purge-Tasks können registriert werden.

---

## Eigenes Maintenance-Module

### 1. Klasse erstellen

```php
namespace App\Maintenance;

use Contao\MaintenanceModuleInterface;
use Symfony\Component\HttpKernel\Attribute\AsController;
use Twig\Environment;

#[AsController]   // Macht Service öffentlich für Dependency Injection
class CustomMaintenanceModule implements MaintenanceModuleInterface
{
    public function __construct(private readonly Environment $twig) {}

    public function run(): string
    {
        return $this->twig->render('custom_maintenance_module.html.twig', [
            'is_active' => $this->isActive(),
        ]);
    }

    public function isActive(): bool
    {
        return false;   // true → nur dieses Modul wird gerendert
    }
}
```

### 2. Template erstellen

```twig
{# templates/custom_maintenance_module.html.twig #}
<div{{ attrs().addClass('maintenance_' ~ (is_active ? 'active' : 'inactive')) }}>
    <h2 class="sub_headline">Custom Maintenance Module</h2>
    <div class="tl_tbox">
        <p>Hello World!</p>
    </div>
</div>
```

### 3. Registrieren

```php
// contao/config/config.php
use App\Maintenance\CustomMaintenanceModule;

$GLOBALS['TL_MAINTENANCE'][] = CustomMaintenanceModule::class;
```

---

## Purge-Tasks

`$GLOBALS['TL_PURGE']` kennt drei Kategorien:

| Kategorie | Zweck | Pflichtschlüssel |
|-----------|-------|-----------------|
| `tables` | Datenbanktabellen leeren | `callback`, `affected` |
| `folders` | Verzeichnisinhalte bereinigen | `callback`, `affected` |
| `custom` | Beliebige Bereinigung | `callback` |

---

### Tabellen purgen

```php
// contao/config/config.php
use App\Maintenance\PurgeFoobarTable;

$GLOBALS['TL_PURGE']['tables']['foobar'] = [
    'callback' => [PurgeFoobarTable::class, '__invoke'],
    'affected' => ['tl_foobar'],    // Zeigt Datensatzanzahl im Backend
];
```

```php
// src/Maintenance/PurgeFoobarTable.php
namespace App\Maintenance;

use Doctrine\DBAL\Connection;
use Symfony\Component\HttpKernel\Attribute\AsController;

#[AsController]
class PurgeFoobarTable
{
    public function __construct(private readonly Connection $db) {}

    public function __invoke(): void
    {
        $this->db->executeQuery('TRUNCATE tl_foobar');
    }
}
```

**Übersetzung:**
```yaml
# translations/contao_tl_maintenance.en.yaml
tl_maintenance_jobs:
    foobar:
        - Purge foobar
        - Truncates the <code>tl_foobar</code> table.
```

---

### Ordner purgen

```php
// contao/config/config.php
$GLOBALS['TL_PURGE']['folders']['foobar'] = [
    'callback' => [PurgeFoobarFolder::class, '__invoke'],
    'affected' => ['%kernel.cache_dir%/foobar'],   // Zeigt Dateianzahl im Backend
];
```

```php
// src/Maintenance/PurgeFoobarFolder.php
namespace App\Maintenance;

use Symfony\Component\DependencyInjection\Attribute\Autowire;
use Symfony\Component\Filesystem\Filesystem;
use Symfony\Component\Filesystem\Path;
use Symfony\Component\Finder\Finder;
use Symfony\Component\HttpKernel\Attribute\AsController;

#[AsController]
class PurgeFoobarFolder
{
    public function __construct(
        private readonly Filesystem $filesystem,
        #[Autowire('%kernel.cache_dir%')]
        private readonly string $cacheDir,
    ) {}

    public function __invoke(): void
    {
        $files = (new Finder())
            ->in(Path::join($this->cacheDir, 'foobar'))
            ->files();

        $this->filesystem->remove($files);
    }
}
```

---

### Custom Purge-Aktion

```php
// contao/config/config.php
$GLOBALS['TL_PURGE']['custom']['foobar'] = [
    'callback' => [PurgeFoobarCustom::class, '__invoke'],
];
```

```php
// src/Maintenance/PurgeFoobarCustom.php
#[AsController]
class PurgeFoobarCustom
{
    public function __invoke(): void
    {
        // Eigene Bereinigungslogik
    }
}
```

```yaml
# translations/contao_tl_maintenance.en.yaml
tl_maintenance_jobs:
    foobar:
        - Purge foobar
        - Executes a custom purging task.
```

---

*Quellen:*
- *https://docs.contao.org/5.x/dev/framework/maintenance-module/*
- *https://docs.contao.org/5.x/dev/framework/maintenance-module/purge-task/*
