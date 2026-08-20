# Sales Agent — Customization

Vollständige Referenz: [AGENT-CUSTOMIZATION-CUSTOMIZATION.md](AGENT-CUSTOMIZATION-CUSTOMIZATION.md)

## Kernprinzip: Nuxt Layer

Sales Agent nutzt das **Nuxt Layer Konzept**. Der Default-Layer `sales-agent`
bleibt unberührt. Anpassungen erfolgen in einem eigenen Layer.
Ein Beispiel-Layer `example` liegt im Quellcode bei.

## Schnellübersicht

| Thema | Vorgehen |
|-------|---------|
| Favicon | `public/favicon.ico` im eigenen Layer |
| App-Titel | `nuxt.config.ts` → `app.head.title` |
| Primärfarbe | CSS-Variable `--color-interaction-primary-default` überschreiben |
| Komponente überschreiben | Datei aus `layers/sales-agent/` in eigenen Layer kopieren |
| i18n überschreiben | `nuxt.config.ts` + `i18n/src/langs/` im eigenen Layer |
