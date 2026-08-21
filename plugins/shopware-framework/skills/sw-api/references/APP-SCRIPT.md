# Shopware 6 — App Scripts

Apps can ship server-side logic as **Twig scripts** (without an own app server), executed at defined
**hooks** (ADR "app-scripting").

```
MyApp/Resources/scripts/<hook-name>/my-script.twig
```
```twig
{% set page = hook.page %}
{% do hook.someService.doSomething() %}
```

- Hooks cover, among others, cart calculation (`cart`), data loading (`product-page-loaded`), custom endpoints (`api-<name>`),
  pricing (ADR "app-script product pricing").
- The services available per hook (data, store, cart, repository) are sandboxed.
- Custom Store API endpoints of an app via script (`api/...` hooks) instead of a PHP route.

For complex logic with an own backend → app server (`shopware-apps`: `sw-app-php-sdk`/`sw-app-sdk-js`).
Plugin counterpart for PHP routes: `sw-store-api-route`.
