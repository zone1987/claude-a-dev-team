# Shopware 6 – Produkte (Products): complete reference

> Source: https://docs.shopware.com/de/shopware-6-de/kataloge/produkte  
> Applies from: Shopware 6.7.9.0+

---

## Contents

- [1. Produktübersicht (Product overview, list view)](#1-produktübersicht-product-overview-list-view)
- [2. Creating a new product – mandatory fields](#2-creating-a-new-product--mandatory-fields)
- [3. Area: Allgemein (General)](#3-area-allgemein-general)
- [4. Area: Zuweisung (Assignment)](#4-area-zuweisung-assignment)
- [5. Tab: Spezifikationen (Specifications)](#5-tab-spezifikationen-specifications)
- [6. Tab: Erweiterte Preise (Advanced prices)](#6-tab-erweiterte-preise-advanced-prices)
- [7. Tab: Varianten (Variants)](#7-tab-varianten-variants)
- [8. Tab: Layout](#8-tab-layout)
- [9. Tab: SEO](#9-tab-seo)
- [10. Tab: Cross Selling](#10-tab-cross-selling)
- [11. Tab: Bundles (Shopware Services feature)](#11-tab-bundles-shopware-services-feature)
- [12. Tab: Bewertungen (Reviews)](#12-tab-bewertungen-reviews)
- [13. Digital products](#13-digital-products)
- [14. Advanced editing mode](#14-advanced-editing-mode)
- [15. Mehrfachänderung (Bulk edit) in the product overview](#15-mehrfachänderung-bulk-edit-in-the-product-overview)
- [16. Product overview link collection](#16-product-overview-link-collection)

## 1. Produktübersicht (Product overview, list view)

Path: **Kataloge** (Catalogues) > **Produkte** (Products)

### Columns of the overview

| Column | Description |
|---|---|
| Aktiv (Active) | Availability status in the shop (green/red dot) |
| Name | Product name, appears on the product detail page |
| Produktnummer (Product number) | Unique identifier of the product |
| Preis (Price) | Price for the default customer group |
| Lagerbestand (Stock) | Current stock (colour coding: red=0, yellow=1–25, green>25) |
| Hersteller (Manufacturer) | Name of the assigned manufacturer |

Columns can be sorted ascending and descending by clicking the column header.
Columns that are not needed can be hidden via **Listeneinstellungen** (List settings).
The **Kompaktmodus** (Compact mode) can also be activated via the list settings.

### Context menu per product

- **Bearbeiten** (Edit): opens the product detail screen
- **Duplizieren** (Duplicate): creates a copy of the product
- **Löschen** (Delete): deletes the product permanently

> **Note**: deleted products remain visible as line items in existing orders. Recommendation: set them to inactive instead of deleting them.

For variant products an icon appears in front of the product name. Clicking it opens a modal with variant details.

---

## 2. Creating a new product – mandatory fields

1. Click on **"Produkt hinzufügen"** (Add product)
2. Minimum information before saving for the first time:
   - **Titel** (Title) – product name
   - **Produktnummer** – manual or auto-generated
   - **Steuersatz** (Tax rate) – choose from the dropdown
   - **Bruttopreis** (Gross price) and **Nettopreis** (Net price)
   - **Lagerbestand** – number ≥ 0
3. Click on **"Speichern"** (Save) → the tabs are unlocked

---

## 3. Area: Allgemein (General)

### 3.1 Informationen (Information)

| Field | Description |
|---|---|
| Titel | Product name for the listing and detail page |
| Hersteller | Selection from existing manufacturers or creation directly in the field |
| Produktnummer | Individually assigned, must be unique |
| Beschreibung (Description) | WYSIWYG editor; paste without formatting: `Ctrl+Shift+V` (Mac: `Cmd+Shift+V`) |
| Produkt hervorheben (Highlight product) | Activates a badge in the listing (e.g. "Neu" (New), "Empfohlen" (Recommended)) |
| AI description assistant | Available from the Rise plan; generates descriptions from product data |

### 3.2 Preise (Prices)

| Field | Description |
|---|---|
| Steuersatz | The default is preselected, must be set correctly |
| Bruttopreis | Selling price incl. VAT |
| Nettopreis | Selling price excl. VAT; both fields are linked (chain icon) |
| Einkaufspreis (Purchase price) | Internal calculation value, not public |
| Streichpreis (List price) | RRP / original price (shown with a strikethrough) |
| Günstigster Preis (Lowest price) (30 days) | EU price indication directive: lowest price of the last 30 days |
| Currency prices | Separate prices can be set for every configured currency channel |
| Chain icon | Links gross and net – changing one field calculates the other automatically |

### 3.3 Lieferbarkeit (Availability)

| Field | Description |
|---|---|
| Lagerbestand | Current stock; can be changed at any time |
| Abverkauf (Clearance sale) | When activated: sale only until stock = 0; not purchasable afterwards |
| Lieferzeit (Delivery time) | Overrides the delivery time of the assigned shipping method |
| Wiederauffüllzeit (Restock time) | Stated in days, when the item will be available again |
| Versandkostenfrei (Free shipping) | Yes/no – the product is exempt from shipping costs |
| Mindestabnahme (Minimum purchase) | Minimum quantity per order |
| Staffelung (Purchase steps) | In which quantity multiples it can be ordered |
| Maximalabnahme (Maximum purchase) | Maximum quantity per order |

### 3.4 Lagerhäuser (Warehouses) and warehouse groups (from 6.4.19.0, Beyond plan)

- Dropdown to select the warehouse group
- After the selection appears: "Verfügbarkeit und Lieferzeit nach Lagern anzeigen" (Show availability and delivery time per warehouse)
- The detail screen shows the stock per individual warehouse
- Priority configurable per warehouse
- Delivery time tab with predefined options: immediately, 1–3 days, 2–5 days, 1–2 weeks, 3–4 weeks

---

## 4. Area: Zuweisung (Assignment)

### 4.1 Visibility and categories

| Field | Description |
|---|---|
| Verkaufskanal (Sales channel) | Sales channels assigned to the product |
| Aktiv | Controls whether the product appears in the storefront |
| Kategorien (Categories) | Multiple assignment possible; appears in the category navigation |
| Erweiterte Sichtbarkeit (Advanced visibility) | Options: visible (listing + search) / hide in product lists / hide in product lists and search |
| Tags | Keywords for rule targeting and internal sorting |
| Such-Schlagwörter (Search keywords) | Extend the search index with additional terms |

### 4.2 Medien (Media)

- Upload product photos, videos, 3D models
- **Recommended image size**: square, 600×600 px (optimal)
- **Zoom quality**: up to 1920×1920 px possible
- **Video formats**: webm, mkv, flv, ogv, ogg, avi, mov, wmv, mp4 (recommendation: MP4)
- **3D models**: GLB format only, rendered with the ThreeJS library
- **AR activation**: possible for iOS 12+ and Android 8.0+ with ARCore 1.9

### 4.3 Auszeichnung (Labelling)

| Field | Description |
|---|---|
| Erscheinungsdatum (Release date) | Informative date for customers (no purchase stop!) |
| EAN | European Article Number / barcode |
| Herstellernummer (Manufacturer number) | Internal reference, not publicly visible |

---

## 5. Tab: Spezifikationen (Specifications)

### 5.1 Dimensions & packaging

**Product dimensions** (can be used for shipping cost calculation):

| Field | Unit |
|---|---|
| Breite (Width) | mm or cm |
| Höhe (Height) | mm or cm |
| Länge (Length) | mm or cm |
| Gewicht (Weight) | kg or g |

**Sales & packaging information** (for the unit price calculation):

| Field | Description |
|---|---|
| Verkaufseinheit (Packing unit) | Content of the product (e.g. 0.25 or 700) |
| Produkteinheit (Product unit) | Unit of the content (e.g. litre, bottle, piece) |
| Grundeinheit (Base unit) | Reference unit for the unit price (e.g. 1 kg, 1 L) – **mandatory** |
| Verpackungseinheit (Packaging unit) | Number of units in the packaging |
| Verpackungseinheit-Mehrzahl (Packaging unit plural) | Plural of the packaging unit |

The **unit price calculation** requires: Verkaufseinheit + Produkteinheit + Grundeinheit.  
Example: bottle with 0.25 L → Verkaufseinheit: 0.25, Produkteinheit: litre, Grundeinheit: 1 litre

### 5.2 Eigenschaften (Properties)

- Filterable product information (e.g. size, colour, material)
- Selection from predefined properties (Kataloge > Eigenschaften)
- Multiple assignments possible
- A search function is available in the selection field
- **AI Copilot**: automatic configuration from the description text (requires a commercial plan)

### 5.3 Wesentliche Merkmale (Essential characteristics)

- Template-based selection
- Shows the most important product characteristics in the cart and checkout
- Can contain: properties, custom fields, product information, unit price details

### 5.4 Zusatzfelder (Custom fields)

- Shows the assigned custom field sets
- Possible field types: checkbox, images, colour picker, text, number, date
- Can be included in templates via variables

---

## 6. Tab: Erweiterte Preise (Advanced prices)

Price rules are based on the **Rule Builder**:

- Quantity-dependent scaled prices
- Customer or customer-group specific prices
- Time-limited price campaigns
- Per rule: gross, net, list price, lowest price (30 days) can be set

---

## 7. Tab: Varianten (Variants)

### 7.1 Generating variants

1. Click the link **"Eigenschaften zuweisen"** (Assign properties)
2. Select the property group (must be created under Kataloge > Eigenschaften)
3. Activate options (checkboxes per option value)
4. Define price surcharges and discounts per option (optional)
5. Configure variant exclusions (several conditions with an AND link)
6. Click **"Varianten generieren"** (Generate variants)

### 7.2 Sorting options in the variant list

- Name, Preis, Lagerbestand, Produktnummer, Aktiv

### 7.3 Storefront presentation

The **display order of properties and options** in the storefront is configurable.  
An **image assignment** per variant is possible.

**Product list display mode:**

| Mode | Behaviour |
|---|---|
| Single main variant → Main product | No preselected variant in the listing |
| Single main variant → Single Variant | Predefined variant preselected (dropdown selection) |
| Expanding the properties | Several variants as separate products in the listing |

### 7.4 Editing a single variant

- The chain icon shows whether a field is **inherited** from the main product (purple icon)
- Removing the inheritance = the field becomes directly editable
- All areas of the main screen can be configured individually per variant

### 7.5 Quick changes (inline editing)

- A **double click** on a row activates quick editing
- Purple chain icon = the inheritance can be removed
- Fields: Preis, Lagerbestand, Produktnummer, Medien, Aktiv status

### 7.6 Mehrfachänderung (Bulk edit) for variants

- Up to **1000 variants** can be selected at once (also across pages)
- Available operations: Überschreiben (Overwrite), Leeren (Clear), Hinzufügen (Add), Entfernen (Remove)
- Progress is shown via a notification

---

## 8. Tab: Layout

- Assign an Erlebniswelten (Shopping Experiences) layout to the product
- Assign an existing layout **or** create a new layout
- Blocks can be edited directly in the product context without switching to Erlebniswelten

---

## 9. Tab: SEO

### 9.1 SEO settings

| Field | Recommendation |
|---|---|
| Meta-Titel (Meta title) | A maximum of ~70 characters (search engines truncate) |
| Meta-Beschreibung (Meta description) | Ideally 130–160 characters |
| Schlüsselwörter (Keywords) | No direct ranking influence, but usable for the internal search |
| Canonical URL for all variants | Defines which variant holds the canonical URL |

### 9.2 SEO URLs

- A separate URL can be defined per Verkaufskanal
- The SEO path is generated automatically from the product name
- For products in several categories: select the **Hauptkategorie** (Main category) for the URL

---

## 10. Tab: Cross Selling

### Type: Dynamische Produktgruppe (Dynamic product group)

| Field | Description |
|---|---|
| Titel | Name of the cross-selling block |
| Aktiv | Switch on/off |
| Position | Order (1, 2, 3, …) |
| Produktgruppe (Product group) | Selection of the dynamic product group |
| Sortierung (Sorting) | Name, price, release date |
| Maximum number of products | Number of products shown |
| Vorschau (Preview) | Shows the products that currently match |

### Type: manual assignment

Identical fields to the above, additionally:
- Manual selection of the assigned products (single or multiple selection)

---

## 11. Tab: Bundles (Shopware Services feature)

### Adding bundles

1. Click **"Produkt zu Bundles hinzufügen"** (Add product to bundles)
2. Search for existing bundles
3. Multiple selection possible
4. Confirm

### Editing bundles

- Overview: number of products, availability, active status
- Context menu:
  - Open the bundle details
  - Show / do not show on the product detail page
  - Remove the bundle

Synchronisation is **bidirectional** between the product and the bundle management.

---

## 12. Tab: Bewertungen (Reviews)

- Overview of all customer reviews for this product
- The **Sichtbar** (Visible) marking is required for a review to appear in the storefront
- Editing via the context menu
- Link to the review detail page (Kataloge > Bewertungen)

---

## 13. Digital products

Digital products use the same screen, additionally:

| Characteristic | Detail |
|---|---|
| File upload | In the Medien area; all common digital formats |
| Backend recognition | A badge indicates that this is a digital product |
| Varianten | Also possible for digital products (e.g. physical + digital) |
| Order process | Checkbox for the legal notice when ordering |
| Delivery | E-mail with the file attached after the payment is received |
| Customer account | Customers download the file under "Mein Konto > Bestellungen" (My account > Orders) |

---

## 14. Advanced editing mode

- Toggle at the top right of the product screen
- When deactivated: checkboxes to show/hide sections
- Affects the areas "Allgemein" and "Spezifikationen"
- Enables a simplified view for beginners

---

## 15. Mehrfachänderung (Bulk edit) in the product overview

1. Select products in the list (max. 1000)
2. Click **"Mehrfachänderung"**
3. Tick the checkboxes of the fields to be changed
4. Enter values
5. Dropdown operations:
   - **Überschreiben**: replace existing values
   - **Leeren**: remove all settings of the block
   - **Hinzufügen**: add without deleting what exists
   - **Entfernen**: delete specific settings selectively
6. Save → progress display

---

## 16. Product overview link collection

| Area | Admin path |
|---|---|
| Produktübersicht | Kataloge > Produkte |
| Eigenschaften | Kataloge > Eigenschaften |
| Kategorien | Kataloge > Kategorien |
| Dynamische Produktgruppen | Kataloge > Dynamische Produktgruppen |
| Steuern (Taxes) | Einstellungen (Settings) > Handel (Commerce) > Steuern |
| Versandarten (Shipping methods) | Einstellungen > Versand (Shipping) > Versandarten |
| Lagerhäuser (Warehouses) | Einstellungen > Lagerhäuser |
| Erlebniswelten | Inhalte (Content) > Erlebniswelten |

---

*Source: https://docs.shopware.com/de/shopware-6-de/kataloge/produkte*
