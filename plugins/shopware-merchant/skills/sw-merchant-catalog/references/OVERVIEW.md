# Shopware 6 – Kataloge (Catalogues) overview

The **Kataloge** (Catalogues) area is the heart of product management in Shopware 6. This is where all product-related data is created and maintained.

## Areas included

| Area | Path in the admin | Skill |
|---|---|---|
| Produkte (Products) | Kataloge > Produkte | `sw-merchant-catalog-products` |
| Kategorien (Categories) | Kataloge > Kategorien | `sw-merchant-catalog-categories` |
| Hersteller (Manufacturers) | Kataloge > Hersteller | `sw-merchant-catalog-manufacturers` |
| Eigenschaften (Properties) | Kataloge > Eigenschaften | `sw-merchant-catalog-properties` |
| Dynamische Produktgruppen (Dynamic product groups) | Kataloge > Dynamische Produktgruppen | `sw-merchant-catalog-product-streams` |
| Bewertungen (Reviews) | Kataloge > Bewertungen | `sw-merchant-catalog-reviews` |
| Medien (Media) | Inhalte (Content) > Medien | `sw-merchant-catalog-media` |

## Quick start

- **Create a new product**: Kataloge > Produkte > "Produkt hinzufügen" (Add product)
- **Create a category**: Kataloge > Kategorien > context menu in the tree structure
- **Create a property** (for filters/variants): Kataloge > Eigenschaften > "Eigenschaft hinzufügen" (Add property)
- **Create a manufacturer**: Kataloge > Hersteller > "Hersteller anlegen" (Create manufacturer)
- **Create a product group**: Kataloge > Dynamische Produktgruppen > "Produktgruppe anlegen" (Create product group)

## Dependencies between the areas

```
Eigenschaften ──→ Produkte (Filter + Varianten)
Hersteller ──→ Produkte (Zuordnung)
Kategorien ──→ Produkte (Navigation)
Dynamische Produktgruppen ──→ Kategorien / Cross-Selling / Erlebniswelten
Medien ──→ Produkte / Kategorien / Hersteller
```

## Source
https://docs.shopware.com/de/shopware-6-de/kataloge
