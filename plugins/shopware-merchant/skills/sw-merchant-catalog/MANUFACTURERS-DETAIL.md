# Shopware 6 – Hersteller (Manufacturers): Complete reference

> Source: https://docs.shopware.com/de/shopware-6-de/produkte/hersteller  
> Applies from: Shopware 6.0.0+

---

## Contents

- [1. Manufacturer overview](#1-manufacturer-overview)
- [2. Creating a manufacturer](#2-creating-a-manufacturer)
- [3. Storefront presentation](#3-storefront-presentation)
- [4. Editing a manufacturer](#4-editing-a-manufacturer)
- [5. Creating a manufacturer page (workaround)](#5-creating-a-manufacturer-page-workaround)
- [6. Manufacturers and products](#6-manufacturers-and-products)
- [7. Deleting a manufacturer](#7-deleting-a-manufacturer)
- [8. Tips](#8-tips)

## 1. Manufacturer overview

Path: **Kataloge** (Catalogues) > **Hersteller** (Manufacturers)

The overview lists all created manufacturers with the most important information in a table.

### Columns and functions

- Columns can be sorted ascending and descending by clicking the column header
- Context menu (**"..."** button) per manufacturer:

| Option | Description |
|---|---|
| Bearbeiten (Edit) | Opens the manufacturer's editing screen |
| Duplizieren (Duplicate) | Creates a copy with all existing data |
| Löschen (Delete) | Deletes the manufacturer (only possible if not assigned to any product) |

---

## 2. Creating a manufacturer

1. Click **"Hersteller anlegen"** (Create manufacturer)
2. Mandatory field: **Name** (the only mandatory field)
3. Optional fields:
   - **Website-Link** (Website link): URL of the manufacturer's website
   - **Logo**: image upload (appears on the product detail page instead of the name)
   - **Beschreibung** (Description): free-text description; supports **Twig variables** for the storefront presentation
4. Save

---

## 3. Storefront presentation

Manufacturer information appears on the **product detail page** in the **top right corner**.

| Situation | Presentation |
|---|---|
| Only name available | Name is displayed as text |
| Logo uploaded | Logo is displayed instead of the name |
| Website link set | Name/logo becomes clickable (redirects to the manufacturer's website) |
| No manufacturer assigned | No manufacturer area on the detail page |

---

## 4. Editing a manufacturer

Accessed by clicking **"Bearbeiten"** in the context menu or by clicking the name directly.

All fields from the creation screen can be edited:
- Name
- Website
- Logo (replace or remove the image)
- Beschreibung

---

## 5. Creating a manufacturer page (workaround)

Shopware 6 has no native manufacturer page. The following workaround creates a dedicated page:

### Step 1: Create a Shopping Experience landing page

1. Inhalte (Content) > Erlebniswelten (Shopping Experiences) > **"Erlebniswelt hinzufügen"** (Add Shopping Experience)
2. Type: select **Landingpage** (Landing page)
3. Design the layout (manufacturer info, products etc.)
4. Save and activate

### Step 2: Create the landing page in Kategorien

1. Kataloge > Kategorien (Categories)
2. Below the category overview: **"Landingpage hinzufügen"** (Add landing page)
3. Fill in the fields:
   - Name (e.g. "Shopware AG")
   - Landingpage ist aktiv (Landing page is active): **Ja** (Yes)
   - Assign a Verkaufskanal (Sales channel)
4. Open the **SEO** tab:
   - **SEO URL** (mandatory): define the path, e.g. `shopwareag`
   - The resulting URL is then: `www.meinshop.de/shopwareag`
5. Open the **Layout** tab:
   - Assign the Shopping Experience created in step 1
6. Save

### Step 3: Enter the SEO URL for the manufacturer

1. Kataloge > Hersteller > open the manufacturer
2. Field **"Hersteller-URL"** (Manufacturer URL) (or a comparable field): enter the SEO URL with a leading `/`
   - Example: `/shopwareag`
3. Save

Result: the manufacturer link on the product detail page now leads to the landing page instead of the external website.

---

## 6. Manufacturers and products

- Exactly **one manufacturer** can be assigned to a product
- The assignment is made in the product screen under **Allgemein** (General) > **Informationen** (Information) > **Hersteller**
- New manufacturers can be created directly from the product screen (without switching to Kataloge > Hersteller)
- A manufacturer can be assigned to any number of products

---

## 7. Deleting a manufacturer

- Deletion is only possible if the manufacturer is **no longer assigned to any product**
- First remove all product assignments, then delete
- Alternatively: duplicating → not needed; simply do not assign the manufacturer to any further product

---

## 8. Tips

- The **Logo** should be uploaded in a format with a transparent background (PNG, SVG), because it is displayed on the product image background
- The **Beschreibung** can contain Twig syntax and is therefore suitable for dynamic content
- For SEO-relevant manufacturer pages, the landing page workaround is the recommended method
- Manufacturers can also be used for internal sorting purposes in the product overview

---

*Source: https://docs.shopware.com/de/shopware-6-de/produkte/hersteller*
