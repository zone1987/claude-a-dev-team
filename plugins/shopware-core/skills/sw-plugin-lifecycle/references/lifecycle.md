# Plugin Lifecycle

## Overview

Shopware plugins extend `Shopware\Core\Framework\Plugin` and can hook into lifecycle events: install, update, activate, deactivate, uninstall, and postInstall/postUpdate.

## Lifecycle Methods

Override these methods in your main plugin class (`src/{PluginName}.php`):

```php
use Shopware\Core\Framework\Plugin;
use Shopware\Core\Framework\Plugin\Context\InstallContext;
use Shopware\Core\Framework\Plugin\Context\UpdateContext;
use Shopware\Core\Framework\Plugin\Context\ActivateContext;
use Shopware\Core\Framework\Plugin\Context\DeactivateContext;
use Shopware\Core\Framework\Plugin\Context\UninstallContext;

class FfContentPlus extends Plugin
{
    public function install(InstallContext $installContext): void
    {
        // Runs on plugin:install
        // Create custom fields, seed data, etc.
    }

    public function postInstall(InstallContext $installContext): void
    {
        // Runs after install() completes
    }

    public function update(UpdateContext $updateContext): void
    {
        // Runs on plugin:update
    }

    public function postUpdate(UpdateContext $updateContext): void
    {
        // Runs after update() completes
    }

    public function activate(ActivateContext $activateContext): void
    {
        // Runs on plugin:activate
    }

    public function deactivate(DeactivateContext $deactivateContext): void
    {
        // Runs on plugin:deactivate
    }

    public function uninstall(UninstallContext $uninstallContext): void
    {
        // Runs on plugin:uninstall
        // IMPORTANT: Check keepUserData before dropping tables/data
        if ($uninstallContext->keepUserData()) {
            return;
        }

        // Drop custom tables, remove custom fields, etc.
    }
}
```

## Context Objects

All context objects extend `Shopware\Core\Framework\Plugin\Context\InstallContext` and provide:

| Method | Returns | Description |
|--------|---------|-------------|
| `getContext()` | `Context` | Shopware context for DAL operations |
| `getCurrentPluginVersion()` | `string` | Current installed version |
| `getMigrationCollection()` | `MigrationCollection` | Access to migrations |

`UninstallContext` additionally provides:
- `keepUserData(): bool` — If `true`, the user chose to keep data. Always check this before deleting anything.

`UpdateContext` additionally provides:
- `getUpdatePluginVersion(): string` — The version being updated to

## build() Method

The `build()` method is called when the Symfony container is being built. Use it to register compiler passes, load additional config, or register the plugin logger:

```php
public function build(ContainerBuilder $container): void
{
    parent::build($container);

    // Register custom compiler passes
    $container->addCompilerPass(new MyCompilerPass());
}
```

## boot() Method

The `boot()` method is called on every request after the container is compiled. Use sparingly — prefer DI over boot logic:

```php
public function boot(): void
{
    parent::boot();
}
```

## Best Practices

1. **Always check `keepUserData()`** in `uninstall()` before deleting data
2. **Use migrations** for database schema changes, not lifecycle methods
3. **Use `install()` or `postInstall()`** for seeding initial data (custom field sets, mail templates)
4. **Prefer `postUpdate()` over `update()`** for data operations that need the updated schema
5. **Never assume the plugin is activated** in `install()` — activation happens separately
6. **Keep lifecycle methods idempotent** — they may be called multiple times
