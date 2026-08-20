# Ersteinrichtungs-Assistent (First-Run Wizard)

**Source**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/ersteinrichtungs-assistent

## Overview

The Ersteinrichtungs-Assistent (First-Run Wizard) starts **automatically after the first installation**
of Shopware 6. It guides you through the basic shop configuration in several steps.

The wizard can be opened again at any time:
> **Einstellungen** (Settings) **> System > Ersteinrichtungs-Assistent**

---

## Steps of the wizard

### 1. Data import (demo data)
- **Option A: load demo data** – import products, categories and manufacturers for testing
- **Option B: skip** – start with an empty shop

> Recommendation: load demo data for initial tests; remove it again before going live.

---

### 2. Default values
- Configuration: which sales channels are **linked automatically to newly created products**?
- Makes inventory management across multiple storefronts easier

---

### 3. Mailer settings
- SMTP configuration for outgoing emails (order confirmations, password reset etc.)
- **Can be configured later** (skipping is possible)
- Path for configuring it later: Einstellungen > System > Mailer

---

### 4. PayPal integration
- Enter the PayPal API credentials
- Optional: set PayPal as the default payment method for all sales channels
- Can also be configured later under **Erweiterungen** (Extensions) **> Meine Erweiterungen** (My extensions) **> PayPal**

---

### 5. Extensions
- Browse recommended extensions by region and category
- Direct installation from within the wizard is possible
- Prerequisite: a Shopware Account must be linked (step 6)

---

### 6. Linking the Shopware Account
- Connect the account with the shop instance
- Enables access to purchased extensions and licences
- **Domain verification** is required for shop operation

---

### 7. Shopware Store connection
- Enable direct access to Shopware Store extensions and services from within the admin
- Prerequisite for the Store area to be displayed in the admin

---

## After the wizard: recommended first steps

1. **Check the basic settings**: Einstellungen > Grundeinstellungen (Basic settings) (shop name, address, contact)
2. **Configure a sales channel**: Verkaufskanäle (Sales channels) > Storefront
3. **Create the first category**: Katalog (Catalogue) > Kategorien (Categories)
4. **Create the first product**: Katalog > Produkte (Products) > Produkt anlegen (Create product)
5. **Activate payment methods**: Einstellungen > Zahlungen (Payments)
6. **Set up shipping methods**: Einstellungen > Versand (Shipping)
7. **Configure tax rules**: Einstellungen > Steuern (Taxes)

---

## Tips

- The wizard is **idempotent** – running it again does not overwrite existing data
- Steps can be skipped individually and completed later
- After the wizard: the dashboard shows the first statistics
