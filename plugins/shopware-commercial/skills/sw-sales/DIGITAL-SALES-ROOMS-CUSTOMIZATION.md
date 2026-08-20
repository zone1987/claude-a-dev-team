# Digital Sales Rooms — Customization

Vollständige Referenz: [DIGITAL-SALES-ROOMS-CUSTOMIZATION-CUSTOMIZATION.md](DIGITAL-SALES-ROOMS-CUSTOMIZATION-CUSTOMIZATION.md)

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
