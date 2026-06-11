---
name: sw-concept-translations
description: >
  Shopware Übersetzungssystem: DAL-Translations, Snippet-Dateien, Fallback-Sprachen,
  Built-in Translation System (ab 6.7), country-agnostic Snippets. Trigger: "Translations Shopware",
  "Übersetzungen Shopware", "Shopware Sprachsystem", "Snippets Shopware", "Fallback Language",
  "Built-in Translation", "wie funktioniert Mehrsprachigkeit", "de-DE fallback",
  "translation:install", "Language Pack Migration", "Shopware translations concept",
  "snippet files", "json translations shopware", "DAL Translations", "Translation Tabelle".
---

# Shopware Übersetzungssystem — Konzept

Vollständige Konzept-Doku: `references/deep/translations.md`

## Kurzüberblick

### DAL-Übersetzungen (Entitäten)

- Jede translatierbare Entity hat eine `*_translation`-Tabelle
- **3-stufige Auflösung**: Aktuelle Sprache → Parent-Sprache → Systemsprache
- Parent-Sprache: Ermöglicht z.B. `de-AT` als Dialekt von `de-DE`

### Snippet-Dateien (UI-Texte)

- JSON-Dateien in `Resources/snippet/<locale>/`
- Storefront: Twig-`trans`-Filter; Administration: Vue I18n
- Ladereihenfolge (Priorität): DB-Translations > Country-spezifisch > Country-agnostisch > Built-in System

### Country-agnostisches Snippet-Layer (ab 6.7)

- Ziel: Duplikate vermeiden (kein `en-US` als Kopie von `en-GB`)
- `messages.<sprache>.base.json` — neutrale Basis-Datei
- `storefront.<sprache>-<region>.json` — kleine Patch-Datei für regionale Unterschiede
- Validierung: `bin/console translation:lint-filenames`

### Built-in Translation System (ersetzt Language Pack)

- Translations aus GitHub-Repo `shopware/translations` (Crowdin-gespeist)
- `translation:install --locales=fr-FR,de-AT` — Sprachen installieren
- `translation:update` — Updates einspielen
- Speichert via Flysystem (lokal, S3, etc.)
- Language Pack Plugin wird in **6.8.0.0 entfernt**

Technische Umsetzung: `shopware-core`, `shopware-storefront` (Dev-Plugins)
