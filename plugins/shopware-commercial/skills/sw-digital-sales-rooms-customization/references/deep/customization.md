# Digital Sales Rooms — Customization (vollständig)

> Alle Anpassungen erfolgen **im eigenen Nuxt-Layer**, nie im Default-Layer `dsr`.

## Das Nuxt-Layer-Konzept

DSR-Frontend basiert auf [Nuxt Layers](https://nuxt.com/docs/getting-started/layers).
Im Quellcode (`dsr-frontends`) existiert:

- **`dsr/`** — Default-Layer (nicht bearbeiten)
- **`example/`** — Beispiel-Customization-Layer (umbenennen und anpassen)

### Eigenen Layer erstellen

1. `example/`-Layer umbenennen (z.B. in `my-brand/`)
2. In `nuxt.config.ts` importieren:

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: ['./my-brand', './dsr'],
  // ...
})
```

Nuxt verwendet immer die zuerst gefundene Version einer Datei (eigener Layer
hat Priorität über `dsr`).

---

## Branding Anpassungen

### Favicon

Im eigenen Layer `public/`-Ordner anlegen (falls nicht vorhanden) und
`favicon.ico` darin platzieren:

```
my-brand/
  public/
    favicon.ico   ← hier ablegen
```

### Web-Application-Titel

`nuxt.config.ts` im eigenen Layer anlegen (falls nicht vorhanden):

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

### Theme-Farbe (Primärfarbe)

`uno.config.ts` im eigenen Layer anlegen:

```js
// my-brand/uno.config.ts
export default {
  theme: {
    colors: {
      primary: {
        DEFAULT: '#000000'   // gewünschte Primärfarbe
      }
    }
  }
}
```

> Tipp: Die vollständige Key-Struktur zum Überschreiben findet sich in
> `dsr/uno.config.ts`.

---

## Komponenten Überschreiben

### Beispiel: `SwWishlistButton` anpassen

1. Original-Komponente im Default-Layer lokalisieren:
   ```
   dsr/components/shared/molecules/SwWishlistButton.vue
   ```

2. Datei in den eigenen Layer kopieren (gleiche Verzeichnisstruktur):
   ```
   my-brand/components/shared/molecules/SwWishlistButton.vue
   ```

3. Komponente im eigenen Layer nach Bedarf anpassen.

Die Frontend-App ignoriert nun `SwWishlistButton` aus dem `dsr`-Layer und
verwendet ausschließlich die Version aus dem eigenen Layer.

**Generelles Prinzip:**
- Alle verfügbaren Komponenten befinden sich unter `dsr/components/`
- Gleiche Dateistruktur im eigenen Layer → automatisches Override

---

## i18n (Internationalisierung) Anpassen

### i18n in `nuxt.config.ts` konfigurieren

Im eigenen Layer:

```js
// my-brand/nuxt.config.ts
export default defineNuxtConfig({
  modules: [
    "@nuxtjs/i18n",
  ],
  i18n: {
    langDir: "./i18n/src/langs/",
    ...i18nConfig,  // aus dem dsr-Layer importieren
  },
})
```

### Übersetzungsdateien anlegen

Verzeichnisstruktur des `example`-Layers als Vorlage verwenden:

```
my-brand/
  i18n/
    src/
      langs/
        en-US.ts   ← nur überschriebene Keys enthalten
        de-DE.ts
```

> Nur die Keys eintragen, die tatsächlich überschrieben werden sollen.
> Fehlende Keys fallen automatisch auf den Default-Layer zurück.
