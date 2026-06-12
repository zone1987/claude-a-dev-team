# Contao 5.x – Anleitungen (Tutorials)

Vollständige Referenz aus dem Contao 5.x Handbuch (deutsch).

---

## 1. Testversionen installieren

### Release Candidates

RC-Tags wie `5.7.0-RC1` erfordern Anpassungen in `composer.json`:

**Option A: `minimum-stability` setzen:**
```json
{
  "minimum-stability": "RC"
}
```

**Option B: Stability-Flags pro Paket:**
```json
{
  "require": {
    "contao/calendar-bundle": "^5.7@RC",
    "contao/core-bundle": "^5.7@RC",
    "contao/manager-bundle": "5.7.*@RC"
  }
}
```

### Entwicklerversionen

```json
{
  "require": {
    "contao/calendar-bundle": "5.x-dev",
    "contao/core-bundle": "5.x-dev",
    "contao/manager-bundle": "5.x-dev"
  }
}
```

**Wichtig:** `contao/core-bundle` muss explizit eingetragen werden.

### Via Contao Manager

1. Bei "Contao Open Source CMS" → Versionsangabe bearbeiten
2. RC: `5.7.*@RC`, Dev: `5.7.x-dev`
3. "Änderungen anwenden"

---

## 2. Die erste Startseite erstellen

Schritt-für-Schritt-Anleitung für eine neue Contao-Installation:

**Schritt 1: Neues Theme erstellen**
- Theme-Manager → Neu → Titel "Demo", Autor eingeben

**Schritt 2: Seitenlayout im Theme anlegen**
- Seitenlayout-Icon im Theme → Neu
- Titel: "Standard"
- Zeilen: "Nur Hauptzeile", Spalten: "Nur Hauptspalte"

**Schritt 3: Website-Startpunkt anlegen**
| Einstellung | Wert |
|-------------|------|
| Seitenname | z.B. "Meine Demo-Website" |
| Seitentyp | Website-Startpunkt |
| Sprache | de |
| Sprach-Fallback | Aktivieren |
| Layout zuweisen | Aktivieren + "Standard" aus "Demo" wählen |
| Seite veröffentlichen | Aktivieren |

**Schritt 4: Startseite anlegen** (unterhalb des Startpunkts)
| Einstellung | Wert |
|-------------|------|
| Seitenname | "Willkommen" |
| Seiten-Alias | "index" |
| Seite veröffentlichen | Aktivieren |

**Schritt 5: Artikel bearbeiten**
Contao erstellt automatisch einen Artikel für die Startseite. Artikel bearbeiten → Inhaltselemente hinzufügen.

**Schritt 6: Inhaltselement hinzufügen**
- Typ "Text" wählen, Überschrift und Text eingeben, speichern

**Schritt 7: Artikel veröffentlichen**
Auge-Icon neben dem Artikel anklicken → grün = veröffentlicht.

---

## 3. Wartungstemplate anpassen

**Wartungsmodus aktivieren:** Backend → Systemwartung.

### Texte anpassen (Sprachdateien)

Sprachvariablen: `XPT.unavailable`, `XPT.maintenance`

Neue Datei `contao/languages/de/exception.xlf`:
```xml
<?xml version="1.0" ?><xliff version="1.1">
  <file>
    <body>
      <trans-unit id="XPT.unavailable">
        <target>Wartungsmodus</target>
      </trans-unit>
      <trans-unit id="XPT.maintenance">
        <target>Benutzerdefinierter Text</target>
      </trans-unit>
    </body>
  </file>
</xliff>
```

**Alternative (PHP):**
```php
$GLOBALS['TL_LANG']['XPT']['unavailable'] = 'Wartungsmodus';
```

### Logo anpassen

Template aus Vendor kopieren nach `/templates/bundles/ContaoCoreBundle/Error/layout.html.twig`:
```html
<div class="header-logo">
    <img src="files/layout/images/logo.png" alt="Mein Logo">
</div>
```

### Komplettes Template ersetzen

`/templates/bundles/ContaoCoreBundle/Error/service_unavailable.html.twig` mit eigenem HTML/CSS überschreiben.

