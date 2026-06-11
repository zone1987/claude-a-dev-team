# Shopware 6 — API End-to-End-Flows (vollständige Referenz)

Quelle: `guides/development/integrations-api/flows/create-product.md`

## Überblick

Dieser Flow zeigt einen vollständigen lokalen Entwicklungs-Ablauf:
1. Kategorie und Produkt mit der Admin API anlegen
2. Produkt mit der Store API lesen
3. Produkt in den Warenkorb legen
4. Kunden im Store API-Kontext registrieren
5. Bestellung aufgeben
6. Zahlung abwickeln (falls nötig)

Entwicklungsumgebung: `http://127.0.0.1:8000`. Benötigte Tools: `curl`, `jq`.

### Wichtige Details für lokale Setups

- Store API verwendet `sw-access-key`, nicht `sw-access-token`
- `/store-api/context` wird mit `GET` aufgerufen
- Store API Context Tokens sind ephemer und können bei längeren Debug-Sessions ablaufen
- `register` oder `login` kann einen neuen `Sw-Context-Token` zurückgeben
- Bei Kontextänderung muss der Warenkorb neu befüllt werden
- Produktanlage erfordert Preis in der **System-Standardwährung**
- Kundenregistrierung erfordert echte IDs: `salutationId`, `countryId`

## Schritt 1: Admin API Token (lokal)

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

## Schritt 2: API-Schemas herunterladen (optional, aber empfohlen)

```bash
curl -s "http://127.0.0.1:8000/api/_info/openapi3.json" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -o openapi.json

curl -s "http://127.0.0.1:8000/api/_info/open-api-schema.json" \
  -H "Authorization: Bearer $ADMIN_TOKEN" -o entity-schema.json
```

## Schritt 3: Benötigte IDs ermitteln

### Tax-ID finden

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

### System-Default-Currency ID

```bash
curl -s -X POST "http://127.0.0.1:8000/api/search/currency" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"includes": {"currency": ["id", "name", "isoCode", "isSystemDefault"]}}' | jq
```

### IDs speichern

```bash
TAX_ID="<aus-response>"
SALES_CHANNEL_ID="<aus-response>"
CURRENCY_ID="<aus-response>"
STORE_API_ACCESS_KEY="<accessKey-aus-response>"
```

## Schritt 4: Kategorie anlegen

```bash
CATEGORY_ID=$(uuidgen | tr '[:upper:]' '[:lower:]' | tr -d '-')

curl -s -X POST "http://127.0.0.1:8000/api/category" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"id\": \"$CATEGORY_ID\", \"name\": \"Beispielkategorie\", \"active\": true}"

# Verifizieren:
curl -s -X POST "http://127.0.0.1:8000/api/search/category" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"ids\": [\"$CATEGORY_ID\"], \"includes\": {\"category\": [\"id\", \"name\", \"active\"]}}" | jq
```

## Schritt 5: Produkt anlegen

```bash
PRODUCT_ID=$(uuidgen | tr '[:upper:]' '[:lower:]' | tr -d '-')
PRODUCT_NUMBER="BeispielProdukt-001"

curl -s -X POST "http://127.0.0.1:8000/api/product" \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"id\": \"$PRODUCT_ID\",
    \"name\": \"Mein Beispielprodukt\",
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

### Visibility-Werte

- `10` (VISIBILITY_LINK): Versteckt in Listings und Suche — nur via direktem Link erreichbar
- `20` (VISIBILITY_SEARCH): Versteckt in Listings — nur in Suche sichtbar
- `30` (VISIBILITY_ALL): Überall sichtbar (Listings + Suche)

### Produkt verifizieren

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

`sw-inheritance: 1` → Vererbung von Parent/Varianten berücksichtigen.

## Schritt 6: Store API Context erstellen

```bash
# Context-Token holen (aus Response-Header)
curl -i "http://127.0.0.1:8000/store-api/context" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY"

# Automatisch extrahieren:
STORE_CONTEXT_TOKEN=$(curl -si "http://127.0.0.1:8000/store-api/context" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  | tr -d '\r' | awk -F': ' 'tolower($1)=="sw-context-token" {print $2}')

