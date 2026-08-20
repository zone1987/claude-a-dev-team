# Shopware 6 – Eigenschaften (Properties)

Properties are managed under **Kataloge** (Catalogues) > **Eigenschaften** (Properties). They serve as filterable
product information (e.g. size, colour) and as the basis for product variants.

## Creating a property

1. Kataloge > Eigenschaften > **"Eigenschaft hinzufügen"** (Add property)
2. Enter a name (appears on the product detail page and in filters)
3. Optional fields: description, filterability, display type, sorting, position
4. Add Ausprägungen (Options) (values)

## Display types

| Type | Presentation in the filter |
|---|---|
| Text | Textual |
| Farbe (Colour) | HEX colour value |
| Bild (Image) | Custom image |
| Dropdown | Dropdown on the product, text in the filter |

## Sorting options

- **Alphanumerisch** (Alphanumeric): default a–z, 1–10
- **Benutzerdefiniert** (Custom): manual position order

## Creating Ausprägungen (options / values)

Every option requires: name, position (for custom sorting).
Optional: colour HEX (for type Farbe) or image (for type Bild).

> **Caution**: deleting a property removes it from ALL assigned products!

See `PROPERTIES-DETAIL.md` for full details.

## Source
https://docs.shopware.com/de/shopware-6-de/produkte/eigenschaften
