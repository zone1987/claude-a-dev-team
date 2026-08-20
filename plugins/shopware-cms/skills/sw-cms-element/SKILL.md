---
name: sw-cms-element
description: Shopware CMS elements: registering an element, its administration component, the storefront template, and the data resolver that loads its data. Use when building a Shopware CMS element.
---

# Shopware CMS elements

An element needs three parts: an admin component, a storefront template, and a data resolver.

## Reference map

- **[ADMIN.md](ADMIN.md)**: Drei Komponenten je Element, registriert unter `.../module/sw-cms/elements/ff-teaser/`:.
- **[CMS.md](CMS.md)**: Plugins can add custom CMS elements and blocks to the Shopping Experiences content management system. [CMS-2](CMS-2.md).
- **[DATA-RESOLVER.md](DATA-RESOLVER.md)**: Lädt serverseitig die Daten eines CMS-Elements.
- **[OVERVIEW.md](OVERVIEW.md)**: Ein Element ist ein konkreter Inhaltsbaustein.
- **[STOREFRONT.md](STOREFRONT.md)**: Das Element wird im Storefront über ein Twig-Template gerendert, Pfad `src/Resources/views/storefront/element….

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