**Nach jeder Änderung:** Produktions-Cache leeren.

---

## 4. Die Contao Demo anpassen

**Installation:** Via Contao-Manager oder Konsole (`composer require contao/contao-demo`).

### Layout anpassen (SCSS)

Farbvariablen in `contaodemo/theme/src/scss/variables/_colors.scss`.

**Eigene Partial-Datei `_custom.scss` anlegen:**
```scss
$c-primary--500: hsla(212, 100%, 48%, 1);
```

**In `_colors.scss` `!default`-Flag hinzufügen:**
```scss
$c-primary--500: hsla(30, 100%, 48%, 1) !default;
```

**In `app.scss` als ersten Import einbinden:**
```scss
@import 'custom';
@import 'variables/_colors.scss';
```

**Wichtig:** Nach Änderungen an Partial-Dateien muss `app.scss` einmal gespeichert werden.

### Dart Sass lokal verwenden

Contao nutzt `scssphp/scssphp` (PHP-Bibliothek), die moderne Dart-Sass-Features wie `@use`/`@forward` nicht unterstützt. Für lokalen Workflow: Dart Sass installieren und `--watch` nutzen.

---

## 5. DCA-Anpassungen

DCA-Dateien in `contao/dca/` ablegen (ab Contao 4.9):

### HTML in Feldern erlauben

```php
// Überschriften in Inhaltselementen
$GLOBALS['TL_DCA']['tl_content']['fields']['headline']['eval']['allowHtml'] = true;

// News-Überschriften
$GLOBALS['TL_DCA']['tl_news']['fields']['headline']['eval']['preserveTags'] = true;

// Seitennamen und -titel
$GLOBALS['TL_DCA']['tl_page']['fields']['title']['eval']['allowHtml'] = true;
$GLOBALS['TL_DCA']['tl_page']['fields']['pageTitle']['eval']['allowHtml'] = true;

// Bildunterschriften
$GLOBALS['TL_DCA']['tl_content']['fields']['caption']['eval']['allowHtml'] = true;
```

### Pflichtfeld setzen

```php
$GLOBALS['TL_DCA']['tl_member']['fields']['company']['eval']['mandatory'] = true;
```

**Nach Änderungen:** Anwendungs-Cache leeren.

---

## 6. Sass/Less Integration

### Direkt in Contao (einfach)

`.scss`- oder `.less`-Dateien im `files`-Ordner. Contao kompiliert automatisch.

Beispiel (`theme.scss`):
```scss
$mainCol: rgb(255, 0, 0) !default;
@import '_elements';
```

**Achtung Partials:** Änderungen an Partial-Dateien (Präfix `_`) werden nicht automatisch übernommen. Hauptdatei manuell speichern oder Script-Cache leeren.

**Einschränkung:** Contao nutzt PHP-Bibliotheken statt des offiziellen Sass — nicht alle Features unterstützt.

### Lokale Vorverarbeitung (empfohlen)

- Unabhängig von Contao-Bibliotheksversionen
- Zugang zu allen aktuellen Preprocessor-Features
- Einfacheres Debugging
- Fertige CSS-Dateien in Contao-Layouts einbinden

---

## 7. TinyMCE-Editor Konfiguration

### Benutzerdefinierte Konfiguration

Template `be_tinyMCE.html5` im Hauptverzeichnis (`templates/`) anlegen oder anpassen.

**Wichtig:** Alle Zeilen innerhalb von `<script>…</script>` bis auf die letzte müssen mit Komma abgeschlossen werden.

### Verschiedene Editor-Konfigurationen

Template umbenennen (z.B. `be_myTinyMCE.html5`), dann in DCA-Datei:
```php
$GLOBALS['TL_DCA']['tl_content']['fields']['text']['eval']['rte'] = 'myTinyMCE';
```

**Nach Änderungen:** Anwendungs-Cache leeren.

### Praktische Konfigurationsbeispiele

**Extended Valid Elements (HTML-Tags freischalten):**
```
extended_valid_elements: 'q[cite|class|title],article,section,hgroup,figure,figcaption'
```

