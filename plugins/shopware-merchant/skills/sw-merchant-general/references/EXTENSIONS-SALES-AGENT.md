# Sales Agent – the field sales frontend app

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/sales-agent  
**Plan**: Shopware Evolve (or higher)  
**Available from**: Shopware 6.5.0.0  
**Type**: A separate frontend application (not an admin plugin)

## Contents

- [Overview](#overview)
- [Technical particularity](#technical-particularity)
- [Administration (Shopware admin)](#administration-shopware-admin)
- [The Sales Agent frontend app](#the-sales-agent-frontend-app)
- [Quote system](#quote-system)
- [Personal settings (Sales Agent portal)](#personal-settings-sales-agent-portal)
- [Use cases](#use-cases)

## Overview

The **Sales Agent** is a user management system for sales teams:
- Field sales staff get their own accounts
- They can view the customers assigned to them and their order history
- They can place orders on behalf of customers
- A quote system for individual price negotiations

> "The Sales Agent is **not** an extension that can be installed in the Shopware admin
> or activated with a click, but a **separate frontend app**."

---

## Technical particularity

The Sales Agent is provided as **source code via a GitLab repository**:
- Agencies and developers can adapt and integrate the app
- Deployment by a technical team is necessary
- The connection to the Shopware backend runs via the API

---

## Administration (Shopware admin)

### Access
**Einstellungen** (Settings) **> System > Sales Agent**

### Creating sales user accounts
1. Click "Neuen Sales Agent anlegen" (Create new Sales Agent)
2. Enter the name and email address
3. Assign customers (multiple selection)
4. Save → an automatic **invitation email** with a link to set the password

### Assigning customers
- Any number of customers can be assigned to a Sales Agent
- A customer can be assigned to several Sales Agents
- The assignment can be changed at any time

---

## The Sales Agent frontend app

### Dashboard features

| Feature | Description |
|---|---|
| Customer list | An overview of all assigned customers |
| Order history | View the orders per customer |
| New order | Order on behalf of the customer |
| Quote creation | Create quotes with individual prices |
| Quote management | Track the status, send quotes |

### A new order on behalf of a customer
1. Select the customer in the list
2. Click "Neue Bestellung" (New order)
3. Select and configure the products
4. Quantity and optional adjustments
5. Place the order

---

## Quote system

### Creating a quote
1. Select the customer
2. Create a "Neues Angebot" (New quote)
3. Add the products
4. Define **individual prices** and **discounts**
5. Set an expiry date
6. **Auto-generate the document** or upload a manual document
7. Send the quote to the customer (an email with a quote link)

### Quote workflow
```
Sales Agent creates a quote
  → Customer receives an email with the quote link
  → Customer opens the quote in the storefront
  → Customer accepts → an order is created
  → Or: customer rejects → Sales Agent is notified
```

---

## Personal settings (Sales Agent portal)

Sales Agents can change the following themselves:
- Display language
- Time zone
- First name / last name
- Phone number
- Password

**Not changeable by the Sales Agent**:
- The email address (admin only)
- The customer assignments (admin only)

---

## Use cases

- B2B field sales: sales staff order on site for customers
- Key account management: dedicated representatives for major customers
- Telephone sales: sales staff take orders over the phone
- Quote processes: price negotiations with traceable quotes
