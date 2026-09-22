---
name: sw-analysis
description: Shopware static analysis: PHPStan at level max, php-cs-fixer, Rector, and phpat for architecture rules — all behind the one command, composer gate. Use when configuring or fixing Shopware static analysis.
---

# Shopware static analysis

The tool chain a Shopware plugin is expected to pass, with the configuration each one needs.

## Reference map

- **[STATIC-ANALYSIS.md](references/STATIC-ANALYSIS.md)**: **Start here.** The whole matrix behind `composer gate`, the order it runs in, and what deliberately stays out of it.
- **[ECS-CS-FIXER.md](references/ECS-CS-FIXER.md)**: **php-cs-fixer, not ECS** — including the seven DocBlock rules that must stay off, or the gate deletes the tags on every run.
- **[PHPSTAN.md](references/PHPSTAN.md)**: `level: max` from the start, no `ignoreErrors`, no baseline. [PHPSTAN-SHOPWARE-RULES](references/PHPSTAN-SHOPWARE-RULES.md), [PHPSTAN-SHOPWARE](references/PHPSTAN-SHOPWARE.md).
- **[RECTOR.md](references/RECTOR.md)**: the full `rector.php`, the twelve skip rules, and why the next major's set is never applied.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20. Coding guidelines and ADRs come from the shopware/shopware repository.
