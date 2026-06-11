# Shopware 6 — Alle Standard-Mail-Template-Typen

Quelle: `src/Core/Content/MailTemplate/MailTemplateTypes.php` + Migrations  
Stand: Shopware 6.7 (trunk)

---

## Konventionen

- **technicalName** = Schlüssel in `mail_template_type.technical_name` (Datenbank)
- **Auslösendes Event** = PHP-Klasse + `EVENT_NAME`-Konstante
- **Root-Variablen** = Top-Level-Twig-Variablen (immer zusätzlich: `eventName`, `salesChannelId`)
- Fixtures liegen unter: `src/Core/Migration/Fixtures/mails/<technicalName>/`

---

## 1. Bestellungen (Order)

### `order_confirmation_mail`
- **Zweck:** Bestellbestätigung nach erfolgreicher Bestellung
- **Event:** `CheckoutOrderPlacedEvent` / `checkout.order.placed`
- **Root-Variablen:** `order` (OrderEntity), `salesChannel` (SalesChannelEntity), `a11yDocuments` (array, optional)
- **Fixture:** `order_confirmation_mail/`

### `order.payment_method.changed`
- **Zweck:** Benachrichtigung bei Änderung der Zahlungsmethode
- **Event:** `OrderPaymentMethodChangedEvent` / `checkout.order.payment_method.changed`
- **Root-Variablen:** `order`, `orderTransaction` (OrderTransactionEntity), `customer` (CustomerEntity), `salesChannel`
- **Fixture:** `order.payment_method.changed/`

---

## 2. Order-State-Mails (Bestellstatus)

Alle vier werden von `OrderStateMachineStateChangeEvent` ausgelöst. Das Event setzt den EVENT_NAME dynamisch auf `state_enter.order.<state>`.

### `order.state.open`
- **Zweck:** Bestellung geöffnet/zurückgesetzt
- **Event:** `state_enter.order.open`
- **Root-Variablen:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order.state.open/`

### `order.state.in_progress`
- **Zweck:** Bestellung in Bearbeitung
- **Event:** `state_enter.order.in_progress`
- **Root-Variablen:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order.state.in_progress/`

### `order.state.completed`
- **Zweck:** Bestellung abgeschlossen
- **Event:** `state_enter.order.completed`
- **Root-Variablen:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order.state.completed/`

### `order.state.cancelled`
- **Zweck:** Bestellung storniert
- **Event:** `state_enter.order.cancelled`
- **Root-Variablen:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order.state.cancelled/`

---

## 3. Lieferstatus-Mails (Order Delivery State)

### `order_delivery.state.shipped`
- **Zweck:** Sendung versandt
- **Event:** `state_enter.order_delivery.shipped`
- **Root-Variablen:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.shipped/`

### `order_delivery.state.shipped_partially`
- **Zweck:** Sendung teilweise versandt
- **Event:** `state_enter.order_delivery.shipped_partially`
- **Root-Variablen:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.shipped_partially/`

### `order_delivery.state.returned`
- **Zweck:** Sendung retourniert
- **Event:** `state_enter.order_delivery.returned`
- **Root-Variablen:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.returned/`

### `order_delivery.state.returned_partially`
- **Zweck:** Sendung teilweise retourniert
- **Event:** `state_enter.order_delivery.returned_partially`
- **Root-Variablen:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.returned_partially/`

### `order_delivery.state.cancelled`
- **Zweck:** Lieferung storniert
- **Event:** `state_enter.order_delivery.cancelled`
- **Root-Variablen:** `order`, `salesChannel`, `a11yDocuments`
- **Fixture:** `order_delivery.state.cancelled/`

---

## 4. Zahlungsstatus-Mails (Order Transaction State)

Alle ausgelöst von `OrderStateMachineStateChangeEvent` mit `state_enter.order_transaction.<state>`.

