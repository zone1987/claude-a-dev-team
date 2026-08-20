# Shopware translation system — complete concept documentation

Sources: `concepts/framework/translations/index.md`, `built-in-translation-system.md`, `fallback-language-selection.md`

---

## Contents

- [Translations — overview (index.md)](#translations--overview-indexmd)
- [Built-in Translation System (built-in-translation-system.md)](#built-in-translation-system-built-in-translation-systemmd)
- [Fallback Language Selection (fallback-language-selection.md)](#fallback-language-selection-fallback-language-selectionmd)

## Translations — overview (index.md)

Shopware 6 is a multilingual platform. Two translation systems:

1. **DAL translations** — entity data (product names, categories, etc.)
2. **Snippets** — UI texts (storefront, administration)

---

## Built-in Translation System (built-in-translation-system.md)

### Overview

Allows the installation and update of translations that are not part of standard Shopware.
Provides the same selection as the **Language Pack plugin** and will replace it completely.

> **Important**: the Language Pack plugin is deprecated and will be **removed with 6.8.0.0**.

### Translations source

GitHub repository: `shopware/translations` (Crowdin-managed, daily sync)
Contains translations for the Shopware core and official plugins.

### CLI commands

**Installation:**
```bash
# Install specific locales
php bin/console translation:install --locales=fr-FR,pl-PL

# All available locales
php bin/console translation:install --all

# Install without activation
php bin/console translation:install --locales=fr-FR --skip-activation
```

Re-installation overwrites existing translations.

**Update:**
```bash
php bin/console translation:update
```

### Language activation

- Default: installed translations are activated automatically
- `--skip-activation` prevents immediate activation
- The `active` flag in the `language` table controls availability in the storefront

### Change detection (metadata)

- `crowdin-metadata.json` in the translations repository: locales, last-update timestamps, completion %
- The `updatedAt` field → comparison with `crowdin-metadata.lock` (private filesystem) → update decision

### Load order (priority, highest first)

1. **Database translations** — highest priority; override everything
2. **Country-specific translations** (e.g. `en-GB`, `de-DE`) — patch files for regional differences
3. **Country-agnostic translations** (`en`, `de`) — fallback; central shared strings
4. **Built-in translation system** — installed translations (lowest priority)

### Flysystem integration

Translations storage via Flysystem (storage abstraction):
- Local (default)
- Cloud: Amazon S3, Google Cloud Storage, Azure Blob Storage
- Custom adapters

### Configuration file

`src/Core/System/Resources/translation.yaml`

Fields:
- `repository-url` — base URL of the translation repository
- `metadata-url` — URL to the metadata.json
- `plugins` — list of supported plugins (e.g. `['SwagB2bPlatform']`)
- `excluded-locales` — locales excluded from processing (default: `['de-DE', 'en-GB']` — included in Shopware)
- `plugin-mapping` — mapping of internal plugin IDs to repository names
- `languages` — supported languages with `name` (native) and `locale` (IETF BCP 47)

### Extensible config loading

- `AbstractTranslationConfigLoader` — abstract class for the decoration pattern
- `TranslationConfig` — data object from `translation.yaml`; available via DI

---

## Fallback Language Selection (fallback-language-selection.md)

### Motivation (from 6.7)

Before 6.7: only country-specific snippet files → developers duplicated files
(e.g. `en-GB` → `en-US`) and changed only a few keys → bloated repositories, inconsistent fallbacks.

**Solution**: a country-independent layer — shared strings in a neutral fallback file,
regional differences in small patch files.

### Fallback languages

| Fallback code | Default variant | Example dialects |
|---|---|---|
| `en` | `en-GB` (British English) | `en-US`, `en-CA`, `en-IN` |
| `de` | `de-DE` (Germany) | `de-AT`, `de-CH` |
| `es` | `es-ES` (Castilian Spanish) | `es-AR`, `es-MX` |
| `pt` | `pt-PT` (European Portuguese) | `pt-BR` |
| `fr` | `fr-FR` (France) | `fr-CA`, `fr-CH` |
| `nl` | `nl-NL` (Netherlands) | `nl-BE` |

Resolution order: country-specific (`de-AT`) → country-agnostic (`de`) → `en` (universal fallback)

### CLI tool for migration

```bash
# Validate file names
bin/console translation:lint-filenames

# Automatic migration to agnostic file names
bin/console translation:lint-filenames --fix

# Include all extensions
bin/console translation:lint-filenames --all

# Only specific extensions
bin/console translation:lint-filenames --extensions=SwagCmsExtensions
```

**Output columns**: Filename, Path, Domain, Locale, Language, Script, Region

### Implementation guidelines for extension developers

- **Create a complete base file** (`messages.<language>.base.json`) per supported language
- **Patch files only where needed** — keep them minimal
- **Aim for neutrality** — country-specific terms only in patch files
- **Choose a default dialect** — for Spanish: Castilian for maximum comprehensibility
- **Naming conventions** — agnostic: `storefront.nl.json`; patch: `storefront.nl-BE.json`
- **Validation**: clear the cache + `bin/console translation:validate` + `translation:lint-filenames`

### File name conventions

```
messages.<language>.base.json       — base file (country-agnostic, defining dialect)
storefront.<language>.json          — agnostic storefront translation
storefront.<language>-<region>.json — regional patch file
administration.<language>.json      — admin translations
```

Base files (`messages.*.base.json`) **must** always use `messages` as the domain.
