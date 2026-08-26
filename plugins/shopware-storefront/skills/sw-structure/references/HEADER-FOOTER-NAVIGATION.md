<!-- distilled from shopware/storefront v6.7.13.1 — layout/header, layout/footer, layout/navbar, layout/navigation, Pagelet/Header, Pagelet/Footer, navbar.plugin.js, offcanvas-menu.plugin.js -->

# Shopware Storefront — header, footer and navigation

The most-modified and least-obvious part of the Storefront. Header and footer are **not** part of
the page: they are separate sub-requests with their own data, their own cache and their own
templates. Getting that wrong is the cause of most "my change works locally but not in production".

## Contents

- [Header and footer are ESI sub-requests](#header-and-footer-are-esi-sub-requests)
- [What that means for a theme](#what-that-means-for-a-theme)
- [Header data: HeaderPagelet](#header-data-headerpagelet)
- [Header template structure](#header-template-structure)
- [Footer data and structure](#footer-data-and-structure)
- [The minimal variants](#the-minimal-variants)
- [Where the category tree comes from](#where-the-category-tree-comes-from)
- [The main navigation](#the-main-navigation)
- [The flyout](#the-flyout)
- [Flyout behaviour: navbar.plugin.js](#flyout-behaviour-navbarpluginjs)
- [The off-canvas navigation](#the-off-canvas-navigation)
- [Responsive behaviour](#responsive-behaviour)
- [Active state](#active-state)
- [Stylesheets](#stylesheets)
- [Moving or rebuilding the navigation](#moving-or-rebuilding-the-navigation)

## Header and footer are ESI sub-requests

`base.html.twig` does not include them. It renders **ESI tags**:

```twig
{% block base_esi_header %}
    {{ render_esi(path('frontend.header', { headerParameters: headerParameters }), { ignore_errors: false }) }}
{% endblock %}

{% block base_esi_footer %}
    {{ render_esi(path('frontend.footer', { footerParameters: footerParameters }), { ignore_errors: false }) }}
{% endblock %}
```

Each resolves to its own request:

```
GET /_esi/global/header   frontend.header   NavigationController::header   layout/header.html.twig
GET /_esi/global/footer   frontend.footer   NavigationController::footer   layout/footer.html.twig
```

The point is caching: the header is identical across thousands of pages, so it is cached once and
stitched into every response instead of being rebuilt each time.

## What that means for a theme

Four consequences, all of which bite in practice:

- **`page` is not available.** The header renders from its own pagelet. `page.product`,
  `page.cmsPage` and everything else on the page struct do not exist in header or footer templates.
  What you get is `header`, `footer`, `context` and the other globals.
- **Data must come from the pagelet.** To add something to the header, subscribe to
  `HeaderPageletLoadedEvent` and `addExtension()`. A `PageLoadedEvent` subscriber cannot reach it.
- **The cache is separate.** A header change may persist after a page cache clear, and vice versa.
  Invalidate the HTTP cache, not just the Twig cache.
- **Never make the header page-specific.** Anything varying per page or per customer defeats the
  cache for every page at once. Load such content over AJAX after render instead.

`headerParameters` and `footerParameters` are passed through the ESI path, which is the intended
way to hand a value into the sub-request — set them in a subscriber on the page.

## Header data: HeaderPagelet

`Storefront/Pagelet/Header/HeaderPageletLoader.php` builds it from three sources:

| Accessor | Type | Loaded from |
|---|---|---|
| `getNavigation()` | `Tree` | `NavigationLoader` — the category tree |
| `getLanguages()` | `LanguageCollection` | `AbstractLanguageRoute` |
| `getCurrencies()` | `CurrencyCollection` | `AbstractCurrencyRoute` |
| `getActiveLanguage()` | `LanguageEntity` | the context (removed in 6.8; read `context.languageId`) |
| `getActiveCurrency()` | `CurrencyEntity` | the context (removed in 6.8; read `context.currency`) |

In Twig this is `header.navigation`, `header.languages`, `header.currencies`.

Both route calls dispatch a request event first — `LanguageRouteRequestEvent`,
`CurrencyRouteRequestEvent` — so the criteria can be changed before the query runs. That is the
supported way to add an association or a filter to the language or currency list.

Extension point: `HeaderPageletLoadedEvent`.

## Header template structure

`layout/header.html.twig` is the ESI entry point; `layout/header/header.html.twig` holds the markup.

```
layout/header.html.twig                     ESI entry, includes the parts below
└── layout/header/top-bar.html.twig         language, currency, service menu
    ├── layout/header/actions/language-widget.html.twig
    └── layout/header/actions/currency-widget.html.twig
└── layout/header/header.html.twig
    ├── layout/header/logo.html.twig        theme_config('sw-logo-*') per breakpoint
    ├── layout/header/search.html.twig      [data-search-widget], suggest over AJAX
    └── actions/
        ├── account-widget.html.twig        [data-account-menu] -> off-canvas on small screens
        ├── cart-widget.html.twig           [data-cart-widget], refreshed over AJAX
        └── wishlist-widget.html.twig       [data-wishlist-widget]
└── layout/navbar/navbar.html.twig          the main navigation
```

`layout/header/search-suggest.html.twig` and the cart widget are also rendered standalone as AJAX
responses (`frontend.search.suggest`, `frontend.checkout.info`), which is why they must stay
renderable without the surrounding header.

## Footer data and structure

`Storefront/Pagelet/Footer/FooterPageletLoader.php`:

| Accessor | Type | Meaning |
|---|---|---|
| `getServiceMenu()` | `CategoryCollection` | the service menu configured on the sales channel |
| `getPaymentMethods()` | `PaymentMethodCollection` | for the payment logos |
| `getShippingMethods()` | `ShippingMethodCollection` | for the shipping logos |

`layout/footer/footer.html.twig` renders the columns from `footer.serviceMenu`, and the columns
collapse on small screens through `[data-collapse-footer-columns]`.

Extension point: `FooterPageletLoadedEvent`.

## The minimal variants

`header-minimal.html.twig` and `footer-minimal.html.twig` `sw_extends` their full counterparts and
strip navigation, search and widgets. They are used in the checkout, where the funnel must not offer
a way out. A theme changing the header must decide whether the minimal variant inherits that change
— it does automatically, unless the block you override is one the minimal variant also overrides.

## Where the category tree comes from

```
SalesChannel.navigationCategoryId       the root category of this channel
SalesChannel.navigationCategoryDepth    how many levels are loaded
  -> NavigationLoader::load(activeId, context, rootId, depth)
  -> Tree of TreeItem
       treeItem.category    CategoryEntity
       treeItem.children    TreeItem[]
  -> header.navigation.tree
```

**The depth is a sales channel setting**, not a template constant. Loading three levels and
rendering two wastes queries; loading two and rendering three silently renders nothing at the third
level. Check the channel configuration before changing the template depth.

Each `category` carries `id`, `translated.name`, `seoUrl`, `type` (`page`, `folder`, `link`),
`linkType`, `shouldOpenInNewTab`, `media` and `childCount`.

**`type == 'folder'`** is the structural case: a folder is a grouping label, rendered as a
`<div>` rather than an `<a>`, and a folder with no children is skipped entirely
(`itemSkipped` in `navbar.html.twig`).

## The main navigation

`layout/navbar/navbar.html.twig` — Bootstrap 5.3 navbar with a dropdown per top-level category.

```html
<nav class="navbar navbar-expand-lg main-navigation-menu" id="main-navigation-menu"
     data-navbar="true" data-navbar-options="{...}">
  <div class="collapse navbar-collapse" id="main_nav">
    <ul class="navbar-nav main-navigation-menu-list flex-wrap">
      <li class="nav-item nav-item-{id}">                      home link, if homeEnabled
      <li class="nav-item nav-item-{id} dropdown position-static">
        <a class="nav-link nav-item-{id}-link root main-navigation-link p-2 dropdown-toggle"
           data-bs-toggle="dropdown">
        <div class="dropdown-menu w-100 p-4">                   the flyout
```

Load-bearing details:

- **`position-static` on the `<li>`** is what lets the dropdown span the full width. Bootstrap
  positions a dropdown against its nearest positioned ancestor; making the item static promotes
  that to the container. Remove it and the flyout collapses to the width of its link.
- **`w-100` on `.dropdown-menu`** completes the full-width effect.
- **`data-bs-toggle="dropdown"`** is present only when the category has children. Bootstrap's own
  dropdown handles the open state; `navbar.plugin.js` adds hover and accessibility on top.
- **`nav-item-{id}` and `nav-item-{id}-link`** carry the category id and are how the active state
  is found. Keep them.
- **Blocks**: `layout_navbar`, `layout_navbar_nav_element`, `layout_navbar_menu_home`,
  `layout_navbar_menu_items`, `layout_navbar_menu_item`, `layout_navbar_menu_item_link`,
  `layout_navbar_menu_item_link_content`, `layout_navbar_menu_item_children`.

## The flyout

```
layout/navbar/navbar.html.twig
└── layout/navbar/content.html.twig      the flyout body; adds the category media column
    └── layout/navbar/categories.html.twig   recursive, one level per call
```

`categories.html.twig` **includes itself** with `only`:

```twig
{% set navigationMaxDepth = 3 %}
{% if level < navigationMaxDepth and treeItem.children %}
    {% sw_include '@Storefront/storefront/layout/navbar/categories.html.twig' with {
        navigationTree: treeItem.children, level: level + 1, page: page
    } only %}
{% endif %}
```

**`only` is the trap.** It cuts the enclosing scope: inside the recursion, only
`navigationTree`, `level` and `page` exist. A variable you set in `navbar.html.twig` is not
visible in `categories.html.twig`, and one set at level 1 is not visible at level 2 — you must pass
it through every level of the include.

Layout mechanics:

- **`navigationMaxDepth = 3`** is a template constant, independent of the loaded depth.
- **Column count depends on media**: `columnCount = navigationMedia ? 3 : 4`, rendered as
  `col-4` or `col-3` in Bootstrap's 12-column grid. Only level 0 gets a column class.
- **`navigation-flyout-col`** is added to every item except the first of each row
  (`loop.index0 % columnCount != 0`) — that is the column separator.
- **`is-level-{n}`** on both the container and each link is what the stylesheet targets per depth.
- **Blocks**: `layout_navbar_categories`, `layout_navbar_categories_item`,
  `layout_navbar_categories_item_link`, `layout_navbar_categories_recoursion` (spelled with the
  typo in core — match it exactly when overriding).

## Flyout behaviour: navbar.plugin.js

Bound to `[data-navbar]`. Bootstrap opens the dropdown on click; this plugin adds hover, debounce
and accessibility.

| Option | Default | Purpose |
|---|---|---|
| `debounceTime` | `200` | delay before a hover closes a dropdown, so crossing a gap does not close it |
| `navItemSelector` | `.nav-item` | the items holding link and dropdown |
| `topLevelLinksSelector` | `.main-navigation-link` | the top-level links |
| `ariaCurrentPageSelector` | `.nav-item-{id}-link` | `{id}` is replaced with the active category id |
| `activeClass` | `active` | class marking the current category |
| `pathIdList` | `[]` | deprecated in 6.8; use `window.activeNavigationPathIdList` |

Behaviour: `mouseleave` on the navbar closes all dropdowns after `debounceTime`; `focusout`
restores focus after a keyboard close; `aria-current="page"` is set on the active link, resolved
from `window.activeNavigationId`.

**Keep these selectors when restructuring.** They are class-based, not attribute-based, so a
markup rewrite that drops `.nav-item` or `.main-navigation-link` breaks hover and keyboard
navigation without any error.

## The off-canvas navigation

The small-screen navigation is a different template tree and loads over AJAX.

```
[data-off-canvas-menu] clicked
  -> offcanvas-menu.plugin.js fetches frontend.menu.offcanvas
  -> NavigationController::offcanvas
  -> layout/navigation/offcanvas/navigation-pagelet.html.twig
       navigation.html.twig      the off-canvas frame
       categories.html.twig      one level at a time
       item-link.html.twig / active-item-link.html.twig
       back-link.html.twig       navigates up
       show-all-link.html.twig / show-active-link.html.twig
```

**One level per request.** Unlike the flyout, the off-canvas menu fetches each level as the user
descends, so the initial payload stays small. Selectors it depends on:
`.js-navigation-offcanvas-link`, `.js-navigation-offcanvas-loading-icon`,
`.navigation-offcanvas-container`, `.js-navigation-offcanvas-initial-content`,
`a.is-current-category`.

`?offcanvas=menu` in the URL opens it on load — useful when returning from a subpage.

## Responsive behaviour

- **`navbar-expand-lg`** is the switch: the horizontal navigation appears at `lg` and above, and
  below that the navbar collapses and the off-canvas takes over.
- **The burger button and the search** are toggled with Bootstrap display utilities in
  `header.html.twig` (`d-none d-sm-block d-lg-none` and similar), not by JavaScript.
- **The logo** is chosen per breakpoint from `theme_config('sw-logo-desktop')`,
  `sw-logo-tablet`, `sw-logo-mobile`, `sw-logo-share`.
- **Changing the breakpoint** means changing `navbar-expand-lg` *and* the display utilities on the
  burger and search, *and* the SCSS breakpoint variables. Changing one leaves a range where both or
  neither navigation shows.

## Active state

Three mechanisms, one deprecated:

- **`window.activeNavigationId`** and **`window.activeNavigationPathIdList`** — the current
  category and its ancestors. `navbar.plugin.js` reads them and applies `.active`.
- **`shopware.navigation`** — the global carrying `id` and `pathIdList` server-side.
- **`layout/navigation/active-styling.html.twig`** — deprecated, removed in 6.8. It emitted a
  per-navigation `<style>` tag. Do not build on it; the class is set by JavaScript now.

The resolution order for the active id: the route's `navigationId` attribute, then the request
parameter, then the landing page's category, then the sales channel root. That is why a landing page
still highlights the right entry.

## Stylesheets

**Navigation styles live in `skin/`, not `layout/`** — the usual reason an override does not
apply:

| File | Selectors |
|---|---|
| `skin/shopware/layout/_main-navigation.scss` | `.main-navigation-menu`, `.main-navigation-link`, `.main-navigation-link-text`, `.dropdown`, `.dropdown-menu`, `.dropup` |
| `skin/shopware/layout/_navigation-flyout.scss` | `.navigation-flyout-categories`, `.navigation-flyout-link`, `.navigation-flyout-category-link`, and the `.is-level-0` / `.is-level-2` / `.active` modifiers |
| `layout/_navigation-offcanvas.scss` | the off-canvas menu |
| `layout/_header.scss`, `layout/_header-minimal.scss` | the header |
| `layout/_footer.scss` | the footer |

`skin` is imported after `layout` in `base.scss`, so a skin rule wins over a layout rule at equal
specificity. Overriding a layout file and finding nothing changed usually means the skin file is
setting it again.

## Moving or rebuilding the navigation

To relocate the navigation — out of the header, into a sidebar, a mega menu of your own:

1. **Move the include, keep the data.** `header.navigation.tree` exists only inside the header ESI
   request. Rendering the navigation elsewhere on the page means either keeping it in the header
   ESI, or loading the tree yourself in a page subscriber via `NavigationLoader`.
2. **Keep `[data-navbar]` on the element** wrapping the whole navigation, and keep `.nav-item`,
   `.main-navigation-link` and `.nav-item-{id}-link` inside it, or reimplement hover, active state
   and keyboard handling yourself.
3. **Decide about Bootstrap.** `data-bs-toggle="dropdown"`, `position-static` and `w-100` are what
   make the full-width flyout work. Dropping Bootstrap's dropdown means owning open and close, click
   outside, and escape.
4. **Mind the recursion scope.** `categories.html.twig` includes itself with `only`; anything your
   markup needs at depth must be threaded through every level.
5. **Match the folder rule.** A `folder` category has no link and is skipped when it has no
   children; a rebuild that renders it as a link produces dead entries.
6. **Handle both navigations.** Flyout and off-canvas are separate template trees. Changing only the
   flyout leaves mobile on the old structure.
7. **Check the minimal header**, which inherits from the full one and is used in the checkout.
8. **Verify the cache.** Header markup is cached per ESI request; confirm your change appears after
   an HTTP cache invalidation, not just in the dev environment.