echo "$STORE_CONTEXT_TOKEN"
```

## Schritt 7: Produkt über Store API lesen

```bash
# Volltextsuche
curl -s -X POST "http://127.0.0.1:8000/store-api/search" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"term\": \"Mein Beispielprodukt\",
    \"limit\": 5,
    \"includes\": {\"product\": [\"id\", \"name\", \"translated\", \"calculatedPrice\"]}
  }" | jq

# Nach productNumber filtern
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

## Schritt 8: Produkt in Warenkorb legen

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

# Warenkorb prüfen:
curl -s -X GET "http://127.0.0.1:8000/store-api/checkout/cart" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" | jq
```

## Schritt 9: Checkout vorbereiten

Vor Bestellaufgabe benötigt der Kontext:
- Eingeloggten Kunden
- Aktive Billing- und Shipping-Adressen
- Versandmethode
- Zahlungsmethode

IDs für Registrierung ermitteln:
```bash
# Salutation IDs
curl -s "http://127.0.0.1:8000/store-api/salutation" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" | jq

# Country IDs
curl -s "http://127.0.0.1:8000/store-api/country" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" | jq
```

## Schritt 10: Kunden registrieren und Bestellung aufgeben

### 10.1 Kunden registrieren

```bash
curl -i -X POST "http://127.0.0.1:8000/store-api/account/register" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"salutationId\": \"$SALUTATION_ID\",
    \"firstName\": \"Max\",
    \"lastName\": \"Mustermann\",
    \"email\": \"test@example.com\",
    \"password\": \"shopware123!\",
    \"acceptedDataProtection\": true,
    \"storefrontUrl\": \"http://127.0.0.1:8000\",
    \"billingAddress\": {
      \"firstName\": \"Max\",
      \"lastName\": \"Mustermann\",
      \"street\": \"Musterstr. 1\",
      \"zipcode\": \"12345\",
      \"city\": \"Musterstadt\",
      \"countryId\": \"$COUNTRY_ID\"
    }
  }"
```

**WICHTIG**: Neuen `Sw-Context-Token` aus dem Response-Header speichern!
```bash
STORE_CONTEXT_TOKEN="NEUER_TOKEN_AUS_HEADER"
```

### 10.2 Produkt nach Kontextwechsel erneut hinzufügen

Nach Register/Login kann sich der Context-Token ändern → Warenkorb ist leer → Produkt erneut hinzufügen.

### 10.3 Bestellung aufgeben

```bash
curl -s -X POST "http://127.0.0.1:8000/store-api/checkout/order" \
  -H "sw-access-key: $STORE_API_ACCESS_KEY" \
  -H "sw-context-token: $STORE_CONTEXT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"customerComment": "Testbestellung"}' | jq
```

Fehler `Cart is empty` → Produkt erneut zum Warenkorb hinzufügen.
Fehler `Customer is not logged in` → Login/Registrierung im korrekten Kontext.

### 10.4 Zahlung abwickeln (falls nötig)

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

`"redirectUrl": null` → Zahlungsmethode erfordert keinen Redirect-Flow.

## Troubleshooting

### Schema-Endpoints liefern 500 oder fehlende Tabellen

DB neu initialisieren:
```bash
docker compose exec web bin/console system:install --create-database --basic-setup
```

### Produkt erscheint nicht in Store API

Checkliste:
- `active: true`
- Gültiger `price` gesetzt
- `visibilities` für den Sales Channel vorhanden
- Korrekte Store API Access Key
- Storefront Sales Channel Domain entspricht lokaler URL

### Relevante Request-Header

- Admin API: `Authorization: Bearer $ADMIN_TOKEN`, optional `sw-language-id`, `sw-version-id`, `sw-inheritance`, `sw-currency-id`
- Store API: `sw-access-key`, `sw-context-token`

## Faustregel: Admin API vs. Store API

| Bereich | API |
|---|---|
| Daten anlegen/verwalten | Admin API |
| Als Käufer agieren | Store API |
| Checkout, Warenkorb | Store API |
| Produkte/Kategorien anlegen | Admin API |
| Headless Storefront | Store API |
