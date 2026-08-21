# Kundenspezifische Preise (Customer-specific prices) – individual pricing

**Source**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/kundenspezifische-preise  
**Plan**: Shopware Beyond (exclusive)  
**Prerequisite**: The Shopware Commercial extension is active

## Contents

- [Overview](#overview)
- [IMPORTANT: API-only approach](#important-api-only-approach)
- [Technical basics](#technical-basics)
- [API endpoints](#api-endpoints)
- [Price definition (JSON schema)](#price-definition-json-schema)
- [Storefront behaviour](#storefront-behaviour)
- [Integration with ERP systems](#integration-with-erp-systems)
- [Access to the API documentation](#access-to-the-api-documentation)

## Overview

**Kundenspezifische Preise** enables individually calculated prices for single customers –
optimised for large B2B shops with an ERP integration.

Special feature: "You can tailor list prices as well as graduated prices or
currency-dependent prices individually to the customer"

---

## IMPORTANT: API-only approach

> **There is NO UI in the admin for customer-specific prices!**
> The feature works **exclusively via API calls**.
> This is by design – optimised for bulk synchronisation from ERP systems.

---

## Technical basics

### Database structure
Customer-specific prices are stored in a dedicated table:
- Customer ID (customer_id)
- Product ID / variant ID (product_id)
- Price definition (JSON with gross/net, graduations, currencies)

### No inheritance
> In contrast to product variants: there is no price inheritance for customer-specific prices.
> For every variant the price has to be set **directly with the variant ID**.
> (Not via the parent product ID)

---

## API endpoints

### Setting prices (POST/PATCH)
```
POST /api/customer-price
PATCH /api/customer-price/{id}
```

### Bulk synchronisation
```
POST /api/_action/sync
```
With a body for the bulk assignment of prices (recommended for the ERP integration)

### Retrieving prices
```
GET /api/customer-price?filter[customer.id]=<customer-id>
```

---

## Price definition (JSON schema)

```json
{
  "customerId": "uuid-des-kunden",
  "productId": "uuid-der-variante",
  "price": [
    {
      "currencyId": "b7d2554b0ce847cd82f3ac9bd1c0dfca",
      "gross": 19.99,
      "net": 16.80,
      "linked": true
    }
  ],
  "quantityStart": 1,
  "quantityEnd": 9
}
```

### Graduated prices (quantity ranges)
Several price rules per customer/product for different quantities:

| quantityStart | quantityEnd | Price |
|---|---|---|
| 1 | 9 | 19.99 € |
| 10 | 49 | 17.99 € |
| 50 | null | 15.99 € |

---

## Storefront behaviour

| State | Display |
|---|---|
| The customer is logged in | The customer-specific price is shown immediately |
| The customer is logged out | The standard list price is shown |
| Graduated price | Depends on the selected quantity (change in the price area) |

---

## Integration with ERP systems

Typical workflow:
1. The ERP (for example SAP, Microsoft Dynamics) holds the individual prices
2. On changes: the ERP calls the Shopware Sync API
3. Shopware stores the new prices in the database
4. The next time the customer logs in: the new prices are visible immediately

### Performance note
- The system is designed for large data volumes ("speed-oriented API")
- Use a bulk sync via `_action/sync` instead of individual calls

---

## Access to the API documentation

Full API documentation: https://shopware.stoplight.io
(Category: Customer Price / Kundenpreise)
