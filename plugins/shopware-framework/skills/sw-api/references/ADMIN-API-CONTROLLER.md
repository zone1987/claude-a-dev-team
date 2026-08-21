# Shopware 6 — Admin API controller

For non-CRUD actions in the backend (imports, triggers, custom operations). Route scope `api`, path under `/api/_action/...`.

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

Auth = admin OAuth (Bearer, `shopware-api` → `sw-admin-api-auth`). Secure with `_acl` (`sw-api-acl`). Entity CRUD
needs no own controller (use the generic admin API). Call from the admin JS via ApiService (`shopware-admin`).
