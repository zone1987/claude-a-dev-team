# Shopware 6 — Webhook-Events Referenz

> Quelle: `resources/references/app-reference/webhook-events-reference.md`

Alle verfügbaren Webhook-Events mit Event-Name, Beschreibung, benötigten Berechtigungen und Payload-Struktur.

---

## Vollständige Event-Tabelle

| Event | Beschreibung | Benötigte Permissions | Payload |
|:------|:-------------|:----------------------|:--------|
| `checkout.customer.before.login` | Wird ausgelöst wenn sich ein Kunde einloggt | — | `{"email":"string"}` |
| `checkout.customer.changed-payment-method` | Wird ausgelöst wenn ein Kunde die Zahlungsmethode im Checkout ändert | `customer:read` | `{"entity":"customer"}` |
| `checkout.customer.deleted` | Wird ausgelöst wenn ein Kunde gelöscht wird | `customer:read` | `{"entity":"customer"}` |
| `checkout.customer.double_opt_in_guest_order` | Wird ausgelöst wenn Double-Opt-In in einer Gastbestellung akzeptiert wird | `customer:read` | `{"entity":"customer","confirmUrl":"string"}` |
| `checkout.customer.double_opt_in_registration` | Wird ausgelöst wenn ein Kunde seine Registrierung via Double-Opt-In bestätigt | `customer:read` | `{"entity":"customer","confirmUrl":"string"}` |
| `checkout.customer.guest_register` | — | `customer:read` | `{"entity":"customer"}` |
| `checkout.customer.login` | Wird ausgelöst wenn sich ein Kunde einloggt | `customer:read` | `{"entity":"customer","contextToken":"string"}` |
| `checkout.customer.logout` | Wird ausgelöst wenn sich ein Kunde ausloggt | `customer:read` | `{"entity":"customer"}` |
| `checkout.customer.register` | Wird ausgelöst wenn ein neuer Kunde registriert wurde | `customer:read` | `{"entity":"customer"}` |
| `checkout.order.payment_method.changed` | — | `order:read` `order_transaction:read` | `{"entity":"order_transaction"}` |
| `checkout.order.placed` | Wird ausgelöst wenn eine Bestellung aufgegeben wird | `order:read` | `{"entity":"order"}` |
| `contact_form.send` | Wird ausgelöst wenn ein Kontaktformular gesendet wird | — | `{"contactFormData":"object"}` |
| `customer.group.registration.accepted` | — | `customer:read` `customer_group:read` | `{"entity":"customer_group"}` |
| `customer.group.registration.declined` | — | `customer:read` `customer_group:read` | `{"entity":"customer_group"}` |
| `customer.recovery.request` | Wird ausgelöst wenn ein Kunde sein Passwort wiederherstellt | `customer_recovery:read` `customer:read` | `{"entity":"customer","resetUrl":"string","shopName":"string"}` |
| `mail.after.create.message` | — | — | `{"data":"array","message":"object"}` |
| `mail.before.send` | Wird ausgelöst bevor eine Mail gesendet wird | — | `{"data":"array","templateData":"array"}` |
| `mail.sent` | Wird ausgelöst wenn eine Mail aus Shopware gesendet wird | — | `{"subject":"string","contents":"string","recipients":"array"}` |
| `newsletter.confirm` | — | `newsletter_recipient:read` | `{"entity":"newsletter_recipient"}` |
| `newsletter.register` | — | `newsletter_recipient:read` | `{"entity":"newsletter_recipient","url":"string"}` |
| `newsletter.unsubscribe` | — | `newsletter_recipient:read` | `{"entity":"newsletter_recipient"}` |
| `product_export.log` | — | — | `{"name":"string"}` |
| `review_form.send` | Wird ausgelöst wenn ein Produktbewertungsformular gesendet wird | `product:read` | `{"reviewFormData":"object","entity":"product"}` |
| `user.recovery.request` | — | `user_recovery:read` | `{"entity":"user_recovery","resetUrl":"string"}` |

---

## Order-State Events (`state_enter.*`)

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

## Order-State Events (`state_leave.*`)

Analog zu `state_enter.*` — gleiche States und Payloads, nur beim Verlassen eines Zustands.

| State-Leave-Events (vollständig) |
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

Alle `state_leave.*`-Events haben `order:read` als Permission und `{"entity":"order"}` als Payload.

---

## Entity-Written/Deleted Events

| Event | Beschreibung | Permissions | Payload |
|:------|:-------------|:------------|:--------|
| `product.written` | Produkt wurde geschrieben | `product:read` | `{"entity":"product","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `product.deleted` | Produkt wurde gelöscht | `product:read` | `{"entity":"product","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `product_price.written` | Produktpreis wurde geschrieben | `product_price:read` | `{"entity":"product_price","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `product_price.deleted` | Produktpreis wurde gelöscht | `product_price:read` | `{"entity":"product_price","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `category.written` | Kategorie wurde geschrieben | `category:read` | `{"entity":"category","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `category.deleted` | Kategorie wurde gelöscht | `category:read` | `{"entity":"category","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `sales_channel.written` | Sales Channel wurde geschrieben | `sales_channel:read` | `{"entity":"sales_channel","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `sales_channel.deleted` | Sales Channel wurde gelöscht | `sales_channel:read` | `{"entity":"sales_channel","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `sales_channel_domain.written` | Sales-Channel-Domain wurde geschrieben | `sales_channel_domain:read` | `{"entity":"sales_channel_domain","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `sales_channel_domain.deleted` | Sales-Channel-Domain wurde gelöscht | `sales_channel_domain:read` | `{"entity":"sales_channel_domain","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `customer.written` | Kunde wurde geschrieben | `customer:read` | `{"entity":"customer","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `customer.deleted` | Kunde wurde gelöscht | `customer:read` | `{"entity":"customer","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `customer_address.written` | Kundenadresse wurde geschrieben | `customer_address:read` | `{"entity":"customer_address","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `customer_address.deleted` | Kundenadresse wurde gelöscht | `customer_address:read` | `{"entity":"customer_address","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `order.written` | Bestellung wurde geschrieben | `order:read` | `{"entity":"order","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `order.deleted` | Bestellung wurde gelöscht | `order:read` | `{"entity":"order","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `order_address.written` | Bestelladresse wurde geschrieben | `order_address:read` | `{"entity":"order_address","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `order_address.deleted` | Bestelladresse wurde gelöscht | `order_address:read` | `{"entity":"order_address","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `document.written` | Dokument wurde geschrieben | `document:read` | `{"entity":"document","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `document.deleted` | Dokument wurde gelöscht | `document:read` | `{"entity":"document","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |
| `media.written` | Media wurde geschrieben | `media:read` | `{"entity":"media","operation":"update insert","primaryKey":"array\|string","payload":"array"}` |
| `media.deleted` | Media wurde gelöscht | `media:read` | `{"entity":"media","operation":"deleted","primaryKey":"array\|string","payload":"array"}` |

---

## App-Lifecycle-Events

| Event | Beschreibung | Permissions | Payload |
|:------|:-------------|:------------|:--------|
| `app.activated` | App wurde aktiviert | — | — |
| `app.deactivated` | App wurde deaktiviert | — | — |
| `app.deleted` | App wurde gelöscht | — | — |
| `app.installed` | App wurde installiert | — | — |
| `app.updated` | App wurde aktualisiert | — | — |
| `shopware.updated` | Shopware wurde aktualisiert | — | — |
