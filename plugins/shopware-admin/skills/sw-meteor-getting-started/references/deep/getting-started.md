# Meteor Design System — Installation & Getting Started

Quelle: `packages/component-library/README.md`, `packages/component-library/src/docs/getting-started/`,
`packages/create-meteor-extension/readme.md`, `packages/component-library/src/docs/getting-started/migration.mdx`

## Überblick

Meteor ist Shopwares Open-Source-Design-System und wird als drei unabhängige npm-Pakete veröffentlicht:

| Paket | Beschreibung |
|---|---|
| `@shopware-ag/meteor-component-library` | Vue 3 Komponentensatz mit integrierten Tokens, Icons und Inter-Font |
| `@shopware-ag/meteor-tokens` | Design Tokens als CSS Custom Properties, framework-agnostisch |
| `@shopware-ag/meteor-icon-kit` | SVG-Iconset, nutzbar standalone oder als Vue-Komponenten via `mt-icon` |

Die drei Pakete können zusammen oder einzeln installiert werden.

---

## 1. Komponentenbibliothek installieren

### Voraussetzungen

- Vue 3 Anwendung
- `vue-i18n` Plugin (für Übersetzungen)

### Installation

```sh
npm install @shopware-ag/meteor-component-library @shopware-ag/meteor-icon-kit
```

### CSS-Importe

Beide Imports in den Anwendungs-Entry-Point eintragen:

```ts
import "@shopware-ag/meteor-component-library/styles.css";
import "@shopware-ag/meteor-component-library/font.css";
```

`styles.css` enthält allgemeine Komponentenstyles. `font.css` lädt die Inter-Schriftart.

### i18n konfigurieren

Englisch und Deutsch sind gebündelt. `vue-i18n` muss vor dem App-Mount registriert werden:

```ts
import { createApp } from "vue";
import { createI18n } from "vue-i18n";
import App from "./App.vue";

const i18n = createI18n({ legacy: false });

createApp(App).use(i18n).mount("#app");
```

### TypeScript

Komponenten sind vollständig in TypeScript gebaut. Keine zusätzliche Konfiguration nötig. Typen werden automatisch aufgelöst beim Import von `@shopware-ag/meteor-component-library`.

### Komponenten verwenden (tree-shakable)

Nur was importiert wird, landet im Bundle:

```vue
<script setup>
import { MtButton, MtBanner } from "@shopware-ag/meteor-component-library";
</script>

<template>
  <MtButton variant="primary">Save</MtButton>
  <MtBanner variant="success">Saved successfully.</MtBanner>
</template>
```

Jede Komponente kann auch direkt aus dem Root importiert werden:

```html
<script>
import { MtButton } from "@shopware-ag/meteor-component-library";

export default {
  components: {
    "mt-button": MtButton,
  },
};
</script>
```

---

## 2. Tokens standalone installieren

Das Token-Paket ist framework-agnostisch und kann unabhängig installiert werden:

```sh
npm install @shopware-ag/meteor-tokens
```

### Import

```ts
import "@shopware-ag/meteor-tokens/administration/light.css";
// Optional für Dark Mode:
import "@shopware-ag/meteor-tokens/administration/dark.css";
```

Das Light-Theme setzt Tokens auf `:root`. Das Dark-Theme wird bei `data-theme="dark"` auf einem DOM-Element aktiv:

```html
<body data-theme="dark">
  <!-- Anwendung -->
</body>
```

### Verwendung

```css
.my-component {
  color: var(--color-text-primary-default);
  background: var(--color-elevation-surface-default);
  padding: var(--scale-size-16);
}
```

---

## 3. Icon Kit installieren

```sh
npm install @shopware-ag/meteor-icon-kit
```

### Als SVG importieren

```ts
import PlusIcon from "@shopware-ag/meteor-icon-kit/icons/regular/plus.svg";
```

### Mit mt-icon (Vue)

`mt-icon` ist in der Komponentenbibliothek enthalten und rendert beliebige Icons per Name:

```html
<mt-icon name="regular-plus" />
<mt-icon name="solid-checkmark" size="20px" />
```

