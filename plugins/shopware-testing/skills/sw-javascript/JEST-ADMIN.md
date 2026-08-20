# Shopware 6 — Jest (Administration)

Admin JS/Vue tests run with Jest. Execute them via `composer admin:unit` (or `admin:unit:watch`).

```js
import { mount } from '@vue/test-utils';
import 'src/module/ff-example';

describe('ff-example-card', () => {
    it('renders title', async () => {
        const wrapper = mount(await Shopware.Component.build('ff-example-card'), { props: { item: { name: 'X' } } });
        expect(wrapper.text()).toContain('X');
    });
});
```

`fail-on-console` is active (ADR) — no console warnings in tests. Test files are JS-only (ADR "jest test files should be
javascript only"). Component tests via `@vue/test-utils` (`sw-vue-test`). Mock repositories/services.
