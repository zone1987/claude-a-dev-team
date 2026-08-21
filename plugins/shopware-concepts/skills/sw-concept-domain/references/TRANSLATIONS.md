# Shopware translation system — concept

Complete concept documentation: `TRANSLATIONS-DETAIL.md`

## Quick overview

### DAL translations (entities)

- Every translatable entity has a `*_translation` table
- **3-step resolution**: current language → parent language → system language
- Parent language: allows e.g. `de-AT` as a dialect of `de-DE`

### Snippet files (UI texts)

- JSON files in `Resources/snippet/<locale>/`
- Storefront: Twig `trans` filter; administration: Vue I18n
- Load order (priority): DB translations > country-specific > country-agnostic > built-in system

### Country-agnostic snippet layer (from 6.7)

- Goal: avoid duplicates (no `en-US` as a copy of `en-GB`)
- `messages.<language>.base.json` — neutral base file
- `storefront.<language>-<region>.json` — small patch file for regional differences
- Validation: `bin/console translation:lint-filenames`

### Built-in translation system (replaces the Language Pack)

- Translations from the GitHub repo `shopware/translations` (fed by Crowdin)
- `translation:install --locales=fr-FR,de-AT` — install languages
- `translation:update` — apply updates
- Stores via Flysystem (local, S3, etc.)
- The Language Pack plugin will be **removed in 6.8.0.0**

Technical implementation: `shopware-core`, `shopware-storefront` (dev plugins)
