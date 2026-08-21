# Shopware 6 — All default mail template types

Source: `src/Core/Content/MailTemplate/MailTemplateTypes.php` + migrations  
Status: Shopware 6.7 (trunk)

---

## Contents

- [Conventions](#conventions)
- [1. Orders (Order)](#1-orders-order)
- [2. Order state mails (order status)](#2-order-state-mails-order-status)
- [3. Delivery state mails (Order Delivery State)](#3-delivery-state-mails-order-delivery-state)
- [4. Payment state mails (Order Transaction State)](#4-payment-state-mails-order-transaction-state)
- [5. Document mails](#5-document-mails)
- [6. Download delivery](#6-download-delivery)
- [7. Customer mails](#7-customer-mails)
- [8. Customer group mails](#8-customer-group-mails)
- [9. Newsletter mails](#9-newsletter-mails)
- [10. Contact form](#10-contact-form)
- [11. Revocation form (new in 6.7)](#11-revocation-form-new-in-67)
- [12. Product review](#12-product-review)
- [13. SEPA & stock warnings (inline, no fixture dirs)](#13-sepa-stock-warnings-inline-no-fixture-dirs)
- [14. Users (admin area)](#14-users-admin-area)
- [Aware interfaces → Twig keys (reference)](#aware-interfaces-twig-keys-reference)

## Conventions

- **technicalName** = key in `mail_template_type.technical_name` (database)
- **Triggering event** = PHP class + `EVENT_NAME` constant
- **Root variables** = top-level Twig variables (always additionally: `eventName`, `salesChannelId`)
- Fixtures live under: `src/Core/Migration/Fixtures/mails/<technicalName>/`

---

## 1. Orders (Order)

### `order_confirmation_mail`
- **Purpose:** order confirmation after a successful order
- **Event:** `CheckoutOrderPlacedEvent` / `checkout.order.placed`
- **Root variables:** `order` (OrderEntity), `salesChannel` (SalesChannelEntity), `a11yDocuments` (array, optional)
- **Fixture:** `order_confirmation_mail/`

### `order.payment_method.changed`
- **Purpose:** notification when the payment method changes
- **Event:** `OrderPaymentMethodChangedEvent` / `checkout.order.payment_method.changed`
- **Root variables:** `order`, `orderTransaction` (OrderTransactionEntity), `customer` (CustomerEntity), `salesChannel`
- **Fixture:** `order.payment_method.changed/`

---

## 2. Order state mails (order status)

All four are triggered by `OrderStateMachineStateChangeEvent`. The event sets EVENT_NAME dynamically to `state_enter.order.<state>`.

### `order.state.open`
- **Purpose:** order opened/reset
- **Event:** `state_enter.order.open`
- **Root variables:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order.state.open/`

### `order.state.in_progress`
- **Purpose:** order in progress
- **Event:** `state_enter.order.in_progress`
- **Root variables:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order.state.in_progress/`

### `order.state.completed`
- **Purpose:** order completed
- **Event:** `state_enter.order.completed`
- **Root variables:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order.state.completed/`

### `order.state.cancelled`
- **Purpose:** order cancelled
- **Event:** `state_enter.order.cancelled`
- **Root variables:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order.state.cancelled/`

---

## 3. Delivery state mails (Order Delivery State)

### `order_delivery.state.shipped`
- **Purpose:** shipment shipped
- **Event:** `state_enter.order_delivery.shipped`
- **Root variables:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.shipped/`

### `order_delivery.state.shipped_partially`
- **Purpose:** shipment partially shipped
- **Event:** `state_enter.order_delivery.shipped_partially`
- **Root variables:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.shipped_partially/`

### `order_delivery.state.returned`
- **Purpose:** shipment returned
- **Event:** `state_enter.order_delivery.returned`
- **Root variables:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.returned/`

### `order_delivery.state.returned_partially`
- **Purpose:** shipment partially returned
- **Event:** `state_enter.order_delivery.returned_partially`
- **Root variables:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.returned_partially/`

### `order_delivery.state.cancelled`
- **Purpose:** delivery cancelled
- **Event:** `state_enter.order_delivery.cancelled`
- **Root variables:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.cancelled/`

---

## 4. Payment state mails (Order Transaction State)

All triggered by `OrderStateMachineStateChangeEvent` with `state_enter.order_transaction.<state>`.

| technicalName | Purpose | Event |
|---|---|---|
| `order_transaction.state.open` | payment open (shows full order details) | `state_enter.order_transaction.open` |
| `order_transaction.state.paid` | payment received | `state_enter.order_transaction.paid` |
| `order_transaction.state.paid_partially` | partial payment received | `state_enter.order_transaction.paid_partially` |
| `order_transaction.state.refunded` | payment refunded | `state_enter.order_transaction.refunded` |
| `order_transaction.state.refunded_partially` | payment partially refunded | `state_enter.order_transaction.refunded_partially` |
| `order_transaction.state.cancelled` | payment cancelled | `state_enter.order_transaction.cancelled` |
| `order_transaction.state.reminded` | payment reminder | `state_enter.order_transaction.reminded` |
| `order_transaction.state.authorized` | payment authorized | `state_enter.order_transaction.authorized` |
| `order_transaction.state.chargeback` | chargeback | `state_enter.order_transaction.chargeback` |
| `order_transaction.state.unconfirmed` | payment unconfirmed | `state_enter.order_transaction.unconfirmed` |

**Root variables (all):** `order`, `salesChannel`, `a11yDocuments`  
**Exception `order_transaction.state.open`:** shows full order details incl. `order.nestedLineItems`

---

## 5. Document mails

All triggered when a document is generated and sent. Root variables: `order`, `salesChannel`, `a11yDocuments`.

| technicalName | Purpose | Fixture |
|---|---|---|
| `invoice_mail` | invoice dispatch | `invoice_mail/` |
| `delivery_mail` | delivery note dispatch | `delivery_mail/` |
| `credit_note_mail` | credit note dispatch | `credit_note_mail/` |
| `cancellation_mail` | cancellation invoice | `cancellation_mail/` |

---

## 6. Download delivery

### `downloads_delivery`
- **Purpose:** digital downloads unlocked after payment
- **Event:** `CheckoutOrderPlacedEvent` or a payment event
- **Root variables:** `order`, `salesChannel`
- **Fixture:** `downloads_delivery/`

---

## 7. Customer mails

### `customer_register`
- **Purpose:** registration confirmation
- **Event:** `CustomerRegisterEvent` / `checkout.customer.register`
- **Root variables:** `customer` (CustomerEntity), `salesChannel`
- **Fixture:** inline in `Migration1536233560BasicData`

### `customer_register.double_opt_in`
- **Purpose:** double opt-in confirmation on registration
- **Event:** `CustomerDoubleOptInRegistrationEvent` / `checkout.customer.double_opt_in_registration`
- **Root variables:** `customer`, `confirmUrl` (string), `salesChannel`
- **Fixture:** inline in `Migration1572425108`

### `guest_order.double_opt_in`
- **Purpose:** double opt-in for a guest order
- **Event:** `DoubleOptInGuestOrderEvent` / `checkout.customer.double_opt_in_guest_order`
- **Root variables:** `customer`, `confirmUrl` (string), `salesChannel`
- **Fixture:** `guest_order.double_opt_in/`

### `password_change`
- **Purpose:** password reset link
- **Event:** `CustomerAccountRecoverRequestEvent` / `customer.recovery.request`
- **Root variables:** `customer`, `resetUrl` (string), `salesChannel`, `shopName` (string)
- **Fixture:** `password_change/`

### `customer.password.changed`
- **Purpose:** confirmation after a completed password change (new in 6.7)
- **Event:** `CustomerPasswordChangedEvent` / `customer.password.changed`
- **Root variables:** `customer`, `shopName` (string), `salesChannel`
- **Fixture:** `customer.password.changed/`

---

## 8. Customer group mails

### `customer_group_change_accept` *(legacy)*
- **Purpose:** customer group change approved (older system)
- **Root variables:** `salesChannel`

### `customer_group_change_reject` *(legacy)*
- **Purpose:** customer group change rejected (older system)
- **Root variables:** none (static text)

### `customer.group.registration.accepted`
- **Purpose:** customer group registration approved
- **Event:** `CustomerGroupRegistrationAccepted` / `customer.group.registration.accepted`
- **Root variables:** `customer`, `customerGroup` (CustomerGroupEntity), `salesChannel`
- **Fixture:** `customer.group.registration.accepted/`

### `customer.group.registration.declined`
- **Purpose:** customer group registration rejected
- **Event:** `CustomerGroupRegistrationDeclined` / `customer.group.registration.declined`
- **Root variables:** `customer`, `customerGroup`, `salesChannel`
- **Fixture:** `customer.group.registration.declined/`

---

## 9. Newsletter mails

The constants (`MAILTYPE_NEWSLETTER`, `MAILTYPE_NEWSLETTER_DO_CONFIRM`, `MAILTYPE_NEWSLETTER_CONFIRMED`) are defined in `MailTemplateTypes.php` but have no fixture directories. DB entries are created inline in the BasicData migration.

| technicalName (DB) | Purpose | Event |
|---|---|---|
| `newsletterRegister` | newsletter subscription confirmation | `newsletter.register` |
| `newsletterDoubleOptIn` | newsletter double opt-in | `newsletter.confirm` |

**Root variables:** `newsletterRecipient` (NewsletterRecipientEntity), `url` (string, DOI), `salesChannel`

---

## 10. Contact form

### `contact_form`
- **Purpose:** contact request confirmation (to the shop operator)
- **Event:** `ContactFormEvent` / `contact_form.send`
- **Root variables:** `contactFormData` (array), `salesChannel`
- **Fixture:** `contact_form/`

---

## 11. Revocation form (new in 6.7)

### `revocation_request.merchant`
- **Purpose:** revocation request to the merchant
- **Root variables:** `revocationRequestFormData` (array), `salesChannel`
- **Fixture:** `revocation_request.merchant/`

### `revocation_request.customer`
- **Purpose:** revocation confirmation to the customer
- **Root variables:** `revocationRequestFormData` (array), `salesChannel`
- **Fixture:** `revocation_request.customer/`

---

## 12. Product review

### `review_form`
- **Purpose:** review confirmation/notification
- **Root variables:** `reviewFormData` (array), `product` (ProductEntity), `salesChannel`
- **Fixture:** `review_form/`

---

## 13. SEPA & stock warnings (inline, no fixture dirs)

| technicalName | Purpose |
|---|---|
| `sepa_confirmation` | SEPA direct debit pre-notification |
| `product_stock_warning` | stock level warning (internal) |

---

## 14. Users (admin area)

| technicalName | Purpose | Migration |
|---|---|---|
| `user.recovery.request` | admin password reset | `Migration1562240231` |
| `admin_sso_user_invite` | admin SSO invitation | `Administration/V6_7/Migration1744203319` |

---

## Aware interfaces → Twig keys (reference)

| Interface | Twig key |
|---|---|
| `OrderAware` | `order`, `orderId` |
| `CustomerAware` | `customer`, `customerId` |
| `CustomerGroupAware` | `customerGroup`, `customerGroupId` |
| `NewsletterRecipientAware` | `newsletterRecipient`, `newsletterRecipientId` |
| `CustomerRecoveryAware` | `customerRecovery`, `customerRecoveryId` |
| `OrderTransactionAware` | `orderTransaction`, `orderTransactionId` |
| `ScalarValuesAware` | dynamic via `getValues()` |
| `MailAware` | `mailStruct`, `salesChannelId` |
| MailService (always) | `salesChannel` |
