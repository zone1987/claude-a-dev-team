# Shopware 6 — Cookie manager / consent

Add your own cookies to the consent management by decorating `CookieProviderInterface` (`sw-service-decoration`).

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

React to consent on the JS side: `document.$emitter.subscribe('CookieConfiguration_Update', cb)`, or set the cookie only
after consent is given. Only functional cookies may be set without consent.
