# B2B Suite – administration & customer account

**Sources**:  
- https://docs.shopware.com/de/shopware-6-de/erweiterungen/b2b-suite-administration  
- https://docs.shopware.com/de/shopware-6-de/erweiterungen/b2b-suite-kundenaccount  
**Plan**: Shopware Evolve (or higher)

## Contents

- [IMPORTANT NOTE: deprecation](#important-note-deprecation)
- [Overview (B2B Suite legacy)](#overview-b2b-suite-legacy)
- [Roles in the B2B Suite](#roles-in-the-b2b-suite)
- [Administration (admin perspective)](#administration-admin-perspective)
- [Customer account features (storefront perspective)](#customer-account-features-storefront-perspective)
- [Migration to B2B Components](#migration-to-b2b-components)

## IMPORTANT NOTE: deprecation

> **The B2B Suite is no longer being developed further!**
> All new features are being delivered through the **B2B Components**.
> End of support: **after Shopware 6.8**
> Migration deadline: **until 24 May 2025** (switch over to B2B Components)

For new projects: use the **B2B Components** (part of Shopware Commercial from the Evolve plan).

---

## Overview (B2B Suite legacy)

The B2B Suite gives companies extended organisational structures for their Shopware 6 instance:
- Multi-level company hierarchies
- Role-based permissions
- Budgets and approval workflows

---

## Roles in the B2B Suite

| Role | Description |
|---|---|
| **Debitor** (Debtor) | Central company account (primary B2B account) |
| **Field Service Representative** | Field sales employee; can access customer accounts |
| **Kontakt** (Contact) | Employee account within the debtor |

---

## Administration (admin perspective)

### Where it is configured
- The B2B configuration is **not available as a separate menu item**
- It is integrated directly into **customer management**: Kunden (Customers) > [customer name] > B2B

### Angebotsverwaltung (Quote management) (Offers)

Workflow for customer-specific prices:

1. The customer submits a price request via the storefront customer account
2. The admin sees the request in the **Angebotsverwaltung**
3. The admin can:
   - **Annehmen** (Accept): confirm the quote at the requested price
   - **Ablehnen** (Reject): turn the request down
   - **Gegenangebot** (Counter-offer): propose their own price

**Status colour codes**:
- Grey: not yet processed (awaiting review)
- Red: rejected
- Blue: accepted / active

---

## Customer account features (storefront perspective)

### Dashboard areas

| Area | Function |
|---|---|
| **Dashboard** | Overview of all B2B features |
| **Unternehmen** (Company) | Manage roles, contacts, addresses, budgets, quotas |
| **Statistiken** (Statistics) | Filterable order analyses |
| **Bestellungen** (Orders) | Order history, pending approvals |
| **Bestelllisten** (Order lists) | Reusable product lists for recurring orders |
| **Schnellbestellung** (Quick order) | Bulk product entry (product number + quantity) |
| **Angebote** (Quotes) | Submit and manage quote requests |
| **Bestellnummern** (Order numbers) | Internal product numbering |

### Roles & permissions (customer view)
Debtors can create sub-accounts (contacts) with specific rights:
- Ordering allowed
- Order limit (budget)
- Access to certain areas

### Budgets & quotas
- Spending limits per period (e.g. €1,000 / month)
- If exceeded: the order enters an approval workflow
- Approval by a supervisor/administrator

---

## Migration to B2B Components

### Why migrate?
- B2B Suite: no new features, end of support after 6.8
- B2B Components: actively developed, part of Shopware Commercial

### Available B2B Components (from the Evolve plan)
- Quick Order (Schnellbestellung)
- Approval processes (order approvals)
- Quotes (Angebote)
- Employee Management
- Order Lists

### Migration guide
→ https://docs.shopware.com/de/shopware-6-de/features/b2b-components
