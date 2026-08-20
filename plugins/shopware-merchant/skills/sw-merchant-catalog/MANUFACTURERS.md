# Shopware 6 – Hersteller (Manufacturers)

Manufacturers are managed under **Kataloge** (Catalogues) > **Hersteller** (Manufacturers) and can be assigned to products.
They appear on the product detail page (top right).

## Creating a manufacturer

1. Kataloge > Hersteller > **"Hersteller anlegen"** (Create manufacturer)
2. **Mandatory field**: Name
3. Optional: website link, logo, description (supports Twig variables)
4. Save

## Manufacturer actions

| Action | Description |
|---|---|
| Bearbeiten (Edit) | Opens the editing screen |
| Duplizieren (Duplicate) | Creates a copy with all data |
| Löschen (Delete) | Only possible if not assigned to any product |

## Creating a manufacturer page (workaround)

Shopware 6 has no native manufacturer page. Procedure:
1. Create a Shopping Experience landing page in "Inhalte > Erlebniswelten" (Content > Shopping Experiences)
2. Create a landing page under Kataloge > Kategorien (Categories) (set the SEO URL)
3. Assign the Shopping Experience layout
4. Enter this SEO URL for the manufacturer under "Hersteller-URL" (Manufacturer URL) (with a leading `/`)

See `MANUFACTURERS-DETAIL.md` for the full guide.

## Source
https://docs.shopware.com/de/shopware-6-de/produkte/hersteller
