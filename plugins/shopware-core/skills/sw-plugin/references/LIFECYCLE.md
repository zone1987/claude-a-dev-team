# Shopware 6 — Plugin Lifecycle

The plugin class can override lifecycle hooks. Each one receives a context with `getContext()`,
`getPlugin()` and (on uninstall) `keepUserData()`.

```php
public function uninstall(UninstallContext $uninstallContext): void
{
    parent::uninstall($uninstallContext);
    if ($uninstallContext->keepUserData()) {
        return; // do NOT drop tables/data
    }
    // clean up: drop your own tables etc.
}
```

Rules of thumb: apply schema changes through **migrations** (`sw-migration` / `shopware-data`), not in the lifecycle.
On `uninstall` always respect `keepUserData()`. Use `activate`/`deactivate` for data that only applies while the plugin is active.

→ All hooks, order & examples: [LIFECYCLE-DETAIL.md](LIFECYCLE-DETAIL.md)
