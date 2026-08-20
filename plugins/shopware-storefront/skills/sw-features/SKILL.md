---
name: sw-features
description: Shopware Storefront features: listing filters, custom sorting, SEO URLs, sitemap, cookie consent, captcha, HTTP caching. Use when the request names a Shopware listing filter or SEO URL.
---

# Shopware Storefront features

Self-contained Storefront features, each with its own extension point.

## Reference map

- **[ACCESSIBILITY.md](ACCESSIBILITY.md)**: WCAG 2.1 AA + BITV 2.0. [ACCESSIBILITY-DETAIL](ACCESSIBILITY-DETAIL.md).
- **[CAPTCHA.md](CAPTCHA.md)**: Formulare werden über Captchas geschützt.
- **[COOKIE-MANAGER.md](COOKIE-MANAGER.md)**: Eigene Cookies in die Consent-Verwaltung aufnehmen, indem der `CookieProviderInterface` dekoriert wird.
- **[CUSTOM-SORTING.md](CUSTOM-SORTING.md)**: Sortier-Optionen im Listing sind Daten, keine Code-Klassen.
- **[LISTING-FILTER.md](LISTING-FILTER.md)**: Eigene Filter ins Produkt-Listing einhängen über zwei Events:.
- **[SEO.md](SEO.md)**: Plugins can register custom SEO URL templates for their entities and extend robots.txt. [SEO-URLS](SEO-URLS.md).
- **[SITEMAP.md](SITEMAP.md)**: Eigene Seiten in die XML-Sitemap aufnehmen über einen `AbstractUrlProvider`.
- **[STOREFRONT-CACHING.md](STOREFRONT-CACHING.md)**: Storefront-Seiten werden http-gecacht.

## Source

Distilled from [developer.shopware.com](https://developer.shopware.com) (Storefront guides and reference) plus the Shopware 6.7 Storefront source, retrieved 2026-08-20.
