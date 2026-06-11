---
name: sw-jest-admin
description: >
  Jest-Tests für die Shopware-6-Administration: Test-Setup (composer admin:unit), Komponenten/Services testen,
  fail-on-console, JS-only Testfiles. Trigger: "Jest admin shopware", "admin:unit", "Administration test jest",
  "Komponente test admin", "fail on console", "admin unit test". Shopware 6.7.
---

# Shopware 6 — Jest (Administration)

Admin-JS/Vue-Tests laufen mit Jest. Ausführen über `composer admin:unit` (bzw. `admin:unit:watch`).

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

`fail-on-console` ist aktiv (ADR) — keine Konsolen-Warnungen in Tests. Testdateien JS-only (ADR „jest test files should be
javascript only"). Komponenten-Tests via `@vue/test-utils` (`sw-vue-test`). Repositories/Services mocken.
