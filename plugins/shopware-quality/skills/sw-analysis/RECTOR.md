# Shopware 6 — Rector

Rector transforms code automatically (PHP version upgrades, Shopware deprecation fixes, codemods).

```php
// rector.php
return RectorConfig::configure()
    ->withPaths([__DIR__ . '/src'])
    ->withPhpSets()                 // PHP level modernization
    ->withSets([/* Shopware Rector set (shopware/rector) */]);
```

```bash
vendor/bin/rector process --dry-run   # preview
vendor/bin/rector process             # apply
```

Especially useful for **major upgrades** (6.6→6.7→6.8): Shopware ships Rector rules for deprecated APIs
(plugin `shopware-migration` → `sw-deprecation-handling`). Verify the result afterwards with ECS/PHPStan.
