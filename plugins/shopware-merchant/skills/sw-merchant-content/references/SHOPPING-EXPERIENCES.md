# Shopware 6 – Erlebniswelten (Shopping Experiences)

Path: **Inhalte** (Content) > **Erlebniswelten**

Shopware's visual drag-and-drop CMS for designing all page types.
No coding knowledge required.

## Architecture

```
Layout (page type)
└── Section
    └── Block (from the library)
        └── Element (text, image, video, ...)
```

## Creating a layout – step by step

1. **Inhalte > Erlebniswelten > "Neues Layout anlegen"** (Create new layout)
2. Choose the page type (Shopseite / Landingpage / Kategorieseite / Produktseite / Bundle — shop page / landing page / category page / product page / bundle)
3. Choose the section layout (sidebar or full width)
4. Name the layout → confirm
5. In the editor: insert blocks by drag and drop from the right-hand sidebar
6. Configure elements (content, appearance, links)
7. **Speichern** (Save) → assign the layout

## Block categories

Full reference: `SHOPPING-EXPERIENCES-DETAIL.md`

## Assigning a layout

| Page type | Assignment |
|---|---|
| Shopseite (Shop page) | Einstellungen (Settings) > Shops > Stammdaten (Master data) |
| Kategorieseite (Category page) | Kataloge (Catalogues) > Kategorien (Categories) > Layout tab |
| Landingpage (Landing page) | Kataloge > Kategorien (as a landing page) |
| Produktseite (Product page) | Kataloge > Produkte (Products) > Layout tab |
