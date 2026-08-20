# Contao 5.x — Seitenstruktur (Page Structure)

Sources:
- https://docs.contao.org/5.x/manual/de/seitenstruktur/
- https://docs.contao.org/5.x/manual/de/seitenstruktur/seiten-als-zentrale-elemente/
- https://docs.contao.org/5.x/manual/de/seitenstruktur/mehrsprachige-webseiten/
- https://docs.contao.org/5.x/manual/de/seitenstruktur/multidomain-betrieb/

---

## Contents

- [Pages as central elements](#pages-as-central-elements)
- [Page types](#page-types)
- [Multi-domain operation](#multi-domain-operation)
- [Multilingual websites](#multilingual-websites)

## Pages as central elements

Contao is a **page-based CMS**. The Seitenstruktur (Page Structure) is the central element:

- Visitors call up pages, not individual posts
- Pages are called up in the frontend via their **Alias**
- Hierarchical nesting is possible (parent/child pages)
- Navigation menus are generated automatically
- Properties are **inherited** by subpages (layout, access rights)

### Analogy

A page works like a television programme: editors create contributions (content), an editor-in-chief decides on publication (page structure and access rights). Content only appears in the frontend once it is assigned to a page.

### Components of a page

Every page knows:
- Which articles are linked to it
- Which **Seitenlayout** (Page layout) is used for the presentation
- Whether it may be cached
- Which users are allowed to access it

The Seitenlayout divides the page into layout sections. These contain frontend modules that generate HTML in order. CSS is embedded in the Seitenlayout (Theme-Manager).

---

## Page types

### Overview of all page types

| Page type | Function |
|-----------|---------|
| **Website-Startseite** (Website start page) | Starting point of a website; enables multi-domain operation and multilingualism |
| **Reguläre Seite** (Regular page) | Normal content page, comparable to a static HTML file |
| **Interne Weiterleitung** (Internal redirect) | Redirects to another page within the same installation |
| **Externe Weiterleitung** (External redirect) | Redirects to an external URL or another domain |
| **Abmelden** (Log out) | Creates a logout link for protected areas (with an optional redirect) |
| **401 Nicht authentifiziert** (401 Not authenticated) | Appears for visitors who are not logged in and have no access to protected pages |
| **403 Zugriff verweigert** (403 Access denied) | Appears for logged-in visitors without sufficient rights |
| **404 Seite nicht gefunden** (404 Page not found) | Appears when non-existent pages are called up |
| **503 Dienst nicht verfügbar** (503 Service unavailable) | Appears when a root page is in maintenance mode |
| **News-Feed** | Creates RSS, Atom or JSON feeds from news archives |

### Website-Startseite (Website start page / root page)

The start page marks the entry point of a website. It defines:
- Domain assignment (for multi-domain operation)
- Language of the website
- Language fallback (yes/no)
- URL prefix (e.g. `/de/` for multilingual sites)

One Contao installation can have several Website-Startseiten (multi-domain, multilingualism).

---

## Multi-domain operation

### Basic principle

Multi-domain operation = one Contao installation is reachable under **several domains** and delivers **different content** depending on the domain.

**True multi-domain operation requires:**
- Several domains AND
- Several Website-Startseiten in the Seitenstruktur (one per domain)

**Not true multi-domain operation**: the same website reachable under several domains → problem: duplicate content for search engines. Solution: choose one primary domain, redirect the others.

### Redirect example (`.htaccess`)

```apache
RewriteEngine On
RewriteCond %{HTTP_HOST} ^www\.example\.com [NC]
RewriteRule (.*) http://www.example.org/$1 [R=301,L]
```

### Application example: agency with several client domains

Domains: `firma.at`, `firma.ch`, `firma.de` — all point to one Contao installation.

Three Website-Startseiten in the Seitenstruktur, each with its domain entered:

| Starting point | Domain | Website called up |
|-----------|--------|-------------------|
| Austria | firma.at | Austrian page only |
| Switzerland | firma.ch | Swiss page only |
| Germany | firma.de | German page only |

**Important**: `www.firma.at/produkte.html` returns 404 if "Produkte" only exists in the Swiss website.

---

## Multilingual websites

### Contao's approach

Contao exclusively supports the approach of **separate websites per language** in the Seitenstruktur. Each language = its own Website-Startseite.

The structures may differ (the German and English versions do not have to have identical pages).

### URL prefix for languages

To include the language in the URL (e.g. `www.example.com/de/`):

Edit the Website-Startseite → enter the **URL-Präfix** (URL prefix, e.g. `de`).

Result:
- `www.example.com/` = English (without prefix)
- `www.example.com/de/` = German
- `www.example.com/fr/` = French

### Clearing the cache after changes

```bash
vendor/bin/contao-console cache:clear --env=prod --no-warmup
vendor/bin/contao-console cache:warmup --env=prod
```

### Finding the right starting point

When a page is called up, Contao checks four possibilities (in this order):

1. Is there a page matching the visitor's **domain AND language**?
2. Is there a page that **matches the domain** and has **Sprachfallback** (language fallback) enabled?
3. Is there a page **without a domain** that matches the visitor's **language**?
4. Is there a page **without a domain** with **Sprachfallback**?

### Practical example: two-domain scenario

Domains: `www.example.com` (company site), `www.example.org` (private site)

Required starting points:

| Page | Domain | Language | Fallback |
|-------|--------|---------|---------|
| Company German | – | de | – |
| Company English | – | en | yes |
| Private | example.org | de | yes |

**Routing table**:

| Domain | Browser language | Target | Match type |
|--------|----------------|------|------------|
| www.example.com | German | Company German | Language |
| www.example.com | English | Company English | Language |
| www.example.com | Spanish | Company English | Fallback |
| www.example.org | any | Private | Domain |

**Without Sprachfallback** the private site would only be accessible to German-speaking visitors. Spanish-speaking visitors would see "No pages found".

### Important note

Third-party extensions can offer alternative multilingualism approaches (e.g. content in a single website with automatic translation).
