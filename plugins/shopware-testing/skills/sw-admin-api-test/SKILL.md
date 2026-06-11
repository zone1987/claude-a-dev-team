---
name: sw-admin-api-test
description: >
  Admin-API-Tests in Shopware 6: AdminApiTestBehaviour, getBrowser (authentifizierter Admin-Client), Requests gegen
  /api, ACL-Fälle. Trigger: "Admin API Test", "AdminApiTestBehaviour", "getBrowser admin test", "api/_action test",
  "authenticated api test shopware". Shopware 6.7.
---

# Shopware 6 — Admin-API-Test

Testet Admin-API-Endpunkte mit authentifiziertem Client (`AdminApiTestBehaviour`/`getBrowser`).

```php
use IntegrationTestBehaviour, AdminApiTestBehaviour;

public function testAction(): void
{
    $this->getBrowser()->request('POST', '/api/_action/ff/import/' . $id);
    static::assertSame(200, $this->getBrowser()->getResponse()->getStatusCode());
}
```

Der Browser hält ein gültiges Bearer-Token. ACL-/Berechtigungsfälle gezielt testen (eigener Integration-User mit
eingeschränkten Rechten). Eigene Endpunkte/ACL: `shopware-framework` (`sw-admin-api-controller`/`sw-api-acl`).
