<!-- distilled from shopware/storefront v6.7.13.1 — utilities/, utility/modal-extension/, plugin/offcanvas/, plugin/ajax-modal/ -->

# Shopware Storefront — modals and off-canvas panels

Two overlay systems with different mechanics. Both are created by JavaScript at runtime, which is
why searching the templates for a modal's markup finds almost nothing.

## Contents

- [Which one to use](#which-one-to-use)
- [Modals are built at runtime](#modals-are-built-at-runtime)
- [The pseudo-modal template contract](#the-pseudo-modal-template-contract)
- [Opening a modal from your own code](#opening-a-modal-from-your-own-code)
- [AjaxModal: a modal from a route](#ajaxmodal-a-modal-from-a-route)
- [Building your own modal](#building-your-own-modal)
- [Off-canvas panels](#off-canvas-panels)
- [The OffCanvas API](#the-offcanvas-api)
- [AjaxOffCanvas](#ajaxoffcanvas)
- [The off-canvas cart](#the-off-canvas-cart)
- [Rebuilding an off-canvas panel](#rebuilding-an-off-canvas-panel)
- [The backdrop](#the-backdrop)
- [Accessibility](#accessibility)

## Which one to use

| | Modal | Off-canvas |
|---|---|---|
| Base | Bootstrap 5.3 modal | Bootstrap 5.3 offcanvas |
| Position | centred over the page | slides in from an edge |
| Markup source | built by `PseudoModalUtil` at runtime | built by `OffCanvas` at runtime |
| Template role | supplies the *content*, not the frame | supplies the *content*, not the frame |
| Typical use | quick view, address form, a confirmation | cart, filters, mobile menu, tabs |
| Content over AJAX | `AjaxModal` (`[data-ajax-modal][data-url]`) | `AjaxOffCanvas` |

Both keep one instance at a time: opening a second replaces the first.

## Modals are built at runtime

`storefront/utilities/modal.html.twig` contains nothing but an empty block:

```twig
{% block utilities_modal %}
{% endblock %}
```

That is not an oversight. The frame — `.modal`, `.modal-dialog`, `.modal-content`, header, close
button — is assembled by `src/utility/modal-extension/pseudo-modal.util.js` from
`storefront/component/pseudo-modal.html.twig`, which `base.html.twig` renders once per page.

So: **you never write modal markup, you write modal content.** `PseudoModalUtil` takes your HTML,
finds the title and content slots in the shared frame, and fills them in.

## The pseudo-modal template contract

Four classes drive the whole mechanism:

| Class | Role |
|---|---|
| `js-pseudo-modal-template` | the frame template rendered once into the page |
| `js-pseudo-modal-template-title-element` | where the title is written |
| `js-pseudo-modal-template-content-element` | where the content is written |
| `js-pseudo-modal-template-root-element` | optional; lets supplied content replace the whole root |

When the content you pass contains an element with `js-pseudo-modal-template-title-element`, its
inner HTML becomes the modal title and the element itself is not repeated in the body. Passing an
element with `js-pseudo-modal-template-root-element` replaces the frame's root instead of filling
the content slot — that is the escape hatch for a modal that needs its own structure.

## Opening a modal from your own code

```javascript
import PseudoModalUtil from 'src/utility/modal-extension/pseudo-modal.util';

const modal = new PseudoModalUtil('<div class="my-content">…</div>');
modal.open();
```

Constructor: `new PseudoModalUtil(content, useBackdrop = true, templateSelector, templateContentSelector, templateTitleSelector)`.
The last three default to the classes above; override them only when supplying your own frame.

Methods: `open(callback, delay)`, `close()`, `updateContent(content, callback)`,
`getModal()`. `updateContent` is what a multi-step modal uses — replace the body without
closing and reopening, so the backdrop does not flash.

**Re-initialise plugins after inserting content.** Markup added to a modal is new to the DOM and no
plugin is bound to it:

```javascript
modal.open(() => {
    window.PluginManager.initializePlugins();
});
```

Forgetting this is the usual reason a form inside a modal does not validate or submit.

## AjaxModal: a modal from a route

`[data-ajax-modal][data-url]` on a link or button opens its `data-url` in a modal:

```twig
<a href="{{ path('frontend.detail.page', { productId: id }) }}"
   data-ajax-modal="true"
   data-url="{{ path('widgets.quickview.minimal', { productId: id }) }}"
   data-modal-class="quickview-modal">
```

| Option | Default | Purpose |
|---|---|---|
| `modalBackdrop` | `true` | show a backdrop |
| `urlAttribute` | `data-url` | where the content is fetched from |
| `prevUrlAttribute` | `data-prev-url` | enables a back step inside the modal |
| `modalClassAttribute` | `data-modal-class` | attribute naming an extra class |
| `modalClass` | `null` | extra class on the modal |
| `centerLoadingIndicatorClass` | `text-center` | wrapper for the loading indicator |

The route must return a **fragment**, not a full page — the quick view route
(`widgets.quickview.minimal`) is the model to copy. `AjaxModal` re-initialises plugins on the
inserted markup itself, so content loaded this way works without extra wiring.

## Building your own modal

1. **Write a fragment template** — content only, no `.modal` wrapper. Give it a title element with
   `js-pseudo-modal-template-title-element` if it needs one.
2. **Decide how it opens.** From a route: `[data-ajax-modal][data-url]` and a controller returning
   the fragment. From existing markup: your own plugin calling `PseudoModalUtil`.
3. **Re-initialise plugins** in the open callback if you insert markup yourself.
4. **Style it** through the class you pass via `data-modal-class`; the frame classes are shared with
   every other modal and must not be restyled globally.
5. **Close from inside** with `data-bs-dismiss="modal"` on a button, or `modal.close()`.

## Off-canvas panels

`storefront/utilities/offcanvas.html.twig` is a real template, and it is the base every panel
extends:

```twig
{% sw_extends '@Storefront/storefront/utilities/offcanvas.html.twig' %}

{% block utilities_offcanvas_content %}
    …your content…
{% endblock %}
```

Blocks: `utilities_offcanvas_meta`, `utilities_offcanvas`, `utilities_offcanvas_header`,
`utilities_offcanvas_close`, `utilities_offcanvas_close_icon`, `utilities_offcanvas_close_text`,
`utilities_offcanvas_content_container`, `utilities_offcanvas_content`.

Core panels that extend it: `component/checkout/offcanvas-cart.html.twig`,
`layout/navigation/offcanvas/navigation.html.twig`, `layout/header/account-menu.html.twig`,
`layout/cookie/cookie-configuration.html.twig`, `layout/cookie/cookie-consent-offcanvas.html.twig`,
`component/product/description.html.twig`, `component/review/review.html.twig`.

`utilities_offcanvas_meta` renders meta tags when the panel is requested **without** XHR — a robot
following the URL directly gets a valid document. Keep it when you override the base.

**`.js-offcanvas-close` on the close button** is what the JavaScript binds to. Restyle the button
freely; keep the class.

## The OffCanvas API

`src/plugin/offcanvas/offcanvas.plugin.js`, all static:

```javascript
import OffCanvas from 'src/plugin/offcanvas/offcanvas.plugin';

OffCanvas.open(content, callback, position, closable, delay, fullwidth, cssClass);
OffCanvas.setContent(content, closable, delay);
OffCanvas.close(delay);
OffCanvas.exists();
OffCanvas.getOffCanvas();
```

- `position` — `'left'` (default), `'right'`, `'top'`, `'bottom'`.
- `closable` — whether a click on the backdrop closes it.
- `delay` — removal delay, default `REMOVE_OFF_CANVAS_DELAY` (350 ms), matching the CSS transition.
  Changing the transition duration means passing a matching delay, or the panel is removed mid-animation.
- `fullwidth` — full-width panel.
- `cssClass` — extra class, the seam for styling one panel differently.

Only one panel exists at a time; `open()` replaces the current one.

## AjaxOffCanvas

`AjaxOffCanvas.open(url, data, callback, position, closable, delay, fullwidth, cssClass)` fetches
the content first. With `data` it POSTs, without it GETs. The route returns a fragment that extends
`utilities/offcanvas.html.twig`.

`executeCallback` re-initialises plugins on the inserted markup, so a form inside an AJAX panel
works without extra wiring.

## The off-canvas cart

`component/checkout/offcanvas-cart.html.twig` (23 blocks) extends the base and is loaded from
`frontend.cart.offcanvas` by `offcanvas-cart.plugin.js` (`[data-off-canvas-cart]`).

It renders **the same line item templates as the cart page**, so an override of
`component/line-item/*` applies in both places. That is the single most useful fact when rebuilding
it: the panel is a different frame around identical item markup.

Its quantity and remove forms use `[data-form-ajax-submit]`, so a change replaces the panel's markup
in place and re-runs the plugins. `offcanvas-cart-summary.html.twig` holds the condensed totals.

## Rebuilding an off-canvas panel

- **Keep `.js-offcanvas-close`** on whatever closes it.
- **Extend the base template** rather than writing the frame yourself, or you lose the meta block,
  the close handling and the backdrop wiring.
- **Keep the forms intact** — `[data-form-ajax-submit]` and the field names are the request payload.
- **Check the narrow width.** A panel is far narrower than the page; a layout that works in the cart
  can overflow here.
- **Match the delay** if you change the CSS transition.
- **Test both cart surfaces** after any line item change, and the mobile navigation after any
  off-canvas base change — they all inherit from the same template.

## The backdrop

`src/utility/backdrop/backdrop.util.js` is shared by both systems: `BackdropUtil.create()` and
`BackdropUtil.remove()`. Modal and off-canvas manage it themselves; call it directly only for an
overlay of your own, and always remove what you create.

## Accessibility

Overlays are where keyboard and screen reader support is most often lost, and BFSG makes that a
compliance problem rather than a nicety:

- **Focus must move into the overlay** when it opens and **return to the trigger** when it closes.
  `FocusHandler` (`src/helper/focus-handler.helper.js`) exists for this — use
  `saveFocusState()` before opening and `resumeFocusState()` after closing.
- **Focus must be trapped** while the overlay is open: tabbing past the last element wraps to the
  first. Bootstrap's modal does this; a hand-built overlay does not.
- **Escape must close it**, and the close button must be reachable and labelled.
- **Announce the overlay**: `role="dialog"`, `aria-modal="true"` and a label via `aria-labelledby`
  pointing at the title element.
- **The page behind must not scroll** while an overlay is open.

Verify with the keyboard alone before shipping: open, move through every control, close, and check
that focus is back on the trigger.
