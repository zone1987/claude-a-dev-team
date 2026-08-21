# Contao 5.x – Article management & content elements

Complete reference from the Contao 5.x manual (German).

---

## Contents

- [1. Article management](#1-article-management)
- [2. Content elements – overview](#2-content-elements--overview)
- [3. Text elements](#3-text-elements)
- [4. Link elements](#4-link-elements)
- [5. File elements](#5-file-elements)
- [6. Media elements](#6-media-elements)
- [7. Miscellaneous (nested elements, as of Contao 5.3)](#7-miscellaneous-nested-elements-as-of-contao-53)
- [8. Include elements](#8-include-elements)
- [9. Legacy elements (wrapper system, before Contao 5.3)](#9-legacy-elements-wrapper-system-before-contao-53)
- [10. Common settings of all content elements](#10-common-settings-of-all-content-elements)

## 1. Article management

Articles link content to pages and layout sections. Every page can contain any number of articles, which are output in order in the assigned layout section.

### Core settings of an article

| Field | Description |
|------|-------------|
| **Artikel-Alias** (Article alias) | Unique reference; enables direct access via the URL `seite/articles/alias.html` |
| **Teasertext** (Teaser text) | Short version for overview pages |
| **Teaser CSS-ID/Klasse** (Teaser CSS ID/class) | Individual styling of the teaser |
| **Teaser anzeigen** (Show teaser) | Is activated automatically when several articles exist per section |
| **Syndikation** (Syndication) | Print function, Facebook and Twitter sharing |
| **Individuelles Template** (Custom template) | Overrides the default template `mod_article` |

### Access protection

- **Schutz aktivieren** (Enable protection) – visible only to logged-in members
- **Erlaubte Mitgliedergruppen** (Permitted member groups) – group selection
- **Nur Gästen anzeigen** (Show to guests only) (expert settings) – is hidden as soon as a member is logged in

### Publication

- Manual switch
- **Anzeigen ab / Anzeigen bis** (Show from / Show until) – scheduled activation/deactivation

---

## 2. Content elements – overview

Contao offers seven categories of content elements. As of Contao 5.3 three elements support **nested content elements** (Akkordeon, Elementgruppe, Content Slider).

---

## 3. Text elements

### Überschrift (Headline)
- **Text** + hierarchy (h1–h6)
- Template: `content_element/headline`

### Text
- Rich text editor (TinyMCE)
- Optional image with alignment (top, bottom, left-aligned, right-aligned)
- Image size modes: exact format, proportional, fit to frame
- Template: `content_element/text`

### HTML
- Any HTML code (permitted tags only)
- No enclosing markup

### Ungefiltertes HTML (Unfiltered HTML) *(as of Contao 5.3)*
- No tag restriction whatsoever (be careful!)
- Template: `content_element/unfilteredHtml`

### Aufzählung (List, ordered/unordered)
- Selectable list type
- CSV import possible
- Template: `content_element/list`

### Tabelle (Table)
- Header/footer row, row header, sortability
- CSV import
- Template: `content_element/table`

### Code
Syntax highlighting for: Apache, Bash, C#, C++, CSS, Diff, HTML, HTTP, Ini, JSON, Java, JavaScript, Markdown, Nginx, Perl, PHP, PowerShell, Python, Ruby, SCSS, SQL, Twig, YAML, XML.
Output: `<div class="content-code"><pre><code>…</code></pre></div>`

### Markdown
- Source: text or file
- Extended syntax (tables, footnotes)
- Template: `content_element/markdown`

### Beschreibungsliste (Description list) *(as of Contao 5.3)*
- Key-value pairs (`<dl>/<dt>/<dd>`)
- Template: `content_element/descriptionList`

---

## 4. Link elements

### Hyperlink
Creates a link to an external URL or e-mail address.

| Field | Description |
|------|-------------|
| **Link-Adresse** (Link address) | URL including protocol (http://, mailto:, tel:) |
| **In neuem Fenster öffnen** (Open in new window) | Opens the link in a new tab |
| **Link-Text** | Displayed text instead of the URL |
| **Den Link einbetten** (Embed the link) | Embeds the link in the surrounding text (`%s` as a placeholder) |
| **Link-Titel** (Link title) | `title` attribute |
| **Lightbox** | `data-lightbox` attribute for lightbox control |
| **Bild als Link** (Image as link) | Replaces the text with an image link |

Template: `content_element/hyperlink`

### Top-Link
Jumps to the top of the page. Link text: default "Nach oben" (To the top).
Template: `content_element/toplink`

---

## 5. File elements

### Download
Single file to download or display in the browser.

| Field | Description |
|------|-------------|
| **Quelldatei** (Source file) | File selection |
| **Im Browser anzeigen** (Show in browser) | No download dialogue |
| **Link überschreiben** (Override link) | Custom link text and title |
| **Vorschaubilder** (Thumbnails) | Shows preview thumbnails; number configurable |

Template: `content_element/download`

### Downloads
Several files / folders. Additionally:
- **Sortieren nach** (Sort by): custom, file name (ascending/descending), date, random
- **Dateien ohne Metadaten ignorieren** (Ignore files without metadata)
- **Home-Verzeichnis verwenden** (Use home directory) (for logged-in members)

Template: `content_elements/downloads`

---

## 6. Media elements

### Bild (Image)
| Field | Description |
|------|-------------|
| **Quelldatei** (Source file) | Image selection |
| **Bildgröße** (Image size) | Dimensions |
| **Lightbox/Neues Fenster** (Lightbox/new window) | Opens the original size on click |
| **Metadaten überschreiben** (Override metadata) | Individual alt/title data |
| **Bildlink-URL** (Image link URL) | Clickable image (disables the lightbox) |
| **Bildunterschrift** (Image caption) | Caption text |

Output: `<figure>` element with an optional `<figcaption>`

### Galerie (Gallery)
| Field | Description |
|------|-------------|
| **Quelldateien** (Source files) | Folder or individual images |
| **Home-Verzeichnis** (Home directory) | For logged-in members |
| **Sortieren nach** (Sort by) | Custom, file name, date, random |
| **Vorschaubilder pro Reihe** (Thumbnails per row) | Number of columns |
| **Elemente pro Seite** (Items per page) | Pagination |
| **Lightbox** | Full screen view |

### Video/Audio
| Setting | Options |
|-------------|---------|
| **Autoplay** | Yes/no |
| **Steuerelemente** (Controls) | Show/hide |
| **Loop** | Yes/no |
| **Inline** | No full screen |
| **Vorladestufe** (Preload level) | Auto, metadata, none |
| **Untertitel** (Subtitles) | Optional track |
| **Start-/Stoppzeit** (Start/stop time) | In seconds |
| **Vorschaubild** (Preview image) | Replaces the first frame |

Template: `content_element/player`

### Vimeo
- **Vimeo-ID**, autoplay, loop, hide profile/title/author
- Control colours (hex), start time
- **Splash-Screen**: load only on click (data protection)

Template: `content_element/vimeo`

### YouTube
- **YouTube-ID**, extensive player options
- **youtube-nocookie.com** domain (data protection)
- Related videos from the same channel
- **Splash-Screen**: lazy load with a custom image

Template: `content_element/youtube`

---

## 7. Miscellaneous (nested elements, as of Contao 5.3)

### Akkordeon (Accordion)
Several expandable/collapsible sections. Only one section open at a time.

| Setting | Description |
|-------------|-------------|
| **Alle Abschnitte schließen** (Close all sections) | Prevents the first section from opening automatically |

Template: `content_element/accordion`
HTML: `<div class="content-accordion">` with `handorgel__header` buttons and `handorgel__content` regions (ARIA).

### Elementgruppe (Element group)
Groups several content elements into one child element — useful inside sliders or accordions.
Template: `content_element/element_group`

### Content Slider
Slideshow made up of various content elements via Swiper.

| Setting | Description |
|-------------|-------------|
| **Slide-Intervall** (Slide interval) | Milliseconds (0 = disabled) |
| **Übergangsgeschwindigkeit** (Transition speed) | Milliseconds |
| **Slide-Versatz** (Slide offset) | Starting position (from 0) |
| **Kontinuierlich** (Continuous) | Loop |

Template: `content_element/swiper`

---

## 8. Include elements

| Element | Description |
|---------|-------------|
| **Artikel** (Article) | Embeds another article (content elements only, no header) |
| **Inhaltselement** (Content element) | Embeds an existing element as an alias |
| **Formular** (Form) | Inserts a form from the Formulargenerator (Form Generator) |
| **Modul** (Module) | Embeds a frontend module |
| **Kommentare** (Comments) | Enables visitor comments; settings: moderation, BBCode, login requirement, spam protection |
| **Individuelles Template** (Custom template) | Template with custom key/value pairs |
| **Artikelteaser** (Article teaser) | Shows the teaser text of another article with a "Weiterlesen" (Read more) link |

---

## 9. Legacy elements (wrapper system, before Contao 5.3)

### Akkordeon (Accordion, legacy)
Uses the `js_accordion` template in the Seitenlayout (Page layout).

| Mode | Function |
|-------|---------|
| Einzelelement (Single element) | Single section with text and an optional image |
| Umschlag Anfang (Wrapper start) | Opens the accordion section |
| Umschlag Ende (Wrapper end) | Closes the accordion section |

- Settings: section headline (HTML permitted), CSS format, classes for the toggler and the accordion
- Templates: `ce_accordionSingle`, `ce_accordionStart`

### Slider (legacy)
Uses the `js_slider` template in the Seitenlayout.

| Mode | Function |
|-------|---------|
| Umschlag Anfang (Wrapper start) | Opens the slider |
| Umschlag Ende (Wrapper end) | Closes the slider |

- Settings: slide interval, transition speed, slide offset, continuous
- Template: `ce_sliderStart`

---

## 10. Common settings of all content elements

- **Template überschreiben** (Override template): a custom template can be chosen
- **Zugriffsschutz** (Access protection): restriction to Mitgliedergruppen (member groups)
- **CSS-ID/-Klasse** (CSS ID/class): in the expert settings
- **Nur Gästen anzeigen** (Show to guests only): visible only to visitors who are not logged in

---

Sources:
- https://docs.contao.org/5.x/manual/en/article-management/
- https://docs.contao.org/5.x/manual/en/article-management/articles/
- https://docs.contao.org/5.x/manual/en/article-management/content-elements/
- https://docs.contao.org/5.x/manual/en/article-management/content-elements/text-elements/
- https://docs.contao.org/5.x/manual/en/article-management/content-elements/media-elements/
- https://docs.contao.org/5.x/manual/en/article-management/content-elements/link-elements/
- https://docs.contao.org/5.x/manual/en/article-management/content-elements/file-elements/
- https://docs.contao.org/5.x/manual/en/article-management/content-elements/include-elements/
- https://docs.contao.org/5.x/manual/en/article-management/content-elements/legacy-elements/
- https://docs.contao.org/5.x/manual/en/article-management/content-elements/miscellaneous/

## Content slider

**Source:** https://docs.contao.org/5.x/manual/en/article-management/content-elements/content-slider/

This page describes the content element "Content Slider", with which a slider is created from different content elements. Upstream, the page is marked hidden and as a redirect to `/en/article-management/content-elements/legacy-element/`, so it may not resolve as a standalone URL.

For the slider to work, the `js_slider` template must be included in the page layout.

### Configuration fields

- **Operation mode**: selects the operation mode of the slider element. Values: `Envelope beginning` (the element opens a new slider section into which any other content elements can be inserted), `End envelope` (the element closes a slider section previously opened using "Envelope Start").
- **Slide Interval**: defines the time interval between slides in milliseconds (1000 = 1s). `0` disables the automatic change.
- **Transition Speed**: sets the transition speed in milliseconds (1000 = 1s).
- **Slide offset**: starts the slider with a specific slide. Counting starts at 0.
- **Continuous**: creates a continuous slider, starting over when the end is reached.
- **Individual template**: overwrites the default `ce_sliderStart` template.

### HTML Output

The element generates the following HTML code:

```html
<div class="ce_sliderStart first block">

    <div class="content-slider" data-config="5000,300,0,1">
        <div class="slider-wrapper">    
            <div class="ce_text block">
                <figure class="image_container float_above">
                <img src="…" alt="…" itemprop="image">
                </figure>
                <p>…</p> 
            </div>
            <div class="ce_text block">
                <figure class="image_container float_above">
                <img src="…" alt="…" itemprop="image">
                </figure>
                <p>…</p> 
            </div>
        </div>
    </div>

    <nav class="slider-control">
        <a href="#" class="slider-prev">Zurück</a>
        <span class="slider-menu"></span>
        <a href="#" class="slider-next">Vorwärts</a>
    </nav>

</div>
```

