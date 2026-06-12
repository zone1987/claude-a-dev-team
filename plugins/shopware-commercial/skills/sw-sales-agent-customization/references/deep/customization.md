# Sales Agent — Customization (vollständig)

> Alle Anpassungen erfolgen **im eigenen Nuxt-Layer**, nie im Default-Layer `sales-agent`.

## Das Nuxt-Layer-Konzept

Sales Agent basiert auf [Nuxt Layers](https://nuxt.com/docs/getting-started/layers).
Im Quellcode existiert:

- **`layers/sales-agent/`** — Default-Layer (nicht bearbeiten)
- **`example/`** — Beispiel-Customization-Layer (umbenennen und anpassen)

### Eigenen Layer erstellen

1. `example/`-Layer umbenennen (z.B. `my-brand/`)
2. In `nuxt.config.ts` importieren:

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: ['./my-brand', './layers/sales-agent'],
  // ...
})
```

---

## Branding Anpassungen

### Favicon

Im eigenen Layer `public/`-Ordner anlegen und `favicon.ico` platzieren:

```
my-brand/
  public/
    favicon.ico
```

### Web-Application-Titel

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

### Theme-Farben (Meteor Component Library)

Sales Agent nutzt die Shopware [Meteor Component Library](https://shopware.design/get-started/installation.html)
mit einem umfassenden CSS-Variablen-System. Es gibt ein Light-Theme und Dark-Theme.

**Farben überschreiben:**

```css
/* my-brand/main.css */
:root {
  --color-interaction-primary-default: #80A1BA;
  /* Weitere CSS-Variablen nach Bedarf */
}
```

**CSS-Datei in Nuxt einbinden:**

```javascript
// my-brand/nuxt.config.ts
export default defineNuxtConfig({
  css: ["./main.css"],
})
```

Verfügbare CSS-Variablen:
- [Light Theme](https://github.com/shopware/meteor/blob/main/packages/tokens/deliverables/administration/light.css)
- [Dark Theme](https://github.com/shopware/meteor/blob/main/packages/tokens/deliverables/administration/dark.css)

---

## Komponenten Überschreiben

### Beispiel: Login-Seite anpassen

1. Original-Komponente im Default-Layer lokalisieren:
   ```
   layers/sales-agent/pages/auth/login.vue
   ```

2. Datei in den eigenen Layer kopieren (gleiche Verzeichnisstruktur):
   ```
   my-brand/pages/auth/login.vue
   ```

3. Komponente nach Bedarf anpassen.

Die App ignoriert `login.vue` aus dem Default-Layer und verwendet ausschließlich
die Version aus dem eigenen Layer.

**Alle verfügbaren Komponenten** befinden sich unter `~/layers/sales-agent`.

---

## i18n (Internationalisierung) Anpassen

### i18n in `nuxt.config.ts` konfigurieren

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

### Übersetzungsdateien anlegen

```
my-brand/
  i18n/
    src/
      langs/
        en-GB.ts   ← nur überschriebene Keys
        de-DE.ts
```

Struktur des `example`-Layers als Vorlage verwenden.
