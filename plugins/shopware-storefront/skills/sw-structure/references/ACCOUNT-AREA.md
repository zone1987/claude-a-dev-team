<!-- distilled from shopware/storefront v6.7.13.1 — page/account/, component/account/, component/address/, Page/Account/, Controller/Account*, Controller/AuthController, Controller/RegisterController -->

# Shopware Storefront — the customer account

Every page behind `/account`, what data each one gets and where that data is loaded. The account is
where a theme meets the most forms, the most state and the most legal requirements at once.

## Contents

- [The pages](#the-pages)
- [The frame: _page.html.twig and the sidebar](#the-frame-_pagehtmltwig-and-the-sidebar)
- [Overview](#overview)
- [Profile](#profile)
- [Addresses](#addresses)
- [The address manager modal](#the-address-manager-modal)
- [Order history](#order-history)
- [How orders are loaded](#how-orders-are-loaded)
- [Order detail and documents](#order-detail-and-documents)
- [Cancelling an order](#cancelling-an-order)
- [Editing an order](#editing-an-order)
- [Login, registration and password recovery](#login-registration-and-password-recovery)
- [Guests](#guests)
- [Every account route](#every-account-route)
- [Rules for rebuilding the account](#rules-for-rebuilding-the-account)

## The pages

| Page | Route | Page class | Template |
|---|---|---|---|
| Overview | `frontend.account.home.page` | `AccountOverviewPage` | `page/account/index.html.twig` |
| Profile | `frontend.account.profile.page` | `AccountProfilePage` | `page/account/profile/index.html.twig` |
| Addresses | `frontend.account.address.page` | `AddressListingPage` | `page/account/addressbook/index.html.twig` |
| Create address | `frontend.account.address.create.page` | `AddressDetailPage` | `page/account/addressbook/create.html.twig` |
| Edit address | `frontend.account.address.edit.page` | `AddressDetailPage` | `page/account/addressbook/edit.html.twig` |
| Order history | `frontend.account.order.page` | `AccountOrderPage` | `page/account/order-history/index.html.twig` |
| Single order | `frontend.account.order.single.page` | `AccountOrderPage` | `page/account/order-history/index.html.twig` |
| Edit order | `frontend.account.edit-order.page` | `AccountEditOrderPage` | `page/account/order/index.html.twig` |
| Login | `frontend.account.login.page` | `AccountLoginPage` | `page/account/register/index.html.twig` |
| Register | `frontend.account.register.page` | `AccountLoginPage` | `page/account/register/index.html.twig` |
| Guest login | `frontend.account.guest.login.page` | `AccountLoginPage` | `page/account/guest-auth.html.twig` |
| Recover password | `frontend.account.recover.page` | `AccountRecoverPasswordPage` | `page/account/profile/recover-password.html.twig` |
| Reset password | `frontend.account.recover.password.page` | `AccountRecoverPasswordPage` | `page/account/profile/reset-password.html.twig` |
| Convert guest | `frontend.account.convert.page` | — | `page/account/convert.html.twig` |
| Group registration | `frontend.account.customer-group-registration.page` | `CustomerGroupRegistrationPage` | `page/account/customer-group-register/index.html.twig` |
| Logout | `frontend.account.logout.page` | — | `page/account/logout.html.twig` |

Login and register share one template: `register/index.html.twig` renders both
`component/account/login.html.twig` and `component/account/register.html.twig`, and the route
decides which is emphasised.

## The frame: _page.html.twig and the sidebar

`page/account/_page.html.twig` extends `base.html.twig` and is what every logged-in account page
extends in turn. It provides the two-column layout and includes
`page/account/sidebar.html.twig` — the account navigation.

Pages **outside** the frame extend `base.html.twig` directly, because they are reached without a
session: `register/index.html.twig`, `guest-auth.html.twig`, `recover-password.html.twig`,
`reset-password.html.twig`, `convert.html.twig`, `customer-group-register/index.html.twig`.

That split is the first thing to check when a change appears on some account pages but not others.

Blocks: `page_account_main`, `page_account_sidebar`, `page_account_content`, plus the
`page_account_sidebar_*` blocks for the navigation entries.

## Overview

`AccountOverviewPage` exposes:

| Getter | Type | Loaded from |
|---|---|---|
| `getCustomer()` | `CustomerEntity` | `AbstractCustomerRoute` |
| `getNewestOrder()` | `?OrderEntity` | `AbstractOrderRoute`, limit 1, newest first |
| `getNewsletterAccountPagelet()` | `NewsletterAccountPagelet` | `NewsletterAccountPageletLoader` |

`getNewestOrder()` is nullable — a new customer has none, and the template must guard.

The overview renders the default billing and shipping address through
`component/address/address.html.twig`, and the personal data through
`component/account/customer-overview-personal-company.html.twig`.

## Profile

`AccountProfilePage` carries only `getSalutations()`; the customer itself comes from
`context.customer`.

`page/account/profile/index.html.twig` (52 blocks) holds **three independent forms**, each posting
to its own route:

| Form | Route | Changes |
|---|---|---|
| Personal data | `frontend.account.profile.save` | salutation, name, birthday, company, VAT id |
| Email | `frontend.account.profile.email.save` | email, requires the current password |
| Password | `frontend.account.profile.password.save` | password, requires the current password |

Plus `frontend.account.profile.delete` for account deletion.

Email and password changes require `password` — the current one — as a separate field. That is a
security requirement, not a convention: removing it lets a hijacked session change the credentials.

## Addresses

`AddressListingPage` exposes `getAddresses()`, `getSalutations()`, `getCountries()`, `getCart()` and
`getAddress()`.

```
page/account/addressbook/index.html.twig
├── component/address/addresses-base.html.twig     the list frame
├── addressbook/address-item.html.twig             one address card
├── addressbook/address-actions.html.twig          edit, delete
├── addressbook/default-address-actions.html.twig  set as default billing or shipping
└── component/address/address-form.html.twig       used by create.html.twig and edit.html.twig
```

`address-form.html.twig` composes from `component/address/field/`: salutation, first and last name,
company, department, VAT id, street, additional line, zipcode, city, country, country state, phone.
Each field is its own template, so a theme can override one without touching the form.

**Country and country state are coupled**: the state select is driven by
`[data-country-state-select]`, which reloads the available states when the country changes. Keep the
attribute and the field ids, or the state field stops updating.

## The address manager modal

A separate flow used in the checkout: `component/address/address-manager-modal.html.twig` with
`-list` and `-create-address` variants, loaded over
`frontend.account.addressmanager.get` and posted to `frontend.account.addressmanager`.

It exists so a customer can change an address without leaving the checkout. `[data-address-manager]`
drives it; `frontend.account.addressmanager.switch` swaps the selected address.

## Order history

`AccountOrderPage` exposes `getOrders()` — an `EntitySearchResult` of orders — and
`getDeepLinkCode()`.

```
page/account/order-history/index.html.twig
└── order-item.html.twig            one order, collapsed        (38 blocks)
    └── order-detail.html.twig      the expanded detail          (39 blocks)
        ├── order-detail-list.html.twig      the line items
        ├── order-detail-document.html.twig  the documents
        └── order-detail-document-item.html.twig
```

The detail is loaded **on demand**: expanding an order requests
`widgets.account.order.detail` and renders `order-detail-list.html.twig` into the row. The list page
therefore stays light regardless of how many orders a customer has.

## How orders are loaded

`AccountOrderPageLoader` builds the criteria and calls `AbstractOrderRoute`:

```php
$criteria = (new Criteria())
    ->addSorting(new FieldSorting('order.createdAt', FieldSorting::DESCENDING))
    ->addAssociation('primaryOrderTransaction.paymentMethod')
    ->addAssociation('primaryOrderTransaction.stateMachineState')
    ->addAssociation('primaryOrderDelivery.shippingMethod')
    ->addAssociation('primaryOrderDelivery.stateMachineState')
    ->addAssociation('deliveries.shippingMethod')
    ->addAssociation('orderCustomer.customer')
    ->addAssociation('lineItems')
    ->addAssociation('lineItems.cover')
    ->addAssociation('lineItems.downloads.media')
    ->addAssociation('addresses')
    ->addAssociation('currency')
    ->addAssociation('stateMachineState')
    ->addAssociation('documents.documentType')
    ->addAssociation('documents.documentMediaFile')
    ->addAssociation('documents.documentA11yMediaFile');
```

Then `OrderRouteRequestEvent` fires **before** the route runs. That event is the extension point:
subscribe to it and add an association or a filter when your template needs data the criteria does
not load. Adding it in a page subscriber afterwards means a second query per order.

Newest first, and the deep link code is what lets a guest reach a single order without an account.

## Order detail and documents

Documents — invoice, delivery note, credit note — come from the `documents` association. Each has a
`documentType`, a `documentMediaFile` and, since accessibility became mandatory, a
`documentA11yMediaFile`: an accessible variant of the same document.

`order-detail-document-item.html.twig` renders both when present. **Keep the accessible variant**;
offering only the visual PDF is exactly what BFSG requires shops to stop doing.

## Cancelling an order

```
the customer opens page/account/order/cancel-order-modal.html.twig
  -> POST frontend.account.order.cancel with orderId
  -> AccountOrderController::cancelOrder
       builds { orderId, transition: 'cancel' }
       dispatches CancelOrderRouteRequestEvent
       calls AbstractCancelOrderRoute::cancel
  -> the order state machine transitions to 'cancelled'
  -> a logged-in customer returns to frontend.account.order.page
     a guest returns to frontend.account.order.single.page with the deep link code
```

Two things follow from this being a **state machine transition**:

- **Cancellation is only possible when the transition is allowed.** The state machine decides;
  an already-shipped order has no `cancel` transition, and the button must not be shown.
- **Cancelling does not refund.** It moves the order state. Payment and refund are separate
  transitions handled by the payment method.

The transition fires the usual state machine events, so a Flow Builder flow can send the
confirmation mail.

## Editing an order

`frontend.account.edit-order.page` handles a failed or open payment. `AccountEditOrderPage` carries
the order plus the available payment and shipping methods.

`page/account/order/index.html.twig` **extends the checkout confirm page**, and
`order/address.html.twig`, `order/confirm-payment.html.twig` and `order/confirm-shipping.html.twig`
extend their checkout counterparts.

**So an override of a checkout confirm partial also changes the edit-order screen.** Verify both
whenever you touch `page/checkout/confirm/`.

`frontend.account.edit-order.change-payment-method` switches the method;
`frontend.account.edit-order.update-order` retries the payment.

## Login, registration and password recovery

`AccountLoginPage` carries the salutations and countries the register form needs.

| Route | Method | Does |
|---|---|---|
| `frontend.account.login` | POST | authenticate |
| `frontend.account.register.save` | POST | create the account |
| `frontend.account.register.mail` | GET | confirm a double opt-in registration |
| `frontend.account.recover.request` | POST | send the recovery mail |
| `frontend.account.recover.password.reset` | POST | set the new password |
| `frontend.account.logout.page` | GET | end the session |
| `frontend.account.login.imitate-customer` | POST | log in as a customer from the administration |

`component/account/register.html.twig` (36 blocks) is the register form: personal data, billing
address, optional different shipping address, password, privacy consent, and the double opt-in
notice where enabled.

Registration is also reachable from the checkout as `frontend.checkout.register.page`, rendering
`page/checkout/address/index.html.twig`, which extends the same component. One form, two contexts.

## Guests

A guest checkout creates a customer with `guest = true`. Three consequences visible in templates:

- **Orders are reached by deep link code**, not by session — `frontend.account.order.single.page`.
- **`guest-auth.html.twig`** asks for the email and postcode to open that order.
- **`convert.html.twig`** (new in 6.7.13) turns a guest into a full account by setting a password,
  posting to `frontend.account.convert.save`.

Templates must guard with `context.customer.guest` before offering account features.

## Every account route

| Route | Path | Method |
|---|---|---|
| `frontend.account.home.page` | `/account` | GET |
| `frontend.account.profile.page` | `/account/profile` | GET |
| `frontend.account.profile.save` | `/account/profile` | POST |
| `frontend.account.profile.email.save` | `/account/profile/email` | POST |
| `frontend.account.profile.password.save` | `/account/profile/password` | POST |
| `frontend.account.profile.delete` | `/account/profile/delete` | POST |
| `frontend.account.address.page` | `/account/address` | GET |
| `frontend.account.address.create.page` | `/account/address/create` | GET |
| `frontend.account.address.create` | `/account/address/create` | POST |
| `frontend.account.address.edit.page` | `/account/address/{addressId}` | GET |
| `frontend.account.address.edit.save` | `/account/address/{addressId}` | POST |
| `frontend.account.address.delete` | `/account/address/delete/{addressId}` | POST |
| `frontend.account.address.set-default-address` | `/account/address/default-{type}/{addressId}` | POST |
| `frontend.account.address.switch-default` | `/account/address/switch` | POST |
| `frontend.account.addressmanager.get` | `/widgets/account/address-manager` | GET |
| `frontend.account.addressmanager` | `/widgets/account/address-manager/{addressId?}` | POST |
| `frontend.account.addressmanager.switch` | `/widgets/account/address-manager/switch` | POST |
| `frontend.account.order.page` | `/account/order` | GET, POST |
| `frontend.account.order.single.page` | `/account/order/{deepLinkCode}` | GET |
| `frontend.account.order.cancel` | `/account/order/cancel` | POST |
| `widgets.account.order.detail` | `/widgets/account/order/detail/{id}` | GET |
| `frontend.account.edit-order.page` | `/account/order/edit/{orderId}` | GET, POST |
| `frontend.account.edit-order.change-payment-method` | `/account/order/payment/{orderId}` | POST |
| `frontend.account.edit-order.update-order` | `/account/order/update/{orderId}` | POST |
| `frontend.account.login.page` | `/account/login` | GET |
| `frontend.account.login` | `/account/login` | POST |
| `frontend.account.guest.login.page` | `/account/guest/login` | GET |
| `frontend.account.logout.page` | `/account/logout` | GET |
| `frontend.account.recover.page` | `/account/recover` | GET |
| `frontend.account.recover.request` | `/account/recover` | POST |
| `frontend.account.recover.password.page` | `/account/recover/password` | GET |
| `frontend.account.recover.password.reset` | `/account/recover/password` | POST |
| `frontend.account.register.page` | `/account/register` | GET |
| `frontend.account.register.save` | `/account/register` | POST |
| `frontend.account.register.mail` | `/registration/confirm` | GET |
| `frontend.account.convert.page` | `/account/convert` | GET |
| `frontend.account.convert.save` | `/account/convert` | POST |
| `frontend.account.customer-group-registration.page` | `/customer-group-registration/{customerGroupId}` | GET |
| `frontend.account.newsletter` | `/widgets/account/newsletter` | POST |
| `frontend.account.login.imitate-customer` | `/account/login/imitate-customer` | POST |

## Rules for rebuilding the account

- **Know which frame a page uses.** Pages inside `_page.html.twig` get the sidebar; the
  session-less ones extend `base.html.twig` directly.
- **Keep the three profile forms separate.** They post to different routes and have different
  validation; merging them into one breaks all three.
- **Keep the current-password fields** on the email and password forms.
- **Extend the order criteria through `OrderRouteRequestEvent`**, never with a second query per
  order in the template.
- **Do not show a cancel button unconditionally** — check that the state machine allows the
  transition.
- **Remember the edit-order screen** when changing checkout confirm partials.
- **Keep `[data-country-state-select]`** and the field ids in address forms.
- **Offer the accessible document variant** where `documentA11yMediaFile` exists.
- **Guard guest features** with `context.customer.guest`.
