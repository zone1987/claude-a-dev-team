---
name: sw-plugin
description: Shopware plugin fundamentals: base class, lifecycle, plugin configuration, extension points, feature flags. Use when creating or configuring a Shopware plugin.
---

# Shopware plugin fundamentals

Where a plugin hooks into the platform, and which lifecycle method runs when.

## Reference map

- **[ARCHITECTURE-OVERVIEW.md](ARCHITECTURE-OVERVIEW.md)**: Shopware ist API-first mit eigenem **Data Abstraction Layer** statt Doctrine-ORM und einem **event-getriebene….
- **[BASE.md](BASE.md)**: Ein Plugin ist ein Symfony-Bundle, das `Shopware\Core\Framework\Plugin` erweitert.
- **[CONFIG.md](CONFIG.md)**: `src/Resources/config/config.xml` definiert die Einstellungsmaske. [CONFIG-CONFIGURATION](CONFIG-CONFIGURATION.md).
- **[EXTENSION-POINTS.md](EXTENSION-POINTS.md)**: Ergänzend zu Events bietet Shopware **Extension Points**: definierte Stellen, an denen der Kern eine `Extensi….
- **[FEATURE-FLAGS.md](FEATURE-FLAGS.md)**: Flags erlauben es, neuen Code hinter einem Schalter auszuliefern.
- **[LIFECYCLE.md](LIFECYCLE.md)**: Die Plugin-Klasse kann Lifecycle-Hooks überschreiben. [LIFECYCLE-DETAIL](LIFECYCLE-DETAIL.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
