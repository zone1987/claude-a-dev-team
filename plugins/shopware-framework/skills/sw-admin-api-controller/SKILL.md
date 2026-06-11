---
name: sw-admin-api-controller
description: >
  Eigener Admin-API-Endpunkt (Aktion) in Shopware 6: Controller mit _routeScope api, /api/_action/..., Auth via Bearer,
  ACL-Absicherung. Trigger: "Admin API Controller", "api/_action eigener endpoint", "_routeScope api", "custom admin api route",
  "Aktion Admin API", "AbstractController shopware api". Shopware 6.7.
---

# Shopware 6 — Admin-API-Controller

Für Nicht-CRUD-Aktionen im Backend (Importe, Trigger, Custom-Operationen). Route-Scope `api`, Pfad unter `/api/_action/...`.

```php
#[Route(defaults: ['_routeScope' => ['api']])]
class FfActionController extends AbstractController
{
    #[Route(path: '/api/_action/ff/import/{id}', name: 'api.action.ff.import', methods: ['POST'],
            defaults: ['_acl' => ['ff_example:update']])]
    public function import(string $id, Context $context): JsonResponse
    {
        // ...
        return new JsonResponse(['success' => true]);
    }
}
```

Auth = Admin-OAuth (Bearer, `shopware-api` → `sw-admin-api-auth`). Mit `_acl` absichern (`sw-api-acl`). Entity-CRUD
braucht keinen eigenen Controller (generische Admin-API nutzen). Vom Admin-JS via ApiService aufrufen (`shopware-admin`).
