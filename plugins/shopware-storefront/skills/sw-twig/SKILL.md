---
name: sw-twig
description: Shopware Storefront Twig: template inheritance and blocks, Twig extensions, available functions, snippets. Use when overriding a Shopware Storefront template or writing a Twig extension.
---

# Shopware Storefront Twig

Templates are overridden by mirroring the path, never by editing core. Blocks are the extension points.

## Reference map

- **[EXTENSION.md](EXTENSION.md)**: Add custom Twig functions/filters through an `AbstractExtension` class, registered with the `twig.extension` tag.
- **[FUNCTIONS.md](FUNCTIONS.md)**: Important built-in functions/helpers in Storefront templates:.
- **[STOREFRONT-TRANSLATIONS.md](STOREFRONT-TRANSLATIONS.md)**: Translations live as JSON in `src/Resources/snippet/<locale>/<name>.<locale>.json` and are loaded automati….
- **[TEMPLATES.md](TEMPLATES.md)**: Templates live in `src/Resources/views/storefront/...` and mirror the core paths.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
