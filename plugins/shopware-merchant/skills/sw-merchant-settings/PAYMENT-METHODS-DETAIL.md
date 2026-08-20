# Shopware 6 – Zahlungsarten (Payment methods) – complete reference

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/Zahlungsarten

---

## Overview

**Path:** Einstellungen (Settings) > Handel (Commerce) > Zahlungsarten

Lists all stored payment methods with name, active status and description.

### Default payment methods (pre-installed)
- Nachnahme (Cash on Delivery)
- Rechnung (Invoice)
- Vorkasse (Prepayment)
- Lastschrift (Direct Debit)

> **Note:** Availability in the shop depends on the assignment in the Verkaufskanäle (Sales channels) settings.

---

## Creating a payment method

Button "Zahlungsart anlegen" (Create payment method)

| Field | No. | Description |
|---|---|---|
| Name | 1 | Display name of the payment method |
| Technischer Name (Technical name) | 2 | Unique identifier (changing it can deactivate existing payment methods!) |
| Position | 3 | Display order in the storefront |
| Beschreibung (Description) | 4 | Short explanation of the payment method |
| Logo | 5 | Upload your own logo |
| Aktiv (Active) | 6 | Activate/deactivate the payment method |
| Zahlungsartwechsel nach Abschluss (Change payment method after completion) | 7 | Customers may change the payment method in their account after ordering |

> **Important:** The technical name must not be changed after creation if the payment method is already in use.

---

## Availability rule

Uses the Rule Builder to determine the conditions under which the payment method is displayed.

- New rules can be created directly
- Existing rules can be selected
- Typical conditions: delivery country, cart value, Kundengruppe (Customer group)

---

## Assigning a payment method to a sales channel

After creation the payment method must be assigned to the sales channel:
1. Verkaufskanäle > [select channel] > Grundeinstellungen (Basic settings) > Zahlungsarten
2. Add payment method
3. Optional: define the default payment method
