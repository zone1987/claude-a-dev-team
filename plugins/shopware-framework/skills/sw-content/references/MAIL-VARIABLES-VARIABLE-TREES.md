# Shopware 6 — the complete variable tree per mail template

Derived from the real entity definitions plus the default Twig fixtures.  
As of Shopware 6.7 (trunk)

Legend: `(?)` = nullable, `[*]` = collection or array, `→` = association or sub-object

---

## Contents

- [`order_confirmation_mail` — order confirmation](#order_confirmation_mail-order-confirmation)
- [`order.state.*` — order state notifications](#orderstate-order-state-notifications)
- [`order_delivery.state.*` — delivery state notifications](#order_deliverystate-delivery-state-notifications)
- [`order_transaction.state.*` — payment state notifications](#order_transactionstate-payment-state-notifications)
- [`order.payment_method.changed` — payment method changed](#orderpayment_methodchanged-payment-method-changed)
- [`invoice_mail` / `delivery_mail` / `credit_note_mail` / `cancellation_mail` — document mails](#invoice_mail-delivery_mail-credit_note_mail-cancellation_mail-document-mails)
- [`downloads_delivery` — digital downloads](#downloads_delivery-digital-downloads)
- [`customer_register` — registration confirmation](#customer_register-registration-confirmation)
- [`customer_register.double_opt_in` — double opt-in registration](#customer_registerdouble_opt_in-double-opt-in-registration)
- [`guest_order.double_opt_in` — double opt-in guest order](#guest_orderdouble_opt_in-double-opt-in-guest-order)
- [`password_change` — password reset request](#password_change-password-reset-request)
- [`customer.password.changed` — password changed successfully (6.7)](#customerpasswordchanged-password-changed-successfully-67)
- [`customer.group.registration.accepted` / `.declined` — customer group registration](#customergroupregistrationaccepted-declined-customer-group-registration)
- [`newsletterRegister` / `newsletterDoubleOptIn` — Newsletter](#newsletterregister-newsletterdoubleoptin-newsletter)
- [`contact_form` — contact form](#contact_form-contact-form)
- [`revocation_request.customer` / `.merchant` — revocation form (6.7)](#revocation_requestcustomer-merchant-revocation-form-67)
- [`review_form` — product review](#review_form-product-review)
- [Variables always available (every template)](#variables-always-available-every-template)
- [Adding variables of your own](#adding-variables-of-your-own)

## `order_confirmation_mail` — order confirmation

The same structure applies to `order_transaction.state.open`, which adds a payment note in its intro.

### Top-level variables

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
├── deepLinkCode                  string  ← customer login link
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
│   ├── isoCode                   string  (e.g. "EUR")
│   ├── symbol                    string  (e.g. "€")
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
│       ├── letterName            string(?) (translated, e.g. "Dear Mr")
│       └── displayName           string(?) (translated, e.g. "Mr")
│
├── stateMachineState             → StateMachineStateEntity
│   ├── technicalName             string  ("open"|"in_progress"|"completed"|"cancelled")
│   └── name                      string(?) (translated, e.g. "Open")
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
│   └── (each entry = OrderAddressEntity, the same fields as billingAddress above)
│
├── deliveries                    [*] → OrderDeliveryCollection
│   └── (each entry = OrderDeliveryEntity, see below)
│
├── deliveries.first              → OrderDeliveryEntity (convenience accessor)
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
│   └── shippingOrderAddress      → OrderAddressEntity (shipping address)
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
├── nestedLineItems               [*] → OrderLineItemCollection (nested)
│   └── (each entry = OrderLineItemEntity, see below)
│
├── lineItems                     [*] → OrderLineItemCollection (flat)
│   └── (each entry = OrderLineItemEntity, see below)
│
└── documents                     [*] → DocumentCollection
    └── (each entry = DocumentEntity)
```

### `order.nestedLineItems[*]` — the line item tree

```
lineItem (each in order.nestedLineItems)
├── label                         string   ← product name at the time of the order
├── quantity                      int
├── unitPrice                     float
├── totalPrice                    float
├── description                   string(?)
├── type                          string(?)  ("product"|"promotion"|"credit"|"custom")
├── position                      int
├── good                          bool
├── referencedId                  string(?)  (product UUID)
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
│   ├── options                   [*] → array (variant options)
│   │   └── {group: string, option: string}
│   └── features                  [*] → array (product features)
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
├── children                      [*] → OrderLineItemCollection (recursive)
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
│       └── url                   string   ← e.g. "https://shop.example.com"
├── currency                      → CurrencyEntity
├── language                      → LanguageEntity
├── country                       → CountryEntity
├── paymentMethod                 → PaymentMethodEntity  (default)
├── shippingMethod                → ShippingMethodEntity (default)
└── mailHeaderFooter              → MailHeaderFooterEntity(?)
```

### `a11yDocuments[*]` — accessible documents

```
a11yDocuments (array)
└── each entry
    ├── documentId               string (UUID)
    ├── deepLinkCode             string
    └── fileExtension            string
```

---

## `order.state.*` — order state notifications

Applies to: `order.state.open`, `order.state.in_progress`, `order.state.completed`, `order.state.cancelled`

### Top-level variables

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
a11yDocuments       [*] (optional)
eventName           string
salesChannelId      string
```

### Paths used

```
order
├── orderNumber                   string
├── orderDateTime                 \DateTimeInterface
├── deepLinkCode                  string
├── stateMachineState             → StateMachineStateEntity
│   └── name                      string (translated)  ← e.g. "Done"
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

## `order_delivery.state.*` — delivery state notifications

Applies to: `shipped`, `shipped_partially`, `returned`, `returned_partially`, `cancelled`

### Top-level variables

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
a11yDocuments       [*] (optional)
```

### Paths used

```
order
├── orderNumber                   string
├── orderDateTime                 \DateTimeInterface
├── deepLinkCode                  string
├── deliveries.first              → OrderDeliveryEntity
│   └── stateMachineState         → StateMachineStateEntity
│       └── name                  string (translated)  ← e.g. "Shipped"
└── orderCustomer                 → OrderCustomerEntity
    ├── firstName, lastName, salutation.letterName

salesChannel.name / salesChannel.domains|first.url
a11yDocuments[].documentId / .deepLinkCode / .fileExtension
```

**Tip — printing the tracking URL:**
```twig
{% set delivery = order.deliveries.first %}
{% for code in delivery.trackingCodes %}
  <a href="{{ delivery.shippingMethod.trackingUrl|replace({'%s': code}) }}">{{ code }}</a>
{% endfor %}
```

---

## `order_transaction.state.*` — payment state notifications

Applies to all but `order_transaction.state.open`, which carries the full order detail.

### Top-level variables

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
a11yDocuments       [*] (optional)
```

### Paths used

```
order
├── orderNumber                   string
├── orderDateTime                 \DateTimeInterface
├── deepLinkCode                  string
├── transactions.first            → OrderTransactionEntity
│   └── stateMachineState         → StateMachineStateEntity
│       └── name                  string (translated)  ← e.g. "Paid"
└── orderCustomer → firstName, lastName, salutation.letterName
```

---

## `order.payment_method.changed` — payment method changed

### Top-level variables

```
order               → OrderEntity
orderTransaction    → OrderTransactionEntity
customer            → CustomerEntity
salesChannel        → SalesChannelEntity
```

### Paths used

```
order
├── orderNumber                   string
└── orderCustomer → firstName, lastName, salutation(?)

order.transactions.last           → OrderTransactionEntity  ← NOTE: .last, not .first
└── paymentMethod
    └── name                      string (translated)
```

---

## `invoice_mail` / `delivery_mail` / `credit_note_mail` / `cancellation_mail` — document mails

### Top-level variables

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
a11yDocuments       [*] (optional)
```

### Paths used

```
order
├── orderNumber                   string
└── orderCustomer → firstName, lastName, salutation.letterName

salesChannel.domains|first.url

a11yDocuments[].documentId / .deepLinkCode / .fileExtension
```

---

## `downloads_delivery` — digital downloads

### Top-level variables

```
order               → OrderEntity
salesChannel        → SalesChannelEntity
```

### Paths used

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

### Top-level variables

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
├── defaultShippingAddress        → CustomerAddressEntity (the same fields)
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

## `customer_register.double_opt_in` — double opt-in registration

### Top-level variables

```
customer            → CustomerEntity  (the same fields as above)
confirmUrl          string            ← the confirmation link
salesChannel        → SalesChannelEntity
```

---

## `guest_order.double_opt_in` — double opt-in guest order

### Top-level variables

```
customer            → CustomerEntity
confirmUrl          string            ← the confirmation link
salesChannel        → SalesChannelEntity
```

### Paths used

```
customer.salutation.translated.displayName
customer.lastName
confirmUrl   (a plain Twig variable)
```

---

## `password_change` — password reset request

### Top-level variables

```
customer            → CustomerEntity
resetUrl            string            ← reset link
salesChannel        → SalesChannelEntity
shopName            string
```

### Paths used

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

### Top-level variables

```
customer            → CustomerEntity
shopName            string
salesChannel        → SalesChannelEntity
```

### Paths used

```
customer.firstName
customer.lastName
shopName
```

---

## `customer.group.registration.accepted` / `.declined` — customer group registration

### Top-level variables

```
customer            → CustomerEntity
customerGroup       → CustomerGroupEntity
salesChannel        → SalesChannelEntity
```

### Paths used

```
customer.salutation.translated.letterName
customer.lastName
customerGroup.translated.name
```

---

## `newsletterRegister` / `newsletterDoubleOptIn` — Newsletter

### Top-level variables

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

## `contact_form` — contact form

### Top-level variables

```
contactFormData     array (form fields)
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
└── comment         string   ← print through |nl2br
```

---

## `revocation_request.customer` / `.merchant` — revocation form (6.7)

### Top-level variables

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
└── submitTime      \DateTimeInterface  ← print through |format_datetime
```

---

## `review_form` — product review

### Top-level variables

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
eventName           string   ← the technical event name
salesChannelId      string   ← the UUID of the sales channel
salesChannel        → SalesChannelEntity (inserted by MailService)
```

---

## Adding variables of your own

### Through MailBeforeValidateEvent (recommended)

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
