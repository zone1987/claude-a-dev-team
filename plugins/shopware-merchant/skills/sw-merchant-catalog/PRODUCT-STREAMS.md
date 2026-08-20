# Shopware 6 – Dynamische Produktgruppen (Dynamic product groups)

Dynamic product groups are managed under **Kataloge** (Catalogues) > **Dynamische Produktgruppen**.
They group products automatically according to defined rules.

## Creating a product group

1. Kataloge > Dynamische Produktgruppen > **"Produktgruppe anlegen"** (Create product group)
2. Enter name and description
3. Define Bedingungen (Conditions) (Rule Builder)
4. Check the Vorschau (Preview)
5. Save

## Condition operators

| Operator | Meaning |
|---|---|
| Gleich (Equals) | Exact value |
| Ungleich (Not equal) | Not this value |
| Eins von (One of) | One of the values |
| Keins von (None of) | None of the values |
| Alle von (All of) | All values must apply |
| Alle außer (All except) | All except these |

## Links

- **UND** (AND): all conditions must be met
- **ODER** (OR): one of the conditions is enough
- **Unterbedingungen** (Sub-conditions): nesting is possible

## Areas of use

- Kategorien (Categories) (fill dynamically instead of manually)
- Product feeds / product comparisons
- Erlebniswelten (Shopping Experiences) (product slider commerce block)
- Cross-selling on the product detail page

See `PRODUCT-STREAMS-DETAIL.md` for the full set of rule options.

## Source
https://docs.shopware.com/de/shopware-6-de/Kataloge/DynamischeProduktgruppen
