# Shopware 6 — Creating a theme: complete reference

Source: `guides/plugins/themes/create-a-theme.md`, `guides/plugins/themes/index.md`,
`guides/plugins/themes/theme-base-guide.md`

---

## Contents

- [What is a theme?](#what-is-a-theme)
- [Step by step: creating a theme](#step-by-step-creating-a-theme)
- [Directory structure of a theme plugin](#directory-structure-of-a-theme-plugin)
- [theme.json — complete scaffold](#themejson--complete-scaffold)
- [PHP class: ThemeInterface](#php-class-themeinterface)
- [Developer Workflow (theme-base-guide)](#developer-workflow-theme-base-guide)
- [Troubleshooting](#troubleshooting)

## What is a theme?

A theme is a specialized kind of plugin (or app) that changes only the visual appearance
of the storefront. Unlike regular plugins, a theme contains **no backend logic**.

**Differences plugin vs. theme:**

| Feature | Plugin/App | Theme |
|---|---|---|
| Backend logic | yes | no |
| Activation | global | per sales channel in the Theme Manager |
| SCSS/JS | possible | core function |
| Twig templates | possible | possible |
| ThemeInterface | no | **yes (mandatory)** |

```text
Extensions
├── Plugin
│   └── can contain a theme (not for Cloud)
└── App
    └── can contain a theme (Cloud-ready)
```

---

## Step by step: creating a theme

### 1. Naming convention

**UpperCamelCase** with a company prefix, e.g. `SwagBasicExampleTheme`.

### 2. Generate the theme scaffold

```bash
bin/console theme:create SwagBasicExampleTheme
```

Output:
```
Creating theme structure under .../development/custom/plugins/SwagBasicExampleTheme
```

### 3. Refresh the plugin list

```bash
bin/console plugin:refresh
```

### 4. Install and activate the theme

```bash
bin/console plugin:install --activate SwagBasicExampleTheme
```

### 5. Assign the theme to a sales channel

```bash
bin/console theme:change
```

Interactive prompt:
```
Please select a sales channel:
[0] Storefront | 64bbbe810d824c339a6c191779b2c205
> 0

Please select a theme:
[0] Storefront
[1] SwagBasicExampleTheme
> 1

Set "SwagBasicExampleTheme" as new theme for sales channel "Storefront"
Compiling theme 13e0a4a46af547479b1347617926995b for sales channel SwagBasicExampleTheme
```

---

## Directory structure of a theme plugin

```bash
SwagBasicExampleTheme/
├── composer.json
└── src
    ├── Resources
    │   ├── app
    │   │   └── storefront
    │   │       ├── dist
    │   │       │   └── storefront
    │   │       │       └── js
    │   │       │           └── swag-basic-example-theme
    │   │       │               └── swag-basic-example-theme.js  # compiled JS
    │   │       └── src
    │   │           ├── assets              # images, fonts, etc.
    │   │           ├── main.js             # JS entry point
    │   │           └── scss
    │   │               ├── base.scss       # main SCSS
    │   │               └── overrides.scss  # Bootstrap/variable overrides (before @Storefront)
    │   └── theme.json                      # core configuration file
    └── SwagBasicExampleTheme.php           # PHP class: implements ThemeInterface
```

---

## theme.json — complete scaffold

```json
{
  "name": "SwagBasicExampleTheme",
  "author": "Shopware AG",
  "description": {
    "en-GB": "My custom theme",
    "de-DE": "Mein custom Theme"
  },
  "previewMedia": "app/storefront/dist/assets/defaultThemePreview.jpg",
  "views": [
    "@Storefront",
    "@Plugins",
    "@SwagBasicExampleTheme"
  ],
  "style": [
    "app/storefront/src/scss/overrides.scss",
    "@Storefront",
    "app/storefront/src/scss/base.scss"
  ],
  "script": [
    "@Storefront",
    "app/storefront/dist/storefront/js/swag-basic-example-theme/swag-basic-example-theme.js"
  ],
  "asset": [
    "@Storefront",
    "app/storefront/src/assets"
  ],
  "configInheritance": [
    "@Storefront"
  ]
}
```

**Fields:**
- `name` — technical name (UpperCamelCase, identical to the PHP class name)
- `author` — author string
- `description` — translated (en-GB/de-DE); optional
- `previewMedia` — path to the preview image (relative to the theme root)
- `views` — Twig template resolution order
- `style` — SCSS/CSS compilation order; `overrides.scss` **must come before** `@Storefront`
- `script` — JS files (compiled dist versions)
- `asset` — paths to asset folders (images, fonts, etc.)
- `configInheritance` — which themes are inherited for config fields
- `iconSets` — custom icon packs (as of Shopware 6.4.1.0)

---

## PHP class: ThemeInterface

```php
<?php declare(strict_types=1);

namespace SwagBasicExampleTheme;

use Shopware\Core\Framework\Plugin;
use Shopware\Storefront\Framework\ThemeInterface;

class SwagBasicExampleTheme extends Plugin implements ThemeInterface
{
    public function getThemeConfigPath(): string
    {
        return 'theme.json';
    }
}
```

---

## Developer Workflow (theme-base-guide)

1. Create the theme: `theme:create`
2. Configure `theme.json`
3. Add SCSS/JS (`sw-theme-compile`)
4. Add assets/icons (`sw-theme-assets`)
5. Override Bootstrap variables/breakpoints (`sw-theme-storefront-customization`)
6. Adjust Twig templates (`sw-twig-templates`)
7. Set up theme inheritance if needed (`sw-theme-inheritance`, `sw-theme-multiple`)

---

## Troubleshooting

```bash
# Theme not visible
bin/console plugin:refresh
bin/console plugin:list

# Theme not applied
bin/console theme:change
bin/console theme:compile

# No update visible
bin/console cache:clear
```

Further help: check `var/log/` and the file permissions in `custom/plugins/`.
