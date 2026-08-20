# Shopware 6 — Store-API-Endpunkte

Base `/store-api`, Header `sw-access-key` (+ `sw-context-token`, `sw-store-api-auth`). Wichtigste Gruppen:

| Bereich | Endpunkte (Beispiele) |
|---|---|
| Kontext | `GET/PATCH /store-api/context` (Sprache/Währung/Versand/Zahlung wechseln) |
| Katalog | `POST /store-api/product`, `POST /store-api/product/{id}`, `POST /store-api/search`, `POST /store-api/search-suggest` |
| Listing | `POST /store-api/product-listing/{categoryId}` (Filter/Sort wie Criteria, `sw-admin-api-search`) |
| Navigation/Kategorie | `POST /store-api/navigation/{activeId}/{rootId}`, `POST /store-api/category/{id}` |
| Warenkorb | `GET /store-api/checkout/cart`, `POST /store-api/checkout/cart/line-item`, `PATCH .../line-item`, `DELETE .../line-item` |
| Bestellung | `POST /store-api/checkout/order`, `GET /store-api/order`, `POST /store-api/handle-payment` |
| Konto | `POST /store-api/account/login`, `/logout`, `/register`, `GET /store-api/account/customer`, `PATCH /store-api/account/change-*` |
| Methoden | `POST /store-api/payment-method`, `POST /store-api/shipping-method` |

Such-/Listing-Requests nutzen denselben Criteria-Body (filter/sort/associations/aggregations) wie die Admin-Suche.
Commercial/Plugin-Erweiterungen (SwagCommercial, SwagCustomizedProducts, SwagDigitalSalesRooms) ergänzen weitere Routen.

→ **Vollständige Endpunktliste (alle 110 Operationen, 20 Bereiche, Store API 6.7):** [API-ENDPOINTS-DETAIL.md](API-ENDPOINTS-DETAIL.md)
→ Shop-spezifische Endpunkte inkl. installierter Plugins: OpenAPI-Katalog (`sw-api-catalog` / `/sw-api-map`).
→ Eigene Store-API-Routen bauen: `shopware-framework` (`sw-store-api-route`).
