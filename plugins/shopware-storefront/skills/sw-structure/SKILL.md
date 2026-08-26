---
name: sw-structure
description: Shopware Storefront structure catalogue: every Twig block nested per template, sw_extends chains, route-to-template chains, CMS element resolver map. Use when overriding a Shopware Storefront block.
---

# Shopware Storefront structure

What exists and where, extracted from the Storefront source. Other skills explain how to change
things; this one says which template, block, resolver or selector to change.

Start here when a design, a screenshot or a class name has to become a code change.

## The chain

```
Route -> Controller -> PageLoader -> Page struct -> Twig template -> block
                                                       |  CMS page -> section -> block -> slot
                                                       |     slot.type -> resolver -> element.data
                                                       |                  admin defaultConfig -> element.config
                                                       +-> class -> SCSS file
                                                       +-> data-* -> JS plugin -> emitter events
```

**Override the innermost block that covers the change.** Overriding a parent replaces every child
inside it, which is the usual way core markup disappears.

**Not every block is free to rewrite.** 120 templates carry selectors a JavaScript plugin queries,
and 204 places hand options from Twig into a plugin. Losing one fails silently — the plugin
initialises, finds nothing and does nothing. Check `OVERRIDE-RISK.md` first.

## Two constraints on every change

**Accessibility is mandatory, not optional.** German shops fall under the BFSG
(Barrierefreiheitsstärkungsgesetz, in force since 28 June 2025), which requires EN 301 549 / WCAG
2.1 AA. Every markup change is therefore also an accessibility change: keep semantic elements,
labels, `aria-*` attributes, focus order and the visually-hidden text the core templates carry.
Removing them is a legal defect, not a styling decision. Call the Skill tool with **"sw-features"**
for the accessibility reference and its checklist.

**The base is Bootstrap 5.3.8.** Grid, utilities, dropdowns, modals, off-canvas and collapse come
from the framework; the theme configures it through SCSS variables. Reach for a Bootstrap mechanism
before writing your own, and check its documentation at getbootstrap.com/docs/5.3 when a class
behaves unexpectedly.

## Reference map

**Blocks**, every one with its nesting, by area:

- **[BLOCKS-COMPONENT.md](references/BLOCKS-COMPONENT.md)**: 119 templates, 817 blocks — cards, forms, addresses, line items, filters, reviews.
- **[BLOCKS-PAGE.md](references/BLOCKS-PAGE.md)**: 74 templates, 645 blocks — account, checkout, detail, search, wishlist, errors.
- **[BLOCKS-LAYOUT.md](references/BLOCKS-LAYOUT.md)**: 46 templates, 289 blocks — header, footer, navigation, meta, `base.html.twig`.
- **[BLOCKS-CMS.md](references/BLOCKS-CMS.md)**: 74 templates, 414 blocks — Shopping Experiences elements, blocks, sections.
- **[BLOCKS-UTILITIES.md](references/BLOCKS-UTILITIES.md)**: 11 templates, 41 blocks — alerts, offcanvas, modals, pagination.

**Where things connect**:

- **[INHERITANCE-CHAINS.md](references/INHERITANCE-CHAINS.md)**: 63 `sw_extends` edges, 203 `sw_include` targets with every call site — the blast radius.
- **[ROUTE-TEMPLATE-MAP.md](references/ROUTE-TEMPLATE-MAP.md)**: route to controller to page to template, both directions.
- **[PAGE-CLASSES.md](references/PAGE-CLASSES.md)**: 33 page domains, their loaders and events, and what each page exposes to Twig.
- **[TEMPLATE-VARIABLES.md](references/TEMPLATE-VARIABLES.md)**: where each variable comes from — globals, controller, `with`, `{% set %}` — plus every Twig function and filter.
- **[DESIGN-TO-CODE.md](references/DESIGN-TO-CODE.md)**: CSS class to template, block, stylesheet and JavaScript binding.
- **[CMS-ELEMENT-MAP.md](references/CMS-ELEMENT-MAP.md)**: element type to admin component, resolver and template, with all 124 configuration fields.
- **[JS-SELECTOR-MAP.md](references/JS-SELECTOR-MAP.md)**: 70 registrations with selectors and options, 111 events, every `data-*` in the templates.
- **[OVERRIDE-RISK.md](references/OVERRIDE-RISK.md)**: **read before overriding any block** — which plugin needs which selector in which block (413 pairs over 120 templates), and the 204 places where Twig hands options into a plugin.

