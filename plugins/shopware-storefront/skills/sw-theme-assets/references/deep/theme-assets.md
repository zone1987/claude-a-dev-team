# Shopware 6 — Theme Assets & Icons: Vollständige Referenz

Quellen: `guides/plugins/themes/assets/add-assets-to-theme.md`,
`guides/plugins/themes/assets/add-icons.md`

---

## Assets in einem Theme einbinden

Es gibt zwei Methoden:

### Methode 1: theme.json (empfohlen für Themes)

In `theme.json` den Asset-Pfad konfigurieren:

```json
{
  "asset": [
    "app/storefront/src/assets"
  ]
}
```

Mit dem Storefront-Default-Theme:
```json
{
  "asset": [
    "@Storefront",
    "app/storefront/src/assets"
  ]
}
```

**Wie es funktioniert:** Der Befehl `bin/console theme:compile` kopiert alle Assets aus dem
konfigurierten Pfad nach `<shopware-root>/public/theme/<theme-asset-uuid>/asset/`.

```text
public/
└── theme/
    ├── <theme-uuid>/
    │   ├── css/
    │   │   └── all.css
    │   └── js/
    │       └── all.js
    └── <theme-asset-uuid>/
        └── asset/
            └── your-image.png   ← hierhin wird kopiert
```

### Methode 2: Plugin-Weg (Standard-Assets)

Funktioniert wie normale Plugin-Assets über `<plugin>/src/Resources/public/`.
Details: `guides/plugins/storefront/styling/add-custom-assets.md`

---

## Assets verlinken

### In Twig-Templates

```twig
<img src="{{ asset('/assets/your-image.png', 'theme') }}">
```

Der zweite Parameter `'theme'` gibt den Asset-Package-Namen an.

### In SCSS

```scss
body {
    background-image: url('#{$app-css-relative-asset-path}/your-image.png');
}
```

Die SCSS-Variable `$app-css-relative-asset-path` wird automatisch von Shopware gesetzt und
zeigt auf das Theme-Asset-Verzeichnis.

---

## Custom Icons

### Standard-Icon-System

Shopware nutzt SVG-Icons. Standard-Icons liegen in:
```
<shopware-root>/src/Storefront/Resources/app/storefront/dist/assets/icon/
├── default/    ← Standard-Pack
└── solid/      ← Solid-Pack
```

### Icon im Twig verwenden

```twig
{% sw_icon 'done-outline-24px' style {
    'size': 'lg',
    'namespace': 'TestPlugin',
    'pack': 'solid'
} %}
```

**`sw_icon` Konfigurations-Parameter:**

| Parameter | Beschreibung |
|---|---|
| `size` | Größe des Icons |
| `namespace` | Plugin/Theme-Name, in dem das Icon gesucht wird — **wichtig für Custom Icons** |
| `pack` | Icon-Pack-Name (default: `default`) |
| `color` | Farbe (Bootstrap-Varianten oder beliebige CSS-Farbe) |
| `class` | Zusätzliche CSS-Klasse |

> **Achtung:** Ohne `namespace`-Konfiguration zeigt Shopware die Standard-Storefront-Icons.

### Eigene Icons ablegen (klassisch)

Icons im Plugin/Theme unter:
```
<YourPlugin>/src/Resources/app/storefront/dist/assets/icon/default/
```

Für eigene Icon-Packs einen Ordner mit dem Pack-Namen erstellen:
```
<YourPlugin>/src/Resources/app/storefront/dist/assets/icon/<pack-name>/
```

> **Achtung:** Icons sind **nicht** Teil der Theme-Vererbung. Custom Icons müssen im eigenen
> Theme-Namespace abgelegt und explizit per `namespace` referenziert werden.

### iconSets in theme.json (ab Shopware 6.4.1.0) — PFLICHT für Apps

Für App-Themes und als bevorzugte Methode:

```json
{
  "iconSets": {
    "custom-icons": "app/storefront/src/assets/icon-pack/custom-icons"
  }
}
```

Verwendung im Twig:
```twig
{% sw_icon 'done-outline-24px' style {
    'pack': 'custom-icons'
} %}
```

> **Hinweis:** Für App-Themes ist `iconSets` **Pflicht**, da Icons sonst nicht geladen werden können.

---

## Schnellreferenz: Pfade

| Zweck | Pfad |
|---|---|
| Assets im Theme | `src/Resources/app/storefront/src/assets/` |
| Default-Icons | `dist/assets/icon/default/` |
| Custom Icon-Pack | `dist/assets/icon/<pack-name>/` |
| Compiled Assets (public) | `public/theme/<theme-asset-uuid>/asset/` |
