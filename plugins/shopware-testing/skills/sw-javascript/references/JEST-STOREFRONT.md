# Shopware 6 — Jest (Storefront)

Test storefront JS plugins with Jest (`composer storefront:unit`). DOM via jsdom, instantiate the plugin and assert its behaviour.

```js
import FfExamplePlugin from 'src/ff-example/ff-example.plugin';

describe('FfExamplePlugin', () => {
    it('binds click', () => {
        document.body.innerHTML = '<div data-ff-example><button data-ff-trigger></button></div>';
        const el = document.querySelector('[data-ff-example]');
        const plugin = new FfExamplePlugin(el);
        // call init() manually if needed; assert events/options
    });
});
```

Mock `window.PluginManager`/`$emitter` where needed. Stub AJAX (`HttpClient`). The same applies to TS plugins
(`shopware-storefront` → `sw-storefront-typescript`). For E2E instead: `sw-playwright-e2e`.
