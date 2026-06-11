---
name: sw-api-flows
description: >
  Shopware 6 API End-to-End-Flows: Produkt anlegen (Admin API) → Store API lesen → Warenkorb →
  Kunde registrieren → Bestellung aufgeben → Zahlung. Alle Schritte mit curl/bash-Beispielen.
  Trigger: "api flow", "produkt anlegen api", "warenkorb api", "bestellung api", "checkout api",
  "customer register api", "end to end api", "order placed api", "product create admin api",
  "store api checkout", "handle-payment api", "create product api flow". Shopware 6.7.
---

# Shopware 6 — API End-to-End-Flows

Vollständige Abläufe als bash/curl-Sequenzen für lokale Entwicklung auf `http://127.0.0.1:8000`.

## Vorbereitung — IDs ermitteln

```bash
ADMIN_TOKEN=$(curl -s -X POST "http://127.0.0.1:8000/api/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{"grant_type":"password","client_id":"administration","scopes":"write","username":"admin","password":"shopware"}' \
  | jq -r '.access_token')

# Tax-ID
curl -s -X POST "http://127.0.0.1:8000/api/search/tax" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" -d '{"limit":10}' | jq

# Sales Channel + Store API Key
curl -s -X POST "http://127.0.0.1:8000/api/search/sales-channel" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" \
  -d '{"limit":10,"includes":{"sales_channel":["id","name","accessKey"]}}' | jq

# System Currency
curl -s -X POST "http://127.0.0.1:8000/api/search/currency" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" \
  -d '{"includes":{"currency":["id","isoCode","isSystemDefault"]}}' | jq
```

## Produkt anlegen (Admin API)

```bash
PRODUCT_ID=$(uuidgen | tr '[:upper:]' '[:lower:]' | tr -d '-')
curl -s -X POST "http://127.0.0.1:8000/api/product" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -H "Content-Type: application/json" \
  -d "{\"id\":\"$PRODUCT_ID\",\"name\":\"Testprodukt\",\"productNumber\":\"TEST-001\",
      \"stock\":10,\"active\":true,\"taxId\":\"$TAX_ID\",
      \"price\":[{\"currencyId\":\"$CURRENCY_ID\",\"gross\":19.99,\"net\":16.80,\"linked\":true}],
      \"visibilities\":[{\"salesChannelId\":\"$SALES_CHANNEL_ID\",\"visibility\":30}]}"
```

`visibility`: 10=nur via Link, 20=Suche, 30=überall sichtbar.

## Store API — Context, Suche, Warenkorb

```bash
# Context-Token holen
STORE_TOKEN=$(curl -si "http://127.0.0.1:8000/store-api/context" \
  -H "sw-access-key: $STORE_KEY" | tr -d '\r' | awk -F': ' 'tolower($1)=="sw-context-token"{print $2}')

# Produkt suchen
curl -s -X POST "http://127.0.0.1:8000/store-api/search" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"term":"Testprodukt","includes":{"product":["id","name","calculatedPrice"]}}' | jq

# Zum Warenkorb hinzufügen
curl -s -X POST "http://127.0.0.1:8000/store-api/checkout/cart/line-item" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"items\":[{\"id\":\"$PRODUCT_ID\",\"referencedId\":\"$PRODUCT_ID\",\"type\":\"product\",\"quantity\":1}]}" | jq
```

## Kunde registrieren → Bestellung

```bash
# Kunde registrieren (gibt ggf. neuen Sw-Context-Token zurück!)
curl -i -X POST "http://127.0.0.1:8000/store-api/account/register" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"salutationId\":\"$SALUTATION_ID\",\"firstName\":\"Max\",\"lastName\":\"Mustermann\",
      \"email\":\"test@example.com\",\"password\":\"shopware123!\",\"acceptedDataProtection\":true,
      \"storefrontUrl\":\"http://127.0.0.1:8000\",
      \"billingAddress\":{\"street\":\"Musterstr. 1\",\"zipcode\":\"12345\",\"city\":\"Stadt\",
      \"countryId\":\"$COUNTRY_ID\",\"firstName\":\"Max\",\"lastName\":\"Mustermann\"}}"
# Neuen Sw-Context-Token aus Header speichern! Dann Produkt nochmal hinzufügen.

# Bestellung aufgeben
curl -s -X POST "http://127.0.0.1:8000/store-api/checkout/order" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" -d '{}' | jq

# Zahlung abwickeln (falls nötig)
curl -s -X POST "http://127.0.0.1:8000/store-api/handle-payment" \
  -H "sw-access-key: $STORE_KEY" -H "sw-context-token: $STORE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"orderId":"ORDER_ID","finishUrl":"http://127.0.0.1:8000/checkout/finish"}' | jq
```

Salutation/Country IDs: `/store-api/salutation` und `/store-api/country`.
Detaillierte Referenz: `references/deep/api-flows.md`. Auth: `sw-api-integration`.
