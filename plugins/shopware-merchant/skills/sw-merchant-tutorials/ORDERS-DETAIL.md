# Shopware 6 — Tutorials: Bestellungen (Orders) — complete reference

---

## Contents

- [1. Creating an order in the admin](#1-creating-an-order-in-the-admin)
- [2. Exporting orders](#2-exporting-orders)
- [3. Orders with PayPal](#3-orders-with-paypal)

## 1. Creating an order in the admin

**Source:** https://docs.shopware.com/de/shopware-6-de/bestellungen/bestellung-im-admin-anlegen  
**From version:** 6.5.0.0

### Step by step

**Step 1 — select a customer:**
- Bestellungen (Orders) > Bestellübersicht (Order overview) > "Bestellung anlegen" (Create order)
- Pick a customer from the list or create one directly in the form

**Step 2 — add products:**
- "Produkte" (Products) section > "Produkt hinzufügen" (Add product)
- The price is determined automatically (adjustable)
- The default tax rate is assigned automatically

**Step 3 — empty line items (for products not in the catalogue):**
- Dropdown next to "Produkt hinzufügen" > "Leere Position hinzufügen" (Add empty line item)
- Enter name, gross price, tax rate and quantity

**Step 4 — credit notes:**
- Dropdown > "Gutschrift hinzufügen" (Add credit note)
- The tax rate is calculated automatically; enter a label and an amount

**Step 5 — configure options:**
- Enable/disable automatic discount promotions
- Set the order language
- Enter a discount code
- Choose a payment method
- Define the billing and delivery address
- Set the shipping method and shipping costs
- Select a currency

**Step 6 — save:**
- "Bestellung speichern" (Save order) → a confirmation mail is sent automatically
- All payment, shipping and order information can be viewed in the details section

### Tips
- Shipping costs: double-click the entry to adjust it manually
- Deleting a line item: tick the checkbox + delete option
- PayPal payment: customers can pay later via their account

---

## 2. Exporting orders

**Source:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/bestellungen-exportieren  
**From version:** 6.4.7.0

### Step 1: create a new profile

Einstellungen (Settings) > Import/Export > Profile > create a new profile.

**Mandatory fields (the export fails without them):**
- `id`
- `salesChannelId`
- `orderDateTime`
- `stateId`

Add further fields via the dropdown in the "Datenbank-Eintrag" (Database entry) column. The value in "Name" becomes the column name in the export.

### Step 2: start the export

Select the "Bestellungen" profile and start the export.

### Step 3: download the file

Download the exported CSV. Recommendation: OpenOffice (no unwanted formatting).

---

## 3. Orders with PayPal

**Source:** https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/bestellungen-mit-paypal  
**From version:** 6.3.0.0

### Basic principle

Payment and order are **separate entities**. The order is created on "Zahlungspflichtig bestellen" (Place binding order) — regardless of whether the payment is completed.

### Payment status explanations

| Status | Cause |
|--------|---------|
| Abgebrochen (Cancelled) | Customer clicks "Zurück zum Shop" (Back to shop) in the PayPal window |
| Fehlgeschlagen (Failed) | The payment was not completed by the customer |
| Unbestätigt (Unconfirmed) | Order triggered, PayPal received no transaction (browser crash) |

### Customer options after a failed order

In their own account, customers can:
- Change the payment method (redirects to the checkout) → order status: "In Bearbeitung" (In progress)
- Repeat the order (a new order is created)

### Field names: Shopware vs. PayPal

| Shopware | PayPal | Meaning |
|----------|--------|-----------|
| `zahlungs_id` | `order_id` | Unique order ID |
| `tracking_id` | `capture_id` / `transaction_id` / `resource_id` | Payment tracking |
| `händler_id` | `merchant_id` / `payer_id` | Merchant identification |

Can be viewed under: Bestellungen > Übersicht (Overview) > Bestellung > PayPal

---

*Source: https://docs.shopware.com/de/shopware-6-de/tutorials-und-faq/bestellungen — as of: 2026-06*
