# Shopware 6 — Storefront-Customization im Theme: Vollständige Referenz

Quellen: `guides/plugins/themes/styling/add-css-js-to-theme.md`,
`guides/plugins/themes/styling/override-bootstrap-variables-in-a-theme.md`,
`guides/plugins/themes/styling/override-theme-breakpoints.md`,
`guides/plugins/themes/inheritance/add-theme-inheritance-without-resources.md`

---

## SCSS in ein Theme einbinden

Der PHP SASS Compiler verarbeitet SCSS. Einstiegspunkte sind in `theme.json` definiert:

```json
{
  "style": [
    "app/storefront/src/scss/overrides.scss",
    "@Storefront",
    "app/storefront/src/scss/base.scss"
  ]
}
```

**Reihenfolge ist entscheidend:**
1. `overrides.scss` — **vor** `@Storefront` für Variable-Overrides
2. `@Storefront` — das Default-Shopware-Theme
3. `base.scss` — eigenes SCSS (nach Storefront → kann Klassen überschreiben)

### base.scss — Eigenes CSS/SCSS

```
src/Resources/app/storefront/src/scss/base.scss
```

Beispiel:
```scss
body {
    background-color: blue;
}

.custom-header {
    font-size: 2rem;
    color: $sw-color-brand-primary; // Theme-Variable verwenden
}
```

Nach Änderungen: `bin/console theme:compile`

---

## Bootstrap-Variablen überschreiben

Bootstrap 4/5 verwendet `!default` für Variablen. Overrides müssen **vor** dem Import deklariert werden.

Der `overrides.scss`-Einstiegspunkt in `theme.json` steht bewusst **vor** `@Storefront`:

```json
"style": [
    "app/storefront/src/scss/overrides.scss",  ← HIER: vor @Storefront
    "@Storefront",
    "app/storefront/src/scss/base.scss"
]
```

### overrides.scss

```scss
// src/Resources/app/storefront/src/scss/overrides.scss
/*
Override variable defaults
==================================================
This file is used to override default SCSS variables from the Shopware Storefront or Bootstrap.
Because of the !default flags, theme variable overrides have to be declared beforehand.
https://getbootstrap.com/docs/4.0/getting-started/theming/#variable-defaults
*/

$border-radius: 0;

// Weitere Override-Beispiele
$icon-base-color: #f00;
$modal-backdrop-bg: rgba(255, 0, 0, 0.5);
$disabled-btn-bg: #f00;
$disabled-btn-border-color: #fc8;
$font-weight-semibold: 300;
```

> **Wichtig:** **Nur** Variablen-Overrides in `overrides.scss`. Kein CSS wie `.container { background: #f00 }`.
> Beim Watch-Mode (`storefront-watch`) werden Variablen dynamisch injiziert — CSS-Selektoren
> in `overrides.scss` können mehrfach im Build erscheinen.

---

## Responsive Breakpoints anpassen

Seit Shopware **6.7.8.0** gibt es sechs Theme-Config-Felder für Breakpoints.
Diese sind im Admin **versteckt** (nur Entwickler-Feature).

### In theme.json definieren

```json
{
  "name": "My custom theme",
  "config": {
    "fields": {
      "sw-breakpoint-xs": { "value": 0 },
      "sw-breakpoint-sm": { "value": 576 },
      "sw-breakpoint-md": { "value": 768 },
      "sw-breakpoint-lg": { "value": 992 },
      "sw-breakpoint-xl": { "value": 1200 },
      "sw-breakpoint-xxl": { "value": 1400 }
    }
  }
}
```

Diese Werte werden automatisch in **Twig** und **JavaScript** verfügbar gemacht.

### Bootstrap-Breakpoints in SCSS synchronisieren

Da Shopware Bootstrap-Defaults in CSS verwendet, müssen SCSS-Breakpoints separat überschrieben werden.
Die Theme-Config-Werte stehen in SCSS als Variablen zur Verfügung:

```scss
// src/Resources/app/storefront/src/scss/overrides.scss
$grid-breakpoints: (
    xs: $sw-breakpoint-xs,
    sm: $sw-breakpoint-sm,
    md: $sw-breakpoint-md,
    lg: $sw-breakpoint-lg,
    xl: $sw-breakpoint-xl,
    xxl: $sw-breakpoint-xxl
);
```

**Single Source of Truth:** Breakpoints nur in `theme.json` definieren, in SCSS darauf referenzieren.

---

## JavaScript in ein Theme einbinden

JavaScript wird mit **webpack** (via shopware-cli) kompiliert.

### Einstiegspunkt

```
src/Resources/app/storefront/src/main.js
```

```javascript
// main.js
console.log('SwagBasicExampleTheme JS loaded');
```

### Kompilieren

```bash
shopware-cli project storefront-build
```

Ausgabe: `src/Resources/app/storefront/dist/storefront/js/swag-basic-example-theme/swag-basic-example-theme.js`

### In theme.json referenzieren

```json
{
  "script": [
    "@Storefront",
    "app/storefront/dist/storefront/js/swag-basic-example-theme/swag-basic-example-theme.js"
  ]
}
```

---

## Theme ohne Shopware-Skin (nur Bootstrap)

Wenn das Theme **ausschließlich** auf Bootstrap aufbauen soll (ohne das Shopware-Storefront-Skin):

```json
{
  "style": [
    "@StorefrontBootstrap",
    "@Plugins",
    "app/storefront/src/scss/base.scss"
  ]
}
```

**Wichtige Einschränkungen für `@StorefrontBootstrap`:**
- Nur in der `style`-Sektion verwendbar — **nicht** in `views` oder `script`
- Alle Theme-Variablen (`$sw-color-brand-primary` etc.) sind weiterhin verfügbar
- `@Storefront` und `@StorefrontBootstrap` **dürfen nicht gleichzeitig** verwendet werden
- `@StorefrontBootstrap` enthält **kein** `@Plugins` — muss explizit hinzugefügt werden
- Das gesamte SCSS aus `src/Storefront/Resources/app/storefront/src/scss/skin` entfällt

**Anwendungsfall:** Vollständig eigenes Design ohne Shopware-Storefront-Styling als Basis.

---

## Namespace-Referenzen in theme.json

Einzelne Dateien aus anderen Themes/Namespaces importieren:

```json
{
  "style": [
    "app/storefront/src/scss/overrides.scss",
    "@Storefront",
    "@BasicTheme/app/storefront/src/scss/custom.scss",
    "app/storefront/src/scss/base.scss"
  ],
  "script": [
    "@Storefront",
    "@Plugins",
    "@BasicTheme/app/storefront/dist/storefront/custom-plugin.js",
    "app/storefront/dist/storefront/js/my-theme/my-theme.js"
  ]
}
```

---

## Schnellreferenz: SCSS-Variablen von Shopware

Shopware injiziert alle `config.fields`-Einträge automatisch als SCSS-Variablen:

```scss
// Aus theme.json config.fields automatisch verfügbar:
color: $sw-color-brand-primary;      // Primärfarbe
background: $sw-color-brand-secondary;
border-radius: $sw-border-radius;
font-family: $sw-font-family-base;

// Breakpoints (ab 6.7.8.0):
@media (min-width: $sw-breakpoint-lg) { ... }
```
