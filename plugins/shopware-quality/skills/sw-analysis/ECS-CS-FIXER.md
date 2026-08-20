# Shopware 6 — ECS / PHP-CS-Fixer

Shopware nutzt **Easy Coding Standard** (ECS) für PHP-Code-Style. Im Plugin ein `ecs.php` mit dem Shopware-Regelset
(bzw. `shopware/conventions`) einbinden.

```php
// ecs.php
return ECSConfig::configure()
    ->withPaths([__DIR__ . '/src', __DIR__ . '/tests'])
    ->withRootFiles()
    ->withSets([/* Shopware-Standard-Set */]);
```

```bash
composer ecs        # prüfen
composer ecs-fix    # automatisch korrigieren
```

`declare(strict_types=1)`, importierte Klassen, einheitliche Formatierung. Vor jedem Commit ausführen (oder Hook,
`shopware-quality` Hooks). Typprüfung separat: `sw-phpstan`.
