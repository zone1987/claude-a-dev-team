---
name: sw-features
description: Shopware Storefront features: listing filters, custom sorting, SEO URLs, sitemap, cookie consent, captcha, HTTP caching. Use when the request names a Shopware listing filter or SEO URL.
---

# Shopware Storefront features

Self-contained Storefront features, each with its own extension point.

## Reference map

- **[ACCESSIBILITY.md](ACCESSIBILITY.md)**: WCAG 2.1 AA + BITV 2.0. [ACCESSIBILITY-DETAIL](ACCESSIBILITY-DETAIL.md).
- **[CAPTCHA.md](CAPTCHA.md)**: Forms are protected by captchas.
- **[COOKIE-MANAGER.md](COOKIE-MANAGER.md)**: Add your own cookies to the consent management by decorating `CookieProviderInterface`.
- **[CUSTOM-SORTING.md](CUSTOM-SORTING.md)**: Sorting options in the listing are data, not code classes.
- **[LISTING-FILTER.md](LISTING-FILTER.md)**: Hook custom filters into the product listing through two events:.
- **[SEO.md](SEO.md)**: Plugins can register custom SEO URL templates for their entities and extend robots.txt. [SEO-URLS](SEO-URLS.md).
- **[SITEMAP.md](SITEMAP.md)**: Add your own pages to the XML sitemap via an `AbstractUrlProvider`.
- **[STOREFRONT-CACHING.md](STOREFRONT-CACHING.md)**: Storefront pages are HTTP-cached.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
