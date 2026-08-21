# Shopware 6 — API end-to-end flows

Complete walkthroughs as bash/curl sequences for local development on `http://127.0.0.1:8000`.

## Preparation — determine IDs

```bash
ADMIN_TOKEN=$(curl -s -X POST "http://127.0.0.1:8000/api/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{"grant_type":"password","client_id":"administration","scopes":"write","username":"admin","password":"shopware"}' \
  | jq -r '.access_token')

# Tax ID
curl -s -X POST "http://127.0.0.1:8000/api/search/tax" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" -d '{"limit":10}' | jq

# Sales Channel + Store API Key
curl -s -X POST "http://127.0.0.1:8000/api/search/sales-channel" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" \
  -d '{"limit":10,"includes":{"sales_channel":["id","name","accessKey"]}}' | jq

# System currency
curl -s -X POST "http://127.0.0.1:8000/api/search/currency" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" \
  -d '{"includes":{"currency":["id","isoCode","isSystemDefault"]}}' | jq
```

## Create a product (Admin API)

```bash
PRODUCT_ID=$(uuidgen | tr '[:upper:]' '[:lower:]' | tr -d '-')
curl -s -X POST "http://127.0.0.1:8000/api/product" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" \
  -d "{\"id\":\"$PRODUCT_ID\",\"name\":\"Test product\",\"productNumber\":\"TEST-001\",
      \"stock\":10,\"active\":true,\"taxId\":\"$TAX_ID\",
      \"price\":[{\"currencyId\":\"$CURRENCY_ID\",\"gross\":19.99,\"net\":16.80,\"linked\":true}],
      \"visibilities\":[{\"salesChannelId\":\"$SALES_CHANNEL_ID\",\"visibility\":30}]}"
```

`visibility`: 10=via link only, 20=search, 30=visible everywhere.

## Store API — context, search, cart

```bash
# Fetch the context token
STORE_TOKEN=$(curl -si "http://127.0.0.1:8000/store-api/context" \
  -H "sw-access-key: $STORE_KEY" | tr -d '\r' | awk -F': ' 'tolower($1)=="sw-context-token"{print $2}')

# Search for the product
curl -s -X POST "http://127.0.0.1:8000/store-api/search" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"term":"Test product","includes":{"product":["id","name","calculatedPrice"]}}' | jq

# Add to the cart
curl -s -X POST "http://127.0.0.1:8000/store-api/checkout/cart/line-item" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"items\":[{\"id\":\"$PRODUCT_ID\",\"referencedId\":\"$PRODUCT_ID\",\"type\":\"product\",\"quantity\":1}]}" | jq
```

## Register a customer → order

```bash
# Register the customer (may return a new Sw-Context-Token!)
curl -i -X POST "http://127.0.0.1:8000/store-api/account/register" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"salutationId\":\"$SALUTATION_ID\",\"firstName\":\"Max\",\"lastName\":\"Sample\",
      \"email\":\"test@example.com\",\"password\":\"shopware123!\",\"acceptedDataProtection\":true,
      \"storefrontUrl\":\"http://127.0.0.1:8000\",
      \"billingAddress\":{\"street\":\"Sample St. 1\",\"zipcode\":\"12345\",\"city\":\"Sampletown\",
      \"countryId\":\"$COUNTRY_ID\",\"firstName\":\"Max\",\"lastName\":\"Sample\"}}"
# Save the new Sw-Context-Token from the header! Then add the product again.

# Place the order
curl -s -X POST "http://127.0.0.1:8000/store-api/checkout/order" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" -d '{}' | jq

# Handle the payment (if required)
curl -s -X POST "http://127.0.0.1:8000/store-api/handle-payment" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"orderId":"ORDER_ID","finishUrl":"http://127.0.0.1:8000/checkout/finish"}' | jq
```

Salutation/country IDs: `/store-api/salutation` and `/store-api/country`.
Detailed reference: `API-FLOWS-DETAIL.md`. Auth: `sw-api-integration`.
