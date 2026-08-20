---
name: sw-twig
description: Shopware Storefront Twig: template inheritance and blocks, Twig extensions, available functions, snippets. Use when overriding a Shopware Storefront template or writing a Twig extension.
---

# Shopware Storefront Twig

Templates are overridden by mirroring the path, never by editing core. Blocks are the extension points.

## Reference map

- **[EXTENSION.md](EXTENSION.md)**: Eigene Twig-Funktionen/-Filter über eine `AbstractExtension`-Klasse, registriert mit `twig.extension`-Tag.
- **[FUNCTIONS.md](FUNCTIONS.md)**: Wichtige eingebaute Funktionen/Helfer in Storefront-Templates:.
- **[STOREFRONT-TRANSLATIONS.md](STOREFRONT-TRANSLATIONS.md)**: Übersetzungen liegen als JSON unter `src/Resources/snippet/<locale>/<name>.<locale>.json` und werden automati….
- **[TEMPLATES.md](TEMPLATES.md)**: Templates liegen unter `src/Resources/views/storefront/...` und spiegeln die Core-Pfade.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