| technicalName | Zweck | Event |
|---|---|---|
| `order_transaction.state.open` | Zahlung offen (zeigt vollst. Bestelldetails) | `state_enter.order_transaction.open` |
| `order_transaction.state.paid` | Zahlung eingegangen | `state_enter.order_transaction.paid` |
| `order_transaction.state.paid_partially` | Teilzahlung eingegangen | `state_enter.order_transaction.paid_partially` |
| `order_transaction.state.refunded` | Zahlung erstattet | `state_enter.order_transaction.refunded` |
| `order_transaction.state.refunded_partially` | Zahlung teilweise erstattet | `state_enter.order_transaction.refunded_partially` |
| `order_transaction.state.cancelled` | Zahlung storniert | `state_enter.order_transaction.cancelled` |
| `order_transaction.state.reminded` | Zahlungserinnerung | `state_enter.order_transaction.reminded` |
| `order_transaction.state.authorized` | Zahlung autorisiert | `state_enter.order_transaction.authorized` |
| `order_transaction.state.chargeback` | Rückbuchung | `state_enter.order_transaction.chargeback` |
| `order_transaction.state.unconfirmed` | Zahlung unbestätigt | `state_enter.order_transaction.unconfirmed` |

**Root-Variablen (alle):** `order`, `salesChannel`, `a11yDocuments`  
**Ausnahme `order_transaction.state.open`:** zeigt vollständige Bestelldetails inkl. `order.nestedLineItems`

---

## 5. Dokument-Mails

Alle ausgelöst wenn ein Dokument erzeugt und versendet wird. Root-Variablen: `order`, `salesChannel`, `a11yDocuments`.

| technicalName | Zweck | Fixture |
|---|---|---|
| `invoice_mail` | Rechnungsversand | `invoice_mail/` |
| `delivery_mail` | Lieferscheinversand | `delivery_mail/` |
| `credit_note_mail` | Gutschriftversand | `credit_note_mail/` |
| `cancellation_mail` | Stornorechnung | `cancellation_mail/` |

---

## 6. Download-Lieferung

### `downloads_delivery`
- **Zweck:** Digitale Downloads nach Zahlung freigeschalten
- **Event:** `CheckoutOrderPlacedEvent` o. Zahlungsevent
- **Root-Variablen:** `order`, `salesChannel`
- **Fixture:** `downloads_delivery/`

---

## 7. Kunden-Mails

### `customer_register`
- **Zweck:** Registrierungsbestätigung
- **Event:** `CustomerRegisterEvent` / `checkout.customer.register`
- **Root-Variablen:** `customer` (CustomerEntity), `salesChannel`
- **Fixture:** inline in `Migration1536233560BasicData`

### `customer_register.double_opt_in`
- **Zweck:** Double-Opt-In-Bestätigung bei Registrierung
- **Event:** `CustomerDoubleOptInRegistrationEvent` / `checkout.customer.double_opt_in_registration`
- **Root-Variablen:** `customer`, `confirmUrl` (string), `salesChannel`
- **Fixture:** inline in `Migration1572425108`

### `guest_order.double_opt_in`
- **Zweck:** Double-Opt-In für Gastbestellung
- **Event:** `DoubleOptInGuestOrderEvent` / `checkout.customer.double_opt_in_guest_order`
- **Root-Variablen:** `customer`, `confirmUrl` (string), `salesChannel`
- **Fixture:** `guest_order.double_opt_in/`

### `password_change`
- **Zweck:** Passwort-Reset-Link
- **Event:** `CustomerAccountRecoverRequestEvent` / `customer.recovery.request`
- **Root-Variablen:** `customer`, `resetUrl` (string), `salesChannel`, `shopName` (string)
- **Fixture:** `password_change/`

### `customer.password.changed`
- **Zweck:** Bestätigung nach erfolgter Passwortänderung (neu in 6.7)
- **Event:** `CustomerPasswordChangedEvent` / `customer.password.changed`
- **Root-Variablen:** `customer`, `shopName` (string), `salesChannel`
- **Fixture:** `customer.password.changed/`

---

## 8. Kundengruppen-Mails

### `customer_group_change_accept` *(legacy)*
- **Zweck:** Kundengruppen-Wechsel genehmigt (älteres System)
- **Root-Variablen:** `salesChannel`

### `customer_group_change_reject` *(legacy)*
- **Zweck:** Kundengruppen-Wechsel abgelehnt (älteres System)
- **Root-Variablen:** keine (statischer Text)

