---
name: shopware-readme
description: >
  Generiert und aktualisiert README.md-Dateien für Shopware 6 Plugins nach einem einheitlichen Schema.
  Verwende diesen Skill wenn der User eine README erstellen, aktualisieren oder generieren möchte,
  "README schreiben", "Plugin dokumentieren", "Dokumentation erstellen", "readme.md" oder ähnliche
  Anfragen stellt. Triggert auch bei "Beschreibe das Plugin" oder "Was macht das Plugin?" im Kontext
  eines Plugin-Verzeichnisses.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - Agent
---

# Shopware 6 Plugin README-Generator

Du generierst und aktualisierst README.md-Dateien für Shopware 6 Plugins. Die README wird **immer auf Deutsch** verfasst und verwendet **GitLab-flavored Markdown**.

**Umlaute und Sonderzeichen:** Verwende **immer** korrekte deutsche Umlaute und Sonderzeichen: ä, ö, ü, Ä, Ö, Ü, ß. Niemals Umschreibungen wie ae, oe, ue, ss verwenden. Dies gilt für alle Texte in der README — Überschriften, Beschreibungen, Tabellen und Codekommentare. Achte besonders darauf, dass Umlaute beim Schreiben und Bearbeiten der Datei nicht durch falsche Kodierung verfälscht werden (UTF-8 sicherstellen).

---

## Workflow

### Schritt 1: Plugin-Verzeichnis ermitteln

Prüfe, ob im aktuellen oder angegebenen Verzeichnis eine `composer.json` mit `"type": "shopware-platform-plugin"` vorhanden ist. Falls nicht, frage den User nach dem Pfad zum Plugin.

### Schritt 2: GitLab Markdown-Referenz laden

Lade die GitLab Markdown-Referenz über WebFetch:

```
WebFetch: https://docs.gitlab.com/user/markdown/
```

Nutze diese Referenz für korrekte Syntax bei Tabellen, Collapsible Sections, Table of Contents und Image-Embedding.

### Schritt 3: Vollständige Codebase-Analyse

Lies und analysiere **ALLE** folgenden Dateien systematisch. Überspringe keine Datei.

**Pflichtdateien (immer lesen):**

| Datei | Zweck |
|:------|:------|
| `composer.json` | Name, Beschreibung, PHP-Version, Shopware-Version (aus `conflict`), Abhängigkeiten |
| `src/{PluginName}.php` | Hauptklasse, install/uninstall/update/activate Hooks, CustomField-Registrierungen |

**Bedingte Dateien (nur lesen wenn vorhanden):**

| Datei | Zweck |
|:------|:------|
| `src/Resources/config/config.xml` | Pluginkonfiguration |
| `src/Resources/config/services.xml` | Registrierte Services, Tags |
| `src/Resources/config/subscribers.xml` | Subscriber-Registrierungen |
| `src/Resources/config/commands.xml` | Command-Registrierungen |
| `src/Resources/config/tasks.xml` | Task-Registrierungen |
| `src/Resources/config/fixtures.xml` | Fixture-Registrierungen |
| `src/Resources/config/packages/monolog.yaml` | Logger-Konfiguration |
| `docs/plugin.png` | Plugin-Bild (nur Existenz prüfen, nicht lesen) |
| `rector.php` | Rector-Konfiguration |
| `psalm.xml` | Psalm-Konfiguration |
| `ecs.php` | ECS-Konfiguration |
| `.phpcs.xml` | PHPCS-Konfiguration |
| `cliff.toml` | git-cliff Konfiguration |

**Verzeichnis-Scans (alle PHP/JS/Vue/Twig-Dateien lesen):**

| Verzeichnis | Inhalt |
|:------------|:-------|
| `src/Command/` | CLI-Befehle |
| `src/Core/Content/` | Entity-Definitionen, Translations, Collections |
| `src/DataResolver/` | CMS Data Resolver |
| `src/Enum/` | Enums |
| `src/Fixtures/` | Fixtures (Mail-Templates, CustomFields etc.) |
| `src/Migration/` | Datenbank-Migrationen (für Entity-Struktur) |
| `src/Service/` | Services |
| `src/Storefront/Controller/` | Storefront-Controller |
| `src/Struct/` | Daten-Structs |
| `src/Subscriber/` | Event-Subscriber |
| `src/Task/` | Scheduled Tasks / MessageQueue Handler |
| `src/Twig/` | Twig-Erweiterungen (Filter, Funktionen) |
| `src/Resources/app/administration/` | Admin-Module und CMS-Komponenten |
| `src/Resources/app/storefront/` | Storefront JS/SCSS |
| `src/Resources/views/` | Twig-Templates |
| `src/Resources/snippet/` | Snippet-Dateien |

