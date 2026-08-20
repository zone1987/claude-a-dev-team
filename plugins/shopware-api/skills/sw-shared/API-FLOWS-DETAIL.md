# Shopware 6 — API end-to-end flows (complete reference)

Source: `guides/development/integrations-api/flows/create-product.md`

## Contents

- [Overview](#overview)
- [Step 1: Admin API token (local)](#step-1-admin-api-token-local)
- [Step 2: download the API schemas (optional, but recommended)](#step-2-download-the-api-schemas-optional-but-recommended)
- [Step 3: determine the required IDs](#step-3-determine-the-required-ids)
- [Step 4: create a category](#step-4-create-a-category)
- [Step 5: create a product](#step-5-create-a-product)
- [Step 6: create a Store API context](#step-6-create-a-store-api-context)
- [Step 7: read the product via the Store API](#step-7-read-the-product-via-the-store-api)
- [Step 8: put the product into the cart](#step-8-put-the-product-into-the-cart)
- [Step 9: prepare the checkout](#step-9-prepare-the-checkout)
- [Step 10: register a customer and place the order](#step-10-register-a-customer-and-place-the-order)
- [Troubleshooting](#troubleshooting)
- [Rule of thumb: Admin API vs. Store API](#rule-of-thumb-admin-api-vs-store-api)

## Overview

This flow shows a complete local development walkthrough:
1. Create a category and a product with the Admin API
2. Read the product with the Store API
3. Put the product into the cart
4. Register a customer in the Store API context
5. Place the order
6. Handle the payment (if required)

Development environment: `http://127.0.0.1:8000`. Required tools: `curl`, `jq`.

### Important details for local setups

- The Store API uses `sw-access-key`, not `sw-access-token`
- `/store-api/context` is called with `GET`
- Store API context tokens are ephemeral and can expire during longer debug sessions
- `register` or `login` can return a new `Sw-Context-Token`
- When the context changes, the cart has to be filled again
- Creating a product requires a price in the **system default currency**
- Customer registration requires real IDs: `salutationId`, `countryId`

## Step 1: Admin API token (local)

```bash
ADMIN_TOKEN=$(curl -s -X POST "http://127.0.0.1:8000/api/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "password",
    "client_id": "administration",
    "scopes": "write",
    "username": "admin",
    "password": "shopware"
  }' | jq -r '.access_token')

printf '%s\n' "$ADMIN_TOKEN"
```

## Step 2: download the API schemas (optional, but recommended)

```bash
curl -s "http://127.0.0.1:8000/api/_info/openapi3.json" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -o openapi.json

curl -s "http://127.0.0.1:8000/api/_info/open-api-schema.json" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -o entity-schema.json
```

## Step 3: determine the required IDs

### Find the tax ID

```bash
curl -s -X POST "http://127.0.0.1:8000/api/search/tax" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"limit": 10, "sort": [{"field": "name", "order": "ASC"}]}' | jq
```

### Sales Channel ID + Store API Access Key

```bash
curl -s -X POST "http://127.0.0.1:8000/api/search/sales-channel" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "limit": 10,
    "includes": {"sales_channel": ["id", "name", "accessKey"]}
  }' | jq
```

### System default currency ID

```bash
curl -s -X POST "http://127.0.0.1:8000/api/search/currency" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"includes": {"currency": ["id", "name", "isoCode", "isSystemDefault"]}}' | jq
```

### Store the IDs

```bash
TAX_ID="<from-response>"
SALES_CHANNEL_ID="<from-response>"
CURRENCY_ID="<from-response>"
STORE_API_ACCESS_KEY="<accessKey-from-response>"
```

## Step 4: create a category

```bash
CATEGORY_ID=$(uuidgen | tr '[:upper:]' '[:lower:]' | tr -d '-')

curl -s -X POST "http://127.0.0.1:8000/api/category" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"id\": \"$CATEGORY_ID\", \"name\": \"Example category\", \"active\": true}"

# Verify:
curl -s -X POST "http://127.0.0.1:8000/api/search/category" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"ids\": [\"$CATEGORY_ID\"], \"includes\": {\"category\": [\"id\", \"name\", \"active\"]}}" | jq
```

## Step 5: create a product

```bash
PRODUCT_ID=$(uuidgen | tr '[:upper:]' '[:lower:]' | tr -d '-')
PRODUCT_NUMBER="ExampleProduct-001"

curl -s -X POST "http://127.0.0.1:8000/api/product" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"id\": \"$PRODUCT_ID\",
    \"name\": \"My example product\",
    \"productNumber\": \"$PRODUCT_NUMBER\",
    \"stock\": 10,
    \"active\": true,
    \"taxId\": \"$TAX_ID\",
    \"price\": [{
      \"currencyId\": \"$CURRENCY_ID\",
      \"gross\": 19.99,
      \"net\": 16.80,
      \"linked\": true
    }],
    \"visibilities\": [{
      \"salesChannelId\": \"$SALES_CHANNEL_ID\",
      \"visibility\": 30
    }],
    \"categories\": [{\"id\": \"$CATEGORY_ID\"}]
  }"
```

### Visibility values

- `10` (VISIBILITY_LINK): hidden in listings and search — reachable only via a direct link
- `20` (VISIBILITY_SEARCH): hidden in listings — visible only in search
- `30` (VISIBILITY_ALL): visible everywhere (listings + search)

### Verify the product

```bash
curl -s -X POST "http://127.0.0.1:8000/api/search/product" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -H "sw-inheritance: 1" \
  -d "{
    \"ids\": [\"$PRODUCT_ID\"],
    \"associations\": {\"categories\": {}},
    \"includes\": {
      \"product\": [\"id\", \"name\", \"productNumber\", \"active\", \"translated\", \"categories\"],
      \"category\": [\"id\", \"name\"]
    }
  }" | jq
```

`sw-inheritance: 1` → take inheritance from parent/variants into account.

## Step 6: create a Store API context

```bash
# Fetch the context token (from the response header)
curl -i "http://127.0.0.1:8000/store-api/context" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY"

# Extract it automatically:
STORE_CONTEXT_TOKEN=$(curl -si "http://127.0.0.1:8000/store-api/context" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  | tr -d '\r' | awk -F': ' 'tolower($1)=="sw-context-token" {print $2}')

echo "$STORE_CONTEXT_TOKEN"
```

## Step 7: read the product via the Store API

```bash
# Full-text search
curl -s -X POST "http://127.0.0.1:8000/store-api/search" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"term\": \"My example product\",
    \"limit\": 5,
    \"includes\": {\"product\": [\"id\", \"name\", \"translated\", \"calculatedPrice\"]}
  }" | jq

# Filter by productNumber
curl -s -X POST "http://127.0.0.1:8000/store-api/search" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"filter\": [
      {\"type\": \"equals\", \"field\": \"active\", \"value\": true},
      {\"type\": \"equals\", \"field\": \"productNumber\", \"value\": \"$PRODUCT_NUMBER\"}
    ],
    \"includes\": {\"product\": [\"id\", \"name\", \"productNumber\", \"calculatedPrice\"]}
  }" | jq
```

## Step 8: put the product into the cart

```bash
curl -s -X POST "http://127.0.0.1:8000/store-api/checkout/cart/line-item" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"items\": [{
      \"id\": \"$PRODUCT_ID\",
      \"referencedId\": \"$PRODUCT_ID\",
      \"type\": \"product\",
      \"quantity\": 1
    }]
  }" | jq

# Check the cart:
curl -s -X GET "http://127.0.0.1:8000/store-api/checkout/cart" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" | jq
```

## Step 9: prepare the checkout

Before placing the order the context needs:
- A logged-in customer
- Active billing and shipping addresses
- A shipping method
- A payment method

Determine the IDs for the registration:
```bash
# Salutation IDs
curl -s "http://127.0.0.1:8000/store-api/salutation" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" | jq

# Country IDs
curl -s "http://127.0.0.1:8000/store-api/country" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" | jq
```

## Step 10: register a customer and place the order

### 10.1 Register the customer

```bash
curl -i -X POST "http://127.0.0.1:8000/store-api/account/register" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"salutationId\": \"$SALUTATION_ID\",
    \"firstName\": \"Max\",
    \"lastName\": \"Sample\",
    \"email\": \"test@example.com\",
    \"password\": \"shopware123!\",
    \"acceptedDataProtection\": true,
    \"storefrontUrl\": \"http://127.0.0.1:8000\",
    \"billingAddress\": {
      \"firstName\": \"Max\",
      \"lastName\": \"Sample\",
      \"street\": \"Sample St. 1\",
      \"zipcode\": \"12345\",
      \"city\": \"Sampletown\",
      \"countryId\": \"$COUNTRY_ID\"
    }
  }"
```

**IMPORTANT**: save the new `Sw-Context-Token` from the response header!
```bash
STORE_CONTEXT_TOKEN="NEW_TOKEN_FROM_HEADER"
```

### 10.2 Add the product again after the context change

After register/login the context token can change → the cart is empty → add the product again.

### 10.3 Place the order

```bash
curl -s -X POST "http://127.0.0.1:8000/store-api/checkout/order" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"customerComment": "Test order"}' | jq
```

Error `Cart is empty` → add the product to the cart again.
Error `Customer is not logged in` → log in/register in the correct context.

### 10.4 Handle the payment (if required)

```bash
curl -s -X POST "http://127.0.0.1:8000/store-api/handle-payment" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "orderId": "ORDER_ID",
    "finishUrl": "http://127.0.0.1:8000/checkout/finish",
    "errorUrl": "http://127.0.0.1:8000/checkout/confirm"
  }' | jq
```

`"redirectUrl": null` → the payment method requires no redirect flow.

## Troubleshooting

### Schema endpoints return 500 or report missing tables

Re-initialise the DB:
```bash
docker compose exec web bin/console system:install --create-database --basic-setup
```

### The product does not appear in the Store API

Checklist:
- `active: true`
- A valid `price` is set
- `visibilities` exist for the sales channel
- The correct Store API access key
- The storefront sales channel domain matches the local URL

### Relevant request headers

- Admin API: `Authorization: Bearer $ADMIN_TOKEN`, optional `sw-language-id`, `sw-version-id`, `sw-inheritance`, `sw-currency-id`
- Store API: `sw-access-key`, `sw-context-token`

## Rule of thumb: Admin API vs. Store API

| Area | API |
|---|---|
| Create/manage data | Admin API |
| Act as a buyer | Store API |
| Checkout, cart | Store API |
| Create products/categories | Admin API |
| Headless storefront | Store API |
