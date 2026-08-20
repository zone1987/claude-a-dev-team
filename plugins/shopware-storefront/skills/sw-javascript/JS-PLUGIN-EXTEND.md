# Shopware 6 — JS-Plugin erweitern (extend)

`extend` registriert eine Subklasse für einen bestehenden Plugin-Namen und behält den Rest des Verhaltens —
geeignet, um gezielt Methoden zu ergänzen.

```js
import AddToCartPlugin from 'src/plugin/add-to-cart/add-to-cart.plugin';

export default class FfAddToCart extends AddToCartPlugin {
    init() {
        super.init();
        this._trackAdd();
    }
    _trackAdd() { /* zusätzliches Tracking */ }
}
// main.js
window.PluginManager.extend('AddToCart', 'FfAddToCart', FfAddToCart, '[data-add-to-cart]');
```

Unterschied zu `override`: `extend` ist additiv/vererbend gedacht, `override` ersetzt komplett (`sw-js-plugin-override`).
`super.*` aufrufen, um Core-Logik zu erhalten.
