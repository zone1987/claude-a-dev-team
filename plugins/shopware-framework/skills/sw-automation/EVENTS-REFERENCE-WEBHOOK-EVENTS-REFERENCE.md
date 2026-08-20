# Shopware 6 — Webhook events reference

> Source: `resources/references/app-reference/webhook-events-reference.md`

All available webhook events with event name, description, required permissions and payload structure.

---

## Contents

- [Complete event table](#complete-event-table)
- [Order state events (`state_enter.*`)](#order-state-events-state_enter)
- [Order state events (`state_leave.*`)](#order-state-events-state_leave)
- [Entity written/deleted events](#entity-writtendeleted-events)
- [App lifecycle events](#app-lifecycle-events)

## Complete event table

| Event | Description | Required permissions | Payload |
|:------|:-------------|:----------------------|:--------|
| `checkout.customer.before.login` | Fired when a customer logs in | — | `{"email":"string"}` |
| `checkout.customer.changed-payment-method` | Fired when a customer changes the payment method in the checkout | `customer:read` | `{"entity":"customer"}` |
| `checkout.customer.deleted` | Fired when a customer is deleted | `customer:read` | `{"entity":"customer"}` |
| `checkout.customer.double_opt_in_guest_order` | Fired when double opt-in is accepted in a guest order | `customer:read` | `{"entity":"customer","confirmUrl":"string"}` |
| `checkout.customer.double_opt_in_registration` | Fired when a customer confirms their registration via double opt-in | `customer:read` | `{"entity":"customer","confirmUrl":"string"}` |
| `checkout.customer.guest_register` | — | `customer:read` | `{"entity":"customer"}` |
| `checkout.customer.login` | Fired when a customer logs in | `customer:read` | `{"entity":"customer","contextToken":"string"}` |
| `checkout.customer.logout` | Fired when a customer logs out | `customer:read` | `{"entity":"customer"}` |
| `checkout.customer.register` | Fired when a new customer has registered | `customer:read` | `{"entity":"customer"}` |
| `checkout.order.payment_method.changed` | — | `order:read` `order_transaction:read` | `{"entity":"order_transaction"}` |
| `checkout.order.placed` | Fired when an order is placed | `order:read` | `{"entity":"order"}` |
| `contact_form.send` | Fired when a contact form is submitted | — | `{"contactFormData":"object"}` |
| `customer.group.registration.accepted` | — | `customer:read` `customer_group:read` | `{"entity":"customer_group"}` |
| `customer.group.registration.declined` | — | `customer:read` `customer_group:read` | `{"entity":"customer_group"}` |
| `customer.recovery.request` | Fired when a customer recovers their password | `customer_recovery:read` `customer:read` | `{"entity":"customer","resetUrl":"string","shopName":"string"}` |
| `mail.after.create.message` | — | — | `{"data":"array","message":"object"}` |
| `mail.before.send` | Fired before a mail is sent | — | `{"data":"array","templateData":"array"}` |
| `mail.sent` | Fired when a mail is sent from Shopware | — | `{"subject":"string","contents":"string","recipients":"array"}` |
| `newsletter.confirm` | — | `newsletter_recipient:read` | `{"entity":"newsletter_recipient"}` |
| `newsletter.register` | — | `newsletter_recipient:read` | `{"entity":"newsletter_recipient","url":"string"}` |
| `newsletter.unsubscribe` | — | `newsletter_recipient:read` | `{"entity":"newsletter_recipient"}` |
| `product_export.log` | — | — | `{"name":"string"}` |
| `review_form.send` | Fired when a product review form is submitted | `product:read` | `{"reviewFormData":"object","entity":"product"}` |
| `user.recovery.request` | — | `user_recovery:read` | `{"entity":"user_recovery","resetUrl":"string"}` |

---

## Order state events (`state_enter.*`)

| Event | Permissions | Payload |
|:------|:------------|:--------|
| `state_enter.order.state.cancelled` | `order:read` | `{"entity":"order"}` |
| `state_enter.order.state.completed` | `order:read` | `{"entity":"order"}` |
| `state_enter.order.state.in_progress` | `order:read` | `{"entity":"order"}` |
| `state_enter.order.state.open` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_delivery.state.cancelled` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_delivery.state.open` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_delivery.state.returned` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_delivery.state.returned_partially` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_delivery.state.shipped` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_delivery.state.shipped_partially` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.authorized` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.cancelled` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.chargeback` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.failed` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.in_progress` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.open` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.paid` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.paid_partially` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.refunded` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.refunded_partially` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.reminded` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction.state.unconfirmed` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction_capture.state.completed` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction_capture.state.failed` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction_capture.state.pending` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction_capture_refund.state.cancelled` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction_capture_refund.state.completed` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction_capture_refund.state.failed` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction_capture_refund.state.in_progress` | `order:read` | `{"entity":"order"}` |
| `state_enter.order_transaction_capture_refund.state.open` | `order:read` | `{"entity":"order"}` |

---

## Order state events (`state_leave.*`)

Analogous to `state_enter.*` — same states and payloads, only on leaving a state.

| State leave events (complete)    |
|:----------------------------------|
| `state_leave.order.state.cancelled` |
| `state_leave.order.state.completed` |
| `state_leave.order.state.in_progress` |
| `state_leave.order.state.open` |
| `state_leave.order_delivery.state.cancelled` |
| `state_leave.order_delivery.state.open` |
| `state_leave.order_delivery.state.returned` |
| `state_leave.order_delivery.state.returned_partially` |
| `state_leave.order_delivery.state.shipped` |
| `state_leave.order_delivery.state.shipped_partially` |
| `state_leave.order_transaction.state.authorized` |
| `state_leave.order_transaction.state.cancelled` |
| `state_leave.order_transaction.state.chargeback` |
| `state_leave.order_transaction.state.failed` |
| `state_leave.order_transaction.state.in_progress` |
| `state_leave.order_transaction.state.open` |
| `state_leave.order_transaction.state.paid` |
| `state_leave.order_transaction.state.paid_partially` |
| `state_leave.order_transaction.state.refunded` |
| `state_leave.order_transaction.state.refunded_partially` |
| `state_leave.order_transaction.state.reminded` |
| `state_leave.order_transaction.state.unconfirmed` |
| `state_leave.order_transaction_capture.state.completed` |
| `state_leave.order_transaction_capture.state.failed` |
| `state_leave.order_transaction_capture.state.pending` |
| `state_leave.order_transaction_capture_refund.state.cancelled` |
| `state_leave.order_transaction_capture_refund.state.completed` |
| `state_leave.order_transaction_capture_refund.state.failed` |
| `state_leave.order_transaction_capture_refund.state.in_progress` |
| `state_leave.order_transaction_capture_refund.state.open` |

All `state_leave.*` events have `order:read` as permission and `{"entity":"order"}` as payload.

---

## Entity written/deleted events

| Event | Description | Permissions | Payload |
|:------|:-------------|:------------|:--------|
| `product.written` | Product was written | `product:read` | `{"entity":"product","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `product.deleted` | Product was deleted | `product:read` | `{"entity":"product","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `product_price.written` | Product price was written | `product_price:read` | `{"entity":"product_price","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `product_price.deleted` | Product price was deleted | `product_price:read` | `{"entity":"product_price","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `category.written` | Category was written | `category:read` | `{"entity":"category","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `category.deleted` | Category was deleted | `category:read` | `{"entity":"category","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `sales_channel.written` | Sales channel was written | `sales_channel:read` | `{"entity":"sales_channel","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `sales_channel.deleted` | Sales channel was deleted | `sales_channel:read` | `{"entity":"sales_channel","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `sales_channel_domain.written` | Sales channel domain was written | `sales_channel_domain:read` | `{"entity":"sales_channel_domain","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `sales_channel_domain.deleted` | Sales channel domain was deleted | `sales_channel_domain:read` | `{"entity":"sales_channel_domain","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `customer.written` | Customer was written | `customer:read` | `{"entity":"customer","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `customer.deleted` | Customer was deleted | `customer:read` | `{"entity":"customer","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `customer_address.written` | Customer address was written | `customer_address:read` | `{"entity":"customer_address","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `customer_address.deleted` | Customer address was deleted | `customer_address:read` | `{"entity":"customer_address","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `order.written` | Order was written | `order:read` | `{"entity":"order","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `order.deleted` | Order was deleted | `order:read` | `{"entity":"order","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `order_address.written` | Order address was written | `order_address:read` | `{"entity":"order_address","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `order_address.deleted` | Order address was deleted | `order_address:read` | `{"entity":"order_address","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `document.written` | Document was written | `document:read` | `{"entity":"document","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `document.deleted` | Document was deleted | `document:read` | `{"entity":"document","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `media.written` | Media was written | `media:read` | `{"entity":"media","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `media.deleted` | Media was deleted | `media:read` | `{"entity":"media","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |

---

## App lifecycle events

| Event | Description | Permissions | Payload |
|:------|:-------------|:------------|:--------|
| `app.activated` | App was activated | — | — |
| `app.deactivated` | App was deactivated | — | — |
| `app.deleted` | App was deleted | — | — |
| `app.installed` | App was installed | — | — |
| `app.updated` | App was updated | — | — |
| `shopware.updated` | Shopware was updated | — | — |
