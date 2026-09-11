# Shopware 6 — Jest (storefront)

**The complete setup — `jest.config.js`, `babel.config.js`, the `plugin.class` double and
the three globals jsdom lacks — is in `sw-testing-standard` →
`STANDARD-JEST-STOREFRONT.md`.** Shopware ships no plugin setup, so every file is the
plugin's own; if it does not exist yet, create it from there.

This file covers writing a spec once that exists.

## The rule

**Everything the plugin's storefront ships is tested, to 100 %**, enforced by
`coverageThreshold` — the run fails below it.

```bash
npm --prefix src/Resources/app/storefront run unit
npm --prefix src/Resources/app/storefront run unit:coverage
```

## A spec

```javascript
import FreeShippingProgressPlugin from './free-shipping-progress.plugin';

describe('plugin/free-shipping-progress', () => {
    let el;

    beforeEach(() => {
        document.body.innerHTML = '<div class="progress-bar"></div>';
        el = document.querySelector('.progress-bar');

        // clearMocks wipes the implementation, not just the calls, so every test that
        // depends on matchMedia sets its return value itself.
        window.matchMedia.mockReturnValue({ matches: true, addEventListener: jest.fn() });
    });

    it('animates the bar to the percentage it was given', () => {
        new FreeShippingProgressPlugin(el, { progress: 40 });

        expect(el.animate).toHaveBeenCalledWith(
            expect.objectContaining({ width: [0, '40%'] }),
            expect.objectContaining({ duration: 500 }),
        );
    });

    it('skips the animation when the visitor asked for reduced motion', () => {
        window.matchMedia.mockReturnValue({ matches: false, addEventListener: jest.fn() });

        new FreeShippingProgressPlugin(el, { progress: 40 });

        expect(el.animate).toHaveBeenCalledWith(
            expect.anything(),
            expect.objectContaining({ duration: 0 }),
        );
    });
});
```

**Test names state the rule**, not the mechanism: `'skips the animation when the visitor
asked for reduced motion'`, never `'binds click'`.

**The constructor calls `init()`**, so instantiating the plugin is the act under test.
There is no separate `init()` call.

## Three things jsdom does not give you

`window.PluginManager`, `Element.prototype.animate` and `window.matchMedia` are all absent,
and **the core has no precedent for stubbing the last two** — verified by grep over the
storefront's own test directory. The stubs live in `test/_setup/storefront.js`.

Without `PluginManager`, `new MyPlugin(el)` throws inside the base class constructor before
a single assertion runs.

## The trap that costs the most time

`moduleNameMapper` is evaluated **in order**. The specific `plugin.class` entry must come
before the generic `^src/(.*)$`, or the generic one swallows it and Jest looks for the base
class inside the plugin:

```javascript
moduleNameMapper: {
    '^src/plugin-system/plugin\\.class$': '<rootDir>/test/_mock/plugin.class.js',
    '^src/(.*)$': '<rootDir>/src/$1',
},
```

## Dead code is deleted, not covered

Reaching 100 % surfaces branches that cannot be true. Delete them. A test written only to
reach a line is what the mutation rules forbid — and a branch that can never be taken is a
defect, not a coverage problem.

## The build has to work first

Shopware 6.7 builds storefront plugins with **Webpack**, not Vite, and Webpack refuses an
extension-less relative import:

```javascript
import('./plugin/my.plugin.js')   // works
import('./plugin/my.plugin')      // "Can't resolve"
```

Verify before trusting any storefront test:

```bash
ddev exec bash -c "cd /var/www/html/shopware && shopware-cli project storefront-build --only-extensions YourPlugin"
```

A plugin whose build fails ships whatever stale files happen to sit in `dist/`.
