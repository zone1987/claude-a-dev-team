---
name: sw-controller
description: Shopware Storefront controllers, Pages, Pagelets, PageLoaders, attaching data, AJAX routes. Use when building a Shopware Storefront controller or page.
---

# Shopware Storefront controllers and pages

A Storefront request becomes a Page built by a PageLoader. Extending existing data means decorating a PageLoader, not the controller.

## Reference map

- **[AJAX-DATA.md](AJAX-DATA.md)**: In a JS plugin, load data through the built-in `HttpClient` or
- **[PAGE-LOADER.md](PAGE-LOADER.md)**: The PageLoader builds the page struct: first the generic page, then its own data, then the event.
- **[STOREFRONT.md](STOREFRONT.md)**: The storefront covers Twig templates, controllers, JavaScript plugins, SCSS styling, and snippet translations…. [STOREFRONT-CONTROLLER](STOREFRONT-CONTROLLER.md), [STOREFRONT-DATA](STOREFRONT-DATA.md), [STOREFRONT-PAGE](STOREFRONT-PAGE.md), [STOREFRONT-PAGELET](STOREFRONT-PAGELET.md).

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
