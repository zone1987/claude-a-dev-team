# Contao maintenance modules & purge tasks (5.x)

## Contents

- [Overview](#overview)
- [Custom maintenance module](#custom-maintenance-module)
- [Purge tasks](#purge-tasks)

## Overview

By default the maintenance area in the Contao back end offers crawler and purge modules. Custom modules and purge tasks can be registered.

---

## Custom maintenance module

### 1. Create the class

```php
namespace App\Maintenance;

use Contao\MaintenanceModuleInterface;
use Symfony\Component\HttpKernel\Attribute\AsController;
use Twig\Environment;

#[AsController]   // Makes the service public for dependency injection
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
        return false;   // true → only this module is rendered
    }
}
```

### 2. Create the template

```twig
{# templates/custom_maintenance_module.html.twig #}
<div{{ attrs().addClass('maintenance_' ~ (is_active ? 'active' : 'inactive')) }}>
    <h2 class="sub_headline">Custom Maintenance Module</h2>
    <div class="tl_tbox">
        <p>Hello World!</p>
    </div>
</div>
```

### 3. Register it

```php
// contao/config/config.php
use App\Maintenance\CustomMaintenanceModule;

$GLOBALS['TL_MAINTENANCE'][] = CustomMaintenanceModule::class;
```

---

## Purge tasks

`$GLOBALS['TL_PURGE']` knows three categories:

| Category | Purpose | Required keys |
|-----------|-------|-----------------|
| `tables` | Empty database tables | `callback`, `affected` |
| `folders` | Clean up directory contents | `callback`, `affected` |
| `custom` | Arbitrary clean-up | `callback` |

---

### Purging tables

```php
// contao/config/config.php
use App\Maintenance\PurgeFoobarTable;

$GLOBALS['TL_PURGE']['tables']['foobar'] = [
    'callback' => [PurgeFoobarTable::class, '__invoke'],
    'affected' => ['tl_foobar'],    // Shows the record count in the back end
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

**Translation:**
```yaml
# translations/contao_tl_maintenance.en.yaml
tl_maintenance_jobs:
    foobar:
        - Purge foobar
        - Truncates the <code>tl_foobar</code> table.
```

---

### Purging folders

```php
// contao/config/config.php
$GLOBALS['TL_PURGE']['folders']['foobar'] = [
    'callback' => [PurgeFoobarFolder::class, '__invoke'],
    'affected' => ['%kernel.cache_dir%/foobar'],   // Shows the file count in the back end
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

### Custom purge action

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
        // Your own clean-up logic
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

*Sources:*
- *https://docs.contao.org/5.x/dev/framework/maintenance-module/*
- *https://docs.contao.org/5.x/dev/framework/maintenance-module/purge-task/*
