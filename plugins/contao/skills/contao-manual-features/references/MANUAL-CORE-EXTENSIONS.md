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

## 5. Comments

Lets visitors leave comments, and can also run a guestbook. Documented as a **content element**
rather than a bundle of its own: the `/core-extensions/comments/` URL redirects to the
include-elements page. Comment settings also exist per news archive, calendar and FAQ category, and
carry the same fields.

### 5.1 Comment settings

- **Sort order**: a guestbook usually shows the newest entry first (descending), comments the oldest
  (ascending). Values: ascending, descending.
- **Items per page**: comments per page, with an automatic page break when needed. `0` disables it.
- **Moderate**: comments appear only after being enabled in the backend.
- **Allow BBCode**: visitors may format their comments. Supported: `[b]`, `[i]`, `[u]`, `[img]`,
  `[code]`, `[color=#f00]`, `[quote]`, `[quote=Tim]`, `[url]`, `[url=http://example.com]`,
  `[email]`, `[email=info@example.com]`.
- **Require login to comment**: only logged-in members may comment. Comments already submitted stay
  visible to everyone.
- **Disable spam protection**: not recommended. Since Contao 4.4 the security question is only shown
  to spambots, so it costs a real visitor nothing.

### 5.2 Template settings

- **Comments template**: the template for the individual posts.
- **Content element template**: overwrites the default `ce_comments`.

### 5.3 Managing comments

Comments are managed centrally through the **Comments** module in the backend **Content** group. All
of them appear there, whether they belong to a content element, an article or a blog post, and can be
filtered by origin or parent element. With moderation on, an administrator approves each one before
it is published.

Source: https://docs.contao.org/5.x/manual/en/article-management/content-elements/include-elements/#comments

---

## 6. Listing

Adds a list of database records that visitors can sort, filter and search. The basis is any table in
the database, `tl_member` for example. Documented as a **front-end module** under
**Layout > Module management > Applications**: the `/core-extensions/listing/` URL redirects there.

### 6.1 Module configuration

- **Table**: the table whose records are listed.
- **Fields**: the fields shown in the list, comma separated.
- **Condition**: a filter for the records. The module does nothing but a database query, so
  SQL-compliant code works (`published=1`), and insert tags are allowed (`user={{user::id}}`).
- **Searchable fields**: marking fields searchable makes Contao build a search form automatically.
- **Order by**: the default sort columns, comma separated.
- **Items per page**: above `0`, results are spread over several pages.
- **Details page fields**: entering one or more adds an icon per row that opens a detail view, which
  can show fields that would not fit the list.
- **Details page condition**: a filter for the detail page's records.

### 6.2 Template settings

- **List template**: the template for the list view.
- **Detail page template**: the template for the detail page.

Source: https://docs.contao.org/5.x/manual/en/layout/module-management/applications/#listing

---

## 7. Settings that repeat across the extensions

Four blocks appear on nearly every archive, item and module. They are written once here, because an
editor needs the exact label and the exact set of values.

### 7.1 Comment settings, per archive

News archives, calendars and FAQ categories all carry this block, identical in each:

- **Enable comments**: activates the function for that archive, calendar or category.
- **Notify**: who hears about a new comment. Values: the system administrator, the author of the
  post, or both.
- **Sort order**: ascending is typical for blog comments.
- **Comments per page**: a page break is created when needed.
- **Moderate comments**: approval in the backend before publication.
- **Allow BBCode**: the twelve tags listed in section 5.1.
- **Require login to comment**: existing comments stay visible to all.
- **Disable spam protection**: available where login is required.

### 7.2 Robots tag, per reader-driven item

A news item, an event and an FAQ each inherit the robots tag from the page holding the reader
module, and may override it:

- **Default (-)**: use the setting from the page with the reader module.
- **index**: add the page to the search index.
- **follow**: follow the links on the page.
- **noindex**: keep the page out of the index.
- **nofollow**: do not follow the links.

`index,follow` lets search engines include the item; `noindex,nofollow` instructs them to exclude it.

### 7.3 Search indexer, Contao 5.6 and later

The same three-way choice on a news item, an event and an FAQ:

- **Default**: index according to the reader page's setting; where that is unset, according to the
  metadata robots tag.
- **Always index**: include the item even when its robots tag says `noindex`, or the reader page says
  otherwise.
- **Never index**: exclude it even when its robots tag says `index`.

An FAQ's metadata and search-indexer settings can only be adjusted when the category has a redirect
page selected.

### 7.4 Image scaling, wherever an image is configured

**Relative format**: `Proportional` fits the longer side and scales proportionally; `Fit to frame`
fits the shorter side.

**Exact format**, nine crop positions: `Important part` (as marked in the file manager), then
`Left/Top`, `Middle/Top`, `Right/Top`, `Left/Center`, `Middle/Center`, `Right/Middle`,
`Left/Bottom`, `Middle/Bottom`, `Right/Bottom`. Each preserves that part of a landscape image and
the corresponding part of a portrait image.

### 7.5 Newsletter dispatch, the numbers that matter

- **Mails per cycle**, **Waiting time in seconds**, **Offset**: the three fields that pace a send.
- **The manual's worked example**: a server limit of 100 mails per minute and 10,000 recipients means
  10 mails every 6 seconds, so the whole send takes 100 minutes.
- **Resuming an interrupted send**: filter the system log (**System > System Log**) for category
  `NEWSLETTER_X`, where X is the newsletter ID, read how many went out, and enter that as the offset.
- **Double opt-in** is on by default: every subscriber gets a confirmation link, without which the
  subscription cannot complete. The manual notes this satisfies section 7 paragraph 2 numbers 2 and 3
  of the German Law against Unfair Competition (UWG).

### 7.6 Reader modules, the constraint that breaks pages

**Only one reader module per page**, whatever its type. Two of them make one or the other return a
404 through an alias conflict.

And a list module with a reader attached does not belong in the page layout: that creates a reader
instance at every layout position and stops other reader modules working.

## Source

Distilled from the [Contao 5 user manual](https://docs.contao.org/5.x/manual/en/core-extensions/),
the 14 pages under `core-extensions/`, retrieved 2026-08-21:

- https://docs.contao.org/5.x/manual/en/core-extensions/
- https://docs.contao.org/5.x/manual/en/core-extensions/news/
- https://docs.contao.org/5.x/manual/en/core-extensions/news/news-management/
- https://docs.contao.org/5.x/manual/en/core-extensions/news/frontend-modules/
- https://docs.contao.org/5.x/manual/en/core-extensions/calendar/
- https://docs.contao.org/5.x/manual/en/core-extensions/calendar/calendar-management/
- https://docs.contao.org/5.x/manual/en/core-extensions/calendar/frontend-modules/
- https://docs.contao.org/5.x/manual/en/core-extensions/faq/
- https://docs.contao.org/5.x/manual/en/core-extensions/faq/faq-management/
- https://docs.contao.org/5.x/manual/en/core-extensions/faq/frontend-modules/
- https://docs.contao.org/5.x/manual/en/core-extensions/newsletter/
- https://docs.contao.org/5.x/manual/en/core-extensions/newsletter/newsletter-management/
- https://docs.contao.org/5.x/manual/en/core-extensions/newsletter/frontend-modules/

`core-extensions/comments/` and `core-extensions/listing/` are redirect stubs; their content lives at
the two targets cited in sections 5 and 6.
