# Shopware 6 — Override a JS plugin (override)

To completely replace the behavior of a core or third-party JS plugin, register a subclass with `override`
(same plugin name, optionally the same selector).

```js
import CookiePermissionPlugin from 'src/plugin/cookie/cookie-permission.plugin';

export default class FfCookiePermission extends CookiePermissionPlugin {
    _registerEvents() {
        super._registerEvents();
        // additional/divergent behavior
    }
}
// main.js
window.PluginManager.override('CookiePermission', FfCookiePermission, '[data-cookie-permission]');
```

`override` replaces the registered class for that name. For additive extension without replacing → `sw-js-plugin-extend`.
Which plugins/selectors exist: catalog via `sw-js-plugin-catalog` / `/sw-js-plugin-map`.
