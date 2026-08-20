# Shopware 6 – Email templates & mailer – complete reference

Sources:
- https://docs.shopware.com/de/shopware-6-de/einstellungen/e-mail-templates
- https://docs.shopware.com/de/shopware-6-de/einstellungen/mailer

---

## Contents

- [Email templates](#email-templates)
- [Variable system](#variable-system)
- [Practical examples](#practical-examples)
- [Mailer configuration](#mailer-configuration)

## Email templates

**Path:** Einstellungen (Settings) > Inhalte (Content) > E-Mail-Templates

Templates for automatically sent emails (registration, order confirmation etc.) as well as central header/footer.  
Assignment happens via the **Flow Builder**.

---

### Editor structure

| Area | Description |
|---|---|
| **1. Sprache** (Language) | Language selection (only activated languages) |
| **2. Informationen** (Information) | Type (predefined function), description |
| **3. Optionen** (Options) | Subject, sender name |
| **4. Anhänge** (Attachments) | File uploads (separately per language) |
| **5. Mail-Text** | HTML version + plain-text version |
| **6. Tools (right)** | Paper plane: test email; `</>`: variable library; eye: preview; image: media library |

---

### Predefined templates (selection)

| Template | Purpose |
|---|---|
| Bestellbestätigung (Order confirmation) | Confirmation when an order is received |
| Kunden-Registrierung (Customer registration) | Welcome email after registration |
| Passwort Änderungsanfrage (Password change request) | Recovery link for resetting |
| Newsletter Double Opt-In | Confirmation email for the newsletter |
| Eintritt Lieferstatus: Versandt (Delivery status reached: Shipped) | Notification when shipped |
| Eintritt Zahlungsstatus: Bezahlt (Payment status reached: Paid) | Payment confirmation |
| Versand digitaler Produkte (Delivery of digital products) | Download link for digital items |
| Kontaktformular (Contact form) | Notification for the shop operator |

---

### Header & footer

**1. Informationen:**
- Name, description, sales channel assignment

**3. Mail-Header:**
```html
<img src="https://meinshop.de/media/logo.png" alt="Logo" />
```

**4. Mail-Footer:**
HTML and plain text for closing formulas, legal notices etc.

---

## Variable system

### Syntax
```twig
{{array.subelement.variable}}
```

Example: `{{order.orderCustomer.firstName}}`

Auto-completion: type `{{` → the available arrays appear.

---

### Array: customer
Available in: customer registration, double opt-in, password recovery

| Variable | Meaning |
|---|---|
| `customerNumber` | Customer number |
| `firstName` / `lastName` | First and last name |
| `email` | Email address |
| `company` | Company name |
| `birthday` | Date of birth |
| `defaultPaymentMethod` | Default payment method |
| `defaultBillingAddress` | Billing address (street, zipcode, city, country, …) |
| `defaultShippingAddress` | Shipping address |
| `salutation.displayName` | Salutation |
| `salutation.letterName` | Formal letter salutation |

---

### Array: customerRecovery
Available in: Passwort Änderungsanfrage

| Variable | Sub-elements |
|---|---|
| `customer` | firstName, lastName, email, company, title |

---

### Array: userRecovery
Available in: Benutzer Passwort Wiederherstellung (User password recovery) (admin accounts)

| Variable | Sub-elements |
|---|---|
| `user` | firstName, lastName, email, username, aclRoles |

---

### Array: newsletterRecipient
Available in: newsletter registration, double opt-in

| Variable | Meaning |
|---|---|
| `firstName` / `lastName` | Names |
| `email` | Newsletter email |
| `city` / `zipCode` / `street` | Address data |

---

### Array: contactFormData
Available in: Kontaktformular

| Variable | Meaning |
|---|---|
| `firstName` / `lastName` | Sender data |
| `email` | Contact email |
| `phone` | Phone number |
| `subject` / `comment` | Message content |

---

### Array: order
Available in: order and delivery related emails

| Variable | Sub-elements | Purpose |
|---|---|---|
| `orderNumber` | — | Order number |
| `orderDateTime` | — | Timestamp |
| `price` | netPrice, totalPrice, taxStatus | Price details |
| `shippingTotal` | — | Shipping costs |
| `orderCustomer` | (see customer) | Buyer data |
| `currency` | isoCode, symbol, shortName | Currency information |
| `addresses[0]` | firstName, lastName, street, zipcode, city, country, vatID, … | Addresses |
| `deliveries[0]` | shippingOrderAddress, shippingMethod, trackingCodes | Shipping details |
| `transactions.first` | paymentMethod, stateMachineState | Payment information |
| `lineItems[0]` | quantity, unitPrice, totalPrice, label, payload.productNumber | Order line items |
| `stateMachineState` | name | Current order status |

---

### Array: salesChannel
Available in: all default templates

| Variable | Sub-elements | Purpose |
|---|---|---|
| `name` | — | Sales channel name |
| `domains.0` | url | Domain URL |

---

## Practical examples

### Payment-method-specific content
```twig
{% for transactions in order.transactions %}
{% if transactions.paymentMethodId == "ID-aus-der-URL" %}
  Bitte überweise {{ order.price.totalPrice }} EUR
  auf IBAN: DEXX XX
  Referenz: {{ order.orderNumber }}
{% endif %}
{% endfor %}
```

> The payment method ID can be found in the URL while editing the payment method.

### Using a custom field
```twig
{{customer.customFields.FeldName}}
```

---

## Mailer configuration

**Path:** Einstellungen > System > Mailer  
**Self-hosted only** (not for SaaS)

---

### 1. Local email agent (sendmail)
| Option | Description |
|---|---|
| Versandmodus (Dispatch mode) | Synchronous (-bs) or asynchronous (-t) — synchronous recommended |
| Versand deaktivieren (Disable dispatch) | Disable email dispatch completely |

---

### 2. SMTP server (basic auth)
| Field | Description |
|---|---|
| Host | SMTP server address |
| Port | Default 25; AOL/Gmail: 587 |
| Benutzername / Passwort (Username / Password) | Login data (often the email address) |
| Verschlüsselung (Encryption) | SSL, TLS or unencrypted |
| Absender-Adresse (Sender address) | Fallback address |
| Empfänger-Adresse (Recipient address) | Test address (receives a copy of all emails) |
| Versand deaktivieren | Global switch |

---

### 3. SMTP server with OAuth 2 (e.g. Office 365)
| Field | Description |
|---|---|
| OAuth URL | Token retrieval URL |
| OAuth Scope | Scope definition |
| Client ID | Application ID |
| Client Secret | Authentication token |

---

### Provider connection data

| Provider | Server | Port | Encryption |
|---|---|---|---|
| 1und1/IONOS | smtp.ionos.de | 465 | SSL |
| Google Mail | smtp.gmail.com | 465 | SSL |
| HostEurope | variable | 25/587/465 | variable |
| Timme Hosting | — | 465 or 587 | SSL/TLS |

---

### Configuration via .env
```env
MAILER_DSN=smtp://Benutzername:Password@mailserveradresse:port
```

Complete documentation: https://symfony.com/doc/current/mailer.html
