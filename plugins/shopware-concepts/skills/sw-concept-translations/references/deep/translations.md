# Shopware Übersetzungssystem — Vollständige Konzept-Doku

Quellen: `concepts/framework/translations/index.md`, `built-in-translation-system.md`, `fallback-language-selection.md`

---

## Übersetzungen — Überblick (index.md)

Shopware 6 ist eine mehrsprachige Plattform. Zwei Übersetzungssysteme:

1. **DAL-Übersetzungen** — Entity-Daten (Produktnamen, Kategorien, etc.)
2. **Snippets** — UI-Texte (Storefront, Administration)

---

## Built-in Translation System (built-in-translation-system.md)

### Übersicht

Erlaubt Installation und Update von Translations, die nicht im Standard-Shopware enthalten sind.
Stellt dieselbe Auswahl wie das **Language Pack Plugin** bereit und wird dieses vollständig ersetzen.

> **Wichtig**: Language Pack Plugin ist deprecated und wird mit **6.8.0.0 entfernt**.

### Translations-Quelle

GitHub-Repository: `shopware/translations` (Crowdin-verwaltet, täglicher Sync)
Enthält Translations für Shopware-Core und offizielle Plugins.

### CLI-Befehle

**Installation:**
```bash
# Bestimmte Locales installieren
php bin/console translation:install --locales=fr-FR,pl-PL

# Alle verfügbaren Locales
php bin/console translation:install --all

# Ohne Aktivierung installieren
php bin/console translation:install --locales=fr-FR --skip-activation
```

Re-Installation überschreibt bestehende Translations.

**Update:**
```bash
php bin/console translation:update
```

### Sprach-Aktivierung

- Standard: installierte Translations werden automatisch aktiviert
- `--skip-activation` verhindert sofortige Aktivierung
- `active`-Flag in `language`-Tabelle steuert Verfügbarkeit im Storefront

### Änderungs-Erkennung (Metadata)

- `crowdin-metadata.json` im translations-Repository: Locales, Last-Update-Timestamps, Completion %
- `updatedAt`-Feld → Vergleich mit `crowdin-metadata.lock` (private filesystem) → Update-Entscheidung

### Ladereihenfolge (Priorität, höchste zuerst)

1. **Datenbank-Translations** — höchste Priorität; überschreiben alles
2. **Country-spezifische Translations** (z.B. `en-GB`, `de-DE`) — Patch-Dateien für regionale Unterschiede
3. **Country-agnostische Translations** (`en`, `de`) — Fallback; zentrale gemeinsame Strings
4. **Built-in Translation System** — installierte Translations (niedrigste Priorität)

### Flysystem-Integration

Translations-Storage via Flysystem (Storage-Abstraktion):
- Lokal (Standard)
- Cloud: Amazon S3, Google Cloud Storage, Azure Blob Storage
- Custom Adapters

### Konfigurationsdatei

`src/Core/System/Resources/translation.yaml`

Felder:
- `repository-url` — Base-URL des Translation-Repositories
- `metadata-url` — URL zur metadata.json
- `plugins` — Liste unterstützter Plugins (z.B. `['SwagB2bPlatform']`)
- `excluded-locales` — von Verarbeitung ausgeschlossene Locales (Default: `['de-DE', 'en-GB']` — in Shopware enthalten)
- `plugin-mapping` — Mapping interner Plugin-IDs auf Repository-Namen
- `languages` — unterstützte Sprachen mit `name` (nativ) und `locale` (IETF BCP 47)

### Erweiterbares Config-Loading

- `AbstractTranslationConfigLoader` — abstrakte Klasse für Decoration Pattern
- `TranslationConfig` — Daten-Objekt aus `translation.yaml`; via DI verfügbar

---

## Fallback Language Selection (fallback-language-selection.md)

### Motivation (ab 6.7)

Vor 6.7: Nur country-spezifische Snippet-Dateien → Entwickler haben Dateien dupliziert
(z.B. `en-GB` → `en-US`) und nur wenige Keys geändert → aufgeblähte Repositories, inkonsistente Fallbacks.

**Lösung**: Country-independent Layer — gemeinsame Strings in neutraler Fallback-Datei,
regionale Unterschiede in kleinen Patch-Dateien.

### Fallback-Sprachen

| Fallback-Code | Standard-Variante | Beispiel-Dialekte |
|---|---|---|
| `en` | `en-GB` (British English) | `en-US`, `en-CA`, `en-IN` |
| `de` | `de-DE` (Deutschland) | `de-AT`, `de-CH` |
| `es` | `es-ES` (Kastilisches Spanisch) | `es-AR`, `es-MX` |
| `pt` | `pt-PT` (Europäisches Portugiesisch) | `pt-BR` |
| `fr` | `fr-FR` (Frankreich) | `fr-CA`, `fr-CH` |
| `nl` | `nl-NL` (Niederlande) | `nl-BE` |

Auflösungsreihenfolge: Country-spezifisch (`de-AT`) → Country-agnostisch (`de`) → `en` (universelles Fallback)

### CLI-Tool für Migration

```bash
# Dateinamen validieren
bin/console translation:lint-filenames

# Automatische Migration zu agnostischen Dateinamen
bin/console translation:lint-filenames --fix

# Alle Extensions einschließen
bin/console translation:lint-filenames --all

# Nur bestimmte Extensions
bin/console translation:lint-filenames --extensions=SwagCmsExtensions
```

**Ausgabe-Spalten**: Filename, Path, Domain, Locale, Language, Script, Region

### Implementierungsrichtlinien für Extension-Entwickler

- **Vollständige Base-Datei erstellen** (`messages.<sprache>.base.json`) pro unterstützter Sprache
- **Patch-Dateien nur bei Bedarf** — minimal halten
- **Neutralität anstreben** — landespezifische Begriffe nur in Patch-Dateien
- **Standard-Dialekt wählen** — für Spanisch: Kastilisch für maximale Verständlichkeit
- **Namenskonventionen** — agnostisch: `storefront.nl.json`; Patch: `storefront.nl-BE.json`
- **Validierung**: Cache leeren + `bin/console translation:validate` + `translation:lint-filenames`

### Dateinamen-Konventionen

```
messages.<sprache>.base.json       — Basis-Datei (country-agnostic, definierender Dialekt)
storefront.<sprache>.json          — Agnostische Storefront-Übersetzung
storefront.<sprache>-<region>.json — Regionale Patch-Datei
administration.<sprache>.json      — Admin-Übersetzungen
```

Basis-Dateien (`messages.*.base.json`) **müssen** immer `messages` als Domain verwenden.
