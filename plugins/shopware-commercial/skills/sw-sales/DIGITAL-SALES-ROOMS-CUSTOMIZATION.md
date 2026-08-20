# Digital Sales Rooms — Customization

Full reference: [DIGITAL-SALES-ROOMS-CUSTOMIZATION-CUSTOMIZATION.md](DIGITAL-SALES-ROOMS-CUSTOMIZATION-CUSTOMIZATION.md)

## Core principle: Nuxt layers

DSR uses the **Nuxt layer concept**. The default layer `dsr` remains untouched.
Customizations are made in your own layer, which is imported in `nuxt.config.ts`.
An example layer `example` ships with the source code.

## Quick overview

| Topic | File in your own layer |
|-------|----------------------|
| Favicon | `public/favicon.ico` |
| App title | `nuxt.config.ts` → `app.head.title` |
| Primary color | `uno.config.ts` → `theme.colors.primary` |
| Override a component | copy the file from `dsr/components/` into your own layer |
| Override i18n | `nuxt.config.ts` + `i18n/src/langs/` in your own layer |
