# Shopware 6 – Kataloge (Catalogues): overview and interrelations

> Source: https://docs.shopware.com/de/shopware-6-de/kataloge

---

## Contents

- [1. What is the catalogue area?](#1-what-is-the-catalogue-area)
- [2. Areas included](#2-areas-included)
- [3. Dependency diagram](#3-dependency-diagram)
- [4. Typical workflow: setting up a new product](#4-typical-workflow-setting-up-a-new-product)
- [5. Important ground rules](#5-important-ground-rules)
- [6. Sales channel linkage](#6-sales-channel-linkage)
- [7. Further documentation](#7-further-documentation)

## 1. What is the catalogue area?

The **Kataloge** (Catalogues) area in the Shopware 6 administration is the heart of product management. This is where all product-related master data is created and maintained.

**Admin path:** main menu > Kataloge

---

## 2. Areas included

| Area | Admin path | Function |
|---|---|---|
| **Produkte** (Products) | Kataloge > Produkte | Product creation, editing, variants, prices |
| **Kategorien** (Categories) | Kataloge > Kategorien | Navigation structure, product assignment |
| **Hersteller** (Manufacturers) | Kataloge > Hersteller | Manage manufacturers, assign them to products |
| **Eigenschaften** (Properties) | Kataloge > Eigenschaften | Filter attributes and the basis for variants |
| **Dynamische Produktgruppen** (Dynamic product groups) | Kataloge > Dynamische Produktgruppen | Rule-based product groups |
| **Bewertungen** (Reviews) | Kataloge > Bewertungen | Moderate customer reviews |
| **Medien** (Media) | Inhalte (Content) > Medien | Central file management (technically not under Kataloge, but linked in terms of content) |

---

## 3. Dependency diagram

```
┌─────────────────────────────────────────────┐
│                  MEDIEN                      │
│  (Bilder, Videos, Dokumente, 3D-Modelle)    │
└──────────────┬──────────────────────────────┘
               │ verwendet in
    ┌──────────┼──────────────┬──────────────┐
    ▼          ▼              ▼              ▼
PRODUKTE   KATEGORIEN    HERSTELLER    ERLEBNISWELTEN

    ▲          ▲
    │ zugewiesen
    │
EIGENSCHAFTEN ──────────────────────→ VARIANTEN
    │                                  (aus Produkten)
    └──────────────────────────────────

DYNAMISCHE PRODUKTGRUPPEN
    │
    ├──→ Kategorien (befüllen)
    ├──→ Produkte (Cross-Selling)
    └──→ Erlebniswelten (Slider)

BEWERTUNGEN ──→ Produkte (verknüpft)
```

---

## 4. Typical workflow: setting up a new product

### Preparatory steps (one-off)

1. **Create properties** (Kataloge > Eigenschaften)
   - Define property groups with their options
   - e.g. Größe (Size: XS, S, M, L, XL), Farbe (Colour: Rot, Blau, Grün)

2. **Create manufacturers** (Kataloge > Hersteller)
   - Name, logo, website URL

3. **Build the category structure** (Kataloge > Kategorien)
   - Define the navigation tree
   - Assign sales channels

4. **Prepare media** (Inhalte > Medien)
   - Upload product images
   - Create the folder structure

### Product creation

5. **Create the product** (Kataloge > Produkte)
   - Mandatory fields: Titel (Title), Produktnummer (Product number), Steuersatz (Tax rate), prices, Lagerbestand (Stock)
   - Assign a manufacturer
   - Assign categories
   - Add images from the media management
   - Assign properties (for filters)
   - Generate variants (if required)
   - Configure the SEO settings
   - Configure cross-selling (optional)

---

## 5. Important ground rules

### Deleting and its consequences

| Action | Consequence |
|---|---|
| Delete a property | It is removed from ALL products |
| Delete a manufacturer | Only possible if no product is assigned |
| Delete a category | All subcategories are deleted along with it |
| Delete a product | It stays visible in existing orders (→ better to set it inactive) |
| Delete a medium | Missing images in the shop if it is still in use |

### Activation

- New categories are initially **inaktiv** (Inactive)
- New products are initially **aktiv** (Active) (if no sales channel is assigned → not visible)
- Reviews are **not visible** after submission (they have to be approved)

---

## 6. Sales channel linkage

The catalogue area is tightly linked to sales channels:

- Products have to be assigned to a sales channel in order to be visible
- Categories are defined as the entry point for a sales channel
- SEO URLs can be configured differently per sales channel
- Prices can vary per currency/channel

---

## 7. Further documentation

| Topic | Skill |
|---|---|
| Understanding products in full | `sw-merchant-catalog-products` |
| Categories and navigation | `sw-merchant-catalog-categories` |
| Managing manufacturers | `sw-merchant-catalog-manufacturers` |
| Properties and filters | `sw-merchant-catalog-properties` |
| Dynamic product groups | `sw-merchant-catalog-product-streams` |
| Moderating reviews | `sw-merchant-catalog-reviews` |
| Media management | `sw-merchant-catalog-media` |

---

*Source: https://docs.shopware.com/de/shopware-6-de/kataloge*
