# Shopware Storefront — the Bootstrap base

The Storefront is built on Bootstrap 5.3.8, vendored at
`Resources/app/storefront/node_modules/bootstrap`. Grid, utilities, dropdowns, modals, off-canvas,
collapse and the form controls come from the framework — the templates supply structure and
Shopware-specific classes on top.

Knowing where the line runs saves rebuilding something the framework already does, and stops a
theme from fighting its own base.

## Contents

- [What comes from Bootstrap](#what-comes-from-bootstrap)
- [Breakpoints](#breakpoints)
- [What Shopware overrides](#what-shopware-overrides)
- [The three layers of customisation](#the-three-layers-of-customisation)
- [Bootstrap JavaScript in the Storefront](#bootstrap-javascript-in-the-storefront)
- [Bootstrap events](#bootstrap-events)
- [Where Bootstrap and Shopware interlock](#where-bootstrap-and-shopware-interlock)
- [Common mistakes](#common-mistakes)

## What comes from Bootstrap

Imported wholesale by `src/scss/vendor/_bootstrap.scss`
(`@import '~vendor/bootstrap/scss/bootstrap'`), so **all** of Bootstrap is available:

| Area | Provides |
|---|---|
| Layout | `_grid.scss`, `_containers.scss` — `.container`, `.row`, `.col-*`, gutters |
| Content | `_reboot.scss`, `_type.scss`, `_images.scss`, `_tables.scss` |
| Forms | `_forms.scss` — `.form-control`, `.form-check`, `.form-select`, validation states |
| Components | accordion, alert, badge, breadcrumb, buttons, button-group, card, carousel, close, dropdown, list-group, modal, nav, navbar, offcanvas, pagination, placeholders, popover, progress, spinners, toasts, tooltip |
| Helpers | ratio, position, stacks, visually-hidden, stretched-link, text-truncate |
| Utilities | spacing, display, flex, text, background, border, sizing — the `.d-*`, `.m-*`, `.text-*` classes |

`_root.scss` emits 94 CSS custom properties (`--bs-*`), so colours, fonts and spacing can be read
and overridden at runtime without recompiling.

## Breakpoints

**Shopware does not override them** — the Bootstrap defaults apply:

| Name | Min width |
|---|---|
| `xs` | 0 |
| `sm` | 576px |
| `md` | 768px |
| `lg` | 992px |
| `xl` | 1200px |
| `xxl` | 1400px |

`lg` (992px) is the one that matters most: `navbar-expand-lg` switches the main navigation between
the horizontal flyout and the off-canvas menu there. Changing it means changing the navbar class,
the display utilities on the burger and search, and any SCSS bound to the same breakpoint — see
`HEADER-FOOTER-NAVIGATION.md`.

`$container-max-widths` **is** overridden by Shopware; the breakpoints themselves are not.

## What Shopware overrides

Only 28 variables, in `src/scss/abstract/variables/`. Everything else is Bootstrap's default.

| Group | Variables |
|---|---|
| Layout | `$container-max-widths`, `$spacer-xs`, `$spacer-sm`, `$spacer-md`, `$spacer-lg`, `$spacer-xl` |
| Feature flags | `$enable-important-utilities`, `$enable-responsive-font-sizes`, `$enable-validation-icons` |
| z-index | `$zindex-levels`, `$cookie-msg-zindex`, `$menu-flyout-zindex`, `$offcanvas-zindex`, `$scroll-up-zindex`, `$search-suggest-zindex`, `$magnifier-overlay-zindex`, `$zoom-modal-action-zindex` |
| Overlays | `$modal-backdrop-bg`, `$modal-transition`, `$element-backdrop-bg` |
| Icons | `$icon-base-color`, `$icon-base-size`, `$icon-review-color`, `$progress-bar-review` |
| Build | `$sw-asset-theme-url`, `$app-css-relative-asset-path`, `$theme-id`, `$sw-features` |

The z-index set is the important one: the Storefront stacks cookie bar, flyout, off-canvas, search
suggest and modals against each other, and a custom overlay must join that scale rather than
inventing a number.

## The three layers of customisation

In order of preference:

1. **Theme configuration** (`theme.json` → `config.fields`) — colours, fonts, logos. Editable in
   the administration, no recompilation by hand, and survives updates. Use this whenever the value
   is something a shop owner might reasonably change.
2. **SCSS variables** — override a Bootstrap or Shopware variable in your theme before the vendor
   import. Reaches every component at once: changing `$primary` restyles buttons, links, focus
   rings and badges together.
3. **CSS rules** — the last resort, for a component that genuinely differs. Prefer overriding the
   `--bs-*` custom property to writing a more specific selector.

A rule that needs `!important` to win is nearly always a sign that layer 1 or 2 was skipped. Note
that `$enable-important-utilities` is on, so Bootstrap's own utility classes already carry
`!important` — competing with them by specificity does not work; use the utility or change the
variable.

## Bootstrap JavaScript in the Storefront

Thirteen components ship JavaScript: `alert`, `button`, `carousel`, `collapse`, `dropdown`,
`modal`, `offcanvas`, `popover`, `scrollspy`, `tab`, `toast`, `tooltip`, plus `base-component`.

The Storefront uses them through `src/utility/bootstrap.util.js` and the `data-bs-*` API. The
attributes Bootstrap itself reads:

`data-bs-toggle`, `data-bs-target`, `data-bs-dismiss`, `data-bs-ride`, `data-bs-slide`,
`data-bs-slide-to`, `data-bs-interval`, `data-bs-spy`, `data-bs-original-title`.

**`data-bs-*` is Bootstrap; `data-*` without the prefix is a Shopware plugin selector.** The two
systems coexist on the same elements — the navbar item carries both `data-bs-toggle="dropdown"`
(Bootstrap opens the dropdown) and sits inside `[data-navbar]` (the Shopware plugin adds hover and
accessibility). Removing either breaks a different half of the behaviour.

## Bootstrap events

Every component fires a four-stage lifecycle on its element, namespaced `.bs.<component>`:

| Event | When |
|---|---|
| `show.bs.modal` | before opening; preventable |
| `shown.bs.modal` | after the transition finishes |
| `hide.bs.modal` | before closing; preventable |
| `hidden.bs.modal` | after the transition finishes |

Same shape for `offcanvas`, `dropdown`, `collapse`, `tab`, `carousel`, `toast`. Modal and off-canvas
additionally fire `hidePrevented` when a click on the backdrop is blocked.

These are **native DOM events**, not the Shopware emitter — subscribe with `addEventListener`:

```javascript
document.querySelector('.modal').addEventListener('shown.bs.modal', () => {
    window.PluginManager.initializePlugins();
});
```

`shown` and `hidden` are the right hooks for work that needs final dimensions; `show` and `hide`
fire before the transition, when the element is not yet measurable.

## Where Bootstrap and Shopware interlock

| Storefront feature | Bootstrap part | Shopware part |
|---|---|---|
| Main navigation | `.navbar`, `.dropdown`, `.dropdown-menu`, `navbar-expand-lg` | `[data-navbar]` for hover, debounce, active state |
| Off-canvas cart / menu | `.offcanvas` markup and transitions | `OffCanvas` utility, AJAX loading, `.js-offcanvas-close` |
| Modals | `.modal` structure, backdrop, focus trap | `PseudoModalUtil` builds the markup, `AjaxModal` loads content |
| Footer columns | `.collapse` | `[data-collapse-footer-columns]` toggles per breakpoint |
| Forms | `.form-control`, validation states | `[data-form-validation]`, `[data-form-ajax-submit]` |
| Product cards | `.card`, grid columns | `[data-product-information]` for tracking |

The pattern is consistent: **Bootstrap owns appearance and basic interaction, Shopware owns data,
AJAX and accessibility refinements.** When rebuilding a component, decide which half you are
replacing — replacing both at once is where weeks disappear.

## Common mistakes

- **Removing `position-static` from a navbar item.** It is what lets the flyout span the full width;
  without it the dropdown shrinks to the link.
- **Restyling `.modal` or `.offcanvas` globally.** Both frames are shared by every overlay. Target
  the extra class instead (`data-modal-class`, the `cssClass` argument).
- **Fighting a utility class with specificity.** Utilities carry `!important` here. Use a different
  utility, or change the variable.
- **Changing a transition duration without the removal delay.** `OffCanvas` removes the element
  after `REMOVE_OFF_CANVAS_DELAY` (350 ms); a longer CSS transition is cut off.
- **Assuming a custom breakpoint.** They are Bootstrap defaults, so `992px` is where navigation
  switches, whatever the design file says.
- **Hand-building a dropdown or modal.** Bootstrap's versions already handle focus trapping, escape
  and click-outside — which BFSG requires and a hand-built one usually misses.

## Source

Bootstrap 5.3.8 as vendored in
`Resources/app/storefront/node_modules/bootstrap` (`package.json` version, `scss/`, `js/src/`).
Upstream documentation: [getbootstrap.com/docs/5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/).
