# Contao 5.x – Guides (tutorials)

Complete reference from the Contao 5.x manual (German).

---

## Contents

- [1. Installing test versions](#1-installing-test-versions)
- [2. Creating the first start page](#2-creating-the-first-start-page)
- [3. Customising the maintenance template](#3-customising-the-maintenance-template)
- [4. Customising the Contao demo](#4-customising-the-contao-demo)
- [5. DCA adjustments](#5-dca-adjustments)
- [6. Sass/Less integration](#6-sassless-integration)
- [7. TinyMCE editor configuration](#7-tinymce-editor-configuration)
- [8. Introduction to grid systems](#8-introduction-to-grid-systems)
- [9. Using SVG files](#9-using-svg-files)
- [10. Storing form data](#10-storing-form-data)
- [11. Local installation](#11-local-installation)

## 1. Installing test versions

### Release candidates

RC tags such as `5.7.0-RC1` require adjustments in `composer.json`:

**Option A: set `minimum-stability`:**
```json
{
  "minimum-stability": "RC"
}
```

**Option B: stability flags per package:**
```json
{
  "require": {
    "contao/calendar-bundle": "^5.7@RC",
    "contao/core-bundle": "^5.7@RC",
    "contao/manager-bundle": "5.7.*@RC"
  }
}
```

### Developer versions

```json
{
  "require": {
    "contao/calendar-bundle": "5.x-dev",
    "contao/core-bundle": "5.x-dev",
    "contao/manager-bundle": "5.x-dev"
  }
}
```

**Important:** `contao/core-bundle` must be entered explicitly.

### Via the Contao Manager

1. At "Contao Open Source CMS" → edit the version specification
2. RC: `5.7.*@RC`, dev: `5.7.x-dev`
3. "Änderungen anwenden" (Apply changes)

---

## 2. Creating the first start page

Step-by-step guide for a new Contao installation:

**Step 1: create a new theme**
- Theme-Manager → Neu (New) → enter the title "Demo" and the author

**Step 2: create a Seitenlayout (page layout) in the theme**
- Seitenlayout icon in the theme → Neu (New)
- Titel (Title): "Standard"
- Zeilen (Rows): "Nur Hauptzeile" (Main row only), Spalten (Columns): "Nur Hauptspalte" (Main column only)

**Step 3: create the website starting point**
| Setting | Value |
|-------------|------|
| Seitenname (Page name) | e.g. "Meine Demo-Website" |
| Seitentyp (Page type) | Website-Startpunkt (Website starting point) |
| Sprache (Language) | de |
| Sprach-Fallback (Language fallback) | Enable |
| Layout zuweisen (Assign layout) | Enable + choose "Standard" from "Demo" |
| Seite veröffentlichen (Publish page) | Enable |

**Step 4: create the start page** (below the starting point)
| Setting | Value |
|-------------|------|
| Seitenname (Page name) | "Willkommen" |
| Seiten-Alias (Page alias) | "index" |
| Seite veröffentlichen (Publish page) | Enable |

**Step 5: edit the article**
Contao automatically creates an article for the start page. Edit the article → add content elements.

**Step 6: add a content element**
- Choose the type "Text", enter a headline and text, save

**Step 7: publish the article**
Click the eye icon next to the article → green = published.

---

## 3. Customising the maintenance template

**Enabling maintenance mode:** backend → Systemwartung (System maintenance).

### Adjusting the texts (language files)

Language variables: `XPT.unavailable`, `XPT.maintenance`

New file `contao/languages/de/exception.xlf`:
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

### Adjusting the logo

Copy the template from the vendor directory to `/templates/bundles/ContaoCoreBundle/Error/layout.html.twig`:
```html
<div class="header-logo">
    <img src="files/layout/images/logo.png" alt="Mein Logo">
</div>
```

### Replacing the entire template

Override `/templates/bundles/ContaoCoreBundle/Error/service_unavailable.html.twig` with your own HTML/CSS.

**After every change:** clear the production cache.

---

## 4. Customising the Contao demo

**Installation:** via the Contao Manager or the console (`composer require contao/contao-demo`).

### Adjusting the layout (SCSS)

Colour variables in `contaodemo/theme/src/scss/variables/_colors.scss`.

**Create your own partial file `_custom.scss`:**
```scss
$c-primary--500: hsla(212, 100%, 48%, 1);
```

**Add the `!default` flag in `_colors.scss`:**
```scss
$c-primary--500: hsla(30, 100%, 48%, 1) !default;
```

**Include it in `app.scss` as the first import:**
```scss
@import 'custom';
@import 'variables/_colors.scss';
```

**Important:** after changes to partial files, `app.scss` must be saved once.

### Using Dart Sass locally

Contao uses `scssphp/scssphp` (a PHP library), which does not support modern Dart Sass features such as `@use`/`@forward`. For a local workflow: install Dart Sass and use `--watch`.

---

## 5. DCA adjustments

Place DCA files in `contao/dca/` (as of Contao 4.9):

### Allowing HTML in fields

```php
// Überschriften in Inhaltselementen
$GLOBALS['TL_DCA']['tl_content']['fields']['headline']['eval']['allowHtml'] = true;

// News-Überschriften
$GLOBALS['TL_DCA']['tl_news']['fields']['headline']['eval']['preserveTags'] = true;

// Page name and page title
$GLOBALS['TL_DCA']['tl_page']['fields']['title']['eval']['allowHtml'] = true;
$GLOBALS['TL_DCA']['tl_page']['fields']['pageTitle']['eval']['allowHtml'] = true;

// Bildunterschriften
$GLOBALS['TL_DCA']['tl_content']['fields']['caption']['eval']['allowHtml'] = true;
```

### Making a field mandatory

```php
$GLOBALS['TL_DCA']['tl_member']['fields']['company']['eval']['mandatory'] = true;
```

**After changes:** clear the application cache.

---

## 6. Sass/Less integration

### Directly in Contao (simple)

`.scss` or `.less` files in the `files` folder. Contao compiles them automatically.

Example (`theme.scss`):
```scss
$mainCol: rgb(255, 0, 0) !default;
@import '_elements';
```

**Caution with partials:** changes to partial files (prefix `_`) are not applied automatically. Save the main file manually or clear the script cache.

**Limitation:** Contao uses PHP libraries instead of the official Sass — not all features are supported.

### Local preprocessing (recommended)

- Independent of the Contao library versions
- Access to all current preprocessor features
- Easier debugging
- Include the finished CSS files in Contao layouts

---

## 7. TinyMCE editor configuration

### Custom configuration

Create or adjust the template `be_tinyMCE.html5` in the main directory (`templates/`).

**Important:** all lines inside `<script>…</script>` except the last one must end with a comma.

### Different editor configurations

Rename the template (e.g. `be_myTinyMCE.html5`), then in a DCA file:
```php
$GLOBALS['TL_DCA']['tl_content']['fields']['text']['eval']['rte'] = 'myTinyMCE';
```

**After changes:** clear the application cache.

### Practical configuration examples

**Extended valid elements (enabling HTML tags):**
```
extended_valid_elements: 'q[cite|class|title],article,section,hgroup,figure,figcaption'
```

**Enabling paste without formatting:**
```
paste_as_text: true
```

**Adjusting the toolbar:**
Removing the alignment buttons: remove `alignleft aligncenter alignright alignjustify` from the toolbar.

**Configuring the menu:**
```
menubar: 'edit insert view format table tools',
removed_menuitems: 'tableprops deletetable'
```

**Custom format definitions:**
```
style_formats: [{ title: 'Eigener Stil', inline: 'span', classes: 'mein-stil' }]
```

**Custom CSS file for the editor preview:**
```
content_css: '/files/css/editor.css'
```

---

## 8. Introduction to grid systems

### Contao's own grid (deprecated, 960px-based)

- 12 columns with 10px gaps
- CSS classes: `grid1` – `grid12`
- Activation in the Seitenlayout → CSS-Framework → "12-Spalten Grid" (12-column grid)

### CSS Grid Layout (modern, without an extension)

```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 20px 20px;
}
```

### Extension-based

`contao-grid-bundle`: backend-integrated grid functionality with a 12-column layout and visual column selection for various viewports.

---

## 9. Using SVG files

### As a normal image file

Copy the SVG into a public `files` directory → select it in the "Bild" (Image) content element. Contao generates a standard `<img>` element with responsive image sizes.

### Inline SVG (more CSS control)

Create the template `mysvgicon.html5` in `templates/`, insert the SVG code, then:
```
{{file::mysvgfolder/mysvgicon.html5}}
```
Advantage: the SVG code is directly in the HTML, CSS can control the SVG elements.

### Colouring an SVG via CSS

The `currentColor` keyword in the `fill` property:
```css
.ce_text svg { color: #f47c00; }
```

### Dynamic colour passing via insert tag

```
{{file::mysvgfolder/mysvgicon.html5?color=#ff0000}}
```

Template implementation:
```php
fill="<?= \Contao\Input::get('color') ?: 'currentColor' ?>"
```

---

## 10. Storing form data

### Method I: the `prepareFormData` hook

Stores data in an existing table (e.g. `tl_calendar_events`).

1. Create a form; enable "Eingaben speichern" (Store submissions); `tl_calendar_events` as the target table
2. The `PrepareFormDataListener` implements:
   - Setting `tstamp`, `pid`, `author`, `published` automatically
   - Generating unique aliases
   - Converting date values via `strtotime()`

**Adjustment:** set `FORM_ID`, `CALENDAR_ID`, `AUTHOR_ID`.
**Clear the cache** after the implementation.

### Method II: the Leads extension (simpler)

1. Enable "Anfragen speichern" (Store enquiries) in the form settings
2. Master form: yes; navigation label; record label with Simple Tokens
3. Per form field: enable "In Anfrage speichern" (Store in enquiry)
4. Data is stored in `tl_lead` and `tl_lead_data`
5. Data management in the backend under "Anfragen" (Enquiries)
6. Presentation via the core module "Auflistung" (Listing) with the table `tl_lead`

---

## 11. Local installation

### DDEV

Docker-based tool for local PHP development environments.

**Quick start:**
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

**Important commands:**
| Command | Function |
|--------|---------|
| `ddev start` / `ddev stop` | Start/stop the project |
| `ddev poweroff` | Stop all projects |
| `ddev ssh` | Container shell |
| `ddev describe` | Services and access URLs |
| `ddev xdebug on` | Enable XDebug |

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

Prebuilt LAMP stack for Docker.

**Configuration in `.env`:**
```
HTTPD_DOCROOT_DIR=public
HTTPD_SERVER=apache-2.4
PHP_SERVER=8.2
MYSQL_SERVER=mariadb-10.3
```

**Start:** `docker-compose up httpd php mysql`

**Dashboard:** http://127.0.0.1

**Project directory:** `data/www/projektname/public/`

**Hosts file:** `127.0.0.1 projektname.loc` (or `.dvl.to` for automatic DNS resolution).

**Xdebug configuration** in `cfg/php-ini-x.y/xdebug.ini`:
```ini
xdebug.mode = debug
xdebug.client_host = host.docker.internal
xdebug.idekey = VSCODE
```

### Laragon (Windows)

WAMP stack installer for Windows with automatic virtual hosts.

**Prerequisites:**
- Windows 7/8/10
- Symlink permission: set up "Create symbolic links" for a normal user with Polsedit

**Configuration:**
- Adjust `laragon.ini`: `memory_limit = -1` or `2G`
- Virtual hosts: `{name}.local`
- PATH variable: Menu → Tools → Environment Variables → Add Laragon to Path

**Contao installation via Laragon:**
1. Menu → New Website → "Contao 4.9 Website"
2. Enter the project name → Composer installs automatically
3. The database is created automatically

**Access URLs after the installation:**
- Frontend: `http://projektname.local/`
- Backend: `http://projektname.local/contao`
- Installation tool: `http://projektname.local/contao/install`
- Contao Manager: `http://projektname.local/contao-manager.phar.php`

**Database credentials** (installation tool):
- User: `root`, password: (empty), database: the project name

---

Sources:
- https://docs.contao.org/5.x/manual/en/guides/
- https://docs.contao.org/5.x/manual/en/guides/install-test-versions/
- https://docs.contao.org/5.x/manual/en/guides/add-first-index-page/
- https://docs.contao.org/5.x/manual/en/guides/maintenance-template/
- https://docs.contao.org/5.x/manual/en/guides/contao-demo/
- https://docs.contao.org/5.x/manual/en/guides/dca/
- https://docs.contao.org/5.x/manual/en/guides/sass-less-integration/
- https://docs.contao.org/5.x/manual/en/guides/tinymce-configuration/
- https://docs.contao.org/5.x/manual/en/guides/grid-system/
- https://docs.contao.org/5.x/manual/en/guides/svg/
- https://docs.contao.org/5.x/manual/en/guides/save-form-data/
- https://docs.contao.org/5.x/manual/en/guides/local-installation/
- https://docs.contao.org/5.x/manual/en/guides/local-installation/ddev/
- https://docs.contao.org/5.x/manual/en/guides/local-installation/devilbox/
- https://docs.contao.org/5.x/manual/en/guides/local-installation/laragon/
