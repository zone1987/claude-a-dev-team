# Shopware 6 – Abonnements (Subscriptions) – complete reference

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/abonnements

---

## Contents

- [Overview](#overview)
- [Configuration: three tabs](#configuration-three-tabs)
- [Storefront presentation](#storefront-presentation)
- [Management](#management)
- [Admin view (mixed orders)](#admin-view-mixed-orders)
- [Integration](#integration)

## Overview

**Path:** Einstellungen (Settings) > Handel (Commerce) > Abonnements  
**Available from:** 6.5.4.0  
**Plan:** Commercial — Shopware Beyond

Enables recurring orders with configurable intervals.

---

## Configuration: three tabs

### Tab 1: Pläne (Plans)

**General settings:**
| Field | Description |
|---|---|
| Name | Name of the subscription |
| Aktiv (Active) | Activation switch |
| Abweichender Storefront-Name (Different storefront name) | Optionally show a different name to customers |
| Beschreibung (Description) | Explanatory text |
| Verfügbarkeitsregeln (Availability rules) | Rule Builder integration |

**Interval configuration:**
| Field | Description |
|---|---|
| Intervalle (Intervals) | Selection of the available intervals |
| Mindestlaufzeit (Minimum term) | Minimum subscription period (e.g. 24 months) |
| Rabatt (Discount) | Percentage discount for the subscription period |

**Product assignment:** select products via checkbox (product name + product number).

---

### Tab 2: Intervalle (Intervals)

**Basic settings per interval:**
| Field | Description |
|---|---|
| Name | Label of the interval |
| Aktiv | Switch on/off |
| Verfügbarkeitsregeln | Rule Builder integration |
| Frequenz (Frequency) | e.g. weekly, fortnightly |
| Zeitintervall (Time interval) | Days, weeks, months |
| Vorschau (Preview) | Future delivery dates |

**Advanced settings:**
- Regular frequency with detailed options
- Weekday selection
- Days in the month
- Months in the year

---

### Tab 3: Einstellungen (Settings) (from v6.7.4.0)

| Option | Description |
|---|---|
| Gemischte Warenkörbe (Mixed carts) | Combine one-off products and subscriptions in one order |

---

## Storefront presentation

- A subscription button appears next to the add-to-cart button
- With several plans: selection via radio button
- The button changes to "Jetzt abonnieren" (Subscribe now) when a plan is selected

---

## Management

### In the admin (Bestellungen (Orders) > Abonnements)
- View subscription details
- Change the status: Aktiv, Pausiert (Paused), Gekündigt (Cancelled)

### In the customer account
- Pause for one cycle
- Cancel the subscription

**Status logic when cancelling before the minimum term:**
The admin shows "zur Kündigung vorgemerkt" (marked for cancellation) — further orders continue to be generated until the minimum term is fulfilled.

---

## Admin view (mixed orders)

- All line items visible
- Subscription items carry a subscription number
- One-off products without a number
- Discounts assigned automatically

---

## Integration

| System | Support |
|---|---|
| Rule Builder | Exclusion of payment methods, availability |
| Flow Builder | Reminder emails with delay function |
| Zahlungsarten (Payment methods) | Vorkasse (Prepayment), Rechnung (Invoice); with PayPal Vaulting also PayPal and credit card |
