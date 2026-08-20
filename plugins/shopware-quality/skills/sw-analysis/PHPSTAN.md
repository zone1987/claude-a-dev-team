# Shopware 6 — PHPStan

Statische Typanalyse. Im Plugin eine `phpstan.neon` mit hohem Level + Shopware-Bootstrap.

```neon
parameters:
    level: 8
    paths: [src]
    bootstrapFiles:
        - vendor/shopware/core/...   # Kernel-Bootstrap für DAL/Container-Typen
includes:
    - vendor/phpstan/phpstan-symfony/extension.neon
    - vendor/shopware/phpstan-shopware/...   # Shopware-Regeln (sw-phpstan-shopware)
```

```bash
composer phpstan
```

Baseline (`phpstan-baseline.neon`) für Bestandscode; neue Fehler vermeiden. Shopware-spezifische Regeln (Decoration,
DAL, internal) über `sw-phpstan-shopware`. Architektur-Schichten zusätzlich mit Deptrac (`sw-deptrac`).