### SCSS/CSS einbinden

```scss
@import "@shopware-ag/meteor-icon-kit/icons/meteor-icon-kit.scss";
```

oder klassisch via CSS:

```html
<link rel="stylesheet" href="your-asset-folder/meteor-icon-kit.css" />
```

### Dynamische Farben (SVG direkt)

```css
.icon-example {
  display: block;
  color: green;

  svg {
    fill: currentColor;

    path,
    use {
      fill: currentColor;
    }
  }
}
```

### Vite-Beispiel (vite-svg-loader)

```js
// vite.config.js
import svgLoader from "vite-svg-loader";

export default {
  plugins: [svgLoader()],
};
```

```vue
<template>
  <ActivityIcon />
</template>

<script setup>
import ActivityIcon from "@shopware-ag/meteor-icon-kit/icons/regular/activity.svg";
</script>
```

---

## 4. Shopware Extension scaffolden (create-meteor-extension)

Für neue Shopware Admin Extensions gibt es ein CLI-Tool:

```bash
# Empfohlen: immer aktuelle Version
npx @shopware-ag/create-meteor-extension

# Oder global installieren
npm install -g @shopware-ag/create-meteor-extension
create-meteor-extension
```

Das CLI fragt interaktiv nach:
- **Extension name**: nur Kleinbuchstaben, Zahlen und Bindestriche (z.B. `my-awesome-extension`)

**Hinweis**: Das CLI erstellt immer einen Ordner `meteor-app` (wie von Shopware 6.7+ Plugin-Struktur gefordert). Der angegebene Name wird in `package.json`, README und Konfigurationsdateien verwendet.

### Non-Interactive Mode (CI/CD)

```bash
npx @shopware-ag/create-meteor-extension --name my-extension --output-dir meteor-app
```

**Optionen:**
- `--name`: Extension-Name (erforderlich im Non-Interactive Mode)
- `--output-dir`: Ausgabe-Verzeichnisname (optional, Standard: `meteor-app`)

### Generierte Struktur

```
meteor-app/
├── src/
│   ├── locations/           # Vue-Komponenten für Admin-Locations
│   │   ├── exampleDashboard.vue
│   │   └── exampleProductTab.vue
│   ├── assets/              # Styles und statische Assets
│   ├── app.ts               # Anwendungs-Einstiegspunkt
│   ├── bootstrap.ts         # SDK-Initialisierung
│   ├── locations.ts         # Location-Konfiguration
│   └── main.ts              # Haupt-Einstiegspunkt
├── snippet/                 # Übersetzungsdateien
│   ├── de-DE.json
│   └── en-GB.json
├── public/                  # Statische Assets
├── package.json
├── vite.config.ts
├── tsconfig.json
└── eslint.config.ts
```

Für Shopware 6.7+ Plugins gehört dies nach:
`custom/plugins/yourPlugin/src/Resources/app/meteor-app`

### Wichtigste Dependencies des Scaffolds

| Package | Zweck |
|---|---|
| `@shopware-ag/meteor-admin-sdk` | Core SDK für Admin-Extensions |
| `@shopware-ag/meteor-component-library` | UI-Komponentenbibliothek |
| Vue 3 + Vue Router | Framework |
| Vite | Build-Tool |

### Verfügbare Example Locations im Template

1. **Dashboard Card** (`example-dashboard-before-content`): Erscheint auf dem Shopware-Dashboard
2. **Product Tab** (`example-product-tab`): Fügt einen Tab zur Produktdetailseite hinzu

### Nach dem Scaffolding

```bash
cd meteor-app
npm install
# Extension in Shopware installieren und aktivieren
```

**Verfügbare Scripts:**
- `npm run type-check` — TypeScript-Compiler-Check
- `npm run lint` — Linting und Autofixing mit ESLint
- `npm run format` — Code-Formatierung mit Prettier

---

## 5. Migration von sw-* auf mt-* (Meteor)

### Komponent-Mapping

