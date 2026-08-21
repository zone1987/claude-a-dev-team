# Shopware 6 – Produktvergleich (Product comparison) (export feeds)

Configuring XML/CSV feeds for price portals and marketplaces.

## Core functions

- Pre-configured templates for well-known portals
- Custom templates possible with Twig
- Scheduler for automatic recalculation
- Dynamische Produktgruppen (Dynamic product groups) for product selection
- Variables for all product data, prices, SEO URLs

## Template types

| Section | Description |
|---|---|
| **Kopfzeile** (Header) | XML/CSV header (once) |
| **Produktzeile** (Product row) | Twig loop per product |
| **Fußzeile** (Footer) | XML closing (XML only) |

## Common Twig variables

- `product.translated.name` – product name
- `product.calculatedPrice.unitPrice` – price
- `product.cover.media.url` – product image
- `seoUrl('frontend.detail.page', {'productId': product.id})` – URL

## Source

https://docs.shopware.com/de/shopware-6-de/Produktvergleich
