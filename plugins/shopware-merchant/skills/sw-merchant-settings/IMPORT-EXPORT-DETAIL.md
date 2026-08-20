# Shopware 6 – Import / Export – complete reference

Source: https://docs.shopware.com/de/shopware6-de/einstellungen/importexport

---

## Overview

**Path:** Einstellungen (Settings) > Automatisierung (Automation) > Import/Export

Allows shop content to be managed via CSV files.

---

## CSV requirements

| Requirement | Value |
|---|---|
| Character encoding | UTF-8 |
| Field separator | Semicolon (`;`) |
| Text delimiter | Quotation marks (`"`) |
| Decimal separator for prices | Full stop (5.00, not 5,00) |

---

## Import

- Upload a CSV file → add or update records
- Validation on faulty entries → error report (download option)
- **Test mode:** validation without commit (no changes to the database)
- The error CSV contains only the faulty records with error descriptions

---

## Export

- Export existing data as CSV
- Export history: last 30 days
- For external use or third-party integrations

### AI Copilot export (from plan Rise)
- Natural-language queries for specific data sets
- Example: "Export all products without a description"

---

## Supported object types & mandatory fields

| Object type | Mandatory fields |
|---|---|
| Produkte (Products) | id, taxId, productNumber, stock, name |
| Kunden (Customers) | id, defaultBillingAddressId, defaultShippingAddressId, customerNumber, firstName, lastName, email |
| Kategorien (Categories) | id, type, name |
| Bestellungen (Orders) | id, salesChannelId, orderDateTime, stateId |
| Medien (Media) | — |
| Newsletter recipients | — |
| Eigenschaften (Properties) | — |
| Advanced prices | — |
| Variant configurations | — |
| Cross-selling | — |

---

## Extended identifier

**Second unique identifier:** allows records to be matched via alternative identifiers instead of UUIDs.

Example: identify a product via `productNumber` instead of a UUID.

---

## Custom profiles

Create your own import/export configurations:
- Map database fields to CSV columns
- Define optional default values
- Determine the position order

---

## Import workflows (step by step)

### Importing products
1. Select a profile (default: "Produkte")
2. Select the CSV file
3. Optional: activate test mode
4. Start the import
5. Check the error report (if any)

### Importing variants
Requires existing parent products; define the product number pattern for variants.

### Further workflows
- Importing newsletter recipients
- Importing properties
- Importing advanced prices
- Importing categories and media
