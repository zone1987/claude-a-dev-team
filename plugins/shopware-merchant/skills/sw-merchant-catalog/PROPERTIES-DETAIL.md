# Shopware 6 – Eigenschaften (Properties): complete reference

> Source: https://docs.shopware.com/de/shopware-6-de/produkte/eigenschaften  
> Applies from: Shopware 6.4.0.0+

---

## Contents

- [1. What are properties?](#1-what-are-properties)
- [2. Property overview](#2-property-overview)
- [3. Creating a new property](#3-creating-a-new-property)
- [4. Creating Ausprägungen (options / values)](#4-creating-ausprägungen-options--values)
- [5. Assigning properties to products](#5-assigning-properties-to-products)
- [6. Properties as the basis for variants](#6-properties-as-the-basis-for-variants)
- [7. Properties in the product filter](#7-properties-in-the-product-filter)
- [8. Difference: properties vs. Zusatzfelder vs. Wesentliche Merkmale](#8-difference-properties-vs-zusatzfelder-vs-wesentliche-merkmale)
- [9. Tips](#9-tips)

## 1. What are properties?

Eigenschaften (Properties) are filterable product information in Shopware 6. They serve two main purposes:

1. **Product filter**: customers can filter by properties in the listing (e.g. size: M, colour: red)
2. **Variant generation**: properties are the basis for product variants

Managed under: **Kataloge** (Catalogues) > **Eigenschaften** (Properties)

---

## 2. Property overview

### Columns of the list

| Column | Description |
|---|---|
| Eigenschaftsname (Property name) | Name of the property group (e.g. "Größe" (Size), "Farbe" (Colour)) |
| Ausprägungen (Options) | Assigned values (e.g. "XS, S, M, L, XL, XXL") |
| Beschreibung (Description) | Optional description of the property |
| Produktfilter-Sichtbarkeit (Product filter visibility) | Shows whether the property appears in the filter |
| Action menu ("...") | Bearbeiten (Edit) or Löschen (Delete) |

> **WARNING**: deleting a property removes it **from all assigned products** including all options!

---

## 3. Creating a new property

1. Click on **"Eigenschaft hinzufügen"** (Add property)
2. Fill in the basic information (see the fields below)
3. Add Ausprägungen (options / values)
4. Save

### 3.1 Basic information fields

| Field | Description | Mandatory |
|---|---|---|
| Name | Property name; appears on the product detail page and in filters | Yes |
| Beschreibung | Optional explanation of the property | No |
| Produktfilter-Sichtbarkeit | Toggle; determines whether this property appears in the listing filter | No |
| Anzeigetyp (Display type) | Kind of presentation in the filter | No |
| Sortierung (Sorting) | Sorting mode for the options | No |
| Position | Order on the product detail page | No |

### 3.2 Display types

| Type | Presentation in the filter | Presentation on the product |
|---|---|---|
| **Text** | Textual (default) | Textual |
| **Farbe** (Colour) | Coloured circles/tiles (HEX value) | Coloured option fields |
| **Bild** (Image) | Custom images | Images as a selection |
| **Dropdown** | Text-based in the filter | Dropdown menu on the detail page |

### 3.3 Sorting options

| Option | Behaviour |
|---|---|
| **Alphanumerisch** (Alphanumeric) | Automatic sorting a–z, then 1–10 |
| **Benutzerdefiniert** (Custom) | Controllable manually via the position field of the options |

---

## 4. Creating Ausprägungen (options / values)

Options are the concrete values of a property.  
Example: property "Größe" → options: XS, S, M, L, XL, XXL

### 4.1 Fields per option

| Field | Description | Available for type |
|---|---|---|
| Name | Label of the option (e.g. "Rot" (Red), "XL") | All |
| Position | Numeric position for custom sorting | All |
| Farb-HEX (Colour HEX) | Hexadecimal colour value (e.g. `#FF0000`) | Only type: Farbe |
| Bild | Image upload or URL | Only type: Bild |

### 4.2 Image upload for options (type: Bild)

Two methods:
1. **Choose from the media management**: select existing media from Inhalte (Content) > Medien (Media)
2. **Upload a local file**: upload a file from the computer directly
3. **URL import**: enter a publicly reachable image URL

---

## 5. Assigning properties to products

In the product screen under **tab Spezifikationen (Specifications) > Eigenschaften**:

1. Open the product screen (Kataloge > Produkte (Products) > product)
2. Choose the tab **Spezifikationen**
3. Area **Eigenschaften** → click **Eigenschaft hinzufügen**
4. Choose the property group from the dropdown
5. Select the options (values)
6. Multiple assignments from different property groups are possible

### AI Copilot (commercial plan)

The **AI Copilot** can configure properties automatically from the product description:
- The description must be sufficiently detailed
- The AI recognises relevant properties and suggests options
- Suggestions can be adjusted manually

---

## 6. Properties as the basis for variants

Properties form the basis for product variants:

1. Create the product (main product)
2. Open the tab **Varianten** (Variants)
3. Click on **"Eigenschaften zuweisen"** (Assign properties)
4. Select the property groups with the desired options
5. Configure variant exclusions (optional)
6. Click **"Varianten generieren"** (Generate variants)

Shopware then automatically creates all combinations of the selected options.

**Example:**
- Property "Größe": S, M, L
- Property "Farbe": Rot, Blau
- Results in: 6 variants (S/Rot, S/Blau, M/Rot, M/Blau, L/Rot, L/Blau)

---

## 7. Properties in the product filter

For a property to appear in the listing filter:

1. Edit the property
2. Activate **"Produktfilter-Sichtbarkeit"**
3. Save

The property then appears automatically in the filter options of the associated category pages.

---

## 8. Difference: properties vs. Zusatzfelder vs. Wesentliche Merkmale

| Function | Eigenschaften | Zusatzfelder (Custom fields) | Wesentliche Merkmale (Essential characteristics) |
|---|---|---|---|
| Filterable | Yes | No | No |
| Variant basis | Yes | No | No |
| Storefront filter | Yes | No | No |
| Cart/checkout | No | Possible | Yes |
| Free text | No | Yes | No |
| Template variable | No | Yes | No |

---

## 9. Tips

- Property names should be chosen **consistently** and **unambiguously** (e.g. always "Größe" instead of "Größe" sometimes and "Size" other times)
- Options can be added **later** without affecting existing variants
- For type **Farbe**: enter the HEX value correctly (#RRGGBB format)
- **Sorting**: with alphanumeric sorting, numbers are sorted correctly (1, 2, 10 instead of 1, 10, 2)
- Removing properties from a product does **not** delete the property system-wide

---

*Source: https://docs.shopware.com/de/shopware-6-de/produkte/eigenschaften*