### Schritt 4: README generieren

Generiere die README.md nach der unten definierten Struktur. **Sektionen die nicht zutreffen werden komplett weggelassen** — kein leerer Abschnitt, kein "nicht vorhanden"-Hinweis.

### Schritt 5: README schreiben

Schreibe die generierte README.md in das Plugin-Wurzelverzeichnis. Wenn eine README.md bereits existiert, lies sie vorher und behalte manuell hinzugefügte Sektionen bei (z.B. "Bekannte Probleme", "FAQ", "Hinweise").

---

## README-Struktur

Die README folgt **exakt diese Reihenfolge**. Jede Sektion wird nur aufgenommen wenn das Plugin entsprechende Dateien/Features enthält.

---

### 1. Badges, Titel und Inhaltsverzeichnis

**Ganz oben in der README — noch VOR dem Haupttitel — werden shields.io-Badges angezeigt.** Die Badges werden aus der `composer.json` und ggf. `package.json` abgeleitet.

```markdown
![Shopware](https://img.shields.io/badge/Shopware-{version}-blue)
![PHP](https://img.shields.io/badge/PHP-{php-version}-brightgreen)
![Node](https://img.shields.io/badge/Node-{node-version}-brightgreen)
[![License](https://img.shields.io/badge/License-{lizenz}-yellow)](LICENSE)

# {Menschenlesbarer Plugin-Name} für Shopware {Version}

[[_TOC_]]
```

**Regeln für Badges:**

- **Shopware-Badge:** Version aus `composer.json` → `conflict` → `shopware/core` ableiten (z.B. `6.7`, `6.6 - 6.7`)
- **PHP-Badge:** Version aus `composer.json` → `require` → `php` (z.B. `>=8.3`, `8.1 || 8.2 || 8.3`)
- **Node-Badge:** Version aus `package.json` → `engines` → `node` ableiten. Wenn keine `package.json` existiert oder keine Node-Version angegeben ist → Badge weglassen
- **Lizenz-Badge:** Aus `composer.json` → `license` ableiten (z.B. `MIT`, `proprietary`). Wenn eine `LICENSE`-Datei existiert, Badge als Link auf die Datei setzen. Wenn kein Lizenzfeld vorhanden → Badge weglassen
- Sonderzeichen in Badge-Werten müssen URL-encodiert werden: Leerzeichen → `%20`, `||` → `%7C%7C`, `>=` → `%3E%3D`, `|` → `%7C`
- Farben: Shopware = `blue`, PHP = `brightgreen`, Node = `brightgreen`, Lizenz = `yellow`
- Badges stehen **immer** auf einer eigenen Zeile direkt am Anfang der Datei, gefolgt von einer Leerzeile vor dem `#`-Titel

**Beispiel mit allen Badges:**

```markdown
![Shopware](https://img.shields.io/badge/Shopware-6.7-blue)
![PHP](https://img.shields.io/badge/PHP-%3E%3D%208.3-brightgreen)
![Node](https://img.shields.io/badge/Node-18.0.0-brightgreen)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

# Sitemap für Shopware 6.7
```

**Beispiel ohne Node und ohne Lizenz:**

```markdown
![Shopware](https://img.shields.io/badge/Shopware-6.6%20--%206.7-blue)
![PHP](https://img.shields.io/badge/PHP-8.1%20%7C%7C%208.2%20%7C%7C%208.3-brightgreen)

# Bewertungs-E-Mails für Shopware 6.6 - 6.7
```

**Regeln für den Titel:**

- **NICHT** den technischen Klassennamen verwenden (FALSCH: "FfContentSitemap")
- Stattdessen den Zweck des Plugins beschreiben: "Sitemap", "CMS Inhaltsblöcke", "Bewertungs-E-Mails"
- Shopware-Version aus `composer.json` → `conflict` → `shopware/core` ableiten
- Beispiel: Conflict `"<6.7 || >=6.8"` → "für Shopware 6.7"
- Beispiel: Conflict `"<6.6 || >=6.8"` → "für Shopware 6.6 - 6.7"

