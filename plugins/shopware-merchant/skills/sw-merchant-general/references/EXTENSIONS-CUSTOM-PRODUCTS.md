# Custom Products – configurable products

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/customproducts  
**Plan**: Shopware Rise (or higher)  
**Path in the admin**: Katalog (Catalogue) > Custom Products

## Contents

- [Overview](#overview)
- [Concept](#concept)
- [Creating a template](#creating-a-template)
- [Option types (12 available)](#option-types-12-available)
- [Price configuration](#price-configuration)
- [Display modes in the storefront](#display-modes-in-the-storefront)
- [Advanced features](#advanced-features)
- [Linking a template to a product](#linking-a-template-to-a-product)
- [Common use cases](#common-use-cases)

## Overview

**Custom Products** makes it possible to offer products with individually configurable options.
Customers can personalise products on the product detail page (for example engravings, prints,
colours, measurements).

---

## Concept

```
Custom Products Template
└── Produkt-Template (Vorlage)
    ├── Optionsgruppe 1 (z. B. "Beschriftung")
    │   ├── Option: Textfeld (Eingabe)
    │   └── Option: Schriftart (Dropdown)
    └── Optionsgruppe 2 (z. B. "Material")
        ├── Option: Holz (+5,00 €)
        └── Option: Metall (+15,00 €)
```

Templates are created and then linked to **any number of products**.

---

## Creating a template

1. Open **Katalog** (Catalogue) **> Custom Products**
2. Create a **Neues Template** (New template)
3. Assign a template name (internal)
4. Add option groups and options

---

## Option types (12 available)

| Type | Description |
|---|---|
| **Textfeld** (Text field) | Single-line text input ("Mit dem Textfeld bietest Du dem Kunden die Möglichkeit, dem Artikel einen einzeiligen Text hinzuzufügen.") |
| **Textarea** | Multi-line text input |
| **Datum** (Date) | Date selection |
| **Zeit** (Time) | Time selection |
| **Farbwähler** (Colour picker) | Colour palette to choose from |
| **Bildauswahl** (Image selection) | Customers upload their own images |
| **Checkbox** | Yes/no option |
| **Mehrfachauswahl** (Multiple selection) | Several options selectable at the same time |
| **Einzelauswahl (Radio)** (Single selection) | Exactly one option selectable |
| **Dropdown** | Selection from a list |
| **Dateiupload** (File upload) | Customers upload files |
| **HTML-Editor** | Rich text input |

---

## Price configuration

### Surcharges per option
- **Absolut** (Absolute): Fixed amount (for example +5.00 €)
- **Relativ (%)** (Relative): Percentage surcharge on the base price
- **Währungsspezifisch** (Currency-specific): Different prices per currency
- **Regelbasiert (Advanced)** (Rule-based): Rule Builder surcharges

### Price display
The final price = base price + the sum of all selected surcharges.
The configuration is shown in the cart and in the order overview.

---

## Display modes in the storefront

### Normal mode
- All options visible at the same time
- Displayed **above** the "In den Warenkorb" (Add to cart) button

### Step-by-step mode
- Customers are guided through the options
- One group visible at a time
- A "Weiter" (Next) button between the groups

---

## Advanced features

| Feature | Description |
|---|---|
| **Inkompatible Optionen ausschließen** (Exclude incompatible options) | Prevent certain combinations |
| **Konfiguration bestätigen** (Confirm configuration) | Customers must explicitly confirm the configuration |
| **Konfigurationslink teilen** (Share configuration link) | Customers can share their configuration as a link |
| **Dateizugriff in Bestelldetails** (File access in order details) | Uploaded files can be retrieved in the admin |

---

## Linking a template to a product

1. Open the product in **Katalog** (Catalogue) **> Produkte** (Products)
2. Select the **Custom Products** tab
3. Select an existing template or create a new one

A template can be linked to any number of products.

---

## Common use cases

- Print shops: text/image prints on T-shirts, mugs
- Jewellery: engravings, choice of material
- Joineries: measurements, type of wood, colour
- Baked goods: lettering, decoration
- Photo services: image upload for photo prints
