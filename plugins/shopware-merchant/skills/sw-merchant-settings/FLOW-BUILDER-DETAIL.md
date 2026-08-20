# Shopware 6 – Flow Builder (complete reference)

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/Flow-Builder

---

## Contents

- [Überblick](#überblick)
- [Konfigurationsbereich "Allgemein"](#konfigurationsbereich-allgemein)
- [Hauptkomponenten](#hauptkomponenten)
- [Custom Trigger (ab v6.5.3.0)](#custom-trigger-ab-v6530)
- [Flows teilen & verwalten](#flows-teilen-verwalten)
- [Verfügbarkeit nach Plan](#verfügbarkeit-nach-plan)
- [Wichtige Hinweise](#wichtige-hinweise)
- [Lernressourcen](#lernressourcen)

## Überblick (Overview)

**Path:** Einstellungen (Settings) > Automatisierung (Automation) > Flow Builder

Enables event-based automation of business processes without programming knowledge.

---

## Configuration area "Allgemein" (General)

| Feld (Field) | Funktion (Function) |
|---|---|
| Name | Identification in the overview |
| Beschreibung (Description) | Meaningful explanation |
| Priorität (Priority) | Execution order for identical triggers (higher = earlier) |
| Aktiv (Active) | Temporary enabling/disabling |

---

## Main components

### 1. Trigger

More than 80 available events, categorised:

**Customer events:**
| Event | Zeitpunkt (Point in time) |
|---|---|
| `checkout.customer.before.login` | Before login |
| `checkout.customer.login` | On login |
| `checkout.customer.register` | New registration |
| `checkout.customer.deleted` | Customer deletion |

**Order events:**
| Event | Zeitpunkt |
|---|---|
| `checkout.order.placed` | Order placed |
| `state_enter.order.state.*` | Status changes (open, in progress, completed, cancelled) |

**Payment events:**
| Event | Zeitpunkt |
|---|---|
| `state_enter.order_transaction.state.paid` | Payment received |
| `state_enter.order_transaction.state.refunded` | Refund |
| `checkout.order.payment_method.changed` | Payment method changed → sets status automatically to "Offen" (Open) |

**Delivery events:**
| Event | Zeitpunkt |
|---|---|
| `state_enter.order_delivery.state.shipped` | Shipped |
| `state_enter.order_delivery.state.returned` | Returned |

**Marketing events:**
| Event | Zeitpunkt |
|---|---|
| `newsletter.register` | Newsletter sign-up |
| `newsletter.confirm` | Newsletter confirmation |
| `review_form.send` | Product review submitted |

**Mail events:**
| Event | Zeitpunkt |
|---|---|
| `mail.before.send` | Before mail is sent |
| `mail.sent` | Mail sent |

**Others:**
| Event | Zeitpunkt |
|---|---|
| `contact_form.send` | Contact form submitted |
| `customer.recovery.request` | Password recovery requested |

---

### 2. Bedingungen (Conditions)

- Based on the Rule Builder
- Two outputs: **Wahr** (True) or **Falsch** (False)
- Several conditions can be combined sequentially
- Determine which action is executed

---

### 3. Verzögerung (Delay) (from plan Shopware Beyond)

**Available time units:**
- Hour, day, week, month
- Custom: format `SS.TT.WW.MM`
- 
**Scheduled actions:**
Overview of all delayed actions with:
- Order number, customer info
- Remaining time, scheduled execution time

---

### 4. Aktionen (Actions)

#### Send mail
| Feld | Optionen (Options) |
|---|---|
| Empfänger (Recipient) | Administrator (all admin users!), customer, specific mail address |
| Absender (Sender) | Configurable |
| Template | Selection from the mail templates |
| Anhänge (Attachments) | Documents can optionally be added |

> **Caution:** "Administrator" sends to **ALL** admin users including external ones (agencies, service providers).

#### Assign status
- Change payment status, delivery status, order status
- **Mind the dependencies:** some statuses require a preceding status (e.g. "Erstattet" (Refunded) only after "Bezahlt" (Paid))

#### Generate documents
- Select the document type in the dropdown
- The new document is added to the order

#### Add / remove tag
- Only for tag-capable entities
- Flexible tag management

#### Assign customer group
- Change the customer group via dropdown

#### Assign account status
- Set the customer to active or inactive

#### Assign custom field
| Feld | Beschreibung |
|---|---|
| Entität (Entity) | Customer or order |
| Zusatzfeld-Set (Custom field set) | Select the set |
| Specific field | Configure the field |

#### Assign affiliate and campaign code
- Entity (customer/order) + code + overwrite option

#### Set download permission
- For digital products: unlock or block the download link

#### Stop flow
- Stops the entire flow
- Prevents subsequent actions
- Useful after "Falsch" conditions

#### Call URL / webhook (from plan Evolve)
**HTTP methods:** GET, POST, PUT, PATCH, DELETE

| Feld | Beschreibung |
|---|---|
| URL | Target address |
| Parameter | Key-value pairs from the shop system |
| URL-Vorschau (URL preview) | Shows the final URL with parameters |
| Header-Parameter | Special server headers |
| Body | JSON/code format (Shopware variables available) |
| Basic Auth | Authentication data |

---

## Custom Trigger (from v6.5.3.0)

Three flow types are possible:
1. Internal Shopware flows
2. Shopware events → webhooks in third-party systems
3. Third-party system events → Shopware flows

---

## Sharing & managing flows

### Download
Context menu → **Herunterladen** (Download) → JSON export

> **Note:** references to categories, products and properties have to be reassigned on upload.

### Upload
Einstellungen > Flow Builder → **Flow hochladen** (Upload flow) → choose file

### Flow templates
Templates provided by Shopware for standard flows.

---

## Availability by plan

| Feature | Plan |
|---|---|
| Basic actions | Standard |
| Flow sharing | Shopware Rise (from v6.4.19.0) |
| Time-delayed actions | Shopware Beyond |
| Webhook actions (Call URL) | Shopware Evolve |

---

## Important notes

- `checkout.order.payment_method.changed` sets the payment status automatically to "Offen" — setting it manually is not necessary
- Some actions (tags) only work with compatible entities

---

## Learning resources

- Learning path: https://hub.shopware.com/learn/unit/user-flow-builder
