# Shopware 6 – Steuern (Taxes) – complete reference

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/steuern

---

## Overview

**Path:** Einstellungen (Settings) > Regional > Steuern

A green check mark identifies the current default tax rate.

---

## Creating a tax rate

| Field | Description |
|---|---|
| Name | Label of the tax rate |
| Prozentwert (Percentage value) | Tax percentage (e.g. 19) |
| Als Standard verwenden (Use as default) | Default for new products |

---

## Editing a tax rate

> **Warning:** Changing a tax rate that is already in use can lead to differing calculations on existing invoices and items.

---

## Country-specific tax rules

Within a tax rate, differentiated rules can be set up for the following units:
- Individual postcodes
- Postcode ranges
- Federal states
- Entire countries

### Field "Aktiv ab" (Active from)
If a date is entered, the tax rate only applies in the storefront from that date onwards.
> **Note:** Prices in the product are **not** recalculated automatically when a tax rate changes.

---

## EU OSS (One-Stop-Shop)

From 1 July 2021 a threshold of **EUR 10,000** applies to intra-community B2C sales.
- Those exceeding it must register in the online OSS portal
- Shopware supports the necessary tax rules per country

---

## Tax providers (external services)

For complex tax systems (e.g. USA) external tax service providers can be integrated:
- Activate the service
- Adjust the Priorität (Priority)
- Configure availability conditions

---

## Integration with customer groups

In the Kundengruppen (Customer groups) settings you can configure individually for each group whether prices are displayed and calculated **gross** or **net**.