---

### 2. Plugin-Bild

**Nur wenn `docs/plugin.png` existiert.** Direkt unter den Titel.

**Bildmaße ermitteln und proportional skalieren:**

1. Ermittle die Originalmaße des Bildes per Bash:
   ```bash
   sips -g pixelWidth -g pixelHeight docs/plugin.png
   ```
   Falls `sips` nicht verfügbar ist, nutze `identify` (ImageMagick) oder `file`.

2. Skaliere proportional so, dass **weder Breite noch Höhe 500px überschreiten**:
   - Berechne den Skalierungsfaktor: `factor = min(500/width, 500/height, 1.0)`
   - Neue Breite: `round(width * factor)`
   - Neue Höhe: `round(height * factor)`
   - Wenn das Bild bereits kleiner als 500x500 ist, Originalmaße beibehalten.

3. Bild im **GitLab-Markdown-Format** einbetten:

```markdown
![image](docs/plugin.png){width={berechnete_breite} height={berechnete_höhe}}
```

**Beispiel:** Originalbild 604x988 → Faktor `min(500/604, 500/988)` = 0.506 → `width=306 height=500`

---

### 3. Beschreibung

```markdown
## Beschreibung

{Klare, prägnante Beschreibung was das Plugin macht und wofür man es nutzen kann.
2-4 Sätze. Basierend auf der tatsächlichen Code-Analyse — NICHT nur die composer.json description kopieren.
Den vollständigen Funktionsumfang beschreiben.}
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

Zusätzliche Anforderungen (z.B. `ext-curl`, `ext-json`) ebenfalls auflisten wenn in `require` vorhanden.

---

### 5. Composer-Abhängigkeiten

Zwei separate Tabellen. PHP und PHP-Extensions werden hier **nicht** nochmal aufgeführt.

```markdown
## Composer-Abhängigkeiten

### Abhängigkeiten

| Paket | Version |
|:------|:--------|
| {package-name} | {version-constraint} |

### Entwicklungs-Abhängigkeiten

| Paket | Version |
|:------|:--------|
| {package-name} | {version-constraint} |
```

- Wenn `require` nur `php` und Extensions enthält → Untertabelle "Abhängigkeiten" weglassen
- Wenn `require-dev` leer ist → Untertabelle "Entwicklungs-Abhängigkeiten" weglassen

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

**Bei Select-Feldern** zusätzlich die Optionen auflisten:

```markdown
#### Optionen für "{Feld-Name}"

| Wert | Bezeichnung |
|:-----|:------------|
| `{value}` | {Label DE} |
```

**Bei Custom-Komponenten** (z.B. `<component name="my-component">`) beschreiben was die Komponente macht und welche Auswahlmöglichkeiten sie bietet.

**Analyse-Checkliste für config.xml:**

- Jede `<card>` mit deutschem Titel extrahieren
- Alle Feld-Typen erfassen: `<input-field>`, `<select>`, `<single-select>`, `<multi-select>`, `<bool>`, `<int>`, `<float>`, `<text>`, `<textarea>`, `<colorpicker>`, `<datetime>`, `<entity>`, `<component>`
- `<label lang="de-DE">` bevorzugen, Fallback auf `<label lang="en-GB">`
- `<helpText lang="de-DE">` als Beschreibung nutzen
- `<defaultValue>` dokumentieren
- Bei Select-Feldern: alle `<option>` mit `<value>` und `<label lang="de-DE">` auflisten
- `<placeholder>` dokumentieren wenn vorhanden
- Für große Konfigurationen `<details>` Collapsible Sections verwenden

---

### 7. CMS

**Nur wenn CMS-Blöcke oder CMS-Elemente vorhanden sind.** Hier gehören KEINE eigenständigen Administrationsmodule hin!

```markdown
## CMS

### CMS Blöcke

| Block | Kategorie | Elemente | Beschreibung |
|:------|:----------|:---------|:-------------|
| {block-name} | {category, z.B. "text-image"} | {geladene Slots/Elemente} | {Wofür der Block gedacht ist} |
```

```markdown
### CMS Elemente

#### {Element-Name}

{Ausführliche Beschreibung: Was macht das Element, wofür kann man es nutzen, was stellt es dar.}

##### Konfiguration

