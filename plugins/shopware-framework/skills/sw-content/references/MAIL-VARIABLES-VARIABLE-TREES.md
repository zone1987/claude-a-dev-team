# Shopware 6 — the complete variable tree per mail template

Abgeleitet aus echten Entity-Definitionen + Default-Twig-Fixtures.  
Stand: Shopware 6.7 (trunk)

Legende: `(?)` = nullable, `[*]` = Collection/Array, `→` = Assoziation/Sub-Objekt

---

## Contents

- [`order_confirmation_mail` — order confirmation](#order_confirmation_mail--order-confirmation)
- [`order.state.*` — Bestellstatus-Benachrichtigungen](#orderstate-bestellstatus-benachrichtigungen)
- [`order_delivery.state.*` — Lieferstatus-Benachrichtigungen](#order_deliverystate-lieferstatus-benachrichtigungen)
- [`order_transaction.state.*` — Zahlungsstatus-Benachrichtigungen](#order_transactionstate-zahlungsstatus-benachrichtigungen)
- [`order.payment_method.changed` — payment method changed](#orderpayment_methodchanged--payment-method-changed)
- [`invoice_mail` / `delivery_mail` / `credit_note_mail` / `cancellation_mail` — Dokument-Mails](#invoice_mail-delivery_mail-credit_note_mail-cancellation_mail-dokument-mails)
- [`downloads_delivery` — Digitale Downloads](#downloads_delivery-digitale-downloads)
- [`customer_register` — registration confirmation](#customer_register--registration-confirmation)
- [`customer_register.double_opt_in` — DOI Registrierung](#customer_registerdouble_opt_in-doi-registrierung)
- [`guest_order.double_opt_in` — DOI Gastbestellung](#guest_orderdouble_opt_in-doi-gastbestellung)
- [`password_change` — Passwort-Reset-Anfrage](#password_change-passwort-reset-anfrage)
- [`customer.password.changed` — password changed successfully (6.7)](#customerpasswordchanged--password-changed-successfully-67)
- [`customer.group.registration.accepted` / `.declined` — Kundengruppen-Registrierung](#customergroupregistrationaccepted-declined-kundengruppen-registrierung)
- [`newsletterRegister` / `newsletterDoubleOptIn` — Newsletter](#newsletterregister-newsletterdoubleoptin-newsletter)
- [`contact_form` — Kontaktformular](#contact_form-kontaktformular)
- [`revocation_request.customer` / `.merchant` — Widerrufsformular (6.7)](#revocation_requestcustomer-merchant-widerrufsformular-67)
- [`review_form` — Produktbewertung](#review_form-produktbewertung)
- [Variables always available (every template)](#variables-always-available-every-template)
- [Adding variables of your own](#adding-variables-of-your-own)

## `order_confirmation_mail` — order confirmation

The same structure applies to `order_transaction.state.open`, which adds a payment note in its intro.

### Top-Level-Variablen

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
a11yDocuments       [*] → array (optional, for accessible document links)
eventName           string
salesChannelId      string (UUID)
```

### `order.*` — the complete tree

```
order
├── orderNumber                   string
├── orderDateTime                 \DateTimeInterface
├── orderDate                     \DateTimeInterface
├── amountTotal                   float
├── amountNet                     float
├── positionPrice                 float
├── shippingTotal                 float
├── taxStatus                     string ("gross"|"net"|"tax-free")
├── deepLinkCode                  string  ← Kunden-Login-Link
├── affiliateCode                 string(?)
├── campaignCode                  string(?)
├── customerComment               string(?)
├── internalComment               string(?)
├── currencyFactor                float
├── billingAddressId              string (UUID)
│
├── price                         → CartPrice
│   ├── totalPrice                float
│   ├── rawTotal                  float
│   ├── netPrice                  float
│   ├── taxStatus                 string
│   └── calculatedTaxes           [*] → CalculatedTax
│       ├── taxRate               float
│       ├── tax                   float
│       └── price                 float
│
├── shippingCosts                 → CalculatedPrice
│   ├── totalPrice                float
│   ├── unitPrice                 float
│   └── quantity                  int
│
├── totalRounding                 → CashRoundingConfig
│   ├── decimals                  int
│   └── interval                  float
│
├── itemRounding                  → CashRoundingConfig
│   └── decimals                  int
│
├── currency                      → CurrencyEntity
│   ├── isoCode                   string  (z.B. "EUR")
│   ├── symbol                    string  (z.B. "€")
│   ├── name                      string(?) (translated)
│   ├── shortName                 string(?) (translated)
│   └── factor                    float
│
├── orderCustomer                 → OrderCustomerEntity
│   ├── email                     string
│   ├── firstName                 string
│   ├── lastName                  string
│   ├── title                     string(?)
│   ├── company                   string(?)
│   ├── customerNumber            string(?)
│   ├── vatIds                    array<string>(?)
│   └── salutation                → SalutationEntity(?)
│       ├── salutationKey         string  ("mr"|"mrs"|"not_specified")
│       ├── letterName            string(?) (translated, z.B. "Sehr geehrter Herr")
│       └── displayName           string(?) (translated, z.B. "Herr")
│
├── stateMachineState             → StateMachineStateEntity
│   ├── technicalName             string  ("open"|"in_progress"|"completed"|"cancelled")
│   └── name                      string(?) (translated, z.B. "Offen")
│
├── billingAddress                → OrderAddressEntity (via order.addresses.get(order.billingAddressId))
│   ├── firstName                 string
│   ├── lastName                  string
│   ├── street                    string
│   ├── zipcode                   string(?)
│   ├── city                      string
│   ├── company                   string(?)
│   ├── department                string(?)
│   ├── title                     string(?)
│   ├── phoneNumber               string(?)
│   ├── additionalAddressLine1    string(?)
│   ├── additionalAddressLine2    string(?)
│   ├── salutation                → SalutationEntity(?)
│   │   ├── letterName            string(?) (translated)
│   │   └── displayName           string(?) (translated)
│   ├── country                   → CountryEntity
│   │   ├── name                  string(?) (translated)
│   │   └── iso                   string(?)
│   └── countryState              → CountryStateEntity(?)
│       └── name                  string(?) (translated)
│
├── addresses                     [*] → OrderAddressCollection
│   └── (each entry = OrderAddressEntity, Felder wie billingAddress oben)
│
├── deliveries                    [*] → OrderDeliveryCollection
│   └── (each entry = OrderDeliveryEntity, s.u.)
│
├── deliveries.first              → OrderDeliveryEntity (Convenience-Zugriff)
│   ├── trackingCodes             array<string>
│   ├── shippingDateEarliest      \DateTimeInterface
│   ├── shippingDateLatest        \DateTimeInterface
│   ├── shippingCosts             → CalculatedPrice
│   │   └── totalPrice            float
│   ├── stateMachineState         → StateMachineStateEntity
│   │   ├── technicalName         string
│   │   └── name                  string(?) (translated)
│   ├── shippingMethod            → ShippingMethodEntity
│   │   ├── name                  string(?) (translated)
│   │   ├── description           string(?) (translated)
│   │   └── trackingUrl           string(?)  ← holds %s for the tracking number
│   └── shippingOrderAddress      → OrderAddressEntity (Lieferadresse)
│       ├── firstName             string
│       ├── lastName              string
│       ├── street                string
│       ├── zipcode               string(?)
│       ├── city                  string
│       ├── company               string(?)
│       ├── additionalAddressLine1 string(?)
│       ├── additionalAddressLine2 string(?)
│       └── country               → CountryEntity
│           └── name              string(?) (translated)
│
├── transactions                  [*] → OrderTransactionCollection
├── transactions.first            → OrderTransactionEntity
│   ├── amount                    → CalculatedPrice
│   │   └── totalPrice            float
│   ├── stateMachineState         → StateMachineStateEntity
│   │   ├── technicalName         string
│   │   └── name                  string(?) (translated)
│   └── paymentMethod             → PaymentMethodEntity
│       ├── name                  string(?) (translated)
│       ├── distinguishableName   string(?) (translated)
│       ├── description           string(?) (translated)
│       ├── shortName             string(?)
│       └── technicalName         string
│
├── nestedLineItems               [*] → OrderLineItemCollection (verschachtelt)
│   └── (each entry = OrderLineItemEntity, s.u.)
│
├── lineItems                     [*] → OrderLineItemCollection (flach)
│   └── (each entry = OrderLineItemEntity, s.u.)
│
└── documents                     [*] → DocumentCollection
    └── (each entry = DocumentEntity)
```

### `order.nestedLineItems[*]` — Positionen-Baum

```
lineItem (each in order.nestedLineItems)
├── label                         string   ← Produktname zum Bestellzeitpunkt
├── quantity                      int
├── unitPrice                     float
├── totalPrice                    float
├── description                   string(?)
├── type                          string(?)  ("product"|"promotion"|"credit"|"custom")
├── position                      int
├── good                          bool
├── referencedId                  string(?)  (Produkt-UUID)
├── identifier                    string     (the cart key)
│
├── price                         → CalculatedPrice(?)
│   ├── totalPrice                float
│   ├── unitPrice                 float
│   ├── quantity                  int
│   └── calculatedTaxes           [*] → CalculatedTax
│
├── payload                       array(?)   ← snapshot data taken at order time
│   ├── productNumber             string
│   ├── manufacturerId            string(?)
│   ├── taxId                     string(?)
│   ├── productType               string
│   ├── categoryIds               array
│   ├── options                   [*] → array (Variantenoptionen)
│   │   └── {group: string, option: string}
│   └── features                  [*] → array (Produktmerkmale)
│       └── {type: string, value: {…}}
│
├── cover                         → MediaEntity(?)
│   └── url                       string
│
├── product                       → ProductEntity(?)
│   ├── productNumber             string
│   ├── name                      string(?) (translated)
│   ├── description               string(?) (translated)
│   ├── ean                       string(?)
│   ├── manufacturerNumber        string(?)
│   ├── stock                     int
│   ├── weight                    float(?)
│   └── manufacturer              → ProductManufacturerEntity(?)
│       └── name                  string(?) (translated)
│
├── children                      [*] → OrderLineItemCollection (rekursiv)
│   └── children.count            int
│
└── downloads                     [*] → OrderLineItemDownloadCollection
    └── (each entry = OrderLineItemDownloadEntity)
        ├── accessGranted         bool
        ├── id                    string (UUID)
        └── media                 → MediaEntity
            ├── fileName          string
            └── fileExtension     string
```

### `salesChannel.*`

```
salesChannel
├── name                          string(?) (translated)
├── shortName                     string(?)
├── active                        bool
├── taxCalculationType            string
├── domains                       [*] → SalesChannelDomainCollection
│   └── domains|first             → SalesChannelDomainEntity
│       └── url                   string   ← z.B. "https://shop.example.com"
├── currency                      → CurrencyEntity
├── language                      → LanguageEntity
├── country                       → CountryEntity
├── paymentMethod                 → PaymentMethodEntity  (Standard)
├── shippingMethod                → ShippingMethodEntity (Standard)
└── mailHeaderFooter              → MailHeaderFooterEntity(?)
```

### `a11yDocuments[*]` — Barrierefreie Dokumente

```
a11yDocuments (array)
└── each entry
    ├── documentId               string (UUID)
    ├── deepLinkCode             string
    └── fileExtension            string
```

---

## `order.state.*` — Bestellstatus-Benachrichtigungen

Applies to: `order.state.open`, `order.state.in_progress`, `order.state.completed`, `order.state.cancelled`

### Top-Level-Variablen

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
a11yDocuments       [*] (optional)
eventName           string
salesChannelId      string
```

### Verwendete Pfade

```
order
├── orderNumber                   string
├── orderDateTime                 \DateTimeInterface
├── deepLinkCode                  string
├── stateMachineState             → StateMachineStateEntity
│   └── name                      string (translated)  ← z.B. "Abgeschlossen"
└── orderCustomer                 → OrderCustomerEntity
    ├── firstName                 string
    ├── lastName                  string
    └── salutation                → SalutationEntity(?)
        └── letterName            string(?) (translated)

salesChannel
├── name                          string(?) (translated)
└── domains|first.url             string

a11yDocuments[]
├── documentId                    string
├── deepLinkCode                  string
└── fileExtension                 string
```

---

## `order_delivery.state.*` — Lieferstatus-Benachrichtigungen

Applies to: `shipped`, `shipped_partially`, `returned`, `returned_partially`, `cancelled`

### Top-Level-Variablen

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
a11yDocuments       [*] (optional)
```

### Verwendete Pfade

```
order
├── orderNumber                   string
├── orderDateTime                 \DateTimeInterface
├── deepLinkCode                  string
├── deliveries.first              → OrderDeliveryEntity
│   └── stateMachineState         → StateMachineStateEntity
│       └── name                  string (translated)  ← z.B. "Versendet"
└── orderCustomer                 → OrderCustomerEntity
    ├── firstName, lastName, salutation.letterName

salesChannel.name / salesChannel.domains|first.url
a11yDocuments[].documentId / .deepLinkCode / .fileExtension
```

**Tipp — Tracking-URL ausgeben:**
```twig
{% set delivery = order.deliveries.first %}
{% for code in delivery.trackingCodes %}
  <a href="{{ delivery.shippingMethod.trackingUrl|replace({'%s': code}) }}">{{ code }}</a>
{% endfor %}
```

---

## `order_transaction.state.*` — Zahlungsstatus-Benachrichtigungen

Applies to all but `order_transaction.state.open`, which carries the full order detail.

### Top-Level-Variablen

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
a11yDocuments       [*] (optional)
```

### Verwendete Pfade

```
order
├── orderNumber                   string
├── orderDateTime                 \DateTimeInterface
├── deepLinkCode                  string
├── transactions.first            → OrderTransactionEntity
│   └── stateMachineState         → StateMachineStateEntity
│       └── name                  string (translated)  ← z.B. "Bezahlt"
└── orderCustomer → firstName, lastName, salutation.letterName
```

---

## `order.payment_method.changed` — payment method changed

### Top-Level-Variablen

```
order               → OrderEntity
orderTransaction    → OrderTransactionEntity
customer            → CustomerEntity
salesChannel        → SalesChannelEntity
```

### Verwendete Pfade

```
order
├── orderNumber                   string
└── orderCustomer → firstName, lastName, salutation(?)

order.transactions.last           → OrderTransactionEntity  ← NOTE: .last, not .first
└── paymentMethod
    └── name                      string (translated)
```

---

## `invoice_mail` / `delivery_mail` / `credit_note_mail` / `cancellation_mail` — Dokument-Mails

### Top-Level-Variablen

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
a11yDocuments       [*] (optional)
```

### Verwendete Pfade

```
order
├── orderNumber                   string
└── orderCustomer → firstName, lastName, salutation.letterName

salesChannel.domains|first.url

a11yDocuments[].documentId / .deepLinkCode / .fileExtension
```

---

## `downloads_delivery` — Digitale Downloads

### Top-Level-Variablen

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
```

### Verwendete Pfade

```
order
├── orderNumber                   string
├── id                            string (UUID)
├── deepLinkCode                  string
└── lineItems                     [*] → OrderLineItemCollection
    └── each lineItem
        ├── label                 string
        ├── payload.productNumber string (if defined)
        └── downloads             [*] → OrderLineItemDownloadCollection
            └── each download
                ├── accessGranted bool
                ├── id            string (UUID)
                └── media         → MediaEntity
                    ├── fileName      string
                    └── fileExtension string

salesChannel.domains|first.url
```

---

## `customer_register` — registration confirmation

### Top-Level-Variablen

```
customer            → CustomerEntity
salesChannel        → SalesChannelEntity
```

### `customer.*` — the complete tree

```
customer
├── customerNumber                string
├── firstName                     string
├── lastName                      string
├── email                         string
├── title                         string(?)
├── company                       string(?)
├── accountType                   string  ("private"|"business")
├── active                        bool
├── guest                         bool
├── birthday                      \DateTimeInterface(?)
├── firstLogin                    \DateTimeInterface(?)
├── lastLogin                     \DateTimeInterface(?)
├── doubleOptInRegistration       bool
├── doubleOptInConfirmDate        \DateTimeInterface(?)
├── affiliateCode                 string(?)
├── campaignCode                  string(?)
├── vatIds                        array<string>(?)
│
├── salutation                    → SalutationEntity(?)
│   ├── salutationKey             string
│   ├── letterName                string(?) (translated)
│   └── displayName               string(?) (translated)
│
├── language                      → LanguageEntity
│   └── name                      string
│
├── group                         → CustomerGroupEntity
│   ├── name                      string(?) (translated)
│   └── displayGross              bool
│
├── defaultBillingAddress         → CustomerAddressEntity
│   ├── firstName, lastName, street, zipcode, city
│   ├── company, department, title, phoneNumber
│   ├── additionalAddressLine1/2
│   ├── country                   → CountryEntity
│   │   ├── name (translated), iso, iso3
│   └── salutation                → SalutationEntity(?)
│
├── defaultShippingAddress        → CustomerAddressEntity (gleiche Felder)
│
├── salesChannel                  → SalesChannelEntity
│   ├── name (translated)
│   └── domains|first.url
│
└── lastPaymentMethod             → PaymentMethodEntity(?)
    ├── name (translated)
    └── description (translated)
```

---

## `customer_register.double_opt_in` — DOI Registrierung

### Top-Level-Variablen

```
customer            → CustomerEntity  (Felder wie oben)
confirmUrl          string            ← the confirmation link
salesChannel        → SalesChannelEntity
```

---

## `guest_order.double_opt_in` — DOI Gastbestellung

### Top-Level-Variablen

```
customer            → CustomerEntity
confirmUrl          string            ← the confirmation link
salesChannel        → SalesChannelEntity
```

### Verwendete Pfade

```
customer.salutation.translated.displayName
customer.lastName
confirmUrl   (direkte Twig-Variable)
```

---

## `password_change` — Passwort-Reset-Anfrage

### Top-Level-Variablen

```
customer            → CustomerEntity
resetUrl            string            ← Reset-Link
salesChannel        → SalesChannelEntity
shopName            string
```

### Verwendete Pfade

```
customer.salutation.translated.letterName
customer.firstName
customer.lastName
resetUrl
salesChannel.translated.name
shopName
```

---

## `customer.password.changed` — password changed successfully (6.7)

### Top-Level-Variablen

```
customer            → CustomerEntity
shopName            string
salesChannel        → SalesChannelEntity
```

### Verwendete Pfade

```
customer.firstName
customer.lastName
shopName
```

---

## `customer.group.registration.accepted` / `.declined` — Kundengruppen-Registrierung

### Top-Level-Variablen

```
customer            → CustomerEntity
customerGroup       → CustomerGroupEntity
salesChannel        → SalesChannelEntity
```

### Verwendete Pfade

```
customer.salutation.translated.letterName
customer.lastName
customerGroup.translated.name
```

---

## `newsletterRegister` / `newsletterDoubleOptIn` — Newsletter

### Top-Level-Variablen

```
newsletterRecipient → NewsletterRecipientEntity
url                 string   ← the double-opt-in confirmation link, on registration
salesChannel        → SalesChannelEntity
```

### `newsletterRecipient.*`

```
newsletterRecipient
├── email                         string
├── firstName                     string(?)
├── lastName                      string(?)
├── title                         string(?)
├── zipCode                       string(?)
├── city                          string(?)
├── street                        string(?)
├── status                        string  ("notSet"|"direct"|"optIn"|"optOut")
├── hash                          string  ← for unsubscribe and confirmation links
├── confirmedAt                   \DateTimeInterface(?)
└── salutation                    → SalutationEntity(?)
    ├── letterName (translated)
    └── displayName (translated)
```

---

## `contact_form` — Kontaktformular

### Top-Level-Variablen

```
contactFormData     array (Formularfelder)
salesChannel        → SalesChannelEntity
```

### `contactFormData.*`

```
contactFormData
├── email           string
├── firstName       string
├── lastName        string
├── phone           string(?)
├── subject         string(?)
└── comment         string   ← via |nl2br ausgeben
```

---

## `revocation_request.customer` / `.merchant` — Widerrufsformular (6.7)

### Top-Level-Variablen

```
revocationRequestFormData   array
salesChannel                → SalesChannelEntity
```

### `revocationRequestFormData.*`

```
revocationRequestFormData
├── contractNumber  string(?)
├── firstName       string
├── lastName        string
├── email           string
├── comment         string(?)
└── submitTime      \DateTimeInterface  ← via |format_datetime ausgeben
```

---

## `review_form` — Produktbewertung

### Top-Level-Variablen

```
reviewFormData      array
product             → ProductEntity
salesChannel        → SalesChannelEntity
```

### `reviewFormData.*`

```
reviewFormData
├── id              string(?) (UUID)
├── name            string(?)
├── lastName        string(?)
├── email           string(?)
├── points          int   (1–5)
├── title           string
└── content         string  ← via |nl2br
```

### `product.*` (in review_form)

```
product
├── productNumber   string
├── name            string(?) (translated)
├── description     string(?) (translated)
└── cover           → ProductMediaEntity(?)
    └── media       → MediaEntity
        └── url     string
```

---

## Variables always available (every template)

```
eventName           string   ← technischer Event-Name
salesChannelId      string   ← UUID des Sales Channel
salesChannel        → SalesChannelEntity (inserted by MailService)
```

---

## Adding variables of your own

### Via MailBeforeValidateEvent (empfohlen)

```php
// src/EventSubscriber/MailDataSubscriber.php
public function onMailValidate(MailBeforeValidateEvent $event): void
{
    $data = $event->getTemplateData();

    // add a new variable
    $data['shopConfig'] = $this->systemConfig->get('MyPlugin.config.someValue');

    // data that depends on the order
    if (isset($data['order'])) {
        $order = $data['order'];
        $data['extraInfo'] = $this->myService->loadForOrder($order->getId());
    }

    $event->setTemplateData($data);
}
```

### Through the flow action "Set variables" (admin)

In the flow builder, the "Set variables" action (SetOrderCustomFieldsAction, or any action based
on ScalarValuesAware) fills keys of your own into `getValues()`, and those then become available as
top-level Twig variables.

### Through a MailTemplateType of your own, with `availableEntities`

```php
// In a migration:
$this->mailTemplateTypeRepo->upsert([[
    'technicalName' => 'my_custom_mail',
    'availableEntities' => [
        'order'       => 'order',
        'customer'    => 'customer',
        'salesChannel'=> 'sales_channel',
        'myEntity'    => 'my_entity',  // an entity definition of your own
    ],
]], $context);
```

`availableEntities` decides which variables the admin template editor suggests. It does not
prevent further variables being added through `MailBeforeValidateEvent`.
