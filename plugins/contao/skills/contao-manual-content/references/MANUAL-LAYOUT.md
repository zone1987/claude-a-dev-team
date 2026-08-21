# Contao 5.x – Layout: Theme-Manager, modules & templates

Complete reference from the Contao 5.x manual (German).

---

## Contents

- [1. Theme-Manager](#1-theme-manager)
- [2. Module management](#2-module-management)
- [3. Templates](#3-templates)

## 1. Theme-Manager

### Managing themes

A theme brings together all design-relevant elements of a website.

**Components of a theme:**
- The theme itself
- Stylesheets
- Frontend modules
- Seitenlayouts (Page layouts)
- Image sizes
- Files (upload directory)
- Customised templates (optional)

Note: stylesheets, modules, layouts and image sizes are stored in the database. Files and templates are stored in subdirectories.

**Configuration fields:**

| Field | Description |
|------|-------------|
| **Theme-Titel** (Theme title) | Name in the backend overview and export file name |
| **Autor** (Author) | Name of the theme designer |
| **Ordner** (Folders) | Associated folders from the upload directory |
| **Bildschirmfoto** (Screenshot) | Screenshot for the theme overview |
| **Templates-Ordner** (Templates folder) | Subfolder with customised templates |

**Export:** `.cto` file (ZIP archive) with `theme.xml`, `files/` and `templates/`.

**Import:** checks for missing fields in tables, non-existent layout sections and templates that already exist. After the import the theme must be activated by assigning a Seitenlayout to a page.

**Security warning:** only install themes from trustworthy vendors.

---

### Managing stylesheets

The internal CSS editor is **deprecated** and will be removed in a future Contao version. Export existing stylesheets and include them as external stylesheets in Seitenlayouts.

**Media types:**
- `all`, `screen`, `print`, `handheld`, `projection`, `aural`, `braille`, `embossed`, `tty`, `tv`
- Most relevant for websites: `screen` and `print`

**Conditional comments:** Internet Explorer-specific directives (`if IE`, `if lt IE 6`, `if gte IE 6`).

**Order of format definitions:** important! Later definitions override earlier ones. Reordering via drag and drop.

**Import/export:** import or export CSS files via the navigation icons.

---

### Managing Seitenlayouts (page layouts)

The Seitenlayout structures the website and divides it into layout sections for frontend modules.

**Header/footer:**
- Configurable row heights
- Typical: company logo at the top, copyright at the bottom

**Column configuration:**
- Up to three columns (left, main, right)
- Adjustable widths for the left and right column
- The main column adapts automatically

**Custom layout sections:**
Five standard sections plus user-defined sections. Positions: `top`, `before`, `main`, `after`, `bottom`, `manual`.

**CSS framework components:**
- Layout builder (required for the page generator)
- Responsive layout
- 12-column grid
- CSS reset
- Form support
- Icon resources

**Stylesheets:**
- Internal and external CSS files
- SCSS and LESS support (caution: the internal library may not support all modern Dart Sass features)
- Configurable loading order
- Optional compression

**Web fonts:** Google Fonts integration; manual inclusion recommended.

**JavaScript templates:**
| Template | Function |
|----------|---------|
| `js_autofocus` | Focus navigation on form errors |
| `js_highlight` | Syntax highlighter |
| `js_nocookie` | CSRF protection notification |
| `js_slider` | Content slider functionality (legacy) |
| `js_accordion` | Accordion (legacy) |

**jQuery and MooTools:** can be loaded optionally. Source: local, CDN or CDN with fallback.

**Analytics:** Google Analytics and Matomo (Piwik) via template.

**Image sizes:** lightbox dimensions with responsive pixel densities (1x, 1.5x, 2x).

**RSS/Atom feeds:** linking with news and calendar feeds in the `<head>`.

**Static layout:** converts a liquid layout into a fixed width (left/right/centred).

**Expert settings:**
- Custom page templates
- Markup compression
- Viewport tag adjustment
- Title tag override
- Body classes and events
- Additional `<head>` tags

---

## 2. Module management

Modules are created within themes and embedded in Seitenlayouts. They generate HTML code for the frontend output.

**Access protection:** restriction to Mitgliedergruppen (member groups); option "Nur Gästen anzeigen" (Show to guests only) in the expert settings.

---

### 2.1 Navigation modules

#### Navigationsmenü (Navigation menu)
Hierarchical navigation from all published, non-hidden pages.

| Setting | Description |
|-------------|-------------|
| **Startlevel** (Start level) | Entry point (e.g. level 2 for submenus) |
| **Stoplevel** (Stop level) | Maximum nesting depth |
| **Harter Grenzwert** (Hard limit) | No elements beyond the stop level |
| **Geschützte Seiten anzeigen** (Show protected pages) | Include pages restricted to logged-in users |
| **Versteckte Seiten anzeigen** (Show hidden pages) | Include pages hidden from the navigation |
| **Referenzseite** (Reference page) | Custom starting point instead of the root |
| **Navigationstemplate** (Navigation template) | Template selection |

Template: `mod_navigation`

#### Individuelle Navigation (Custom navigation)
Menu made of freely selectable pages (without hierarchy dependency).
Template: `mod_customnav`

#### Navigationspfad (Breadcrumb)
Shows the path to the current page.
Template: `mod_breadcrumb`

#### Quicknavigation (dropdown)
Dropdown menu for jumping directly to a page.
- Custom label, stop level, hard limit, reference page
- Template: `mod_quicknav`

#### Quicklink
Dropdown made of freely selectable pages.
Template: `mod_quicklink`

#### Buchnavigation (Book navigation)
Forward/back/up navigation through pages ("page turning").
Template: `mod_booknav`

#### Artikelnavigation (Article navigation)
Forward/back navigation through the articles of a page.
- **Erstes Element laden** (Load first element): load the first article automatically
- Template: `mod_articlenav`

#### HTML-Sitemap
Overview of all published, non-hidden pages.
Template: `mod_sitemap`

**HTML output:** all navigation modules use `<!-- indexer::stop -->` and `<!-- indexer::continue -->` comments as well as schema.org markup.

---

### 2.2 User modules

#### Login-Formular (Login form)
Authentication for registered members.
- Auto login, password reset page (as of 5.3), redirect page
- Option: redirect to the last visited page
- Template: `ce_login`

#### Personendaten (Personal data)
Members can edit their personal data.
- Editable fields configurable
- Newsletter subscription (if the extension is active)
- Templates: `member_default` (linear) or `member_grouped` (fieldsets)

#### Registrierung (Registration)
New registration for visitors.
- Mandatory fields, Mitgliedergruppen, home directory, spam protection
- E-mail-based activation (24-hour link)
- Placeholders: `##firstname##`, `##domain##`, `##link##`
- Templates: `member_default`, `member_grouped`

#### Passwort ändern (Change password)
For logged-in members. The old password is verified.
Template: `ce_changePassword`

#### Passwort vergessen (Forgot password)
Recovery via e-mail. Spam protection, confirmation page, e-mail template.
Template: `ce_lostPassword`

#### Konto schließen (Close account)
Deactivate or permanently delete the account, optionally remove the home directory.
Template: `ce_closeAccount`

#### Zwei-Faktor-Authentifizierung (Two-factor authentication)
TOTP/2FA setup with a QR code for authenticator apps, backup key display.
Template: `ce_two_factor`

---

### 2.3 Website search

#### Suchmodul (Search module)

| Setting | Function |
|-------------|---------|
| **Standard-Abfragetyp** (Default query type) | AND or OR |
| **Ungenaue Suche** (Fuzzy search) | Wildcard-like results |
| **Kontext-Spannweite** (Context range) | Number of characters around the found terms |
| **Minimale Suchwort-Länge** (Minimum keyword length) | Minimum number of characters (0 = disabled) |
| **Elemente pro Seite** (Items per page) | Pagination |
| **Suchformular-Layout** (Search form layout) | Simple or extended (with AND/OR options) |
| **Weiterleitungsseite** (Redirect page) | Target after form submission |
| **Referenzseite** (Reference page) | Restriction to a page area |

**Search syntax:**
- `"web design"` – phrase search (exact order)
- `web*` – wildcard search
- `+web` – force a term
- `-web` – exclude a term

**Indexing control:**
```html
<!-- indexer::stop -->
[content is not indexed]
<!-- indexer::continue -->
```

**Indexing protected pages** (in `config/config.yaml`):
```yaml
contao:
  search:
    index_protected: true
```

---

### 2.4 Application modules

#### Formular (Form)
Embeds a form from the Formulargenerator (Form Generator).
Setting: **Formular** — selection of the form to insert.

#### Auflistung (Listing)
Lists database records — sortable, filterable, searchable.

| Setting | Description |
|-------------|-------------|
| **Tabelle** (Table) | Database source |
| **Felder** (Fields) | Comma-separated field list |
| **Bedingung** (Condition) | SQL filter or insert tags |
| **Durchsuchbare Felder** (Searchable fields) | Generates a search form |
| **Sortieren nach** (Sort by) | Default sorting |
| **Elemente pro Seite** (Items per page) | Pagination |
| **Felder der Detailseite** (Fields of the detail page) | Activate the detail view |

---

### 2.5 Miscellaneous

#### Artikelliste (Article list)
Shows all articles of a selected column.
- Skipping elements, column selection, reference page
- Template: `mod_articlelist`

#### Zufallsbild (Random image)
Random image from a folder/selection.
- Scaling modes, lightbox, image caption
- Template: `mod_randomImage`

#### Eigener HTML-Code (Custom HTML code)
Any HTML code (backend security rules apply).
Template: `mod_html`

#### RSS-Reader
Subscribes to and displays RSS feeds.
- Feed URLs, total items, items per page, cache duration
- Templates: `rss_default` (header + posts) or `rss_items_only`

#### Startpunktabhängige Module (Start point-dependent modules)
Selects different modules per starting point — avoids several layout variants.

#### Individuelles Template (Custom template)
Template with custom key/value pairs.
Template: `mod_template`

---

## 3. Templates

Templates control the HTML output of modules, content elements, forms and other components. Under
**Layout > Templates** they are customised without update risk.

Contao 5 ships two systems: **Twig**, the standard since 5.0, and the legacy **PHP** templates. From
5.7 every `.html5` template has a Twig equivalent, though a `.html5` file of the same name in
`templates` still takes precedence over the Twig one.

For a CSS adjustment a template override is often unnecessary: the CSS id and class can be set in the
element's expert settings.

Syntax, storage paths, inheritance and the `dump()` helper are in
[MANUAL-TEMPLATES.md](MANUAL-TEMPLATES.md).

---

Sources:
- https://docs.contao.org/5.x/manual/en/layout/
- https://docs.contao.org/5.x/manual/en/layout/theme-manager/
- https://docs.contao.org/5.x/manual/en/layout/theme-manager/manage-themes/
- https://docs.contao.org/5.x/manual/en/layout/theme-manager/manage-stylesheets/
- https://docs.contao.org/5.x/manual/en/layout/theme-manager/manage-page-layouts/
- https://docs.contao.org/5.x/manual/en/layout/module-management/
- https://docs.contao.org/5.x/manual/en/layout/module-management/navigation-modules/
- https://docs.contao.org/5.x/manual/en/layout/module-management/user-modules/
- https://docs.contao.org/5.x/manual/en/layout/module-management/website-search/
- https://docs.contao.org/5.x/manual/en/layout/module-management/applications/
- https://docs.contao.org/5.x/manual/en/layout/module-management/miscellaneous/
- https://docs.contao.org/5.x/manual/en/layout/templates/
