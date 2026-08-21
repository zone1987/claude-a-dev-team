# Shopware 6 — Extend a JS plugin (extend)

`extend` registers a subclass for an existing plugin name and keeps the rest of the behavior —
suitable for adding specific methods.

```js
import AddToCartPlugin from 'src/plugin/add-to-cart/add-to-cart.plugin';

export default class FfAddToCart extends AddToCartPlugin {
    init() {
        super.init();
        this._trackAdd();
    }
    _trackAdd() { /* additional tracking */ }
}
// main.js
window.PluginManager.extend('AddToCart', 'FfAddToCart', FfAddToCart, '[data-add-to-cart]');
```

Difference to `override`: `extend` is meant to be additive/inheriting, `override` replaces completely (`sw-js-plugin-override`).
Call `super.*` to preserve the core logic.
