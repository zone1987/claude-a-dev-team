# Contao 5.x – Core extensions

Complete reference from the Contao 5.x manual (German).
Package: part of the "complete installation".

---

## Contents

- [1. News/blog extension (`contao/news-bundle`)](#1-newsblog-extension-contaonews-bundle)
- [2. Calendar extension (`contao/calendar-bundle`)](#2-calendar-extension-contaocalendar-bundle)
- [3. FAQ extension (`contao/faq-bundle`)](#3-faq-extension-contaofaq-bundle)
- [4. Newsletter extension (`contao/newsletter-bundle`)](#4-newsletter-extension-contaonewsletter-bundle)
- [5. Comments (cross-reference)](#5-comments-cross-reference)
- [6. Auflistung / Listing (cross-reference)](#6-auflistung--listing-cross-reference)

## 1. News/blog extension (`contao/news-bundle`)

News items can be managed in the backend and output with frontend modules. Items can be structured freely with content elements.

### 1.1 Nachrichtenarchive (News archives)

Archives organise news items by topic or language.

**Title and redirect:**
- **Titel** (Title): backend display
- **Weiterleitungsseite** (Redirect page): target for "Weiterlesen" (Read more) links (should contain a Nachrichtenleser module)

**Access protection:** protect the archive, permitted Mitgliedergruppen (member groups).

**Comments:**
| Setting | Description |
|-------------|-------------|
| Enable comments | Activation switch |
| Notification to | System admin, article author or both |
| Sort order | Ascending (oldest first) or descending |
| Comments per page | Pagination limit |
| Moderate | Approval before publication |
| Allow BBCode | [b], [i], [u], [img], [code], [color], [quote], [url], [email] |
| Login required to comment | Registered members only |
| Disable spam protection | For authenticated users |

**RSS feeds:** RSS 2.0, Atom or JSON. Configuration via the "News-Feed" page type.

### 1.2 Nachrichtenbeiträge (News items)

Settings:

| Field | Description |
|------|-------------|
| **Titel** (Title) | Article headline |
| **Beitrag hervorheben** (Feature item) | Featured status (across archives) |
| **Nachrichtenalias** (News alias) | URL reference |
| **Autor** (Author) | Can be changed |
| **Datum/Uhrzeit** (Date/time) | Publication date |

**Redirect target:**
- Default (the archive's default page)
- Page / article / custom URL
- Link text, canonical URL (as of 5.3), new window

**Metadata:**
- Meta title, robots tag (index/follow/noindex/nofollow), meta description (150–300 characters)
- Google search result preview

**Content:**
- Subheadline, teaser text
- Image with alignment (top/bottom/left/right), scaling modes, lightbox, alt text, link
- Enclosures (files for RSS export and download)

**Expert settings:**
- CSS class
- Disable comments
- Search indexer (as of 5.6): default / always index / never index

**Publication:** manual, Anzeigen ab (Show from), Anzeigen bis (Show until).

### 1.3 Frontend modules

#### Nachrichtenliste (News list)
Shows items from one or more archives.

| Setting | Description |
|-------------|-------------|
| Nachrichtenarchive | Source archives |
| Nachrichtenleser (News reader) | Switch automatically when an item is selected |
| Number of items | Limit |
| Featured items | All / featured only / skip featured / featured first |
| Sort order | Date ascending/descending, headline ascending/descending, random |
| Skip items | Offset |
| Items per page | Pagination |

**Templates:**
- `news_full` – complete article (recommended for the Nachrichtenleser)
- `news_latest` – metadata, image, headline, teaser, "Weiterlesen"
- `news_short` – metadata, headline, teaser, "Weiterlesen"
- `news_simple` – date and headline

#### Nachrichtenleser (News reader)
Shows individual items via the URL alias (permalink).
Example: `www.example.com/nachricht/form-folgt-funktion.html`
Returns HTTP 404 if no article is found.

| Setting | Description |
|-------------|-------------|
| Nachrichtenarchive | Archives to be searched |
| Current URL for canonical links | As of Contao 5.3 |
| Overview page | Page for the "Zurück zur Übersicht" (Back to the overview) link |

#### Nachrichtenarchiv (News archive)
Lists all items of a period (day/month/year).
- Archive format: day, month or year
- "No period selected": hide the module / show the current period / show all

#### Nachrichtenarchiv-Menü (News archive menu)
Navigation menu by day/month/year.
- Show item count, sort order, redirect page

**Caution:** only one reader module is allowed per page. Do not build news lists into Seitenlayouts (page layouts) (avoid the auto switch).

---

## 2. Calendar extension (`contao/calendar-bundle`)

Manages past and future events. Supports recurring dates.

### 2.1 Terminarchive (Event archives)

**Comments:** identical configuration to the news archives.

**RSS feeds:**
| Setting | Description |
|-------------|-------------|
| Format | RSS 2.0 or Atom |
| Export type | Teaser text or complete entries |
| Max. items | Typically 25 |
| Base URL | For multi-domain setups |

### 2.2 Termine (Events)

| Field | Description |
|------|-------------|
| **Titel** (Title) | Event name |
| **Zeit hinzufügen** (Add time) | Enables time information |
| **Start-/Endzeit** (Start/end time) | Optional (without an end: open end) |
| **Start-/Enddatum** (Start/end date) | Multi-day events |
| **Veranstaltungsort** (Venue) | Name and address |
| **Teasertext** (Teaser text) | Short version for lists |

**Recurrences:**
- Can be enabled; interval: day(s), week(s), month(s), year(s)
- Number of recurrences; hide automatically after N recurrences

**Metadata and enclosures:** analogous to news items.

### 2.3 Frontend modules

#### Kalender (Calendar)
- Standard calendar (`cal_default`) – large, clickable events
- Mini calendar (`cal_mini`) – compact with day links
- Shortened presentation for multi-day events
- Featured events: all / featured only / skip featured
- Redirect page for the mini calendar

#### Eventleser (Event reader)
Shows individual events via a permalink.
Example: `www.example.com/event/european-design-awards.html`

**Event templates:**
- `event_full` – complete (recommended for the reader)
- `event_list` – title, date/time, event text
- `event_teaser` – title, date/time, teaser, "Weiterlesen"
- `event_upcoming` – date and title

#### Eventliste (Event list)
Lists by period; display format:
- Event list (period), upcoming events (preview), past events (retrospective)

#### Eventliste-Menü (Event list menu)
Navigation by day/month/year. Should use the same calendars as the Eventliste.

---

## 3. FAQ extension (`contao/faq-bundle`)

Manages frequently asked questions in categories.

### 3.1 FAQ categories

**Settings:**
- **Titel** (Title, backend)
- **Überschrift** (Headline, frontend)
- **Weiterleitungsseite** (Redirect page) (should contain an FAQ-Leser module)
- **Comments**: identical configuration to news

### 3.2 Questions

| Field | Description |
|------|-------------|
| **Frage** (Question) | The question |
| **FAQ-Alias** | URL reference |
| **Autor** (Author) | Can be changed |
| **Antwort** (Answer) | Rich text editor |
| **Bild** (Image) | Optional, with scaling modes and alignment |
| **Anlagen** (Enclosures) | Files for download |

**Metadata:** meta title, robots tag, meta description, Google preview.

### 3.3 Frontend modules

#### FAQ-Liste (FAQ list)
Shows questions from one or more categories as a list with links.
```html
<div class="mod_faqlist block">
  <ul><li><a href="…">…</a></li></ul>
</div>
```

#### FAQ-Leser (FAQ reader)
Shows the answer to a particular question via a permalink.
Example: `example.com/frage/kann-ich-eigene-php-skripte-verwenden.html`
Returns HTTP 404 if not found.

#### FAQ-Seite (FAQ page)
Shows all questions and answers from the selected categories on a single page.
```html
<div class="mod_faqpage block">
  <article>
    <h2>FAQ</h2>
    <section><h3>…</h3><div class="ce_text block">…</div></section>
    <p class="toplink"><a href="#top">Nach oben</a></p>
  </article>
</div>
```

---

## 4. Newsletter extension (`contao/newsletter-bundle`)

Manages newsletters and recipient lists. Dispatch directly from the backend. Double opt-in integrated.

### 4.1 Verteiler (Distribution list / newsletter archive)

**Settings:**
| Field | Description |
|------|-------------|
| **Titel** (Title) | Backend reference |
| **Weiterleitungsseite** (Redirect page) | Target for frontend module links |

**E-mail templates (as of 5.3):**
- `mail_default` – HTML 3.2 for broad compatibility
- `mail_responsive` – modern responsive design

Template variables: `$this->charset`, `$this->title`, `$this->body`, `$this->css`

**Sender configuration:**
- Sender e-mail (mandatory field)
- Sender name
- Mailer transport (for multi-domain setups)

### 4.2 Newsletter content

| Setting | Description |
|-------------|-------------|
| **Betreff** (Subject) | E-mail subject line |
| **Newsletter-Alias** | URL-friendly identifier |
| **HTML-Inhalt** (HTML content) | Rich text with preheader text (5.3+, 40–130 characters) |
| **Text-Inhalt** (Text content) | Plaintext fallback |
| **Anlagen** (Enclosures) | Files for dispatch |

**Personalisation with Simple Tokens:**
```
##firstname## ##lastname##
{if gender=="male"}Herr {elseif gender=="female"}Frau {else}Damen und Herren{endif}
```

**Expert settings:**
- Text-only mode
- External images (prevents embedding in the HTML version)

### 4.3 Subscriber management

- Records contain only the e-mail address and activation status (data protection)
- Double opt-in: confirmation e-mail before activation
- Manual activation possible in the backend
- CSV import: separators comma, semicolon, tab, line break

### 4.4 Dispatch process

**Server limit configuration:**
- E-mails per cycle
- Waiting time between cycles (seconds)
- Offset for an interrupted dispatch

Example: 100 e-mails/minute → 10 e-mails every 6 seconds

**Resuming an interrupted dispatch:**
1. Check the system log (category: `NEWSLETTER_X`)
2. Note the number of e-mails sent
3. Enter this value as the offset

### 4.5 Frontend modules

#### Abonnieren (Subscribe)
- Select the Verteiler, hide the distribution list menu, spam protection
- Custom text (GDPR notices)
- Redirect page
- Confirmation e-mail with `##channel##`, `##domain##`, `##link##`

#### Kündigen (Unsubscribe)
- Verteiler, hide the menu, spam protection
- Redirect page
- Confirmation e-mail with `##channel##`, `##domain##`

#### Newsletterliste (Newsletter list)
Shows all sent newsletters (sorted by date, newest first).

#### Newsletterleser (Newsletter reader)
An individual newsletter via a permalink.
Example: `www.example.com/newsletterleser/newsletteralias.html`
Returns HTTP 404 if not found.

---

## 5. Comments (cross-reference)

The comment function is embedded as an include content element and is not a standalone core extension in its own right. Comment settings are configured per archive (news, calendar, FAQ) or directly in the "Kommentare" (Comments) content element.

Settings: sorting, pagination, moderation, BBCode, login requirement, spam protection.

---

## 6. Auflistung / Listing (cross-reference)

The Auflistung (Listing) module is located under Layout > Modulverwaltung (Module management) > Anwendungen (Applications) and is not a separate core bundle but part of the core. See the layout reference for details.

---

Sources:
- https://docs.contao.org/5.x/manual/de/core-erweiterungen/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/nachrichten/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/nachrichten/nachrichtenverwaltung/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/nachrichten/frontend-module/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/kalender/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/kalender/terminverwaltung/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/kalender/frontend-module/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/faq/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/faq/faq-verwaltung/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/faq/frontend-module/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/newsletter/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/newsletter/newsletter-verwaltung/
- https://docs.contao.org/5.x/manual/de/core-erweiterung/newsletter/frontend-module/
