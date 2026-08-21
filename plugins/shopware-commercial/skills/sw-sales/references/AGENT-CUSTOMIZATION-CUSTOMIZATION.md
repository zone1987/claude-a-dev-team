# Sales Agent — Customization (complete)

> All customizations happen **in your own Nuxt layer**, never in the default layer `sales-agent`.

## Contents

- [The Nuxt Layer Concept](#the-nuxt-layer-concept)
- [Branding Customizations](#branding-customizations)
- [Overriding Components](#overriding-components)
- [Customizing i18n (Internationalization)](#customizing-i18n-internationalization)

## The Nuxt Layer Concept

Sales Agent is based on [Nuxt Layers](https://nuxt.com/docs/getting-started/layers).
The source code contains:

- **`layers/sales-agent/`** — default layer (do not edit)
- **`example/`** — example customization layer (rename and adapt)

### Creating Your Own Layer

1. Rename the `example/` layer (e.g. `my-brand/`)
2. Import it in `nuxt.config.ts`:

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: ['./my-brand', './layers/sales-agent'],
  // ...
})
```

---

## Branding Customizations

### Favicon

Create a `public/` folder in your own layer and place `favicon.ico` in it:

```
my-brand/
  public/
    favicon.ico
```

### Web Application Title

```js
// my-brand/nuxt.config.ts
export default defineNuxtConfig({
  app: {
    head: {
      title: 'Your app name'
    }
  }
})
```

### Theme Colors (Meteor Component Library)

Sales Agent uses the Shopware [Meteor Component Library](https://shopware.design/get-started/installation.html)
with a comprehensive CSS variable system. There is a light theme and a dark theme.

**Overriding colors:**

```css
/* my-brand/main.css */
:root {
  --color-interaction-primary-default: #80A1BA;
  /* Further CSS variables as needed */
}
```

**Including the CSS file in Nuxt:**

```javascript
// my-brand/nuxt.config.ts
export default defineNuxtConfig({
  css: ["./main.css"],
})
```

Available CSS variables:
- [Light Theme](https://github.com/shopware/meteor/blob/main/packages/tokens/deliverables/administration/light.css)
- [Dark Theme](https://github.com/shopware/meteor/blob/main/packages/tokens/deliverables/administration/dark.css)

---

## Overriding Components

### Example: Customizing the Login Page

1. Locate the original component in the default layer:
   ```
   layers/sales-agent/pages/auth/login.vue
   ```

2. Copy the file into your own layer (same directory structure):
   ```
   my-brand/pages/auth/login.vue
   ```

3. Adapt the component as needed.

The app ignores `login.vue` from the default layer and uses exclusively
the version from your own layer.

**All available components** are located under `~/layers/sales-agent`.

---

## Customizing i18n (Internationalization)

### Configuring i18n in `nuxt.config.ts`

```js
// my-brand/nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    "@nuxtjs/i18n",
  ],
  i18n: {
    langDir: "./i18n/src/langs/",
    locales: [
      {
        code: "en-GB",
        iso: "en-GB",
        file: "en-GB.ts",
      },
      {
        code: "de-DE",
        iso: "de-DE",
        file: "de-DE.ts",
      },
    ],
  },
})
```

### Creating Translation Files

```
my-brand/
  i18n/
    src/
      langs/
        en-GB.ts   ← only overridden keys
        de-DE.ts
```

Use the structure of the `example` layer as a template.
