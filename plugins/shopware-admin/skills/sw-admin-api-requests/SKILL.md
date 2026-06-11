---
name: sw-admin-api-requests
description: >
  Eigene API-Requests im Shopware-6-Admin: httpClient/ApiService, eigenen ApiService registrieren, gegen eigene
  Admin-API-Route (api/_action) sprechen, Auth-Header. Trigger: "Admin API request", "httpClient admin", "ApiService",
  "api/_action admin", "eigener ApiService", "custom endpoint admin call". Shopware 6.7.
---

# Shopware 6 — Admin-API-Requests

Für Nicht-CRUD-Aufrufe (eigene Aktionen) einen `ApiService` registrieren bzw. den `httpClient` nutzen.

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

Server-seitig dazu eine Admin-API-Route `api/_action/...` (`shopware-framework` → `sw-admin-api-controller`).
Für reine Entity-CRUD das Repository nutzen (`sw-admin-data-handling`). Eigene Services allgemein: `sw-admin-services`.
