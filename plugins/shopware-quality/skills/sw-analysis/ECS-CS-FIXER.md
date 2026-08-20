# Shopware 6 — ECS / PHP-CS-Fixer

Shopware uses **Easy Coding Standard** (ECS) for PHP code style. In a plugin, add an `ecs.php` that includes the
Shopware rule set (or `shopware/conventions`).

```php
// ecs.php
return ECSConfig::configure()
    ->withPaths([__DIR__ . '/src', __DIR__ . '/tests'])
    ->withRootFiles()
    ->withSets([/* Shopware standard set */]);
```

```bash
composer ecs        # check
composer ecs-fix    # fix automatically
```

`declare(strict_types=1)`, imported classes, consistent formatting. Run it before every commit (or as a hook,
`shopware-quality` hooks). Type checking is separate: `sw-phpstan`.
