# Shopware 6 — PHPStan

Static type analysis. In a plugin, add a `phpstan.neon` with a high level plus the Shopware bootstrap.

```neon
parameters:
    level: 8
    paths: [src]
    bootstrapFiles:
        - vendor/shopware/core/...   # kernel bootstrap for DAL/container types
includes:
    - vendor/phpstan/phpstan-symfony/extension.neon
    - vendor/shopware/phpstan-shopware/...   # Shopware rules (sw-phpstan-shopware)
```

```bash
composer phpstan
```

Use a baseline (`phpstan-baseline.neon`) for legacy code; avoid new errors. Shopware-specific rules (decoration,
DAL, internal) via `sw-phpstan-shopware`. Cover architecture layers additionally with Deptrac (`sw-deptrac`).
