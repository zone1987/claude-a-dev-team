# Contao 5 — Translations

## Contents

- [Übersicht](#übersicht)
- [Unterstützte Sprachen](#unterstützte-sprachen)
- [Translation-Struktur](#translation-struktur)
- [Implementierungsmethoden](#implementierungsmethoden)
- [Symfony-Integration (ab Contao 5.3)](#symfony-integration-ab-contao-53)
- [Übersetzungen abrufen](#übersetzungen-abrufen)
- [Übersetzungsschlüssel finden](#übersetzungsschlüssel-finden)
- [Eigene Translations in Bundles](#eigene-translations-in-bundles)
- [Häufige Übersetzungsschlüssel](#häufige-übersetzungsschlüssel)

## Übersicht

Contao stellt ein eigenes Translations-Framework bereit, das parallel zu Symfonys
Translation-Komponente betrieben werden kann. Übersetzungen werden in
`contao/languages/` oder `Resources/contao/languages/` gespeichert.

**Unterstützte Formate:** XLIFF (`.xlf`) und PHP-Arrays (`.php`)

---

## Unterstützte Sprachen

**Frontend:** ISO 639 Sprachcodes (z.B. `de`) oder ISO 15897 POSIX Locales (z.B. `de_AT`)

**Backend:** Beschränkt auf konfigurierte Sprachen:

```yaml
# config/config.yaml
contao:
    intl:
        enabled_locales:
            - en
            - de_AT
```

Englisch (`en`) dient als Fallback-Sprache in allen Kontexten.

---

## Translation-Struktur

Hierarchie: **Sprache → Domain → Kategorie → Schlüssel → Label/Beschreibung**

Alle Übersetzungen befüllen das `$GLOBALS['TL_LANG']`-Array:

```php
$GLOBALS['TL_LANG']['MSC']['goBack'] = 'Go back';
```

### Domains

| Domain | Zweck |
|--------|-------|
| `default` | Allgemeine Frontend-/Backend-Übersetzungen |
| `tl_content` | Content-Element-Felder |
| `tl_module` | Frontend-Modul-Felder |
| `modules` | Backend-Modul-Namen |
| `countries` | Ländernamen |
| `languages` | Sprachnamen |
| `exception` | Fehlermeldungen |
| `explain` | Erklärungstexte |

Für jede DCA-Tabelle gibt es eine eigene Domain (z.B. `tl_news`).

### Kategorien (Auswahl)

| Kategorie | Bedeutung |
|-----------|-----------|
| `MSC` | Verschiedene allgemeine Labels |
| `ERR` | Fehlermeldungen |
| `CTE` | Content-Element-Typen |
| `FMD` | Frontend-Modul-Typen |
| `PTY` | Seitentypen |
| `MOD` | Backend-Modul-Typen |
| `CNT` | Ländernamen |
| `DAYS` | Wochentage |
| `MONTHS` | Monatsnamen |

---

## Implementierungsmethoden

### PHP-Format

```php
// contao/languages/en/default.php
$GLOBALS['TL_LANG']['MSC']['goBack'] = 'Back';
$GLOBALS['TL_LANG']['MSC']['readMore'] = ['Read more …', 'Read the full article.'];
```

### XLIFF-Format

```xml
<!-- contao/languages/en/default.xlf -->
<?xml version="1.0" encoding="UTF-8"?>
<xliff version="1.1">
  <file datatype="php" original="src/Resources/contao/languages/en/default.php" source-language="en">
    <body>
      <trans-unit id="MSC.goBack">
        <source>Back</source>
      </trans-unit>
      <trans-unit id="MSC.readMore.0">
        <source>Read more …</source>
      </trans-unit>
      <trans-unit id="MSC.readMore.1">
        <source>Read the full article.</source>
      </trans-unit>
    </body>
  </file>
</xliff>
```

---

## Symfony-Integration (ab Contao 5.3)

Ab Version 5.3 können Symfony-Übersetzungsformate mit `contao_`-Präfix verwendet werden:

### YAML-Format

```yaml
# translations/contao_default.en.yaml
MSC:
    goBack: Return back
    readMore:
        - Read more …
        - Read the full article.
```

### Andere Domains

```yaml
# translations/contao_tl_content.en.yaml
CTE:
    my_element:
        - My Content Element
        - A short description.

# translations/contao_modules.en.yaml
MOD:
    my_module:
        - My Module
        - Manage entries.
```

---

## Übersetzungen abrufen

### Symfony Translator (empfohlen)

```php
use Symfony\Contracts\Translation\TranslatorInterface;

class MyService
{
    public function __construct(private readonly TranslatorInterface $translator) {}

    public function getLabel(): string
    {
        return $this->translator->trans('MSC.goBack', [], 'contao_default');
    }
}
```

### In PHP-Templates

```php
<?= $this->trans('MSC.goBack') ?>
<?= $this->trans('MSC.readMore', [], 'contao_default') ?>
```

### In Twig-Templates

```twig
{{ 'MSC.goBack'|trans({}, 'contao_default') }}

{# Mit Default-Domain #}
{% trans_default_domain 'contao_default' %}
{{ 'MSC.goBack'|trans }}
```

---

## Übersetzungsschlüssel finden

Da Schlüssel und Domains oft nur im Quellcode zu finden sind:

1. Symfony-Debug-Tools nutzen (`debug:translation`)
2. `$GLOBALS['TL_LANG']` debuggen
3. Contao-Kerncode in `vendor/contao/*/contao/languages/en/` durchsuchen

---

## Eigene Translations in Bundles

Verzeichnisstruktur:

```
contao/
└── languages/
    ├── en/
    │   ├── default.php (oder .xlf)
    │   ├── tl_my_table.php
    │   └── modules.php
    └── de/
        ├── default.php
        └── tl_my_table.php
```

Ab Contao 5.3 alternativ:

```
translations/
├── contao_default.en.yaml
├── contao_default.de.yaml
├── contao_tl_my_table.en.yaml
└── contao_modules.en.yaml
```

---

## Häufige Übersetzungsschlüssel

### Backend-Modul-Labels

```php
// contao/languages/en/modules.php
$GLOBALS['TL_LANG']['MOD']['my_module'] = ['My Module', 'Manage my records.'];
```

### DCA-Felder

```php
// contao/languages/en/tl_my_table.php
$GLOBALS['TL_LANG']['tl_my_table']['name'] = ['Name', 'Enter the name here.'];
$GLOBALS['TL_LANG']['tl_my_table']['edit'] = ['Edit record ID %s', ''];
```

### Content Element Typen

```php
// contao/languages/en/default.php
$GLOBALS['TL_LANG']['CTE']['my_element'] = ['My Element', 'A custom content element.'];
```

---

*Quelle: https://docs.contao.org/5.x/dev/framework/translations/*  
*https://docs.contao.org/5.x/dev/getting-started/translations/*
