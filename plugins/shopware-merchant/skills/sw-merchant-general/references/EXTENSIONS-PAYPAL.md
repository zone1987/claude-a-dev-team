# PayPal – integration & configuration

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/paypal

## Contents

- [Overview](#overview)
- [Installation & activation](#installation-activation)
- [Onboarding (linking the account)](#onboarding-linking-the-account)
- [Supported payment methods](#supported-payment-methods)
- [Configuration areas](#configuration-areas)
- [Data protection & data transfer](#data-protection-data-transfer)
- [Storefront configuration](#storefront-configuration)
- [Troubleshooting](#troubleshooting)

## Overview

The **PayPal extension** is an all-in-one payment solution for Shopware 6 and, besides
classic PayPal, also supports credit card, direct debit and many local payment methods.
Merchants receive the **full payment immediately** – customers choose their own payment date.

**Special feature**: PayPal is pre-installed in Shopware (only the activation is needed).

---

## Installation & activation

### Variant 1: During the first-run setup wizard
- In the PayPal wizard step: enter the API credentials

### Variant 2: Manually
1. Open **Erweiterungen** (Extensions) **> Meine Erweiterungen** (My extensions)
2. Find the PayPal entry → **Aktivieren** (Activate)
3. Alternatively: Erweiterungen > Store → search for "PayPal" → Hinzufügen (Add)

**Prerequisite**: Being logged in to the Shopware Account.

---

## Onboarding (linking the account)

1. **Erweiterungen > Meine Erweiterungen > PayPal > Konfigurieren** (Configure)
2. **Onboarding** section
3. Click **Mit PayPal verbinden** (Connect with PayPal) → you are redirected to PayPal
4. Log in to the PayPal merchant account → grant the permissions
5. Automatic credential generation (no manual API key entry needed)

> **Sandbox vs. live**: For tests activate the sandbox mode first.

---

## Supported payment methods

| Method | Description |
|---|---|
| PayPal (wallet) | Payment from the PayPal account |
| Credit card | Mastercard, Visa, Amex (without a PayPal account) |
| Direct debit (SEPA) | Direct bank debit |
| PayPal instalments | Split the cost into monthly instalments |
| PayPal invoice purchase | Purchase on invoice (up to 14 days) |
| Pay Later | "Buy now, pay later" |
| Local payment methods | Depending on the country setting |

---

## Configuration areas

### Onboarding
- Link the PayPal merchant account
- Switch between sandbox/live mode
- API credentials (automatic or manual)

### Shipping Tracking (from version 5.3.0)
- Carrier integration: transmit shipment tracking directly to PayPal
- Reduces buyer protection disputes

### Vaulting (from version 8.0.0)
- Recurring payments (subscriptions)
- Customers can save payment methods

### Invoice Purchase
- Purchase on invoice with automatic payment instructions in the order confirmation email
- Buy Now Pay Later (BNPL)

### Smart Payment Buttons
- Customisable checkout buttons (colour, shape, size)
- Show alternative payment methods directly in the button area
- Placement: product page, cart, checkout

### Express Checkout
- The PayPal button directly on the product detail page
- Customers can buy immediately without a Shopware account

### Conflict Management
- Monitor PayPal disputes directly in the Shopware admin
- Track the transaction status and escalations

---

## Data protection & data transfer

Shopware transmits **exclusively aggregated daily data** (total transaction volume) to Shopware:
- No personal data
- No order numbers
- No individual transactions

---

## Storefront configuration

| Element | Configurable |
|---|---|
| Express Checkout button | Position, visibility |
| Pay Later banner | Placement on product pages, cart |
| Button styling | Colour (gold, blue, silver, black), shape (rectangle, pill) |
| Payment instructions | Email template for the invoice purchase |

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Webhooks not active | Check the PayPal dashboard > Webhooks; or repeat the onboarding |
| Update error | Clear the cache (`php bin/console cache:clear`), then update again |
| Sandbox payments are not processed | Make sure the sandbox mode is active and the sandbox credentials are correct |
| Express Checkout does not appear | Check the button configuration in the PayPal settings |
