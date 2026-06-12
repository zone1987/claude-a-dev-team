---
name: sw-digital-sales-rooms-customization
description: >
  Anpassung der Digital Sales Rooms Frontend-App: Nuxt-Layer-Konzept,
  Branding (Favicon, Titel, Farben), Komponenten überschreiben, i18n anpassen.
  Triggers: "DSR anpassen", "customize digital sales rooms", "dsr branding",
  "dsr nuxt layer", "dsr component override", "dsr i18n", "dsr theme color",
  "dsr favicon", "SwWishlistButton override", "dsr custom layer"
---

# Digital Sales Rooms — Customization

Vollständige Referenz: [references/deep/customization.md](references/deep/customization.md)

## Kernprinzip: Nuxt Layer

DSR nutzt das **Nuxt Layer Konzept**. Der Default-Layer `dsr` bleibt unberührt.
Anpassungen erfolgen in einem eigenen Layer, der in `nuxt.config.ts` importiert wird.
Ein Beispiel-Layer `example` liegt im Quellcode bei.

## Schnellübersicht

| Thema | Datei im eigenen Layer |
|-------|----------------------|
| Favicon | `public/favicon.ico` |
| App-Titel | `nuxt.config.ts` → `app.head.title` |
| Primärfarbe | `uno.config.ts` → `theme.colors.primary` |
| Komponente überschreiben | Datei aus `dsr/components/` in eigenen Layer kopieren |
| i18n überschreiben | `nuxt.config.ts` + `i18n/src/langs/` im eigenen Layer |