| Option | Technischer Name | Typ | Beschreibung | Standardwert |
|:-------|:-----------------|:----|:-------------|:-------------|
| {Label} | `{name}` | {type} | {Was die Option bewirkt} | `{default}` |
```

**Für jedes Element mit eigenem DataResolver:**

```markdown
##### DataResolver: {ResolverClassName}

{Genaue Beschreibung was der DataResolver macht, welche Daten er lädt und aufbereitet.}

**Datenausgabe:**

| Zugriff | Pfad | Beschreibung |
|:--------|:-----|:-------------|
| Daten | `element.data.{key}` | {Was hier verfügbar ist} |
| Konfiguration | `element.config.{key}.value` | {Konfigurationswerte} |

**Zugriff in Twig:**

```twig
{# Daten abrufen #}
{% set myData = element.data.{property} %}
{{ myData.name }}

{# Konfiguration abrufen #}
{% set config = element.config.{key}.value %}
```
```

**Analyse-Checkliste für CMS:**

- Admin-Komponenten in `src/Resources/app/administration/src/module/sw-cms/` durchsuchen
- Block-Registrierungen in `index.js` Dateien finden (Kategorie, Slots)
- Element-Konfigurationen aus `config/index.js` extrahieren
- DataResolver-Klassen in `src/DataResolver/` analysieren: `getType()`, `enrich()`, `collect()` Methoden
- Struct-Klassen in `src/Struct/` analysieren für Datenstruktur
- Twig-Templates in `src/Resources/views/storefront/element/` für Zugriffsbeispiele prüfen
- Storefront-Komponenten in `src/Resources/app/storefront/` prüfen

---

### 8. Administrationsmodule

**Nur wenn eigene Admin-Module existieren** (in `src/Resources/app/administration/src/module/` — aber NICHT `sw-cms`, das gehört zu Sektion 7).

```markdown
## Administrationsmodule

### {Modul-Name}

**Menü-Pfad:** {Wo das Modul im Admin zu finden ist, z.B. "Inhalte → {Modul-Name}"}

{Ausführliche Beschreibung: Was macht das Modul, welche Funktionen bietet es.}

| Einstellung/Funktion | Beschreibung | Auswirkung |
|:---------------------|:-------------|:-----------|
| {name} | {Was man hier einstellen/tun kann} | {Was passiert wenn man es nutzt} |
```

**Analyse-Checkliste:**

- `src/Resources/app/administration/src/module/` durchsuchen (OHNE `sw-cms`)
- `index.js` für Modul-Registrierungen prüfen (Route, Navigation, Berechtigungen)
- Alle Vue-Komponenten des Moduls analysieren
- Snippet-Dateien für Labels und Beschreibungen heranziehen

---

### 9. Subscriber

**Nur wenn `src/Subscriber/` existiert und Subscriber enthält.**

```markdown
## Subscriber

### {SubscriberClassName}

{Kurze Beschreibung wofür dieser Subscriber zuständig ist.}

| Event | Methode | Beschreibung |
|:------|:--------|:-------------|
| `{EventKlasse::EVENT_NAME}` | `{methodName}()` | {Was die Methode konkret macht} |
```

**Analyse-Checkliste:**

- `getSubscribedEvents()` auswerten
- Jede Event-Handler-Methode analysieren und Zweck beschreiben
- Event-Klasse mit vollem Namespace oder bekanntem Shortname angeben

---

### 10. Commands

**Nur wenn `src/Command/` existiert und Commands enthält.**

```markdown
## Commands

### `{command:name}`

{Ausführliche Beschreibung was der Befehl macht.}

**Argumente:**

| Argument | Beschreibung | Pflicht |
|:---------|:-------------|:--------|
| `{name}` | {Wofür das Argument ist} | Ja / Nein |

**Optionen:**

| Option | Kurzform | Beschreibung | Standardwert |
|:-------|:---------|:-------------|:-------------|
| `--{name}` | `-{shortcut}` | {Was die Option bewirkt} | `{default}` |

**Beispiel:**

```bash
bin/console {command:name} {praxisnahe-beispiel-argumente}
```
```

**Analyse-Checkliste:**

- `configure()` Methode: Command-Name, Beschreibung, Argumente, Optionen extrahieren
- `execute()` Methode: Tatsächliche Funktionalität beschreiben
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
| `{ActionName}` | {Auslösendes Event} | {Was die Action macht} |

### Rules

| Rule | Beschreibung | Konfiguration |
|:-----|:-------------|:--------------|
| `{RuleName}` | {Wann die Regel greift} | {Konfigurierbare Parameter} |
```

