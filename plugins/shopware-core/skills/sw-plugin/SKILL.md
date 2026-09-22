---
name: sw-plugin
description: Shopware plugin fundamentals: base class, lifecycle, plugin configuration, extension points, feature flags. Use when creating or configuring a Shopware plugin.
---

# Shopware plugin fundamentals

Where a plugin hooks into the platform, and which lifecycle method runs when.

## Reference map

- **[ARCHITECTURE-OVERVIEW.md](references/ARCHITECTURE-OVERVIEW.md)**: Shopware is API-first with its own **Data Abstraction Layer** instead of the Doctrine ORM and an **event-driv….
- **[BASE.md](references/BASE.md)**: A plugin is a Symfony bundle extending `Shopware\Core\Framework\Plugin`.
- **[CONFIG.md](references/CONFIG.md)**: `src/Resources/config/config.xml` defines the settings form. [CONFIG-CONFIGURATION](references/CONFIG-CONFIGURATION.md).
- **[EXTENSION-POINTS.md](references/EXTENSION-POINTS.md)**: In addition to events, Shopware offers **extension points**: defined places where the core dispatches an `Ext….
- **[FEATURE-FLAGS.md](references/FEATURE-FLAGS.md)**: Flags let you ship new code behind a switch.
- **[LIFECYCLE.md](references/LIFECYCLE.md)**: The plugin class can override lifecycle hooks.
- **[PLUGIN-STRUCTURE.md](references/PLUGIN-STRUCTURE.md)**: The full directory tree of a plugin plus the complete `.gitignore` and the five entries that need an explanation.
- **[PLUGIN-COMPOSER.md](references/PLUGIN-COMPOSER.md)**: The plugin `composer.json` in full: head, `conflict` block, `require-dev` with a reason per package, `config.allow-plugins`, all 22 scripts.
- **[PLUGIN-PACKAGE-ATTRIBUTE.md](references/PLUGIN-PACKAGE-ATTRIBUTE.md)**: Why a plugin ships its own `#[Package]` attribute instead of the core's `@internal` one, the complete class, and the `ignoreErrors` block it removes.
- **[PLUGIN-CHECKLIST.md](references/PLUGIN-CHECKLIST.md)**: The checklist for a new plugin, from skeleton and tooling through tests to completion.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
