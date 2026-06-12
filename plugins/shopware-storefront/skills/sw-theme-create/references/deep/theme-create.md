# Shopware 6 — Theme erstellen: Vollständige Referenz

Quelle: `guides/plugins/themes/create-a-theme.md`, `guides/plugins/themes/index.md`,
`guides/plugins/themes/theme-base-guide.md`

---

## Was ist ein Theme?

Ein Theme ist eine spezialisierte Art von Plugin (oder App), die ausschließlich das visuelle Erscheinungsbild
des Storefronts verändert. Im Gegensatz zu regulären Plugins enthält ein Theme **keine Backend-Logik**.

**Unterschiede Plugin vs. Theme:**

| Merkmal | Plugin/App | Theme |
|---|---|---|
| Backend-Logik | ja | nein |
| Aktivierung | global | per SalesChannel im Theme Manager |
| SCSS/JS | möglich | Kernfunktion |
| Twig-Templates | möglich | möglich |
| ThemeInterface | nein | **ja (Pflicht)** |

```text
Extensions
├── Plugin
│   └── kann Theme enthalten (nicht für Cloud)
└── App
    └── kann Theme enthalten (Cloud-ready)
```

---

## Schritt-für-Schritt: Theme erstellen

### 1. Naming-Konvention

**UpperCamelCase** mit Firmen-Prefix, z.B. `SwagBasicExampleTheme`.

### 2. Theme-Gerüst generieren

```bash
bin/console theme:create SwagBasicExampleTheme
```

Ausgabe:
```
Creating theme structure under .../development/custom/plugins/SwagBasicExampleTheme
```

### 3. Plugin-Liste aktualisieren

```bash
bin/console plugin:refresh
```

### 4. Theme installieren und aktivieren

```bash
bin/console plugin:install --activate SwagBasicExampleTheme
```

### 5. Theme einem SalesChannel zuweisen

```bash
bin/console theme:change
```

Interaktiver Prompt:
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

## Verzeichnisstruktur eines Theme-Plugins

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
    │   │       │               └── swag-basic-example-theme.js  # kompiliertes JS
    │   │       └── src
    │   │           ├── assets              # Bilder, Fonts, etc.
    │   │           ├── main.js             # JS-Einstiegspunkt
    │   │           └── scss
    │   │               ├── base.scss       # Haupt-SCSS
    │   │               └── overrides.scss  # Bootstrap/Variable-Overrides (vor @Storefront)
    │   └── theme.json                      # Kern-Konfigurationsdatei
    └── SwagBasicExampleTheme.php           # PHP-Klasse: implements ThemeInterface
```

---

## theme.json — Vollständiges Gerüst

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

**Felder:**
- `name` — Technischer Name (UpperCamelCase, identisch mit PHP-Klassenname)
- `author` — Autor-String
- `description` — Übersetzt (en-GB/de-DE); optional
- `previewMedia` — Pfad zum Vorschaubild (relativ zum Theme-Root)
- `views` — Twig-Template-Auflösungsreihenfolge
- `style` — SCSS/CSS-Kompilierungsreihenfolge; `overrides.scss` **muss vor** `@Storefront` stehen
- `script` — JS-Dateien (kompilierte dist-Versionen)
- `asset` — Pfade zu Asset-Ordnern (Bilder, Fonts, etc.)
- `configInheritance` — Welche Themes für Config-Felder geerbt werden
- `iconSets` — Custom Icon-Packs (ab Shopware 6.4.1.0)

---

## PHP-Klasse: ThemeInterface

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

1. Theme erstellen: `theme:create`
2. `theme.json` konfigurieren
3. SCSS/JS hinzufügen (`sw-theme-compile`)
4. Assets/Icons hinzufügen (`sw-theme-assets`)
5. Bootstrap-Variablen/Breakpoints überschreiben (`sw-theme-storefront-customization`)
6. Twig-Templates anpassen (`sw-twig-templates`)
7. Theme-Vererbung einrichten wenn nötig (`sw-theme-inheritance`, `sw-theme-multiple`)

---

## Troubleshooting

```bash
# Theme nicht sichtbar
bin/console plugin:refresh
bin/console plugin:list

# Theme nicht angewendet
bin/console theme:change
bin/console theme:compile

# Kein Update sichtbar
bin/console cache:clear
```

Weitere Hilfe: `var/log/`, Dateiberechtigungen in `custom/plugins/` prüfen.