**Einfügen ohne Formatierung aktivieren:**
```
paste_as_text: true
```

**Toolbar anpassen:**
Ausrichtungsbuttons entfernen: `alignleft aligncenter alignright alignjustify` aus Toolbar entfernen.

**Menü konfigurieren:**
```
menubar: 'edit insert view format table tools',
removed_menuitems: 'tableprops deletetable'
```

**Eigene Format-Definitionen:**
```
style_formats: [{ title: 'Eigener Stil', inline: 'span', classes: 'mein-stil' }]
```

**Eigene CSS-Datei für Editor-Vorschau:**
```
content_css: '/files/css/editor.css'
```

---

## 8. Grid-System Einführung

### Contao-eigenes Grid (veraltet, 960px-basiert)

- 12 Spalten mit 10px-Abständen
- CSS-Klassen: `grid1` – `grid12`
- Aktivierung in Seitenlayout → CSS-Framework → "12-Spalten Grid"

### CSS Grid Layout (modern, ohne Erweiterung)

```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 20px 20px;
}
```

### Erweiterungsbasiert

`contao-grid-bundle`: Backend-integrierte Grid-Funktionalität mit 12-Spalten-Layout und visueller Spaltenauswahl für verschiedene Viewports.

---

## 9. SVG-Dateien einsetzen

### Als normale Bild-Datei

SVG in öffentliches `files`-Verzeichnis kopieren → Im Inhaltselement "Bild" auswählen. Contao generiert Standard-`<img>`-Element mit responsiven Bildgrößen.

### Inline SVG (mehr CSS-Kontrolle)

Template `mysvgicon.html5` in `templates/` erstellen, SVG-Code einfügen, dann:
```
{{file::mysvgfolder/mysvgicon.html5}}
```
Vorteil: SVG-Code direkt im HTML, CSS kann SVG-Elemente steuern.

### SVG per CSS kolorieren

`currentColor`-Schlüsselwort in der `fill`-Eigenschaft:
```css
.ce_text svg { color: #f47c00; }
```

### Dynamische Farbübergabe per Insert-Tag

```
{{file::mysvgfolder/mysvgicon.html5?color=#ff0000}}
```

Template-Implementierung:
```php
fill="<?= \Contao\Input::get('color') ?: 'currentColor' ?>"
```

---

## 10. Formulardaten speichern

### Methode I: Hook `prepareFormData`

Speichert Daten in bestehender Tabelle (z.B. `tl_calendar_events`).

1. Formular erstellen; "Eingaben speichern" aktivieren; `tl_calendar_events` als Zieltabelle
2. `PrepareFormDataListener` implementiert:
   - Setzt `tstamp`, `pid`, `author`, `published` automatisch
   - Generiert eindeutige Aliases
   - Konvertiert Datumswerte via `strtotime()`

**Anpassung:** `FORM_ID`, `CALENDAR_ID`, `AUTHOR_ID` setzen.
**Cache leeren** nach Implementierung.

### Methode II: Leads-Erweiterung (einfacher)

1. "Anfragen speichern" in Formular-Einstellungen aktivieren
2. Master-Formular: Ja; Navigations-Bezeichnung; Datensatz-Bezeichnung mit Simple Tokens
3. Pro Formularfeld: "In Anfrage speichern" aktivieren
4. Daten werden in `tl_lead` und `tl_lead_data` gespeichert
5. Datenverwaltung im Backend unter "Anfragen"
6. Darstellung via Core-Modul "Auflistung" mit Tabelle `tl_lead`

---

## 11. Lokale Installation

### DDEV

Docker-basiertes Tool für lokale PHP-Entwicklungsumgebungen.

**Schnellstart:**
```bash
mkdir contao && cd contao
ddev config --project-type=php --docroot=public --webserver-type=apache-fpm --php-version=8.2
ddev composer create-project contao/managed-edition:5.7
ddev dotenv set .env.local \
  --database-url=mysql://db:db@db:3306/db \
  --mailer-dsn=smtp://localhost:1025
ddev exec contao-console contao:migrate --no-interaction
ddev exec contao-console contao:user:create \
  --username=admin --name=Administrator \
  --email=admin@example.com --language=de \
  --password=Password123 --admin
ddev launch contao
```

