# Shopware 6 — Admin API requests

For non-CRUD calls (your own actions) register an `ApiService` or use the `httpClient`.

```js
const { Application } = Shopware;
class FfExampleApiService extends Shopware.Classes.ApiService {
    constructor(httpClient, loginService, apiEndpoint = 'ff-example') { super(httpClient, loginService, apiEndpoint); }
    triggerImport(id) {
        return this.httpClient
            .post(`/_action/ff-example/${id}/import`, {}, { headers: this.getBasicHeaders() })
            .then(r => Shopware.Classes.ApiService.handleResponse(r));
    }
}
Application.addServiceProvider('ffExampleApiService', (container) =>
    new FfExampleApiService(Shopware.Application.getContainer('init').httpClient, container.loginService));
```

On the server side this needs a matching Admin API route `api/_action/...` (`shopware-framework` → `sw-admin-api-controller`).
For plain entity CRUD use the repository (`sw-admin-data-handling`). Custom services in general: `sw-admin-services`.
