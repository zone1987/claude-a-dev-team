# Shopware 6 — Theme kompilieren & Build: Vollständige Referenz

Quellen: `guides/plugins/themes/styling/add-css-js-to-theme.md`,
`guides/plugins/themes/create-a-theme.md`,
`guides/plugins/themes/configuration/theme-configuration.md`

---

## Überblick: SCSS vs. JavaScript

| Sprache | Compiler | Befehl |
|---|---|---|
| SCSS/CSS | PHP SASS Compiler | `bin/console theme:compile` |
| JavaScript | Node.js / webpack | `shopware-cli project storefront-build` |

---

## SCSS kompilieren

SCSS wird von einem **PHP SASS Compiler** verarbeitet. Der Einstiegspunkt ist in `theme.json` definiert:

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

Dieser Befehl:
1. Liest die `style`-Einträge aus `theme.json`
2. Kompiliert SCSS in CSS
3. Kopiert Assets aus den `asset`-Pfaden nach `public/theme/<theme-asset-uuid>/`

---

## theme.json-Änderungen aktualisieren

Nach Änderungen an `theme.json` (neue Felder, Pfade, etc.):

```bash
bin/console theme:refresh
```

Aktualisiert die Config-Vererbungs-Beziehungen und liest neue Felder ein.

---

## JavaScript bauen

JavaScript kann **nicht** vom PHP-Compiler verarbeitet werden. Shopware verwendet
[webpack](https://webpack.js.org/). Code wird in ES6 geschrieben.

**Einstiegspunkt:** `src/Resources/app/storefront/src/main.js`

```bash
# Beispiel main.js
console.log('SwagBasicExampleTheme JS loaded');
```

**Build-Befehl** (shopware-cli):
```bash
shopware-cli project storefront-build
```

Ausgabedatei (automatisch erkannt von Shopware):
```
src/Resources/app/storefront/dist/storefront/js/swag-basic-example-theme/swag-basic-example-theme.js
```

Diese Datei muss in `theme.json` referenziert werden:
```json
{
  "script": [
    "@Storefront",
    "app/storefront/dist/storefront/js/swag-basic-example-theme/swag-basic-example-theme.js"
  ]
}
```

---

## Dev-Server mit Live-Reload

Für effizientes Entwickeln: Dev-Server auf Port `9998` mit automatischem Reload.

```bash
# shopware-cli (Template / Standard)
shopware-cli project storefront-watch

# Contribution/Platform-Setup, ab Shopware 6.7.11.0
composer run storefront:dev-server

# Vor Shopware 6.7.11.0 (platform only)
composer run watch:storefront
```

Storefront unter `localhost:9998` öffnen — Seite aktualisiert sich bei Dateiänderungen automatisch.

> **Hinweis:** Beim Verwenden von `storefront-watch` werden SCSS-Variablen dynamisch von webpack
> injiziert. Selektoren und Properties in `overrides.scss` können daher **mehrfach** im kompilierten
> CSS erscheinen. Nur Variablen-Overrides gehören in `overrides.scss`.

---

## Workflow: Vollständiger Build-Zyklus

```bash
# 1. JS bauen (bei JS-Änderungen)
shopware-cli project storefront-build

# 2. Theme kompilieren (SCSS + Assets)
bin/console theme:compile

# 3. Cache leeren
bin/console cache:clear
```

Oder für theme.json-Änderungen:
```bash
bin/console theme:refresh
bin/console theme:compile
bin/console cache:clear
```

---

## Atomic Theme Compilation

Shopware kompiliert Themes **atomar** — jeder SalesChannel bekommt eine eigene Theme-Version.
Das ermöglicht, dass verschiedene SalesChannels unterschiedliche Themes oder Theme-Konfigurationen
verwenden können, ohne sich gegenseitig zu beeinflussen.

Kompilierte Themes landen in:
```
public/theme/<theme-uuid>/
├── css/all.css
└── js/all.js
```

Assets (Bilder, Fonts):
```
public/theme/<theme-asset-uuid>/asset/
```

---

## Schnellreferenz: Alle Theme-CLI-Befehle

```bash
bin/console theme:create <ThemeName>      # Neues Theme-Gerüst erstellen
bin/console theme:install <ThemeName>     # Theme installieren
bin/console theme:change                  # Theme einem SalesChannel zuweisen (interaktiv)
bin/console theme:compile                 # SCSS kompilieren + Assets kopieren
bin/console theme:refresh                 # theme.json neu einlesen (nach Änderungen)
bin/console theme:dump                    # Theme-Konfiguration ausgeben (Debugging)
bin/console theme:list                    # Alle Themes auflisten
```
