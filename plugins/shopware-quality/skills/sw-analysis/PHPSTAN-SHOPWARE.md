# sw-phpstan-shopware

Shopware-specific PHPStan extension (`shopwarelabs/phpstan-shopware`).
Contains around 27 rules for security, DAL correctness, internal API protection and best practices.

## Installation

```bash
composer require --dev shopwarelabs/phpstan-shopware
```

The rules are registered **automatically** via `phpstan/extension-installer` (no manual include needed as long as `extra.phpstan.includes` in composer.json applies).

Without the extension installer, include them manually in `phpstan.neon`:

```yaml
includes:
    - vendor/shopwarelabs/phpstan-shopware/rules.neon
```

## Recommended level

Level **6–8** for plugin development. The Shopware rules are level-independent and apply on every level.

```yaml
parameters:
    level: 8
    paths:
        - src
```

## What is included?

- 27 rules in `rules.neon` (loaded automatically)
- 1 type extension: `CollectionHasSpecifyingExtension` (improves type inference for `Collection::has()`)
- 2 collectors: `DALDefinitionCollector`, `DALEntityCollector` (for reconciling DAL definitions against entities)

Complete rule list with descriptions and examples: `PHPSTAN-SHOPWARE-RULES.md`
