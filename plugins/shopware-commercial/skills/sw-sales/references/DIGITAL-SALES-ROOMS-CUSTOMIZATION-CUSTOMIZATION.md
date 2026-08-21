# Digital Sales Rooms — Customization (complete)

> All customizations happen **in your own Nuxt layer**, never in the default layer `dsr`.

## Contents

- [The Nuxt Layer Concept](#the-nuxt-layer-concept)
- [Branding Customizations](#branding-customizations)
- [Overriding Components](#overriding-components)
- [Customizing i18n (Internationalization)](#customizing-i18n-internationalization)

## The Nuxt Layer Concept

The DSR frontend is based on [Nuxt Layers](https://nuxt.com/docs/getting-started/layers).
The source code (`dsr-frontends`) contains:

- **`dsr/`** — default layer (do not edit)
- **`example/`** — example customization layer (rename and adapt)

### Creating Your Own Layer

1. Rename the `example/` layer (e.g. to `my-brand/`)
2. Import it in `nuxt.config.ts`:

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: ['./my-brand', './dsr'],
  // ...
})
```

Nuxt always uses the first version of a file it finds (your own layer takes
priority over `dsr`).

---

## Branding Customizations

### Favicon

Create a `public/` folder in your own layer (if it does not exist yet) and
place `favicon.ico` inside it:

```
my-brand/
  public/
    favicon.ico   ← place it here
```

### Web Application Title

Create `nuxt.config.ts` in your own layer (if it does not exist yet):

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

### Theme Color (Primary Color)

Create `uno.config.ts` in your own layer:

```js
// my-brand/uno.config.ts
export default {
  theme: {
    colors: {
      primary: {
        DEFAULT: '#000000'   // desired primary color
      }
    }
  }
}
```

> Tip: The complete key structure available for overriding can be found in
> `dsr/uno.config.ts`.

---

## Overriding Components

### Example: Customizing `SwWishlistButton`

1. Locate the original component in the default layer:
   ```
   dsr/components/shared/molecules/SwWishlistButton.vue
   ```

2. Copy the file into your own layer (same directory structure):
   ```
   my-brand/components/shared/molecules/SwWishlistButton.vue
   ```

3. Adapt the component in your own layer as needed.

The frontend app now ignores `SwWishlistButton` from the `dsr` layer and
uses exclusively the version from your own layer.

**General principle:**
- All available components are located under `dsr/components/`
- The same file structure in your own layer → automatic override

---

## Customizing i18n (Internationalization)

### Configuring i18n in `nuxt.config.ts`

In your own layer:

```js
// my-brand/nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    "@nuxtjs/i18n",
  ],
  i18n: {
    langDir: "./i18n/src/langs/",
    ...i18nConfig,  // import from the dsr layer
  },
})
```

### Creating Translation Files

Use the directory structure of the `example` layer as a template:

```
my-brand/
  i18n/
    src/
      langs/
        en-US.ts   ← contains only overridden keys
        de-DE.ts
```

> Only enter the keys that should actually be overridden.
> Missing keys automatically fall back to the default layer.
