# Shopware 6 – Versandarten (Shipping methods) – complete reference

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/versand

---

## Overview

**Path:** Einstellungen (Settings) > Handel (Commerce) > Versand (Shipping)

Table with name, description, active status and position.

---

## Creating a shipping method – basic information

| Field | Description |
|---|---|
| Name | Name used internally and externally |
| Technischer Name (Technical name) | Unique identifier for the admin and for extensions |
| Position | Display order in the checkout (1 = first place) |
| Aktiv (Active) | Activation status |
| Beschreibung (Description) | Explanation (visible in the overview and the frontend) |
| Logo | Custom logo (media library or upload) |
| Lieferzeit (Delivery time) | Time shown when selecting the shipping method (requires activation under the cart settings) |
| Tracking-URL | Tracking link with placeholder `%s` for automatic insertion of the tracking number |
| Tags | Keywords for better findability |

---

## Availability rule

Defines via the Rule Builder when this shipping method is available.
- New rules can be created directly
- Typical conditions: delivery country, cart value, weight

---

## Tax calculation

| Option | Description |
|---|---|
| **Automatisch** (Automatic) | Proportional calculation based on the cart's tax rates |
| **Höchste** (Highest) | Calculation with the highest tax rate in the cart |
| **Festgelegt** (Fixed) | Manually selected tax rate |

---

## Price matrix

### By properties
Shipping prices depending on:
| Property | Unit |
|---|---|
| Anzahl Positionen (Number of line items) | All line items in the cart |
| Warenkorbwert (Cart value) | Total of all line items |
| Gewicht (Weight) | Default: kilograms |
| Volumen (Volume) | Width × height × length (in cubic millimetres) |

**Structure of the matrix:**
- Up to a certain value → price X
- Above a certain value → price Y
- Any number of tiers is possible

### By Rule Builder
Alternatively: use custom rules from the Rule Builder (e.g. differentiate by delivery country).

---

## Sales channel assignment

Shipping methods must be assigned to the sales channels:
1. Verkaufskanäle (Sales channels) > [select channel] > Grundeinstellungen (Basic settings) > Versandarten
2. Add shipping method
3. Optional: define the default shipping method
