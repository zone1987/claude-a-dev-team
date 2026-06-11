---
name: sw-ajax-data
description: >
  Daten per JavaScript im Shopware-6-Storefront laden: HttpClient / StoreApiClient, fetch gegen frontend.*-Route
  oder store-api, Daten via data-Attribute ins DOM, JSON-Response aus Controller. Trigger: "AJAX Storefront",
  "HttpClient storefront", "Daten nachladen JS", "fetch frontend route", "StoreApiClient", "JSON controller storefront".
  Shopware 6.7.
---

# Shopware 6 — Daten per JavaScript laden

Im JS-Plugin Daten über den eingebauten `HttpClient` (interne `frontend.*`-Routen) bzw. `StoreApiClient`
(Store-API) nachladen.

```js
import HttpClient from 'src/service/http-client.service';
const client = new HttpClient();
client.get(this.options.url, (response) => {
    const data = JSON.parse(response);
    // DOM aktualisieren
});
```

Server-seitig eine `frontend.*`-Route, die `JsonResponse`/`renderStorefront` liefert (`sw-storefront-controller`).
Initiale Daten möglichst via `data-*`-Attribute aus dem Twig übergeben (spart Roundtrips). CSRF/Caching beachten
(`sw-storefront-caching`).
