# Shopware B2B Components – Complete documentation

## Contents

- [Overview](#overview)
- [Feature 1: Angebots-Management (Quote Management)](#feature-1-angebots-management-quote-management)
- [Feature 2: Mitarbeiterverwaltung (Employee Management)](#feature-2-mitarbeiterverwaltung-employee-management)
- [Feature 3: Bestellgenehmigungen (Order Approvals)](#feature-3-bestellgenehmigungen-order-approvals)
- [Feature 4: Organisationseinheiten (Organizational Units)](#feature-4-organisationseinheiten-organizational-units)
- [Feature 5: Extended product catalogues](#feature-5-extended-product-catalogues)
- [Feature 6: Budgets](#feature-6-budgets)
- [Feature 7: B2B customer-specific prices](#feature-7-b2b-customer-specific-prices)
- [Feature 8: Schnell-Bestellungen (Quick Orders)](#feature-8-schnell-bestellungen-quick-orders)
- [Feature 9: Einkaufslisten (Shopping Lists)](#feature-9-einkaufslisten-shopping-lists)
- [Feature 10: Sales Agent (field sales)](#feature-10-sales-agent-field-sales)
- [Activation overview](#activation-overview)

## Overview

The B2B Components are a set of functionalities for B2B trade in Shopware 6. They activate essential B2B workflows through the Shopware Commercial extension.

**Availability:** Evolve plan and higher
**Activation:** Individually per customer or via customer group registration forms

### Activating B2B for individual customers
Path: Kunden (Customers) → Übersicht (Overview) → select the customer → B2B area → Aktivieren (Activate)

### Activating B2B for customer groups
Path: Einstellungen (Settings) → Kunden → Kundengruppen (Customer groups) → registration form with the B2B option

---

## Feature 1: Angebots-Management (Quote Management)

**Available from:** Evolve plan

### Workflow
1. Customers fill the cart and request a quote
2. The merchant sees the request under: Bestellungen (Orders) → Angebote (Quotes)
3. The merchant reviews it and replies with:
   - Individual prices or discounts
   - An optional expiry date
4. Customers receive the quote and can accept/decline it

### For the Sales Agent
Field sales staff can create quotes through the Sales Agent app:
- General info: customer choice, Verkaufskanal (Sales channel)
- Positionen (Line items): add products with standard and special prices
- Discounts: absolute or percentage
- Documents: auto-PDF or upload
- Dispatch settings: expiry date, personal message

---

## Feature 2: Mitarbeiterverwaltung (Employee Management)

**Available from:** Shopware 6.5.6.0 (Evolve+)

### Scope of functions
- Companies register employees in the B2B area
- Assign roles with specific permissions:
  - Employee management
  - Role management
  - Orders

### Employee roles
Administrators define roles and determine which actions employees are allowed to perform.

**Path in the admin:** Kunden → B2B → Mitarbeiter (Employees)

---

## Feature 3: Bestellgenehmigungen (Order Approvals)

**Available from:** Shopware 6.5.8.0 (Evolve+)

### How it works
1. The merchant creates approval rules per role
2. The rule defines: who has to approve orders? Under which conditions?
   - Example: an order value above 1,000 € requires manager approval
   - Example: certain shipping methods require a release
3. The order is paused when approval is required
4. The approving employee receives a notification and can release/decline it

---

## Feature 4: Organisationseinheiten (Organizational Units)

**Available from:** Evolve+

### Use cases
- Multi-site companies (e.g. branches)
- Educational institutions with departments
- Groups with subsidiaries

### Functions per unit
- Its own order history
- Separate delivery addresses
- Its own users and roles
- Independent budget management

---

## Feature 5: Extended product catalogues

**Available from:** Evolve+

Merchants can restrict the visibility of product categories per organizational unit:
- In the storefront: products visible only for certain units
- In the admin: release/block categories for certain units

---

## Feature 6: Budgets

**Available from:** Shopware 6.7.4.0 (Evolve+)

### Configuration
- Set spending limits for organizational units
- Automatic renewal options (daily/monthly/yearly)
- Notifications when a threshold is approached

### Behaviour
- Employees cannot order beyond their budget
- Approvers can manually release budget overruns

---

## Feature 7: B2B customer-specific prices

**Available from:** Shopware 6.7.8.0 (Evolve+)

Percentage, fixed or tiered discounts based on:
- Rules assigned to organizational units
- Customer tags

**Important:** This is the B2B-internal variant. Full customer-specific pricing via API is a Beyond feature (→ `sw-merchant-commercial-custom-pricing`).

---

## Feature 8: Schnell-Bestellungen (Quick Orders)

**Available from:** Evolve+

Accelerated ordering process for recurring B2B buyers:

**Method 1: product number search**
- Customers enter product numbers directly
- The system completes product name and price automatically

**Method 2: CSV upload**
```
product_number,quantity
SW-100,5
SW-200,10
SW-300,2
```

Both methods forward directly into the cart.

---

## Feature 9: Einkaufslisten (Shopping Lists)

**Available from:** Evolve+

### Customer shopping lists
- Customers create personal lists for frequent purchases
- Lists can be saved, named and managed
- Can be transferred into the cart directly

### Pre-configured lists (merchant)
- Merchants create lists for specific use cases
- Make them available to customer groups or individual customers
- Example: "Standard-Bürobedarf" (standard office supplies) for corporate customers

---

## Feature 10: Sales Agent (field sales)

Separate skill: `sw-merchant-commercial-sales-agent`

The Sales Agent app enables field sales staff to:
- View and manage customer data
- Create orders directly for customers
- Create and send quotes

---

## Activation overview

| Feature | Plan | Minimum version |
|---|---|---|
| Angebots-Management | Evolve+ | 6.5.x |
| Mitarbeiterverwaltung | Evolve+ | 6.5.6.0 |
| Bestellgenehmigungen | Evolve+ | 6.5.8.0 |
| Organisationseinheiten | Evolve+ | 6.5.x |
| Extended product catalogues | Evolve+ | 6.5.x |
| Budgets | Evolve+ | 6.7.4.0 |
| B2B customer prices | Evolve+ | 6.7.8.0 |
| Schnell-Bestellungen | Evolve+ | 6.5.x |
| Einkaufslisten | Evolve+ | 6.5.x |
| Sales Agent | Evolve+ | 6.5.0.0 |

---

*Source: https://docs.shopware.com/de/shopware-6-de/commercial-features/b2b-components (as of: 2026-06)*
