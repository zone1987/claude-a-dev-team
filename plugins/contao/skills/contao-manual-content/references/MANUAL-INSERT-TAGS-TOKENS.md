# Contao 5.x – Insert tags & Simple Tokens

Complete reference from the Contao 5.x manual (German).

---

## Contents

- [Insert tags](#insert-tags)
- [1. Link tags](#1-link-tags)
- [2. Member properties](#2-member-properties)
- [3. Page properties](#3-page-properties)
- [4. Environment variables](#4-environment-variables)
- [5. Include tags](#5-include-tags)
- [6. Miscellaneous](#6-miscellaneous)
- [7. Nested insert tags](#7-nested-insert-tags)
- [8. Insert tag flags](#8-insert-tag-flags)
- [9. Basic entities](#9-basic-entities)
- [Simple Tokens](#simple-tokens)

## Insert tags

Insert tags are placeholders of the form `{{keyword}}` or `{{keyword::parameter}}` that are replaced by their values when a page is rendered. They can be used anywhere in Contao.

---

## 1. Link tags

| Tag | Description |
|-----|-------------|
| `{{link::*}}` | HTML link; parameter: page ID, alias or absolute URL |
| `{{link::login}}` | Link to the login page of the current frontend user |
| `{{link_open::*}}` / `{{link_close}}` | Opening and closing link tag |
| `{{link_url::*}}` | The URL only |
| `{{link_title::*}}` | Title attribute of the page |
| `{{link_name::*}}` | Name of the page |
| `{{article::*}}` | Link to an article (ID or alias) |
| `{{article_open::*}}` / `{{article_url::*}}` / `{{article_title::*}}` | Article variants |
| `{{news::*}}` | Link to a news item |
| `{{news_open::*}}` / `{{news_url::*}}` / `{{news_title::*}}` / `{{news_feed::*}}` | News variants |
| `{{event::*}}` | Link to an event |
| `{{event_open::*}}` / `{{event_url::*}}` / `{{event_title::*}}` / `{{calendar_feed::*}}` | Event variants |
| `{{faq::*}}` | Link to an FAQ question |
| `{{faq_open::*}}` / `{{faq_url::*}}` / `{{faq_title::*}}` | FAQ variants |

### Link parameters
- `::absolute` – output as an absolute URL
- `::blank` – opens in a new window with `target="_blank" rel="noreferrer noopener"`

---

## 2. Member properties

Access fields of the `tl_member` table of the logged-in frontend user.

| Tag | Description |
|-----|-------------|
| `{{user::*}}` | Any field from `tl_member` |
| `{{user::firstname}}` | First name |
| `{{user::lastname}}` | Last name |
| `{{user::company}}` | Company |
| `{{user::phone}}` / `{{user::mobile}}` / `{{user::fax}}` | Phone numbers |
| `{{user::email}}` | E-mail address |
| `{{user::website}}` | Website URL |
| `{{user::street}}` | Street |
| `{{user::postal}}` | Postcode |
| `{{user::city}}` | City |
| `{{user::country}}` | Country |
| `{{user::username}}` | User name |

---

## 3. Page properties

Access fields of the `tl_page` table of the current page.

| Tag | Description |
|-----|-------------|
| `{{page::*}}` | Any field from `tl_page` |
| `{{page::id}}` | Current page ID |
| `{{page::alias}}` | Current page alias |
| `{{page::title}}` | Seitenname (Page name) |
| `{{page::pageTitle}}` | Seitentitel (Page title) |
| `{{page::description}}` | Page description |
| `{{page::language}}` | Page language |
| `{{page::parentAlias}}` / `{{page::parentTitle}}` / `{{page::parentPageTitle}}` | Parent page |
| `{{page::mainAlias}}` / `{{page::mainTitle}}` / `{{page::mainPageTitle}}` | Main parent page |
| `{{page::rootTitle}}` / `{{page::rootPageTitle}}` | Website name and title |

---

## 4. Environment variables

| Tag | Description |
|-----|-------------|
| `{{env::host}}` | Current host name (e.g. example.com) |
| `{{env::url}}` | Host name with protocol (e.g. https://www.example.com) |
| `{{env::path}}` | Base URL with the path to the Contao directory |
| `{{env::request}}` | Current request string (e.g. news/items/welcome.html) |
| `{{env::ip}}` | IP address of the visitor |
| `{{env::referer}}` | URL of the previously visited page |
| `{{env::files_url}}` | Static URL for the upload directory |
| `{{env::assets_url}}` | Static URL for the assets directory |

---

## 5. Include tags

| Tag | Description |
|-----|-------------|
| `{{insert_article::*}}` | Embed an article by ID or alias |
| `{{insert_content::*}}` | Embed a content element by ID |
| `{{insert_module::*}}` | Embed a module by ID |
| `{{insert_form::*}}` | Embed a form by ID |
| `{{article_teaser::*}}` | Teaser text of an article |
| `{{news_teaser::*}}` | Teaser of a news item |
| `{{event_teaser::*}}` | Teaser of an event |
| `{{file::*}}` | Embedding of .php or .html5 files from templates/; UUID reference possible |

---

## 6. Miscellaneous

| Tag | Description |
|-----|-------------|
| `{{fragment::*}}` | Is rendered as an ESI fragment |
| `{{date}}` | Current date (global format) |
| `{{date::*}}` | Date with a custom format (PHP date function) |
| `{{format_date::*::*}}` | Format a UNIX timestamp or a standardised date |
| `{{convert_date::*::*::*}}` | Convert a date from one format into another |
| `{{last_update}}` / `{{last_update::*}}` | Last update timestamp |
| `{{email::*}}` | Encoded e-mail link |
| `{{email_open::*}}` / `{{email_close}}` | Encoded e-mail link parts |
| `{{email_url::*}}` | Encoded e-mail address only |
| `{{form_session_data::*}}` | Access to submitted form field values |
| `{{lang::*}}...{{lang}}` | Mark up text in a foreign language |
| `{{abbr::*}}...{{abbr}}` | Mark up abbreviations |
| `{{acronym::*}}...{{acronym}}` | Mark up acronyms |
| `{{iflng::*}}` | Show content only for certain language(s) |
| `{{ifnlng::*}}` | Show content for languages other than the one specified |
| `{{image::*}}` | Image preview with width, height, alt, class, rel, mode |
| `{{picture::*}}` | Responsive `<picture>` element with size configuration |
| `{{figure::*}}` | `<figure>` element with `<picture>` and `<figcaption>` |
| `{{label::*}}` | Translation from the language files |
| `{{trans::*::*::*}}` | Symfony translation system |
| `{{version}}` | Current Contao version |
| `{{toggle_view}}` | Switches between the mobile and desktop layout |
| `{{br}}` | HTML line break `<br>` |
| `{{asset::*::*}}` | Embed CSS/JavaScript paths from packages |
| `{{empty}}` | Empty string |

---

## 7. Nested insert tags

Tags that output IDs or aliases can be nested:

```
{{link::{{page::id}}::absolute}}   → Link zur aktuellen Seite (absolut)
{{link_url::{{page::id}}}}#anchor  -> relative link with an anchor
```

**Caution:** avoid endless loops (e.g. `{{insert_article::{{page::alias}}}}`) — a page crash is possible.

---

## 8. Insert tag flags

Flags process the tag output further. Several flags can be combined:

```
{{ua::browser|uncached}}
{{page::title|standardize|strtoupper}}
```

| Flag | Description |
|------|-------------|
| `refresh` | Regenerate the output on every request |
| `attr` | Special characters as HTML entities (for attributes) |
| `urlattr` | Like `attr`, additionally URL-encodes colons (prevents `javascript:` protocols) |
| `addslashes` | Backslash before certain characters |
| `standardize` | Standardise the output (e.g. page aliases) |
| `ampersand` | Convert & into entities |
| `specialchars` | Convert special characters into entities |
| `nl2br` | Insert HTML line breaks before line endings |
| `strtolower` | Lower case |
| `utf8_strtolower` | Unicode-aware lower case |
| `strtoupper` | Upper case |
| `utf8_strtoupper` | Unicode-aware upper case |
| `ucfirst` | Capitalise the first letter |
| `lcfirst` | Lower-case the first letter |
| `ucwords` | Capitalise the first letter of every word |
| `trim` | Remove whitespace at both ends |
| `ltrim` | Remove whitespace at the beginning |
| `rtrim` | Remove whitespace at the end |
| `utf8_romanize` | Convert into Roman characters |
| `encodeEmail` | Encode e-mail addresses |
| `number_format` | Format a number (no decimal places) |
| `currency_format` | Format a currency (two decimal places) |
| `readable_size` | Convert into a readable format |
| `urlencode` | URL-encode |
| `rawurlencode` | RFC 3986 encoding |
| `flatten` | Array into a comma-separated key:value list |

---

## 9. Basic entities

Special syntax for HTML entities (when `basicEntities` is enabled via the DCA):

| Syntax | Entity | Purpose |
|--------|--------|-------|
| `[&]` | `&amp;` | Ampersand |
| `[lt]` | `&lt;` | Less-than |
| `[gt]` | `&gt;` | Greater-than |
| `[nbsp]` | `&nbsp;` | Non-breaking space |
| `[-]` | `&shy;` | Soft hyphen |
| `[zwsp]` | `&ZeroWidthSpace;` | Zero-width space |
| `[lsqb]` | `&lsqb;` | Opening square bracket |
| `[rsqb]` | `&rsqb;` | Closing square bracket |
| `[{]` / `[}]` | `{{` / `}}` | Display insert tag syntax in the frontend |

---

## Simple Tokens

Simple Tokens are placeholders similar to insert tags, but the area of use is determined by the respective function (developer). As of Contao 4.10 they are based on the Symfony Expression Language.

### Syntax

- **Output:** `##tokenname##`
- **Condition:** `{if tokenname=="wert"}…{endif}` (no hashes in conditions, curly braces instead)

### Available standard tokens

| Token | Description | Module |
|-------|-------------|-------|
| `##tstamp##` | Current timestamp | General |
| `##flang##` | Current language | General |
| `##domain##` | Current domain | Newsletter |
| `##link##` | Newsletter link | Newsletter |
| `##channels##` | Subscribed channels | Newsletter |

### Areas of use

- User registration and password recovery modules
- Newsletter management (readers, subscriptions, cancellations)
- Extensions: Notification Center, Isotope eCommerce, Leads, MetaModels
- Insert tag placeholders

### Practical application

Dynamic file names: `datei_von_##tstamp##.pdf`
File paths: `files/data/##form_broschuere##.pdf`

### Condition operators

| Operator | Function |
|----------|---------|
| `==` / `!=` | Equality comparison |
| `===` / `!==` | Strict type comparison |
| `<` / `>` / `<=` / `>=` | Comparison operators |
| `&&` / `\|\|` | Logical AND/OR (as of 4.10) |
| `in` / `not in` | Array operations (as of 4.10) |
| `contains` / `starts with` / `ends with` | String comparison (as of 4.10) |
| `matches` | Regex pattern (as of 4.10) |

---

Sources:
- https://docs.contao.org/5.x/manual/en/article-management/insert-tags/
- https://docs.contao.org/5.x/manual/en/article-management/simple-tokens/
