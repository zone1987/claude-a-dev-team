# Page types

Every page type Contao 5 offers, with every field the backend shows for it. The type is chosen from
the **Seitentyp** (Page type) dropdown when a page is created.

## Contents

- [Fields common to most types](#fields-common-to-most-types)
- [Website root](#website-root)
- [Regular page](#regular-page)
- [Internal redirect](#internal-redirect)
- [External redirect](#external-redirect)
- [Logout](#logout)
- [401 Not authenticated](#401-not-authenticated)
- [403 Access denied](#403-access-denied)
- [404 Page not found](#404-page-not-found)
- [503 Service unavailable](#503-service-unavailable)
- [News feed](#news-feed)
- [Source](#source)

## Fields common to most types

These groups appear on almost every page type with the same meaning. Each type below lists only
what it adds or changes.

### Name and type

- **Page name**: shown in the navigation, and the fallback for the page title.
- **Page type**: the type itself, chosen from the dropdown.

### Routing

- **Page alias**: the unique, meaningful reference used to reach the page in a browser. Left empty
  on creation, Contao generates it.
- **Route path**: a preview of the final path, placeholders included, that matches this page.
- **Route priority**: affects the order in which routes are matched.

### Metadata

- **Page title**: goes into the `<title>` tag and often appears in search results. Not more than 65
  characters. Falls back to the page name.
- **Robots tag**: how search engines treat the page. Values: `index`, `follow`, `noindex`,
  `nofollow`. Default `index,follow`.
- **Description of the page**: indexed by search engines and shown in results. 150 to 300 characters
  recommended.

### Access protection

- **Protect page**: restricts front-end access. Unselected, protection is inherited from the parent.
- **Allowed member groups**: which member groups may access the page.

### Layout settings

- **Assign a layout**: assigns a page layout, which applies to sub-pages without one of their own.
- **Page layout**: every available layout, grouped by theme.
- **Subpage layout**: `Inherit page layout` by default, or a separate layout for sub-pages.

### Cache settings

- **Set cache timeouts**: assigns cache times. Unselected, they are inherited from the parent.
- **Private cache timeout** (client cache): seconds after which the browser treats the page as stale.
- **Shared cache timeout** (server cache): seconds after which a shared cache treats it as stale.
- **Always load from shared cache**: serves the cached page even to a logged-in member, which
  disables personalisation.

### Access rights

- **Assign access rights**: assigns backend permissions. Unselected, they are inherited.
- **Owner**, **Group**, **Access rights**: the page's owner, its group, and the rights per access
  level.

### Expert settings

- **CSS class**: applied to the `body` tag and in navigation modules.
- **Show in HTML sitemap**: values `Default`, `Always display`, `Never display`.
- **Hide in menu**: the page leaves the menu but stays reachable by direct link or in a front-end
  module.

### Keyboard navigation

- **Shortcut keys**: a single character that reaches the page from the keyboard.

### Publication

- **Publish page**: makes the page live.
- **Show from** / **Show until**: activates and deactivates on a date.

## Website root

The starting point of a website inside the page structure. One Contao instance can manage several
websites, in different languages or entirely independent under different domains.

Adds these groups on top of the common ones:

### URL settings

- **Domain name**: for a site that must answer on a specific domain such as `company.com`.
- **Protocol**: set accordingly where the site is reachable over HTTPS.
- **URL prefix**: an optional prefix applied to every page alias below this root.
- **URL suffix**: appended to the alias. Can be changed or removed.
- **Alias settings**: values `Unicode numbers and small letters`, `Unicode numbers and letters`,
  `ASCII numbers and small letters`, `ASCII numbers and letters`. Default not stated upstream.
- **Enable folder URLs**: puts the page hierarchy's aliases into the URL.

### Language settings

- **Language**: the language of this root, recorded as the primary subtag per ISO 639-1.
- **Language fallback**: marks this root as the fallback, the welcome page in effect.
- **Disable language redirect**: excludes this root, or all of them, from the automatic redirect.

### Website settings

- **Favicon**: served at the domain's `/favicon.ico`.
- **Custom robots.txt content**: served at the domain's `/robots.txt`.
- **Maintenance mode**: visitors see that the site is being maintained.

### Content Security Policy

- **Enable CSP**: sends the `Content-Security-Policy` header for this website.
- **Content Security Policy**: the policies to apply. Default `default-src 'self'`.
- **Reporting only**: the browser reports violations without enforcing the policy.
- **Enable report logging**: logs the violation reports the browser sends.

### Global settings

- **Mailer transport**: a domain-specific email configuration.
- **Enable rel="canonical"**: allows `rel="canonical"` output.
- **E-mail address of the website administrator**: overrides the backend setting.
- **Date format**, **Time format**, **Date and time format**: override the backend settings.
- **File URL**: a CDN for the `files` directory.
- **Assets URL**: a CDN for the `assets` directory.

### Two-factor authentication

Enforces two-factor authentication and selects a redirect page. Exact labels not stated upstream.

Source: https://docs.contao.org/5.x/manual/en/site-structure/website-root/

---

## Regular page

Outputs content, much like a static HTML file uploaded to a server and requested in a browser.

Adds to the common groups:

### Routing

- **Require an item**: a 404 is shown when the URL carries no element alias.
- **Route conflicts**: notifies about similar aliases.

The home page's alias should always be `index`.

### Metadata

- **Google search results preview**: a visual preview tool.

### Canonical URL

- **Custom URL**: a canonical URL of your own.
- **Query parameters**: comma-separated parameters to preserve. `*` is a wildcard.

### Expert settings

- **Search indexer** (Contao 5.6 and later): values `Default (-)`, `Always index`, `Never index`.

Source: https://docs.contao.org/5.x/manual/en/site-structure/regular-page/

---

## Internal redirect

Redirects a visitor to another page in the page structure.

### Redirecting

- **Redirect page**: the target page. Mandatory not stated upstream.
- **Redirect type**: temporary (HTTP 302) or permanent (HTTP 301).
- **Always redirect**: redirects even when query or path parameters are present.

Source: https://docs.contao.org/5.x/manual/en/site-structure/pages-as-central-elements/internal-redirect/

---

## External redirect

Redirects to a page outside the server, or to one inside the structure but under a different domain.

### Redirecting

- **Redirect type**: temporary (HTTP 302) or permanent (HTTP 301).
- **Link address**: the destination. Use `https://` for another website, `mailto:` for an email
  address, `tel:` for a phone number. Mandatory not stated upstream.
- **Open in a new window**: opens the target in a new browser window.

Source: https://docs.contao.org/5.x/manual/en/site-structure/external-redirect/

---

## Logout

Creates a logout link for a protected area.

### Auto-forward

- **Redirect page**: where the member lands after logging out. Without one, they go to the first
  regular sub-page.
- **Redirect to last page visited**: returns the member to the last page instead.

This type has no metadata, layout or cache groups.

Source: https://docs.contao.org/5.x/manual/en/site-structure/logout/

---

## 401 Not authenticated

Rendered when a visitor is not logged in and therefore may not reach a protected page. It can show a
hint or forward to the login page.

### Auto-forward

- **Forward to another page**: redirects the visitor.
- **Redirect page**: the target. Without one, the first regular sub-page.

Has no routing group, and no `Show in HTML sitemap` or `Hide in menu` under expert settings.

Source: https://docs.contao.org/5.x/manual/en/site-structure/not-authenticated/

---

## 403 Access denied

Rendered when a member is logged in but lacks the rights for a protected page.

Same shape as 401: an **Auto-forward** group with **Forward to another page** and **Redirect page**,
no routing group, and only **CSS class** under expert settings.

Source: https://docs.contao.org/5.x/manual/en/site-structure/access-denied/

---

## 404 Page not found

Rendered when a visitor requests a page that does not exist. It can act as a regular page, sitemap
included, or forward automatically.

Same shape as 401 and 403: **Forward to another page** and **Redirect page**, no routing group, and
only **CSS class** under expert settings.

Source: https://docs.contao.org/5.x/manual/en/site-structure/page-not-found/

---

## 503 Service unavailable

Called when a root page is in maintenance mode.

Same shape as the other error types: **Forward to another page** and **Redirect page**, and only
**CSS class** under expert settings.

Source: https://docs.contao.org/5.x/manual/en/site-structure/service-unavailable/

---

## News feed

Produces an RSS, Atom or JSON feed from the news archives.

### News archives

- **News archives**: which archives feed this page. Mandatory not stated upstream.

### Feed settings

- **Feed format**: values `RSS 2.0`, `Atom`, `JSON`.
- **Export settings**: teaser texts only, or the complete posts.
- **Maximum number of contributions**: caps the number of posts.
- **Featured items**: all, featured only, or non-featured only.
- **Feed description**: a description of the feed.

### Image settings

- **Image size**: scaling values `Proportional`, `Fit to frame`, `Exact format`. Crop positions:
  `Important part`, `Left/Top`, `Middle/Top`, `Right/Top`, `Left/Middle`, `Center/Center`,
  `Right/Middle`, `Left/Bottom`, `Middle/Bottom`, `Right/Bottom`.

### Expert settings

- **Do not search**: excludes the page from the search.

Has no metadata, access-protection or layout group.

Source: https://docs.contao.org/5.x/manual/en/site-structure/news-feed/

## Source

Distilled from the [Contao 5 user manual](https://docs.contao.org/5.x/manual/en/site-structure/),
the ten page-type pages under `site-structure/`, retrieved 2026-08-21. Each type names the page it
came from.
