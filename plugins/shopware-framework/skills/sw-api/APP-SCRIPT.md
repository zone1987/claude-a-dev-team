# Shopware 6 — App Scripts

Apps können serverseitige Logik als **Twig-Scripts** mitliefern (ohne eigenen App-Server), ausgeführt an definierten
**Hooks** (ADR „app-scripting").

```
MyApp/Resources/scripts/<hook-name>/my-script.twig
```
```twig
{% set page = hook.page %}
{% do hook.someService.doSomething() %}
```

- Hooks decken u.a. Cart-Berechnung (`cart`), Data-Loading (`product-page-loaded`), Custom-Endpoints (`api-<name>`),
  Pricing (ADR „app-script product pricing") ab.
- Verfügbare Services je Hook (data, store, cart, repository) sind gesandboxed.
- Custom Store-API-Endpunkte einer App via Script (`api/...`-Hooks) statt PHP-Route.

Für komplexe Logik mit eigenem Backend → App-Server (`shopware-apps`: `sw-app-php-sdk`/`sw-app-sdk-js`).
Plugin-Pendant für PHP-Routen: `sw-store-api-route`.
