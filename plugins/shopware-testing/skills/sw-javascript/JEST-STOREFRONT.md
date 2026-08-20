# Shopware 6 — Jest (Storefront)

Storefront-JS-Plugins mit Jest testen (`composer storefront:unit`). DOM via jsdom, Plugin instanziieren und Verhalten prüfen.

```js
import FfExamplePlugin from 'src/ff-example/ff-example.plugin';

describe('FfExamplePlugin', () => {
    it('binds click', () => {
        document.body.innerHTML = '<div data-ff-example><button data-ff-trigger></button></div>';
        const el = document.querySelector('[data-ff-example]');
        const plugin = new FfExamplePlugin(el);
        // init() ggf. manuell aufrufen; Events/Optionen prüfen
    });
});
```

`window.PluginManager`/`$emitter` bei Bedarf mocken. AJAX (`HttpClient`) stubben. Für TS-Plugins gilt dasselbe
(`shopware-storefront` → `sw-storefront-typescript`). E2E stattdessen: `sw-playwright-e2e`.