**Subsystems**, read before rebuilding one:

- **[HEADER-FOOTER-NAVIGATION.md](references/HEADER-FOOTER-NAVIGATION.md)**: the ESI mechanism, the pagelets, the flyout recursion, the off-canvas menu, responsive switching.
- **[ACCOUNT-AREA.md](references/ACCOUNT-AREA.md)**: every account page and its data, how orders are loaded, the cancellation transition, why the edit-order screen shares the checkout partials.
- **[FORMS.md](references/FORMS.md)**: the seven field components, both validation layers, `formViolations`, the CMS form types, and the contact and revocation forms through to the Flow Builder mail.
- **[CHECKOUT-FLOW.md](references/CHECKOUT-FLOW.md)**: four pages and their data, line item dispatch, every cart route, what a change recalculates, data layer events.
- **[CATEGORY-SIDEBAR-AND-FILTERS.md](references/CATEGORY-SIDEBAR-AND-FILTERS.md)**: the sidebar section layout, category navigation, why the filter panel reads the listing slot, adding a filter.
- **[MODALS-AND-OFFCANVAS.md](references/MODALS-AND-OFFCANVAS.md)**: why modal markup is built at runtime, the template contract, the OffCanvas API.
- **[COOKIE-CONSENT.md](references/COOKIE-CONSENT.md)**: how a cookie enters the banner, from `CookieGroupCollectEvent` to `COOKIE_CONFIGURATION_UPDATE`.
- **[PRICE-AND-QUANTITY.md](references/PRICE-AND-QUANTITY.md)**: how a price is calculated, `CalculatedPrice` in Twig, rounding, the cart pipeline, the quantity chain.
- **[STRUCTURED-DATA-AND-TRACKING.md](references/STRUCTURED-DATA-AND-TRACKING.md)**: the six JSON-LD schemas and the analytics event system to build a tag manager on.

**Styling and text**:

- **[BOOTSTRAP-BASE.md](references/BOOTSTRAP-BASE.md)**: what Bootstrap 5.3.8 provides, the breakpoints, the 28 variables Shopware overrides.
- **[SCSS-VARIABLES.md](references/SCSS-VARIABLES.md)**: 977 Bootstrap and 179 Shopware variables with defaults, 400 custom properties, 27 functions, 84 mixins.
- **[THEME-JSON.md](references/THEME-JSON.md)**: the keys, `@Storefront` and `@Plugins` ordering, the 26 config fields, inheritance, compilation.
- **[USER-PREFERENCES-BFSG.md](references/USER-PREFERENCES-BFSG.md)**: the seven `prefers-*` features, what Bootstrap already guards, the 30 unguarded Shopware animations, and the WCAG criteria they serve.
- **[CSS-FEATURE-SUPPORT.md](references/CSS-FEATURE-SUPPORT.md)**: which CSS features a theme may use — `:has()` and container queries are ruled out for layout — and the safe alternatives.
- **[SNIPPETS.md](references/SNIPPETS.md)**: all 821 keys with their text and the templates using them, and which do not resolve at this version.

## Check the project before trusting the catalogue

These catalogues describe the **Shopware core**. Every project also runs its own extensions, and
they routinely override more templates than the core ships — a single icon or navigation plugin can
rewrite hundreds.

**Before answering "which template does X", check what this project overrides.** Run
`/sw-structure-map` and read `.shopware-catalog/structure.md`. It records:

- every plugin under `custom/plugins/`, `custom/static-plugins/` and `custom/apps/`,
- which of them are **theme plugins** — identified by `implements ThemeInterface` or a
  `Resources/theme.json`, never by name, since the name differs in every project and a shop may run
  several,
- which templates and blocks each one overrides, and whether it keeps `{{ parent() }}`,
- **core templates overridden by more than one extension**, which is where changes silently fail.

Storefront work belongs in the project's theme plugin in most cases. Name which one you mean when
several exist.

## Related

Call the Skill tool with **"sw-twig"** for how to override, **"sw-controller"** for building pages,
**"sw-javascript"** for plugin behaviour, **"sw-theme"** for SCSS and theme configuration.

## Source

Extracted from the Shopware Storefront and Administration sources at `v6.7.13.1` by the generators in
`scripts/`; each reference file carries its generator and source hash on line 1. Concepts follow
[developer.shopware.com](https://developer.shopware.com/docs/guides/plugins/plugins/storefront/),
retrieved 2026-08-26.