---

### 12. Entities

**Nur wenn Entity-Definitionen in `src/Core/Content/` existieren.**

```markdown
## Entities

### {EntityName} (`{tabellen_name}`)

{Kurze Beschreibung wofür diese Entity genutzt wird.}

#### Felder

| Feld | Typ | Beschreibung | Standard | Pflicht |
|:-----|:----|:-------------|:---------|:--------|
| `{fieldName}` | `{FieldType}` | {Wofür das Feld ist} | `{defaultValue}` | Ja / Nein |

#### Assoziationen

| Assoziation | Typ | Ziel-Entity | Beschreibung |
|:------------|:----|:------------|:-------------|
| `{name}` | {ManyToOne / OneToMany / ManyToMany} | `{ZielDefinition}` | {Zweck der Assoziation} |
```

Wenn die Entity eine Übersetzung hat:

```markdown
#### Übersetzbare Felder

| Feld | Typ | Beschreibung |
|:-----|:----|:-------------|
| `{fieldName}` | `{FieldType}` | {Beschreibung} |
```

**Analyse-Checkliste:**

- `defineFields()` Methode vollständig auswerten
- Feld-Typen korrekt benennen: `IdField`, `StringField`, `BoolField`, `IntField`, `FloatField`, `DateTimeField`, `JsonField`, `FkField`, `LongTextField`, `TextField` etc.
- Flags beachten: `AllowHtml`, `Required`, `PrimaryKey`, `Inherited`
- Translations-Entity (`*TranslationDefinition`) separat dokumentieren
- Default-Werte aus `defineFields()` und Migrationen ableiten
- Migrationen für Tabellenstruktur und Constraints heranziehen

---

### 13. Freitextfelder und Freitextfeldsets

**WICHTIG:** Immer **"Freitextfeld(er)"** statt "Customfield(s)" und **"Freitextfeldset(s)"** statt "CustomFieldSet(s)" verwenden!

**Nur wenn CustomFields/CustomFieldSets im Plugin registriert werden.**

```markdown
## Freitextfelder

### Freitextfeldset: {Menschenlesbarer Set-Name}

**Technischer Name:** `{technical_set_name}`
**Zugeordnete Entities:** {entity1}, {entity2}

| Freitextfeld | Technischer Name | Typ | Beschreibung |
|:-------------|:-----------------|:----|:-------------|
| {Label DE} | `{technical_name}` | {Typ: Text, Bool, Int, Float, Select, etc.} | {Was das Feld speichert} |
```

Bei Select-Freitextfeldern zusätzlich:

```markdown
#### Optionen für "{Feld-Name}"

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

{# Prüfung ob Freitextfeld gesetzt ist #}
{% if product.customFields.{technical_name} is defined and product.customFields.{technical_name} is not empty %}
    {{ product.customFields.{technical_name} }}
{% endif %}
```
```

**Analyse-Checkliste:**

- Hauptklasse (`{PluginName}.php`) auf `install()`, `update()`, `activate()` prüfen
- CustomFieldSet-Registrierungen mit `customFieldSetRepository` finden
- Fixtures-Verzeichnis auf CustomField-Definitionen prüfen
- Service-Klassen die CustomFields verwalten analysieren (z.B. `CustomFieldService`)
- Alle Felder mit Typ, Optionen und zugeordneten Entity-Relationen dokumentieren

---

### 14. Services

**Nur wenn `src/Service/` existiert und Services mit öffentlichen Methoden enthält.**

```markdown
## Services

### {ServiceClassName}

{Kurze Beschreibung wofür der Service zuständig ist.}

| Methode | Parameter | Rückgabe | Beschreibung |
|:--------|:----------|:---------|:-------------|
| `{methodName}()` | `{Type} $name` | `{ReturnType}` | {Was die Methode macht} |
```

**Analyse-Checkliste:**

- Nur **öffentliche (public)** Methoden dokumentieren
- `__construct()` NICHT dokumentieren
- Parameter mit Typen angeben
- Rückgabetypen aus Type Declarations oder PHPDoc
- Abstrakte Klassen als solche kennzeichnen

---

### 15. Tasks / MessageQueue

**Nur wenn `src/Task/` existiert oder ScheduledTasks/MessageQueue-Handler vorhanden sind.**

```markdown
## Tasks / MessageQueue

