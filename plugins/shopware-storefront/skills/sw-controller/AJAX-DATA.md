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
