<!-- distilled from shopware/storefront v6.7.13.1 — page/checkout, component/line-item, CheckoutController, CartLineItemController, google-analytics events -->

# Shopware Storefront — the checkout

Four pages, one cart, and a recalculation behind every interaction. The checkout is the part of a
theme where a wrong assumption costs orders, so the rules below are tighter than elsewhere.

## Contents

- [The four pages](#the-four-pages)
- [The frame: _page.html.twig](#the-frame-_pagehtmltwig)
- [The cart page](#the-cart-page)
- [Line items](#line-items)
- [The summary](#the-summary)
- [The confirm page](#the-confirm-page)
- [Placing the order](#placing-the-order)
- [The finish page](#the-finish-page)
- [The off-canvas cart](#the-off-canvas-cart)
- [Every cart route](#every-cart-route)
- [How a cart interaction works](#how-a-cart-interaction-works)
- [Data layer events](#data-layer-events)
- [Rules for changing the checkout](#rules-for-changing-the-checkout)

## The four pages

| Step | Route | Page class | Template |
|---|---|---|---|
| Cart | `frontend.checkout.cart.page` | `CheckoutCartPage` | `page/checkout/cart/index.html.twig` |
| Register / address | `frontend.checkout.register.page` | `CheckoutRegisterPage` | `page/checkout/address/index.html.twig` |
| Confirm | `frontend.checkout.confirm.page` | `CheckoutConfirmPage` | `page/checkout/confirm/index.html.twig` |
| Finish | `frontend.checkout.finish.page` | `CheckoutFinishPage` | `page/checkout/finish/index.html.twig` |

All four `sw_extends` `page/checkout/_page.html.twig`, which itself extends `base.html.twig`.

The register step appears only for guests and new customers; a logged-in customer goes from cart
straight to confirm.

## The frame: _page.html.twig

`page/checkout/_page.html.twig` is what makes the checkout look different from the rest of the shop:

- It renders **`header-minimal.html.twig`** and **`footer-minimal.html.twig`** instead of the full
  ones — no navigation, no search, no widgets. That is deliberate funnel design.
- It provides the step indicator and the container layout every checkout page sits in.
- Blocks: `base_header`, `base_footer`, `base_content`, plus `page_checkout_*` for the frame.

A theme changing the header must check this file: the minimal header inherits from the full one, so
a block you override in the full header also changes the checkout unless the minimal variant
overrides the same block.

## The cart page

`page/checkout/cart/index.html.twig` (31 blocks). Structure:

```
page_checkout_cart
├── component/checkout/cart-header.html.twig      the column headings
├── component/checkout/cart-alerts.html.twig      errors and notices from the cart
├── for lineItem in page.cart.lineItems
│     component/line-item/line-item.html.twig
├── component/checkout/add-product-by-number.html.twig   the SKU field
├── the promotion code form
└── page/checkout/summary.html.twig               the totals
```

`page.cart` is a `Cart` object: `lineItems`, `price`, `deliveries`, `errors`, `transactions`.
`page.cart.errors` is what `cart-alerts.html.twig` renders — stock problems, expired promotions,
products that became unavailable. **Never remove that include**: a customer who cannot see why the
cart changed will abandon it.

## Line items

`component/line-item/line-item.html.twig` is a dispatcher, not markup. It reads the type and
includes the matching template:

| Condition | Template |
|---|---|
| `lineItem.type == 'product'` | `type/product.html.twig` |
| `not lineItem.good and totalPrice <= 0`, or type `discount` | `type/discount.html.twig` |
| `lineItem.type == 'container'` | `type/container.html.twig` |
| anything else | `type/generic.html.twig` |

The discount test is deliberately broad: a line item that is not a "good" and costs nothing or less
renders as a discount whatever its type. A custom line item type therefore falls through to
`generic.html.twig` unless you extend the dispatcher — override
`component_line_item_type_include` and add your branch before the fallback.

Each type composes from `component/line-item/element/`: `image`, `label`,
`variant-characteristics`, `quantity`, `unit-price`, `total-price`, `tax-price`,
`delivery-date`, `downloads`, `download-item`, `remove`, `children-wrapper`.

`children-wrapper.html.twig` renders nested line items — a container line item holding a bundle or
a set. `hidden-line-items-information.html.twig` covers items the customer must not see
individually.

## The summary

`page/checkout/summary.html.twig` includes one partial per row, each receiving
`{ summary: ..., isoCode: ... }` through `with`:

| Partial | Row |
|---|---|
| `summary-position.html.twig` | subtotal of the line items |
| `summary-shipping.html.twig` | shipping costs |
| `summary-net.html.twig` | net total |
| `summary-tax.html.twig` | one row per tax rate |
| `summary-total.html.twig` | the total |
| `summary-total-rounded.html.twig` | the cash-rounded total, where total rounding applies |

Two totals exist because item rounding and total rounding are separate settings; the rounded row
appears only when they differ. Prices are formatted with `|currency` — see
`PRICE-AND-QUANTITY.md`.

## The confirm page

`page/checkout/confirm/index.html.twig` (43 blocks), the most-overridden checkout template.

`CheckoutConfirmPage` exposes `getCart()`, `getPaymentMethods()`, `getShippingMethods()`.

```
page_checkout_confirm
├── confirm-address.html.twig     billing and shipping address, with change links
├── confirm-shipping.html.twig    shipping method radio list
├── confirm-payment.html.twig     payment method radio list
├── the line items again, read-only
├── summary.html.twig
├── the terms and revocation checkboxes
└── the submit button
```

Changing shipping or payment submits the form and **recalculates the cart** — shipping costs and
tax can change. The lists are rendered from the page's collections, which are already filtered by
availability rules, so a method absent here is excluded by rule, not by template.

The account order pages reuse these: `page/account/order/index.html.twig` extends the confirm page,
and `address`, `confirm-payment`, `confirm-shipping` under `page/account/order/` extend their
checkout counterparts. **An override of a confirm partial therefore also changes the "edit order"
screen** — verify both.

## Placing the order

```
POST /checkout/order    frontend.checkout.finish.order   CheckoutController::order
  -> the cart is recalculated one final time
  -> the order is created from the cart
  -> the payment handler runs
       redirect payment  -> the provider, returning to frontend.checkout.finish.page
       direct payment    -> straight to the finish page
  -> on failure          -> back to confirm with an error
```

The final recalculation is why a price cannot be trusted from the rendered page: it is recomputed
before the order is written.

## The finish page

`page/checkout/finish/index.html.twig` plus `finish-address.html.twig` and
`finish-details.html.twig`. `CheckoutFinishPage` carries the created `order`, not a cart — the
cart no longer exists.

This is the only page where the order data is available client-side, which makes it the place for
purchase tracking.

## The off-canvas cart

`component/checkout/offcanvas-cart.html.twig` `sw_extends` `utilities/offcanvas.html.twig` and is
loaded over AJAX from `frontend.cart.offcanvas`. It renders the same line item templates as the
cart page, so a line item override applies in both — verify it in the narrow off-canvas width too.

`offcanvas-cart-summary.html.twig` is its condensed summary.

## Every cart route

| Route | Path | Does |
|---|---|---|
| `frontend.checkout.line-item.add` | `POST /checkout/line-item/add` | add a line item |
| `frontend.checkout.product.add-by-number` | `POST /checkout/product/add-by-number` | add by SKU |
| `frontend.checkout.line-item.change-quantity` | `POST /checkout/line-item/change-quantity/{id}` | change one quantity |
| `frontend.checkout.line-items.update` | `POST /checkout/line-item/update` | update several |
| `frontend.checkout.line-item.delete` | `POST /checkout/line-item/delete/{id}` | remove one |
| `frontend.checkout.line-items.delete` | `POST /checkout/line-item/delete` | remove several |
| `frontend.checkout.cart.delete` | `POST /checkout/cart/delete` | empty the cart |
| `frontend.checkout.promotion.add` | `POST /checkout/promotion/add` | apply a promotion code |
| `frontend.checkout.cart.json` | `GET /checkout/cart.json` | the cart as JSON |
| `frontend.checkout.info` | `GET /widgets/checkout/info` | the header cart widget |
| `frontend.cart.offcanvas` | `GET /checkout/offcanvas` | the off-canvas cart |

`frontend.checkout.cart.json` is the cheapest way for custom JavaScript to read the current cart
without scraping the DOM.

## How a cart interaction works

```
the customer changes a quantity or removes an item
  -> the enclosing form submits
       cart page       [data-form-auto-submit]   full page submit
       off-canvas      [data-form-ajax-submit]   AJAX, markup replaced in place
  -> POST to the matching route
  -> the whole cart runs through the processor pipeline again
  -> the response re-renders cart, summary and widget
  -> PluginManager re-initialises the replaced markup
```

**Every interaction recalculates everything.** Promotions can drop out, shipping can change, stock
can be exhausted — which is why `cart-alerts.html.twig` has to stay and why the summary must be
re-rendered with the line items, never cached separately.

Markup replaced by AJAX loses its JavaScript unless `PluginManager` runs again. Custom behaviour
must be a registered plugin, not a script bound once on load.

## Data layer events

Tracking in the checkout is route-driven: each analytics event declares in `supports()` which route
it runs on. From `src/plugin/google-analytics/events/`:

| Event | Fires on | Trigger |
|---|---|---|
| `view-cart` | `frontend.checkout.cart.page`, off-canvas open | page load |
| `checkout-progress` | `frontend.checkout.cart.page` | the checkout button |
| `begin-checkout` | any page | the checkout button |
| `begin-checkout-on-cart` | `frontend.checkout.cart.page` | the checkout button |
| `add-shipping-info` | `frontend.checkout.confirm.page` | shipping method changed |
| `add-payment-info` | `frontend.checkout.confirm.page` | payment method changed |
| `purchase` | `frontend.checkout.finish.page` | page load, gated on `window.trackOrders` |
| `add-to-cart` | any page | `beforeFormSubmit` on the add-to-cart form |
| `remove-from-cart` | cart and off-canvas | the remove form |

Two things to copy when building your own tag manager plugin:

- **`window.trackOrders`** guards the purchase event so a page reload does not count a second
  order. Respect it.
- **`supports(controllerName, actionName, activeRoute)`** decides per page. Use `activeRoute` —
  the first two parameters are deprecated in 6.8.

Order data on the finish page comes from the rendered page, so a template override that removes the
order details can break purchase tracking silently. See
`STRUCTURED-DATA-AND-TRACKING.md` for the plugin structure.

## Rules for changing the checkout

- **Never compute a price in Twig.** The order is written from the recalculated cart; a number
  invented in a template appears nowhere else and makes page, order and invoice disagree.
- **Keep the form structure.** Quantity inputs, remove buttons and method selectors must stay inside
  the form that submits them, and keep their `name` attributes — those are the request payload.
- **Keep `cart-alerts.html.twig`.** It is the only place cart errors surface.
- **Keep the terms and revocation checkboxes.** They are legally required, and removing them lets
  orders through without consent.
- **Extend the line item dispatcher** rather than replacing `line-item.html.twig`, or custom types
  fall back to the generic template.
- **Check the confirm partials twice** — they are shared with the account order pages.
- **Test the off-canvas too**, at its narrow width, whenever you change a line item template.
- **Verify tracking after a template change**, since the analytics events read the rendered markup.