### {TaskName}

{Beschreibung was der Task macht und wofür er gedacht ist.}

| Eigenschaft | Wert |
|:------------|:-----|
| Task-Name | `{getTaskName() Rückgabewert}` |
| Intervall | {Sekunden} ({menschenlesbar, z.B. "alle 24 Stunden"}) |
| Handler | `{HandlerClassName}` |
| Beschreibung | {Was der Handler bei Ausführung konkret macht} |
```

**Analyse-Checkliste:**

- `getTaskName()` und `getDefaultInterval()` aus der ScheduledTask-Klasse
- `run()` oder `__invoke()` Methode des Handlers analysieren
- Intervall menschenlesbar umrechnen: 3600 = stündlich, 86400 = täglich, 604800 = wöchentlich

---

### 16. Twig-Erweiterungen

**Nur wenn `src/Twig/` existiert und Twig-Extensions enthält.**

```markdown
## Twig-Erweiterungen

### Filter

| Filter | Beschreibung | Beispiel |
|:-------|:-------------|:---------|
| `{filterName}` | {Was der Filter macht} | `{{ variable \| {filterName} }}` |

### Funktionen

| Funktion | Parameter | Beschreibung | Beispiel |
|:---------|:----------|:-------------|:---------|
| `{functionName}` | `{parameter1}, {parameter2}` | {Was die Funktion macht} | `{{ {functionName}(param1, param2) }}` |
```

**Analyse-Checkliste:**

- `getFilters()` und `getFunctions()` Methoden analysieren
- Für jeden Filter/jede Funktion: Name, Parameter, Rückgabe, Zweck
- Praxisnahe Twig-Beispiele erstellen
- Wenn nur Filter → "Funktionen"-Abschnitt weglassen und umgekehrt

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

### 18. Tests & Codequalität

**Nur wenn mindestens eine der Konfigurationsdateien existiert.** Nur die Tools auflisten die tatsächlich vorhanden sind.

```markdown
## Tests & Codequalität
```

**Rector** (wenn `rector.php` existiert):

```markdown
### Rector

Rector prüft und aktualisiert PHP-Code automatisch auf moderne Syntax und Shopware-Konventionen.

| Einstellung | Wert |
|:------------|:-----|
| PHP-Version | {PHP-Set aus rector.php, z.B. "PHP 8.3"} |
| Shopware-Set | {Shopware-Set, z.B. "SHOPWARE_6_7_0"} |

```bash
# Prüfung (Dry-Run)
vendor/bin/rector process --dry-run

# Änderungen anwenden
vendor/bin/rector process --clear-cache
```
```

Wenn in der `composer.json` Scripts für rector definiert sind (z.B. `"rector": "vendor/bin/rector process --dry-run"`), dann stattdessen die composer-Scripts verwenden:

```markdown
```bash
# Prüfung (Dry-Run)
composer run rector

# Änderungen anwenden
vendor/bin/rector process --clear-cache
```
```

**Psalm** (wenn `psalm.xml` existiert):

```markdown
### Psalm

Statische Code-Analyse zur Erkennung von Typfehlern und potenziellen Bugs.

| Einstellung | Wert |
|:------------|:-----|
| Level | {errorLevel aus psalm.xml} |
| PHP-Version | {phpVersion aus psalm.xml} |

```bash
composer run psalm
```
```

**ECS** (wenn `ecs.php` existiert):

```markdown
### ECS (Easy Coding Standard)

Automatische Prüfung und Korrektur von Coding-Standards.

```bash
# Prüfen
composer run ecs

# Automatisch korrigieren
composer run ecs-fix
```
```

**PHPCS** (wenn `.phpcs.xml` existiert):

```markdown
### PHPCS (PHP CodeSniffer)

Prüfung der Code-Formatierung nach definierten Standards.

```bash
composer run phpcs
```
```

**Analyse-Checkliste:**

- `rector.php` lesen: verwendete Sets (`SetList::PHP_*`, `ShopwareSetList::*`), Skip-Regeln
- `psalm.xml` lesen: `errorLevel`, `phpVersion`
- `ecs.php` lesen: verwendete Sets und Regeln
- `.phpcs.xml` lesen: Standard und Regeln
- `composer.json` → `scripts` Sektion für die korrekten Ausführungsbefehle prüfen

---

### 19. Changelog

**Nur wenn `cliff.toml` existiert.**

```markdown
## Changelog

