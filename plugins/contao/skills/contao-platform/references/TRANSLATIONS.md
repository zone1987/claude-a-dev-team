# Contao 5 — Translations

## Contents

- [Overview](#overview)
- [Supported languages](#supported-languages)
- [Translation structure](#translation-structure)
- [Implementation methods](#implementation-methods)
- [Symfony integration (Contao 5.3 and later)](#symfony-integration-contao-53-and-later)
- [Retrieving translations](#retrieving-translations)
- [Finding translation keys](#finding-translation-keys)
- [Custom translations in bundles](#custom-translations-in-bundles)
- [Common translation keys](#common-translation-keys)

## Overview

Contao provides its own translations framework, which can be operated alongside Symfony's
Translation component. Translations are stored in
`contao/languages/` or `Resources/contao/languages/`.

**Supported formats:** XLIFF (`.xlf`) and PHP arrays (`.php`)

---

## Supported languages

**Front end:** ISO 639 language codes (e.g. `de`) or ISO 15897 POSIX locales (e.g. `de_AT`)

**Back end:** limited to the configured languages:

```yaml
# config/config.yaml
contao:
    intl:
        enabled_locales:
            - en
            - de_AT
```

English (`en`) serves as the fallback language in all contexts.

---

## Translation structure

Hierarchy: **language → domain → category → key → label/description**

All translations populate the `$GLOBALS['TL_LANG']` array:

```php
$GLOBALS['TL_LANG']['MSC']['goBack'] = 'Go back';
```

### Domains

| Domain | Purpose |
|--------|-------|
| `default` | General front end/back end translations |
| `tl_content` | Content element fields |
| `tl_module` | Front end module fields |
| `modules` | Back end module names |
| `countries` | Country names |
| `languages` | Language names |
| `exception` | Error messages |
| `explain` | Explanatory texts |

Every DCA table has its own domain (e.g. `tl_news`).

### Categories (selection)

| Category | Meaning |
|-----------|-----------|
| `MSC` | Various general labels |
| `ERR` | Error messages |
| `CTE` | Content element types |
| `FMD` | Front end module types |
| `PTY` | Page types |
| `MOD` | Back end module types |
| `CNT` | Country names |
| `DAYS` | Weekdays |
| `MONTHS` | Month names |

---

## Implementation methods

### PHP format

```php
// contao/languages/en/default.php
$GLOBALS['TL_LANG']['MSC']['goBack'] = 'Back';
$GLOBALS['TL_LANG']['MSC']['readMore'] = ['Read more …', 'Read the full article.'];
```

### XLIFF format

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

## Symfony integration (Contao 5.3 and later)

From version 5.3 onwards, Symfony translation formats can be used with the `contao_` prefix:

### YAML format

```yaml
# translations/contao_default.en.yaml
MSC:
    goBack: Return back
    readMore:
        - Read more …
        - Read the full article.
```

### Other domains

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

## Retrieving translations

### Symfony Translator (recommended)

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

### In PHP templates

```php
<?= $this->trans('MSC.goBack') ?>
<?= $this->trans('MSC.readMore', [], 'contao_default') ?>
```

### In Twig templates

```twig
{{ 'MSC.goBack'|trans({}, 'contao_default') }}

{# With a default domain #}
{% trans_default_domain 'contao_default' %}
{{ 'MSC.goBack'|trans }}
```

---

## Finding translation keys

Because keys and domains can often only be found in the source code:

1. Use the Symfony debug tools (`debug:translation`)
2. Debug `$GLOBALS['TL_LANG']`
3. Search the Contao core code in `vendor/contao/*/contao/languages/en/`

---

## Custom translations in bundles

Directory structure:

```
contao/
└── languages/
    ├── en/
    │   ├── default.php (or .xlf)
    │   ├── tl_my_table.php
    │   └── modules.php
    └── de/
        ├── default.php
        └── tl_my_table.php
```

From Contao 5.3 onwards, alternatively:

```
translations/
├── contao_default.en.yaml
├── contao_default.de.yaml
├── contao_tl_my_table.en.yaml
└── contao_modules.en.yaml
```

---

## Common translation keys

### Back end module labels

```php
// contao/languages/en/modules.php
$GLOBALS['TL_LANG']['MOD']['my_module'] = ['My Module', 'Manage my records.'];
```

### DCA fields

```php
// contao/languages/en/tl_my_table.php
$GLOBALS['TL_LANG']['tl_my_table']['name'] = ['Name', 'Enter the name here.'];
$GLOBALS['TL_LANG']['tl_my_table']['edit'] = ['Edit record ID %s', ''];
```

### Content element types

```php
// contao/languages/en/default.php
$GLOBALS['TL_LANG']['CTE']['my_element'] = ['My Element', 'A custom content element.'];
```

---

*Source: https://docs.contao.org/5.x/dev/framework/translations/*  
*https://docs.contao.org/5.x/dev/getting-started/translations/*
