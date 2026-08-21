# Shopware 6 – Dynamische Produktgruppen (Dynamic product groups): complete reference

> Source: https://docs.shopware.com/de/shopware-6-de/Kataloge/DynamischeProduktgruppen  
> Applies from: Shopware 6.4.12.0+

---

## Contents

- [1. What are dynamic product groups?](#1-what-are-dynamic-product-groups)
- [2. Product group overview](#2-product-group-overview)
- [3. Creating a new product group](#3-creating-a-new-product-group)
- [4. Bedingungen (Conditions) / rule set](#4-bedingungen-conditions--rule-set)
- [5. Vorschau (Preview)](#5-vorschau-preview)
- [6. Areas of use](#6-areas-of-use)
- [7. Status and validation](#7-status-and-validation)
- [8. Examples](#8-examples)
- [9. Tips and best practices](#9-tips-and-best-practices)

## 1. What are dynamic product groups?

Dynamische Produktgruppen (also: product streams) are rule-based product sets. Shopware automatically collects all products that fulfil the defined conditions. The group updates dynamically – new products that fulfil the rules are added automatically; products that no longer match drop out automatically.

Managed under: **Kataloge** (Catalogues) > **Dynamische Produktgruppen**

---

## 2. Product group overview

### Columns of the overview

| Column | Description |
|---|---|
| Name | Name of the product group |
| Beschreibung (Description) | Optional description |
| Änderungsdatum (Modification date) | Date of the last edit |
| Status | Shows whether all rules are valid and fully configured |

### Context menu

| Option | Description |
|---|---|
| Bearbeiten (Edit) | Opens the editing screen of the product group |
| Duplizieren (Duplicate) | Creates a copy including all conditions |
| Löschen (Delete) | Deletes the product group (assignments in categories etc. are removed as well) |

---

## 3. Creating a new product group

1. Click on **"Produktgruppe anlegen"** (Create product group)
2. Enter a **Name** (mandatory field)
3. Enter a **Beschreibung** (optional)
4. **Speichern** (Save) or **"Speichern und duplizieren"** (Save and duplicate)
5. Define the conditions in the rule set

---

## 4. Bedingungen (Conditions) / rule set

### 4.1 Structure of the rule set

The rule set is a visual editor with the following elements:

| Element | Description |
|---|---|
| Property selection (1) | Kind of condition (category, price, tag, etc.) |
| Condition type (2) | Comparison operator (equals, greater than, etc.) |
| UND (AND) link (3) | All conditions on this level must apply |
| ODER (OR) link (4) | At least one condition must apply |
| Unterbedingungen (Sub-conditions) (5) | Nested condition groups |
| Context menu (6) | Insert before/after existing conditions |
| Vorschau (Preview) button (7) | Shows the products that currently match the rules |

### 4.2 Available operators

| Operator | Meaning |
|---|---|
| Gleich (Equals) | Exactly this value |
| Ungleich (Not equal) | Not this value |
| Eins von (One of) | One of the given values |
| Keins von (None of) | None of the given values |
| Alle von (All of) | All given values must apply |
| Alle außer (All except) | All except the given values |
| Größer als (Greater than) | Numeric comparison (e.g. price) |
| Kleiner als (Less than) | Numeric comparison |
| Größer gleich (Greater or equal) | Numeric comparison including equality |
| Kleiner gleich (Less or equal) | Numeric comparison including equality |
| Enthält (Contains) | Text substring search |
| Enthält nicht (Does not contain) | Text substring exclusion |

### 4.3 Available condition types

**Product conditions:**
- Produkt (Product) (explicit product selection by ID/name)
- Produktnummer (Product number)
- Produktname (Product name)

**Category conditions:**
- Kategorie (Category) (with category path selection)
- Category tree level

**Properties and options:**
- Property group
- Property option (specific value)

**Tags:**
- Tag (keyword assignment)

**Price conditions:**
- Preis (Price) (gross/net, filterable separately per currency)
- Streichpreis (List price)
- Einkaufspreis (Purchase price)

**Stock & availability:**
- Lagerbestand (Stock) (numeric comparison)
- Abverkauf (Clearance sale) (yes/no)
- Versandkostenfrei (Free shipping) (yes/no)

**Delivery times:**
- Lieferzeit (Delivery time) (ID or name of the delivery time)

**Manufacturer:**
- Hersteller (Manufacturer) (selection of the manufacturer)

**Media:**
- Has media / has no media

**Active status:**
- Produkt aktiv (Product active) (yes/no)

**Custom fields:**
- Zusatzfelder (Custom fields) – field-specific conditions

### 4.4 Link logic

```
Bedingungsgruppe (UND)
├── Kategorie = "Bekleidung"           ← muss zutreffen
└── ODER-Gruppe
    ├── Farbe = "Rot"                  ← mindestens eine dieser
    └── Farbe = "Blau"                 ← Bedingungen muss zutreffen

+ Preis < 50 EUR                       ← muss ebenfalls zutreffen
```

Sub-conditions allow complex nesting for a precise product selection.

---

## 5. Vorschau (Preview)

The **Vorschau** button shows in real time which products currently match the defined rules.

- Shows product name, price, stock
- Helps with testing and validating the rules before activation
- Updates immediately after rule changes

---

## 6. Areas of use

### 6.1 Filling categories dynamically

Instead of a manual product assignment in categories:

1. Open the category (Kataloge > Kategorien (Categories))
2. Tab **Produkte** (Products)
3. Choose type: **Dynamische Produktgruppe**
4. Select the product group

> **Note**: switching to dynamic assignment deactivates all manual assignments in this category!

### 6.2 Product feeds / product comparisons

- Product groups can be used for external feeds (e.g. Google Shopping)
- Enables automatic feed updates without manual maintenance

### 6.3 Erlebniswelten (Shopping Experiences) (product slider)

In Erlebniswelten (Inhalte (Content) > Erlebniswelten):
- The **commerce block "Produkt-Slider"** (Product slider) can use a dynamic product group as its source
- Products update automatically depending on rule fulfilment

### 6.4 Cross-selling on the product detail page

In the product screen under **tab Cross Selling**:
- Choose type: **Dynamische Produktgruppe**
- Select the product group
- Set the sorting (name, price, release date) and the maximum number

---

## 7. Status and validation

The **Status** in the overview shows:
- Green/active: all rules are valid and fully configured
- Red/inactive: rules have errors or are incomplete (e.g. missing values)

---

## 8. Examples

### Example 1: all products under 20 EUR in the category "Sale"

Conditions:
```
UND
├── Kategorie = "Sale"
└── Preis <= 20.00 EUR
```

### Example 2: products of one manufacturer in a certain colour

Conditions:
```
UND
├── Hersteller = "Nike"
└── Eigenschaft Farbe = EINS VON ["Rot", "Blau", "Schwarz"]
```

### Example 3: new products of the last 30 days with stock

Conditions:
```
UND
├── Lagerbestand > 0
├── Abverkauf = Nein
└── Erscheinungsdatum >= [Datum vor 30 Tagen]
```

### Example 4: marking bestsellers by tag

Conditions:
```
UND
└── Tag = "Bestseller"
```
(add the tag "Bestseller" to the products manually)

---

## 9. Tips and best practices

- Dynamic product groups should have **meaningful names** that clearly describe their content
- Use the **Vorschau** before saving to avoid unexpected product sets
- Complex nesting makes rules hard to maintain → keep it simple
- Date-based conditions are well suited for seasonal campaigns
- Too many ODER links can result in very large product sets → check the product count in the Vorschau
- When **duplicating** a product group, all conditions are carried over – ideal for similar groups

---

*Source: https://docs.shopware.com/de/shopware-6-de/Kataloge/DynamischeProduktgruppen*
