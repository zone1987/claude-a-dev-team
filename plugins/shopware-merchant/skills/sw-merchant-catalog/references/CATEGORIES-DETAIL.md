# Shopware 6 – Kategorien (Categories): complete reference

> Source: https://docs.shopware.com/de/shopware-6-de/kataloge/kategorien  
> Applies from: Shopware 6.4.0.0+

---

## Contents

- [1. Category overview](#1-category-overview)
- [2. Creating a category](#2-creating-a-category)
- [3. Category types](#3-category-types)
- [4. Tab: Allgemein (General)](#4-tab-allgemein-general)
- [5. Tab: Produkte (Products)](#5-tab-produkte-products)
- [6. Tab: Layout](#6-tab-layout)
- [7. Tab: SEO](#7-tab-seo)
- [8. Category structure examples](#8-category-structure-examples)
- [9. Landing pages](#9-landing-pages)
- [10. Tips and notes](#10-tips-and-notes)

## 1. Category overview

Path: **Kataloge** (Catalogues) > **Kategorien** (Categories)

The category management shows a **tree structure** (left-hand side) with all categories that exist.

### Tree structure features

- **Drag & drop**: categories can be moved on all levels
- Categories can be dragged under others to become subcategories
- Several independent category trees are possible (e.g. for footer, service navigation)
- Right-click / three-dot menu opens the context menu

---

## 2. Creating a category

### Context menu options

| Option | Result |
|---|---|
| Neue Kategorie davor (New category before) | New category on the same level, before the current one |
| Neue Kategorie danach (New category after) | New category on the same level, after the current one |
| Neue Subkategorie (New subcategory) | Subordinate category below the current one |
| Bearbeiten (Edit) | Opens the editing view |
| Löschen (Delete) | Deletes the category including all subcategories |

### Step by step

1. Open the context menu of the parent category
2. Choose the desired creation option
3. Enter the category name
4. Confirm with the check mark
5. Open the category and switch on **"Kategorie ist aktiv"** (Category is active)
6. Assign a Verkaufskanal (Sales channel) (if it is an entry point)

> **Important**: newly created categories are **inactive** at first!

---

## 3. Category types

| Type | Use | Tabs available |
|---|---|---|
| Seite/Liste (Page/List) | Standard product listing, shop pages | Allgemein, Produkte, Layout, SEO |
| Strukturierungselement/Einstiegspunkt (Structuring element/Entry point) | Navigation grouping only, no content | Allgemein |
| Link | Redirect to internal/external targets | Allgemein |

---

## 4. Tab: Allgemein (General)

### 4.1 Basic settings

| Field | Description |
|---|---|
| Name (1) | Category name; can be changed later; appears in the navigation |
| Kategorie ist aktiv (Category is active) (2) | Switch; determines whether the category appears in the frontend |
| Tags (3) | Keywords for other program areas (e.g. Rule Builder) |
| Kategorietyp (Category type) (4) | Selection: Seite/Liste, Strukturierungselement, Link |

### 4.2 Benutzerdefinierter Link (Custom link) (only for type "Link")

| Field | Description |
|---|---|
| Linktyp (Link type) (1) | External (URL) or internal (Shopware entity) |
| Entität / Linkziel (Entity / Link target) (2) | External: full URL; internal: entity selection |
| In neuem Tab öffnen (Open in new tab) (3) | Opens the link in a new browser tab |

### 4.3 Einstiegspunkt (Entry point) (for Seite/Liste and Strukturierungselement)

| Field | Description |
|---|---|
| Einstiegspunkt (Entry point) (1) | Where the category tree is anchored in the shop |
| | **Hauptnavigation** (Main navigation): classic product structure at the top |
| | **Footernavigation** (Footer navigation): lower page area (imprint, privacy policy) |
| | **Servicenavigation** (Service navigation): top right (e.g. login, contact) |
| Verkaufskanäle (Sales channels) (2) | Multiple selection; which channels this tree is assigned to |
| Startseite konfigurieren (Configure home page) (3) | Channel-specific home page settings |

### 4.4 Menü-Einstellungen (Menu settings)

| Field | Description |
|---|---|
| In der Navigation ausblenden (Hide in navigation) (1) | Removes the category from the navigation bar (the page stays reachable) |
| Anzeigebild (Display image) (2) | Image shown in the navigation dropdown menu |
| Beschreibung (Description) (3) | Customer information about the category (e.g. in the hover menu) |

---

## 5. Tab: Produkte (Products)

| Field | Description |
|---|---|
| Typ (Type) (1) | Manual selection or Dynamische Produktgruppe (Dynamic product group) |
| Produkte / Dynamische Produktgruppe (2) | Select products manually or link a product group |
| Produktliste (Product list) (3) | Overview of the currently assigned products |

> **Note**: when switching to dynamic assignment, all manual assignments in this category are deactivated!

---

## 6. Tab: Layout

### 6.1 Assigning a layout

- Select an Erlebniswelten (Shopping Experiences) layout from the existing layouts
- **"Neues Layout erstellen"** (Create new layout): opens the Shopping Experiences editor directly
- Blocks can be adjusted directly in the category context (without switching to Erlebniswelten)

### 6.2 Customisation hierarchy (multi-language)

Priority order for language selection (highest priority first):

1. Language-specific customisations in this category
2. Parent-child language fallback
3. System default language
4. Layout settings (lowest priority)

**Examples:**

- Only an English customisation exists → all storefronts show the English version
- Austrian customisation + layout English/German → Austria gets its own customisation
- German + English exist → Austria automatically inherits from German

### 6.3 Visibility and sorting

| Function | Description |
|---|---|
| Sichtbarkeit anzeigen (Show visibility) | Shows the viewport visibility of the layout block |
| Block-Sichtbarkeit (Block visibility) | Configurable per block (desktop/tablet/mobile) |
| Produkt-Sortierung anzeigen (Show product sorting) | Frontend dropdown for customers to sort |
| Eigene Sortierung verwenden (Use own sorting) | Enables advanced sorting options in the admin |
| Standard-Sortierung (Default sorting) | Fallback if no own sorting is chosen |
| Priorität (Priority) | Order when several sorting options exist |

---

## 7. Tab: SEO

| Field | Description |
|---|---|
| SEO-Titel (SEO title) | Title for search engines (appears in the browser tab) |
| SEO-Beschreibung (SEO description) | Meta description for search engines |
| Keywords | Additional search terms |
| SEO URLs | Configurable per Verkaufskanal; by default depends on the SEO settings |

---

## 8. Category structure examples

### Example 1: Shop with subcategories

```
Katalog #1 (Einstiegspunkt: Hauptnavigation)
├── Lebensmittel
│   ├── Getränke
│   └── Snacks
├── Bekleidung
│   ├── Herren
│   └── Damen
└── Freizeit & Elektro
```

Creation:
1. "Katalog #1" → context menu → "Neue Subkategorien"
2. Per main category: context menu → "Neue Subkategorie"

### Example 2: Several shops (subshop setup)

```
Katalog #1 (Verkaufskanal A)
├── Kategorie A1
└── Kategorie A2

Katalog #2 (Verkaufskanal B)
├── Kategorie B1
└── Kategorie B2
```

Creation:
1. "Katalog #1" → context menu → "Neue Kategorie danach" → "Katalog #2"
2. Assign the matching Verkaufskanal to each catalogue

---

## 9. Landing pages

Landing pages are **internal pages without a navigation entry**. They can only be reached via a direct URL.  
Address: `[Verkaufskanal-URL]/[Landingpage-SEO-URL]`

### Management

- Below the category overview (separate area)
- The order of landing pages is irrelevant
- Context menu: remove, duplicate, edit
- **"Landingpage hinzufügen"** (Add landing page) button

### Tab: Allgemein (Landing pages)

| Field | Description |
|---|---|
| Name (1) | Internal name and page title |
| Landingpage ist aktiv (Landing page is active) (2) | Controls URL accessibility |
| Verkaufskanäle (3) | Assignment to one or more channels |
| Tags (4) | Helps with the admin search |

### Tab: SEO (Landing pages)

| Field | Description |
|---|---|
| SEO-Titel | Search engine title |
| SEO-Beschreibung | Meta description |
| Keywords | Additional search terms |
| SEO URL (**mandatory field**) | Unique page identifier; e.g. "aktion-sommer" → URL: `www.shop.de/aktion-sommer` |

The SEO URL is generated automatically from the name, but can be adjusted manually.

### Tab: Layout (Landing pages)

Identical to the category layout:
- Assign an Erlebniswelt (Shopping Experience)
- Block-based customisation
- Multi-language customisations possible

---

## 10. Tips and notes

- Categories can serve as an entry point for several Verkaufskanäle
- One category can be visible in several shops (different Verkaufskanäle)
- When a parent category is deleted, **all subcategories** are deleted with it
- Products remain in the system after a category is deleted, but may no longer be assigned to any category
- The category sorting in the tree matches the sorting in the frontend

---

*Source: https://docs.shopware.com/de/shopware-6-de/kataloge/kategorien*
