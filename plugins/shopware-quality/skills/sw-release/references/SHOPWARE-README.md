# Shopware 6 plugin README generator

You generate and update README.md files for Shopware 6 plugins. **The README is written in German** — it addresses the shop operator, not the developer, and it is the one file exempt from the English-only rule. It uses **GitLab-flavored Markdown**.

**Encoding:** write the file as UTF-8. Where a product name, a backend label or example data carries an accented character, keep the character itself — never transliterate it away.

---

## Contents

- [Workflow](#workflow)
- [README structure](#readme-structure)
- [Description](#description)
- [System requirements](#system-requirements)
- [Composer dependencies](#composer-dependencies)
- [Plugin configuration](#plugin-configuration)
- [CMS](#cms)
- [Administration modules](#administration-modules)
- [Subscriber](#subscriber)
- [Commands](#commands)
- [Flows & Rules](#flows-rules)
- [Entities](#entities)
- [Custom fields](#custom-fields)
- [Services](#services)
- [Tasks / MessageQueue](#tasks-messagequeue)
- [Twig extensions](#twig-extensions)
- [Logging](#logging)
- [Tests and code quality](#tests-and-code-quality)
- [Changelog](#changelog)
- [Anti-patterns — what must NOT be done](#anti-patterns--what-must-not-be-done)
- [Updating an existing README](#updating-an-existing-readme)
- [Examples of good output](#examples-of-good-output)
- [Description](#description-1)
- [Plugin configuration](#plugin-configuration-1)
- [Entities](#entities-1)
- [Custom fields](#custom-fields-1)
- [Commands](#commands-1)
- [Tasks / MessageQueue](#tasks-messagequeue)

## Workflow

### Step 1: locate the plugin directory

Check whether the current or given directory holds a `composer.json` with `"type": "shopware-platform-plugin"`. Where it does not, ask the user for the path to the plugin.

### Step 2: load the GitLab Markdown reference

Fetch the GitLab Markdown reference:

```
WebFetch: https://docs.gitlab.com/user/markdown/
```

Use it for the exact syntax of tables, collapsible sections, the table of contents and embedded images.

### Step 3: full codebase analysis

Read and analyse **EVERY** file below, systematically. Skip none of them.

**Mandatory files, always read:**

| File | Purpose |
|:------|:------|
| `composer.json` | name, description, PHP version, Shopware version (from `conflict`), dependencies |
| `src/{PluginName}.php` | the main class, the install, uninstall, update and activate hooks, custom-field registrations |

**Conditional files, read only where present:**

| File | Purpose |
|:------|:------|
| `src/Resources/config/config.xml` | plugin configuration |
| `src/Resources/config/services.php` and `src/Resources/config/services/*.php` | registered services and tags (the current standard — PHP, not XML) |
| `src/Resources/config/services.xml`, `subscribers.xml`, `commands.xml`, `tasks.xml`, `fixtures.xml` | the same, in existing plugins not yet migrated off XML |
| `src/Resources/config/packages/monolog.yaml` | logger configuration |
| `docs/plugin.png` | the plugin image — check it exists, do not read it |
| `rector.php` | Rector configuration |
| `psalm.xml` | Psalm configuration |
| `ecs.php` | ECS configuration |
| `.phpcs.xml` | PHPCS configuration |
| `cliff.toml` | git-cliff configuration |

**Directory scans, reading every PHP, JS, Vue and Twig file:**

| Directory | Contents |
|:------------|:-------|
| `src/Command/` | CLI commands |
| `src/Core/Content/` | entity definitions, translations, collections |
| `src/DataResolver/` | CMS data resolvers |
| `src/Enum/` | Enums |
| `src/Fixtures/` | fixtures (mail templates, custom fields and so on) |
| `src/Migration/` | database migrations, for the entity structure |
| `src/Service/` | Services |
| `src/Storefront/Controller/` | storefront controllers |
| `src/Struct/` | data structs |
| `src/Subscriber/` | event subscribers |
| `src/Task/` | scheduled tasks and message queue handlers |
| `src/Twig/` | Twig extensions (filters, functions) |
| `src/Resources/app/administration/` | admin modules and CMS components |
| `src/Resources/app/storefront/` | storefront JS and SCSS |
| `src/Resources/views/` | Twig templates |
| `src/Resources/snippet/` | snippet files |

### Step 4: generate the README

Generate the README.md to the structure defined below. **A section that does not apply is left out entirely** — no empty heading, and no "not present" note.

### Step 5: write the README

Write the generated README.md into the plugin root. Where a README.md already exists, read it first and keep the sections somebody added by hand (Known issues, FAQ, Notes and the like).

---

## README structure

The README follows **exactly this order**. A section is included only where the plugin has the files or features it describes.

---

### 1. Badges, title and table of contents

**shields.io badges go at the very top of the README, BEFORE the main title.** Derive them from `composer.json`, and from `package.json` where that exists.

```markdown
![Shopware](https://img.shields.io/badge/Shopware-{version}-blue)
![PHP](https://img.shields.io/badge/PHP-{php-version}-brightgreen)
![Node](https://img.shields.io/badge/Node-{node-version}-brightgreen)
[![License](https://img.shields.io/badge/License-{licence}-yellow)](LICENSE)

# {Human-readable plugin name} for Shopware {version}

[[_TOC_]]
```

**Rules for the badges:**

- **Shopware badge:** derive the version from `composer.json` → `conflict` → `shopware/core` (e.g. `6.7`, `6.6 - 6.7`)
- **PHP badge:** the version from `composer.json` → `require` → `php` (e.g. `>=8.3`, `8.1 || 8.2 || 8.3`)
- **Node-Badge:** Version aus `package.json` → `engines` → `node` ableiten. Wenn keine `package.json` existiert oder keine Node-Version angegeben ist → Badge weglassen
- **Licence badge:** derive it from `composer.json` → `license` (e.g. `MIT`, `proprietary`). Where a `LICENSE` file exists, make the badge link to it. Where there is no licence field, leave the badge out
- Special characters in a badge value have to be URL-encoded: a space becomes `%20`, `||` becomes `%7C%7C`, `>=` becomes `%3E%3D`, `|` becomes `%7C`
- Farben: Shopware = `blue`, PHP = `brightgreen`, Node = `brightgreen`, Lizenz = `yellow`
- The badges **always** sit on a line of their own at the very top of the file, followed by a blank line before the `#` title

**Example with every badge:**

```markdown
![Shopware](https://img.shields.io/badge/Shopware-6.7-blue)
![PHP](https://img.shields.io/badge/PHP-%3E%3D%208.3-brightgreen)
![Node](https://img.shields.io/badge/Node-18.0.0-brightgreen)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

# Sitemap for Shopware 6.7
```

**Example without Node and without a licence:**

```markdown
![Shopware](https://img.shields.io/badge/Shopware-6.6%20--%206.7-blue)
![PHP](https://img.shields.io/badge/PHP-8.1%20%7C%7C%208.2%20%7C%7C%208.3-brightgreen)

# Review emails for Shopware 6.6 - 6.7
```

**Rules for the title:**

- **NICHT** den technischen Klassennamen verwenden (FALSCH: "FfContentSitemap")
- Name what the plugin is for instead: "Sitemap", "CMS content blocks", "Review emails"
- Shopware-Version aus `composer.json` → `conflict` → `shopware/core` ableiten
- Example: a conflict of `"<6.7 || >=6.8"` gives "for Shopware 6.7"
- Example: a conflict of `"<6.6 || >=6.8"` gives "for Shopware 6.6 - 6.7"

---

### 2. Plugin-Bild

**Nur wenn `docs/plugin.png` existiert.** Direkt unter den Titel.

**Measure the image and scale it proportionally:**

1. Read the original dimensions from the shell:
   ```bash
   sips -g pixelWidth -g pixelHeight docs/plugin.png
   ```
   Where `sips` is unavailable, use `identify` (ImageMagick) or `file`.

2. Scale proportionally so that **neither width nor height exceeds 500px**:
   - Berechne den Skalierungsfaktor: `factor = min(500/width, 500/height, 1.0)`
   - Neue Breite: `round(width * factor)`
   - New height: `round(height * factor)`
   - Where the image is already smaller than 500x500, keep its original dimensions.

3. Bild im **GitLab-Markdown-Format** einbetten:

```markdown
![image](docs/plugin.png){width={computed_width} height={computed_height}}
```

**Beispiel:** Originalbild 604x988 → Faktor `min(500/604, 500/988)` = 0.506 → `width=306 height=500`

---

### 3. Beschreibung

```markdown
## Beschreibung

{A clear, concise description of what the plugin does and what it is for.
Two to four sentences, based on the actual code analysis — do NOT simply copy the composer.json description.
Describe the full scope of what it does.}
```

---

### 4. Systemanforderungen

```markdown
## Systemanforderungen

| Anforderung | Version |
|:------------|:--------|
| PHP         | {php-version aus require, z.B. ">= 8.3"} |
| Shopware    | {version aus conflict, z.B. "6.7.x"} |
```

List any further requirements (`ext-curl`, `ext-json` and so on) where `require` names them.

---

### 5. Composer dependencies

Two separate tables. PHP itself and the PHP extensions are **not** repeated here.

```markdown
## Composer dependencies

### Dependencies

| Paket | Version |
|:------|:--------|
| {package-name} | {version-constraint} |

### Development dependencies

| Paket | Version |
|:------|:--------|
| {package-name} | {version-constraint} |
```

- Where `require` holds only `php` and extensions, leave the "Dependencies" subtable out
- Where `require-dev` is empty, leave the "Development dependencies" subtable out

---

### 6. Pluginkonfiguration

**Nur wenn `src/Resources/config/config.xml` existiert.**

```markdown
## Pluginkonfiguration

Die Konfiguration ist erreichbar unter **Erweiterungen → Meine Erweiterungen → {Plugin-Name} → Konfiguration**.

### {Card-Titel (deutsch)}

| Feld | Technischer Name | Typ | Beschreibung | Standardwert |
|:-----|:-----------------|:----|:-------------|:-------------|
| {Label DE} | `{name}` | {Typ} | {helpText DE oder abgeleitete Beschreibung} | `{defaultValue}` |
```

**For a select field**, list its options as well:

```markdown
#### Options for "{field name}"

| Wert | Bezeichnung |
|:-----|:------------|
| `{value}` | {Label DE} |
```

**For a custom component** (e.g. `<component name="my-component">`), say what the component does and which choices it offers.

**Analysis checklist for config.xml:**

- Extract every `<card>` with its title
- Alle Feld-Typen erfassen: `<input-field>`, `<select>`, `<single-select>`, `<multi-select>`, `<bool>`, `<int>`, `<float>`, `<text>`, `<textarea>`, `<colorpicker>`, `<datetime>`, `<entity>`, `<component>`
- `<label lang="de-DE">` bevorzugen, Fallback auf `<label lang="en-GB">`
- `<helpText lang="de-DE">` als Beschreibung nutzen
- `<defaultValue>` dokumentieren
- For a select field, list every `<option>` with its `<value>` and `<label>`
- `<placeholder>` dokumentieren wenn vorhanden
- For a large configuration, use `<details>` collapsible sections

---

### 7. CMS

**Only where CMS blocks or CMS elements exist.** Standalone administration modules do NOT belong here.

```markdown
## CMS

### CMS blocks

| Block | Kategorie | Elemente | Beschreibung |
|:------|:----------|:---------|:-------------|
| {block-name} | {category, e.g. "text-image"} | {the slots and elements it loads} | {what the block is for} |
```

```markdown
### CMS Elemente

#### {Element-Name}

{A full description: what the element does, what it is for, what it renders.}

##### Konfiguration

| Option | Technischer Name | Typ | Beschreibung | Standardwert |
|:-------|:-----------------|:----|:-------------|:-------------|
| {Label} | `{name}` | {type} | {what the option does} | `{default}` |
```

**For every element with a data resolver of its own:**

```markdown
##### DataResolver: {ResolverClassName}

{Exactly what the data resolver does, and which data it loads and prepares.}

**Datenausgabe:**

| Zugriff | Pfad | Beschreibung |
|:--------|:-----|:-------------|
| Data | `element.data.{key}` | {what is available here} |
| Konfiguration | `element.config.{key}.value` | {Konfigurationswerte} |

**Zugriff in Twig:**

```twig
{# Daten abrufen #}
{% set myData = element.data.{property} %}
{{ myData.name }}

{# Konfiguration abrufen #}
{% set config = element.config.{key}.value %}
```

**Analysis checklist for CMS:**

- Admin-Komponenten in `src/Resources/app/administration/src/module/sw-cms/` durchsuchen
- Block-Registrierungen in `index.js` Dateien finden (Kategorie, Slots)
- Element-Konfigurationen aus `config/index.js` extrahieren
- DataResolver-Klassen in `src/DataResolver/` analysieren: `getType()`, `enrich()`, `collect()` Methoden
- Read the struct classes in `src/Struct/` for the data structure
- Check the Twig templates in `src/Resources/views/storefront/element/` for access examples
- Check the storefront components in `src/Resources/app/storefront/`

---

### 8. Administrationsmodule

**Only where the plugin has admin modules of its own** (in `src/Resources/app/administration/src/module/`, but NOT `sw-cms`, which belongs to section 7).

```markdown
## Administrationsmodule

### {Modul-Name}

**Menu path:** {where the module sits in the admin, e.g. "Content → {module name}"}

{A full description: what the module does and which functions it offers.}

| Einstellung/Funktion | Beschreibung | Auswirkung |
|:---------------------|:-------------|:-----------|
| {name} | {what can be set or done here} | {what happens when it is used} |
```

**Analyse-Checkliste:**

- `src/Resources/app/administration/src/module/` durchsuchen (OHNE `sw-cms`)
- Check `index.js` for the module registrations (route, navigation, privileges)
- Alle Vue-Komponenten des Moduls analysieren
- Take the labels and descriptions from the snippet files

---

### 9. Subscriber

**Only where `src/Subscriber/` exists and holds subscribers.**

```markdown
## Subscriber

### {SubscriberClassName}

{Briefly, what this subscriber is responsible for.}

| Event | Methode | Beschreibung |
|:------|:--------|:-------------|
| `{EventClass::EVENT_NAME}` | `{methodName}()` | {what the method actually does} |
```

**Analyse-Checkliste:**

- `getSubscribedEvents()` auswerten
- Read every event handler method and state its purpose
- Give the event class with its full namespace, or its well-known short name

---

### 10. Commands

**Only where `src/Command/` exists and holds commands.**

```markdown
## Commands

### `{command:name}`

{A full description of what the command does.}

**Argumente:**

| Argument | Beschreibung | Pflicht |
|:---------|:-------------|:--------|
| `{name}` | {what the argument is for} | Yes / No |

**Optionen:**

| Option | Kurzform | Beschreibung | Standardwert |
|:-------|:---------|:-------------|:-------------|
| `--{name}` | `-{shortcut}` | {what the option does} | `{default}` |

**Beispiel:**

```bash
bin/console {command:name} {praxisnahe-beispiel-argumente}
```

**Analyse-Checkliste:**

- `configure()` Methode: Command-Name, Beschreibung, Argumente, Optionen extrahieren
- The `execute()` method: describe what it actually does
- Praxisnahe Beispielaufrufe konstruieren
- Wenn keine Argumente → Argumente-Tabelle weglassen
- Wenn keine Optionen → Optionen-Tabelle weglassen

---

### 11. Flows & Rules

**Nur wenn Flow-Actions oder Custom Rules existieren.**

```markdown
## Flows & Rules

### Flow Actions

| Action | Trigger | Beschreibung |
|:-------|:--------|:-------------|
| `{ActionName}` | {the event that triggers it} | {what the action does} |

### Rules

| Rule | Beschreibung | Konfiguration |
|:-----|:-------------|:--------------|
| `{RuleName}` | {when the rule applies} | {its configurable parameters} |
```

---

### 12. Entities

**Nur wenn Entity-Definitionen in `src/Core/Content/` existieren.**

```markdown
## Entities

### {EntityName} (`{tabellen_name}`)

{Briefly, what this entity is used for.}

#### Felder

| Feld | Typ | Beschreibung | Standard | Pflicht |
|:-----|:----|:-------------|:---------|:--------|
| `{fieldName}` | `{FieldType}` | {what the field is for} | `{defaultValue}` | Yes / No |

#### Assoziationen

| Assoziation | Typ | Ziel-Entity | Beschreibung |
|:------------|:----|:------------|:-------------|
| `{name}` | {ManyToOne / OneToMany / ManyToMany} | `{TargetDefinition}` | {what the association is for} |
```

Where the entity has a translation:

```markdown
#### Translatable fields

| Feld | Typ | Beschreibung |
|:-----|:----|:-------------|
| `{fieldName}` | `{FieldType}` | {Beschreibung} |
```

**Analyse-Checkliste:**

- Read `defineFields()` in full
- Feld-Typen korrekt benennen: `IdField`, `StringField`, `BoolField`, `IntField`, `FloatField`, `DateTimeField`, `JsonField`, `FkField`, `LongTextField`, `TextField` etc.
- Flags beachten: `AllowHtml`, `Required`, `PrimaryKey`, `Inherited`
- Translations-Entity (`*TranslationDefinition`) separat dokumentieren
- Derive the default values from `defineFields()` and the migrations
- Take the table structure and constraints from the migrations

---

### 13. Custom fields and custom field sets

**IMPORTANT:** write **"custom field(s)"** and **"custom field set(s)"**, matching the terms the administration uses.

**Only where the plugin registers custom fields or custom field sets.**

```markdown
## Freitextfelder

### Freitextfeldset: {Menschenlesbarer Set-Name}

**Technischer Name:** `{technical_set_name}`
**Zugeordnete Entities:** {entity1}, {entity2}

| Freitextfeld | Technischer Name | Typ | Beschreibung |
|:-------------|:-----------------|:----|:-------------|
| {Label} | `{technical_name}` | {type: text, bool, int, float, select, …} | {what the field stores} |
```

For a select custom field, additionally:

```markdown
#### Options for "{field name}"

| Wert | Bezeichnung |
|:-----|:------------|
| `{value}` | {Label DE} |
```

Immer den Twig-Zugriff dokumentieren:

```markdown
**Zugriff in Twig:**

```twig
{# Storefront #}
{{ product.customFields.{technical_name} }}

{# check whether the custom field is set #}
{% if product.customFields.{technical_name} is defined and product.customFields.{technical_name} is not empty %}
    {{ product.customFields.{technical_name} }}
{% endif %}
```

**Analyse-Checkliste:**

- Check the main class (`{PluginName}.php`) for `install()`, `update()` and `activate()`
- Find the custom field set registrations through `customFieldSetRepository`
- Check the fixtures directory for custom-field definitions
- Read the service classes that manage custom fields (e.g. `CustomFieldService`)
- Document every field with its type, options and the entity relations it is bound to

---

### 14. Services

**Only where `src/Service/` exists and holds services with public methods.**

```markdown
## Services

### {ServiceClassName}

{Briefly, what the service is responsible for.}

| Method | Parameters | Returns | Description |
|:--------|:----------|:---------|:-------------|
| `{methodName}()` | `{Type} $name` | `{ReturnType}` | {what the method does} |
```

**Analyse-Checkliste:**

- Document **public** methods only
- `__construct()` NICHT dokumentieren
- Give each parameter with its type
- Take return types from the type declarations or PHPDoc
- Abstrakte Klassen als solche kennzeichnen

---

### 15. Tasks / MessageQueue

**Nur wenn `src/Task/` existiert oder ScheduledTasks/MessageQueue-Handler vorhanden sind.**

```markdown
## Tasks / MessageQueue

### {TaskName}

{What the task does and what it is for.}

| Eigenschaft | Wert |
|:------------|:-----|
| Task name | `{the getTaskName() return value}` |
| Intervall | {Sekunden} ({menschenlesbar, z.B. "alle 24 Stunden"}) |
| Handler | `{HandlerClassName}` |
| Description | {what the handler actually does when it runs} |
```

**Analyse-Checkliste:**

- `getTaskName()` and `getDefaultInterval()` from the ScheduledTask class
- `run()` oder `__invoke()` Methode des Handlers analysieren
- Convert the interval to something readable: 3600 is hourly, 86400 daily, 604800 weekly

---

### 16. Twig-Erweiterungen

**Only where `src/Twig/` exists and holds Twig extensions.**

```markdown
## Twig-Erweiterungen

### Filter

| Filter | Beschreibung | Beispiel |
|:-------|:-------------|:---------|
| `{filterName}` | {what the filter does} | `{{ variable \| {filterName} }}` |

### Funktionen

| Funktion | Parameter | Beschreibung | Beispiel |
|:---------|:----------|:-------------|:---------|
| `{functionName}` | `{parameter1}, {parameter2}` | {what the function does} | `{{ {functionName}(param1, param2) }}` |
```

**Analyse-Checkliste:**

- Read the `getFilters()` and `getFunctions()` methods
- Per filter and function: name, parameters, return value, purpose
- Praxisnahe Twig-Beispiele erstellen
- Where there are only filters, leave the "Functions" section out, and the other way round

---

### 17. Logging

**Nur wenn `src/Resources/config/packages/monolog.yaml` existiert.**

```markdown
## Logging

| Eigenschaft | Wert |
|:------------|:-----|
| Log-Datei | `var/log/{dateiname}.log` |
| Log-Level | {level, z.B. "debug", "info", "warning"} |
| Channel | `{channel-name}` |
| Rotation | {Ja/Nein — wenn ja: max. {max_files} Dateien} |
| Typ | {Handler-Typ, z.B. "rotating_file", "stream"} |
```

---

### 18. Tests and code quality

**Only where at least one of those configuration files exists.** List only the tools actually presnden sind.

```markdown
## Tests and code quality
```

**Rector** (wenn `rector.php` existiert):

```markdown
### Rector

Rector checks PHP code and updates it automatically to modern syntax and Shopware conventions.

| Einstellung | Wert |
|:------------|:-----|
| PHP-Version | {PHP-Set aus rector.php, z.B. "PHP 8.3"} |
| Shopware-Set | {Shopware-Set, z.B. "SHOPWARE_6_7_0"} |

```bash
# check only (dry run)
vendor/bin/rector process --dry-run

# apply the changes
vendor/bin/rector process --clear-cache
```

Where `composer.json` defines scripts for rector (e.g. `"rector": "vendor/bin/rector process --dry-run"`), use those composer scripts instead:

```markdown
```bash
# check only (dry run)
composer run rector

# apply the changes
vendor/bin/rector process --clear-cache
```

**Psalm** (wenn `psalm.xml` existiert):

```markdown
### Psalm

Static analysis, to find type errors and potential bugs.

| Einstellung | Wert |
|:------------|:-----|
| Level | {errorLevel aus psalm.xml} |
| PHP-Version | {phpVersion aus psalm.xml} |

```bash
composer run psalm
```

**The gate** (whenever `composer.json` declares a `gate` script — it should):

```markdown
### Quality gate

One command runs the fixers and then every check: php-cs-fixer, PHPStan at `level: max`,
Rector, the phpat architecture rules, Stylelint and the unit tests.

```bash
# fix, then check
composer gate

# check only
composer gate:check
```

**PHPCS** (wenn `.phpcs.xml` existiert):

```markdown
### PHPCS (PHP CodeSniffer)

Checks code formatting against the defined standards.

```bash
composer run phpcs
```

**Analyse-Checkliste:**

- `rector.php` lesen: verwendete Sets (`SetList::PHP_*`, `ShopwareSetList::*`), Skip-Regeln
- `psalm.xml` lesen: `errorLevel`, `phpVersion`
- Read `ecs.php`: the sets and rules in use
- Read `.phpcs.xml`: the standard and its rules
- Read the `scripts` section of `composer.json` for the exact commands to run

---

### 19. Changelog

**Nur wenn `cliff.toml` existiert.**

```markdown
## Changelog

The changelog is generated with [git-cliff](https://git-cliff.org/):

```bash
git cliff --tag X.Y.Z --output CHANGELOG.md
```

Replace `X.Y.Z` with the version number you want.
```

---

## Anti-patterns — what must NOT be done

| Nr. | Anti-Pattern | Richtig |
|:----|:-------------|:--------|
| 1 | Using the technical class name as the title ("# FfContentSitemap") | Use a human-readable name ("# Sitemap for Shopware 6.7") |
| 2 | Leere Sektionen anzeigen ("## Commands — Keine vorhanden") | Sektion komplett weglassen |
| 3 | Writing "Customfield" or "CustomFieldSet" | Write "custom field" and "custom field set" |
| 4 | Mixing languages in headings or descriptions | Everything in English (technical terms such as "Entity", "DataResolver", "Subscriber" sind erlaubt) |
| 5 | Copying the composer.json description verbatim | Base the description on the code analysis, describing what it actuahlichen Funktionsumfang |
| 6 | Listing admin modules under CMS | CMS means CMS blocks and elements; admin modules are standalone |
| 7 | Documenting private or protected service methods | Document the public API only |
| 8 | Giving an interval in seconds only | Always convert it (86400 seconds is daily) |
| 9 | Standard Markdown instead of GitLab Markdown | `[[_TOC_]]` for the table of contents, `<details>` for a collapsible Sections |
| 10 | Guessing at or inventing a missing file | Where a file does not exist, leave its section out |
| 11 | Documenting `__construct()` as a service method | A constructor is not public API |
| 12 | A CMS section for a pure admin extension | CMS refers only to CMS blocks and CMS elemente |
| 13 | Ignoring what an existing README holds | On an update, keep the sections added by hand |
| 14 | Transliterating an accented character in a name or label | Keep the character itself, and write the file as UTF-8 |

---

## Updating an existing README

Wenn eine README.md bereits existiert:

1. Read the existing README **first**
2. Analysiere den gesamten Plugin-Code (wie bei Neuerstellung)
3. Compare what it holds against the code you analysed
4. Update every section — drop what is obsolete, add what is new
5. **Keep the sections added by hand** that this generator does not produce (Known issume", "FAQ", "Hinweise", "Mitwirkende")
6. Tell the user what changed substantially

---

## Examples of good output

### Example: badges and a title with an image

```markdown
![Shopware](https://img.shields.io/badge/Shopware-6.7-blue)
![PHP](https://img.shields.io/badge/PHP-%3E%3D%208.3-brightgreen)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

# Sitemap for Shopware 6.7

[[_TOC_]]

![image](docs/plugin.png){width=306 height=500}

## Beschreibung

This plugin generates an XML sitemap for every sales channel, covering
products, categories and CMS pages. The sitemap can be rebuilt through a CLI command
either by hand or automatically through a scheduled task.
```

### Example: plugin configuration with select options

```markdown
## Pluginkonfiguration

Die Konfiguration ist erreichbar unter **Erweiterungen → Meine Erweiterungen → Shopvote → Konfiguration**.

### Allgemein

| Feld | Technischer Name | Typ | Beschreibung | Standardwert |
|:-----|:-----------------|:----|:-------------|:-------------|
| Active | `active` | bool | switches the review requests on | `true` |
| API key | `apiKey` | text | the Shopvote API key used to authenticate | _(empty)_ |
| Dispatch time | `sendDelay` | single select | when the review request is sent | `7_days` |

#### Options for "Dispatch time"

| Wert | Bezeichnung |
|:-----|:------------|
| `immediately` | Sofort |
| `3_days` | Nach 3 Tagen |
| `7_days` | Nach 7 Tagen |
| `14_days` | Nach 14 Tagen |
```

### Example: an entity with a translation

```markdown
## Entities

### Retailer (`ff_retailer`)

Stores dealer locations for the dealer search, with address data and geo coordinates.

#### Felder

| Feld | Typ | Beschreibung | Standard | Pflicht |
|:-----|:----|:-------------|:---------|:--------|
| `id` | `IdField` | the primary key | _(auto)_ | Yes |
| `name` | `StringField` | the dealer name (translatable) | — | Yes |
| `street` | `StringField` | street | — | Yes |
| `zip` | `StringField` | Postleitzahl | — | Nein |
| `city` | `StringField` | Stadt | — | Ja |
| `latitude` | `FloatField` | Breitengrad | — | Nein |
| `longitude` | `FloatField` | longitude | — | No |
| `active` | `BoolField` | whether the dealer is active | `true` | No |

#### Translatable fields

| Feld | Typ | Beschreibung |
|:-----|:----|:-------------|
| `name` | `StringField` | the dealer name |
| `description` | `LongTextField` | the dealer description |
```

### Beispiel: Freitextfelder

```markdown
## Freitextfelder

### Freitextfeldset: Shopvote Bewertungsdaten

**Technischer Name:** `ff_shopvote_evaluation`
**Zugeordnete Entities:** order

| Freitextfeld | Technischer Name | Typ | Beschreibung |
|:-------------|:-----------------|:----|:-------------|
| Review request sent | `ff_shopvote_evaluation_sent` | bool | whether a review request has been sent for this order |
| Sent at | `ff_shopvote_evaluation_sent_at` | datetime | when the review request was sent |

**Zugriff in Twig:**

```twig
{% if order.customFields.ff_shopvote_evaluation_sent %}
    Bewertungsanfrage gesendet am: {{ order.customFields.ff_shopvote_evaluation_sent_at|date('d.m.Y H:i') }}
{% endif %}
```

### Beispiel: Command

```markdown
## Commands

### `ff:shopvote:send-mail`

Versendet Bewertungsanfragen per E-Mail an Kunden deren Bestellung abgeschlossen wurde.

**Optionen:**

| Option | Kurzform | Beschreibung | Standardwert |
|:-------|:---------|:-------------|:-------------|
| `--dry-run` | — | Simuliert den Versand ohne E-Mails zu senden | `false` |
| `--limit` | `-l` | Maximale Anzahl zu versendender E-Mails | `100` |

**Beispiel:**

```bash
# Normaler Versand
bin/console ff:shopvote:send-mail

# a test run with a limit
bin/console ff:shopvote:send-mail --dry-run --limit 10
```

### Beispiel: Scheduled Task

```markdown
## Tasks / MessageQueue

### SendEvaluationRequestMailTask

Versendet automatisch Bewertungsanfragen an Kunden nach Abschluss ihrer Bestellung.

| Eigenschaft | Wert |
|:------------|:-----|
| Task-Name | `ff_shopvote.send_evaluation_request_mail` |
| Interval | 86400 seconds (daily) |
| Handler | `SendEvaluationRequestMailTaskHandler` |
| Description | finds orders whose review window has passed and sends the review request emails |
```

### Example: a collapsible section for a large configuration

```markdown
<details>
<summary>Erweiterte CMS Element-Konfiguration anzeigen</summary>

#### Hero Slider Konfiguration

| Option | Technischer Name | Typ | Beschreibung | Standardwert |
|:-------|:-----------------|:----|:-------------|:-------------|
| Autoplay | `autoplay` | bool | the slider advances to the next slide on its own | `true` |
| Geschwindigkeit | `speed` | Int | Wechselgeschwindigkeit in Millisekunden | `5000` |
| Show navigation | `showNavigation` | bool | show the previous and next arrows | `true` |
| Pagination anzeigen | `showPagination` | Bool | Punkt-Indikatoren anzeigen | `true` |

</details>
```