**Wichtige Befehle:**
| Befehl | Funktion |
|--------|---------|
| `ddev start` / `ddev stop` | Projekt starten/stoppen |
| `ddev poweroff` | Alle Projekte stoppen |
| `ddev ssh` | Container-Shell |
| `ddev describe` | Dienste und Zugangs-URLs |
| `ddev xdebug on` | XDebug aktivieren |

**Adminer:** `ddev add-on get ddev/ddev-adminer && ddev restart`

**Cronjob:**
```bash
ddev add-on get ddev/ddev-cron
```
`/.ddev/web-build/contao.cron`:
```
* * * * * php /var/www/html/vendor/bin/contao-console contao:cron
```

### Devilbox (Docker)

Vorgefertigter LAMP-Stack für Docker.

**Konfiguration in `.env`:**
```
HTTPD_DOCROOT_DIR=public
HTTPD_SERVER=apache-2.4
PHP_SERVER=8.2
MYSQL_SERVER=mariadb-10.3
```

**Start:** `docker-compose up httpd php mysql`

**Dashboard:** http://127.0.0.1

**Projektverzeichnis:** `data/www/projektname/public/`

**Hosts-Datei:** `127.0.0.1 projektname.loc` (oder `.dvl.to` für automatische DNS-Auflösung).

**Xdebug-Konfiguration** in `cfg/php-ini-x.y/xdebug.ini`:
```ini
xdebug.mode = debug
xdebug.client_host = host.docker.internal
xdebug.idekey = VSCODE
```

### Laragon (Windows)

WAMP-Stack-Installer für Windows mit automatischen virtuellen Hosts.

**Voraussetzungen:**
- Windows 7/8/10
- Symlink-Berechtigung: Mit Polsedit "Create symbolic links" für normalen Benutzer einrichten

**Konfiguration:**
- `laragon.ini` anpassen: `memory_limit = -1` oder `2G`
- Virtuelle Hosts: `{name}.local`
- PATH-Variable: Menu → Tools → Environment Variables → Add Laragon to Path

**Contao-Installation via Laragon:**
1. Menu → New Website → "Contao 4.9 Website"
2. Projektname eingeben → Composer installiert automatisch
3. Datenbank wird automatisch erstellt

**Zugangs-URLs nach Installation:**
- Frontend: `http://projektname.local/`
- Backend: `http://projektname.local/contao`
- Installation Tool: `http://projektname.local/contao/install`
- Contao Manager: `http://projektname.local/contao-manager.phar.php`

**Datenbank-Zugangsdaten** (Installation Tool):
- Benutzer: `root`, Passwort: (leer), Datenbank: Projektname

---

Quellen:
- https://docs.contao.org/5.x/manual/de/anleitungen/
- https://docs.contao.org/5.x/manual/de/anleitungen/testversionen-installieren/
- https://docs.contao.org/5.x/manual/de/anleitungen/die-erste-startseite/
- https://docs.contao.org/5.x/manual/de/anleitungen/wartungstemplate-anpassen/
- https://docs.contao.org/5.x/manual/de/anleitungen/contao-demo/
- https://docs.contao.org/5.x/manual/de/anleitungen/dca/
- https://docs.contao.org/5.x/manual/de/anleitungen/sass-less-integration/
- https://docs.contao.org/5.x/manual/de/anleitungen/tinymce-konfiguration/
- https://docs.contao.org/5.x/manual/de/anleitungen/grid/
- https://docs.contao.org/5.x/manual/de/anleitungen/svg/
- https://docs.contao.org/5.x/manual/de/anleitungen/formulardaten-speichern/
- https://docs.contao.org/5.x/manual/de/anleitungen/lokale-installation/
- https://docs.contao.org/5.x/manual/de/anleitungen/lokale-installation/ddev/
- https://docs.contao.org/5.x/manual/de/anleitungen/lokale-installation/devilbox/
- https://docs.contao.org/5.x/manual/de/anleitungen/lokale-installation/laragon/
