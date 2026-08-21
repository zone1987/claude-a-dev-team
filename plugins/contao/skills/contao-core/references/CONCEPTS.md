# Contao 5 — Core Concepts

## Contents

- [Overview](#overview)
- [1. Data Container Arrays (DCA) & Models](#1-data-container-arrays-dca-models)
- [2. Front End Modules](#2-front-end-modules)
- [3. Content Elements](#3-content-elements)
- [4. Templating](#4-templating)
- [5. Assets & Images](#5-assets-images)
- [6. Hooks](#6-hooks)
- [7. Extensions (Bundles)](#7-extensions-bundles)
- [8. Insert Tags](#8-insert-tags)
- [Framework overview (further concepts)](#framework-overview-further-concepts)

## Overview

Contao offers a broad set of extension and customisation mechanisms. The eight
central concepts form the foundation of any Contao development.

---

## 1. Data Container Arrays (DCA) & Models

**DCA** (Data Container Arrays) are a core concept of the Contao framework. They
describe how records are managed — fields, palettes, list views,
operations and the database schema.

**Models** are object-oriented representations of DCA records. They allow
creating, loading and modifying data through a clean API.

Example: `NewsModel::findByPk(5)` — loads a news record as a model object.

**Key points:**
- One DCA file per table in `contao/dca/<tablename>.php`
- Define fields: `inputType`, `eval`, `sql`
- Palettes control the back end form view
- `PaletteManipulator` for non-destructive extensions of existing palettes

---

## 2. Front End Modules

Front end modules handle complex functionality on specific pages or
at specific places on the website. Examples: navigation lists, news lists,
member forms.

- Implemented as fragment controllers (`AbstractFrontendModuleController`)
- Registration via the `#[AsFrontendModule]` attribute
- DCA configuration in `tl_module`
- Template: `frontend_module/<type>.html.twig`

---

## 3. Content Elements

Content elements manage arbitrary and complex content within the
page structure — static page content, news detail views, etc.

- Implemented as fragment controllers (`AbstractContentElementController`)
- Registration via the `#[AsContentElement]` attribute
- DCA configuration in `tl_content` (palettes)
- Template: `content_element/<type>.html.twig`
- As of Contao 5.3: nested fragments (nested child elements)

---

## 4. Templating

Since version 4.12 Contao natively uses Symfony's **Twig template system**.
As of Contao 5 most content elements are exclusively Twig-based.
PHP templates (legacy) are still supported up to Contao 5 and will be dropped as of Contao 6.

**Core mechanism:** the managed namespace `@Contao` enables template inheritance without
the participating bundles knowing about each other. Several bundles can extend the same
template independently of one another.

---

## 5. Assets & Images

Contao supports responsive image processing via GD lib, Imagick and Gmagick.

Assets are included through global arrays (`$GLOBALS['TL_CSS']`, `$GLOBALS['TL_JAVASCRIPT']`)
or in the Twig template via `{% use %}` and the `add` tag.

---

## 6. Hooks

Hooks allow the modification of internal processes at defined execution points.

**Registration** via the PHP attribute `#[AsHook('hookName')]` — with autowiring
and autoconfigure enabled, a single PHP file is sufficient.

Example hooks: `parseArticles`, `updatePersonalData`, `loadDataContainer`,
`replaceInsertTags`, `generatePage`, `initializeFrontend`, etc.

---

## 7. Extensions (Bundles)

Extensions are Symfony bundles that integrate into Contao applications automatically
(via the Manager Plugin) or manually.

**Directory structure of a bundle:**
```
src/
├── ContaoExampleBundle.php       # Bundle class
├── ContaoManager/
│   └── Plugin.php                # Manager Plugin
├── Controller/                   # Controller classes
├── EventListener/                # Hook and event listeners
config/
├── services.yaml
└── routes.yaml
contao/
├── config/config.php
├── dca/
├── languages/
└── templates/
```

**composer.json:**
```json
{
    "type": "contao-bundle",
    "extra": {
        "contao-manager-plugin": "Vendor\\Bundle\\ContaoManager\\Plugin"
    }
}
```

---

## 8. Insert Tags

Insert tags are special tokens in the format `{{TAG_NAME}}` or `{{TAG_NAME::PARAMETER}}`
that are replaced with dynamic content before the front end delivery.

- Built in: `{{link::*}}`, `{{env::*}}`, `{{date::*}}`, `{{asset::*::*}}`, etc.
- Custom tags: `#[AsInsertTag('name')]` attribute
- Block tags: `#[AsBlockInsertTag('name', endTag: 'endname')]`
- Flags for output transformation: `#[AsInsertTagFlag('flag')]`

---

## Framework overview (further concepts)

Beyond that, the Contao framework contains:

| Area | Description |
|---------|-------------|
| Caching | HTTP caching integration |
| Cron | Contao cron functionality |
| Data Container Array | Complete DCA configuration |
| Filesystem | Working with files in Contao |
| Form Widgets | Custom input widgets |
| Image Processing | Image processing and responsive images |
| Models | ORM-like database abstraction |
| Page Controllers | Page types in the page structure |
| Routing | Custom routes and request attributes |
| Search Indexing | Search index integration |
| Security | Symfony Security integration |
| Translations | Translation system |

---

*Source: https://docs.contao.org/5.x/dev/getting-started/core-concepts/*  
*https://docs.contao.org/5.x/dev/framework/*