### `customer.group.registration.accepted`
- **Zweck:** Kundengruppen-Registrierung genehmigt
- **Event:** `CustomerGroupRegistrationAccepted` / `customer.group.registration.accepted`
- **Root-Variablen:** `customer`, `customerGroup` (CustomerGroupEntity), `salesChannel`
- **Fixture:** `customer.group.registration.accepted/`

### `customer.group.registration.declined`
- **Zweck:** Kundengruppen-Registrierung abgelehnt
- **Event:** `CustomerGroupRegistrationDeclined` / `customer.group.registration.declined`
- **Root-Variablen:** `customer`, `customerGroup`, `salesChannel`
- **Fixture:** `customer.group.registration.declined/`

---

## 9. Newsletter-Mails

Die Konstanten (`MAILTYPE_NEWSLETTER`, `MAILTYPE_NEWSLETTER_DO_CONFIRM`, `MAILTYPE_NEWSLETTER_CONFIRMED`) sind in `MailTemplateTypes.php` definiert, haben aber keine Fixture-Verzeichnisse. DB-Einträge werden inline in der BasicData-Migration erstellt.

| technicalName (DB) | Zweck | Event |
|---|---|---|
| `newsletterRegister` | Newsletter-Anmeldung-Bestätigung | `newsletter.register` |
| `newsletterDoubleOptIn` | Newsletter-Double-Opt-In | `newsletter.confirm` |

**Root-Variablen:** `newsletterRecipient` (NewsletterRecipientEntity), `url` (string, DOI), `salesChannel`

---

## 10. Kontaktformular

### `contact_form`
- **Zweck:** Kontaktanfrage-Bestätigung (an Shop-Betreiber)
- **Event:** `ContactFormEvent` / `contact_form.send`
- **Root-Variablen:** `contactFormData` (array), `salesChannel`
- **Fixture:** `contact_form/`

---

## 11. Widerrufsformular (neu in 6.7)

### `revocation_request.merchant`
- **Zweck:** Widerrufsantrag an Händler
- **Root-Variablen:** `revocationRequestFormData` (array), `salesChannel`
- **Fixture:** `revocation_request.merchant/`

### `revocation_request.customer`
- **Zweck:** Widerrufsbestätigung an Kunden
- **Root-Variablen:** `revocationRequestFormData` (array), `salesChannel`
- **Fixture:** `revocation_request.customer/`

---

## 12. Produktbewertung

### `review_form`
- **Zweck:** Bewertungsbestätigung/-benachrichtigung
- **Root-Variablen:** `reviewFormData` (array), `product` (ProductEntity), `salesChannel`
- **Fixture:** `review_form/`

---

## 13. SEPA & Lagerwarnungen (inline, keine Fixture-Dirs)

| technicalName | Zweck |
|---|---|
| `sepa_confirmation` | SEPA-Lastschrift-Vorankündigung |
| `product_stock_warning` | Lagerbestand-Warnung (intern) |

---

## 14. Benutzer (Admin-Bereich)

| technicalName | Zweck | Migration |
|---|---|---|
| `user.recovery.request` | Admin-Passwort-Reset | `Migration1562240231` |
| `admin_sso_user_invite` | Admin-SSO-Einladung | `Administration/V6_7/Migration1744203319` |

---

## Aware-Interfaces → Twig-Schlüssel (Referenz)

| Interface | Twig-Schlüssel |
|---|---|
| `OrderAware` | `order`, `orderId` |
| `CustomerAware` | `customer`, `customerId` |
| `CustomerGroupAware` | `customerGroup`, `customerGroupId` |
| `NewsletterRecipientAware` | `newsletterRecipient`, `newsletterRecipientId` |
| `CustomerRecoveryAware` | `customerRecovery`, `customerRecoveryId` |
| `OrderTransactionAware` | `orderTransaction`, `orderTransactionId` |
| `ScalarValuesAware` | dynamisch via `getValues()` |
| `MailAware` | `mailStruct`, `salesChannelId` |
| MailService (immer) | `salesChannel` |
