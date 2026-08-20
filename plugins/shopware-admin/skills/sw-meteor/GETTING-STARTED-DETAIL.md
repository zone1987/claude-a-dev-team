# Meteor design system — installation & getting started

Source: `packages/component-library/README.md`, `packages/component-library/src/docs/getting-started/`,
`packages/create-meteor-extension/readme.md`, `packages/component-library/src/docs/getting-started/migration.mdx`

## Contents

- [Overview](#overview)
- [1. Installing the component library](#1-installing-the-component-library)
- [2. Installing the tokens standalone](#2-installing-the-tokens-standalone)
- [3. Installing the icon kit](#3-installing-the-icon-kit)
- [4. Scaffolding a Shopware extension (create-meteor-extension)](#4-scaffolding-a-shopware-extension-create-meteor-extension)
- [5. Migrating from sw-* to mt-* (Meteor)](#5-migrating-from-sw--to-mt--meteor)
- [6. Browser support](#6-browser-support)
- [7. Stylelint plugin for Meteor](#7-stylelint-plugin-for-meteor)
- [8. Prettier config](#8-prettier-config)
- [Further documentation](#further-documentation)

## Overview

Meteor is Shopware's open source design system and is published as three independent npm packages:

| Package | Description |
|---|---|
| `@shopware-ag/meteor-component-library` | Vue 3 component set with integrated tokens, icons and the Inter font |
| `@shopware-ag/meteor-tokens` | Design tokens as CSS custom properties, framework-agnostic |
| `@shopware-ag/meteor-icon-kit` | SVG icon set, usable standalone or as Vue components via `mt-icon` |

The three packages can be installed together or individually.

---

## 1. Installing the component library

### Prerequisites

- Vue 3 application
- `vue-i18n` plugin (for translations)

### Installation

```sh
npm install @shopware-ag/meteor-component-library @shopware-ag/meteor-icon-kit
```

### CSS imports

Add both imports to the application entry point:

```ts
import "@shopware-ag/meteor-component-library/styles.css";
import "@shopware-ag/meteor-component-library/font.css";
```

`styles.css` contains the general component styles. `font.css` loads the Inter typeface.

### Configuring i18n

English and German are bundled. `vue-i18n` must be registered before the app is mounted:

```ts
import { createApp } from "vue";
import { createI18n } from "vue-i18n";
import App from "./App.vue";

const i18n = createI18n({ legacy: false });

createApp(App).use(i18n).mount("#app");
```

### TypeScript

Components are built entirely in TypeScript. No additional configuration is needed. Types are resolved automatically when importing `@shopware-ag/meteor-component-library`.

### Using components (tree-shakable)

Only what is imported ends up in the bundle:

```vue
<script setup>
import { MtButton, MtBanner } from "@shopware-ag/meteor-component-library";
</script>

<template>
  <MtButton variant="primary">Save</MtButton>
  <MtBanner variant="success">Saved successfully.</MtBanner>
</template>
```

Every component can also be imported directly from the root:

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

## 2. Installing the tokens standalone

The token package is framework-agnostic and can be installed independently:

```sh
npm install @shopware-ag/meteor-tokens
```

### Import

```ts
import "@shopware-ag/meteor-tokens/administration/light.css";
// Optional for dark mode:
import "@shopware-ag/meteor-tokens/administration/dark.css";
```

The light theme sets the tokens on `:root`. The dark theme becomes active on a DOM element carrying `data-theme="dark"`:

```html
<body data-theme="dark">
  <!-- application -->
</body>
```

### Usage

```css
.my-component {
  color: var(--color-text-primary-default);
  background: var(--color-elevation-surface-default);
  padding: var(--scale-size-16);
}
```

---

## 3. Installing the icon kit

```sh
npm install @shopware-ag/meteor-icon-kit
```

### Importing as SVG

```ts
import PlusIcon from "@shopware-ag/meteor-icon-kit/icons/regular/plus.svg";
```

### With mt-icon (Vue)

`mt-icon` is contained in the component library and renders any icon by name:

```html
<mt-icon name="regular-plus" />
<mt-icon name="solid-checkmark" size="20px" />
```

### Including SCSS/CSS

```scss
@import "@shopware-ag/meteor-icon-kit/icons/meteor-icon-kit.scss";
```

or classically via CSS:

```html
<link rel="stylesheet" href="your-asset-folder/meteor-icon-kit.css" />
```

### Dynamic colours (SVG directly)

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

### Vite example (vite-svg-loader)

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

## 4. Scaffolding a Shopware extension (create-meteor-extension)

There is a CLI tool for new Shopware admin extensions:

```bash
# Recommended: always the current version
npx @shopware-ag/create-meteor-extension

# Or install globally
npm install -g @shopware-ag/create-meteor-extension
create-meteor-extension
```

The CLI asks interactively for:
- **Extension name**: lower-case letters, digits and hyphens only (e.g. `my-awesome-extension`)

**Note**: The CLI always creates a folder `meteor-app` (as required by the Shopware 6.7+ plugin structure). The name you give is used in `package.json`, the README and the configuration files.

### Non-interactive mode (CI/CD)

```bash
npx @shopware-ag/create-meteor-extension --name my-extension --output-dir meteor-app
```

**Options:**
- `--name`: extension name (required in non-interactive mode)
- `--output-dir`: output directory name (optional, default: `meteor-app`)

### Generated structure

```
meteor-app/
├── src/
│   ├── locations/           # Vue components for admin locations
│   │   ├── exampleDashboard.vue
│   │   └── exampleProductTab.vue
│   ├── assets/              # styles and static assets
│   ├── app.ts               # application entry point
│   ├── bootstrap.ts         # SDK initialisation
│   ├── locations.ts         # location configuration
│   └── main.ts              # main entry point
├── snippet/                 # translation files
│   ├── de-DE.json
│   └── en-GB.json
├── public/                  # static assets
├── package.json
├── vite.config.ts
├── tsconfig.json
└── eslint.config.ts
```

For Shopware 6.7+ plugins this belongs in:
`custom/plugins/yourPlugin/src/Resources/app/meteor-app`

### The scaffold's most important dependencies

| Package | Purpose |
|---|---|
| `@shopware-ag/meteor-admin-sdk` | core SDK for admin extensions |
| `@shopware-ag/meteor-component-library` | UI component library |
| Vue 3 + Vue Router | framework |
| Vite | build tool |

### Example locations available in the template

1. **Dashboard Card** (`example-dashboard-before-content`): appears on the Shopware dashboard
2. **Product Tab** (`example-product-tab`): adds a tab to the product detail page

### After scaffolding

```bash
cd meteor-app
npm install
# install and activate the extension in Shopware
```

**Available scripts:**
- `npm run type-check` — TypeScript compiler check
- `npm run lint` — linting and autofixing with ESLint
- `npm run format` — code formatting with Prettier

---

## 5. Migrating from sw-* to mt-* (Meteor)

### Component mapping

| Old sw-* component | New mt-* component |
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

### Migrating design tokens

Replace hardcoded CSS values with Meteor tokens:

```css
/* Before */
color: #1a1a1a;

/* After */
color: var(--color-text-primary-default);
```

### admin-extension-sdk → meteor-admin-sdk

The package `@shopware-ag/admin-extension-sdk` was archived in March 2024 and replaced by `@shopware-ag/meteor-admin-sdk`:

```sh
npm uninstall @shopware-ag/admin-extension-sdk
npm install @shopware-ag/meteor-admin-sdk
```

Adjust the imports:

```js
// Before
import { notification } from "@shopware-ag/admin-extension-sdk";

// After
import { notification } from "@shopware-ag/meteor-admin-sdk";
```

### Step-by-step migration

Meteor works alongside existing components. Migrate page by page:

1. Install Meteor next to the existing configuration
2. Replace components one at a time
3. Move the styling over to design tokens gradually
4. Test every step before the next one

---

## 6. Browser support

Meteor targets all modern evergreen browsers. The features it uses are limited to the [Baseline Widely Available](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility) standard — supported in the current stable releases of Chrome, Edge, Firefox and Safari, without polyfills.

Legacy browsers and non-evergreen environments are not supported.

---

## 7. Stylelint plugin for Meteor

The stylelint plugin enforces the use of Meteor tokens in CSS:

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

**Available rules:**

| Rule | Description |
|---|---|
| `meteor/no-primitive-token` | Forbids primitive tokens (e.g. `--gray-800`); only semantic tokens are allowed |
| `meteor/prefer-background-token` | Semantic tokens only for background colours |
| `meteor/prefer-border-token` | Border tokens only for border colours |
| `meteor/prefer-color-token` | Color tokens only for `color` properties |
| `meteor/prefer-font-token` | Font tokens only for typography properties |
| `meteor/prefer-sizing-token` | Sizing tokens only for spacing (margin, padding, gap, …) |

**Example prefer-sizing-token:**

```css
/* Wrong */
a { margin: 10px; }

/* Right */
a { margin: var(--scale-size-10); }
```

**Example no-primitive-token:**

```css
/* Wrong */
a { color: var(--gray-800); }

/* Right */
a { color: var(--color-text-primary-default); }
```

---

## 8. Prettier config

The Prettier configuration package can be used for consistent code formatting:

```sh
npm install --save-dev @shopware-ag/prettier-config
```

---

## Further documentation

- All mt-* components (props/events/slots): skill `sw-meteor-components` → `references/deep/components.md`
- Design tokens in full: skill `sw-meteor-components` → `references/deep/tokens.md`; extended in `sw-meteor-design-tokens`
- Composables & directives: skill `sw-meteor-composables`
- Complete Admin SDK documentation: skill `sw-meteor-admin-sdk`
- Usage guidelines & accessibility: skill `sw-meteor-usage-guidelines`
