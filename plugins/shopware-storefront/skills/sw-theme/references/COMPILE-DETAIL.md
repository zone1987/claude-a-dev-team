# Shopware 6 — Compiling a theme & build: complete reference

Sources: `guides/plugins/themes/styling/add-css-js-to-theme.md`,
`guides/plugins/themes/create-a-theme.md`,
`guides/plugins/themes/configuration/theme-configuration.md`

---

## Contents

- [Overview: SCSS vs. JavaScript](#overview-scss-vs-javascript)
- [Compiling SCSS](#compiling-scss)
- [Applying theme.json changes](#applying-themejson-changes)
- [Building JavaScript](#building-javascript)
- [Dev server with live reload](#dev-server-with-live-reload)
- [Workflow: complete build cycle](#workflow-complete-build-cycle)
- [Atomic Theme Compilation](#atomic-theme-compilation)
- [Quick reference: all theme CLI commands](#quick-reference-all-theme-cli-commands)

## Overview: SCSS vs. JavaScript

| Language | Compiler | Command |
|---|---|---|
| SCSS/CSS | PHP SASS Compiler | `bin/console theme:compile` |
| JavaScript | Node.js / webpack | `shopware-cli project storefront-build` |

---

## Compiling SCSS

SCSS is processed by a **PHP SASS Compiler**. The entry point is defined in `theme.json`:

```json
{
  "style": [
    "app/storefront/src/scss/overrides.scss",
    "@Storefront",
    "app/storefront/src/scss/base.scss"
  ]
}
```

```bash
bin/console theme:compile
```

This command:
1. Reads the `style` entries from `theme.json`
2. Compiles SCSS into CSS
3. Copies assets from the `asset` paths to `public/theme/<theme-asset-uuid>/`

---

## Applying theme.json changes

After changes to `theme.json` (new fields, paths, etc.):

```bash
bin/console theme:refresh
```

Updates the config inheritance relationships and reads in new fields.

---

## Building JavaScript

JavaScript **cannot** be processed by the PHP compiler. Shopware uses
[webpack](https://webpack.js.org/). Code is written in ES6.

**Entry point:** `src/Resources/app/storefront/src/main.js`

```bash
# Example main.js
console.log('SwagBasicExampleTheme JS loaded');
```

**Build command** (shopware-cli):
```bash
shopware-cli project storefront-build
```

Output file (detected automatically by Shopware):
```
src/Resources/app/storefront/dist/storefront/js/swag-basic-example-theme/swag-basic-example-theme.js
```

This file must be referenced in `theme.json`:
```json
{
  "script": [
    "@Storefront",
    "app/storefront/dist/storefront/js/swag-basic-example-theme/swag-basic-example-theme.js"
  ]
}
```

---

## Dev server with live reload

For efficient development: dev server on port `9998` with automatic reload.

```bash
# shopware-cli (template / standard)
shopware-cli project storefront-watch

# Contribution/platform setup, as of Shopware 6.7.11.0
composer run storefront:dev-server

# Before Shopware 6.7.11.0 (platform only)
composer run watch:storefront
```

Open the storefront at `localhost:9998` — the page refreshes automatically on file changes.

> **Note:** When using `storefront-watch`, SCSS variables are injected dynamically by webpack.
> Selectors and properties in `overrides.scss` can therefore appear **multiple times** in the
> compiled CSS. Only variable overrides belong in `overrides.scss`.

---

## Workflow: complete build cycle

```bash
# 1. Build JS (on JS changes)
shopware-cli project storefront-build

# 2. Compile the theme (SCSS + assets)
bin/console theme:compile

# 3. Clear the cache
bin/console cache:clear
```

Or for theme.json changes:
```bash
bin/console theme:refresh
bin/console theme:compile
bin/console cache:clear
```

---

## Atomic Theme Compilation

Shopware compiles themes **atomically** — each sales channel gets its own theme version.
This makes it possible for different sales channels to use different themes or theme
configurations without affecting each other.

Compiled themes end up in:
```
public/theme/<theme-uuid>/
├── css/all.css
└── js/all.js
```

Assets (images, fonts):
```
public/theme/<theme-asset-uuid>/asset/
```

---

## Quick reference: all theme CLI commands

```bash
bin/console theme:create <ThemeName>      # Create a new theme scaffold
bin/console theme:install <ThemeName>     # Install a theme
bin/console theme:change                  # Assign a theme to a sales channel (interactive)
bin/console theme:compile                 # Compile SCSS + copy assets
bin/console theme:refresh                 # Re-read theme.json (after changes)
bin/console theme:dump                    # Output the theme configuration (debugging)
bin/console theme:list                    # List all themes
```
