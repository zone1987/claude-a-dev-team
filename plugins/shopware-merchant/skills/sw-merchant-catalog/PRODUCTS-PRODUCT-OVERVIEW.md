# Shopware 6 – Produktübersicht (Product overview, list view): complete reference

> Source: https://docs.shopware.com/de/shopware-6-de/produkte/uebersicht  
> Applies from: Shopware 6.0.0+

---

## Contents

- [1. Overview](#1-overview)
- [2. Columns and presentation](#2-columns-and-presentation)
- [3. Context menu per product](#3-context-menu-per-product)
- [4. Mehrfachänderung (Bulk edit)](#4-mehrfachänderung-bulk-edit)
- [5. Search and filters](#5-search-and-filters)
- [6. Important notes](#6-important-notes)

## 1. Overview

The product overview under **Kataloge** (Catalogues) > **Produkte** (Products) is the central list of all products that exist. It provides quick orientation and enables bulk operations.

---

## 2. Columns and presentation

### Default columns

| Column | Description | Sortable |
|---|---|---|
| Aktiv (Active) | Availability status (green = active, red = inactive) | Yes |
| Name | Product name | Yes |
| Produktnummer (Product number) | Unique identifier | Yes |
| Preis (Price) | Price for the default customer group | Yes |
| Lagerbestand (Stock) | Current stock (colour-coded) | Yes |
| Hersteller (Manufacturer) | Assigned manufacturer name | Yes |

### Stock colour coding

| Colour | Stock |
|---|---|
| Red | 0 (not in stock) |
| Yellow | 1–25 (low stock) |
| Green | > 25 (sufficient) |

### Adjusting columns

Via **Listeneinstellungen** (List settings) (gear icon):
- Show and hide columns
- Adjust the column order by drag & drop
- Activate **Kompaktmodus** (Compact mode) (less row height, more products visible)

---

## 3. Context menu per product

Click on **"..."** (three-dot button) to the right of a product:

| Option | Description |
|---|---|
| Bearbeiten (Edit) | Opens the full product detail screen |
| Duplizieren (Duplicate) | Creates a copy of the product with all settings |
| Löschen (Delete) | Deletes the product permanently |

### Variant products

- An icon in front of the product name shows that this is a variant product
- Clicking the icon opens a **modal** with an overview of all variants and their core information

---

## 4. Mehrfachänderung (Bulk edit)

### What is Mehrfachänderung?

The bulk edit allows several products to be edited at the same time without having to open each one individually. It is especially useful for mass updates of prices, categories or status.

### Prerequisites

- A maximum of **1000 products** per operation
- The selection can span several pages

### Step by step

1. Select products (checkbox to the left of the product)
   - Individual products: click the checkboxes
   - All on the page: checkbox in the table header
   - All pages: use the extended selection
2. Click the button **"Mehrfachänderung"** (Bulk edit)
3. Activate the desired fields via **checkbox**
4. Enter values or choose operations
5. Save → a progress bar appears

### Dropdown operations

| Operation | Behaviour |
|---|---|
| **Überschreiben** (Overwrite) | Replaces all previous values with the new value |
| **Leeren** (Clear) | Removes all settings of this block (deletes values) |
| **Hinzufügen** (Add) | Adds the new value without deleting existing values |
| **Entfernen** (Remove) | Specifically deletes the given value from the assignment |

### Editable fields

**Allgemein (General):**
- Aktiv status (on/off for all selected products)
- Hersteller
- Tags (add/remove)
- Sichtbarkeit (Visibility) / Erweiterte Sichtbarkeit (Advanced visibility)
- Kategorien (Categories)
- Search keywords
- Versandkostenfrei (Free shipping)

**Lieferbarkeit (Availability):**
- Lagerbestand
- Abverkauf (Clearance sale)
- Lieferzeit (Delivery time)
- Wiederauffüllzeit (Restock time)
- Minimum/scaled/maximum purchase quantity

**Preise (Prices) (basic price fields):**
- Steuersatz (Tax rate)
- Bruttopreis (Gross price) / Nettopreis (Net price)
- Streichpreis (List price)
- Einkaufspreis (Purchase price)
- Günstigster Preis (Lowest price) (30 days)

**Erweiterte Preise (Advanced prices):**
- Scaled prices and rule-based prices via a modal interface
- Options: duplicate, delete, add price rules

---

## 5. Search and filters

### Full text search

- Search field at the top of the product list
- Searches in: name, product number, EAN, manufacturer number

### List filters

Filter options (available depending on the configuration):
- Aktiv / Inaktiv (Active / Inactive)
- Hersteller
- Kategorien
- Stock ranges
- Verkaufskanal (Sales channel) assignment

---

## 6. Important notes

### Deleting vs. deactivating products

> **Recommendation**: do **not delete** products if they appear in existing orders!
> 
> Deleted products do remain visible as line items in orders, but all further management options (returns, reorders etc.) may be restricted.
>
> **Better**: set the product to **inaktiv** (deactivate the Aktiv status)

### Variant products in the list

- The variant icon only appears on the main product
- The variants themselves do not appear as separate rows in the list
- Use the modal (click on the variant icon) to get a quick variant overview

---

*Source: https://docs.shopware.com/de/shopware-6-de/produkte/uebersicht*