| Alte sw-* Komponente | Neue mt-* Komponente |
|---|---|
| `sw-button` | `mt-button` |
| `sw-text-field` | `mt-text-field` |
| `sw-card` | `mt-card` |
| `sw-banner` | `mt-banner` |
| `sw-checkbox` | `mt-checkbox` |
| `sw-switch-field` | `mt-switch` |
| `sw-select` | `mt-select` |
| `sw-datepicker` | `mt-datepicker` |
| `sw-icon` | `mt-icon` |

### Design Tokens migrieren

Hardcodierte CSS-Werte durch Meteor-Tokens ersetzen:

```css
/* Vorher */
color: #1a1a1a;

/* Nachher */
color: var(--color-text-primary-default);
```

### admin-extension-sdk → meteor-admin-sdk

Das Paket `@shopware-ag/admin-extension-sdk` wurde im März 2024 archiviert und durch `@shopware-ag/meteor-admin-sdk` ersetzt:

```sh
npm uninstall @shopware-ag/admin-extension-sdk
npm install @shopware-ag/meteor-admin-sdk
```

Imports anpassen:

```js
// Vorher
import { notification } from "@shopware-ag/admin-extension-sdk";

// Nachher
import { notification } from "@shopware-ag/meteor-admin-sdk";
```

### Schrittweise Migration

Meteor funktioniert parallel zu bestehenden Komponenten. Seitenweise migrieren:

1. Meteor neben der bestehenden Konfiguration installieren
2. Komponenten einzeln ersetzen
3. Styling schrittweise auf Design Tokens umstellen
4. Jeden Schritt testen vor dem nächsten

---

## 6. Browser-Support

Meteor zielt auf alle modernen Evergreen-Browser ab. Genutzte Features sind auf den [Baseline Widely Available](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility) Standard beschränkt — unterstützt in den aktuellen stabilen Releases von Chrome, Edge, Firefox und Safari, ohne Polyfills.

Legacy-Browser und Nicht-Evergreen-Umgebungen werden nicht unterstützt.

---

## 7. Stylelint Plugin für Meteor

Das Stylelint-Plugin erzwingt die Verwendung von Meteor-Tokens in CSS:

```sh
npm i -D @shopware-ag/stylelint-plugin-meteor
```

```json
{
  "plugins": ["@shopware-ag/stylelint-plugin-meteor"],
  "rules": {
    "meteor/prefer-sizing-token": [true, { "severity": "warning" }]
  }
}
```

**Verfügbare Regeln:**

| Regel | Beschreibung |
|---|---|
| `meteor/no-primitive-token` | Verbietet primitive Tokens (z.B. `--gray-800`); nur semantische Tokens erlaubt |
| `meteor/prefer-background-token` | Nur semantische Tokens für Hintergrundfarben |
| `meteor/prefer-border-token` | Nur Border-Tokens für Border-Farben |
| `meteor/prefer-color-token` | Nur Color-Tokens für `color`-Properties |
| `meteor/prefer-font-token` | Nur Font-Tokens für Typografie-Properties |
| `meteor/prefer-sizing-token` | Nur Sizing-Tokens für Spacing (margin, padding, gap, …) |

**Beispiel prefer-sizing-token:**

```css
/* Falsch */
a { margin: 10px; }

/* Richtig */
a { margin: var(--scale-size-10); }
```

**Beispiel no-primitive-token:**

```css
/* Falsch */
a { color: var(--gray-800); }

/* Richtig */
a { color: var(--color-text-primary-default); }
```

---

## 8. Prettier Config

Das Prettier-Konfigurationspaket kann für konsistente Code-Formatierung genutzt werden:

```sh
npm install --save-dev @shopware-ag/prettier-config
```

---

## Weiterführende Dokumentation

- Alle mt-*-Komponenten (Props/Events/Slots): Skill `sw-meteor-components` → `references/deep/components.md`
- Design Tokens vollständig: Skill `sw-meteor-components` → `references/deep/tokens.md`; erweitert in `sw-meteor-design-tokens`
- Composables & Direktiven: Skill `sw-meteor-composables`
- Admin SDK Komplettdoku: Skill `sw-meteor-admin-sdk`
- Nutzungsrichtlinien & Accessibility: Skill `sw-meteor-usage-guidelines`
