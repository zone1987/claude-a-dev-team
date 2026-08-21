# Klarna Payments – integration & configuration

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/klarna

## Overview

**Klarna Payments** for Shopware 6 offers a simple shopping experience:
- Merchants receive the **full payment immediately**
- Customers choose their own payment date (instalments, invoice, direct payment)

---

## Payment options

| Option | Description |
|---|---|
| **Rechnung (Invoice)** | Buy now, pay within 14 days – free of charge for customers |
| **Ratenzahlung (Installments)** | Split the cost into monthly payments |
| **Sofortzahlung (Direct)** | Bank transfer, direct debit, credit card |

---

## Installation

### Variant 1: First-run setup wizard
- In the "Erweiterungen" (Extensions) wizard step, search for Klarna and install it

### Variant 2: Shopware Store
1. https://store.shopware.com → search for "Klarna"
2. Acquire a licence
3. In the admin: **Erweiterungen** (Extensions) **> Meine Erweiterungen** (My extensions) → install + activate

### Variant 3: Directly in the admin
1. **Erweiterungen** (Extensions) **> Store** in the admin
2. Search for "Klarna" → add/buy
3. Activation via the toggle in Meine Erweiterungen

**Prerequisite**: Being logged in to the Shopware Account (for licence verification).

---

## Configuration

For the complete setup the Shopware documentation refers to the official
Klarna documentation: https://klarna-shopware.426-upgrade.com/de/index.html

### Basic steps
1. Create a Klarna merchant account: https://portal.klarna.com
2. Enter the API credentials (API key + secret) in the Klarna configuration in the Shopware admin
3. Activate the payment methods (invoice, instalments, direct payment)
4. Assign the payment methods to the sales channels (Einstellungen (Settings) > Zahlungen (Payments))
5. Configure rules for availability (for example only for certain countries)

---

## Regional availability

Klarna Payments is available in the following countries (as of 2024):
- Germany, Austria, Switzerland
- Sweden, Norway, Finland, Denmark
- Netherlands, Belgium
- United Kingdom
- USA, Canada, Australia
- and further countries

---

## Notes on usage

- Klarna checks the customers' creditworthiness automatically in the background
- Unavailable payment methods are hidden automatically in the checkout
- Manage disputes and refunds via the Klarna portal
