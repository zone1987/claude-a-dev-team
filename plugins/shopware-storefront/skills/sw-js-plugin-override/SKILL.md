---
name: sw-js-plugin-override
description: >
  Ein bestehendes JS-Storefront-Plugin in Shopware 6 vollständig ersetzen via PluginManager.override (gleicher Name).
  Trigger: "JS Plugin überschreiben", "PluginManager.override", "Storefront Plugin ersetzen", "override CookiePermission",
  "override AddToCart plugin". Shopware 6.7.
---

# Shopware 6 — JS-Plugin überschreiben (override)

Um das Verhalten eines Core-/Fremd-JS-Plugins komplett zu ersetzen, eine Subklasse registrieren mit `override`
(gleicher Plugin-Name, optional gleicher Selector).

```js
import CookiePermissionPlugin from 'src/plugin/cookie/cookie-permission.plugin';

export default class FfCookiePermission extends CookiePermissionPlugin {
    _registerEvents() {
        super._registerEvents();
        // zusätzliches/abweichendes Verhalten
    }
}
// main.js
window.PluginManager.override('CookiePermission', FfCookiePermission, '[data-cookie-permission]');
```

`override` ersetzt die registrierte Klasse für diesen Namen. Für additive Erweiterung ohne Ersetzen → `sw-js-plugin-extend`.
Welche Plugins/Selektoren existieren: Katalog via `sw-js-plugin-catalog` / `/sw-js-plugin-map`.
