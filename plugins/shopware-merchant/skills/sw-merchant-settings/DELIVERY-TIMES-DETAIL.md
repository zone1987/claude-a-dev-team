# Shopware 6 – Lieferzeiten (Delivery times) (complete reference)

Source: https://docs.shopware.com/de/shopware-6-de/einstellungen/lieferzeiten

---

## Overview

**Path:** Einstellungen (Settings) > Handel (Commerce) > Lieferzeiten

Allows expected delivery times to be shown on product detail pages.

---

## Creating a delivery time

| Field | Type | Description |
|---|---|---|
| Name | Text | Customer-friendly label (appears on the product detail page) |
| Einheit (Unit) | Dropdown | Tag (Day), Woche (Week), Monat (Month), Jahr (Year) |
| Minimum | Integer | Minimum duration |
| Maximum | Integer | Maximum duration |

---

## Assigning a delivery time

### On shipping methods
- In the Basisinformationen (Basic information) of the Versandart (Shipping method) → select a Lieferzeit
- This acts as the default for products without their own delivery time assignment
- Useful for country-specific or shipping-method-specific differences

### On products
- In the "Lieferbarkeit" (Deliverability) area of the product information
- A product-specific delivery time **overrides** the shipping method delivery time

---

## Cart display

**Activation:** Einstellungen > Allgemein (General) > Warenkorb (Cart) > "Lieferzeit im Warenkorb anzeigen" (Show delivery time in the cart)

- Configurable per Verkaufskanal (Sales channel)
- Calculated from the current date
- Takes stock levels and restocking times into account

---

## Calculation logic

The dynamic display combines:
1. The delivery time of the product
2. Available stock
3. Restocking time (when stock is insufficient)

**Example:**
- Current date: 01/01/2020
- Delivery time: 1–3 days
- Stock: available
- Result: "expected 02/01/2020–04/01/2020"

---

## Storefront presentation

- Next to the availability status on product detail pages
- Dynamic date range in the cart and checkout (when enabled)
- Individually for every item in the cart
