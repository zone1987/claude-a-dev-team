---
name: sw-cookie-manager
description: >
  Cookies & Cookie-Consent im Shopware-6-Storefront: Cookie zur Cookie-Konfiguration hinzufügen via
  CookieProviderInterface (Decorator), auf Consent-Änderungen reagieren. Trigger: "Cookie Consent", "CookieProvider",
  "Cookie hinzufügen storefront", "cookie configuration", "cookie group", "consent changed storefront". Shopware 6.7.
---

# Shopware 6 — Cookie-Manager / Consent

Eigene Cookies in die Consent-Verwaltung aufnehmen, indem der `CookieProviderInterface` dekoriert wird (`sw-service-decoration`).

```php
class FfCookieProvider implements CookieProviderInterface
{
    public function __construct(private readonly CookieProviderInterface $inner) {}
    public function getCookieGroups(): array
    {
        $groups = $this->inner->getCookieGroups();
        $groups[] = ['snippet_name' => 'ff.cookie.group', 'entries' => [
            ['snippet_name' => 'ff.cookie.tracking', 'cookie' => 'ff-tracking', 'value' => '1', 'expiration' => '30'],
        ]];
        return $groups;
    }
}
```

JS-seitig auf Consent reagieren: `document.$emitter.subscribe('CookieConfiguration_Update', cb)` bzw. Cookie erst
nach Zustimmung setzen. Nur funktionale Cookies ohne Consent.
