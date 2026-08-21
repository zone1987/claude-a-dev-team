---
name: sw-cms-element
description: Shopware CMS elements: registering an element, its administration component, the storefront template, and the data resolver that loads its data. Use when building a Shopware CMS element.
---

# Shopware CMS elements

An element needs three parts: an admin component, a storefront template, and a data resolver.

## Reference map

- **[ADMIN.md](references/ADMIN.md)**: Three components per element, registered under `.../module/sw-cms/elements/ff-teaser/`.
- **[CMS.md](references/CMS.md)**: Plugins can add custom CMS elements and blocks to the Shopping Experiences content management system. [CMS-2](references/CMS-2.md).
- **[DATA-RESOLVER.md](references/DATA-RESOLVER.md)**: Loads a CMS element's data server-side.
- **[OVERVIEW.md](references/OVERVIEW.md)**: An element is a concrete content building block.
- **[STOREFRONT.md](references/STOREFRONT.md)**: The element is rendered in the storefront through a Twig template, path `src/Resources/views/storefront/element….

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) plus the Shopware 6.7 source, retrieved 2026-08-20.
