# Internationalisation

**Source**: https://docs.shopware.com/de/shopware-6-de/erste-schritte/internationalisierung

## Overview

Shopware 6 supports international selling via multilingualism, multi-currency
and country-specific payment and shipping options. This article describes the
structured approach for the international setup.

---

## Preliminary considerations before the setup

The following questions should be clarified before the implementation:

| Question | Relevance |
|---|---|
| Which payment methods are preferred abroad? | Configure payment methods per country |
| Which tax rules apply? | Set up country-specific tax rates |
| Are several currencies needed? | Create currencies and configure exchange rates |
| Are translations available? | Translate product texts, email templates, category names |
| Which shipping options exist internationally? | Define shipping methods + delivery countries |

---

## Implementation steps (recommended order)

### Step 1: set up the language
- Path: **Einstellungen** (Settings) **> Sprachen** (Languages)
- Add a new language (via the Sprachpaket extension)
- Default: German and English are already available
- Further languages: install the Sprachpaket → `../../../sw-merchant-extensions/references/deep/sprachpaket.md`

### Step 2: activate countries
- Path: **Einstellungen > Länder & Gebiete** (Countries & regions)
- Activate the desired countries for customer registration (tick)
- Without activation, customers from that country cannot register

### Step 3: configure currencies
- Path: **Einstellungen > Währungen** (Currencies)
- Create a new currency (e.g. GBP, USD, CHF)
- Enter exchange rates manually or fetch them automatically (via an extension)
- Rounding rules are configurable per currency

### Step 4: set up tax rates
- Path: **Einstellungen > Steuern** (Taxes)
- Create country-specific tax rates
- Example: DE 19%, AT 20%, FR 20%, UK 0% (after Brexit)
- Tax rules can be tied to customer groups and countries

### Step 5: configure payment methods
- Path: **Einstellungen > Zahlungen** (Payments)
- Per payment method: restrict availability by country (Rule Builder)
- Example: SEPA only for SEPA countries, local payment methods for specific markets

### Step 6: define shipping methods
- Path: **Einstellungen > Versand** (Shipping)
- Shipping rules (Rule Builder): which shipping methods to which countries?
- Configure international shipping costs separately

### Step 7: set up sales channels
- Option A: **one sales channel with multilingualism** (language selection in the storefront)
- Option B: **separate sales channels per country** (own domain, own configuration)
- For option B: separate domains per country are recommended (e.g. `shop.de`, `shop.co.uk`)

---

## Managing translations

Shopware uses an **inheritance model** for translations:
- Fields without a translation **inherit** from the default language
- Translations have to be maintained in the respective language view

Translatable areas:

| Area | Path |
|---|---|
| Product descriptions | Katalog > Produkte > [product] > select language |
| E-Mail-Templates | Einstellungen > E-Mail-Templates |
| Category names | Katalog > Kategorien > [category] > select language |
| Erlebniswelten (Shopping Experiences, CMS) | Content > Erlebniswelten |
| Eigenschaften (Properties) & options | Katalog > Eigenschaften |

---

## Test phase before go-live

- Check all translations for completeness
- Test payment and shipping rules for each target region (test order)
- Verify the tax calculation in the checkout
- Check the currency display in the storefront

---

## Shopware Cloud vs. self-hosted

With **Shopware Cloud** some settings (e.g. domain management) have to be configured via the
cloud dashboard; the admin interface remains the same.
