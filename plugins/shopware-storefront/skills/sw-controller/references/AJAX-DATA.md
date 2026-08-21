# Shopware 6 — Loading data via JavaScript

In a JS plugin, load data through the built-in `HttpClient` (internal `frontend.*` routes) or `StoreApiClient`
(Store API).

```js
import HttpClient from 'src/service/http-client.service';
const client = new HttpClient();
client.get(this.options.url, (response) => {
    const data = JSON.parse(response);
    // update the DOM
});
```

On the server side, provide a `frontend.*` route that returns `JsonResponse`/`renderStorefront` (`sw-storefront-controller`).
Pass initial data via `data-*` attributes from Twig where possible (saves roundtrips). Mind CSRF and caching
(`sw-storefront-caching`).
