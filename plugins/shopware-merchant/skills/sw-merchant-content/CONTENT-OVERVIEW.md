# Shopware 6 – Inhalte (Content): full overview

**Source:** https://docs.shopware.com/de/shopware-6-de/inhalte  
**Version:** from 6.7.0.0

---

## Contents

- [Area in the admin](#area-in-the-admin)
- [Erlebniswelten (Shopping Experiences)](#erlebniswelten-shopping-experiences)
- [Medien](#medien)
- [Themes](#themes)
- [CMS-Erweiterungen](#cms-erweiterungen)

## Area in the admin

Path: **Inhalte** (main navigation on the left)

The Inhalte area contains the four main modules:

1. **Erlebniswelten** (Shopping Experiences) – visual page builder (CMS)
2. **Medien** (Media) – central media library
3. **Themes** – design configuration of the storefront
4. **CMS-Erweiterungen** (CMS extensions) – additional functions (Shopware Evolve+)

---

## Erlebniswelten (Shopping Experiences)

Path: Inhalte > Erlebniswelten

Shopware's own drag-and-drop CMS. Allows layouts for various page types to be
created and assigned without any coding knowledge.

### Architecture

```
Layout
└── Sektion (Section)
    └── Block
        └── Element (Text, Bild, Video, ...)
```

### Layout types

| Type | Use | Particularity |
|---|---|---|
| Shopseite (Shop page) | T&Cs, imprint, contact | Assigned under Einstellungen (Settings) > Shops |
| Landingpage (Landing page) | Marketing pages | Own URL via category assignment |
| Kategorieseite (Category page) | Category start pages | Includes the product listing automatically |
| Produktseite (Product page) | Product detail pages | Individual adjustment per product possible |
| Bundle-Seite (Bundle page) | Product bundles | Automatic bundle data population |

### Block categories and elements

#### Text blocks
- Full WYSIWYG editor with formatting (bold, italic, lists, links)
- **Datenzuordnung** (Data mapping): dynamic content from category/product data
- **Variables**: `{{ variable }}` syntax for direct data entry
- **AI Copilot** (commercial): AI-generated text suggestions
- **Link types**: URL, product, category, email, phone

#### Image blocks
- Image selection from the media area or direct upload
- Data mapping for automatic image population
- **Display modes**: Standard | Füllen (Fill) | Strecken (Stretch)
- **Alignment**: configurable vertically and horizontally
- **Link**: the image can be used as a link
- **Size recommendation**: 1280×528 px for full-width images; max. 1320 px at Full HD

#### Slider
- **Display modes**: Original | Feste Höhe (Fixed height) | Zugeschnitten (Cropped)
- Minimum height configurable
- Arrow and dot navigation (can be enabled/disabled)
- Auto-play with delay (ms) – note the accessibility advice
- Images can be linked individually
- Decorative image flag for screen reader accessibility

#### Gallery
- Several display modes selectable
- Preview navigation (left or bottom)
- Zoom function
- Full-screen mode
- Aspect ratio retention

#### Commerce blocks

**Produktname & Hersteller-Logo** (Product name & manufacturer logo)
- On product pages: automatic population with the product name and manufacturer logo

**Drei Spalten Produkte-Boxen** (Three-column product boxes)
- Display up to 3 products
- Layout type: Standard | Großes Bild (Large image) | Minimaler Text (Minimal text)

**Produkt-Slider** (Product slider)
- Horizontal slider for several products
- Minimum width adjustable
- Border can be enabled/disabled
- Auto-rotation with animation duration (ms)

**Cross-Selling**
- Specify the product used as the cross-selling basis on the "Inhalt" (Content) tab
- Linked products are loaded automatically

**Bundles**
- Automatic population: product list, bundle name, gallery, description
- Specifically for the bundle page type

#### Video blocks

| Type | Particularities |
|---|---|
| Video (local) | Auto-play, mute, load on demand |
| YouTube | Enhanced privacy mode, start/end time |
| Vimeo | Colour adjustment, information overlay configurable |

**Caution**: auto-play automatically disables the sound option (accessibility).

#### Further blocks

- **Sidebar**: populated automatically (filters, navigation)
- **Formular** (Form): contact form with configurable recipient email addresses
- **HTML**: embed HTML directly (mind the HTML sanitizer settings)
- **3D models** (commercial, "Rise" plan): .glb format, realistic product visualisation

#### Product listing block (category pages)

Integrated into category pages automatically. Configurable:

**Sortings:**
- Enable/disable "Produktsortierung anzeigen" (Show product sorting)
- Custom or standard sortings
- Change the Priorität (Priority) by double-clicking
- Select the default sorting

**Filters:**
- General filters: Hersteller (Manufacturers), Preis (Price)
- Property-based filters configurable
- Filters are only shown if products with that property exist

---

### Settings in the layout editor

#### Block settings (click a block → right-hand sidebar)

| Setting | Beschreibung (Description) |
|---|---|
| Name | Designation for the navigator |
| Hintergrundfarbe (Background colour) | Colour picker incl. hex entry |
| Hintergrundbild (Background image) | Image from the media library |
| Bildmodus (Image mode) | Standard/Füllen/Strecken |
| Layout/CSS classes | Custom CSS classes and spacing |

#### Section settings

| Setting | Beschreibung |
|---|---|
| Sektionsname (Section name) | For identification in the navigator |
| CSS classes | Separate several with spaces |
| Größenmodus (Size mode) | Full width or centred |
| Mobile sidebar behaviour | "Nicht angezeigt" (Not displayed) to hide it on mobile |
| Hintergrundfarbe/-bild | Identical to the block settings |

#### Sichtbarkeit (Visibility) (viewport control)

Every element and every section can be shown/hidden depending on the device.
Setting per viewport: Desktop | Tablet | Mobil (Mobile).

#### Navigator

Right-hand sidebar tab. Shows all blocks as a hierarchy:
- **Drag & drop**: change the order by dragging
- **Plus icon**: duplicate the block
- **Bin icon**: delete the block

#### Error handling

When saving, the system shows:
- The exact error message
- The affected element
- The error position in the layout

---

### Layout assignment

#### Shop pages
Einstellungen > Shops > Stammdaten (Master data) > "Shopseiten" area

#### Category pages
Kataloge (Catalogues) > Kategorien (Categories) > open the category > "Layout" tab > assign the layout

#### Landing pages
1. Create a landing page layout
2. Assign it to a category under Kataloge > Kategorien
3. Access it via the category's URL

#### Product pages
Kataloge > Produkte (Products) > open the product > "Layout" tab > select the layout
→ individual element values can be overridden per product

#### Defining default layouts
Layout editor > sidebar > Layout-Zuweisung (Layout assignment) > Standardlayouts (Default layouts) > "Als Standardlayout verwenden" (Use as default layout)
- Saves time with new categories/products

---

## Medien

Path: Inhalte > Medien

Central media library. Details: `sw-merchant-content-media`

## Themes

Path: Inhalte > Themes

Design configuration (colours, fonts, logos). Details: `sw-merchant-content-themes`

## CMS-Erweiterungen

Path: Erweiterungen > CMS-Erweiterungen (Shopware Evolve+)

Details: `sw-merchant-content-cms-extensions`
