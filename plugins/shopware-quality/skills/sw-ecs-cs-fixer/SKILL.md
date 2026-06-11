---
name: sw-ecs-cs-fixer
description: >
  Code-Style für Shopware-6-Plugins mit Easy Coding Standard (ECS) / PHP-CS-Fixer: Config, Shopware-Regelset,
  composer ecs / ecs-fix. Trigger: "ECS shopware", "php-cs-fixer shopware", "code style fix", "ecs-fix", "coding standard php plugin".
  Shopware 6.7.
---

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