Das Changelog wird mit [git-cliff](https://git-cliff.org/) generiert:

```bash
git cliff --tag X.Y.Z --output CHANGELOG.md
```

Ersetze `X.Y.Z` durch die gewünschte Versionsnummer.
```

---

## Anti-Patterns — Was NICHT getan werden darf

| Nr. | Anti-Pattern | Richtig |
|:----|:-------------|:--------|
| 1 | Technischen Klassennamen als Titel verwenden ("# FfContentSitemap") | Menschenlesbaren Namen nutzen ("# Sitemap für Shopware 6.7") |
| 2 | Leere Sektionen anzeigen ("## Commands — Keine vorhanden") | Sektion komplett weglassen |
| 3 | "Customfield" oder "CustomFieldSet" schreiben | Immer "Freitextfeld" und "Freitextfeldset" |
| 4 | Englische Überschriften oder Beschreibungen | Alles auf Deutsch (Fachbegriffe wie "Entity", "DataResolver", "Subscriber" sind erlaubt) |
| 5 | composer.json-Beschreibung 1:1 kopieren | Beschreibung basiert auf Code-Analyse und beschreibt den tatsächlichen Funktionsumfang |
| 6 | Admin-Module unter CMS auflisten | CMS = CMS-Blöcke/-Elemente, Admin-Module = eigenständige Module |
| 7 | Private/protected Methoden von Services dokumentieren | Nur öffentliche (public) API dokumentieren |
| 8 | Intervalle nur in Sekunden angeben | Immer menschenlesbar umrechnen (86400 Sekunden = täglich) |
| 9 | Standard-Markdown statt GitLab-Markdown | `[[_TOC_]]` für Inhaltsverzeichnis, `<details>` für Collapsible Sections |
| 10 | Fehlende Dateien erraten oder erfinden | Wenn eine Datei nicht existiert → zugehörige Sektion weglassen |
| 11 | `__construct()` als Service-Methode dokumentieren | Konstruktor ist keine öffentliche API |
| 12 | CMS-Abschnitt für reine Admin-Erweiterungen | CMS bezieht sich ausschließlich auf CMS-Blöcke und CMS-Elemente |
| 13 | Bestehende README-Inhalte ignorieren | Bei Updates: manuell hinzugefügte Sektionen beibehalten |
| 14 | Umlaute als ae/oe/ue/ss umschreiben | Immer korrekte Umlaute verwenden: ä, ö, ü, Ä, Ö, Ü, ß |

---

## Hinweise für die Aktualisierung bestehender READMEs

Wenn eine README.md bereits existiert:

1. Lies die bestehende README **zuerst**
2. Analysiere den gesamten Plugin-Code (wie bei Neuerstellung)
3. Vergleiche bestehenden Inhalt mit dem analysierten Code
4. Aktualisiere alle Sektionen — entferne veraltete, füge neue hinzu
5. **Behalte manuell hinzugefügte Sektionen bei** die nicht automatisch generiert werden (z.B. "Bekannte Probleme", "FAQ", "Hinweise", "Mitwirkende")
6. Informiere den User über wesentliche Änderungen

---

## Beispiele für gute Ausgaben

### Beispiel: Badges, Titel mit Bild

```markdown
![Shopware](https://img.shields.io/badge/Shopware-6.7-blue)
![PHP](https://img.shields.io/badge/PHP-%3E%3D%208.3-brightgreen)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

# Sitemap für Shopware 6.7

[[_TOC_]]

![image](docs/plugin.png){width=306 height=500}

## Beschreibung

Dieses Plugin generiert eine XML-Sitemap für alle Sales Channels und berücksichtigt
dabei Produkte, Kategorien und CMS-Seiten. Die Sitemap kann über ein CLI-Command
manuell oder per Scheduled Task automatisch erstellt werden.
```

### Beispiel: Pluginkonfiguration mit Select-Optionen

```markdown
## Pluginkonfiguration

Die Konfiguration ist erreichbar unter **Erweiterungen → Meine Erweiterungen → Shopvote → Konfiguration**.

### Allgemein

| Feld | Technischer Name | Typ | Beschreibung | Standardwert |
|:-----|:-----------------|:----|:-------------|:-------------|
| Aktiv | `active` | Bool | Aktiviert die Bewertungsanfragen | `true` |
| API-Schlüssel | `apiKey` | Text | Shopvote API-Schlüssel für die Authentifizierung | _(leer)_ |
| Versandzeitpunkt | `sendDelay` | Single-Select | Wann die Bewertungsanfrage versendet wird | `7_days` |

#### Optionen für "Versandzeitpunkt"

| Wert | Bezeichnung |
|:-----|:------------|
| `immediately` | Sofort |
| `3_days` | Nach 3 Tagen |
| `7_days` | Nach 7 Tagen |
| `14_days` | Nach 14 Tagen |
```

### Beispiel: Entity mit Übersetzung

```markdown
## Entities

### Retailer (`ff_retailer`)

Speichert Händlerstandorte für die Händlersuche mit Adressdaten und Geokoordinaten.

#### Felder

| Feld | Typ | Beschreibung | Standard | Pflicht |
|:-----|:----|:-------------|:---------|:--------|
| `id` | `IdField` | Primärschlüssel | _(auto)_ | Ja |
| `name` | `StringField` | Name des Händlers (übersetzbar) | — | Ja |
| `street` | `StringField` | Straße | — | Ja |
| `zip` | `StringField` | Postleitzahl | — | Nein |
| `city` | `StringField` | Stadt | — | Ja |
| `latitude` | `FloatField` | Breitengrad | — | Nein |
| `longitude` | `FloatField` | Längengrad | — | Nein |
| `active` | `BoolField` | Ob der Händler aktiv ist | `true` | Nein |

#### Übersetzbare Felder

| Feld | Typ | Beschreibung |
|:-----|:----|:-------------|
| `name` | `StringField` | Name des Händlers |
| `description` | `LongTextField` | Beschreibung des Händlers |
```

### Beispiel: Freitextfelder

```markdown
## Freitextfelder

### Freitextfeldset: Shopvote Bewertungsdaten

**Technischer Name:** `ff_shopvote_evaluation`
**Zugeordnete Entities:** order

| Freitextfeld | Technischer Name | Typ | Beschreibung |
|:-------------|:-----------------|:----|:-------------|
| Bewertungsanfrage gesendet | `ff_shopvote_evaluation_sent` | Bool | Ob eine Bewertungsanfrage für diese Bestellung versendet wurde |
| Sendedatum | `ff_shopvote_evaluation_sent_at` | Datetime | Zeitpunkt der Versendung der Bewertungsanfrage |

**Zugriff in Twig:**

```twig
{% if order.customFields.ff_shopvote_evaluation_sent %}
    Bewertungsanfrage gesendet am: {{ order.customFields.ff_shopvote_evaluation_sent_at|date('d.m.Y H:i') }}
{% endif %}
```
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

# Testlauf mit Limit
bin/console ff:shopvote:send-mail --dry-run --limit 10
```
```

### Beispiel: Scheduled Task

```markdown
## Tasks / MessageQueue

### SendEvaluationRequestMailTask

Versendet automatisch Bewertungsanfragen an Kunden nach Abschluss ihrer Bestellung.

| Eigenschaft | Wert |
|:------------|:-----|
| Task-Name | `ff_shopvote.send_evaluation_request_mail` |
| Intervall | 86400 Sekunden (täglich) |
| Handler | `SendEvaluationRequestMailTaskHandler` |
| Beschreibung | Sucht Bestellungen deren Bewertungszeitraum abgelaufen ist und versendet Bewertungsanfrage-E-Mails |
```

### Beispiel: Collapsible Section für große Konfigurationen

```markdown
<details>
<summary>Erweiterte CMS Element-Konfiguration anzeigen</summary>

#### Hero Slider Konfiguration

| Option | Technischer Name | Typ | Beschreibung | Standardwert |
|:-------|:-----------------|:----|:-------------|:-------------|
| Automatisch abspielen | `autoplay` | Bool | Slider wechselt automatisch zum nächsten Slide | `true` |
| Geschwindigkeit | `speed` | Int | Wechselgeschwindigkeit in Millisekunden | `5000` |
| Navigation anzeigen | `showNavigation` | Bool | Vor/Zurück-Pfeile anzeigen | `true` |
| Pagination anzeigen | `showPagination` | Bool | Punkt-Indikatoren anzeigen | `true` |

</details>
```