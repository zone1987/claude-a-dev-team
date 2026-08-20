---
name: sw-plugin
description: Shopware plugin fundamentals: base class, lifecycle, plugin configuration, extension points, feature flags. Use when creating or configuring a Shopware plugin.
---

# Shopware plugin fundamentals

Where a plugin hooks into the platform, and which lifecycle method runs when.

## Reference map

- **[ARCHITECTURE-OVERVIEW.md](ARCHITECTURE-OVERVIEW.md)**: Shopware is API-first with its own **Data Abstraction Layer** instead of the Doctrine ORM and an **event-driv….
- **[BASE.md](BASE.md)**: A plugin is a Symfony bundle extending `Shopware\Core\Framework\Plugin`.
- **[CONFIG.md](CONFIG.md)**: `src/Resources/config/config.xml` defines the settings form. [CONFIG-CONFIGURATION](CONFIG-CONFIGURATION.md).
- **[EXTENSION-POINTS.md](EXTENSION-POINTS.md)**: In addition to events, Shopware offers **extension points**: defined places where the core dispatches an `Ext….
- **[FEATURE-FLAGS.md](FEATURE-FLAGS.md)**: Flags let you ship new code behind a switch.
- **[LIFECYCLE.md](LIFECYCLE.md)**: The plugin class can override lifecycle hooks. [LIFECYCLE-DETAIL](LIFECYCLE-DETAIL.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
