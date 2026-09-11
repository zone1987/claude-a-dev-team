# Shopware 6 — Jest (administration)

**The complete setup — `jest.config.js`, `babel.config.js`, the Twig and style
transformers and the global `Shopware` stub with its mixin stand-ins — is in
`sw-testing-standard` → `STANDARD-JEST-ADMIN.md`.** Shopware ships no plugin setup, so
every file is the plugin's own; if it does not exist yet, create it from there.

## The rule

**Everything the plugin adds to the administration is tested, to 100 %**: every component,
function, statement, method, button, page, dropdown, flow and mixin. Enforced by
`coverageThreshold` on all four metrics — the run fails below it, so a gap cannot reach the
branch quietly.

```bash
npm --prefix src/Resources/app/administration run unit
npm --prefix src/Resources/app/administration run unit:coverage
```

Wire it into composer as `test:admin` so one command runs it.

## Specs sit beside the code

`index.js` and `index.spec.js` in the same directory, not in a mirrored tree. **Every
`index.js` has one.**

## A spec

```javascript
import { mount } from '@vue/test-utils';
import DropshippingProductCard from './index';

describe('component/ag-dropshipping-product-card', () => {
    const createWrapper = (props = {}) => mount(DropshippingProductCard, {
        props: { productId: 'a-product', ...props },
        global: {
            stubs: {
                // Real templates, so slots render and a click reaches the handler under
                // test. An empty stub hides exactly what the test is for.
                'mt-card': { template: '<div><slot /></div>' },
                'mt-banner': { template: '<div><slot /></div>' },
                'sw-data-grid': { template: '<div><slot /></div>', props: ['dataSource'] },
            },
        },
    });

    it('says so plainly when no supplier carries the product', async () => {
        const wrapper = createWrapper();
        await flushPromises();

        expect(wrapper.find('.ag-dropshipping-product-card__empty').exists()).toBe(true);
    });

    it('names both suppliers when two carry the same product', async () => {
        // The merchant's question: the same article under two names is still one product.
        …
    });
});
```

**Test names state the rule**, never `it('renders')`. The name is the documentation that
survives a refactoring.

## What makes admin components testable at all

**The Twig transformer.** A component imports its template and assigns it to the `template`
option, which needs Vue's runtime compiler — hence the `vue` mapping to the full build. The
transformer strips the Twig block directives, which exist only so third parties can
override markup and carry no meaning when rendering.

**The mixin stand-ins.** A page declaring `listing` throws on its first `onColumnSort`
binding without one. The stub mirrors `src/app/mixin/listing.mixin.js` closely enough for a
component test, with `disableRouteParams: true` because a component test has no router.

**The notification collector.** Vue binds mixin methods to the instance, which loses a
`jest.fn`'s identity — so calls are collected in an array, exposed as
`global.__shopwareNotifications`, and cleared by a `beforeEach` the stub registers itself:

```javascript
expect(global.__shopwareNotifications).toContainEqual(
    expect.objectContaining({ type: 'error' }),
);
```

## What to assert

Not that it rendered. **What it does:**

- the request it makes, with the criteria it builds
- what it shows when the answer is empty
- what it shows when the answer has several entries
- what a click on each button triggers
- which notification a failure raises
- what a dropdown selection changes

A component test that only checks `wrapper.exists()` reaches 100 % and proves nothing.
